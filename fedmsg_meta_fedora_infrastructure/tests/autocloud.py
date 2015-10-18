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
#
""" Tests for autocloud messages """

import unittest

from fedmsg_meta_fedora_infrastructure.tests.base import Base

from .common import add_doc


class TestImageTestQueued(Base):
    """ These messages are published when an image is queued for testing in
    Autocloud app.
    """
    expected_title = "autocloud.image.queued"
    expected_subti = 'Fedora-Cloud-Base is queued for testing'
    expected_link = 'https://kojipkgs.fedoraproject.org//work/' + \
        'taskstasks/1410/10291410/Fedora-Cloud-Base-22-20150705.i386.qcow2'
    expected_secondary_icon = "https://apps.fedoraproject.org/img/icons/" + \
        "fedimg.png"
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set(['autocloud/image/queued'])
    msg = {
        u'username': u'apache',
        u'i': 1,
        u'timestamp': 1379638157.759283,
        u'msg_id': u'2015-4b5aae66-b713-4c22-bb4a-1277d4402375',
        u'topic': u'org.fedoraproject.prod.autocloud.image.queued',
        u'msg': {
            u'buildid': u'10291410',
            u'status': u'queued',
            u'image_url': u'https://kojipkgs.fedoraproject.org//work/'
            'taskstasks/1410/10291410/Fedora-Cloud-Base-22-20150705.i386.qcow2',
            u'image_name': u'Fedora-Cloud-Base'
        }
    }


class TestImageTestRunning(Base):
    """ These messages are published when tests for an image starts
    in Autocloud app.
    """
    expected_title = "autocloud.image.running"
    expected_subti = 'The tests for the Fedora-Cloud-Base (rawhide) have started running'
    expected_link = 'https://kojipkgs.fedoraproject.org//work/' + \
        'taskstasks/1410/10291410/Fedora-Cloud-Base-22-20150705.i386.qcow2'
    expected_secondary_icon = "https://apps.fedoraproject.org/img/icons/" + \
        "fedimg.png"
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set(['autocloud/image/running'])
    msg = {
        u'username': u'apache',
        u'i': 1,
        u'timestamp': 1379638157.759283,
        u'msg_id': u'2015-4b5aae66-b713-4c22-bb4a-1277d4402375',
        u'topic': u'org.fedoraproject.prod.autocloud.image.running',
        u'msg': {
            u'buildid': u'10291410',
            u'status': u'running',
            u'image_url': u'https://kojipkgs.fedoraproject.org//work/'
            'taskstasks/1410/10291410/Fedora-Cloud-Base-22-20150705.i386.qcow2',
            u'image_name': u'Fedora-Cloud-Base',
            u'release': 'rawhide',
        }
    }


class TestImageTestAborted(Base):
    """ These messages are published when tests for an image starts
    in Autocloud app.
    """
    expected_title = "autocloud.image.aborted"
    expected_subti = 'The tests for the Fedora-Cloud-Base (rawhide) have been aborted'
    expected_link = 'https://kojipkgs.fedoraproject.org//work/' + \
        'taskstasks/1410/10291410/Fedora-Cloud-Base-22-20150705.i386.qcow2'
    expected_secondary_icon = "https://apps.fedoraproject.org/img/icons/" + \
        "fedimg.png"
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set(['autocloud/image/aborted'])
    msg = {
        u'username': u'apache',
        u'i': 1,
        u'timestamp': 1379638157.759283,
        u'msg_id': u'2015-4b5aae66-b713-4c22-bb4a-1277d4402375',
        u'topic': u'org.fedoraproject.prod.autocloud.image.aborted',
        u'msg': {
            u'buildid': u'10291410',
            u'status': u'aborted',
            u'image_url': u'https://kojipkgs.fedoraproject.org//work/'
            'taskstasks/1410/10291410/Fedora-Cloud-Base-22-20150705.i386.qcow2',
            u'image_name': u'Fedora-Cloud-Base',
            u'release': 'rawhide',
        }
    }


class TestImageTestFailed(Base):
    """ These messages are published when tests for an image starts
    in Autocloud app.
    """
    expected_title = "autocloud.image.failed"
    expected_subti = 'The tests for the Fedora-Cloud-Base (23) failed'
    expected_link = 'https://apps.fedoraproject.org/autocloud/jobs/412/output'
    expected_secondary_icon = "https://apps.fedoraproject.org/img/icons/" + \
        "fedimg.png"
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set(['autocloud/image/failed'])
    msg = {
        u'username': u'apache',
        u'i': 1,
        u'timestamp': 1379638157.759283,
        u'msg_id': u'2015-4b5aae66-b713-4c22-bb4a-1277d4402375',
        u'topic': u'org.fedoraproject.prod.autocloud.image.failed',
        u'msg': {
            u'buildid': u'10291410',
            u'status': u'failed',
            u'job_id': 412,
            u'image_url': u'https://kojipkgs.fedoraproject.org//work/'
            'taskstasks/1410/10291410/Fedora-Cloud-Base-22-20150705.i386.qcow2',
            u'image_name': u'Fedora-Cloud-Base',
            u'release': u'23',
        }
    }


class TestImageTestSuccess(Base):
    """ These messages are published when tests for an image successfully
    completes in Autocloud app.
    """
    expected_title = "autocloud.image.success"
    expected_subti = 'The tests for Fedora-Cloud-Base were a success'
    expected_link = 'https://kojipkgs.fedoraproject.org//work/' + \
        'taskstasks/1410/10291410/Fedora-Cloud-Base-22-20150705.i386.qcow2'
    expected_secondary_icon = "https://apps.fedoraproject.org/img/icons/" + \
        "fedimg.png"
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set(['autocloud/image/success'])
    msg = {
        u'username': u'apache',
        u'i': 1,
        u'timestamp': 1379638157.759283,
        u'msg_id': u'2015-4b5aae66-b713-4c22-bb4a-1277d4402375',
        u'topic': u'org.fedoraproject.prod.autocloud.image.success',
        u'msg': {
            u'buildid': u'10291410',
            u'status': u'success',
            u'image_url': u'https://kojipkgs.fedoraproject.org//work/'
            'taskstasks/1410/10291410/Fedora-Cloud-Base-22-20150705.i386.qcow2',
            u'image_name': u'Fedora-Cloud-Base'
        }
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
