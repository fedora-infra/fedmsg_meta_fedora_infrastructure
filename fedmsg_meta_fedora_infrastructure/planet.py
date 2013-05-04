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


class PlanetProcessor(BaseProcessor):
    __name__ = "fedoraplanet"
    __description__ = "the Fedora blog aggregator"
    __link__ = "http://planet.fedoraproject.org/"
    __docs__ = "https://fedoraproject.org/wiki/Planet"
    __obj__ = "Blog Posts"

    def handle_msg(self, msg, **config):
        return 'planet.post.new' in msg['topic']

    def link(self, msg, **config):
        return msg['msg']['post']['link']

    def subtitle(self, msg, **config):
        title = msg['msg']['post']['title']
        if 'username' in msg['msg']:
            tmpl = self._('{user} posted "{title}"')
            return tmpl.format(title=title, user=msg['msg']['username'])

        tmpl = self._('New post: "{title}"')
        return tmpl.format(title=title)

    def secondary_icon(self, msg, **config):
        return msg['msg'].get('face', None)

    def usernames(self, msg, **config):
        if 'username' in msg['msg']:
            return set([msg['msg']['username']])

        return set()

    def objects(self, msg, **config):
        link = self.link(msg, **config)
        link = link.replace('https://', '').replace('http://', '')
        return set([link])
