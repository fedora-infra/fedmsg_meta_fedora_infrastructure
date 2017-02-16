# This file is part of fedmsg.
# Copyright (C) 2017 Red Hat, Inc.
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

from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url
from fedmsg_meta_fedora_infrastructure import BaseProcessor

class MBSProcessor(BaseProcessor):
    __name__ = "mbs"
    __description__ = "Module Build Service"
    __link__ = "https://mbs.fedoraproject.org"
    __docs__ = "https://fedoraproject.org/wiki/Changes/ModuleBuildService"
    __obj__ = "Module Builds"
    __icon__ = "https://apps.fedoraproject.org/img/icons/modularity.png"

    def link(self, msg, **config):
        tmpl = "https://mbs.fedoraproject.org/module-build-service/1/module-builds/{id}"
        return tmpl.format(**msg['msg'])

    def subtitle(self, msg, **config):
        tmpl = self._(
            "{owner}'s build of modules/{name} entered the {state_name} state."
        )
        return tmpl.format(**msg['msg'])

    def secondary_icon(self, msg, **config):
        user = msg['msg']['owner']
        return avatar_url(user)

    def usernames(self, msg, **config):
        user = msg['msg']['owner']
        return set([user])

    def objects(self, msg, **config):
        return set([msg['msg']['name']])

    def packages(self, msg, **config):
        return set([]) # Not sure what to do with this yet...
