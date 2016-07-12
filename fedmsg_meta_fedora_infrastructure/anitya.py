# This file is part of fedmsg.
# Copyright (C) 2013, 2014 Red Hat, Inc.
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
#           Pierre-Yves Chibon <pingou@pingoured.fr>
#

from fedmsg_meta_fedora_infrastructure.fasshim import \
        avatar_url, avatar_url_from_email, email2fas
from fedmsg_meta_fedora_infrastructure import BaseProcessor
import fedmsg.meta.base

class AnityaProcessor(BaseProcessor):
    topic_prefix_re = 'org\\.release-monitoring\\.(dev|stg|prod)'

    __name__ = "anitya"
    __description__ = "Upstream Release Monitoring"
    __link__ = "https://release-monitoring.org"
    __docs__ = "https://github.com/fedora-infra/anitya"
    __obj__ = "Upstream Releases"
    __icon__ = ("https://apps.fedoraproject.org/packages/"
                "images/icons/package_128x128.png")

    def _get_user(self, msg, **config):
        try:
            agent = msg['msg']['message']['agent']
        except KeyError:
            return msg.get('username', 'anitya')
        else:
            if 'id.fedoraproject.org' in agent:
                agent = agent.partition(
                    '.id.fedoraproject.org')[0].partition('//')[-1]
                return agent
            elif agent.endswith('@fedoraproject.org'):
                return agent.split('@fedoraproject.org')[0]
            elif '@' in agent:
                return email2fas(agent, **config)
            else:
                return agent

    def link(self, msg, **config):
        if msg['msg']['project']:
            proj = msg['msg']['project']['id']
            return "https://release-monitoring.org/project/%s/" % proj
        elif msg['topic'].endswith('project.flag.set'):
            return "https://release-monitoring.org/"
        else:
            return "https://release-monitoring.org/distros"

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
                '{user} added the distro named "{distro}" to anitya')
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
                          '"{project}" to anitya '
                          '(but it already exists there)')
            return tmpl.format(user=user, project=project)
        elif 'project.add' in msg['topic']:
            project = msg['msg']['project']['name']
            tmpl = self._('{user} added the project "{project}" to anitya')
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
        elif 'project.map.remove' in msg['topic']:
            project = msg['msg']['project']['name']
            distro = msg['msg']['message']['distro']
            tmpl = self._(
                '{user} deleted the mapping of "{project}" project '
                'on "{distro}"')
            return tmpl.format(user=user, project=project, distro=distro)
        elif 'project.version.update' in msg['topic']:
            project = msg['msg']['project']['name']

            if 'message' in msg['msg']:
                message = msg['msg']['message']
            else:
                message = msg['msg']

            # If this project is mapped to one or more Fedora package,
            # then just add the mapped packages to make
            # everyone's emails more readable.
            # https://github.com/fedora-infra/the-new-hotness/issues/21
            packages = []
            for package in message.get('packages', []):
                if package['distro'] == 'Fedora':
                    packages.append(package['package_name'])
            packages = fedmsg.meta.base.BaseConglomerator.list_to_series(
                packages)
            odd = message.get('odd_change', False)
            old = message['old_version']
            new = message['upstream_version']
            tmpl = self._(
                'A new version of "{project}" has been detected:  '
                '"{new}", packaged as "{packages}"')
            if old and not odd:
                tmpl = self._(
                    'A new version of "{project}" has been detected:  '
                    '"{new}" newer than "{old}", packaged as "{packages}"')

            return tmpl.format(project=project, new=new, old=old, packages=packages)
        elif 'project.version.remove' in msg['topic']:
            project = msg['msg']['project']['name']
            version = msg['msg']['message']['version']
            tmpl = self._(
                '{user} deleted the version {version} of "{project}"')
            return tmpl.format(user=user, project=project, version=version)
        elif 'distro.remove' in msg['topic']:
            project = msg['msg']['distro']['name']
            tmpl = self._(
                '{user} deleted the distro "{project}"')
            return tmpl.format(user=user, project=project)
        elif msg['topic'].endswith('project.flag.set'):
            action = msg['msg']['message']['state']
            flagid = msg['msg']['message']['flag']
            tmpl = self._(
                '{user} {action} flag "{flagid}"')
            return tmpl.format(user=user, action=action, flagid=flagid)
        elif msg['topic'].endswith('project.flag'):
            project = msg['msg']['project']['name']
            tmpl = self._(
                '{user} flagged the project "{project}"')
            return tmpl.format(user=user, project=project)
        else:
            pass

    def secondary_icon(self, msg, **config):
        username = self._get_user(msg, **config)
        packages = self.packages(msg, **config)
        if username:
            if '@' in username:
                return avatar_url_from_email(username)
            else:
                return avatar_url(username)
        elif packages:
            tmpl = 'https://apps.fedoraproject.org/packages/' + \
                'images/icons/%s.png'
            return tmpl % list(packages)[0]
        else:
            return None

    def usernames(self, msg, **config):
        username = self._get_user(msg, **config)
        if username and '@' not in username:
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
        elif 'project.version.remove' in msg['topic']:
            return set(['projects/%s' % msg['msg']['project']['name']])
        elif 'project.remove' in msg['topic']:
            return set(['projects/%s' % msg['msg']['project']['name']])
        elif 'project.map.remove' in msg['topic']:
            return set(['projects/%s' % msg['msg']['project']['name']])
        elif 'project.version.update' in msg['topic']:
            return set(['projects/%s' % msg['msg']['project']['name']])
        elif 'project.edit' in msg['topic']:
            return set(['projects/%s' % msg['msg']['project']['name']])
        elif 'project.add.tried' in msg['topic']:
            return set(['projects/%s' % msg['msg']['project']['name']])
        elif 'project.add' in msg['topic']:
            return set(['projects/%s' % msg['msg']['project']['name']])
        elif msg['topic'].endswith('project.flag'):
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
        elif 'distro.remove' in msg['topic']:
            distro = msg['msg']['distro']['name']
            return set(['distros/%s' % distro])
        elif msg['topic'].endswith('project.flag.set'):
            flagid = msg['msg']['message']['flag']
            return set(['flag/%s' % flagid])

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
            if 'message' in msg['msg']:
                packages = msg['msg']['message']['packages']
            else:
                packages = msg['msg']['packages']
            return set([
                pkg['package_name']
                for pkg in packages
                if pkg['distro'].lower() == 'fedora'
            ])
        elif msg['topic'].endswith('project.flag'):
            packages = msg['msg'].get('packages', [])
            return set([
                pkg['package_name']
                for pkg in packages
                if pkg['distro'].lower() == 'fedora'
            ])

        return set([])
