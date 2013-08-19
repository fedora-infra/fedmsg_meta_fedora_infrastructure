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

from fasshim import gravatar_url
from fedmsg_meta_fedora_infrastructure import BaseProcessor


class BadgesProcessor(BaseProcessor):
    __name__ = "fedbadges"
    __description__ = "the Fedora Open Badges System"
    __link__ = "https://badges.fedoraproject.org/"
    __docs__ = "https://fedoraproject.org/wiki/Open_Badges"
    __obj__ = "New Badges"

    def link(self, msg, **config):
        username = msg['msg']['user']['username']
        return "https://badges.fedoraproject.org/user/%s" % username

    def subtitle(self, msg, **config):
        user = msg['msg']['user']['username']
        name = msg['msg']['badge']['name']
        tmpl = self._('{user} has been awarded the "{name}" badge')
        return tmpl.format(user=user, name=name)

    def icon(self, msg, **config):
        return msg['msg']['badge']['image_url']

    def secondary_icon(self, msg, **config):
        return gravatar_url(msg['msg']['user']['username'])

    def usernames(self, msg, **config):
        return set([msg['msg']['user']['username']])

    def objects(self, msg, **config):
        return set([msg['msg']['badge']['name'].lower().replace(' ', '-')])
