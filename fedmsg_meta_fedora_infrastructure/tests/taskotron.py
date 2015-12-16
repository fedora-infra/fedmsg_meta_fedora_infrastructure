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
# Authors:  Martin Krizek <mkrizek@redhat.com>
#           Ralph Bean <rbean@redhat.com>
#
""" Tests for taskotron messages """

import os
import unittest

from fedmsg.tests.test_meta import Base

from .common import add_doc


class TestTaskotronResultNew(Base):
    """ Taskotron emits messages on this topic anytime a task finishes.

    Here's an example message of a new **taskotron result** published about a
    **koji build**.
    """
    expected_title = "taskotron.result.new"
    expected_subti = "fedoratest PASSED for foobar-1.0-1.fc99"
    expected_link = ("https://taskotron.fedoraproject.org/taskmaster/"
                     "/builders/x86_64/builds/1/steps/runtask/logs/stdio")
    expected_secondary_icon = ("https://apps.fedoraproject.org/packages/"
                               "images/icons/foobar.png")
    expected_packages = set(['foobar'])
    expected_objects = set(['fedoratest/foobar/PASSED'])
    msg = {
        u'username': u'taskotron',
        u'i': 1,
        u'timestamp': 1389298195,
        u'msg_id': u'2014-10b5b1b6-42c7-4d64-aeae-5029b9515d47',
        u'topic': u'org.fedoraproject.stg.taskotron.result.new',
        u'msg': {
            u'task': {
                'name': 'fedoratest',
                'type': 'koji_build',
                'item': 'foobar-1.0-1.fc99',
            },
            u'result': {
                'id': '1',
                'submit_time': '2015-01-30 13:11:35.366862',
                'outcome': 'PASSED',
                'job_url': 'https://taskotron.fedoraproject.org/resultsdb/jobs/1',
                'log_url': ('https://taskotron.fedoraproject.org/taskmaster/'
                           '/builders/x86_64/builds/1/steps/runtask/logs/stdio'),
            },
        }
    }


class TestTaskotronBodhiUpdate(Base):
    """ Taskotron emits messages on this topic anytime a task finishes.

    Here's an example message of a new **taskotron result** published about a
    **bodhi update**.
    """
    expected_title = "taskotron.result.new"
    expected_subti = "upgradepath PASSED for FEDORA-2015-2f6c7508b7"
    expected_link = ("https://taskotron.fedoraproject.org/artifacts/"
                     "all/64981220-a418-11e5-91ee-52540053ee00/"
                     "task_output/FEDORA-2015-2f6c7508b7.log")
    msg = {
        "i": 177,
        "timestamp": 1450286061.0,
        "msg_id": "2015-2ff9d8af-8263-4886-8e3d-61cc7a5eeeb4",
        "topic": "org.fedoraproject.prod.taskotron.result.new",
        "msg": {
            "task": {
                "item": "FEDORA-2015-2f6c7508b7",
                "type": "bodhi_update",
                "name": "upgradepath"
            },
            "result": {
                "job_url": ("https://taskotron.fedoraproject.org/execdb/"
                            "/jobs/64981220-a418-11e5-91ee-52540053ee00"),
                "submit_time": "2015-12-16 17:14:21 UTC",
                "outcome": "PASSED",
                "id": 5202575,
                "log_url": ("https://taskotron.fedoraproject.org/artifacts/"
                            "all/64981220-a418-11e5-91ee-52540053ee00/"
                            "task_output/FEDORA-2015-2f6c7508b7.log"),
            }
        }
    }


#  only run these two tests if we have network connectivity.
#  (they'll fail in koji)
if not 'FEDMSG_META_NO_NETWORK' in os.environ:
    TestTaskotronBodhiUpdate.expected_secondary_icon = (
        "https://apps.fedoraproject.org/packages/"
        "images/icons/copy-jdk-configs.png")
    TestTaskotronBodhiUpdate.expected_packages = set(['copy-jdk-configs'])
    TestTaskotronBodhiUpdate.expected_objects = set([
        'upgradepath/copy-jdk-configs/PASSED'])


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
