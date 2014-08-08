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
    __link__ = "https://github.com/oddshocks/fedimg"
    # TODO: Create an icon and set its URL to __icon__
    __docs__ = "https://fedoraproject.org/wiki/Features/" + \
               "FirstClassCloudImages/KojiPlan"
    __obj__ = "New cloud image upload"

    def subtitle(self, msg, **config):
        if 'image.upload' in msg['topic']:
            if msg['msg']['status'] is "started":
                name = msg['msg']['image_name']
                dest = msg['msg']['destination']
                tmpl = self._('Image {image_name} started uploading to {dest}')
                return tmpl.format(image_name=name, dest=dest)
            elif msg['msg']['status'] is "completed":
                name = msg['msg']['image_name']
                dest = msg['msg']['destination']
                tmpl = self._('Image {image_name} finished uploading to to {dest}')
                return tmpl.format(image_name=name, dest=dest)
            elif msg['msg']['status'] is "failed":
                name = msg['msg']['image_name']
                dest = msg['msg']['destination']
                tmpl = self._('Image {image_name} failed to upload to {dest}')
                return tmpl.format(image_name=name, dest=dest)
        if 'image.test' in msg['topic']:
            if msg['msg']['status'] is "started":
                name = msg['msg']['image_name']
                dest = msg['msg']['destination']
                tmpl = self._('Image {image_name} started testing on {dest}')
                return tmpl.format(image_name=name, dest=dest)
            elif msg['msg']['status'] is "completed":
                name = msg['msg']['image_name']
                dest = msg['msg']['destination']
                tmpl = self._('Image {image_name} finished testing on {dest}')
                return tmpl.format(image_name=name, dest=dest)
            elif msg['msg']['status'] is "failed":
                name = msg['msg']['image_name']
                dest = msg['msg']['destination']
                tmpl = self._('Image {image_name} failed testing on {dest}')
                return tmpl.format(image_name=name, dest=dest)
