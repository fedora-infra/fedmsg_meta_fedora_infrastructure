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
from fedmsg.meta.base import BaseProcessor
from fasshim import gravatar_url


class PkgdbProcessor(BaseProcessor):
    __name__ = "Pkgdb"
    __description__ = "the Fedora Package DB"
    __link__ = "https://admin.fedoraproject.org/pkgdb"
    __docs__ = "https://fedorahosted.org/packagedb/"
    __obj__ = "Package ACL Updates"
    __icon__ = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"

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
        elif 'pkgdb.owner.update' in msg['topic']:
            tmpl = self._(
                u"{agent} changed owner of {package} ({branch}) to '{owner}'")
            owner = msg['msg']['package_listing']['owner']
            package = msg['msg']['package_listing']['package']['name']
            agent = msg['msg']['agent']
            branch = msg['msg']['package_listing']['collection']['branchname']
            return tmpl.format(
                agent=agent,
                owner=owner,
                package=package,
                branch=branch)
        else:
            raise NotImplementedError

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

        if 'pkgdb.acl.update' in msg['topic']:
            objs.add('acls/{package}/{acl}/{user}'.format(
                package=msg['msg']['package_listing']['package']['name'],
                acl=msg['msg']['acl'],
                user=msg['msg']['username']
            ))

        if 'pkgdb.owner.update' in msg['topic']:
            objs.add('{package}/owner/{branch}'.format(
                package=msg['msg']['package_listing']['package']['name'],
                branch=msg['msg']['package_listing']['collection']['branchname'],
            ))

        return objs

    def packages(self, msg, **config):
        packages = set()

        try:
            packages.add(msg['msg']['package_listing']['package']['name'])
        except KeyError:
            pass

        return packages

    def link(self, msg, **config):
        tmpl = "https://admin.fedoraproject.org/pkgdb/acls/name/{package}"

        if any(map(msg['topic'].__contains__, [
            'pkgdb.acl.update',
            'pkgdb.owner.update',
        ])):
            return tmpl.format(
                package=msg['msg']['package_listing']['package']['name']
            )

        return ""
