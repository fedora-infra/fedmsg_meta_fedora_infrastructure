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

from fedmsg_meta_fedora_infrastructure import BaseProcessor
from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url


class WaiverDBProcessor(BaseProcessor):
    __name__ = "waiverdb"
    __description__ = "WaiverDB"
    __link__ = "https://pagure.io/waiverdb"
    __docs__ = ("https://fedoraproject.org/wiki/Infrastructure/"
                "Factory2/Focus/WaiverDB")
    __obj__ = "New result waivers"
    __icon__ = "https://apps.fedoraproject.org/img/icons/waiverdb.png"

    def subtitle(self, msg, **config):
        tmpl = self._('{username} waived result {result_id} '
                      '({product_version}): "{comment}"')
        return tmpl.format(**msg['msg'])

    def link(self, msg, **config):
        template = ('https://waiverdb-web-waiverdb.app.os.fedoraproject.org/'
                    'api/v1.0/waivers/{id}')
        return template.format(**msg['msg'])

    def agent(self, msg, **config):
        return msg['msg']['username']

    def usernames(self, msg, **config):
        return set([self.agent(msg, **config)])

    def secondary_icon(self, msg, **config):
        return avatar_url(username=self.agent(msg, **config))
