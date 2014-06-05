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
from fedmsg_meta_fedora_infrastructure import BaseProcessor
from fedmsg_meta_fedora_infrastructure.fasshim import nick2fas, gravatar_url

blacklisted_people = [
    'zodbot',
]


class SupybotProcessor(BaseProcessor):
    __name__ = "meetbot"
    __description__ = "the Fedora IRC bot"
    __link__ = "https://meetbot.fedoraproject.org/"
    __docs__ = "https://fedoraproject.org/wiki/Zodbot"
    __obj__ = "IRC Meetings"
    __icon__ = "https://apps.fedoraproject.org/img/icons/meetbot.png"

    def link(self, msg, **config):
        if 'meetbot.meeting.complete' in msg['topic']:
            return msg['msg']['url'].replace('http://', 'https://') + ".html"
        else:
            return None

    def subtitle(self, msg, **config):
        if 'meetbot.meeting.start' in msg['topic']:
            if msg['msg']['meeting_topic']:
                tmpl = self._('{user} started meeting "{name}" in {channel}')
            else:
                tmpl = self._('{user} started a meeting in {channel}')

        elif 'meetbot.meeting.complete' in msg['topic']:
            if msg['msg']['meeting_topic']:
                tmpl = self._('{user}\'s meeting titled "{name}" '
                              'ended in {channel}')
            else:
                tmpl = self._('{user}\'s meeting ended in {channel}')

        elif 'meetbot.meeting.topic.update' in msg['topic']:
            if msg['msg']['meeting_topic']:
                tmpl = self._('The topic of {user}\'s "{name}" meeting '
                              'changed to "{topic}" in {channel}')
            else:
                tmpl = self._('The topic of {user}\'s meeting '
                              'changed to "{topic}" in {channel}')
        else:
            raise NotImplementedError("%r" % msg)

        user = nick2fas(msg['msg']['owner'], **config)
        name = msg['msg']['meeting_topic']
        channel = msg['msg']['channel']
        topic = msg['msg'].get('topic', 'no topic')

        return tmpl.format(user=user, name=name, channel=channel, topic=topic)

    def usernames(self, msg, **config):
        return set([
            nick2fas(nick, **config)
            for nick in msg['msg']['attendees']
            if nick not in blacklisted_people
        ])

    def secondary_icon(self, msg, **config):
        user = nick2fas(msg['msg']['owner'], **config)
        return gravatar_url(user)

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
