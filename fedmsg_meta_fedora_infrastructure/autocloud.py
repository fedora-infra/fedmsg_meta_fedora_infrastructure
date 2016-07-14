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


    def _func_router(self, msg, fname, **config):
        """
        This method routes the messages based on the params and calls the
        appropriate method to process the message. The utility of the method is
        to cope up with the major message change during different releases.
        """
        FNAME = 'handle_%s_autocloud_%s'

        if ('compose_id' in msg['msg'] or 'compose_job_id' in msg['msg'] or
                'autocloud.compose' in msg['topic']):
            return getattr(self, FNAME % ('v2', fname))(msg, **config)
        else:
            return getattr(self, FNAME % ('v1', fname))(msg, **config)

    def subtitle(self, msg, **config):
        return self._func_router(msg, 'subtitle', **config)

    def secondary_icon(self, msg, **config):
        return self.__icon__

    def link(self, msg, **config):
        return self._func_router(msg, 'link', **config)

    def objects(self, msg, **config):
        return self._func_router(msg, 'objects', **config)

    def handle_v2_autocloud_subtitle(self, msg, **config):
        status = msg['msg']['status']
        if 'autocloud.image' in msg['topic']:
            compose_id = msg['msg']['compose_id']
            image_name = msg['msg']['image_name']
            release = msg['msg'].get('release')

            if status == "queued":
                tmpl = self._("{image_name}({compose_id}) is {status} for "
                                "testing")
            if status == "running":
                tmpl = self._("The tests for the {image_name}({compose_id}) "
                                "have started {status}")
            if status == "aborted":
                tmpl = self._("The tests for the {image_name}({compose_id}) "
                                "have been {status}")
            if status == "failed":
                tmpl = self._("The tests for the {image_name}({compose_id}) "
                                "{status}")
            if status == "success":
                tmpl = self._("The tests for {image_name}({compose_id}) were a"
                                " {status}")

            if release:
                image_name = "%s (%s)" % (image_name, release)

            return tmpl.format(image_name=image_name, status=status,
                                compose_id=compose_id)

        if "autocloud.compose" in msg['topic']:
            compose_id = msg['msg'].get(
                    'id', msg['msg'].get('compose_id', 'A compose'))

            if status == 'queued':
                tmpl = self._("{compose_id} is {status} for testing")
            if status == 'running':
                tmpl = self._("{compose_id} tests have started {status}")
            if status == 'completed':
                tmpl = self._("{compose_id} tests have {status}")

            return tmpl.format(compose_id=compose_id, status=status)

    def handle_v2_autocloud_link(self, msg, **config):
        if 'autocloud.image' in msg['topic']:
            job_id = msg['msg'].get('job_id')
            if job_id:
                template = 'https://apps.fedoraproject.org/autocloud/jobs/' + \
                    '%s/output'
                return template % job_id
            else:
                return msg['msg']['image_url']
        elif 'autocloud.compose' in msg['topic']:
            compose_job_id = msg['msg'].get('compose_job_id')
            if compose_job_id is not None:
                return 'https://apps.fedoraproject.org/autocloud/jobs/%s' % (
                    compose_job_id)
        return 'https://apps.fedoraproject.org/autocloud/'

    def handle_v2_autocloud_objects(self, msg, **config):
        status = msg['msg']['status']
        if 'autocloud.image' in msg['topic']:
            return set(['autocloud/image/' + status])
        elif 'autocloud.compose' in msg['topic']:
            return set(['autocloud/compose/' + status])

    def handle_v1_autocloud_subtitle(self, msg, **config):
        image_name = msg['msg']['image_name']
        status = msg['msg']['status']
        release = msg['msg'].get('release')
        if 'autocloud.image' in msg['topic']:
            if status == "queued":
                tmpl = self._("{image_name} is {status} for testing")
            if status == "running":
                tmpl = self._("The tests for the {image_name} have "
                              "started {status}")
            if status == "aborted":
                tmpl = self._("The tests for the {image_name} have "
                              "been {status}")
            if status == "failed":
                tmpl = self._("The tests for the {image_name} {status}")
            if status == "success":
                tmpl = self._("The tests for {image_name} were a {status}")

            if release:
                image_name = "%s (%s)" % (image_name, release)

            return tmpl.format(image_name=image_name, status=status)

    def handle_v1_autocloud_link(self, msg, **config):
        job_id = msg['msg'].get('job_id')
        if job_id:
            template = 'https://apps.fedoraproject.org/autocloud/jobs/%s/output'
            return template % job_id
        else:
            return msg['msg']['image_url']

    def handle_v1_autocloud_objects(self,msg, **config):
        status = msg['msg']['status']
        return set(['autocloud/image/' + status])


