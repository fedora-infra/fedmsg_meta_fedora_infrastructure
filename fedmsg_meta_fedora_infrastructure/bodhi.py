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

from fedmsg_meta_fedora_infrastructure import BaseProcessor
from fasshim import gravatar_url

def _u2p(update):
    """ Take an update, and return the package name """
    # TODO -- make this unnecessary by having bodhi emit the
    # package name (and not just the update name) to begin with.
    return [build.rsplit('-', 2)[0] for build in update.split(',')]


class BodhiProcessor(BaseProcessor):
    __name__ = "Bodhi"
    __description__ = "the Fedora update system"
    __link__ = "https://admin.fedoraproject.org/updates"
    __docs__ = "http://fedoraproject.org/wiki/Bodhi"
    __obj__ = "Package Updates"
    __icon__ = "https://admin.fedoraproject.org/updates" + \
               "/static/images/bodhi-icon-48.png"

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
        if 'bodhi.update.comment' in msg['topic']:
            author = msg['msg']['comment']['author']
            karma = msg['msg']['comment']['karma']
            title = msg['msg']['comment']['update_title']

            if len(title) >= 35:
                title = title[:35] + '...'

            tmpl = self._(
                "{author} commented on bodhi update {title} (karma: {karma})"
            )
            return tmpl.format(author=author, karma=karma, title=title)
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
            author = msg['msg']['agent']
            title = msg['msg']['update']['title']
            if status in ('unpush', 'obsolete', 'revoke'):
                # make our status past-tense
                status = status + (status[-1] == 'e' and 'd' or 'ed')
                tmpl = self._("{author} {status} {title}").format(
                        author=author, status=status, title=title)
            else:
                tmpl = self._("{author} submitted {title} to {status}").format(
                        author=author, status=status, title=title)
            return tmpl
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
            return self._("bodhi masher finished waiting on mirror repos " + \
                          "to sync")
        elif 'bodhi.buildroot_override.tag' in msg['topic']:
            return self._("{submitter} submitted a buildroot override " +
                          "for {build}").format(**msg['msg']['override'])
        elif 'bodhi.buildroot_override.untag' in msg['topic']:
            return self._("{submitter} expired a buildroot override " +
                          "for {build}").format(**msg['msg']['override'])
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

        return set(users)

    def objects(self, msg, **config):
        if 'bodhi.mashtask.mashing' in msg['topic']:
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
