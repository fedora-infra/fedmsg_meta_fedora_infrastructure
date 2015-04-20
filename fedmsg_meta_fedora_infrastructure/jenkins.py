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
# Authors:  Ricky Elrod <codeblock@fedoraproject.org>

from fedmsg_meta_fedora_infrastructure import BaseProcessor
from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url


class JenkinsProcessor(BaseProcessor):
    __name__ = "Jenkins"
    __description__ = "Jenkins CI system"
    __link__ = "http://jenkins.cloud.fedoraproject.org/"
    __docs__ = "https://fedoraproject.org/wiki/Jenkins@infra"
    __obj__ = "Jenkins build status"
    __icon__ = ("https://wiki.jenkins-ci.org/download/attachments/"
                "2916393/logo.png?version=1")

    def subtitle(self, msg, **config):
        project = msg['msg'].get('project')

        if 'jenkins.build.failed' in msg['topic']:
            tmpl = self._("Jenkins project '{project}' failed to build")
        elif 'jenkins.build.passed' in msg['topic']:
            tmpl = self._("Jenkins project '{project}' built successfully")
        elif 'jenkins.build.unstable' in msg['topic']:
            tmpl = self._("Jenkins project '{project}' built with warnings")
        elif 'jenkins.build.notbuilt' in msg['topic']:
            tmpl = self._("Jenkins project '{project}' did not build")
        elif 'jenkins.build.aborted' in msg['topic']:
            tmpl = self._("Jenkins project '{project}' build aborted")
        elif 'jenkins.build.start' in msg['topic']:
            tmpl = self._("Jenkins project '{project}' started building")
        elif 'jenkins.build.unknown' in msg['topic']:
            tmpl = self._("Jenkins project '{project}' "
                          "entered an unknown state")
        else:
            raise NotImplementedError(msg['topic'])

        return tmpl.format(project=project)

    def link(self, msg, **config):
        build_id = msg['msg'].get('build')
        project = msg['msg'].get('project')

        if build_id is not None and project is not None:
            tmpl = ("http://jenkins.cloud.fedoraproject.org/job/{project}/"
                    "{build_id}/")
            return tmpl.format(build_id=build_id, project=project)
        else:
            return None

    def secondary_icon(self, msg, **config):
        return ''

    def usernames(self, msg, **config):
        return set()

    def objects(self, msg, **config):
        items = ['jenkins', msg['msg']['project']]
        items.append('.'.join(msg['topic'].split('.')[-2:]))
        return set(['/'.join(items)])
