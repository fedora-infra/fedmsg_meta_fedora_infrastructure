# This file is part of fedmsg.
# Copyright (C) 2013-2014 Red Hat, Inc.
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

import copy

from fedmsg_meta_fedora_infrastructure import BaseProcessor
from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url

from fedmsg_meta_fedora_infrastructure.conglomerators.copr import \
        copr as copr_conglomerator

_statuses = {
    0: 'failed',
    1: 'success',
    3: 'running',
    5: 'skipped',
}


_long_template = """Package:  {pkg}
COPR:     {owner}/{copr}
Built by: {user}
Status:   {status}
ID:       {build}

Logs:
  Build:     https://copr-be.cloud.fedoraproject.org/results/{owner}/{copr}/{chroot}/{build}-{pkg_name}/build.log.gz
  Root:      https://copr-be.cloud.fedoraproject.org/results/{owner}/{copr}/{chroot}/{build}-{pkg_name}/root.log.gz
  Copr:      https://copr-be.cloud.fedoraproject.org/results/{owner}/{copr}/{chroot}/build-{build}.log
  Mockchain: https://copr-be.cloud.fedoraproject.org/results/{owner}/{copr}/{chroot}/{build}-{pkg_name}/mockchain.log.gz
Results:     https://copr-be.cloud.fedoraproject.org/results/{owner}/{copr}/{chroot}/{build}-{pkg_name}/
Repodata:    https://copr-be.cloud.fedoraproject.org/results/{owner}/{copr}/{chroot}/repodata/
"""


def apply_backwards_compat(msg):
    if msg.get('pkg') and msg.get('version'):
        if msg['version'] not in msg['pkg']:
            msg['pkg'] = msg['pkg'] + '-' + msg['version']

    if 'user' in msg and 'owner' not in msg:
        msg['owner'] = msg['user']

    return msg


class CoprsProcessor(BaseProcessor):
    __name__ = "Copr"
    __description__ = "the Cool Other Package Repositories system"
    __link__ = "https://copr.fedorainfracloud.org"
    __docs__ = "https://fedorahosted.org/copr"
    __obj__ = "Extra Repository Updates"
    __icon__ = "https://apps.fedoraproject.org/img/icons/copr.png"

    conglomerators = [
        copr_conglomerator.ByCopr,
        copr_conglomerator.ByUser,
    ]

    def long_form(self, msg, **config):
        if 'copr.build.end' in msg['topic']:
            kwargs = copy.copy(msg['msg'])

            kwargs = apply_backwards_compat(kwargs)

            kwargs['status'] = _statuses.get(kwargs.get('status'), 'unknown')

            # Zero pad buildid
            kwargs['build'] = '%08d' % (kwargs['build'])

            if '-' not in kwargs['version']:
                # This has happened.
                # Example: 2017-c1e242e3-3a1c-4de9-8d37-61640b5e99fa
                name = '?? WHO KNOWS ??'
            else:
                # Also, extract the name from the NVR.
                name, version, release = kwargs['pkg'].rsplit('-', 2)
            kwargs['pkg_name'] = name

            details = _long_template.format(**kwargs)
            return details

    def subtitle(self, msg, **config):

        # So many changes to this message format over time...
        msg['msg'] = apply_backwards_compat(msg['msg'])

        user = msg['msg'].get('user')
        copr = msg['msg'].get('copr')
        chroot = msg['msg'].get('chroot')
        pkg = msg['msg'].get('pkg')

        status = _statuses.get(msg['msg'].get('status'), 'unknown')

        if 'copr.build.start' in msg['topic']:
            if user:
                tmpl = self._("{user} started a new build of the {copr} copr")
            else:
                tmpl = self._("Automated build of the {copr} copr has been started")
        elif 'copr.build.end' in msg['topic']:
            if user:
                tmpl = self._(
                    "{user}'s {copr} copr build of {pkg} for {chroot} "
                    "finished with '{status}'")
            else:
                tmpl = self._(
                    "Automated {copr} copr build of {pkg} for {chroot} "
                    "finished with '{status}'")
        elif 'copr.chroot.start' in msg['topic']:
            tmpl = self._("{user}'s {copr} copr started a new {chroot} chroot")
        elif 'copr.worker.create' in msg['topic']:
            tmpl = self._("a new worker was created")
        else:
            raise NotImplementedError()

        return tmpl.format(user=user, copr=copr, pkg=pkg,
                           chroot=chroot, status=status)

    def link(self, msg, **config):
        user = msg['msg'].get('owner', msg['msg'].get('user'))
        if user and user.startswith('@'):
            # It's a group
            user = user.replace('@', 'g/')
        copr = msg['msg'].get('copr')
        chroot = msg['msg'].get('chroot', None)
        build = msg['msg'].get('build')

        if 'chroot' in msg['topic']:
            tmpl = ("https://copr-be.cloud.fedoraproject.org/"
                    "results/{user}/{copr}/{chroot}/")
        elif 'build' in msg['topic']:
            tmpl = ("https://copr.fedoraproject.org/"
                    "coprs/{user}/{copr}/build/{build}/")
        else:
            return "https://copr.fedoraproject.org"

        return tmpl.format(user=user, copr=copr, chroot=chroot, build=build)

    def secondary_icon(self, msg, **config):
        if 'user' in msg['msg']:
            return avatar_url(msg['msg']['user'])

    def usernames(self, msg, **config):
        usernames = set()
        if 'user' in msg['msg']:
            usernames.add(msg['msg']['user'])
        if 'owner' in msg['msg']:
            usernames.add(msg['msg']['owner'])
        # Filter out any None values
        return set([u for u in usernames if u])

    def objects(self, msg, **config):
        items = ['coprs']

        if 'copr' in msg['msg']:
            items.append(msg['msg']['copr'])

        items.append('.'.join(msg['topic'].split('.')[-2:]))

        if 'chroot' in msg['topic']:
            items.append(msg['msg']['chroot'])

        return set(['/'.join(items)])
