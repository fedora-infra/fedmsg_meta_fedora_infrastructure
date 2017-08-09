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
from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url


class AskbotProcessor(BaseProcessor):
    __name__ = "Askbot"
    __description__ = "the Fedora 'Ask' Forum"
    __link__ = "https://ask.fedoraproject.org"
    __docs__ = "https://askbot.com"
    __icon__ = "https://apps.fedoraproject.org/img/icons/ask_fedora.png"
    __obj__ = "Ask Fedora Qs & As"

    # No icon that I can find..
    #__icon__ = "https://apps.fedoraproject.org/packages/" + \
    #    "images/icons/package_128x128.png"

    def subtitle(self, msg, **config):
        user = msg['msg']['agent']
        title = ""
        if 'askbot.post.edit' in msg['topic']:
            title = msg['msg']['thread']['title']
            if msg['msg']['created']:
                if msg['msg']['post']['post_type'] == 'question':
                    tmpl = self._("{user} asked the question '{title}'")
                else:
                    tmpl = self._(
                        "{user} suggested an answer to the question '{title}'")
            else:
                if msg['msg']['post']['post_type'] == 'question':
                    tmpl = self._("{user} updated the question '{title}'")
                else:
                    tmpl = self._(
                        "{user} updated an answer to the question '{title}'")
        elif 'askbot.tag.update' in msg['topic']:
            title = msg['msg']['thread']['title']
            tmpl = self._("{user} altered tags on askbot question '{title}'")
        elif 'askbot.post.flag_offensive.add' in msg['topic']:
            title = msg['msg']['thread']['title']
            if msg['msg']['instance']['post_type'] == 'question':
                tmpl = self._("{user} flagged a question as offensive!")
            else:
                tmpl = self._("{user} flagged an answer as offensive!")
        elif 'askbot.post.flag_offensive.delete' in msg['topic']:
            if msg['msg']['instance']['post_type'] == 'question':
                tmpl = self._("{user} unflagged a question as offensive...")
            else:
                tmpl = self._("{user} unflagged an answer as offensive...")
        elif 'askbot.post.delete' in msg['topic']:
            title = msg['msg']['thread']['title']
            if msg['msg']['instance']['post_type'] == 'question':
                tmpl = self._("{user} deleted the question '{title}'")
            else:
                tmpl = self._("{user} deleted an answer on '{title}'")
        else:
            raise NotImplementedError("%r" % msg)

        return tmpl.format(user=user, title=title)

    def secondary_icon(self, msg, **config):
        user = None

        try:
            user = msg['msg']['agent']
        except KeyError:
            pass

        if not user:
            return ""

        return avatar_url(username=user)

    def usernames(self, msg, **config):
        users = set()

        try:
            users.add(msg['msg']['agent'])
        except KeyError:
            pass

        for user in msg['msg'].get('newly_mentioned_users', []):
            users.add(user)

        return users

    def objects(self, msg, **config):
        objs = set()

        if 'tags' in msg['msg']:
            for tag in msg['msg']['tags']:
                if not tag:
                    continue
                objs.add('tags/{tag}'.format(tag=tag))
        elif 'thread' in msg['msg']:
            for tag in msg['msg']['thread']['tagnames']:
                if not tag:
                    continue
                objs.add('tags/{tag}'.format(tag=tag))

        if 'thread' in msg['msg']:
            objs.add('threads/{pk}'.format(
                pk=msg['msg']['thread']['pk']))

        return objs

    def link(self, msg, **config):
        if 'stg' in msg['topic']:
            tmpl = "https://ask.stg.fedoraproject.org/question/{pk}/"
        else:
            tmpl = "https://ask.fedoraproject.org/question/{pk}/"

        pk = msg['msg']['topmost_post_id']
        post = ""

        if 'post' in msg['msg']:
            post = msg['msg']['post']['pk']
            #tmpl += "?answer={post}#post-id-{post}"
        elif 'instance' in msg['msg']:
            post = msg['msg']['instance']['pk']
            #tmpl += "?answer={post}#post-id-{post}"
        else:
            pass

        return tmpl.format(pk=pk, post=post)
