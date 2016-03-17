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
    __name__ = "planet"
    __description__ = "the Fedora blog aggregator"
    __link__ = "http://planet.fedoraproject.org/"
    __docs__ = "https://fedoraproject.org/wiki/Planet"
    __icon__ = "https://apps.fedoraproject.org/img/icons/planet_logo.png"
    __obj__ = "Blog Posts"

    def link(self, msg, **config):
        return msg['msg']['post']['link']

    def subtitle(self, msg, **config):
        title = msg['msg']['post'].get('title', '(no title found)')
        if 'username' in msg['msg']:
            tmpl = self._('{user} posted "{title}"')
            return tmpl.format(title=title, user=msg['msg']['username'])

        tmpl = self._('New post: "{title}"')
        return tmpl.format(title=title)

    def long_form(self, msg, **config):
        if 'summary' in msg['msg']['post']:
            return msg['msg']['post']['summary']
        elif 'content' in msg['msg']['post']:
            if msg['msg']['post']['content']:
                return msg['msg']['post']['content'][0]['value']

    def lexer(self, msg, **config):
        # Be explicit about returning None here.  We don't want to lex the html
        # from their summary.. but we want to return it literally.  So, don't
        # implement a lexer here, please.  --ralph
        return None

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
