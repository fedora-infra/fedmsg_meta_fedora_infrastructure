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
# Authors:  Ralph Bean <rbean@redhat.com>
#
""" Tests for bugzilla2fedmsg messages """

import unittest

from fedmsg_meta_fedora_infrastructure.tests.base import Base

from .common import add_doc


class TestLegacy030BugzillaUpdate(Base):
    """ Even `Red Hat's Bugzilla instance <https://bugzilla.redhat.com>`_ is
    hooked into fedmsg.

    Messages of *this* type were published by bugzilla2fedmsg 0.3.0
    (the state in which it was first deployed, on 2016-03-29) whenever
    someone **updated a bug** on the *Fedora* or *Fedora EPEL* products.
    """

    expected_title = "bugzilla.bug.update"
    expected_subti = "ralph updated 'status', 'resolution', and 'cf_last_closed' on " + \
        "RHBZ#1301537 'RuntimeError: dictionary changed size du...'"
    expected_link = "https://bugzilla.redhat.com/show_bug.cgi?id=1301537"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bugzilla.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
    expected_packages = set(['python-fedora'])
    expected_usernames = set(['ralph', 'puiterwijk'])
    expected_objects = set([
        'Fedora/python-fedora/1301537',
    ])

    msg = {
        "username": None,
        "source_name": "datanommer",
        "i": 1,
        "timestamp": 1459215197,
        "msg_id": "2016-63bc94ba-8a96-4559-841d-3cecbe233db1",
        "topic": "org.fedoraproject.prod.bugzilla.bug.update",
        "msg": {
            "comment": None,
            "bug": {
                "attachments": [],
                "classification": "Fedora",
                "creator": "msuchy@redhat.com",
                "cc": [
                    "cheese@nosuchhost.net",
                    "infra-sig@lists.fedoraproject.org",
                    "jonstanley@gmail.com",
                    # this is an edit from the original message (it was
                    # originally lmacken) to test user name gathering
                    # we also drop ralph from the cc list to make sure
                    # we're picking him up some other way
                    "puiterwijk@gmail.com",
                    "relrod@redhat.com",
                    "ricky@rzhou.org"
                ],
                "depends_on": [],
                "weburl": "https://bugzilla.redhat.com/show_bug.cgi?id=1301537",
                "creation_time": 1453717800.0,
                "docs_contact": "",
                "is_open": False,
                "platform": "Unspecified",
                "keywords": [],
                "summary": "RuntimeError: dictionary changed size during iteration",
                "external_bugs": [],
                "id": 1301537,
                "qa_contact": "extras-qa@fedoraproject.org",
                "severity": "unspecified",
                "is_confirmed": True,
                "is_creator_accessible": True,
                "comments": [
                    {
                        "count": 0,
                        "creator": "msuchy@redhat.com",
                        "text": "Description of problem:\nWhen I call client.group_members(\"packager\") it results in traceback (see below)\n\nVersion-Release number of selected component (if applicable):\npython3-fedora-0.7.1-1.fc23.noarch\n\nHow reproducible:\ndeterministc\n\nSteps to Reproduce:\n#!/usr/bin/python3\nfrom fedora.client import AuthError, AccountSystem\nclient = AccountSystem()\n#client.username = \"msuchy\"\n#client.password = \"XXXX\"\npackagers = client.group_members(\"packager\")\n\nActual results:\n$ ./guard-fedora-sponsors.py\nTraceback (most recent call last):\n  File \"./guard-fedora-sponsors.py\", line 97, in <module>\n    packagers = client.group_members(\"packager\")\n  File \"/usr/lib/python3.4/site-packages/fedora/client/fas2.py\", line 395, in group_members\n    quote(groupname), auth=True)\n  File \"/usr/lib/python3.4/site-packages/fedora/client/baseclient.py\", line 362, in send_request\n    for key, value in auth_params.items() if not value]\n  File \"/usr/lib/python3.4/site-packages/fedora/client/baseclient.py\", line 361, in <listcomp>\n    [auth_params.__delitem__(key)\nRuntimeError: dictionary changed size during iteration",
                        "author": "msuchy@redhat.com",
                        "creation_time": 1453717849.0,
                        "bug_id": 1301537,
                        "creator_id": 206427,
                        "time": 1453717849.0,
                        "id": 9006742,
                        "is_private": False
                    },
                    {
                        "count": 1,
                        "creator": "rbean@redhat.com",
                        "text": "Should be fixed upstream here:  https://github.com/fedora-infra/python-fedora/pull/177/files",
                        "author": "rbean@redhat.com",
                        "creation_time": 1453736234.0,
                        "bug_id": 1301537,
                        "creator_id": 269108,
                        "time": 1453736234.0,
                        "id": 9007748,
                        "is_private": False
                    }
                ],
                "priority": "unspecified",
                "estimated_time": 0.0,
                "version": "23",
                "fixed_in": "",
                "status": "CLOSED",
                "product": "Fedora",
                "blocks": [],
                "description": "Description of problem:\nWhen I call client.group_members(\"packager\") it results in traceback (see below)\n\nVersion-Release number of selected component (if applicable):\npython3-fedora-0.7.1-1.fc23.noarch\n\nHow reproducible:\ndeterministc\n\nSteps to Reproduce:\n#!/usr/bin/python3\nfrom fedora.client import AuthError, AccountSystem\nclient = AccountSystem()\n#client.username = \"msuchy\"\n#client.password = \"XXXX\"\npackagers = client.group_members(\"packager\")\n\nActual results:\n$ ./guard-fedora-sponsors.py\nTraceback (most recent call last):\n  File \"./guard-fedora-sponsors.py\", line 97, in <module>\n    packagers = client.group_members(\"packager\")\n  File \"/usr/lib/python3.4/site-packages/fedora/client/fas2.py\", line 395, in group_members\n    quote(groupname), auth=True)\n  File \"/usr/lib/python3.4/site-packages/fedora/client/baseclient.py\", line 362, in send_request\n    for key, value in auth_params.items() if not value]\n  File \"/usr/lib/python3.4/site-packages/fedora/client/baseclient.py\", line 361, in <listcomp>\n    [auth_params.__delitem__(key)\nRuntimeError: dictionary changed size during iteration",
                "see_also": [],
                "component": "python-fedora",
                "remaining_time": 0.0,
                "target_release": [
                    "---"
                ],
                "groups": [],
                "target_milestone": "---",
                "is_cc_accessible": True,
                "versions": [
                    "23"
                ],
                "url": "",
                "whiteboard": "",
                "last_change_time": 1459215187.0,
                "alias": [],
                "op_sys": "Unspecified",
                "flags": [],
                "components": [
                    "python-fedora"
                ],
                "assigned_to": "infra-sig@lists.fedoraproject.org",
                "resolution": "UPSTREAM",
                "actual_time": 0.0
              },
              "event": {
                  "when": 1459215187.0,
                  "who": "rbean@redhat.com",
                  "changes": [
                    {
                        "removed": "NEW",
                        "added": "CLOSED",
                        "field_name": "status"
                    },
                    {
                        "removed": "",
                        "added": "UPSTREAM",
                        "field_name": "resolution"
                    },
                    {
                        "removed": "",
                        "added": "2016-03-28 21:33:07",
                        "field_name": "cf_last_closed"
                    }
                  ]
              }
          }
    }


class TestLegacy030BugzillaNew(Base):
    """ Even `Red Hat's Bugzilla instance <https://bugzilla.redhat.com>`_ is
    hooked into fedmsg.

    Messages of *this* type were published by bugzilla2fedmsg 0.3.0
    (the state in which it was first deployed, on 2016-03-29) whenever
    someone **filed a new bug** on the *Fedora* or *Fedora EPEL* products.

    Note that the ``event`` field is left empty (``None``) for new bug events.
    """

    expected_title = "bugzilla.bug.new"
    expected_subti = "michal.jnn@gmail.com filed a new bug " + \
        "RHBZ#1321709 'rpm manpage fails to mention multiple, a...'"
    expected_link = "https://bugzilla.redhat.com/show_bug.cgi?id=1321709"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bugzilla.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "cb6f8d7811206a445b4be991eca63896?s=64&d=retro")
    expected_packages = set(['rpm'])
    expected_usernames = set()
    expected_objects = set([
        'Fedora/rpm/1321709',
    ])

    msg = {
      "username": None,
      "source_name": "datanommer",
      "i": 5,
      "timestamp": 1459216044.0,
      "msg_id": "2016-f9c606ca-7011-4c26-8658-ed7d792a4930",
      "crypto": None,
      "topic": "org.fedoraproject.prod.bugzilla.bug.new",
      "headers": {},
      "msg": {
        "comment": {
          "count": 0,
          "creator": "michal.jnn@gmail.com",
          "text": "Description of problem:\n\nIn an output of 'rpm --help' there are options which do not show up in 'man rpm' at all and an output of '--help' is understandably quite terse. This is what looks like the current list:\n --nocontexts\n--macros\n--noplugins\n--xml\n--filetriggers\n--dupes\n--fileclass\n--filecolor\n--fscontext\n--fileprovide\n--filerequire\n--filecaps\n\nAlso a '--usage' fits above but that can be guessed, I think. :-)\n\nVersion-Release number of selected component (if applicable):\nrpm-4.13.0-0.rc1.27.fc25 (and others)",
          "author": "michal.jnn@gmail.com",
          "creation_time": 1459216024.0,
          "bug_id": 1321709,
          "creator_id": 389281,
          "time": 1459216024.0,
          "id": 9185926,
          "is_private": False
        },
        "bug": {
          "attachments": [],
          "classification": "Fedora",
          "creator": "michal.jnn@gmail.com",
          "cc": [
            "jzeleny@redhat.com",
            "lkardos@redhat.com",
            "novyjindrich@gmail.com",
            "packaging-team-maint@redhat.com",
            "pknirsch@redhat.com"
          ],
          "depends_on": [],
          "weburl": "https://bugzilla.redhat.com/show_bug.cgi?id=1321709",
          "creation_time": 1459216020.0,
          "docs_contact": "",
          "is_open": True,
          "platform": "Unspecified",
          "keywords": [],
          "summary": "rpm manpage fails to mention multiple, apparently existing, options",
          "external_bugs": [],
          "id": 1321709,
          "qa_contact": "extras-qa@fedoraproject.org",
          "severity": "unspecified",
          "is_confirmed": True,
          "is_creator_accessible": True,
          "comments": [
            {
              "count": 0,
              "creator": "michal.jnn@gmail.com",
              "text": "Description of problem:\n\nIn an output of 'rpm --help' there are options which do not show up in 'man rpm' at all and an output of '--help' is understandably quite terse. This is what looks like the current list:\n --nocontexts\n--macros\n--noplugins\n--xml\n--filetriggers\n--dupes\n--fileclass\n--filecolor\n--fscontext\n--fileprovide\n--filerequire\n--filecaps\n\nAlso a '--usage' fits above but that can be guessed, I think. :-)\n\nVersion-Release number of selected component (if applicable):\nrpm-4.13.0-0.rc1.27.fc25 (and others)",
              "author": "michal.jnn@gmail.com",
              "creation_time": 1459216024.0,
              "bug_id": 1321709,
              "creator_id": 389281,
              "time": 1459216024.0,
              "id": 9185926,
              "is_private": False
            }
          ],
          "priority": "unspecified",
          "estimated_time": 0.0,
          "version": "rawhide",
          "fixed_in": "",
          "status": "NEW",
          "product": "Fedora",
          "blocks": [],
          "description": "Description of problem:\n\nIn an output of 'rpm --help' there are options which do not show up in 'man rpm' at all and an output of '--help' is understandably quite terse. This is what looks like the current list:\n --nocontexts\n--macros\n--noplugins\n--xml\n--filetriggers\n--dupes\n--fileclass\n--filecolor\n--fscontext\n--fileprovide\n--filerequire\n--filecaps\n\nAlso a '--usage' fits above but that can be guessed, I think. :-)\n\nVersion-Release number of selected component (if applicable):\nrpm-4.13.0-0.rc1.27.fc25 (and others)",
          "see_also": [],
          "component": "rpm",
          "remaining_time": 0.0,
          "target_release": [
            "---"
          ],
          "groups": [],
          "target_milestone": "---",
          "is_cc_accessible": True,
          "versions": [
            "rawhide"
          ],
          "url": "",
          "whiteboard": "",
          "last_change_time": 1459216024.0,
          "alias": [],
          "op_sys": "Unspecified",
          "flags": [],
          "components": [
            "rpm"
          ],
          "assigned_to": "packaging-team-maint@redhat.com",
          "resolution": "",
          "actual_time": 0.0
        },
        "event": None
      }
    }


class TestLegacy84cd3720BugzillaComment(Base):
    """ Even `Red Hat's Bugzilla instance <https://bugzilla.redhat.com>`_ is
    hooked into fedmsg.

    Messages of *this* type were published by bugzilla2fedmsg 84cd3720
    (which stopped including attachments in the bug dict) whenever someone
    **added a comment** on the *Fedora* or *Fedora EPEL* products. This is
    a bugzilla.bug.update message, but there are some specific properties
    of 'comment added' messages we should test. Production was updated to
    84cd3720 (or somewhere around there) very shortly after it was first
    deployed: only the first five messages ever emitted have 'attachments'
    in their 'bug' dict, and it is an empty list in every case.

    The test message is hacked up a bit to test username gathering. In the
    original message, far more things are Ralph: he's in the cc list, the
    bug is assigned to him, and the event 'who' is him too (in reality,
    the comment 'creator' and the event 'who' are always going to be the
    same). We change these values to other ones that are in the mock
    fas_cache so we can test that gathering usernames from all these
    different places works.
    """

    expected_title = "bugzilla.bug.update"
    expected_subti = "ralph commented on " + \
        "RHBZ#1316316 'python-alembic-0.8.5 is available'"
    expected_link = "https://bugzilla.redhat.com/show_bug.cgi?id=1316316"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bugzilla.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
    expected_packages = set(['python-alembic'])
    expected_usernames = set(['puiterwijk', 'nim', 'ralph', 'upstream-release-monitoring'])
    expected_objects = set([
        'Fedora/python-alembic/1316316',
    ])

    msg = {
  "username": None,
  "source_name": "datanommer",
  "i": 1,
  "timestamp": 1459217000.0,
  "msg_id": "2016-946d5113-5d3e-4d38-a538-fbc1155dc8fe",
  "crypto": None,
  "topic": "org.fedoraproject.prod.bugzilla.bug.update",
  "headers": {},
  "source_version": "0.6.5",
  "msg": {
    "comment": {
      "count": 5,
      "creator": "rbean@redhat.com",
      "text": "Built in rawhide.",
      "author": "rbean@redhat.com",
      "creation_time": 1459216972.0,
      "bug_id": 1316316,
      "creator_id": 269108,
      "time": 1459216972.0,
      "id": 9185953,
      "is_private": False
    },
    "bug": {
      "classification": "Fedora",
      "creator": "upstream-release-monitoring@fedoraproject.org",
      "cc": [
        "bob@redhat.com"
      ],
      "depends_on": [],
      "weburl": "https://bugzilla.redhat.com/show_bug.cgi?id=1316316",
      "creation_time": 1457568780.0,
      "docs_contact": "",
      "is_open": False,
      "platform": "Unspecified",
      "keywords": [
        "FutureFeature",
        "Triaged"
      ],
      "summary": "python-alembic-0.8.5 is available",
      "external_bugs": [],
      "id": 1316316,
      "qa_contact": "extras-qa@fedoraproject.org",
      "severity": "unspecified",
      "is_confirmed": True,
      "is_creator_accessible": True,
      "comments": [
        {
          "count": 0,
          "creator": "upstream-release-monitoring@fedoraproject.org",
          "text": "Latest upstream release: 0.8.5\nCurrent version/release in rawhide: 0.8.3-4.fc24\nURL: https://pypi.python.org/pypi/alembic\n\nPlease consult the package updates policy before you issue an update to a stable branch: https://fedoraproject.org/wiki/Updates_Policy\n\nMore information about the service that created this bug can be found at: https://fedoraproject.org/wiki/Upstream_release_monitoring\n\nPlease keep in mind that with any upstream change, there may also be packaging changes that need to be made. Specifically, please remember that it is your responsibility to review the new version to ensure that the licensing is still correct and that no non-free or legally problematic items have been added upstream.",
          "author": "upstream-release-monitoring@fedoraproject.org",
          "creation_time": 1457568796.0,
          "bug_id": 1316316,
          "creator_id": 282165,
          "time": 1457568796.0,
          "id": 9135877,
          "is_private": False
        },
        {
          "count": 1,
          "creator": "upstream-release-monitoring@fedoraproject.org",
          "text": "Patching or scratch build for python-alembic and version 0.8.3 FAILED.\nSee for details",
          "author": "upstream-release-monitoring@fedoraproject.org",
          "creation_time": 1457568808.0,
          "bug_id": 1316316,
          "creator_id": 282165,
          "time": 1457568808.0,
          "id": 9135878,
          "is_private": False
        },
        {
          "count": 2,
          "creator": "upstream-release-monitoring@fedoraproject.org",
          "text": "Rebase helper failed.\nSee logs and attachments in this bugzilla global name 'os' is not defined",
          "author": "upstream-release-monitoring@fedoraproject.org",
          "creation_time": 1457568809.0,
          "bug_id": 1316316,
          "creator_id": 282165,
          "time": 1457568809.0,
          "id": 9135879,
          "is_private": False
        },
        {
          "count": 3,
          "creator": "upstream-release-monitoring@fedoraproject.org",
          "text": "Patches were not touched. All were applied properly",
          "author": "upstream-release-monitoring@fedoraproject.org",
          "creation_time": 1457568811.0,
          "bug_id": 1316316,
          "creator_id": 282165,
          "time": 1457568811.0,
          "id": 9135880,
          "is_private": False
        },
        {
          "count": 4,
          "creator": "upstream-release-monitoring@fedoraproject.org",
          "text": "ralph's python-alembic-0.8.5-1.fc25 completed http://koji.fedoraproject.org/koji/buildinfo?buildID=749417",
          "author": "upstream-release-monitoring@fedoraproject.org",
          "creation_time": 1459216693.0,
          "bug_id": 1316316,
          "creator_id": 282165,
          "time": 1459216693.0,
          "id": 9185947,
          "is_private": False
        },
        {
          "count": 5,
          "creator": "rbean@redhat.com",
          "text": "Built in rawhide.",
          "author": "rbean@redhat.com",
          "creation_time": 1459216972.0,
          "bug_id": 1316316,
          "creator_id": 269108,
          "time": 1459216972.0,
          "id": 9185953,
          "is_private": False
        }
      ],
      "priority": "unspecified",
      "estimated_time": 0.0,
      "version": "rawhide",
      "fixed_in": "",
      "status": "CLOSED",
      "product": "Fedora",
      "blocks": [],
      "description": "Latest upstream release: 0.8.5\nCurrent version/release in rawhide: 0.8.3-4.fc24\nURL: https://pypi.python.org/pypi/alembic\n\nPlease consult the package updates policy before you issue an update to a stable branch: https://fedoraproject.org/wiki/Updates_Policy\n\nMore information about the service that created this bug can be found at: https://fedoraproject.org/wiki/Upstream_release_monitoring\n\nPlease keep in mind that with any upstream change, there may also be packaging changes that need to be made. Specifically, please remember that it is your responsibility to review the new version to ensure that the licensing is still correct and that no non-free or legally problematic items have been added upstream.",
      "see_also": [],
      "component": "python-alembic",
      "remaining_time": 0.0,
      "target_release": [
        "---"
      ],
      "groups": [],
      "target_milestone": "---",
      "is_cc_accessible": True,
      "versions": [
        "rawhide"
      ],
      "url": "",
      "whiteboard": "",
      "last_change_time": 1459216972.0,
      "alias": [],
      "op_sys": "Unspecified",
      "flags": [],
      "components": [
        "python-alembic"
      ],
      "assigned_to": "nicolas.mailhot@laposte.net",
      "resolution": "RAWHIDE",
      "actual_time": 0.0
    },
    "event": {
      "when": 1459216972.0,
      "who": "puiterwijk@gmail.com",
      "changes": [
        {
          "removed": "NEW",
          "added": "CLOSED",
          "field_name": "status"
        },
        {
          "removed": "",
          "added": "RAWHIDE",
          "field_name": "resolution"
        },
        {
          "removed": "",
          "added": "2016-03-28 22:02:52",
          "field_name": "cf_last_closed"
        }
      ]
    }
  }
}


class TestLegacy018492a2BugzillaUpdate(Base):
    """ Even `Red Hat's Bugzilla instance <https://bugzilla.redhat.com>`_ is
    hooked into fedmsg.

    Messages of *this* type were published by bugzilla2fedmsg 018492a2
    (which added stomp headers to the message dict) whenever someone
    **updated a bug** on the *Fedora* or *Fedora EPEL* products. This
    is a sample message from right before Bugzilla 5 was deployed; the
    differences between this and a 2016-03 vintage message aren't that
    big and don't really matter to the processor, but it seems a good
    idea to document the format for future changes.
    """

    expected_title = "bugzilla.bug.update"
    expected_subti = "redhat-bugzilla@linuxnetz.de updated 'flagtypes.name' on " + \
        "RHBZ#1657056 'Please build adplug for EPEL 7'"
    expected_link = "https://bugzilla.redhat.com/show_bug.cgi?id=1657056"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bugzilla.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "3fe422169a76188717509fe0a041c773?s=64&d=retro")
    expected_packages = set(['adplug'])
    expected_usernames = set([])
    expected_objects = set([
        'Fedora/adplug/1657056',
    ])

    msg = {
      "username": "fedmsg",
      "source_name": "datanommer",
      "i": 36,
      "timestamp": 1544313430.0,
      "msg_id": "2018-70b5fc63-f85f-4554-97e9-ddcb901a64aa",
      "crypto": "x509",
      "topic": "org.fedoraproject.prod.bugzilla.bug.update",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "comment": None,
        "headers": {
          "breadcrumbId": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.com-40687-1544310967484-2:146:-1:1:7",
          "expires": "1544918229717",
          "esbSourceSystem": "bugzilla",
          "timestamp": "1544313429717",
          "destination": "/queue/fedora_from_esb",
          "persistent": "true",
          "priority": "4",
          "subscription": "/queue/fedora_from_esb",
          "CamelJmsDeliveryMode": "1",
          "message-id": "ID:messaging-devops-router02.web.prod.ext.phx2.redhat.com-37393-1536884332865-3:22:2:1:2546",
          "esbMessageType": "bugzillaNotification"
        },
        "bug": {
          "classification": "Fedora",
          "creator": "redhat-bugzilla@linuxnetz.de",
          "cc": [
            "triad@df.lth.se"
          ],
          "depends_on": [],
          "weburl": "https://bugzilla.redhat.com/show_bug.cgi?id=1657056",
          "creation_time": 1544140260.0,
          "docs_contact": "",
          "is_open": True,
          "platform": "All",
          "keywords": [],
          "summary": "Please build adplug for EPEL 7",
          "external_bugs": [],
          "id": 1657056,
          "qa_contact": "extras-qa@fedoraproject.org",
          "severity": "medium",
          "is_confirmed": True,
          "is_creator_accessible": True,
          "comments": [
            {
              "count": 0,
              "creator": "redhat-bugzilla@linuxnetz.de",
              "text": "Description of problem:\nPlease build adplug for EPEL 7. Just rebuilding adplug-2.2.1-6.fc29 package\nseems to be sufficient. Updated audacious-plugins are going to depend on it.\n\nVersion-Release number of selected component (if applicable):\nadplug-2.2.1-6.fc29\n\nActual results:\nNo adplug in EPEL 7\n\nExpected results:\nadplug-2.2.1-6.el7 or better ;-)\n\nAdditional info:\nPlease let me know if you are not interested in maintaining the package on\nEPEL 7 branch.",
              "author": "redhat-bugzilla@linuxnetz.de",
              "creation_time": 1544140263.0,
              "bug_id": 1657056,
              "creator_id": 148426,
              "time": 1544140263.0,
              "id": 12282545,
              "is_private": False
            }
          ],
          "priority": "unspecified",
          "estimated_time": 0.0,
          "version": "rawhide",
          "fixed_in": "",
          "status": "NEW",
          "product": "Fedora",
          "blocks": [],
          "description": "Description of problem:\nPlease build adplug for EPEL 7. Just rebuilding adplug-2.2.1-6.fc29 package\nseems to be sufficient. Updated audacious-plugins are going to depend on it.\n\nVersion-Release number of selected component (if applicable):\nadplug-2.2.1-6.fc29\n\nActual results:\nNo adplug in EPEL 7\n\nExpected results:\nadplug-2.2.1-6.el7 or better ;-)\n\nAdditional info:\nPlease let me know if you are not interested in maintaining the package on\nEPEL 7 branch.",
          "see_also": [],
          "component": "adplug",
          "remaining_time": 0.0,
          "target_release": [
            "---"
          ],
          "groups": [],
          "target_milestone": "---",
          "is_cc_accessible": True,
          "versions": [
            "rawhide"
          ],
          "url": "",
          "whiteboard": "",
          "last_change_time": 1544313405.0,
          "alias": [],
          "op_sys": "Linux",
          "flags": [
            {
              "requestee": "triad@df.lth.se",
              "status": "?",
              "name": "needinfo",
              "modification_date": 1544313405.0,
              "type_id": 16,
              "is_active": 1,
              "creation_date": 1544313405.0,
              "id": 3863784,
              "setter": "redhat-bugzilla@linuxnetz.de"
            }
          ],
          "components": [
            "adplug"
          ],
          "assigned_to": "triad@df.lth.se",
          "resolution": "",
          "actual_time": 0.0
        },
        "event": {
          "when": 1544313405.0,
          "who": "redhat-bugzilla@linuxnetz.de",
          "changes": [
            {
              "removed": "",
              "added": "needinfo?(triad@df.lth.se)",
              "field_name": "flagtypes.name"
            }
          ]
        }
      }
    }


class Test031BugzillaUpdate(Base):
    """ Even `Red Hat's Bugzilla instance <https://bugzilla.redhat.com>`_ is
    hooked into fedmsg.

    Messages of *this* type are published by bugzilla2fedmsg 0.3.1
    (the currently-deployed version as of 2019-06-05) whenever someone
    **updates a bug** on the *Fedora* or *Fedora EPEL* products.

    0.3.1 was the first attempt to migrate bugzilla2fedmsg to Bugzilla
    5. The messages are no longer generated based on a Bugzilla db
    query, because the messages Bugzilla emits via the STOMP protocol
    were enhanced considerably in Bugzilla 5: now bugzilla2fedmsg just
    takes the upstream message and messes around with it a bit.
    Unfortunately, 0.3.1 had several bugs which mean the messages have
    a lot of silly fields with 'None' as the value. It also never
    emits 'bugzilla.bug.new' messages because its 'new bug' detection
    is broken - we just get a 'bugzilla.bug.update' message when a bug
    is created. Also, the creation of a comment or an attachment does
    not result in a message being emitted at all.

    This is an example of a fairly not-broken bug update message.
    """

    expected_title = "bugzilla.bug.update"
    expected_subti = "lvrabec@redhat.com updated 'assigned_to', 'bug_status', 'cc', and " + \
        "'component' on RHBZ#1649293 'SELinux is preventing restorecon from 'm...'"
    expected_link = "https://bugzilla.redhat.com/show_bug.cgi?id=1649293"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bugzilla.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "4eb918bfdb582ba411d577a43ebd63c8?s=64&d=retro")
    expected_packages = set(['pcp'])
    expected_usernames = set([])
    expected_objects = set(['Fedora/pcp/1649293'])

    msg = {
      "username": "fedmsg",
      "source_name": "datanommer",
      "i": 2,
      "timestamp": 1545071620.0,
      "msg_id": "2018-7309f571-5227-4b6b-b65b-d7dec586837d",
      "crypto": "x509",
      "topic": "org.fedoraproject.prod.bugzilla.bug.update",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "comment": None,
        "bug": {
          "attachments": None,
          "classification": "Fedora",
          "creator": None,
          "cc": [],
          "depends_on": None,
          "weburl": None,
          "creation_time": "2018-11-13T10:39:32",
          "docs_contact": None,
          "is_open": None,
          "platform": "x86_64",
          "keywords": [],
          "summary": "SELinux is preventing restorecon from 'map' accesses on the fil /usr/sbin/setfiles.",
          "external_bugs": None,
          "id": 1649293,
          "qa_contact": {
            "login": "extras-qa@fedoraproject.org",
            "id": 171387,
            "real_name": "Fedora Extras Quality Assurance"
          },
          "severity": "unspecified",
          "is_confirmed": None,
          "is_creator_accessible": None,
          "comments": None,
          "priority": "unspecified",
          "estimated_time": None,
          "version": {
            "id": 5331,
            "name": "28"
          },
          "fixed_in": None,
          "status": {
            "id": 3,
            "name": "ASSIGNED"
          },
          "product": {
            "id": 49,
            "name": "Fedora"
          },
          "blocks": None,
          "description": None,
          "see_also": None,
          "component": "pcp",
          "remaining_time": None,
          "target_release": None,
          "groups": None,
          "target_milestone": None,
          "is_cc_accessible": None,
          "versions": None,
          "url": "",
          "whiteboard": "abrt_hash:13fc4382f854b589b6f88e73b20a755b3fe143301c7d538dad14bc35c92a0585;",
          "last_change_time": "2018-11-13T10:39:32",
          "alias": [],
          "op_sys": None,
          "flags": [],
          "components": None,
          "assigned_to": "nathans@redhat.com",
          "resolution": "",
          "actual_time": None
        },
        "event": {
          "who": "lvrabec@redhat.com",
          "target": "bug",
          "change_set": "7883.1545071600.05693",
          "routing_key": "bug.modify",
          "bug_id": 1649293,
          "user": {
            "login": "lvrabec@redhat.com",
            "id": 316673,
            "real_name": "Lukas Vrabec"
          },
          "time": "2018-12-17T18:33:20",
          "action": "modify",
          "changes": [
            {
              "field": "assigned_to",
              "removed": "lvrabec@redhat.com",
              "added": "nathans@redhat.com",
              "field_name": "assigned_to"
            },
            {
              "field": "bug_status",
              "removed": "NEW",
              "added": "ASSIGNED",
              "field_name": "bug_status"
            },
            {
              "field": "cc",
              "removed": "",
              "added": "brolley@redhat.com, fche@redhat.com, lberk@redhat.com, mgoodwin@redhat.com, nathans@redhat.com, scox@redhat.com",
              "field_name": "cc"
            },
            {
              "field": "component",
              "removed": "selinux-policy",
              "added": "pcp",
              "field_name": "component"
            }
          ]
        }
      }
    }


class Test031BugzillaNew(Base):
    """ Even `Red Hat's Bugzilla instance <https://bugzilla.redhat.com>`_ is
    hooked into fedmsg.

    Messages of *this* type are published by bugzilla2fedmsg 0.3.1
    (the currently-deployed version as of 2019-06-05) whenever someone
    **creates a bug** on the *Fedora* or *Fedora EPEL* products.

    0.3.1 was the first attempt to migrate bugzilla2fedmsg to Bugzilla
    5. The messages are no longer generated based on a Bugzilla db
    query, because the messages Bugzilla emits via the STOMP protocol
    were enhanced considerably in Bugzilla 5: now bugzilla2fedmsg just
    takes the upstream message and messes around with it a bit.
    Unfortunately, 0.3.1 had several bugs which mean the messages have
    a lot of silly fields with 'None' as the value. It also never
    emits 'bugzilla.bug.new' messages because its 'new bug' detection
    is broken - we just get a 'bugzilla.bug.update' message when a bug
    is created. Also, the creation of a comment or an attachment does
    not result in a message being emitted at all.

    This is an example of the bug 'update' message we get when a new
    bug is created. The processor is able to detect these messages and
    produce a correct subtitle for them.
    """

    expected_title = "bugzilla.bug.update"
    expected_subti = "vaf0001@uah.edu filed a new bug " + \
        "RHBZ#1717615 'VTK inoperative on NVidia'"
    expected_link = "https://bugzilla.redhat.com/show_bug.cgi?id=1717615"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bugzilla.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "2634daafb32dfee24a61cd573b7ab096?s=64&d=retro")
    expected_packages = set(['vtk'])
    expected_usernames = set([])
    expected_objects = set(['Fedora/vtk/1717615'])

    msg = {
      "username": "fedmsg",
      "source_name": "datanommer",
      "certificate": "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUVkekNDQStDZ0F3SUJBZ0lDQWJvd0RRWUpL\nb1pJaHZjTkFRRUZCUUF3Z2FBeEN6QUpCZ05WQkFZVEFsVlQKTVFzd0NRWURWUVFJRXdKT1F6RVFN\nQTRHQTFVRUJ4TUhVbUZzWldsbmFERVhNQlVHQTFVRUNoTU9SbVZrYjNKaApJRkJ5YjJwbFkzUXhE\nekFOQmdOVkJBc1RCbVpsWkcxelp6RVBNQTBHQTFVRUF4TUdabVZrYlhObk1ROHdEUVlEClZRUXBF\nd1ptWldSdGMyY3hKakFrQmdrcWhraUc5dzBCQ1FFV0YyRmtiV2x1UUdabFpHOXlZWEJ5YjJwbFkz\nUXUKYjNKbk1CNFhEVEUwTURZeU1ESXdNREl6TVZvWERUSTBNRFl4TnpJd01ESXpNVm93Z2dFRU1R\nc3dDUVlEVlFRRwpFd0pWVXpFTE1Ba0dBMVVFQ0JNQ1RrTXhFREFPQmdOVkJBY1RCMUpoYkdWcFoy\nZ3hGekFWQmdOVkJBb1REa1psClpHOXlZU0JRY205cVpXTjBNUTh3RFFZRFZRUUxFd1ptWldSdGMy\nY3hRVEEvQmdOVkJBTVRPR0oxWjNwcGJHeGgKTW1abFpHMXpaeTFpZFdkNmFXeHNZVEptWldSdGMy\nY3dNUzV3YUhneUxtWmxaRzl5WVhCeWIycGxZM1F1YjNKbgpNVUV3UHdZRFZRUXBFemhpZFdkNmFX\neHNZVEptWldSdGMyY3RZblZuZW1sc2JHRXlabVZrYlhObk1ERXVjR2g0Ck1pNW1aV1J2Y21Gd2Nt\nOXFaV04wTG05eVp6RW1NQ1FHQ1NxR1NJYjNEUUVKQVJZWFlXUnRhVzVBWm1Wa2IzSmgKY0hKdmFt\nVmpkQzV2Y21jd2daOHdEUVlKS29aSWh2Y05BUUVCQlFBRGdZMEFNSUdKQW9HQkFMMmVrQnE2TlZK\nbQpONVFSdzhpM0diRDlRV213ZFV6Z1ZCVDRSaW5lU0tGbUlSditNNmM5aW1IbTVZcXpOMWl4eEJT\na21ibjZ1WWUrCkRFbEMzYUJ5MzREY2YzY2s0S3Nvams2YTk3SU5MQ0s1cWpKYmFuK3c0QU92ZDJn\nUHNUUCtmSHRLUUxDTUJEcEsKZVFLUk1tUUhUUjFjSWpiQmtSdDBWelRvZVBHNk5HL0xBZ01CQUFH\namdnRlhNSUlCVXpBSkJnTlZIUk1FQWpBQQpNQzBHQ1dDR1NBR0crRUlCRFFRZ0ZoNUZZWE41TFZK\nVFFTQkhaVzVsY21GMFpXUWdRMlZ5ZEdsbWFXTmhkR1V3CkhRWURWUjBPQkJZRUZIZlVVWlNJeGxl\nb3dud0JyMEE1Wm1jK2hZUTZNSUhWQmdOVkhTTUVnYzB3Z2NxQUZHdEEKV3ZrU0NJbFo1MW5sQmZV\nQ0hRcE9meFFBb1lHbXBJR2pNSUdnTVFzd0NRWURWUVFHRXdKVlV6RUxNQWtHQTFVRQpDQk1DVGtN\neEVEQU9CZ05WQkFjVEIxSmhiR1ZwWjJneEZ6QVZCZ05WQkFvVERrWmxaRzl5WVNCUWNtOXFaV04w\nCk1ROHdEUVlEVlFRTEV3Wm1aV1J0YzJjeER6QU5CZ05WQkFNVEJtWmxaRzF6WnpFUE1BMEdBMVVF\nS1JNR1ptVmsKYlhObk1TWXdKQVlKS29aSWh2Y05BUWtCRmhkaFpHMXBia0JtWldSdmNtRndjbTlx\nWldOMExtOXlaNElKQU9OUQpIa2RQRng1Rk1CTUdBMVVkSlFRTU1Bb0dDQ3NHQVFVRkJ3TUNNQXNH\nQTFVZER3UUVBd0lIZ0RBTkJna3Foa2lHCjl3MEJBUVVGQUFPQmdRQjAwYU52aHJMZ0p6ckRGK2cy\nOG5ZclZ4WXZMYzdDaE5hUU5wTFNUK2hGaWxqZ2lRblEKSnJTN2hCN3crV1hNbmp1MVNmWWRET09M\nQjU3V3ovR0RkM1lYU2ZZU0RjckphY1dRR2ZvRjZUT1ZoeDRJejlkdAp3RktXMG1wWDRYSXNacDN2\nR1JkY05KUVI3TWlCZkZTUkh0blR6Nkdoajd0eVRLNHRPMlRBSHpoUlBnPT0KLS0tLS1FTkQgQ0VS\nVElGSUNBVEUtLS0tLQo=\n",
      "i": 5309,
      "timestamp": 1559764461.0,
      "msg_id": "2019-77f8185e-c78a-4591-ac47-3225e61c8dc8",
      "crypto": "x509",
      "topic": "org.fedoraproject.prod.bugzilla.bug.update",
      "headers": {},
      "signature": "JuWS85uO8UHp+7vwFKRvXt6LgFbN82B2SUa6YLoqo+UxWVi2GcQGS2SrWh45+R6IFlqbP/OFp8rG\nPSHRbh/yQDdOq98fNjgr4X/NpHd1EE42iTmUS6nMeczVVhWZInlCYSRyTiyll6vkW0saQVMvw+Rq\nYsmWZW0DEVyaNJH86zw=\n",
      "source_version": "0.9.0",
      "msg": {
        "comment": None,
        "headers": {
          "content-length": "1336",
          "expires": "1559850861770",
          "esbMessageType": "bugzillaNotification",
          "timestamp": "1559764461770",
          "JMSXUserID": "msg-client-bugzilla",
          "destination": "/topic/VirtualTopic.eng.bugzilla.bug.create",
          "correlation-id": "8a7860d4-e710-4469-99a8-e1286e49f44d",
          "priority": "4",
          "subscription": "/queue/Consumer.fedora.DO-NOT-COPY.VirtualTopic.eng.bugzilla.>",
          "amq6100_destination": "queue://Consumer.fedora.DO-NOT-COPY.VirtualTopic.eng.bugzilla.>",
          "amq6100_originalDestination": "topic://VirtualTopic.eng.bugzilla.bug.create",
          "message-id": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.com-46058-1559753698477-3:47:-1:1:2155",
          "original-destination": "/topic/VirtualTopic.eng.bugzilla.bug.create",
          "esbSourceSystem": "bugzilla"
        },
        "bug": {
          "classification": "Fedora",
          "creator": None,
          "cc": [],
          "depends_on": None,
          "weburl": None,
          "creation_time": "2019-06-05T19:54:08",
          "docs_contact": None,
          "is_open": None,
          "platform": "x86_64",
          "keywords": [],
          "summary": "VTK inoperative on NVidia",
          "external_bugs": None,
          "id": 1717615,
          "qa_contact": {
            "login": "extras-qa@fedoraproject.org",
            "id": 171387,
            "real_name": "Fedora Extras Quality Assurance"
          },
          "severity": "high",
          "is_confirmed": None,
          "is_creator_accessible": None,
          "comments": None,
          "priority": "unspecified",
          "estimated_time": None,
          "version": {
            "id": 5713,
            "name": "30"
          },
          "fixed_in": None,
          "status": {
            "id": 1,
            "name": "NEW"
          },
          "product": {
            "id": 49,
            "name": "Fedora"
          },
          "blocks": None,
          "description": None,
          "see_also": None,
          "component": "vtk",
          "remaining_time": None,
          "target_release": None,
          "groups": None,
          "target_milestone": None,
          "is_cc_accessible": None,
          "versions": None,
          "url": "",
          "whiteboard": "",
          "last_change_time": "2019-06-05T19:54:08",
          "alias": [],
          "op_sys": None,
          "flags": [],
          "components": None,
          "assigned_to": "orion@nwra.com",
          "resolution": "",
          "actual_time": None
        },
        "event": {
          "who": "vaf0001@uah.edu",
          "target": "bug",
          "change_set": "588.1559764448.1403",
          "routing_key": "bug.create",
          "bug_id": 1717615,
          "user": {
            "login": "vaf0001@uah.edu",
            "id": 287333,
            "real_name": "Vladimir Florinski"
          },
          "time": "2019-06-05T19:54:08",
          "action": "create",
          "changes": []
        }
      }
    }


class Test031BugzillaUpdateEmpty(Base):
    """ Even `Red Hat's Bugzilla instance <https://bugzilla.redhat.com>`_ is
    hooked into fedmsg.

    Messages of *this* type are published by bugzilla2fedmsg 0.3.1
    (the currently-deployed version as of 2019-06-05) when Bugzilla
    emits a broken `bug.modify` message with no `changes`. This seems
    to happen sometimes when someone adds a comment to a bug on the
    *Fedora* or *Fedora EPEL* products. Red Hatters can see an issue
    report on this here:
    https://projects.engineering.redhat.com/browse/BUGZILLA-1315

    Ideally bugzilla2fedmsg should detect these broken upstream
    messages and simply not emit a fedmsg for them. But it doesn't yet
    do that, so we need to be aware of these and process them somehow.
    """

    expected_title = "bugzilla.bug.update"
    expected_subti = "bmason@redhat.com updated nothing? (likely bugzilla sent us a buggy " + \
        "message) on RHBZ#837790 'It's impossible to print more than one f...'"
    expected_link = "https://bugzilla.redhat.com/show_bug.cgi?id=837790"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bugzilla.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "643a2b348a82894fa989d1b2663fb1de?s=64&d=retro")
    expected_packages = set(['cups-pdf'])
    expected_usernames = set([])
    expected_objects = set(['Fedora/cups-pdf/837790'])

    msg = {
      "username": "fedmsg",
      "source_name": "datanommer",
      "certificate": "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUVkekNDQStDZ0F3SUJBZ0lDQWJvd0RRWUpL\nb1pJaHZjTkFRRUZCUUF3Z2FBeEN6QUpCZ05WQkFZVEFsVlQKTVFzd0NRWURWUVFJRXdKT1F6RVFN\nQTRHQTFVRUJ4TUhVbUZzWldsbmFERVhNQlVHQTFVRUNoTU9SbVZrYjNKaApJRkJ5YjJwbFkzUXhE\nekFOQmdOVkJBc1RCbVpsWkcxelp6RVBNQTBHQTFVRUF4TUdabVZrYlhObk1ROHdEUVlEClZRUXBF\nd1ptWldSdGMyY3hKakFrQmdrcWhraUc5dzBCQ1FFV0YyRmtiV2x1UUdabFpHOXlZWEJ5YjJwbFkz\nUXUKYjNKbk1CNFhEVEUwTURZeU1ESXdNREl6TVZvWERUSTBNRFl4TnpJd01ESXpNVm93Z2dFRU1R\nc3dDUVlEVlFRRwpFd0pWVXpFTE1Ba0dBMVVFQ0JNQ1RrTXhFREFPQmdOVkJBY1RCMUpoYkdWcFoy\nZ3hGekFWQmdOVkJBb1REa1psClpHOXlZU0JRY205cVpXTjBNUTh3RFFZRFZRUUxFd1ptWldSdGMy\nY3hRVEEvQmdOVkJBTVRPR0oxWjNwcGJHeGgKTW1abFpHMXpaeTFpZFdkNmFXeHNZVEptWldSdGMy\nY3dNUzV3YUhneUxtWmxaRzl5WVhCeWIycGxZM1F1YjNKbgpNVUV3UHdZRFZRUXBFemhpZFdkNmFX\neHNZVEptWldSdGMyY3RZblZuZW1sc2JHRXlabVZrYlhObk1ERXVjR2g0Ck1pNW1aV1J2Y21Gd2Nt\nOXFaV04wTG05eVp6RW1NQ1FHQ1NxR1NJYjNEUUVKQVJZWFlXUnRhVzVBWm1Wa2IzSmgKY0hKdmFt\nVmpkQzV2Y21jd2daOHdEUVlKS29aSWh2Y05BUUVCQlFBRGdZMEFNSUdKQW9HQkFMMmVrQnE2TlZK\nbQpONVFSdzhpM0diRDlRV213ZFV6Z1ZCVDRSaW5lU0tGbUlSditNNmM5aW1IbTVZcXpOMWl4eEJT\na21ibjZ1WWUrCkRFbEMzYUJ5MzREY2YzY2s0S3Nvams2YTk3SU5MQ0s1cWpKYmFuK3c0QU92ZDJn\nUHNUUCtmSHRLUUxDTUJEcEsKZVFLUk1tUUhUUjFjSWpiQmtSdDBWelRvZVBHNk5HL0xBZ01CQUFH\namdnRlhNSUlCVXpBSkJnTlZIUk1FQWpBQQpNQzBHQ1dDR1NBR0crRUlCRFFRZ0ZoNUZZWE41TFZK\nVFFTQkhaVzVsY21GMFpXUWdRMlZ5ZEdsbWFXTmhkR1V3CkhRWURWUjBPQkJZRUZIZlVVWlNJeGxl\nb3dud0JyMEE1Wm1jK2hZUTZNSUhWQmdOVkhTTUVnYzB3Z2NxQUZHdEEKV3ZrU0NJbFo1MW5sQmZV\nQ0hRcE9meFFBb1lHbXBJR2pNSUdnTVFzd0NRWURWUVFHRXdKVlV6RUxNQWtHQTFVRQpDQk1DVGtN\neEVEQU9CZ05WQkFjVEIxSmhiR1ZwWjJneEZ6QVZCZ05WQkFvVERrWmxaRzl5WVNCUWNtOXFaV04w\nCk1ROHdEUVlEVlFRTEV3Wm1aV1J0YzJjeER6QU5CZ05WQkFNVEJtWmxaRzF6WnpFUE1BMEdBMVVF\nS1JNR1ptVmsKYlhObk1TWXdKQVlKS29aSWh2Y05BUWtCRmhkaFpHMXBia0JtWldSdmNtRndjbTlx\nWldOMExtOXlaNElKQU9OUQpIa2RQRng1Rk1CTUdBMVVkSlFRTU1Bb0dDQ3NHQVFVRkJ3TUNNQXNH\nQTFVZER3UUVBd0lIZ0RBTkJna3Foa2lHCjl3MEJBUVVGQUFPQmdRQjAwYU52aHJMZ0p6ckRGK2cy\nOG5ZclZ4WXZMYzdDaE5hUU5wTFNUK2hGaWxqZ2lRblEKSnJTN2hCN3crV1hNbmp1MVNmWWRET09M\nQjU3V3ovR0RkM1lYU2ZZU0RjckphY1dRR2ZvRjZUT1ZoeDRJejlkdAp3RktXMG1wWDRYSXNacDN2\nR1JkY05KUVI3TWlCZkZTUkh0blR6Nkdoajd0eVRLNHRPMlRBSHpoUlBnPT0KLS0tLS1FTkQgQ0VS\nVElGSUNBVEUtLS0tLQo=\n",
      "i": 5389,
      "timestamp": 1559777808.0,
      "msg_id": "2019-49a30bc8-5825-42e0-8e43-9d9bdd15cd01",
      "crypto": "x509",
      "topic": "org.fedoraproject.prod.bugzilla.bug.update",
      "headers": {},
      "signature": "iU+9xeTCw19ZIr1/WQuWiXDyR4qI+WtLwSjqokZ09dJWygURNiX2Tk0BE4zKgXEyOg8gff6CWnGe\nHypa5UkUrdgws4SagjRiA+oTkEjSpqOqyhquVradD5vlOUR16dn6p3NSferIu7U7yRp7A4LFeznG\ngvEDIPff2v1jyDkFq8U=\n",
      "source_version": "0.9.0",
      "msg": {
        "comment": None,
        "headers": {
          "content-length": "1439",
          "expires": "1559864208975",
          "esbMessageType": "bugzillaNotification",
          "timestamp": "1559777808975",
          "JMSXUserID": "msg-client-bugzilla",
          "destination": "/topic/VirtualTopic.eng.bugzilla.bug.modify",
          "correlation-id": "8cae1209-3d1a-438f-bd81-99830fa88b82",
          "priority": "4",
          "subscription": "/queue/Consumer.fedora.DO-NOT-COPY.VirtualTopic.eng.bugzilla.>",
          "amq6100_destination": "queue://Consumer.fedora.DO-NOT-COPY.VirtualTopic.eng.bugzilla.>",
          "amq6100_originalDestination": "topic://VirtualTopic.eng.bugzilla.bug.modify",
          "message-id": "ID:messaging-devops-broker02.web.prod.ext.phx2.redhat.com-46058-1559753698477-3:47:-1:1:3549",
          "original-destination": "/topic/VirtualTopic.eng.bugzilla.bug.modify",
          "esbSourceSystem": "bugzilla"
        },
        "bug": {
          "classification": "Fedora",
          "creator": None,
          "cc": [],
          "depends_on": None,
          "weburl": None,
          "creation_time": "2012-07-05T09:22:40",
          "docs_contact": None,
          "is_open": None,
          "platform": "Unspecified",
          "keywords": [],
          "summary": "It's impossible to print more than one file in one lpr command to a cups-pdf printer",
          "external_bugs": None,
          "id": 837790,
          "qa_contact": {
            "login": "extras-qa@fedoraproject.org",
            "id": 171387,
            "real_name": "Fedora Extras Quality Assurance"
          },
          "severity": "unspecified",
          "is_confirmed": None,
          "is_creator_accessible": None,
          "comments": None,
          "priority": "unspecified",
          "estimated_time": None,
          "version": {
            "id": 5713,
            "name": "30"
          },
          "fixed_in": None,
          "status": {
            "id": 1,
            "name": "NEW"
          },
          "product": {
            "id": 49,
            "name": "Fedora"
          },
          "blocks": None,
          "description": None,
          "see_also": None,
          "component": "cups-pdf",
          "remaining_time": None,
          "target_release": None,
          "groups": None,
          "target_milestone": None,
          "is_cc_accessible": None,
          "versions": None,
          "url": "",
          "whiteboard": "",
          "last_change_time": "2019-04-28T17:05:00",
          "alias": [],
          "op_sys": None,
          "flags": [],
          "components": None,
          "assigned_to": "robert@marcanoonline.com",
          "resolution": "",
          "actual_time": None
        },
        "event": {
          "who": "bmason@redhat.com",
          "target": "bug",
          "change_set": "68879.1559777807.65753",
          "routing_key": "bug.modify",
          "bug_id": 837790,
          "user": {
            "login": "bmason@redhat.com",
            "id": 184677,
            "real_name": "Bryan Mason"
          },
          "time": "2019-06-05T23:36:47",
          "action": "modify",
          "changes": []
        }
      }
    }

add_doc(locals())

if __name__ == '__main__':
    unittest.main()
