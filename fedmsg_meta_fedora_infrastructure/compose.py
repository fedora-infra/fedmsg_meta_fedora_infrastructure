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


class ComposeProcessor(BaseProcessor):
    __name__ = "compose"
    __description__ = "Fedora Release Engineering"
    __link__ = "http://git.fedorahosted.org/cgit/releng"
    __docs__ = "https://fedoraproject.org/wiki/ReleaseEngineering"
    __obj__ = "Composes"

    def subtitle(self, msg, **config):
        branch = msg['msg']['branch']
        arch = msg['msg'].get('arch', '')
        arch = arch and ' (%s)' % arch


        if msg['topic'].endswith('.rsync.start'):
            tmpl = self._(
                "started rsyncing {branch} compose{arch}")
        elif msg['topic'].endswith('.rsync.complete'):
            tmpl = self._(
                "finished rsync of {branch} compose{arch}")
        elif msg['topic'].endswith('.mash.start'):
            tmpl = self._(
                "{branch} compose{arch} started mashing")
        elif msg['topic'].endswith('.mash.complete'):
            tmpl = self._(
                "{branch} compose{arch} finished mashing")
        elif msg['topic'].endswith('.pungify.start'):
            tmpl = self._(
                "started building boot.iso for {branch}{arch}")
        elif msg['topic'].endswith('.pungify.complete'):
            tmpl = self._(
                "finished building boot.iso for {branch}{arch}")
        elif msg['topic'].endswith('.start'):
            tmpl = self._("{branch} compose{arch} started")
        elif msg['topic'].endswith('.complete'):
            tmpl = self._("{branch} compose{arch} completed")
        else:
            raise NotImplementedError("%r" % msg)

        return tmpl.format(branch=branch, arch=arch)

    def link(self, msg, **config):
        arch = msg['msg'].get('arch', '')
        if arch:
            base = "https://dl.fedoraproject.org/pub/" + \
                "fedora-secondary/development"
        else:
            base = "https://dl.fedoraproject.org/pub/" + \
                "fedora/linux/development"

        # For backwards compatibility (with old messages in datanommer)
        if 'rawhide' in msg['topic']:
            return base + "/rawhide"

        return base + "/" + msg['msg'].get('branch', '')

    def objects(self, msg, **config):
        branch = msg['topic'].split('.')[4]
        arch = msg['msg'].get('arch', '')
        arch = arch or 'primary'
        return set(["%s/%s" % (branch, arch)])
