# This file is part of fedmsg.
# Copyright (C) 2014 Red Hat, Inc.
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
# Authors:  Michael Simacek <msimacek@redhat.com>

from fedmsg_meta_fedora_infrastructure import BaseProcessor


class KoscheiProcessor(BaseProcessor):
    __name__ = 'koschei'
    __description__ = "Continuous integration for Fedora packages"
    __link__ = "https://apps.fedoraproject.org/koschei"
    __docs__ = "https://apps.fedoraproject.org/koschei/documentation"
    __obj__ = "Watched packages"
    __icon__ = ("https://fedoraproject.org/w/uploads/e/e9/Koschei.png")

    def subtitle(self, msg, **config):
        # Emitted by Koschei whenever state of package changes, for
        # example when package starts to fail to build, package
        # dependencies become unresolved or when package is fixed.
        if 'koschei.package.state.change' in msg['topic']:
            content = msg['msg']
            if content['new'] == 'ok' and content['old'] == 'ignored':
                info = "{name} added to Koschei"
            else:
                info = {
                    'failing': "{name}'s builds started to fail",
                    'ok': "{name}'s builds are back to normal",
                    'ignored': "{name} became retired or ignored",
                    'unresolved': "{name}'s dependencies failed to resolve",
                }[content['new']]
            info += ' in {collection}'
            if content['koji_instance'] != 'primary':
                info += ' ({koji_instance})'
            collection = content.get('collection_name', content.get('repo'))
            return info.format(name=content['name'],
                               collection=collection,
                               koji_instance=content['koji_instance'])
        # Emitted by Koschei whenever state of collection changes, for
        # example when collection buildroot becomes unresolvable
        # (broken) or when it is fixed.
        elif 'koschei.collection.state.change' in msg['topic']:
            content = msg['msg']
            if content['new'] == 'ok' and content['old'] == 'unknown':
                info = "{collection} added to Koschei"
            else:
                info = {
                    'ok': "{collection} buildroot was fixed",
                    'unresolved': "{collection} buildroot was broken",
                }[content['new']]
            if content['koji_instance'] != 'primary':
                info += ' ({koji_instance})'
            collection = content['collection_name']
            return info.format(collection=collection,
                               koji_instance=content['koji_instance'])
        else:
            raise NotImplementedError("%r" % msg)

    def secondary_icon(self, msg, **config):
        tmpl = 'https://apps.fedoraproject.org/packages/images/icons/%s.png'
        # Emitted by Koschei whenever state of package changes, for
        # example when package starts to fail to build, package
        # dependencies become unresolved or when package is fixed.
        if 'koschei.package.state.change' in msg['topic']:
            return tmpl % msg['msg']['name']

    def link(self, msg, **config):
        baseurl = 'https://apps.fedoraproject.org/koschei'
        # Emitted by Koschei whenever state of package changes, for
        # example when package starts to fail to build, package
        # dependencies become unresolved or when package is fixed.
        if 'koschei.package.state.change' in msg['topic']:
            url = '{baseurl}/package/{name}'.format(baseurl=baseurl,
                                                    name=msg['msg']['name'])
            if 'collection' in msg['msg']:
                url += '?collection=' + msg['msg']['collection']
            return url
        # Emitted by Koschei whenever state of collection changes, for
        # example when collection buildroot becomes unresolvable
        # (broken) or when it is fixed.
        elif 'koschei.collection.state.change' in msg['topic']:
            url = '{baseurl}/collection/{name}'.format(baseurl=baseurl,
                                                    name=msg['msg']['collection'])
            return url
        else:
            raise NotImplementedError("%r" % msg)

    def packages(self, msg, **config):
        if 'koschei.package.state.change' in msg['topic']:
            return set([msg['msg']['name']])
        else:
            raise NotImplementedError("%r" % msg)
