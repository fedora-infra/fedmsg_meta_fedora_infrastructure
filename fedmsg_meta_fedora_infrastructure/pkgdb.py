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
                "on {package} to '{status}'"
            )
            user = msg['msg']['username']
            status = msg['msg']['status']
            package = msg['msg']['package_listing']['package']['name']
            acl = msg['msg']['acl']
            agent = msg['msg']['agent']
            return tmpl.format(
                agent=agent, acl=acl,
                user=user, status=status,
                package=package)
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
        users = []

        try:
            users.append(msg['msg']['agent'])
        except KeyError:
            pass

        try:
            users.append(msg['msg']['package_listing']['owner'])
        except KeyError:
            pass

        try:
            users.append(msg['msg']['username'])
        except KeyError:
            pass

        return set(users)

    def objects(self, msg, **config):
        objs = set()

        if 'pkgdb.acl.update' in msg['topic']:
            objs.add('acls/{package}/{acl}/{user}'.format(
                package=msg['msg']['package_listing']['package']['name'],
                acl=msg['msg']['acl'],
                user=msg['msg']['username']
            ))

        return objs

    def packages(self, msg, **config):
        if 'pkgdb.acl.update' in msg['topic']:
            return set([msg['msg']['package_listing']['package']['name']])

        return set()

    def link(self, msg, **config):
        tmpl = "https://admin.fedoraproject.org/pkgdb/acls/name/{package}"

        if 'pkgdb.acl.update' in msg['topic']:
            return tmpl.format(
                package=msg['msg']['package_listing']['package']['name']
            )

        return ""
