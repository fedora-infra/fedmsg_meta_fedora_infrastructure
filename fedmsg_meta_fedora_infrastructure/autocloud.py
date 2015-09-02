# This file is part of fedmsg.
# Copyright (C) 2015 Sayan Chowdhury.
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
# Authors:  Sayan Chowdhury <sayanchowdhury@fedoraproject.org>

from fedmsg_meta_fedora_infrastructure import BaseProcessor


class AutoCloudProcessor(BaseProcessor):
    __name__ = "autocloud"
    __description__ = "Automated Fedora Cloud Image Testing service"
    __link__ = "https://github.com/kushaldas/autocloud"
    __docs__ = "https://github.com/kushaldas/autocloud"
    __icon__ = "https://apps.fedoraproject.org/img/icons/fedimg.png"
    __obj__ = "Cloud Image Test"

    def subtitle(self, msg, **config):
        image_name = msg['msg']['image_name']
        status = msg['msg']['status']
        if 'autocloud.image' in msg['topic']:
            if status == "queued":
                tmpl = self._("{image_name} is {status} for testing")
            if status == "running":
                tmpl = self._("The tests for the {image_name} has "
                              "started {status}")
            if status == "aborted":
                tmpl = self._("The tests for the {image_name} has "
                              "been {status}")
            if status == "failed":
                tmpl = self._("The tests for the {image_name} {status}")
            if status == "success":
                tmpl = self._("The tests for {image_name} was {status}")

            return tmpl.format(image_name=image_name, status=status)

    def link(self, msg, **config):
        return self.__link__

    def secondary_icon(self, msg, **config):
        return self.__icon__

    def link(self, msg, **config):
        image_url = msg['msg']['image_url']
        return image_url

    def objects(self, msg, **config):
        status = msg['msg']['status']
        return set(['autocloud/image/' + status])
