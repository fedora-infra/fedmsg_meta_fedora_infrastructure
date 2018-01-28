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
# Authors:  Pierre-Yves Chibon <pingou@pingoured.fr>
#


from fedmsg_meta_fedora_infrastructure import BaseProcessor

from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url


class CentosCiProcessor(BaseProcessor):
    topic_prefix_re = 'org\\.centos\\.(dev|stage|prod)'

    __name__ = "ci"
    __description__ = "The CentOS Continuous Integration System"
    __link__ = "http://ci.centos.org/"
    __icon__ = "https://ci.centos.org/static/ec6de755/images/headshot.png"
    __docs__ = "https://github.com/CentOS-PaaS-SIG/ci-pipeline/"
    __obj__ = "CI Results"

    def subtitle(self, msg, **config):
        commit = msg['msg']['rev'][:8]
        branch = msg['msg']['branch']
        pkg = msg['msg']['repo']
        namespace = msg['msg']['namespace']
        status = msg['msg']['status']

        def _get_status(status):
            if status.lower() == 'success':
                status = 'passed'
            elif status.lower() == 'aborted':
                status = 'was aborted on'
            elif status.lower() == 'unstable':
                status = 'errored'
            else:
                status = 'failed'
            return status

        if 'ci.pipeline.package.ignore' in msg['topic']:
            tmpl = self._(
                'Commit "{commit}" of package {ns}/{pkg} is being '
                'ignored by the Atomic CI pipeline on branch {branch}')

        elif 'ci.pipeline.complete' in msg['topic']:
            status = _get_status(status)
            tmpl = self._(
                'Commit "{commit}" of package {ns}/{pkg} {status}'
                ' the Atomic CI pipeline on branch {branch}')

        elif 'ci.pipeline.package.complete' in msg['topic']:
            status = _get_status(status)
            tmpl = self._(
                'Commit {commit} of package {ns}/{pkg} {status} building '
                'in the Atomic CI pipeline on branch {branch}')

        elif 'ci.pipeline.package.queued' in msg['topic']:
            tmpl = self._(
                'Commit {commit} of package {ns}/{pkg} is queued to be built '
                'in the Atomic CI pipeline on branch {branch}')
        elif 'ci.pipeline.package.running' in msg['topic']:
            tmpl = self._(
                'Commit {commit} of package {ns}/{pkg} is being built in the '
                'Atomic CI pipeline on branch {branch}')

        elif 'ci.pipeline.package.test.functional.complete' in msg['topic']:
            status = _get_status(status)
            tmpl = self._(
                'Commit {commit} of package {ns}/{pkg} {status} its '
                'functional tests in the Atomic CI pipeline on branch {branch}')

        elif 'ci.pipeline.package.test.functional.queued' in msg['topic']:
            tmpl = self._(
                'Commit {commit} of package {ns}/{pkg} is queued for '
                'functional testing in the Atomic CI pipeline on branch {branch}')
        elif 'ci.pipeline.package.test.functional.running' in msg['topic']:
            tmpl = self._(
                'Commit {commit} of package {ns}/{pkg} is running its '
                'functional tests in the Atomic CI pipeline on branch {branch}')

        elif 'ci.pipeline.compose.complete' in msg['topic']:
            status = _get_status(status)
            tmpl = self._(
                'Commit {commit} of package {ns}/{pkg} {status} a '
                'compose in the Atomic CI pipeline on branch {branch}')

        elif 'ci.pipeline.compose.queued' in msg['topic']:
            tmpl = self._(
                'Commit {commit} of package {ns}/{pkg} is queued for a '
                'compose in the Atomic CI pipeline on branch {branch}')
        elif 'ci.pipeline.compose.running' in msg['topic']:
            tmpl = self._(
                'Commit {commit} of package {ns}/{pkg} is being part of a '
                'compose in the Atomic CI pipeline on branch {branch}')

        elif 'ci.pipeline.compose.test.integration.complete' in msg['topic']:
            status = _get_status(status)
            tmpl = self._(
                'Commit {commit} of package {ns}/{pkg} {status} its tests as '
                'part of a compose in the Atomic CI pipeline on branch {branch}')

        elif 'ci.pipeline.compose.test.integration.queued' in msg['topic']:
            tmpl = self._(
                'Commit {commit} of package {ns}/{pkg} is queued for tests '
                'as part of a compose in the Atomic CI pipeline on branch {branch}')
        elif 'ci.pipeline.compose.test.integration.running' in msg['topic']:
            tmpl = self._(
                'Commit {commit} of package {ns}/{pkg} is being tested as '
                'part of a compose in the Atomic CI pipeline on branch {branch}')

        elif 'ci.pipeline.image.complete' in msg['topic']:
            status = _get_status(status)
            tmpl = self._(
                'Commit {commit} of package {ns}/{pkg} {status} being built '
                'in an image in the Atomic CI pipeline on branch {branch}')

        elif 'ci.pipeline.image.queued' in msg['topic']:
            tmpl = self._(
                'Commit {commit} of package {ns}/{pkg} is queued to be built '
                'in an image in the Atomic CI pipeline on branch {branch}')
        elif 'ci.pipeline.image.running' in msg['topic']:
            tmpl = self._(
                'Commit {commit} of package {ns}/{pkg} is being built '
                'in an image in the Atomic CI pipeline on branch {branch}')

        elif 'ci.pipeline.image.test.smoke.complete' in msg['topic']:
            status = _get_status(status)
            tmpl = self._(
                'Commit {commit} of package {ns}/{pkg} {status} its tests '
                'in an image in the Atomic CI pipeline on branch {branch}')

        elif 'ci.pipeline.image.test.smoke.queued' in msg['topic']:
            tmpl = self._(
                'Commit {commit} of package {ns}/{pkg} is queued to be tested '
                'in an image in the Atomic CI pipeline on branch {branch}')
        elif 'ci.pipeline.image.test.smoke.running' in msg['topic']:
            tmpl = self._(
                'Commit {commit} of package {ns}/{pkg} is being tested '
                'in an image in the Atomic CI pipeline on branch {branch}')

        else:
            tmpl = ""

        return tmpl.format(
            commit=commit,
            ns=namespace,
            pkg=pkg,
            branch=branch,
            status=status,
        )

    def secondary_icon(self, msg, **config):
        try:
            user = msg['msg']['username']
            return avatar_url(user)
        except KeyError:
            return None

    def link(self, msg, **config):
        try:
            return msg['msg']['build_url']
        except KeyError:
            return self.__link__

    def usernames(self, msg, **config):
        try:
            return set([msg['msg']['username']])
        except KeyError:
            return set()

    def objects(self, msg, **config):
        namespace = msg['msg']['namespace']
        pkg = msg['msg']['repo']
        commit = msg['msg']['rev']
        branch = msg['msg']['branch']
        actions = msg['topic'].split('.pipeline.', 1)[1].split('.')

        return set(['/'.join([namespace, pkg, commit, branch] + actions)])
