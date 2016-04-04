# This file is part of fedmsg.
# Copyright (C) 2016 Red Hat, Inc.
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
# Authors:  Adam Williamson <awilliam@redhat.com>
#
"""Tests for openQA messages."""

import unittest
from fedmsg.tests.test_meta import Base
from .common import add_doc

class TestOpenQAJobDuplicateAuto(Base):
    """openQA emits messages on this topic when a job is duplicated.
    The 'id' is the job that was duplicated, the 'result' is the new
    job.
    """
    expected_title = "openqa.job.duplicate"
    expected_subti = ("job 10625 automatically duplicated as 10695 for "
                      "Fedora-24-20160323.n.0")
    expected_link = "https://openqa.fedoraproject.org/tests/10625"
    expected_objects = set(["Fedora-24-20160323.n.0"])
    msg = {
        "i": 1,
        "msg": {
            "auto": "1",
            "build": "Fedora-24-20160323.n.0",
            "id": "10625",
            "remaining": 39,
            "result": "10695"
        },
        "msg_id": "2016-809a50c2-0829-46b7-beb1-e9cf0ed2ca1a",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1458740621.0,
        "topic": "org.fedoraproject.prod.openqa.job.duplicate"
    }


class TestOpenQAJobDuplicateManual(Base):
    """openQA emits messages on this topic when a job is duplicated.
    The 'id' is the job that was duplicated, the 'result' is the new
    job.
    """
    # here we're testing the 'manual' vs. 'auto' difference
    expected_title = "openqa.job.duplicate"
    expected_subti = ("job 10625 manually duplicated as 10695 for "
                      "Fedora-24-20160323.n.0")
    expected_link = "https://openqa.fedoraproject.org/tests/10625"
    expected_objects = set(["Fedora-24-20160323.n.0"])
    msg = {
        "i": 1,
        "msg": {
            "auto": "0",
            "build": "Fedora-24-20160323.n.0",
            "id": "10625",
            "remaining": 39,
            "result": "10695"
        },
        "msg_id": "2016-809a50c2-0829-46b7-beb1-e9cf0ed2ca1a",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1458740621.0,
        "topic": "org.fedoraproject.prod.openqa.job.duplicate"
    }


class TestOpenQAJobRestart(Base):
    """openQA emits messages on this topic when a job is restarted.
    The 'id' is the job that was restarted, the 'result' is the id of
    the new job.
    """
    expected_title = "openqa.job.restart"
    expected_subti = "job 10589 restarted as 10619 for Fedora-24-20160322.4"
    expected_link = "https://openqa.fedoraproject.org/tests/10589"
    msg = {
        "i": 1,
        "msg": {
            "build": "Fedora-24-20160322.4",
            "id": "10589",
            "remaining": 2,
            "result": "10619"
        },
        "msg_id": "2016-02ec7b3a-ca9d-4844-8361-f46bc883a91d",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1458702088.0,
        "topic": "org.fedoraproject.prod.openqa.job.restart"
    }

class TestOpenQAJobDoneStaging(Base):
    """openQA emits messages on this topic when a job completes.
    'remaining' indicates the number of jobs for the same compose that
    are either running or waiting to start. 'result' should indicate
    the result of the job, but at present it is always None due to
    upstream openQA issues.
    """
    expected_title = "openqa.job.done"
    expected_subti = ("staging job 10826 completed for "
                      "Fedora-Rawhide-20160323.n.0, 23 remaining jobs")
    expected_link = "https://openqa.stg.fedoraproject.org/tests/10826"
    msg = {
        "i": 1,
        "msg": {
            "build": "Fedora-Rawhide-20160323.n.0",
            "id": "10826",
            "newbuild": None,
            "remaining": 23,
            "result": None,
        },
        "msg_id": "2016-fb9690a0-96fd-41e7-a532-0547a4b9229b",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1458779794.0,
        "topic": "org.fedoraproject.stg.openqa.job.done"
    }

add_doc(locals())

if __name__ == '__main__':
    unittest.main()
