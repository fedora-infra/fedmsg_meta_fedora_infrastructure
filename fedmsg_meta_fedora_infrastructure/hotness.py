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
# Authors:  Ralph Bean <rbean@redhat.com>

from fedmsg_meta_fedora_infrastructure import BaseProcessor


class HotnessProcessor(BaseProcessor):
    __name__ = 'hotness'
    __description__ = "A fedmsg consumer that files bugzilla bugs " + \
        "for upstream releases"
    __link__ = "https://release-monitoring.org"
    __docs__ = "https://fedoraproject.org/wiki/Upstream_release_monitoring"
    __obj__ = "Fresh Builds & Bugs"
    __icon__ = ("https://apps.fedoraproject.org/packages/"
                "images/icons/package_128x128.png")

    def subtitle(self, msg, **config):
        if 'hotness.update.bug.file' in msg['topic']:
            original = msg['msg']['trigger']['msg']
            packages = [
                pkg['package_name'] for pkg in original['message']['packages']
                if pkg['distro'] == 'Fedora'
            ]
            tmpl= self._('the-new-hotness filed a bug on {packages}')
            return tmpl.format(packages=", ".join(packages))
        elif 'hotness.update.bug.followup' in msg['topic']:
            original = msg['msg']['trigger']['msg']
            srpm = original['srpm']
            bug_id = msg['msg']['bug']['bug_id']

            # The original statuses from koji can be found like this
            # >>> import koji
            # >>> koji.TASK_STATES.keys()
            # ['FAILED', 'FREE', 'ASSIGNED', 'CANCELED', 'CLOSED', 'OPEN']
            status_lookup = {
                'FAILED': self._('failed'),
                'FREE': self._('submitted'),
                'ASSIGNED': self._('assigned'),
                'CANCELLED': self._('cancelled'),
                'CLOSED': self._('completed'),
                'OPEN': self._('started'),
            }
            status = status_lookup.get(original['new'], 'unknown')

            tmpl= self._('scratch build of {srpm} for RHBZ#{bug_id} {status}')
            return tmpl.format(srpm=srpm, bug_id=bug_id, status=status)
        elif 'hotness.update.drop' in msg['topic']:
            original = msg['msg']['trigger']['msg']
            reason = msg['msg']['reason']

            packages = self.packages(msg, **config)
            if packages:
                thing = list(packages)[0]
            else:
                thing = original['project']['name']

            prefix = self._('the-new-hotness saw an update for {thing}, but ')
            qualifiers = {
                'anitya': self._("release-monitoring.org doesn't know what "
                                 "that project is called in Fedora land"),
                'bugzilla': self._("a bugzilla ticket had already been filed"),
                'pkgdb': self._("pkgdb says the package owner is not "
                                "interested in bugs being filed"),
            }
            errmsg = self._('.... I dunno.  Whatever.')
            return prefix.format(thing=thing) + qualifiers.get(reason, errmsg)

    def link(self, msg, **config):
        if 'bug' in msg['msg']:
            base = 'bugzilla.redhat.com/show_bug.cgi?id=%i'
            if '.stg.' in msg['topic']:
                base = 'partner-' + base
            return 'https://' + base % msg['msg']['bug']['bug_id']
        else:
            original = msg['msg']['trigger']['msg']
            base = 'https://release-monitoring.org/project/%i/'
            return base % original['project']['id']

    def secondary_icon(self, msg, **config):
        return self.icon(msg, **config)

    def objects(self, msg, **config):
        bugs = []
        if 'bug' in msg['msg']:
            bugs = ['bugs/%i' % msg['msg']['bug']['bug_id']]

        if 'anitya' in msg['msg']['trigger']['topic']:
            original = msg['msg']['trigger']['msg']
            packages = [
                'packages/' + pkg['package_name']
                for pkg in original['message']['packages']
                if pkg['distro'] == 'Fedora'
            ]
            projects = ['projects/' + original['project']['name']]
            return set(packages + projects + bugs)

        return set(bugs)

    def packages(self, msg, **config):
        if 'anitya' in msg['msg']['trigger']['topic']:
            original = msg['msg']['trigger']['msg']
            return set([
                pkg['package_name'] for pkg in original['message']['packages']
                if pkg['distro'] == 'Fedora'
            ])

        return set()
