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
# Authors:  Ralph Bean <rbean@redhat.com>
#
from fedmsg_meta_fedora_infrastructure import BaseProcessor
from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url


class SummerShumProcessor(BaseProcessor):
    __name__ = "summershum"
    __description__ = "a backend tool that extracts hashes of source files"
    __link__ = "https://github.com/fedora-infra/summershum"
    __docs__ = "https://github.com/fedora-infra/summershum"
    __obj__ = "Source File Hashes"
    __icon__ = "https://raw.githubusercontent.com/" + \
        "fedora-infra/summershum/develop/summershum.png"

    def subtitle(self, msg, **config):
        if msg['topic'].endswith('fail'):
            tmpl = self._('yikes!  summershum failed to process {filename} '
                          'for {name}')
        elif msg['topic'].endswith('complete'):
            tmpl = self._('summershum ingested {filename} '
                          'for {name}')
        elif msg['topic'].endswith('start'):
            tmpl = self._('summershum started working on {filename} '
                          'for {name}')
        else:
            tmpl = self._('(unhandled)')

        return tmpl.format(**msg['msg']['original'])

    def secondary_icon(self, msg, **config):
        return avatar_url(msg['msg']['original']['agent'])

    def usernames(self, msg, **config):
        return set([msg['msg']['original']['agent']])

    def packages(self, msg, **config):
        return set([msg['msg']['original']['name']])

    def objects(self, msg, **config):
        original = msg['msg']['original']
        return set(['/'.join([
            'digests',
            original['name'],
            original['filename'],
            original['md5sum'],
        ])])

    def link(self, msg, **config):
        o = msg['msg']['original']
        prefix = "http://pkgs.fedoraproject.org/lookaside/pkgs"

        if 'path' in o:
            path = o['path']

        else:
            # Fallback to the old message format from the dark ages of MD5
            name = o['name']
            md5sum = o['md5sum']
            filename = o['filename']
            tmpl = "{name}/{filename}/{md5sum}/{filename}"

            path = tmpl.format(name=name, md5sum=md5sum, filename=filename)

        return "{prefix}/{path}".format(prefix=prefix, path=path)
