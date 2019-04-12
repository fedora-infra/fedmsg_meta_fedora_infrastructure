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


class AtomicCiProcessor(BaseProcessor):
    topic_prefix_re = 'org\\.centos\\.(dev|stage|prod)'

    __name__ = "ci.pipeline"
    __description__ = "The Atomic Continuous Integration pipeline"
    __link__ = "http://ci.centos.org/"
    __icon__ = "https://ci.centos.org/static/ec6de755/images/headshot.png"
    __docs__ = "https://github.com/CentOS-PaaS-SIG/ci-pipeline/"
    __obj__ = "CI Results"

    pipeline_name = 'Atomic CI'

    def subtitle(self, msg, **config):
        rev = msg['msg']['rev'] or ""
        if rev.startswith('kojitask-'):
            revtype = "Koji task"
            rev = rev.split('kojitask-')[1]
        elif rev.startswith('PR-'):
            revtype = "Pull request"
            rev = rev.split('PR-')[1]
        else:
            # I'm assuming there aren't any other types, here...
            revtype = "Commit"
            rev = rev[:8]
        branch = msg['msg']['branch'] or 'unknown_branch'
        pkg = msg['msg']['repo'] or 'unknown_repo'
        namespace = msg['msg']['namespace'] or 'unknown_namespace'
        status = msg['msg']['status'] or 'unknown_status'

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

        name = self.__name__
        pipeline_name = self.pipeline_name

        # current allpackages pipelines as of 2019-04-12
        if '%s.allpackages-build' % name in msg['topic']:
            name = "ci.pipeline.allpackages-build"
            pipeline_name = 'All Packages (Build) CI'

        elif '%s.allpackages-pr' % name in msg['topic']:
            name = "ci.pipeline.allpackages-pr"
            pipeline_name = 'All Packages (PR) CI'

        # old allpackages pipeline from before PR testing
        elif '%s.allpackages' % name in msg['topic']:
            name = "ci.pipeline.allpackages"
            pipeline_name = 'All Packages CI'

        elif '%s.container' % name in msg['topic']:
            name = "ci.pipeline.container-pr"
            pipeline_name = 'Container CI'

        if '%s.package.ignore' % name in msg['topic']:
            tmpl = self._(
                '{revtype} "{rev}" of package {ns}/{pkg} is being '
                'ignored by the {pipeline_name} pipeline on branch {branch}')

        elif '%s.complete' % name in msg['topic']:
            status = _get_status(status)
            tmpl = self._(
                '{revtype} "{rev}" of package {ns}/{pkg} {status}'
                ' the {pipeline_name} pipeline on branch {branch}')
            if pipeline_name == 'Container CI':
                tmpl = self._(
                    '{revtype} "{rev}" of container {ns}/{pkg} {status}'
                    ' the {pipeline_name} pipeline on branch {branch}')

        elif '%s.package.complete' % name in msg['topic']:
            status = _get_status(status)
            tmpl = self._(
                '{revtype} {rev} of package {ns}/{pkg} {status} building '
                'in the {pipeline_name} pipeline on branch {branch}')

        elif '%s.package.queued' % name in msg['topic']:
            tmpl = self._(
                '{revtype} {rev} of package {ns}/{pkg} is queued to be built '
                'in the {pipeline_name} pipeline on branch {branch}')

        elif '%s.package.running' % name in msg['topic']:
            tmpl = self._(
                '{revtype} {rev} of package {ns}/{pkg} is being built in '
                'the {pipeline_name} pipeline on branch {branch}')

        elif '%s.package.test.functional.complete' % name in msg['topic']:
            status = _get_status(status)
            tmpl = self._(
                '{revtype} {rev} of package {ns}/{pkg} {status} its '
                'functional tests in the {pipeline_name} pipeline on '
                'branch {branch}')

        elif '%s.package.test.functional.queued' % name in msg['topic']:
            tmpl = self._(
                '{revtype} {rev} of package {ns}/{pkg} is queued for '
                'functional testing in the {pipeline_name} pipeline on '
                'branch {branch}')

        elif '%s.package.test.functional.running' % name in msg['topic']:
            tmpl = self._(
                '{revtype} {rev} of package {ns}/{pkg} is running its '
                'functional tests in the {pipeline_name} pipeline on '
                'branch {branch}')

        elif '%s.container.test.functional.complete' % name in msg['topic']:
            status = _get_status(status)
            tmpl = self._(
                '{revtype} {rev} of container {ns}/{pkg} {status} its '
                'functional tests in the {pipeline_name} pipeline on '
                'branch {branch}')

        elif '%s.container.test.functional.queued' % name in msg['topic']:
            tmpl = self._(
                '{revtype} {rev} of container {ns}/{pkg} is queued for '
                'functional testing in the {pipeline_name} pipeline on '
                'branch {branch}')

        elif '%s.container.test.functional.running' % name in msg['topic']:
            tmpl = self._(
                '{revtype} {rev} of container {ns}/{pkg} is running its '
                'functional tests in the {pipeline_name} pipeline on '
                'branch {branch}')

        elif '%s.compose.complete' % name in msg['topic']:
            status = _get_status(status)
            tmpl = self._(
                '{revtype} {rev} of package {ns}/{pkg} {status} a '
                'compose in the {pipeline_name} pipeline on branch {branch}')

        elif '%s.compose.queued' % name in msg['topic']:
            tmpl = self._(
                '{revtype} {rev} of package {ns}/{pkg} is queued for a '
                'compose in the {pipeline_name} pipeline on branch {branch}')

        elif '%s.compose.running' % name in msg['topic']:
            tmpl = self._(
                '{revtype} {rev} of package {ns}/{pkg} is being part of a '
                'compose in the {pipeline_name} pipeline on branch {branch}')

        elif '%s.compose.test.integration.complete' % name in msg['topic']:
            status = _get_status(status)
            tmpl = self._(
                '{revtype} {rev} of package {ns}/{pkg} {status} its tests '
                'as part of a compose in the {pipeline_name} pipeline on '
                'branch {branch}')

        elif '%s.compose.test.integration.queued' % name in msg['topic']:
            tmpl = self._(
                '{revtype} {rev} of package {ns}/{pkg} is queued for tests '
                'as part of a compose in the {pipeline_name} pipeline on '
                'branch {branch}')

        elif '%s.compose.test.integration.running' % name in msg['topic']:
            tmpl = self._(
                '{revtype} {rev} of package {ns}/{pkg} is being tested as '
                'part of a compose in the {pipeline_name} pipeline on '
                'branch {branch}')

        elif '%s.image.complete' % name in msg['topic']:
            status = _get_status(status)
            tmpl = self._(
                '{revtype} {rev} of package {ns}/{pkg} {status} being built '
                'in an image in the {pipeline_name} pipeline on '
                'branch {branch}')

        elif '%s.image.queued' % name in msg['topic']:
            tmpl = self._(
                '{revtype} {rev} of package {ns}/{pkg} is queued to be built '
                'in an image in the {pipeline_name} pipeline on '
                'branch {branch}')

        elif '%s.image.running' % name in msg['topic']:
            tmpl = self._(
                '{revtype} {rev} of package {ns}/{pkg} is being built '
                'in an image in the {pipeline_name} pipeline on '
                'branch {branch}')

        elif '%s.image.test.smoke.complete' % name in msg['topic']:
            status = _get_status(status)
            tmpl = self._(
                '{revtype} {rev} of package {ns}/{pkg} {status} its tests '
                'in an image in the {pipeline_name} pipeline on '
                'branch {branch}')

        elif '%s.image.test.smoke.queued' % name in msg['topic']:
            tmpl = self._(
                '{revtype} {rev} of package {ns}/{pkg} is queued to be tested '
                'in an image in the {pipeline_name} pipeline on '
                'branch {branch}')

        elif '%s.image.test.smoke.running' % name in msg['topic']:
            tmpl = self._(
                '{revtype} {rev} of package {ns}/{pkg} is being tested '
                'in an image in the {pipeline_name} pipeline on '
                'branch {branch}')

        else:
            tmpl = ""

        return tmpl.format(
            revtype=revtype,
            rev=rev,
            ns=namespace,
            pkg=pkg,
            branch=branch,
            status=status,
            pipeline_name=pipeline_name
        )

    def secondary_icon(self, msg, **config):
        user = msg['msg'].get('username')
        if user:
            user = avatar_url(user)
        return user

    def link(self, msg, **config):
        try:
            return msg['msg']['build_url']
        except KeyError:
            return self.__link__

    def usernames(self, msg, **config):
        user = msg['msg'].get('username')
        if user:
            return set([user])
        return set()

    def objects(self, msg, **config):
        namespace = msg['msg']['namespace'] or 'unknown_namespace'
        pkg = msg['msg']['repo'] or 'unknown_pkg'
        commit = msg['msg']['rev'] or 'unknown_rev'
        branch = msg['msg']['branch'] or 'unknown_branch'
        actions = msg['topic'].split('.pipeline.', 1)[1].split('.')

        return set(['/'.join([namespace, pkg, commit, branch] + actions)])


class OldAllpackagesCiProcessor(AtomicCiProcessor):
    topic_prefix_re = 'org\\.centos\\.(dev|stage|prod)'

    __name__ = "allpackages.pipeline"
    __description__ = "The CentOS Continuous Integration pipeline for all " \
        "packages"
    __link__ = "http://ci.centos.org/"
    __icon__ = "https://ci.centos.org/static/ec6de755/images/headshot.png"
    __docs__ = "https://github.com/CentOS-PaaS-SIG/ci-pipeline/"
    __obj__ = "CI AllPackages Results"

    pipeline_name = 'All Packages CI'

class OldContainerCiProcessor(AtomicCiProcessor):
    topic_prefix_re = 'org\\.centos\\.(dev|stage|prod)'

    __name__ = "container.pipeline"
    __description__ = "The CentOS Continuous Integration pipeline for " \
        "containers"
    __link__ = "http://ci.centos.org/"
    __icon__ = "https://ci.centos.org/static/ec6de755/images/headshot.png"
    __docs__ = "https://github.com/CentOS-PaaS-SIG/ci-pipeline/"
    __obj__ = "CI Container Results"

    pipeline_name = 'Container CI'
