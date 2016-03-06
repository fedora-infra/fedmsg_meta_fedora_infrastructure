# This file is part of fedmsg.
# Copyright (C) 2012 Red Hat, Inc.
#
# fedmsg is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# fedmsg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with fedmsg; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Authors:  Ralph Bean <rbean@redhat.com>
#

import re

import requests

from fedmsg_meta_fedora_infrastructure import BaseProcessor
from fedmsg_meta_fedora_infrastructure.fasshim import nick2fas, avatar_url

from fedmsg_meta_fedora_infrastructure.conglomerators.meetbot import \
        meetbot as meetbot_conglomerator

blacklisted_people = [
    'zodbot',
]

link_regex = re.compile('(https?:\/\/[a-z0-9\.:].*?)[ $]')

class SupybotProcessor(BaseProcessor):
    __name__ = "meetbot"
    __description__ = "the Fedora IRC bot"
    __link__ = "https://meetbot.fedoraproject.org/"
    __docs__ = "https://fedoraproject.org/wiki/Zodbot"
    __obj__ = "IRC Meetings"
    __icon__ = "https://apps.fedoraproject.org/img/icons/meetbot.png"

    conglomerators = [
        meetbot_conglomerator.ByURL,
    ]

    def link(self, msg, **config):
        if 'meetbot.meeting.complete' in msg['topic']:
            return msg['msg']['url'].replace('http://', 'https://') + ".html"
        elif 'meetbot.meeting.item.link' in msg['topic']:
            line = msg['msg']['details']['line']
            results = link_regex.findall(line)
            if not results:
                return None
            return results[0]
        else:
            return None

    def long_form(self, msg, **config):
        if '.meeting.complete' in msg['topic']:
            url = msg['msg']['url'] + '.txt'
            response = requests.get(url)
            if response.status_code == 200:
                return response.text

    def subtitle(self, msg, **config):
        action = None
        agent = None
        line = None

        if 'meetbot.meeting.start' in msg['topic']:
            if msg['msg']['meeting_topic']:
                tmpl = self._('{owner} started meeting "{name}" in {channel}')
            else:
                tmpl = self._('{owner} started a meeting in {channel}')

        elif 'meetbot.meeting.complete' in msg['topic']:
            if msg['msg']['meeting_topic']:
                tmpl = self._('{owner}\'s meeting titled "{name}" '
                              'ended in {channel}')
            else:
                tmpl = self._('{owner}\'s meeting ended in {channel}')

        elif 'meetbot.meeting.topic.update' in msg['topic']:
            if msg['msg']['meeting_topic']:
                tmpl = self._('The topic of {owner}\'s "{name}" meeting '
                              'changed to "{topic}" in {channel}')
            else:
                tmpl = self._('The topic of {owner}\'s meeting '
                              'changed to "{topic}" in {channel}')
        elif 'meetbot.meeting.item.' in msg['topic']:
            if msg['msg']['meeting_topic']:
                tmpl = self._('{agent} {action} in the "{name}" meeting '
                              'in {channel}: "{line}"')
            else:
                tmpl = self._('{agent} {action} in a meeting '
                              'in {channel}: "{line}"')
            key = msg['topic'].rsplit('.')[-1]
            action_lookup = {
                'agreed': 'noted agreement',
                'accepted': 'accepted an item',
                'rejected': 'rejected an item',
                'action': 'noted an action',
                'info': 'raised a point of information',
                'idea': 'proposed an idea',
                'help': 'called for help',
                'link': 'linked to more information',
            }
            action = action_lookup[key]
            line = msg['msg']['details']['line']
        else:
            raise NotImplementedError("%r" % msg)

        if 'details' in msg['msg']:
            agent = nick2fas(msg['msg']['details']['nick'], **config)

        owner = nick2fas(msg['msg']['owner'], **config)
        name = msg['msg']['meeting_topic']
        channel = msg['msg']['channel']
        topic = msg['msg'].get('topic', 'no topic')

        return tmpl.format(owner=owner, agent=agent, name=name,
                           channel=channel, topic=topic,
                           action=action, line=line)

    def usernames(self, msg, **config):
        return set([
            nick2fas(nick, **config)
            for nick in msg['msg']['attendees']
            if nick not in blacklisted_people
        ])

    def secondary_icon(self, msg, **config):
        if 'details' in msg['msg']:
            user = nick2fas(msg['msg']['details']['nick'], **config)
        else:
            user = nick2fas(msg['msg']['owner'], **config)
        return avatar_url(user)

    def objects(self, msg, **config):
        objs = set([
            'attendees/' + nick2fas(person, **config)
            for person in msg['msg']['attendees']
            if person not in blacklisted_people
        ] + [
            'channels/' + msg['msg']['channel']
        ])

        if msg['msg']['meeting_topic']:
            objs.add('titles/' + msg['msg']['meeting_topic'])

        if msg['msg'].get('topic', None):
            objs.add('topics/' + msg['msg']['topic'])

        return objs
