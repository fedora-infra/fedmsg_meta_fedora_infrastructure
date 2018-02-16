# This file is part of fedmsg.
# Copyright (C) 2018 Red Hat, Inc.
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
# Authors:  Pierre-Yves Chibon <pingou@pingoured.fr>
#
""" Tests for pagure messages """

import unittest

from fedmsg_meta_fedora_infrastructure.tests.base import Base

from .common import add_doc


class TestSimpleKojiCiPR(Base):
    """ These messages are published when someone asks for a re-run of
    simple-koji-ci on a pull-request on `dist-git
    <https://src.fedoraproject.org/>`_.
    """
    expected_title = "rats.test.simple-koji-ci"
    expected_subti = 'pingou requested a run of simple-koji-ci on ' + \
        '"rpms/python-arrow/pull-request/13"'
    expected_link = "https://src.fedoraproject.org/rpms/python-arrow/pull-request/13"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['simple-koji-ci/rpms/python-arrow/pull-request/13'])
    msg = {
      "i": 1,
      "timestamp": 1515756462,
      "msg_id": "2018-40a4a95d-9274-4972-be1b-db43a1959012",
      "topic": "org.fedoraproject.dev.rats.test.simple-koji-ci",
      "msg": {
        "agent": "pingou",
        "extras": {},
        "pull_request": {
          "status": "Open",
          "last_updated": "1506692613",
          "branch_from": "master",
          "uid": "11700bb635a94953b449c8de14d2d16d",
          "title": "Test PR",
          "initial_comment": None,
          "comments": [],
          "id": 13,
          "project": {
            "custom_keys": [],
            "description": "The python-arrow rpms",
            "parent": None,
            "date_modified": "1507625578",
            "access_users": {
              "admin": [
                "pingou"
              ],
              "commit": [],
              "ticket": [],
              "owner": [
                "ralph"
              ]
            },
            "namespace": "rpms",
            "priorities": {},
            "id": 16710,
            "access_groups": {
              "admin": [],
              "commit": [
                "infra-sig"
              ],
              "ticket": []
            },
            "milestones": {},
            "user": {
              "fullname": "Ralph Bean",
              "name": "ralph"
            },
            "date_created": "1501276912",
            "fullname": "rpms/python-arrow",
            "url_path": "rpms/python-arrow",
            "close_status": [],
            "tags": [],
            "name": "python-arrow"
          },
          "commit_stop": "f71b3aa0f313d34eabb8b182619314de37c67c90",
          "repo_from": None,
          "updated_on": "1506619100",
          "assignee": None,
          "commit_start": "b9750aae92def8c714a3378c8086d0f3c90ffcc0",
          "branch": "master",
          "date_created": "1506619100",
          "remote_git": None,
          "closed_at": None,
          "closed_by": None,
          "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
          }
        },
        "test": "simple-koji-ci",
        "identifier": "rpms/python-arrow/pull-request/13",
        "result_id": None
      }
    }


class TestTaskotronBuild(Base):
    """ These messages are published when someone asks for a re-run of
    a specific test on taskotron for a specific build.
    """
    expected_title = "rats.test.taskotron"
    expected_subti = 'pingou requested a run of taskotron\'s ' + \
        'dist.rpmdeplint on "audit-2.8-1.fc26"'
    expected_link = None
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['taskotron/dist.rpmdeplint/audit-2.8-1.fc26'])
    msg = {
      "i": 1,
      "timestamp": 1515768967,
      "msg_id": "2018-96b2b575-0b83-412d-b931-6cf73b653011",
      "topic": "org.fedoraproject.dev.rats.test.taskotron",
      "msg": {
        "agent": "pingou",
        "extras": {
          "groups": "foobar"
        },
        "groups": "foobar",
        "test": "dist.rpmdeplint",
        "identifier": "audit-2.8-1.fc26",
        "result_id": None
      }
    }


class TestTaskotronResultId(Base):
    """ These messages are published when someone asks for a re-run of
    a specific test on taskotron from a resultsdb's result identifier.
    """
    expected_title = "rats.test.taskotron"
    expected_subti = 'pingou requested a run of taskotron on ' + \
        'resultsdb\'s result id: "17783947"'
    expected_link = None
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['taskotron/resultsdb/17783947'])
    msg = {
      "i": 1,
      "timestamp": 1515770465,
      "msg_id": "2018-aacc5b52-a3a2-4b34-a111-3a4cde2eead4",
      "topic": "org.fedoraproject.dev.rats.test.taskotron",
      "msg": {
        "agent": "pingou",
        "extras": {},
        "groups": [
          "7275e744-90a2-58ee-9973-b0d6fa7c0267",
          "cf4f1f88-e873-5432-86a4-15a12e400f87",
          "0f3309ea-6d4c-59b2-b422-d73e9b8511f3"
        ],
        "test": None,
        "identifier": None,
        "result_id": "17783947"
      }
    }


class TestAtomicCIPR(Base):
    """ These messages are published when someone asks for a re-run of
    the Atomic CI pipeline from a pull-request.
    """
    expected_title = "rats.test.atomic-ci"
    expected_subti = 'pingou requested a run of atomic-ci on ' + \
        '"rpms/python-arrow/pull-request/13"'
    expected_link = None
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['AtomicCI/rpms/python-arrow/pull-request/13'])
    msg = {
      "i": 4,
      "timestamp": 1516010094,
      "msg_id": "2018-a7b54439-4bb8-48e5-87b7-975fea6efd15",
      "topic": "org.fedoraproject.dev.rats.test.atomic-ci",
      "msg": {
        "old_result": None,
        "agent": "pingou",
        "extras": {},
        "pull_request": {
          "status": "Open",
          "last_updated": "1506692613",
          "branch_from": "master",
          "uid": "11700bb635a94953b449c8de14d2d16d",
          "title": "Test PR",
          "initial_comment": None,
          "comments": [
            {
              "comment": "test comment\r\n\r\nEdited2",
              "parent": None,
              "notification": False,
              "tree": None,
              "filename": None,
              "edited_on": "1506692613",
              "editor": {
                "fullname": "Pierre-YvesChibon",
                "name": "pingou"
              },
              "date_created": "1506689892",
              "commit": None,
              "line": None,
              "id": 27,
              "user": {
                "fullname": "Pierre-YvesChibon",
                "name": "pingou"
              }
            }
          ],
          "id": 13,
          "project": {
            "custom_keys": [],
            "description": "The python-arrow rpms",
            "parent": None,
            "date_modified": "1507625578",
            "access_users": {
              "admin": [
                "pingou"
              ],
              "commit": [],
              "ticket": [],
              "owner": [
                "ralph"
              ]
            },
            "namespace": "rpms",
            "priorities": {},
            "id": 16710,
            "access_groups": {
              "admin": [],
              "commit": [
                "infra-sig"
              ],
              "ticket": []
            },
            "milestones": {},
            "user": {
              "fullname": "Ralph Bean",
              "name": "ralph"
            },
            "date_created": "1501276912",
            "fullname": "rpms/python-arrow",
            "url_path": "rpms/python-arrow",
            "close_status": [],
            "tags": [],
            "name": "python-arrow"
          },
          "commit_stop": "f71b3aa0f313d34eabb8b182619314de37c67c90",
          "repo_from": None,
          "updated_on": "1506619100",
          "assignee": None,
          "commit_start": "b9750aae92def8c714a3378c8086d0f3c90ffcc0",
          "branch": "master",
          "date_created": "1506619100",
          "remote_git": None,
          "closed_at": None,
          "closed_by": None,
          "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
          }
        },
        "test": "AtomicCI",
        "identifier": "rpms/python-arrow/pull-request/13",
        "result_id": None
      }
    }


class TestAtomicCIResultId(Base):
    """ These messages are published when someone asks for a re-run of
    the Atomic CI pipeline from a resultsdb's result identifier.
    """
    expected_title = "rats.test.atomic-ci"
    expected_subti = 'pingou requested a run of atomic-ci on ' + \
        'resultsdb\'s result id: "17786885"'
    expected_link = None
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['AtomicCI/resultsdb/17786885'])
    msg = {
      "i": 5,
      "timestamp": 1516009806,
      "msg_id": "2018-390b5760-0bfa-4f08-bd98-513c24d2ed7b",
      "topic": "org.fedoraproject.dev.rats.test.atomic-ci",
      "msg": {
        "old_result": {
          "testcase": {
            "ref_url": None,
            "href": "https://taskotron.fedoraproject.org/resultsdb_api/api/v2.0/testcases/org.centos.prod.ci.pipeline.complete",
            "name": "org.centos.prod.ci.pipeline.complete"
          },
          "ref_url": "https://jenkins-continuous-infra.apps.ci.centos.org/job/continuous-infra-ci-pipeline-f27/46/",
          "note": None,
          "href": "https://taskotron.fedoraproject.org/resultsdb_api/api/v2.0/results/17786885",
          "groups": [],
          "submit_time": "2017-10-23T18:12:12.381783",
          "outcome": "PASSED",
          "data": {
            "build_id": [
              "46"
            ],
            "status": [
              "SUCCESS"
            ],
            "msg_id": [
              "2017-2acbcd52-fd49-4d34-8411-70476139cdd8"
            ],
            "group": [
              "None"
            ],
            "nvr": [
              "glusterfs-3.12.2-2.408.202c34e.fc27.x86_64"
            ],
            "ref": [
              "x86_64"
            ],
            "rev": [
              "202c34e6826fd2cba34ee61fc14312126ede808f"
            ],
            "username": [
              "fedora-atomic"
            ],
            "build_url": [
              "https://jenkins-continuous-infra.apps.ci.centos.org/job/continuous-infra-ci-pipeline-f27/46/"
            ],
            "namespace": [
              "rpms"
            ],
            "repo": [
              "glusterfs"
            ],
            "topic": [
              "org.centos.prod.ci.pipeline.complete"
            ],
            "original_spec_nvr": [
              "glusterfs-3.12.2-2.fc27"
            ],
            "centos_ci_resultsdb": [
              "True"
            ],
            "branch": [
              "f27"
            ],
            "centos_ci_resultsdb_id": [
              "32627"
            ],
            "centos_ci_resultsdb_submit_time": [
              "2017-10-23T18:11:13.949695"
            ]
          },
          "id": 17786885
        },
        "agent": "pingou",
        "extras": {},
        "pull_request": None,
        "test": None,
        "identifier": None,
        "result_id": "17786885"
      }
    }

add_doc(locals())

if __name__ == '__main__':
    unittest.main()
