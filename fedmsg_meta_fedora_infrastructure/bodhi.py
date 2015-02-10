# This file is part of fedmsg.
# Copyright (C) 2012-2014 Red Hat, Inc.
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

import re

from fedmsg_meta_fedora_infrastructure import BaseProcessor
from fasshim import gravatar_url

import conglomerators.bodhi.requests
import conglomerators.bodhi.comments


def get_sync_product(msg):
    # Extract the product name from a ftpsync message.
    product = msg['topic'].split('.')[-2]
    if product == 'fedora':
        product = 'Fedora'
    elif product == 'epel':
        product = 'EPEL'
    else:
        pass
    return product


def is_ftp_sync(msg):
    return 'bodhi.updates.' in msg['topic'] and msg['topic'].endswith('.sync')


def author_link(username):
    return "<a href='https://admin.fedoraproject.org/updates/" + \
        "user/{user}'>{user}</a>".format(user=username)


def update_link(title):
    return "<a href='https://admin.fedoraproject.org/updates/" + \
        "{title}'>{title}</a>".format(title=title)


class BodhiProcessor(BaseProcessor):
    __name__ = "Bodhi"
    __description__ = "the Fedora update system"
    __link__ = "https://admin.fedoraproject.org/updates"
    __docs__ = "https://fedoraproject.org/wiki/Bodhi"
    __obj__ = "Package Updates"
    __icon__ = ("https://admin.fedoraproject.org/updates"
                "/static/images/bodhi-icon-48.png")
    conglomerators = [
        conglomerators.bodhi.requests.ByUserAndPackageTesting,
        conglomerators.bodhi.requests.ByUserAndPackageStable,
        conglomerators.bodhi.requests.ByPackage,
        conglomerators.bodhi.requests.ByUser,
        conglomerators.bodhi.comments.ByUpdate,
        conglomerators.bodhi.comments.ByUser,
    ]

    def _u2p(self, update):
        """ Take an update, and return the package name """
        # TODO -- make this unnecessary by having bodhi emit the
        # package name (and not just the update name) to begin with.
        return [build.rsplit('-', 2)[0] for build in update.split(',')]

    def secondary_icon(self, msg, **config):
        username = ''
        if 'bodhi.update.comment' in msg['topic']:
            username = msg['msg']['comment']['author']
        elif 'bodhi.buildroot_override' in msg['topic']:
            username = msg['msg']['override']['submitter']
        elif 'bodhi.stack' in msg['topic']:
            username = msg['msg']['agent']
        elif 'update' in msg['msg'] and 'submitter' in msg['msg']['update']:
            username = msg['msg']['update']['submitter']
        else:
            username = msg['msg'].get('agent')

        if isinstance(username, dict):
            username = username['name']

        gravatar = ''
        if username:
            gravatar = gravatar_url(username)
        return gravatar

    def subtitle(self, msg, **config):
        markup = config.get('markup', False)

        if is_ftp_sync(msg):
            product = get_sync_product(msg)
            msg = msg['msg']
            tmpl = self._(
                'New {product} {release} {repo} content synced out '
                '({bytes} changed with {deleted} files deleted)')
            return tmpl.format(product=product, **msg)
        elif 'bodhi.update.comment' in msg['topic']:
            author = msg['msg']['comment']['author']
            karma = msg['msg']['comment']['karma']
            title = msg['msg']['comment']['update_title']

            if len(title) >= 35:
                title = title[:35] + '...'

            tmpl = self._(
                "{author} commented on bodhi update {title} (karma: {karma})"
            )
            if not markup:
                return tmpl.format(author=author, karma=karma, title=title)
            else:
                return tmpl.format(
                    author=author_link(author),
                    title=update_link(title),
                    karma=karma,
                )

        elif 'bodhi.update.complete.' in msg['topic']:
            author = msg['msg']['update']['submitter']
            if isinstance(author, dict):
                author = author['name']
            package = msg['msg']['update']['title']
            status = msg['msg']['update']['status']
            tmpl = self._(
                "{author}'s {package} bodhi update completed push to {status}"
            )
            return tmpl.format(author=author, package=package, status=status)
        elif 'bodhi.update.eject' in msg['topic']:
            author = msg['msg']['update']['submitter']
            if isinstance(author, dict):
                author = author['name']
            package = msg['msg']['update']['title']
            repo = msg['msg']['repo']
            reason = msg['msg']['reason']
            tmpl = self._(
                "{author}'s {package} bodhi update was ejected from "
                "the {repo} mash.  Reason: \"{reason}\"")
            return tmpl.format(author=author, package=package,
                               repo=repo, reason=reason)
        elif 'bodhi.update.edit' in msg['topic']:
            author = msg['msg']['agent']
            update = msg['msg']['update']['title']
            tmpl = self._("{author} edited {update}")
            return tmpl.format(author=author, update=update)
        elif 'bodhi.update.request' in msg['topic']:
            status = msg['topic'].split('.')[-1]
            author = msg['msg'].get('agent')
            title = msg['msg']['update']['title']
            if status in ('unpush', 'obsolete', 'revoke'):
                # make our status past-tense
                status = status + (status[-1] == 'e' and 'd' or 'ed')
                tmpl = self._("{author} {status} {title}")
            else:
                tmpl = self._("{author} submitted {title} to {status}")

            if not markup:
                return tmpl.format(author=author, title=title, status=status)
            else:
                return tmpl.format(
                    author=author_link(author),
                    title=update_link(title),
                    status=status,
                )
        elif 'bodhi.mashtask.mashing' in msg['topic']:
            repo = msg['msg'].get('repo')
            tmpl = self._("bodhi masher started mashing {repo}")
            return tmpl.format(repo=repo)
        elif 'bodhi.mashtask.start' in msg['topic']:
            return self._("bodhi masher started a push")
        elif 'bodhi.mashtask.complete' in msg['topic']:
            success = msg['msg']['success']
            if success:
                tmpl = self._("bodhi masher successfully mashed {repo}")
            else:
                tmpl = self._("bodhi masher failed to mash {repo}")
            return tmpl.format(repo=msg['msg'].get('repo'))
        elif 'bodhi.mashtask.sync.wait' in msg['topic']:
            return self._("bodhi masher is waiting for {repo} to "
                          "hit the master mirror").format(
                              repo=msg['msg'].get('repo'))
        elif 'bodhi.mashtask.sync.done' in msg['topic']:
            return self._("bodhi masher finished waiting for {repo} to "
                          "hit the master mirror").format(
                              repo=msg['msg'].get('repo'))
        elif 'bodhi.buildroot_override.tag' in msg['topic']:
            tmpl = self._("{submitter} submitted a buildroot override " +
                          "for {build}")

            submitter = msg['msg']['override']['submitter']
            build = msg['msg']['override']['build']

            if isinstance(submitter, dict):
                submitter = submitter['name']
            if isinstance(build, dict):
                build = build['nvr']

            if markup:
                return tmpl.format(submitter=author_link(submitter),
                                   build=build)
            else:
                return tmpl.format(submitter=submitter, build=build)
        elif 'bodhi.buildroot_override.untag' in msg['topic']:
            tmpl = self._("{submitter} expired a buildroot override " +
                          "for {build}")

            submitter = msg['msg']['override']['submitter']
            build = msg['msg']['override']['build']

            if isinstance(submitter, dict):
                submitter = submitter['name']
            if isinstance(build, dict):
                build = build['nvr']

            if markup:
                return tmpl.format(submitter=author_link(submitter),
                                   build=build)
            else:
                return tmpl.format(submitter=submitter, build=build)
        elif 'bodhi.stack.save' in msg['topic']:
            tmpl = self._("{agent} updated the \"{name}\" stack")
            agent = msg['msg']['agent']
            name = msg['msg']['stack']['name']
            return tmpl.format(agent=agent, name=name)
        elif 'bodhi.stack.delete' in msg['topic']:
            tmpl = self._("{agent} deleted the \"{name}\" stack")
            agent = msg['msg']['agent']
            name = msg['msg']['stack']['name']
            return tmpl.format(agent=agent, name=name)
        else:
            raise NotImplementedError("%r" % msg)

    def link(self, msg, **config):
        prefix = 'https://admin.fedoraproject.org'
        tmpl = prefix + "/updates/{title}"
        if 'bodhi.update.comment' in msg['topic']:
            return tmpl.format(title=msg['msg']['comment']['update_title'])
        elif 'bodhi.update.complete' in msg['topic']:
            return tmpl.format(title=msg['msg']['update']['title'])
        elif 'bodhi.update.request' in msg['topic']:
            return tmpl.format(title=msg['msg']['update']['title'])
        elif 'bodhi.update.edit' in msg['topic']:
            return tmpl.format(title=msg['msg']['update']['title'])
        elif 'bodhi.update.eject' in msg['topic']:
            return tmpl.format(title=msg['msg']['update']['title'])
        elif 'bodhi.stack' in msg['topic']:
            return prefix + "/updates/stacks/{title}".format(
                title=msg['msg']['stack']['name'])
        elif is_ftp_sync(msg):
            link = "https://download.fedoraproject.org/pub/"
            repo = msg['msg']['repo']
            product = get_sync_product(msg).lower()
            link += product + "/"

            if product == 'fedora':
                if repo == 'atomic':
                    link += "linux/atomic/"
                else:
                    link += "linux/updates/"

            if repo.endswith('testing'):
                link += "testing/"

            link += msg['msg']['release'] + "/"
            return link

    def packages(self, msg, **config):
        if 'bodhi.update.comment' in msg['topic']:
            return set(self._u2p(msg['msg']['comment']['update_title']))
        elif 'bodhi.update.complete' in msg['topic']:
            return set(self._u2p(msg['msg']['update']['title']))
        elif 'bodhi.update.request' in msg['topic']:
            return set(self._u2p(msg['msg']['update']['title']))
        elif 'bodhi.update.edit' in msg['topic']:
            return set(self._u2p(msg['msg']['update']['title']))
        elif 'bodhi.update.eject' in msg['topic']:
            return set(self._u2p(msg['msg']['update']['title']))
        elif 'bodhi.buildroot_override.' in msg['topic']:
            nvr = msg['msg']['override']['build']
            if isinstance(nvr, dict):
                nvr = nvr['nvr']
            return set(self._u2p(nvr))
        elif 'bodhi.stack' in msg['topic']:
            return set([p['name'] for p in msg['msg']['stack']['packages']])

        return set()

    def usernames(self, msg, **config):
        users = []

        for obj in ['update', 'override']:
            try:
                username = msg['msg'][obj]['submitter']
                if isinstance(username, dict):
                    username = username['name']
                users.append(username)
            except KeyError:
                pass

        try:
            users.append(msg['msg']['comment']['author'])
        except KeyError:
            pass

        if 'comment' in msg['msg']:
            text = msg['msg']['comment']['text']
            mentions = re.findall('@\w+', text)
            for mention in mentions:
                users.append(mention[1:])

        if 'agent' in msg['msg']:
            users.append(msg['msg']['agent'])

        return set(users)

    def objects(self, msg, **config):
        if is_ftp_sync(msg):
            product = get_sync_product(msg).lower()
            msg = msg['msg']
            return set(['/'.join([product, msg['repo'], msg['release']])])
        elif 'bodhi.mashtask.mashing' in msg['topic']:
            return set(['repos/' + msg['msg'].get('repo')])
        elif 'bodhi.update.comment' in msg['topic']:
            return set([
                'packages/' + p for p in
                self._u2p(msg['msg']['comment']['update_title'])
            ])
        elif 'bodhi.update.complete' in msg['topic']:
            return set([
                'packages/' + p for p in
                self._u2p(msg['msg']['update']['title'])
            ])
        elif 'bodhi.update.request' in msg['topic']:
            return set([
                'packages/' + p for p in
                self._u2p(msg['msg']['update']['title'])
            ])
        elif 'bodhi.update.edit' in msg['topic']:
            return set([
                'packages/' + p for p in
                self._u2p(msg['msg']['update']['title'])
            ])
        elif 'bodhi.update.eject' in msg['topic']:
            return set([
                'packages/' + p for p in
                self._u2p(msg['msg']['update']['title'])
            ])
        elif 'bodhi.buildroot_override.' in msg['topic']:
            nvr = msg['msg']['override']['build']
            if isinstance(nvr, dict):
                nvr = nvr['nvr']
            return set([
                'packages/' + p for p in
                self._u2p(nvr)
            ])
        elif 'bodhi.stack' in msg['topic']:
            return set(
                [
                    'packages/' + p['name']
                    for p in msg['msg']['stack']['packages']
                ] + ['stacks/' + msg['msg']['stack']['name']]
            )

        return set()
