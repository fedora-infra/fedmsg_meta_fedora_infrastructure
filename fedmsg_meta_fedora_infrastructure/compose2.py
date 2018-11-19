# This file is part of fedmsg.
# Copyright (C) 2015 Red Hat, Inc.
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


class PungiKojiProcessor(BaseProcessor):
    __name__ = "pungi"
    __description__ = "Fedora Release Engineering"
    __link__ = "https://pagure.io/releng"
    __docs__ = "https://pagure.io/docs/releng"
    __icon__ = "https://apps.fedoraproject.org/img/icons/pungi.png"
    __obj__ = "Composes"

    def subtitle(self, msg, **config):
        compose = msg['msg'].get('compose_id')
        if msg['topic'].endswith('pungi.compose.status.change'):
            statuses = {
                'STARTED': self._('started'),
                'FINISHED': self._('just finished'),
                'DOOMED': self._('failed in a horrible fire'),
                'TERMINATED': self._('was terminated'),
            }
            status = statuses.get(msg['msg']['status'], msg['msg']['status'])
            tmpl = self._("pungi-koji compose of {compose} {status}")
            return tmpl.format(compose=compose, status=status)
        elif msg['topic'].endswith('pungi.compose.phase.start'):
            phase = msg['msg']['phase_name']
            tmpl = self._("pungi-koji started the {phase} phase "
                          "of the {compose} compose")
            return tmpl.format(compose=compose, phase=phase)
        elif msg['topic'].endswith('pungi.compose.phase.stop'):
            phase = msg['msg']['phase_name']
            tmpl = self._("pungi-koji finished the {phase} phase "
                          "of the {compose} compose")
            return tmpl.format(compose=compose, phase=phase)
        elif msg['topic'].endswith('pungi.compose.createiso.imagedone'):
            image = msg['msg']['file'].split('compose/')[-1]
            tmpl = self._("pungi-koji finished createiso for {image}")
            return tmpl.format(image=image)
        elif msg['topic'].endswith('pungi.compose.createiso.imagefail'):
            image = msg['msg']['file'].split('compose/')[-1]
            tmpl = self._("pungi-koji createiso for {image} failed!")
            return tmpl.format(image=image)
        elif msg['topic'].endswith('pungi.compose.createiso.targets'):
            N = len(msg['msg']['deliverables'])
            tmpl = self._("pungi-koji assigned {N} createiso targets")
            return tmpl.format(N=N)
        elif msg['topic'].endswith('pungi.compose.ostree'):
            ref = msg['msg']['ref']
            arch = msg['msg']['arch']
            commitid = msg['msg']['commitid']
            tmpl = self._('pungi-koji ostree compose {compose} produced '
                          'ostree commit {commitid} for {arch} {ref}')
            return tmpl.format(compose=compose, arch=arch, commitid=commitid,
                               ref=ref)
        elif msg['topic'].endswith('pungi.compose.fail.to.start'):
            config = msg['msg'].get('config')
            detail = msg['msg'].get('detail')
            tmpl = self._('failed to compose from {config}: "{detail}"')
            return tmpl.format(config=config, detail=detail)

    def link(self, msg, **config):
        if 'location' in msg['msg']:
            return msg['msg']['location'].strip('/').strip('/compose')

    def objects(self, msg, **config):
        if 'deliverables' in msg['msg']:
            return set([d.strip('/') for d in msg['msg']['deliverables']])
        elif 'file' in msg['msg']:
            return set([msg['msg']['file'].strip('/')])
        elif 'compose_id' in msg['msg']:
            compose = msg['msg']['compose_id']
            return set(["rawhide/" + "/".join(compose.split('.'))])
