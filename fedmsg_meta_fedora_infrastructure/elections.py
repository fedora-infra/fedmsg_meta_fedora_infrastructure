# This file is part of fedmsg.
# Copyright (C) 2014 Red Hat, Inc.
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
# Authors:  Pierre-Yves Chibon <pingou@pingoured.fr>
#           Ralph Bean <rbean@redhat.com>

from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url
from fedmsg_meta_fedora_infrastructure import BaseProcessor


class ElectionsProcessor(BaseProcessor):
    __name__ = "fedora_elections"
    __description__ = "the fedora voting system"
    __link__ = "https://admin.fedoraproject.org/voting/"
    __docs__ = "https://github.com/fedora-infra/elections"
    __obj__ = "Fedora Elections"

    def link(self, msg, **config):
        msg = msg['msg']
        if 'election' in msg:
            msg = msg['election']
        name = msg['alias']
        return "https://admin.fedoraproject.org/voting/about/%s" % (name)

    def subtitle(self, msg, **config):
        if 'election' in msg['msg']:
            name = msg['msg']['election']['alias']  # Old style
        else:
            name = msg['msg']['alias']  # New style

        if 'agent' in msg['msg']:
            agent = msg['msg']['agent']  # Old style
        else:
            agent = msg['msg']['fas_user']  # New style

        kwargs = dict(name=name, agent=agent)

        if 'election.new' in msg['topic']:
            tmpl = self._(
                '{agent} created election "{name}"')
        elif 'election.edit' in msg['topic']:
            tmpl = self._(
                '{agent} edited election "{name}"')
        elif 'candidate.new' in msg['topic']:
            tmpl = self._(
                '{agent} added candidate "{cand_name}" to '
                'election "{name}"')
            kwargs['cand_name'] = msg['msg']['candidate']['name']
        elif 'candidate.edit' in msg['topic']:
            tmpl = self._(
                '{agent} edited candidate "{cand_name}" of '
                'election "{name}"')
            kwargs['cand_name'] = msg['msg']['candidate']['name']
        elif 'candidate.delete' in msg['topic']:
            tmpl = self._(
                '{agent} deleted candidate "{cand_name}" of '
                'election "{name}"')
            kwargs['cand_name'] = msg['msg']['candidate']['name']
        else:
            tmpl = ''

        return tmpl.format(**kwargs)

    def secondary_icon(self, msg, **config):
        if 'agent' in msg['msg']:
            agent = msg['msg']['agent']  # Old style
        else:
            agent = msg['msg']['fas_user']  # New style
        return avatar_url(agent)

    def usernames(self, msg, **config):
        try:
            if 'agent' in msg['msg']:
                agent = msg['msg']['agent']  # Old style
            else:
                agent = msg['msg']['fas_user']  # New style
            return set([agent])
        except KeyError:
            return set()

    def objects(self, msg, **config):
        kind = msg['topic'].split('.')[-2]
        action = msg['topic'].split('.')[-1]

        if 'election' in msg['msg']:
            name = msg['msg']['election']['alias']  # Old style
        else:
            name = msg['msg']['alias']  # New style

        tokens = [name, kind, action]
        return set(['/'.join(map(str, tokens))])
