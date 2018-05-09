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
# Authors:  David Gay <oddshocks@riseup.net

from fedmsg_meta_fedora_infrastructure import BaseProcessor


class FedimgProcessor(BaseProcessor):
    __name__ = "fedimg"
    __description__ = "The Fedora cloud image service"
    __link__ = "https://github.com/fedora-infra/fedimg"
    __docs__ = "https://fedimg.readthedocs.io"
    __obj__ = "New cloud image upload"
    __icon__ = "https://apps.fedoraproject.org/img/icons/fedimg.png"

    def subtitle(self, msg, **config):
        name = msg['msg']['image_name']
        dest = msg['msg']['destination']
        extra = msg['msg'].get('extra', {})
        ami = extra.get('id')
        virt = extra.get('virt_type')
        vol = extra.get('vol_type')
        if 'image.upload' in msg['topic']:
            if msg['msg']['status'] == "started":
                tmpl = self._('{image_name} started uploading to {dest}')
                return tmpl.format(image_name=name, dest=dest)
            elif msg['msg']['status'] == "completed":
                ami = extra.get('id')
                virt = extra.get('virt_type')
                vol = extra.get('vol_type')
                tmpl = self._('{image_name} finished uploading to {dest} '
                              '({ami}, {virt}, {vol})')
                return tmpl.format(image_name=name, dest=dest, ami=ami,
                                   virt=virt, vol=vol)
            elif msg['msg']['status'] == "failed":
                tmpl = self._('{image_name} failed to upload to {dest}')
                return tmpl.format(image_name=name, dest=dest)
        if 'image.test' in msg['topic']:
            tmpl = ''
            if msg['msg']['status'] == "started":
                tmpl = self._('{image_name} started testing on {dest} '
                              '({ami}, {virt}, {vol})')
            elif msg['msg']['status'] == "completed":
                tmpl = self._('{image_name} finished testing on {dest} '
                              '({ami}, {virt}, {vol})')
            elif msg['msg']['status'] == "failed":
                tmpl = self._('{image_name} failed testing on {dest} '
                              '({ami}, {virt}, {vol})')
            return tmpl.format(image_name=name, dest=dest, ami=ami,
                               virt=virt, vol=vol)

        if 'image.publish' in msg['topic']:
            tmpl = self._('{image_name} published in region, {dest} '
                          '({ami}, {virt}, {vol})')

            return tmpl.format(image_name=name, dest=dest, ami=ami,
                               virt=virt, vol=vol)

        if 'image.copy' in msg['topic']:
            source_image_id = extra.get('source_image_id')

            tmpl = self._('{image_name} copied to {dest} using source image, '
                          '{source_image_id} ({ami}, {virt}, {vol})')

            return tmpl.format(image_name=name, dest=dest, ami=ami,
                               source_image_id=source_image_id, virt=virt,
                               vol=vol)

    def objects(self, msg, **config):
        status = msg['msg'].get('status')
        if 'image.upload' in msg['topic']:
            return set(['image/upload/' + status])
        elif 'image.test' in msg['topic']:
            return set(['image/test/' + status])

        return set([])
