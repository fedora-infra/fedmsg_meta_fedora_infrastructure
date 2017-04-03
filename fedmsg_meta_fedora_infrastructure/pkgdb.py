# This file is part of fedmsg.
# Copyright (C) 2012 Red Hat, Inc.
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
#
import six

from fedmsg_meta_fedora_infrastructure import BaseProcessor
from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

from fedmsg_meta_fedora_infrastructure.conglomerators.pkgdb import \
        acls as pkgdb_acls

def get_agent(msg):
    """ Handy hack to handle legacy messages where 'agent' was a list.  """
    agent = msg['msg']['agent']
    if isinstance(agent, list):
        agent = agent[0]
    return agent


class PkgdbProcessor(BaseProcessor):
    __name__ = "Pkgdb"
    __description__ = "the Fedora Package DB"
    __link__ = "https://admin.fedoraproject.org/pkgdb"
    __docs__ = "https://fedorahosted.org/packagedb/"
    __obj__ = "Package ACL Updates"
    __icon__ = ("https://apps.fedoraproject.org/packages/"
                "images/icons/package_128x128.png")
    conglomerators = [
        pkgdb_acls.BySubject,
        pkgdb_acls.ByPackage,
        pkgdb_acls.ByAgent,
    ]

    def subtitle(self, msg, **config):
        if 'pkgdb.acl.update' in msg['topic']:
            tmpl = self._(
                u"{agent} changed {user}'s '{acl}' permission " +
                "on {namespace}/{package} ({branch}) to '{status}'"
            )
            user = msg['msg']['username']
            status = msg['msg']['status']
            namespace = msg['msg']['package_listing']['package'].get('namespace', 'rpms')
            package = msg['msg']['package_listing']['package']['name']
            acl = msg['msg']['acl']
            agent = get_agent(msg)
            branch = msg['msg']['package_listing']['collection']['branchname']
            return tmpl.format(
                agent=agent, acl=acl,
                user=user, status=status,
                package=package, branch=branch,
                namespace=namespace,
            )
        elif 'pkgdb.branch.clone' in msg['topic']:
            tmpl = self._(u"{agent} branched {namespace}/{package} {branch} from {master}")
            agent = get_agent(msg)
            namespace = msg['msg'].get('namespace', 'rpms')
            package = msg['msg']['package']
            branch = msg['msg']['branch']
            master = msg['msg']['master']
            return tmpl.format(agent=agent, package=package,
                               branch=branch, master=master,
                               namespace=namespace)
        elif 'pkgdb.package.update.status' in msg['topic']:
            tmpl = self._(u"{agent} {verb} {namespace}/{package}{extra}")
            extra = ""

            # prev_status, status and package_listing only apear in
            # pkgdb.package.update.status messages, but there are also
            # pgkdb.package.update messages
            prev_status = msg['msg'].get('prev_status')
            status = msg['msg'].get('status')
            if 'package_listing' in msg['msg']:
                branchname = msg['msg']['package_listing']['collection'][
                    'branchname']
                extra = self._(u" in {branchname}".format(
                    branchname=branchname))

            status_map = OrderedDict([
                ("Orphaned", [self._(u"unorphaned"), self._(u"orphaned")]),
                ("Retired", [self._(u"unretired"), self._(u"retired")]),
            ])
            verb = self._(u"made some updates to")
            for key, values in status_map.items():
                left, right = values
                if prev_status == key and status != key:
                    verb = left
                elif prev_status != key and status == key:
                    verb = right

            agent = get_agent(msg)

            try:
                namespace = msg['msg']['package_listing']['package'].get('namespace', 'rpms')
                package = msg['msg']['package_listing']['package']['name']
            except KeyError:
                namespace = msg['msg'].get('namespace', 'rpms')
                package = msg['msg']['package']

            return tmpl.format(agent=agent, package=package, verb=verb,
                               extra=extra, namespace=namespace)
        elif msg['topic'].endswith('pkgdb.package.update'):
            agent = get_agent(msg)

            try:
                namespace = msg['msg']['package_listing']['package'].get('namespace', 'rpms')
                package = msg['msg']['package_listing']['package']['name']
            except KeyError:
                namespace = msg['msg'].get('namespace', 'rpms')
                package = msg['msg']['package']
            if isinstance(package, dict):
                namespace = package.get('namespace', namespace)
                package = package['name']

            if 'fields' in msg['msg']:
                # New pkgdb2 style
                tmpl = self._(u"{agent} updated: {fields} of {namespace}/{package}")
                fields = ', '.join(msg['msg'].get('fields'))
                return tmpl.format(agent=agent, package=package, namespace=namespace, fields=fields)
            else:
                # old old pkgdb1 style
                tmpl = self._(u"{agent} made some updates to {namespace}/{package}")
                return tmpl.format(agent=agent, package=package, namespace=namespace)
        elif 'pkgdb.critpath.update' in msg['topic']:
            tmpl = self._(
                u"{agent} altered the critpath status for some packages")
            agent = get_agent(msg)
            return tmpl.format(agent=agent)
        elif msg['topic'].endswith('pkgdb.package.new'):
            tmpl = self._(
                u"{agent} added a new package '{namespace}/{package}' ({branch})")
            agent = get_agent(msg)
            namespace = msg['msg']['package_listing']['package'].get('namespace', 'rpms')
            package = msg['msg']['package_listing']['package']['name']
            branch = msg['msg']['package_listing']['collection']['branchname']
            return tmpl.format(agent=agent, package=package, branch=branch, namespace=namespace)
        elif 'pkgdb.acl.request.toggle' in msg['topic']:
            tmpl = self._(
                u"{agent} has {action} '{acl}' on {namespace}/{package} ({branch})"
            )
            namespace = msg['msg']['package_listing']['package'].get('namespace', 'rpms')
            package = msg['msg']['package_listing']['package']['name']
            acl = msg['msg']['acl']
            agent = get_agent(msg)
            branch = msg['msg']['package_listing']['collection']['branchname']
            action = msg['msg']['acl_action']
            return tmpl.format(
                agent=agent, acl=acl, action=action,
                package=package, branch=branch,
                namespace=namespace,
            )
        elif 'pkgdb.package.retire' in msg['topic']:
            tmpl = self._(
                u"{agent} {action} {namespace}/{package} ({branch})!"
            )
            namespace = msg['msg']['package_listing']['package'].get('namespace', 'rpms')
            package = msg['msg']['package_listing']['package']['name']
            action = msg['msg']['retirement']
            agent = get_agent(msg)
            branch = msg['msg']['package_listing']['collection']['branchname']
            return tmpl.format(
                agent=agent, action=action,
                package=package, branch=branch,
                namespace=namespace,
            )
        elif 'pkgdb.owner.update' in msg['topic']:
            tmpl = self._(
                u"{agent} changed owner of {namespace}/{package} ({branch}) to '{owner}'")

            # Owners got renamed to points of contact in packagedb2
            try:
                owner = msg['msg']['package_listing']['point_of_contact']
            except KeyError:
                owner = msg['msg']['package_listing']['owner']

            namespace = msg['msg']['package_listing']['package'].get('namespace', 'rpms')
            package = msg['msg']['package_listing']['package']['name']
            agent = get_agent(msg)
            branch = msg['msg']['package_listing']['collection']['branchname']
            return tmpl.format(
                agent=agent,
                owner=owner,
                package=package,
                branch=branch,
                namespace=namespace)
        elif 'pkgdb.acl.user.remove' in msg['topic']:
            tmpl = self._(
                u"{agent} removed {user} from {namespace}/{package} ({branches})")
            namespace = msg['msg']['package_listings'][0]['package'].get('namespace', 'rpms')
            package = msg['msg']['package_listings'][0]['package']['name']
            user = msg['msg']['username']
            agent = get_agent(msg)
            branches = ", ".join([
                p['collection']['branchname']
                for p in msg['msg']['package_listings']
            ])
            return tmpl.format(
                agent=agent,
                user=user,
                package=package,
                branches=branches,
                namespace=namespace,
            )
        elif 'pkgdb.branch.start' in msg['topic']:
            tmpl = self._(
                u"{agent} started a branch of {tobranch} from {frombranch}")
            agent = get_agent(msg)
            frombranch = msg['msg']['collection_from']['branchname']
            tobranch = msg['msg']['collection_to']['branchname']
            return tmpl.format(
                agent=agent,
                frombranch=frombranch,
                tobranch=tobranch,
            )
        elif 'pkgdb.branch.complete' in msg['topic']:
            tmpl = self._(
                u"{agent}'s branch of {tobranch} from {frombranch} completed")
            agent = get_agent(msg)
            frombranch = msg['msg']['collection_from']['branchname']
            tobranch = msg['msg']['collection_to']['branchname']
            return tmpl.format(
                agent=agent,
                frombranch=frombranch,
                tobranch=tobranch,
            )
        elif 'pkgdb.collection.new' in msg['topic']:
            tmpl = self._(
                u"{agent} created a new collection for {name} {version}")
            agent = get_agent(msg)
            name = msg['msg']['collection']['name']
            version = msg['msg']['collection']['version']
            return tmpl.format(
                agent=agent,
                name=name,
                version=version,
            )
        elif 'pkgdb.collection.update' in msg['topic']:
            tmpl = self._(
                u"{agent} updated the following fields of the "
                "{name} {version} collection: {fields}")
            agent = get_agent(msg)
            name = msg['msg']['collection']['name']
            version = msg['msg']['collection']['version']
            fields = ", ".join(msg['msg']['fields'])
            return tmpl.format(
                agent=agent,
                name=name,
                version=version,
                fields=fields,
            )
        elif 'pkgdb.package.delete' in msg['topic']:
            tmpl = self._(
                u"{agent} deleted the '{namespace}/{package}' package from the pkgdb")
            agent = get_agent(msg)
            namespace = msg['msg']['package'].get('namespace', 'rpms')
            package = msg['msg']['package']['name']
            return tmpl.format(agent=agent, package=package, namespace=namespace)
        elif 'pkgdb.package.branch.delete' in msg['topic']:
            tmpl = self._(
                u"{agent} deleted the {branch} branch "
                "of the '{namespace}/{package}' package")
            agent = get_agent(msg)
            namespace = msg['msg']['package_listing']['package'].get('namespace', 'rpms')
            package = msg['msg']['package_listing']['package']['name']
            branch = msg['msg']['package_listing']['collection']['branchname']
            return tmpl.format(agent=agent, branch=branch, package=package, namespace=namespace)
        elif msg['topic'].endswith('pkgdb.package.branch.new'):
            tmpl = self._(
                u"{agent} created the branch '{branch}' for the package "
                "'{namespace}/{package}'")
            agent = get_agent(msg)
            namespace = msg['msg']['package'].get('namespace', 'rpms')
            package = msg['msg']['package']['name']
            branch = msg['msg']['package_listing']['collection']['branchname']
            return tmpl.format(agent=agent, branch=branch, package=package, namespace=namespace)
        elif 'pkgdb.acl.delete' in msg['topic']:
            tmpl = self._(
                u"{agent} deleted {user}'s {acl} "
                "rights from {namespace}/{package} ({branch})")
            _msg = msg['msg']['acl']
            namespace = _msg['packagelist']['package'].get('namespace', 'rpms')
            package = _msg['packagelist']['package']['name']
            branch = _msg['packagelist']['collection']['branchname']
            acl = _msg['acl']
            user = _msg['fas_name']
            agent = msg['msg']['agent']
            return tmpl.format(agent=agent, user=user, acl=acl,
                               package=package, branch=branch,
                               namespace=namespace)
        elif msg['topic'].endswith('pkgdb.package.branch.request'):
            tmpl = self._(
                u"{agent} requested branch {new_branch} for package {namespace}/{package}")
            _msg = msg['msg']
            namespace = _msg['package'].get('namespace', 'rpms')
            package = _msg['package']['name']
            new_branch = _msg['collection_to']['branchname']
            agent = msg['msg']['agent']
            return tmpl.format(agent=agent, new_branch=new_branch,
                               package=package, namespace=namespace)
        elif msg['topic'].endswith('pkgdb.package.new.request'):
            tmpl = self._(
                u"{agent} requested package {namespace}/{package} on branch {branch}")
            _msg = msg['msg']
            namespace = _msg['info'].get('namespace', 'rpms')
            package = _msg['info']['pkg_name']
            branch = _msg['collection']['branchname']
            agent = msg['msg']['agent']
            return tmpl.format(agent=agent, branch=branch, package=package, namespace=namespace)
        elif msg['topic'].endswith('pkgdb.admin.action.status.update'):
            tmpl = self._(
                u"{agent} changed {owner}'s {action} "
                "for {namespace}/{package} in {branch} "
                "from {old_status} to {new_status}")
            _msg = msg['msg']

            agent = _msg['agent']
            owner = _msg['action']['user']

            branch = _msg['action']['collection']['branchname']
            try:
                namespace = _msg['action']['info'].get('namespace', 'rpms')
                package = _msg['action']['info']['pkg_name']
            except KeyError:
                namespace = _msg['action']['package'].get('namespace', 'rpms')
                package = _msg['action']['package']['name']

            action = _msg['action']['action']
            substitutes = {
                'request.package': self._('package request'),
                'request.branch': self._('branch request'),
            }
            action = substitutes.get(action, action)

            old_status = _msg['old_status']
            new_status = _msg['new_status']

            message = _msg['action'].get('message', None)
            if message:
                tmpl += self._(" with message: {message}")

            return tmpl.format(
                agent=agent, owner=owner, action=action,
                package=package, branch=branch,
                old_status=old_status, new_status=new_status, message=message,
                namespace=namespace,
            )
        elif msg['topic'].endswith('pkgdb.package.critpath.update'):
            tmpl = self._(
                u"{agent} {action} the critpath flag on the "
                "{namespace}/{package} package ({branches})")
            agent = msg['msg']['agent']
            action = ['unset', 'set'][msg['msg']['critpath']]
            namespace = msg['msg']['package'].get('namespace', 'rpms')
            package = msg['msg']['package']['name']
            branches = ', '.join(msg['msg']['branches'])
            return tmpl.format(agent=agent, action=action,
                               package=package, branches=branches,
                               namespace=namespace)
        elif msg['topic'].endswith('pkgdb.package.monitor.update'):
            tmpl = self._(
                u"{agent} set the monitor flag of {namespace}/{package} to {status}")
            agent = msg['msg']['agent']
            status = msg['msg']['status']
            namespace = msg['msg']['package'].get('namespace', 'rpms')
            package = msg['msg']['package']['name']
            return tmpl.format(agent=agent, status=status, package=package, namespace=namespace)
        elif msg['topic'].endswith('pkgdb.package.unretire.request'):
            tmpl = self._(
                u"{agent} asks that {namespace}/{package} be unretired on {branch}")
            agent = msg['msg']['agent']
            branch = msg['msg']['collection']['branchname']
            namespace = msg['msg']['package'].get('namespace', 'rpms')
            package = msg['msg']['package']['name']
            return tmpl.format(agent=agent, branch=branch, package=package, namespace=namespace)
        elif msg['topic'].endswith('pkgdb.package.koschei.update'):
            tmpl = self._(
                u"{agent} set the koschei monitoring flag of {namespace}/{package} to "
                "{status}")
            agent = msg['msg']['agent']
            status = msg['msg']['status']
            namespace = msg['msg']['package'].get('namespace', 'rpms')
            package = msg['msg']['package']['name']
            return tmpl.format(agent=agent, status=status, package=package, namespace=namespace)
        else:
            raise NotImplementedError("%r" % msg)

    def secondary_icon(self, msg, **config):
        user = None

        try:
            user = get_agent(msg)
        except KeyError:
            pass

        try:
            user = msg['msg']['username']
        except KeyError:
            pass

        if not user:
            return ""

        return avatar_url(username=user)

    def usernames(self, msg, **config):
        users = set()

        try:
            users.add(get_agent(msg))
        except KeyError:
            pass

        try:
            users.add(msg['msg']['acl']['fas_name'])
        except (KeyError, TypeError):
            pass

        try:
            users.add(msg['msg']['username'])
        except KeyError:
            pass

        if 'orphan' in users:
            users.remove('orphan')

        return users

    def objects(self, msg, **config):
        objs = set()

        _msg = msg['msg']

        if 'pkgdb.acl.update' in msg['topic']:
            objs.add('{package}/acls/{branch}/{acl}/{user}'.format(
                package=_msg['package_listing']['package']['name'],
                branch=_msg['package_listing']['collection']['branchname'],
                acl=_msg['acl'],
                user=_msg['username']
            ))
        elif msg['topic'].endswith('pkgdb.package.new'):
            objs.add('{package}/create'.format(
                package=_msg['package_listing']['package']['name'],
            ))
        elif 'pkgdb.acl.request.toggle' in msg['topic']:
            objs.add('{package}/acls/{branch}/{acl}/{user}'.format(
                package=_msg['package_listing']['package']['name'],
                branch=_msg['package_listing']['collection']['branchname'],
                acl=_msg['acl'],
                user=_msg['agent']
            ))
        elif 'pkgdb.package.retire' in msg['topic']:
            objs.add('{package}/retire'.format(
                package=_msg['package_listing']['package']['name'],
            ))
        elif 'pkgdb.acl.user.remove' in msg['topic']:
            objs.add('{package}/remove/{user}'.format(
                package=_msg['package_listings'][0]['package']['name'],
                user=_msg['username'],
            ))
        elif 'pkgdb.owner.update' in msg['topic']:
            objs.add('{package}/owner/{branch}'.format(
                package=_msg['package_listing']['package']['name'],
                branch=_msg['package_listing']['collection']['branchname'],
            ))
        elif 'pkgdb.package.update' in msg['topic']:
            try:
                package = _msg['package_listing']['package']['name']
            except KeyError:
                package = _msg['package']
            if isinstance(package, dict):
                package = package['name']
            objs.add('{package}/update'.format(package=package))
        elif 'pkgdb.branch.clone' in msg['topic']:
            objs.add('{package}/branch'.format(package=_msg['package']))
        elif 'pkgdb.package.delete' in msg['topic']:
            package = _msg['package']['name']
            objs.add('{package}/package/delete'.format(package=package))
        elif 'pkgdb.package.branch.delete' in msg['topic']:
            package = _msg['package_listing']['package']['name']
            branch = _msg['package_listing']['collection']['branchname']
            objs.add('{package}/{branch}/delete'.format(
                package=package, branch=branch))
        elif 'pkgdb.package.branch.new' in msg['topic']:
            package = _msg['package']['name']
            branch = _msg['package_listing']['collection']['branchname']
            objs.add('{package}/{branch}/new'.format(
                package=package, branch=branch))
        elif 'pkgdb.acl.delete' in msg['topic']:
            objs.add('{package}/acls/{branch}/{acl}/{user}'.format(
                package=_msg['acl']['packagelist']['package']['name'],
                branch=_msg['acl']['packagelist']['collection']['branchname'],
                acl=_msg['acl']['acl'],
                user=_msg['acl']['fas_name'],
            ))
        elif msg['topic'].endswith('pkgdb.package.branch.request'):
            objs.add('{package}/branch/request/{branch}/{user}'.format(
                package=_msg['package']['name'],
                branch=_msg['collection_to']['branchname'],
                user=_msg['agent'],
            ))
        elif msg['topic'].endswith('pkgdb.package.new.request'):
            objs.add('new/package/request/{package}/{branch}/{user}'.format(
                package=_msg['info']['pkg_name'],
                branch=_msg['collection']['branchname'],
                user=_msg['agent'],
            ))
        elif msg['topic'].endswith('pkgdb.admin.action.status.update'):
            try:
                package = _msg['action']['info']['pkg_name']
            except KeyError:
                package = _msg['action']['package']['name']
            objs.add(
                'action/{actionid}/status/{package}/{branch}/{user}'.format(
                    actionid=_msg['action']['id'],
                    package=package,
                    branch=_msg['action']['collection']['branchname'],
                    user=_msg['agent'],
                )
            )
        elif msg['topic'].endswith('pkgdb.package.critpath.update'):
            objs.add(_msg['package']['name'] + "/critpath")
        elif msg['topic'].endswith('pkgdb.package.monitor.update'):
            objs.add(
                '{package}/monitor/{status}'.format(
                package=_msg['package']['name'],
                status=str(_msg['status']).lower())
            )
        elif msg['topic'].endswith('pkgdb.package.koschei.update'):
            objs.add(
                '{package}/koschei/{status}'.format(
                package=_msg['package']['name'],
                status=str(_msg['status']).lower())
            )
        elif msg['topic'].endswith('pkgdb.package.unretire.request'):
            objs.add(
                '{package}/unretire/{branch}'.format(
                package=_msg['package']['name'],
                branch=msg['msg']['collection']['branchname'])
            )

        return objs

    def packages(self, msg, **config):
        requested_namespace = config.get('namespace', 'rpms')
        packages = set()

        try:
            package = msg['msg']['package_listing']['package']
            if 'namespace' not in package or package['namespace'] == requested_namespace:
                packages.add(package['name'])
        except KeyError:
            pass

        try:
            for package in msg['msg']['package_listings']:
                package = package['package']
                if 'namespace' not in package or package['namespace'] == requested_namespace:
                    packages.add(package['name'])
        except KeyError:
            pass

        try:
            if isinstance(msg['msg']['package'], six.string_types):
                if 'namespace' not in msg['msg'] or \
                        msg['msg']['namespace'] == requested_namespace:
                    packages.add(msg['msg']['package'])
            else:
                package = msg['msg']['package']
                if 'namespace' not in package or package['namespace'] == requested_namespace:
                    packages.add(package['name'])
        except (KeyError, TypeError):
            pass

        try:
            package = msg['msg']['acl']['packagelist']['package']
            if 'namespace' not in package or package['namespace'] == requested_namespace:
                packages.add(package['name'])
        except (KeyError, TypeError):
            pass

        try:
            if 'pkg_namespace' not in msg['msg']['info'] or  \
                    msg['msg']['info']['pkg_namespace'] == requested_namespace:
                packages.add(msg['msg']['info']['pkg_name'])
        except (KeyError, TypeError):
            pass

        try:
            if 'pkg_namespace' not in msg['msg']['action']['info'] or  \
                    msg['msg']['info']['action']['pkg_namespace'] == requested_namespace:
                packages.add(msg['msg']['action']['info']['pkg_name'])
        except (KeyError, TypeError):
            pass

        try:
            if 'namespace' not in msg['msg']['action']['package'] or  \
                    msg['msg']['action']['package']['namespace'] == requested_namespace:
                packages.add(msg['msg']['action']['package']['name'])
        except (KeyError, TypeError):
            pass

        return packages

    def link(self, msg, **config):
        tmpl = "https://admin.fedoraproject.org/pkgdb/package/{namespace}/{package}/"

        if any(map(msg['topic'].__contains__, [
            'pkgdb.package.new.request',
        ])):
            return tmpl.format(
                namespace=msg['msg']['info'].get('namespace', 'rpms'),
                package=msg['msg']['info']['pkg_name'],
            )


        if any(map(msg['topic'].__contains__, [
            'pkgdb.admin.action.status.update',
        ])):
            try:
                namespace = msg['msg']['action']['info'].get('namespace', 'rpms')
                package = msg['msg']['action']['info']['pkg_name']
            except KeyError:
                namespace = msg['msg']['action']['package'].get('namespace', 'rpms')
                package = msg['msg']['action']['package']['name']
            return tmpl.format(namespace=namespace, package=package)

        if any(map(msg['topic'].__contains__, [
            'pkgdb.acl.update',
            'pkgdb.acl.request.toggle',
            'pkgdb.owner.update',
            'pkgdb.package.retire',
            'pkgdb.package.new',
            'pkgdb.package.branch.new',
        ])):
            return tmpl.format(
                namespace=msg['msg']['package_listing']['package'].get('namespace', 'rpms'),
                package=msg['msg']['package_listing']['package']['name'],
            )

        if any(map(msg['topic'].__contains__, [
            'pkgdb.acl.user.remove',
        ])):
            return tmpl.format(
                namespace=msg['msg']['package_listings'][0]['package'].get('namespace', 'rpms'),
                package=msg['msg']['package_listings'][0]['package']['name']
            )

        if any(map(msg['topic'].__contains__, [
            'pkgdb.package.update',
            'pkgdb.branch.clone',
            'package.branch.request',
        ])):
            try:
                namespace = msg['msg']['package_listing']['package'].get('namespace', 'rpms')
                package = msg['msg']['package_listing']['package']['name']
            except KeyError:
                namespace = msg['msg'].get('namespace', 'rpms')
                package = msg['msg']['package']
            if isinstance(package, dict):
                namespace = package.get('namespace', namespace)
                package = package['name']
            return tmpl.format(namespace=namespace, package=package)

        return ""
