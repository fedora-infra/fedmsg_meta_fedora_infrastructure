# This file is part of fedmsg.
# Copyright (C) 2015 Red Hat, Inc.
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


class RelengProcessor(BaseProcessor):
    __name__ = "releng"
    __description__ = "Fedora Release Engineering"
    __link__ = "https://git.fedorahosted.org/cgit/releng"
    __docs__ = "https://fedoraproject.org/wiki/ReleaseEngineering"
    __obj__ = "Releng Events"
    __icon__ = "https://apps.fedoraproject.org/img/icons/atomic.png"

    def subtitle(self, msg, **config):
        if 'x86_64' in msg['msg'].keys():
            release = msg['msg']['x86_64']['atomic_raw'].get('release', '')
        else:
            release = msg['msg']['atomic_raw'].get('release', '')
        if msg['topic'].endswith('.releng.atomic.twoweek.begin'):
            tmpl = self._("Release engineering scripts started evaluating a "
                          "new set of builds for a Fedora {release} Atomic "
                          "Host release")
            return tmpl.format(release=release)
        elif msg['topic'].endswith('.releng.atomic.twoweek.complete'):
            tmpl = self._("A new release of Fedora {release} Atomic "
                          "Host is ready")
            return tmpl.format(release=release)
        else:
            return None

    def link(self, msg, **config):
        return "https://download.fedoraproject.org/pub/alt/atomic/stable/"

    def secondary_icon(self, msg, **config):
        return self.__icon__

    def objects(self, msg, **config):
        if 'x86_64' in msg['msg'].keys():
            return set(msg['msg'].keys())
        else:
            return set([
                "%s/%s" % (msg['msg'][key]['release'], key)
                for key in msg['msg'] if key.startswith('atomic_')
            ])
