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
from fedmsg_meta_fedora_infrastructure import BaseProcessor
from fasshim import gravatar_url


class PkgdbProcessor(BaseProcessor):
    __name__ = "Pkgdb"
    __description__ = "the Fedora Package DB"
    __link__ = "https://admin.fedoraproject.org/pkgdb"
    __docs__ = "https://fedorahosted.org/packagedb/"
    __obj__ = "Package ACL Updates"
    __icon__ = ("https://apps.fedoraproject.org/packages/"
               "images/icons/package_128x128.png")

    def subtitle(self, msg, **config):
        if 'pkgdb.acl.update' in msg['topic']:
            tmpl = self._(
                u"{agent} changed {user}'s '{acl}' permission " +
                "on {package} ({branch}) to '{status}'"
            )
            user = msg['msg']['username']
            status = msg['msg']['status']
            package = msg['msg']['package_listing']['package']['name']
            acl = msg['msg']['acl']
            agent = msg['msg']['agent']
            branch = msg['msg']['package_listing']['collection']['branchname']
            return tmpl.format(
                agent=agent, acl=acl,
                user=user, status=status,
                package=package, branch=branch)
        elif 'pkgdb.branch.clone' in msg['topic']:
            tmpl = self._(u"{agent} branched {package} {branch} from {master}")
            agent = msg['msg']['agent']
            package = msg['msg']['package']
            branch = msg['msg']['branch']
            master = msg['msg']['master']
            return tmpl.format(agent=agent, package=package,
                               branch=branch, master=master)
        elif 'pkgdb.package.update' in msg['topic']:
            tmpl = self._(u"{agent} made some updates to {package}")
            agent = msg['msg']['agent']
            try:
                package = msg['msg']['package_listing']['package']['name']
            except KeyError:
                package = msg['msg']['package']

            return tmpl.format(agent=agent, package=package)
        elif 'pkgdb.critpath.update' in msg['topic']:
            tmpl = self._(
                u"{agent} altered the critpath status for some packages")
            agent = msg['msg']['agent']
            return tmpl.format(agent=agent)
        elif 'pkgdb.package.new' in msg['topic']:
            tmpl = self._(
                u"{agent} added a new package '{package}' ({branch})")
            agent = msg['msg']['agent']
            package = msg['msg']['package_listing']['package']['name']
            branch = msg['msg']['package_listing']['collection']['branchname']
            return tmpl.format(agent=agent, package=package, branch=branch)
        elif 'pkgdb.acl.request.toggle' in msg['topic']:
            tmpl = self._(
                u"{agent} has {action} '{acl}' on {package} ({branch})"
            )
            package = msg['msg']['package_listing']['package']['name']
            acl = msg['msg']['acl']
            agent = msg['msg']['agent']
            branch = msg['msg']['package_listing']['collection']['branchname']
            action = msg['msg']['acl_action']
            return tmpl.format(
                agent=agent, acl=acl, action=action,
                package=package, branch=branch)
        elif 'pkgdb.package.retire' in msg['topic']:
            tmpl = self._(
                u"{agent} {action} {package} ({branch})!"
            )
            package = msg['msg']['package_listing']['package']['name']
            action = msg['msg']['retirement']
            agent = msg['msg']['agent']
            branch = msg['msg']['package_listing']['collection']['branchname']
            return tmpl.format(
                agent=agent, action=action,
                package=package, branch=branch)
        elif 'pkgdb.owner.update' in msg['topic']:
            tmpl = self._(
                u"{agent} changed owner of {package} ({branch}) to '{owner}'")

            # Owners got renamed to points of contact in packagedb2
            try:
                owner = msg['msg']['package_listing']['point_of_contact']
            except KeyError:
                owner = msg['msg']['package_listing']['owner']

            package = msg['msg']['package_listing']['package']['name']
            agent = msg['msg']['agent']
            branch = msg['msg']['package_listing']['collection']['branchname']
            return tmpl.format(
                agent=agent,
                owner=owner,
                package=package,
                branch=branch)
        elif 'pkgdb.acl.user.remove' in msg['topic']:
            tmpl = self._(
                u"{agent} removed {user} from {package} ({branches})")
            package = msg['msg']['package_listings'][0]['package']['name']
            user = msg['msg']['username']
            agent = msg['msg']['agent']
            branches = ", ".join([
                p['collection']['branchname']
                for p in msg['msg']['package_listings']
            ])
            return tmpl.format(
                agent=agent,
                user=user,
                package=package,
                branches=branches)
        elif 'pkgdb.branch.start' in msg['topic']:
            tmpl = self._(
                u"{agent} started a branch of {tobranch} from {frombranch}")
            agent = msg['msg']['agent']
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
            agent = msg['msg']['agent']
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
            agent = msg['msg']['agent']
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
            agent = msg['msg']['agent']
            name = msg['msg']['collection']['name']
            version = msg['msg']['collection']['version']
            fields = ", ".join(msg['msg']['fields'])
            return tmpl.format(
                agent=agent,
                name=name,
                version=version,
                fields=fields,
            )
        else:
            raise NotImplementedError("%r" % msg)

    def secondary_icon(self, msg, **config):
        user = None

        try:
            user = msg['msg']['agent']
        except KeyError:
            pass

        try:
            user = msg['msg']['username']
        except KeyError:
            pass

        if not user:
            return ""

        return gravatar_url(username=user)

    def usernames(self, msg, **config):
        users = set()

        try:
            users.add(msg['msg']['agent'])
        except KeyError:
            pass

        try:
            users.add(msg['msg']['package_listing']['point_of_contact'])
        except KeyError:
            pass

        try:
            users.add(msg['msg']['package_listing']['owner'])
        except KeyError:
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
        elif 'pkgdb.package.new' in msg['topic']:
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
            objs.add('{package}/update'.format(package=package))
        elif 'pkgdb.branch.clone' in msg['topic']:
            objs.add('{package}/branch'.format(package=_msg['package']))

        return objs

    def packages(self, msg, **config):
        packages = set()

        try:
            packages.add(msg['msg']['package_listing']['package']['name'])
        except KeyError:
            pass

        try:
            for package in msg['msg']['package_listings']:
                packages.add(package['package']['name'])
        except KeyError:
            pass

        try:
            if isinstance(msg['msg']['package'], basestring):
                packages.add(msg['msg']['package'])
        except KeyError:
            pass

        return packages

    def link(self, msg, **config):
        tmpl = "https://admin.fedoraproject.org/pkgdb/acls/name/{package}"

        if any(map(msg['topic'].__contains__, [
            'pkgdb.acl.update',
            'pkgdb.acl.request.toggle',
            'pkgdb.owner.update',
            'pkgdb.package.retire',
            'pkgdb.package.new',
        ])):
            return tmpl.format(
                package=msg['msg']['package_listing']['package']['name']
            )

        if any(map(msg['topic'].__contains__, [
            'pkgdb.acl.user.remove',
        ])):
            return tmpl.format(
                package=msg['msg']['package_listings'][0]['package']['name']
            )

        if any(map(msg['topic'].__contains__, [
            'pkgdb.package.update',
            'pkgdb.branch.clone',
        ])):
            try:
                package = msg['msg']['package_listing']['package']['name']
            except KeyError:
                package = msg['msg']['package']
            return tmpl.format(package=package)

        return ""
