# This file is part of fedmsg.
# Copyright (C) 2013, 2014 Red Hat, Inc.
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


class MirrorManagerProcessor(BaseProcessor):
    __name__ = "mirrormanager"
    __description__ = "Mirror Manager activity"
    __link__ = "https://mirrors.fedoraproject.org"
    __docs__ = "https://github.com/fedora-infra/mirrormanager2"
    __obj__ = "Mirror Updates"
    __icon__ = "https://apps.fedoraproject.org/img/icons/downloads.png"

    def link(self, msg, **config):
        return self.__link__

    def subtitle(self, msg, **config):
        topic, msg = msg['topic'], msg['msg']
        if 'mirrormanager.crawler.complete' in topic:
            results = msg['results']
            total = len(results)
            succeeded = len([1 for r in results if r['rc'] == 0])
            failed = len([1 for r in results if r['rc'] != 0])
            tmpl = self._(
                "mirrormanager's crawler finished a crawl of {total} mirrors "
                "({succeeded} succeeded, {failed} failed)"
            )
            return tmpl.format(total=total, succeeded=succeeded, failed=failed)
        elif 'mirrormanager.crawler.start' in topic:
            total = len(msg['hosts'])
            tmpl = self._(
                "mirrormanager's crawler started a crawl of {total} mirrors")
            return tmpl.format(total=total)
        elif 'mirrormanager.netblocks.get' in topic:
            type = msg['type']

            if msg['success']:
                status = self._("successfully updated")
            else:
                status = self._("failed to update")

            tmpl = self._(
                "mirrormanager's backend {status} its {type} netblocks file")
            return tmpl.format(status=status, type=type)

    def secondary_icon(self, msg, **config):
        return self.icon(msg, **config)

    def usernames(self, msg, **config):
        return set()

    def packages(self, msg, **config):
        return set()

    def objects(self, msg, **config):
        if 'mirrormanager.crawler' in msg['topic']:
            if 'hosts' in msg['msg']:
                return set([
                    'mirrors/%s' % host.get('host', host.get('name'))
                    for host in msg['msg']['hosts']
                ])
            else:
                return set([
                    'mirrors/%s' % result['host']['name']
                    for result in msg['msg']['results']
                ])
        if 'mirrormanager.netblocks' in msg['topic']:
            return set([
                'netblocks/' + msg['msg']['type']
            ])

        return set([])

