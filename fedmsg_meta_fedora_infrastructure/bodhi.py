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
#           Luke Macken <lmacken@redhat.com>

import re

from fedmsg_meta_fedora_infrastructure import BaseProcessor
from fasshim import gravatar_url


def _u2p(update):
    """ Take an update, and return the package name """
    # TODO -- make this unnecessary by having bodhi emit the
    # package name (and not just the update name) to begin with.
    return [build.rsplit('-', 2)[0] for build in update.split(',')]


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

    def secondary_icon(self, msg, **config):
        username = ''
        if 'bodhi.update.comment' in msg['topic']:
            username = msg['msg']['comment']['author']
        elif 'bodhi.buildroot_override' in msg['topic']:
            username = msg['msg']['override']['submitter']
        else:
            username = msg['msg'].get('update', {}).get('submitter')
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
            package = msg['msg']['update']['title']
            status = msg['msg']['update']['status']
            tmpl = self._(
                "{author}'s {package} bodhi update completed push to {status}"
            )
            return tmpl.format(author=author, package=package, status=status)
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
            repo = msg['msg']['repo']
            tmpl = self._("bodhi masher is mashing {repo}")
            return tmpl.format(repo=repo)
        elif 'bodhi.mashtask.start' in msg['topic']:
            return self._("bodhi masher started its mashtask")
        elif 'bodhi.mashtask.complete' in msg['topic']:
            success = msg['msg']['success']
            if success:
                return self._("bodhi masher successfully completed mashing")
            else:
                return self._("bodhi masher failed to complete its mashtask!")
        elif 'bodhi.mashtask.sync.wait' in msg['topic']:
            return self._("bodhi masher is waiting on mirror repos to sync")
        elif 'bodhi.mashtask.sync.done' in msg['topic']:
            return self._("bodhi masher finished waiting on mirror repos "
                          "to sync")
        elif 'bodhi.buildroot_override.tag' in msg['topic']:
            tmpl = self._("{submitter} submitted a buildroot override " +
                          "for {build}")
            if markup:
                return tmpl.format(
                    submitter=author_link(msg['msg']['override']['submitter']),
                    build=msg['msg']['override']['build'],
                )
            else:
                return tmpl.format(**msg['msg']['override'])
        elif 'bodhi.buildroot_override.untag' in msg['topic']:
            tmpl = self._("{submitter} expired a buildroot override " +
                          "for {build}")
            if markup:
                return tmpl.format(
                    submitter=author_link(msg['msg']['override']['submitter']),
                    build=msg['msg']['override']['build'],
                )
            else:
                return tmpl.format(**msg['msg']['override'])
        else:
            raise NotImplementedError("%r" % msg)

    def link(self, msg, **config):
        tmpl = "https://admin.fedoraproject.org/updates/{title}"
        if 'bodhi.update.comment' in msg['topic']:
            return tmpl.format(title=msg['msg']['comment']['update_title'])
        elif 'bodhi.update.complete' in msg['topic']:
            return tmpl.format(title=msg['msg']['update']['title'])
        elif 'bodhi.update.request' in msg['topic']:
            return tmpl.format(title=msg['msg']['update']['title'])
        elif is_ftp_sync(msg):
            link = "https://download.fedoraproject.org/pub/"
            product = get_sync_product(msg).lower()
            link += product + "/"

            if product == 'fedora':
                link += "linux/updates/"

            if msg['msg']['repo'].endswith('testing'):
                link += "testing/"

            link += msg['msg']['release'] + "/"
            return link

    def packages(self, msg, **config):
        if 'bodhi.update.comment' in msg['topic']:
            return set(_u2p(msg['msg']['comment']['update_title']))
        elif 'bodhi.update.complete' in msg['topic']:
            return set(_u2p(msg['msg']['update']['title']))
        elif 'bodhi.update.request' in msg['topic']:
            return set(_u2p(msg['msg']['update']['title']))
        elif 'bodhi.buildroot_override.' in msg['topic']:
            return set(_u2p(msg['msg']['override']['build']))

        return set()

    def usernames(self, msg, **config):
        users = []

        for obj in ['update', 'override']:
            try:
                users.append(msg['msg'][obj]['submitter'])
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

        return set(users)

    def objects(self, msg, **config):
        if is_ftp_sync(msg):
            product = get_sync_product(msg).lower()
            msg = msg['msg']
            return set(['/'.join([product, msg['repo'], msg['release']])])
        elif 'bodhi.mashtask.mashing' in msg['topic']:
            return set(['repos/' + msg['msg']['repo']])
        elif 'bodhi.update.comment' in msg['topic']:
            return set([
                'packages/' + p for p in
                _u2p(msg['msg']['comment']['update_title'])
            ])
        elif 'bodhi.update.complete' in msg['topic']:
            return set([
                'packages/' + p for p in
                _u2p(msg['msg']['update']['title'])
            ])
        elif 'bodhi.update.request' in msg['topic']:
            return set([
                'packages/' + p for p in
                _u2p(msg['msg']['update']['title'])
            ])
        elif 'bodhi.buildroot_override.' in msg['topic']:
            return set([
                'packages/' + p for p in
                _u2p(msg['msg']['override']['build'])
            ])

        return set()
