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
            if msg['msg']['trigger']['topic'].endswith('.project.map.new'):
                packages = [original['message']['new']]
            else:
                packages = [
                    pkg['package_name']
                    for pkg in original['message']['packages']
                    if pkg['distro'] == 'Fedora'
                ]
            tmpl= self._('the-new-hotness filed a bug on {packages}')
            return tmpl.format(packages=", ".join(packages))
        elif 'hotness.update.bug.followup' in msg['topic']:
            # This could be one of two different kinds of followup
            original = msg['msg']['trigger']['msg']
            bug_id = msg['msg']['bug']['bug_id']
            if 'srpm' in original:
                srpm = original['srpm']

                # The original task statuses from koji can be found like this
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

                tmpl= self._('scratch build of {srpm} '
                             'for RHBZ#{bug_id} {status}')
                return tmpl.format(srpm=srpm, bug_id=bug_id, status=status)
            else:
                user = original['owner']
                build = '-'.join([
                    original[k] for k in ['name', 'version', 'release']])

                # The original build statuses from koji can be found like this
                # >>> import koji
                # >>> koji.BUILD_STATES
                # {'BUILDING': 0, 'DELETED': 2, 'CANCELED': 4,
                # 'COMPLETE': 1, 'FAILED': 3}
                status_lookup = [
                    self._('started'),
                    self._('completed'),
                    self._('deleted'),
                    self._('cancelled'),
                    self._('failed'),
                ]
                status = status_lookup[original['new']]
                tmpl= self._("{user}'s real build of {build} "
                             "for RHBZ#{bug_id} {status}")
                return tmpl.format(user=user, build=build,
                                   bug_id=bug_id, status=status)
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
                'pkgdb': self._("pkgdb says the maintainers are not "
                                "interested in bugs being filed"),
                'rawhide': self._("no rawhide version of the "
                                  "package could be found yet")
            }
            errmsg = self._('.... I dunno.  Whatever.')
            return prefix.format(thing=thing) + qualifiers.get(reason, errmsg)
        elif 'hotness.project.map' in msg['topic']:
            original = msg['msg']['trigger']['msg']
            if 'package_listing' in original:
                package = original['package_listing']['package']['name']
            else:
                package = original['package']['name']

            if 'reason' in msg['msg']:
                return self._(
                    'hotness tried to map {package} to an upstream project, '
                    'but failed:  "{reason}"').format(
                        package=package,
                        reason=msg['msg']['reason'],
                    )
            elif 'total' in msg['msg']:
                return self._(
                    'hotness tried to map {package} to an upstream project, '
                    'but failed due to ambiguity.  {total} other projects '
                    'share the same homepage').format(
                        package=package,
                        total=msg['msg']['total']
                    )
            elif 'project' in msg['msg']:
                if msg['msg']['success']:
                    return self._(
                        'hotness mapped {package} to the pre-existing '
                        'upstream project {project}').format(
                            package=package,
                            project=msg['msg']['project']['name'],
                        )
                else:
                    return self._(
                        'hotness tried to map {package} to the pre-existing '
                        'upstream project {project}, but failed for unknown '
                        'reasons').format(
                            package=package,
                            project=msg['msg']['project']['name'],
                        )
            else:
                if msg['msg']['success']:
                    return self._(
                        'hotness mapped {package} to a '
                        'brand-new upstream project'
                    ).format(package=package)
                else:
                    return self._(
                        'hotness tried to map {package} to a brand-new '
                        'upstream project, but failed for unknown reasons'
                    ).format(package=package)

    def link(self, msg, **config):
        if 'bug' in msg['msg']:
            base = 'bugzilla.redhat.com/show_bug.cgi?id=%i'
            if '.stg.' in msg['topic']:
                base = 'partner-' + base
            return 'https://' + base % msg['msg']['bug']['bug_id']
        elif 'trigger' in msg['msg']:
            original = msg['msg']['trigger']['msg']
            if 'project' in original:
                base = 'https://release-monitoring.org/project/%i/'
                return base % original['project']['id']
            elif 'project' in msg['msg']:
                base = 'https://release-monitoring.org/project/%i/'
                return base % msg['msg']['project']['id']
            elif 'package_listing' in original:
                return original['package_listing']['package']['review_url']
            elif 'package' in original:
                return original['package']['upstream_url']

    def secondary_icon(self, msg, **config):
        tmpl = 'https://apps.fedoraproject.org/packages/images/icons/%s.png'
        packages = self.packages(msg, **config)
        return tmpl % (list(packages)[0] if packages else "package_128x128")

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

        if 'package_listing' in msg['msg']['trigger']['msg']:
            original = msg['msg']['trigger']['msg']
            packages = [
                'packages/' + original['package_listing']['package']['name']
            ]
            projects = []
            if 'project' in msg['msg']:
                projects += ['projects/' + msg['msg']['project']['name']]
            return set(packages + projects)

        if 'package' in msg['msg']['trigger']['msg']:
            original = msg['msg']['trigger']['msg']
            packages = [
                'packages/' + original['package']['name']
            ]
            return set(packages)

        return set(bugs)

    def usernames(self, msg, **config):
        if 'buildsys.build' in msg['msg']['trigger']['topic']:
            return set([msg['msg']['trigger']['msg']['owner']])

        return set()

    def packages(self, msg, **config):
        if 'anitya' in msg['msg']['trigger']['topic']:
            original = msg['msg']['trigger']['msg']

            packages = None
            if 'packages' in original['message']:
                packages = original['message']['packages']
            elif 'packages' in original:
                packages = original['packages']

            if packages:
                return set([
                    pkg['package_name'] for pkg in packages
                    if pkg['distro'] == 'Fedora'
                ])

        if 'package_listing' in msg['msg']['trigger']['msg']:
            original = msg['msg']['trigger']['msg']
            return set([original['package_listing']['package']['name']])

        if 'buildsys.build' in msg['msg']['trigger']['topic']:
            return set([msg['msg']['trigger']['msg']['name']])

        if 'package' in msg['msg']['trigger']['msg']:
            original = msg['msg']['trigger']['msg']
            return set([original['package']['name']])

        return set()
