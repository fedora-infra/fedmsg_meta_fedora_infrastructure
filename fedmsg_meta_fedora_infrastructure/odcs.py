# This file is part of fedmsg.
# Copyright (C) 2020 Red Hat, Inc.
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
# Authors:  Jan Kaluza <jkaluza@redhat.com>
#

from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url
from fedmsg_meta_fedora_infrastructure import BaseProcessor

class ODCSProcessor(BaseProcessor):
    __name__ = "odcs"
    __description__ = "On Demand Compose Service"
    __link__ = "https://odcs.engineering.redhat.com/api/1/composes/"
    __docs__ = "https://docs.pagure.org/odcs/"
    __obj__ = "ODCS Composes"
    __icon__ = "https://apps.fedoraproject.org/img/icons/odcs.png"

    def link(self, msg, **config):
        tmpl = "https://odcs.fedoraproject.org/api/1/composes/{id}"
        return tmpl.format(**msg['msg']['compose'])

    def subtitle(self, msg, **config):
        c = msg['msg']['compose']
        tmpl = self._(
            "{owner}'s compose {compose_id} entered the {state_name} state."
        )
        return tmpl.format(
            owner=c['owner'],
            compose_id=c['pungi_compose_id'] or c['id'],
            state_name=c['state_name']
        )

    def secondary_icon(self, msg, **config):
        user = msg['msg']['compose']['owner']
        return avatar_url(user)

    def usernames(self, msg, **config):
        user = msg['msg']['compose']['owner']
        return set([user])

    def objects(self, msg, **config):
        return set([msg['msg']['compose']['id']])
