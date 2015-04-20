# This file is part of fedmsg.
# Copyright (C) 2012-2014 Red Hat, Inc.
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

from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url
from fedmsg_meta_fedora_infrastructure import BaseProcessor


class KernelTestProcessor(BaseProcessor):
    __name__ = "kerneltest"
    __description__ = "Kernel Testing Initiative"
    __link__ = "https://apps.fedoraproject.org/kerneltest"
    __icon__ = "https://apps.fedoraproject.org/img/icons/tux.png"
    __docs__ = "https://fedoraproject.org/wiki/KernelTestingInitiative"
    __obj__ = "Kernel Tests"

    def link(self, msg, **config):
        if 'test' in msg['msg']:
            vers = msg['msg']['test']['kernel_version']
            return 'https://apps.fedoraproject.org/kerneltest/kernel/' + vers
        return 'https://apps.fedoraproject.org/kerneltest/stats'

    def subtitle(self, msg, **config):
        user = msg['msg']['agent']

        if 'test' in msg['msg']:
            tmpl = self._('{user} ran a test of {version} ({result})')
            version = msg['msg']['test']['kernel_version']
            result = msg['msg']['test']['result']
            return tmpl.format(user=user, version=version, result=result)
        elif 'release.edit' in msg['topic']:
            tmpl = self._(
                '{user} edited the {release}-{support} '
                'release for kerneltest')
            release = msg['msg']['release']['releasenum']
            support = msg['msg']['release']['support']
            return tmpl.format(user=user, release=release, support=support)
        elif 'release.new' in msg['topic']:
            tmpl = self._(
                '{user} added a new release for kerneltest: '
                '{release} {support}')
            release = msg['msg']['release']['releasenum']
            support = msg['msg']['release']['support']
            return tmpl.format(user=user, release=release, support=support)

    def secondary_icon(self, msg, **config):
        return avatar_url(msg['msg']['agent'])

    def usernames(self, msg, **config):
        return set([msg['msg']['agent']])

    def packages(self, msg, **config):
        return set(['kernel'])

    def objects(self, msg, **config):
        if 'test' in msg['msg']:
            vers = msg['msg']['test']['kernel_version']
            return set(['kernel/' + vers])
        elif 'release' in msg['msg']:
            releasenum = msg['msg']['release']['releasenum']
            support = msg['msg']['release']['support']
            return set(['release/{releasenum}/{support}'.format(
                releasenum=releasenum, support=support)])
