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
            agent = get_agent(msg)
            branch = msg['msg']['package_listing']['collection']['branchname']
            return tmpl.format(
                agent=agent, acl=acl,
                user=user, status=status,
                package=package, branch=branch)
        elif 'pkgdb.branch.clone' in msg['topic']:
            tmpl = self._(u"{agent} branched {package} {branch} from {master}")
            agent = get_agent(msg)
            package = msg['msg']['package']
            branch = msg['msg']['branch']
            master = msg['msg']['master']
            return tmpl.format(agent=agent, package=package,
                               branch=branch, master=master)
        elif 'pkgdb.package.update.status' in msg['topic']:
            tmpl = self._(u"{agent} {verb} {package}{extra}")
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
            if prev_status == "Retired" and status != "Retired":
                verb = self._(u"unretired")
            elif prev_status != "Retired" and status == "Retired":
                verb = self._(u"retired")
            else:
                verb = self._(u"made some updates to")
            agent = get_agent(msg)
            try:
                package = msg['msg']['package_listing']['package']['name']
            except KeyError:
                package = msg['msg']['package']

            return tmpl.format(agent=agent, package=package, verb=verb,
                               extra=extra)
        elif msg['topic'].endswith('pkgdb.package.update'):
            agent = get_agent(msg)

            try:
                package = msg['msg']['package_listing']['package']['name']
            except KeyError:
                package = msg['msg']['package']
            if isinstance(package, dict):
                package = package['name']

            if 'fields' in msg['msg']:
                # New pkgdb2 style
                tmpl = self._(u"{agent} updated: {fields} of {package}")
                fields = ', '.join(msg['msg'].get('fields'))
                return tmpl.format(agent=agent, package=package, fields=fields)
            else:
                # old old pkgdb1 style
                tmpl = self._(u"{agent} made some updates to {package}")
                return tmpl.format(agent=agent, package=package)
        elif 'pkgdb.critpath.update' in msg['topic']:
            tmpl = self._(
                u"{agent} altered the critpath status for some packages")
            agent = get_agent(msg)
            return tmpl.format(agent=agent)
        elif 'pkgdb.package.new' in msg['topic']:
            tmpl = self._(
                u"{agent} added a new package '{package}' ({branch})")
            agent = get_agent(msg)
            package = msg['msg']['package_listing']['package']['name']
            branch = msg['msg']['package_listing']['collection']['branchname']
            return tmpl.format(agent=agent, package=package, branch=branch)
        elif 'pkgdb.acl.request.toggle' in msg['topic']:
            tmpl = self._(
                u"{agent} has {action} '{acl}' on {package} ({branch})"
            )
            package = msg['msg']['package_listing']['package']['name']
            acl = msg['msg']['acl']
            agent = get_agent(msg)
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
            agent = get_agent(msg)
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
            agent = get_agent(msg)
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
            agent = get_agent(msg)
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

        return gravatar_url(username=user)

    def usernames(self, msg, **config):
        users = set()

        try:
            users.add(get_agent(msg))
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
            if isinstance(package, dict):
                package = package['name']
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
            else:
                packages.add(msg['msg']['package']['name'])
        except KeyError:
            pass

        return packages

    def link(self, msg, **config):
        tmpl = "https://admin.fedoraproject.org/pkgdb/package/{package}/"

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
            if isinstance(package, dict):
                package = package['name']
            return tmpl.format(package=package)

        return ""
