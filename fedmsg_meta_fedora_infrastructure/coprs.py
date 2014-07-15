# This file is part of fedmsg.
# Copyright (C) 2013 Red Hat, Inc.
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
from fasshim import gravatar_url


class CoprsProcessor(BaseProcessor):
    __name__ = "Copr"
    __description__ = "the Cool Other Package Repositories system"
    __link__ = "https://copr-fe.cloud.fedoraproject.org"
    __docs__ = "http://fedorahosted.org/copr"
    __obj__ = "Extra Repository Updates"
    __icon__ = "https://apps.fedoraproject.org/img/icons/copr.png"

    def subtitle(self, msg, **config):

        user = msg['msg'].get('user')
        copr = msg['msg'].get('copr')
        chroot = msg['msg'].get('chroot')

        statuses = {
            0: 'failed',
            1: 'success',
            3: 'running',
            5: 'skipped',
        }

        status = statuses.get(msg['msg'].get('status'), 'unknown')

        if 'copr.build.start' in msg['topic']:
            tmpl = self._("{user} started a new build of the {copr} copr")
        elif 'copr.build.end' in msg['topic']:
            tmpl = self._(
                "{user}'s {copr} copr build finished {chroot} with '{status}'")
        elif 'copr.chroot.start' in msg['topic']:
            tmpl = self._("{user}'s {copr} copr started a new {chroot} chroot")
        elif 'copr.worker.create' in msg['topic']:
            tmpl = self._("a new worker was created")
        else:
            raise NotImplementedError()

        return tmpl.format(user=user, copr=copr, chroot=chroot, status=status)

    def link(self, msg, **config):
        user = msg['msg'].get('user')
        copr = msg['msg'].get('copr')
        chroot = msg['msg'].get('chroot', None)

        if 'chroot' in msg['topic']:
            tmpl = ("https://copr-be.cloud.fedoraproject.org/"
                    "results/{user}/{copr}/{chroot}/")
        elif 'build' in msg['topic']:
            tmpl = ("https://copr.fedoraproject.org/"
                    "coprs/{user}/{copr}/")
        else:
            return "https://copr.fedoraproject.org"

        return tmpl.format(user=user, copr=copr, chroot=chroot)

    def secondary_icon(self, msg, **config):
        if 'user' in msg['msg']:
            return gravatar_url(msg['msg']['user'])

    def usernames(self, msg, **config):
        if 'user' in msg['msg']:
            return set([msg['msg']['user']])
        return set()

    def objects(self, msg, **config):
        items = ['coprs']

        if 'copr' in msg['msg']:
            items.append(msg['msg']['copr'])

        items.append('.'.join(msg['topic'].split('.')[-2:]))

        if 'chroot' in msg['topic']:
            items.append(msg['msg']['chroot'])

        return set(['/'.join(items)])
