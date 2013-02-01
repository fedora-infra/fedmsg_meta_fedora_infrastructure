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


class KojiProcessor(BaseProcessor):
    __name__ = "buildsys"
    __description__ = "the Fedora build system"
    __link__ = "https://koji.fedoraproject.org/koji"
    __docs__ = "https://fedoraproject.org/wiki/Using_the_Koji_build_system"
    __obj__ = "Koji Builds"
    __icon__ = "http://fedoraproject.org/w/uploads/2/20/" + \
        "Artwork_DesignService_koji-icon-48.png"

    def handle_msg(self, msg, **config):
        return '.buildsys.' in msg['topic']

    def subtitle(self, msg, **config):
        if 'buildsys.tag' in msg['topic']:
            tmpl = self._("{owner}'s {name}-{version}-{release} tagged {tag}")
            return tmpl.format(**msg['msg'])
        elif 'buildsys.untag' in msg['topic']:
            tmpl = self._(
                "{owner}'s {name}-{version}-{release} untagged from {tag}"
            )
            return tmpl.format(**msg['msg'])
        elif 'buildsys.repo.init' in msg['topic']:
            tmpl = self._('Repo initialized:  {tag}')
            return tmpl.format(**msg['msg'])
        elif 'buildsys.repo.done' in msg['topic']:
            tmpl = self._('Repo done:  {tag}')
            return tmpl.format(**msg['msg'])
        elif 'buildsys.build.state.change' in msg['topic']:
            templates = [
                self._(
                    "{owner}'s {name}-{version}-{release} started building"
                ),
                self._("{owner}'s {name}-{version}-{release} completed"),
                self._("{owner}'s {name}-{version}-{release} was deleted"),
                self._("{owner}'s {name}-{version}-{release} failed to build"),
                self._("{owner}'s {name}-{version}-{release} was cancelled"),
            ]
            tmpl = templates[msg['msg']['new']]
            return tmpl.format(**msg['msg'])
        else:
            raise NotImplementedError()

    def usernames(self, msg, **config):
        if 'buildsys.tag' in msg['topic']:
            return set([
                msg['msg']['owner'],
                msg['msg']['user'],
            ])
        elif 'buildsys.untag' in msg['topic']:
            return set([
                msg['msg']['owner'],
                msg['msg']['user'],
            ])
        elif 'buildsys.repo.init' in msg['topic']:
            return set()
        elif 'buildsys.repo.done' in msg['topic']:
            return set()
        elif 'buildsys.build.state.change' in msg['topic']:
            return set([
                msg['msg']['owner'],
            ])
        else:
            raise NotImplementedError()

    def packages(self, msg, **config):
        if 'buildsys.tag' in msg['topic']:
            return set([msg['msg']['name']])
        elif 'buildsys.untag' in msg['topic']:
            return set([msg['msg']['name']])
        elif 'buildsys.repo.init' in msg['topic']:
            return set([])
        elif 'buildsys.repo.done' in msg['topic']:
            return set([])
        elif 'buildsys.build.state.change' in msg['topic']:
            return set([msg['msg']['name']])
        else:
            raise NotImplementedError()

    def link(self, msg, **config):
        if 'buildsys.tag' in msg['topic']:
            return "https://koji.fedoraproject.org/koji/taginfo?tagID=%i" % (
                msg['msg']['tag_id'])
        elif 'buildsys.untag' in msg['topic']:
            return "https://koji.fedoraproject.org/koji/taginfo?tagID=%i" % (
                msg['msg']['tag_id'])
        elif 'buildsys.repo.init' in msg['topic']:
            return "https://koji.fedoraproject.org/koji/taginfo?tagID=%i" % (
                msg['msg']['tag_id'])
        elif 'buildsys.repo.done' in msg['topic']:
            return "https://koji.fedoraproject.org/koji/taginfo?tagID=%i" % (
                msg['msg']['tag_id'])
        elif 'buildsys.build.state.change' in msg['topic']:
            return "https://koji.fedoraproject.org/koji/buildinfo?buildID=%i" \
                % (msg['msg']['build_id'])
        else:
            raise NotImplementedError()

    def objects(self, msg, **config):
        if 'buildsys.tag' in msg['topic']:
            return set([
                '/'.join([
                    'koji', 'builds',
                    msg['msg']['name'],
                    msg['msg']['version'],
                    msg['msg']['release'],
                ]),
                '/'.join([
                    'koji', 'tags',
                    msg['msg']['tag'],
                ]),
            ])
        elif 'buildsys.untag' in msg['topic']:
            return set([
                '/'.join([
                    'koji', 'builds',
                    msg['msg']['name'],
                    msg['msg']['version'],
                    msg['msg']['release'],
                ]),
                '/'.join([
                    'koji', 'tags',
                    msg['msg']['tag'],
                ]),
            ])
        elif 'buildsys.build.state.change' in msg['topic']:
            return set(['/'.join([
                'koji', 'builds',
                msg['msg']['name'],
                msg['msg']['version'],
                msg['msg']['release'],
            ])])
        elif 'buildsys.repo.init' in msg['topic']:
            return set(['/'.join([
                'koji', 'repos',
                msg['msg']['tag'],
            ])])
        elif 'buildsys.repo.done' in msg['topic']:
            return set(['/'.join([
                'koji', 'repos',
                msg['msg']['tag'],
            ])])
        else:
            raise NotImplementedError()
