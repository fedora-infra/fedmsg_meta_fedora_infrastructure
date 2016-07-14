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
    expected_subti = 'Fedora-Cloud-Base-24-20160420.n.0 (24)' + \
        '(Fedora-24-20160420.n.0) is queued for testing'
    expected_link = 'https://apps.fedoraproject.org/autocloud/jobs/27/output'
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
            u'compose_id': u'Fedora-24-20160420.n.0',
            u'compose_url': u'http://kojipkgs.fedoraproject.org/compose//" + \
            "branched/Fedora-24-20160420.n.0/compose/CloudImages/x86_64/" + \
            "images/Fedora-Cloud-Base-24-20160420.n.0.x86_64.qcow2',
            u'family': u'Base',
            u'image_name': u'Fedora-Cloud-Base-24-20160420.n.0',
            u'job_id': 27,
            u'release': u'24',
            u'status': u'queued',
            u'type': u'qcow2'
        },
    }


class TestImageTestRunning(Base):
    """ These messages are published when tests for an image starts
    in Autocloud app.
    """
    expected_title = "autocloud.image.running"
    expected_subti = 'The tests for the Fedora-Cloud-Base-24-20160420.n.0' + \
        ' (24)(Fedora-24-20160420.n.0) have started running'
    expected_link = 'https://apps.fedoraproject.org/autocloud/jobs/27/output'
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
            u'compose_id': u'Fedora-24-20160420.n.0',
            u'compose_url': u'http://kojipkgs.fedoraproject.org/compose//" + \
            "branched/Fedora-24-20160420.n.0/compose/CloudImages/x86_64/" + \
            "images/Fedora-Cloud-Base-24-20160420.n.0.x86_64.qcow2',
            u'family': u'Base',
            u'image_name': u'Fedora-Cloud-Base-24-20160420.n.0',
            u'job_id': 27,
            u'release': u'24',
            u'status': u'running',
            u'type': u'qcow2'
        },
    }


class TestImageTestAborted(Base):
    """ These messages are published when tests for an image aborts
    in Autocloud app.
    """
    expected_title = "autocloud.image.aborted"
    expected_subti = 'The tests for the Fedora-Cloud-Base-24-20160420.n.0 ' + \
        '(24)(Fedora-24-20160420.n.0) have been aborted'
    expected_link = 'https://apps.fedoraproject.org/autocloud/jobs/27/output'
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
            u'compose_id': u'Fedora-24-20160420.n.0',
            u'compose_url': u'http://kojipkgs.fedoraproject.org/compose//" + \
            "branched/Fedora-24-20160420.n.0/compose/CloudImages/x86_64/" + \
            "images/Fedora-Cloud-Base-24-20160420.n.0.x86_64.qcow2',
            u'family': u'Base',
            u'image_name': u'Fedora-Cloud-Base-24-20160420.n.0',
            u'job_id': 27,
            u'release': u'24',
            u'status': u'aborted',
            u'type': u'qcow2'
        },
    }


class TestImageTestFailed(Base):
    """ These messages are published when tests for an image failed
    in Autocloud app.
    """
    expected_title = "autocloud.image.failed"
    expected_subti = 'The tests for the Fedora-Cloud-Base-24-20160420.n.0 ' + \
        '(24)(Fedora-24-20160420.n.0) failed'
    expected_link = 'https://apps.fedoraproject.org/autocloud/jobs/27/output'
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
            u'compose_id': u'Fedora-24-20160420.n.0',
            u'compose_url': u'http://kojipkgs.fedoraproject.org/compose//" + \
            "branched/Fedora-24-20160420.n.0/compose/CloudImages/x86_64/" + \
            "images/Fedora-Cloud-Base-24-20160420.n.0.x86_64.qcow2',
            u'family': u'Base',
            u'image_name': u'Fedora-Cloud-Base-24-20160420.n.0',
            u'job_id': 27,
            u'release': u'24',
            u'status': u'failed',
            u'type': u'qcow2'
        },
    }


class TestImageTestSuccess(Base):
    """ These messages are published when tests for an image successfully
    completes in Autocloud app.
    """
    expected_title = "autocloud.image.success"
    expected_subti = 'The tests for Fedora-Cloud-Base-24-20160420.n.0 (24)' + \
        '(Fedora-24-20160420.n.0) were a success'
    expected_link = 'https://apps.fedoraproject.org/autocloud/jobs/27/output'
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
            u'compose_id': u'Fedora-24-20160420.n.0',
            u'compose_url': u'http://kojipkgs.fedoraproject.org/compose//" + \
            "branched/Fedora-24-20160420.n.0/compose/CloudImages/x86_64/" + \
            "images/Fedora-Cloud-Base-24-20160420.n.0.x86_64.qcow2',
            u'family': u'Base',
            u'image_name': u'Fedora-Cloud-Base-24-20160420.n.0',
            u'job_id': 27,
            u'release': u'24',
            u'status': u'success',
            u'type': u'qcow2'
        },
    }


class ComposeTestQueued(Base):
    """ These messages are published when compose queued for testing
    in Autocloud app.
    """
    expected_title = 'autocloud.compose.queued'
    expected_subti = 'Fedora-24-20160419.n.1 is queued for testing'
    expected_link = 'https://apps.fedoraproject.org/autocloud/jobs/37'
    expected_secondary_icon = "https://apps.fedoraproject.org/img/icons/" + \
        "fedimg.png"
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set(['autocloud/compose/queued'])
    msg = {
        u'username': u'apache',
        u'i': 1,
        u'timestamp': 1379638157.759283,
        u'msg_id': u'2015-4b5aae66-b713-4c22-bb4a-1277d4402375',
        u'topic': u'org.fedoraproject.prod.autocloud.compose.queued',
        u'msg': {
            u'status': u'queued',
            u'respin': 1,
            u'release': u'24',
            u'compose_job_id': 37,
            u'date': u'20160419',
            u'type': u'nightly',
            u'id': u'Fedora-24-20160419.n.1'
        }
    }


class ComposeTestRunning(Base):
    """ These messages are published when tests for a compose has started
    running in Autocloud app.
    """
    expected_title = "autocloud.compose.running"
    expected_subti = 'Fedora-24-20160419.n.1 tests have started running'
    expected_link = 'https://apps.fedoraproject.org/autocloud/jobs/37'
    expected_secondary_icon = "https://apps.fedoraproject.org/img/icons/" + \
        "fedimg.png"
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set(['autocloud/compose/running'])
    msg = {
        u'username': u'apache',
        u'i': 1,
        u'timestamp': 1379638157.759283,
        u'msg_id': u'2015-4b5aae66-b713-4c22-bb4a-1277d4402375',
        u'topic': u'org.fedoraproject.prod.autocloud.compose.running',
        u'msg': {
            u'status': u'running',
            u'respin': 1,
            u'release': u'24',
            u'compose_job_id': 37,
            u'date': u'20160419',
            u'type': u'nightly',
            u'id': u'Fedora-24-20160419.n.1'
        }
    }


class ComposeTestCompleted(Base):
    """ These messages are published when tests for a compose completes
    in Autocloud app.
    """
    expected_title = "autocloud.compose.complete"
    expected_subti = 'Fedora-24-20160419.n.1 tests have completed'
    expected_link = 'https://apps.fedoraproject.org/autocloud/jobs/37'
    expected_secondary_icon = "https://apps.fedoraproject.org/img/icons/" + \
        "fedimg.png"
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set(['autocloud/compose/completed'])
    msg = {
        u'username': u'apache',
        u'i': 1,
        u'timestamp': 1379638157.759283,
        u'msg_id': u'2015-4b5aae66-b713-4c22-bb4a-1277d4402375',
        u'topic': u'org.fedoraproject.prod.autocloud.compose.complete',
        u'msg': {
            u'status': u'completed',
            u'respin': 1,
            u'release': u'24',
            u'results': {
                u'failed': 0,
                u'success': 6
            },
            u'compose_job_id': 37,
            u'date': u'20160419',
            u'type': u'nightly',
            u'id': u'Fedora-24-20160419.n.1'
        }
    }


class LegacyComposeTestRunning(Base):
    """ These messages are published when tests for a compose has started
    running in Autocloud app.
    """
    expected_title = "autocloud.compose.running"
    expected_subti = 'Fedora-24-20160419.n.1 tests have started running'
    expected_link = 'https://apps.fedoraproject.org/autocloud/'
    expected_secondary_icon = "https://apps.fedoraproject.org/img/icons/" + \
        "fedimg.png"
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set(['autocloud/compose/running'])
    msg = {
        u'username': u'apache',
        u'i': 1,
        u'timestamp': 1379638157.759283,
        u'msg_id': u'2015-4b5aae66-b713-4c22-bb4a-1277d4402375',
        u'topic': u'org.fedoraproject.prod.autocloud.compose.running',
        u'msg': {
            u'status': u'running',
            u'respin': 1,
            u'release': u'24',
            u'date': u'20160419',
            u'type': u'nightly',
            u'id': u'Fedora-24-20160419.n.1'
        }
    }


class LegacyComposeTestCompleted(Base):
    """ These messages are published when tests for a compose completes
    in Autocloud app.
    """
    expected_title = "autocloud.compose.complete"
    expected_subti = 'Fedora-24-20160419.n.1 tests have completed'
    expected_link = 'https://apps.fedoraproject.org/autocloud/jobs/37'
    expected_secondary_icon = "https://apps.fedoraproject.org/img/icons/" + \
        "fedimg.png"
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set(['autocloud/compose/completed'])
    msg = {
        u'username': u'apache',
        u'i': 1,
        u'timestamp': 1379638157.759283,
        u'msg_id': u'2015-4b5aae66-b713-4c22-bb4a-1277d4402375',
        u'topic': u'org.fedoraproject.prod.autocloud.compose.complete',
        u'msg': {
            u'status': u'completed',
            u'respin': 1,
            u'release': u'24',
            u'results': {
                u'failed': 0,
                u'success': 6
            },
            u'compose_job_id': 37,
            u'date': u'20160419',
            u'type': u'nightly',
            u'compose_id': u'Fedora-24-20160419.n.1'
        }
    }


class LegacyDefaultComposeTestCompleted(Base):
    """ These messages are published when tests for a compose completes
    in Autocloud app but the message has both compose_id and id key missing
    """
    expected_title = "autocloud.compose.complete"
    expected_subti = 'A compose tests have completed'
    expected_link = 'https://apps.fedoraproject.org/autocloud/jobs/37'
    expected_secondary_icon = "https://apps.fedoraproject.org/img/icons/" + \
        "fedimg.png"
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set(['autocloud/compose/completed'])
    msg = {
        u'username': u'apache',
        u'i': 1,
        u'timestamp': 1379638157.759283,
        u'msg_id': u'2015-4b5aae66-b713-4c22-bb4a-1277d4402375',
        u'topic': u'org.fedoraproject.prod.autocloud.compose.complete',
        u'msg': {
            u'status': u'completed',
            u'respin': 1,
            u'release': u'24',
            u'results': {
                u'failed': 0,
                u'success': 6
            },
            u'compose_job_id': 37,
            u'date': u'20160419',
            u'type': u'nightly',
        }
    }


class LegacyTestImageTestQueued(Base):
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


class LegacyTestImageTestRunning(Base):
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


class LegacyTestImageTestAborted(Base):
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


class LegacyTestImageTestFailed(Base):
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


class LegacyTestImageTestSuccess(Base):
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
