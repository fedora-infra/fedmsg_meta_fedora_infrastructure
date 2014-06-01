# This file is part of fedmsg.
# Copyright (C) 2012, 2013 Red Hat, Inc.
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
#           Luke Macken <lmacken@redhat.com>

from fasshim import gravatar_url, email2fas
from fedmsg_meta_fedora_infrastructure import BaseProcessor


def project2fedora_package(project):
    # TODO -- this function should go out and query cnucnu/api/project/PROJECT
    # and get back the list of distro mappings for that project.  It should
    # then return the name of the package in Fedora.
    # For now, we'll have this dummy code here so the tests pass until we can
    # actually deploy cnucnu.
    if project == 'ansi2html':
        return 'python-ansi2html'
    else:
        return project


class CnuCnuWebProcessor(BaseProcessor):
    __name__ = "cnucnuweb"
    __description__ = "Upstream Release Monitoring"
    __link__ = "https://apps.fedoraproject.org/cnucnu/"
    __docs__ = "https://fedoraproject.org/wiki/Upstream_Release_Monitoring"
    __obj__ = "Upstream Releases"
    __icon__ = "https://todo.com/image.png"

    def _get_user(self, msg, **config):
        try:
            email = msg['msg']['message']['agent']
        except KeyError:
            return None
        else:
            return email2fas(email, **config)

    def link(self, msg, **config):
        if msg['msg']['project']:
            proj = msg['msg']['project']['name']
            return "https://apps.fedoraproject.org/cnucnu/project/%s/" % proj
        else:
            return "https://apps.fedoraproject.org/cnucnu/distros"

        return None

    def subtitle(self, msg, **config):
        user = self._get_user(msg, **config)
        if 'project.map.new' in msg['topic']:
            project = msg['msg']['project']['name']
            distro = msg['msg']['distro']['name']
            new = msg['msg']['message']['new']
            tmpl = self._(
                '{user} mapped the name of "{project}" in {distro} '
                'to "{new}"'
            )
            return tmpl.format(
                user=user, project=project, distro=distro, new=new)
        elif 'project.map.update' in msg['topic']:
            project = msg['msg']['project']['name']
            distro = msg['msg']['distro']['name']
            old = msg['msg']['message']['prev']
            new = msg['msg']['message']['new']
            tmpl = self._(
                '{user} updated the name of "{project}" in '
                '"{distro}" from "{old}" to "{new}"')
            return tmpl.format(
                user=user, project=project, distro=distro, new=new, old=old)
        elif 'distro.add' in msg['topic']:
            distro = msg['msg']['distro']['name']
            tmpl = self._(
                '{user} added the distro named "{distro}" to cnucnuweb')
            return tmpl.format(user=user, distro=distro)
        elif 'distro.edit' in msg['topic']:
            old = msg['msg']['message']['old']
            new = msg['msg']['message']['new']
            tmpl = self._(
                '{user} changed a distro name from "{old}" to "{new}"')
            return tmpl.format(user=user, old=old, new=new)
        elif 'project.add.tried' in msg['topic']:
            project = msg['msg']['project']['name']
            tmpl = self._('{user} tried to add the project '
                          '"{project}" to cnucnuweb')
            return tmpl.format(user=user, project=project)
        elif 'project.add' in msg['topic']:
            project = msg['msg']['project']['name']
            tmpl = self._('{user} added the project "{project}" to cnucnuweb')
            return tmpl.format(user=user, project=project)
        elif 'project.edit' in msg['topic']:
            project = msg['msg']['project']['name']
            fields = ', '.join(msg['msg']['message']['fields'])
            tmpl = self._(
                '{user} edited the following fields of the '
                '"{project}" project: {fields}')
            return tmpl.format(user=user, project=project, fields=fields)
        elif 'project.remove' in msg['topic']:
            project = msg['msg']['project']['name']
            tmpl = self._('{user} deleted the "{project}" project')
            return tmpl.format(user=user, project=project)
        elif 'project.version.update' in msg['topic']:
            project = msg['msg']['project']['name']
            old = msg['msg']['old_version']
            new = msg['msg']['upstream_version']
            tmpl = self._(
                'A new version of "{project}" has been detected:  '
                '"{new}" in advance of "{old}"')
            return tmpl.format(project=project, new=new, old=old)
        else:
            pass

    def secondary_icon(self, msg, **config):
        username = self._get_user(msg, **config)
        if username:
            return gravatar_url(self._get_user(msg, **config))
        else:
            return None

    def usernames(self, msg, **config):
        username = self._get_user(msg, **config)
        if username:
            return set([username])
        else:
            return set([])

    def objects(self, msg, **config):
        if 'project.map.update' in msg['topic']:
            distro = msg['msg']['distro']['name']
            return set([
                'mappings/%s/%s' % (distro, msg['msg']['message']['new']),
                'mappings/%s/%s' % (distro, msg['msg']['message']['prev']),
                'distros/%s' % distro,
                'projects/%s' % msg['msg']['project']['name'],
            ])
        elif 'project.map.new' in msg['topic']:
            distro = msg['msg']['distro']['name']
            return set([
                'mappings/%s/%s' % (distro, msg['msg']['message']['new']),
                'distros/%s' % distro,
                'projects/%s' % msg['msg']['project']['name'],
            ])
        elif 'project.remove' in msg['topic']:
            return set(['projects/%s' % msg['msg']['project']['name']])
        elif 'project.version.update' in msg['topic']:
            return set(['projects/%s' % msg['msg']['project']['name']])
        elif 'project.edit' in msg['topic']:
            return set(['projects/%s' % msg['msg']['project']['name']])
        elif 'project.add.tried' in msg['topic']:
            return set(['projects/%s' % msg['msg']['project']['name']])
        elif 'project.add' in msg['topic']:
            return set(['projects/%s' % msg['msg']['project']['name']])
        elif 'distro.add' in msg['topic']:
            distro = msg['msg']['distro']['name']
            return set(['distros/%s' % distro])
        elif 'distro.edit' in msg['topic']:
            distro_old = msg['msg']['message']['old']
            distro_new = msg['msg']['message']['new']
            return set([
                'distros/%s' % distro_old,
                'distros/%s' % distro_new,
            ])

        return set([])

    def packages(self, msg, **config):
        if 'project.map.update' in msg['topic']:
            if msg['msg']['distro']['name'].lower() == 'fedora':
                return set([
                    msg['msg']['message']['new'],
                    msg['msg']['message']['prev'],
                ])
        elif 'project.map.new' in msg['topic']:
            if msg['msg']['distro']['name'].lower() == 'fedora':
                return set([msg['msg']['message']['new']])
        elif 'project.version.update' in msg['topic']:
            return set([project2fedora_package(msg['msg']['project']['name'])])

        return set([])
