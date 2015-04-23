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


class NuancierProcessor(BaseProcessor):
    __name__ = "nuancier"
    __description__ = "the supplemental wallpaper voting system"
    __link__ = "https://apps.fedoraproject.org/nuancier/"
    __icon__ = "https://apps.fedoraproject.org/img/icons/nuancier.png"
    __docs__ = "https://github.com/fedora-infra/nuancier-lite"
    __obj__ = "Wallpaper Elections"

    def link(self, msg, **config):

        if 'original_url' in msg['msg'].get('candidate', {}):
            return msg['msg']['candidate']['original_url']

        kind = msg['topic'].split('.')[4]
        item = msg['msg']['election']['id']
        return "https://apps.fedoraproject.org/nuancier/%s/%s" % (kind, item)

    def subtitle(self, msg, **config):
        kwargs = dict(
            agent=msg['msg']['agent'],
            name=msg['msg']['election']['name'],
        )
        if 'election.update' in msg['topic']:
            tmpl = self._(
                '{agent} changed the following details '
                'on the "{name}" election: {details}')
            kwargs['details'] = ', '.join(msg['msg']['updated'])
        elif 'election.new' in msg['topic']:
            tmpl = self._(
                '{agent} created a new election "{name}"')
        elif 'candidate.new' in msg['topic']:
            tmpl = self._(
                '{agent} uploaded a new candidate for the '
                '"{name}" wallpaper election')
        elif 'candidate.denied' in msg['topic']:
            tmpl = self._(
                '{agent} denied {author}\'s "{candidate}" submission to the '
                '"{name}" wallpaper election')
            kwargs['author'] = msg['msg']['candidate']['submitter']
            kwargs['candidate'] = msg['msg']['candidate']['name']
        elif 'candidate.approved' in msg['topic']:
            tmpl = self._(
                '{agent} approved {author}\'s "{candidate}" submission to the '
                '"{name}" wallpaper election')
            kwargs['author'] = msg['msg']['candidate']['submitter']
            kwargs['candidate'] = msg['msg']['candidate']['name']
        else:
            tmpl = ''

        return tmpl.format(**kwargs)

    def secondary_icon(self, msg, **config):
        return avatar_url(msg['msg']['agent'])

    def usernames(self, msg, **config):
        users = [msg['msg']['agent']]

        if 'candidate' in msg['msg']:
            users.append(msg['msg']['candidate']['submitter'])

        return set(users)

    def objects(self, msg, **config):
        kind = msg['topic'].split('.')[-2]
        action = msg['topic'].split('.')[-1]
        year = msg['msg']['election']['year']
        name = msg['msg']['election']['name']
        candidate = msg['msg'].get('candidate', {}).get('name')
        tokens = [year, name, kind, action]
        if candidate:
            tokens.insert(2, candidate)
        return set(['/'.join(map(str, tokens))])
