# This file is part of fedmsg.
# Copyright (C) 2012, 2013 Red Hat, Inc.
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
#           Luke Macken <lmacken@redhat.com>

from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url
from fedmsg_meta_fedora_infrastructure import BaseProcessor


class BadgesProcessor(BaseProcessor):
    __name__ = "fedbadges"
    __description__ = "the Fedora Open Badges System"
    __link__ = "https://badges.fedoraproject.org/"
    __icon__ = "https://apps.fedoraproject.org/img/icons/badges.png"
    __docs__ = "https://fedoraproject.org/wiki/Open_Badges"
    __obj__ = "New Badges"

    def _get_user(self, msg):
        # Handle the difference between badge.award and person.rank.advance.
        if 'user' in msg['msg']:
            return msg['msg']['user']['username']
        else:
            return msg['msg']['person']['nickname']

    def link(self, msg, **config):
        username = self._get_user(msg)
        return "https://badges.fedoraproject.org/user/%s" % username

    def long_form(self, msg, **config):
        if 'badge.award' in msg['topic']:
            return msg['msg']['badge']['description']

    def subtitle(self, msg, **config):
        user = self._get_user(msg)
        if 'badge.award' in msg['topic']:
            name = msg['msg']['badge']['name']
            tmpl = self._('{user} has been awarded the "{name}" badge')
            return tmpl.format(user=user, name=name)
        elif 'person.rank.advance' in msg['topic']:
            rank = msg['msg']['person']['rank']
            tmpl = self._('{user} moved to position {rank} '
                          'on the badges leaderboard')
            return tmpl.format(user=user, rank=rank)
        elif 'person.login.first' in msg['topic']:
            tmpl = self._('{user} logged in to badges.fedoraproject.org '
                          'for the first time')
            return tmpl.format(user=user)
        else:
            pass

    def icon(self, msg, **config):
        if 'badge.award' in msg['topic']:
            return msg['msg']['badge']['image_url']
        else:
            return super(BadgesProcessor, self).icon(msg, **config)

    def secondary_icon(self, msg, **config):
        return avatar_url(self._get_user(msg))

    def usernames(self, msg, **config):
        return set([self._get_user(msg)])

    def objects(self, msg, **config):
        if 'badge.award' in msg['topic']:
            return set([msg['msg']['badge']['name'].lower().replace(' ', '-')])
        else:
            return set([])
