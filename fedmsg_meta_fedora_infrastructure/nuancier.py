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


class NuancierProcessor(BaseProcessor):
    __name__ = "nuancier"
    __description__ = "the supplemental wallpaper voting system"
    __link__ = "https://apps.fedoraproject.org/nuancier/"
    __docs__ = "https://github.com/fedora-infra/nuancier-lite"
    __obj__ = "Wallpaper Elections"

    def link(self, msg, **config):
        kind = msg['topic'].split('.')[4]
        item = msg['msg']['election']['id']
        lookup = {
            'publish': 'results',
            'open': 'election',
        }
        kind = lookup[kind]
        return "https://apps.fedoraproject.org/nuancier/%s/%s" % (kind, item)

    def subtitle(self, msg, **config):
        agent = msg['msg']['agent']
        name = msg['msg']['election']['name']
        if 'publish.toggle.on' in msg['topic']:
            tmpl = self._(
                '{agent} published the results of the "{name}" election')
        elif 'publish.toggle.off' in msg['topic']:
            tmpl = self._(
                '{agent} rescinded the results of the "{name}" election')
        elif 'open.toggle.on' in msg['topic']:
            tmpl = self._(
                '{agent} opened the "{name}" election for voting')
        elif 'open.toggle.off' in msg['topic']:
            tmpl = self._(
                '{agent} closed the "{name}" election for voting')
        else:
            tmpl = ''

        return tmpl.format(agent=agent, name=name)

    def secondary_icon(self, msg, **config):
        return gravatar_url(msg['msg']['agent'])

    def usernames(self, msg, **config):
        return set([msg['msg']['agent']])

    def objects(self, msg, **config):
        kind = msg['topic'].split('.')[4]
        action = msg['topic'].split('.')[-1]
        year = msg['msg']['election']['year']
        name = msg['msg']['election']['name']
        return set(['/'.join(map(str, [year, name, kind, action]))])
