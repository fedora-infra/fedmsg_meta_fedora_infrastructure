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

class TestOpenQACommentCreate(Base):
    """openQA emits messages on this topic when a new comment is
    created.
    """
    expected_title = "openqa.comment.create"
    expected_subti = (
        "perci created comment #1 on openQA job 15052, text: test comment")
    expected_link = "https://openqa.fedoraproject.org/tests/15052#comments"
    expected_objects = set([15052])
    expected_usernames = set(['perci'])
    msg = {
        "i": 1,
        "msg": {
            "created": "2016-12-01T12:22:52Z",
            "group_id": None,
            "id": 1,
            "job_id": 15052,
            "text": "test comment",
            "updated": "2016-12-01T12:22:52Z",
            "user": "perci"
        },
        "msg_id": "2016-809a50c2-0829-46b7-beb1-e9cf0ed2ca1a",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1458740621.0,
        "topic": "org.fedoraproject.prod.openqa.comment.create"
    }

class TestOpenQACommentUpdate(Base):
    """openQA emits messages on this topic when a comment is updated.
    """
    expected_title = "openqa.comment.update"
    expected_subti = (
        "perci updated comment #2 on openQA group 1, text: "
        "some text longer than 30 chara...")
    expected_link = "https://openqa.fedoraproject.org/group_overview/1"
    expected_objects = set([1])
    expected_usernames = set(['perci'])
    msg = {
        "i": 1,
        "msg": {
            "created": "2016-12-01T12:22:52Z",
            "group_id": 1,
            "id": 2,
            "job_id": None,
            "text": "some text longer than 30 characters",
            "updated": "2016-12-01T12:22:52Z",
            "user": "perci"
        },
        "msg_id": "2016-809a50c2-0829-46b7-beb1-e9cf0ed2ca1a",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1458740621.0,
        "topic": "org.fedoraproject.prod.openqa.comment.update"
    }

class TestOpenQACommentDelete(Base):
    """openQA emits messages on this topic when a comment is deleted.
    """
    expected_title = "openqa.comment.delete"
    expected_subti = (
        "perci deleted comment #1 on openQA job 15052, text: test comment")
    expected_link = "https://openqa.fedoraproject.org/tests/15052#comments"
    expected_objects = set([15052])
    expected_usernames = set(['perci'])
    msg = {
        "i": 1,
        "msg": {
            "created": "2016-12-01T12:22:52Z",
            "group_id": None,
            "id": 1,
            "job_id": 15052,
            "text": "test comment",
            "updated": "2016-12-01T12:22:52Z",
            "user": "perci"
        },
        "msg_id": "2016-809a50c2-0829-46b7-beb1-e9cf0ed2ca1a",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1458740621.0,
        "topic": "org.fedoraproject.prod.openqa.comment.delete"
    }

class TestOpenQAJobDuplicateAuto(Base):
    """openQA emits messages on this topic when a job is duplicated.
    The 'id' is the job that was duplicated, the 'result' is the new
    job.
    """
    expected_title = "openqa.job.duplicate"
    expected_subti = (
        "job 10625 (test base_selinux on 64bit for iso "
        "Fedora-Everything-netinst-x86_64-24-20160323.n.0.iso) automatically "
        "duplicated as 10695 for Fedora-24-20160323.n.0")
    expected_link = "https://openqa.fedoraproject.org/tests/10625"
    expected_objects = set(
        ["Fedora-24-20160323.n.0",
         "Fedora-Everything-netinst-x86_64-24-20160323.n.0.iso"])
    msg = {
        "i": 1,
        "msg": {
            "ARCH": "x86_64",
            "BUILD": "Fedora-24-20160323.n.0",
            "FLAVOR": "Everything-boot-iso",
            "ISO": "Fedora-Everything-netinst-x86_64-24-20160323.n.0.iso",
            "MACHINE": "64bit",
            "TEST": "base_selinux",
            "auto": "1",
            "id": 10625,
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
    expected_subti = (
        "job 10625 (test base_selinux on 64bit for iso "
        "Fedora-Everything-netinst-x86_64-24-20160323.n.0.iso) manually "
        "duplicated as 10695 for Fedora-24-20160323.n.0")
    expected_link = "https://openqa.fedoraproject.org/tests/10625"
    expected_objects = set(
        ["Fedora-24-20160323.n.0",
         "Fedora-Everything-netinst-x86_64-24-20160323.n.0.iso"])
    # note this test also checks behaviour when both ISO and HDD_1
    # are present vs. only one or the other. Should behave exactly
    # like when only ISO is present, as when both are present, HDD_1
    # is usually a test asset that is of no external interest.
    msg = {
        "i": 1,
        "msg": {
            "ARCH": "x86_64",
            "BUILD": "Fedora-24-20160323.n.0",
            "FLAVOR": "Everything-boot-iso",
            "HDD_1": "disk_Everything-boot-iso_64bit.qcow2",
            "ISO": "Fedora-Everything-netinst-x86_64-24-20160323.n.0.iso",
            "MACHINE": "64bit",
            "TEST": "base_selinux",
            "auto": "0",
            "id": 10625,
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
    expected_subti = (
        "job 10589 (test server_simple_encrypted on uefi for iso "
        "Fedora-Everything-netinst-x86_64-24_Alpha-1.7.iso) restarted as "
        "10619 for Fedora-24-20160322.4")
    expected_link = "https://openqa.fedoraproject.org/tests/10589"
    expected_objects = set(
        ["Fedora-24-20160322.4",
         "Fedora-Everything-netinst-x86_64-24_Alpha-1.7.iso"])
    msg = {
        "i": 1,
        "msg": {
            "ARCH": "x86_64",
            "BUILD": "Fedora-24-20160322.4",
            "FLAVOR": "universal",
            "ISO": "Fedora-Everything-netinst-x86_64-24_Alpha-1.7.iso",
            "MACHINE": "uefi",
            "TEST": "server_simple_encrypted",
            "id": 10589,
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
    expected_subti = (
        "staging job 10826 (test install_xfs on 64bit for iso "
        "Fedora-Everything-netinst-x86_64-Rawhide-20160323.n.0.iso) completed "
        "for Fedora-Rawhide-20160323.n.0, 23 remaining jobs")
    expected_link = "https://openqa.stg.fedoraproject.org/tests/10826"
    expected_objects = set(
        ["Fedora-Rawhide-20160323.n.0",
         "Fedora-Everything-netinst-x86_64-Rawhide-20160323.n.0.iso"])
    msg = {
        "i": 1,
        "msg": {
            "ARCH": "x86_64",
            "BUILD": "Fedora-Rawhide-20160323.n.0",
            "FLAVOR": "universal",
            "ISO": "Fedora-Everything-netinst-x86_64-Rawhide-20160323.n.0.iso",
            "MACHINE": "64bit",
            "TEST": "install_xfs",
            "id": 10826,
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

class TestOpenQAHdd1(Base):
    """Here we check that a message with HDD_1 and no ISO behaves as
    expected (subtitle should refer to the disk image and it should be
    in the objects set). As I'm writing this we don't actually have
    any such messages, this is future-proofing for when we add ARM
    tests soon, so the message is faked up based on the previous test.
    """
    # This is a corner case behaviour test and we don't want the doc
    # string showing up in openqa.job.done docs.
    nodoc = True
    expected_title = "openqa.job.done"
    expected_subti = (
        "staging job 10826 (test base_selinux on arm for disk "
        "Fedora-Minimal-armhfp-Rawhide-20160323.0-sda.raw.xz) completed for "
        "Fedora-Rawhide-20160323.n.0, 23 remaining jobs")
    expected_link = "https://openqa.stg.fedoraproject.org/tests/10826"
    expected_objects = set(
        ["Fedora-Rawhide-20160323.n.0",
         "Fedora-Minimal-armhfp-Rawhide-20160323.0-sda.raw.xz"])
    msg = {
        "i": 1,
        "msg": {
            "ARCH": "armhfp",
            "BUILD": "Fedora-Rawhide-20160323.n.0",
            "FLAVOR": "universal",
            "HDD_1": "Fedora-Minimal-armhfp-Rawhide-20160323.0-sda.raw.xz",
            "MACHINE": "arm",
            "TEST": "base_selinux",
            "id": 10826,
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

# LEGACY tests: fedmsg format changed 2016-04 to include more data,
# meta messages were improved. These tests cover the old message
# format and expected meta bits. job IDs are reliably ints after the
# change, may have been unpredictably ints or strings before.

class TestLegacyOpenQAJobDuplicateAuto(Base):
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


class TestLegacyOpenQAJobDuplicateManual(Base):
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


class TestLegacyOpenQAJobRestart(Base):
    """openQA emits messages on this topic when a job is restarted.
    The 'id' is the job that was restarted, the 'result' is the id of
    the new job.
    """
    expected_title = "openqa.job.restart"
    expected_subti = "job 10589 restarted as 10619 for Fedora-24-20160322.4"
    expected_link = "https://openqa.fedoraproject.org/tests/10589"
    expected_objects = set(["Fedora-24-20160322.4"])
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

class TestLegacyOpenQAJobDoneStaging(Base):
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
    expected_objects = set(["Fedora-Rawhide-20160323.n.0"])
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
