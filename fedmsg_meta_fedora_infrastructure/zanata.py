# This file is part of fedmsg.
# Copyright (C) 2012-2015 Red Hat, Inc.
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


class ZanataProcessor(BaseProcessor):
    __name__ = "Zanata"
    __description__ = "translation events"
    __link__ = "https://fedora.zanata.org"
    __docs__ = "http://zanata.org/help/workflow-overview/"
    __obj__ = "Translation Events"
    __icon__ = "https://pbs.twimg.com/profile_images/" + \
        "378800000417679469/47eb45c6205aa9f2cdb8705e6d46745c_normal.png"

    def subtitle(self, msg, **config):
        tmpl = self._(
            "{docId} from the {project} project "
            "is now {milestone} in the '{locale}' locale"
        )
        return tmpl.format(**msg['msg']).lower()

    def secondary_icon(self, msg, **config):
        return self.__icon__

    def _object(self, msg):
        return "/".join([
            msg['msg']['project'],
            msg['msg']['version'],
            'languages',
            msg['msg']['locale'],
        ])

    def objects(self, msg, **config):
        return set([self._object(msg)])

    def link(self, msg, **config):
        return "https://fedora.zanata.org/iteration/view/" + self._object(msg)
