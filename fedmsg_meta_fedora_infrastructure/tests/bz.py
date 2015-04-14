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


class TestBugzillaUpdate(Base):
    """ Even `Red Hat's Bugzilla instance <https://bugzilla.redhat.com>`_ is
    hooked into fedmsg.

    Messages of *this* type are published whenever someone **updates a bug**
    on the *Fedora* or *Fedora EPEL* products.
    """

    expected_title = "bugzilla.bug.update"
    expected_subti = "ralph updated 'status', 'cc', and 'assigned_to' on " + \
        "RHBZ#968947 'Review Request: gallery3-openid - OpenID...'"
    expected_link = "https://bugzilla.redhat.com/show_bug.cgi?id=968947"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bugzilla.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['ralph', 'puiterwijk'])
    expected_objects = set([
        'Fedora/Package Review/968947',
    ])

    msg = {
        "username": "threebean",
        "i": 1,
        "timestamp": 1395760459,
        "msg_id": "2014-0bc98222-a864-4aea-bc6b-e3b090d2cc3d",
        "topic": "org.fedoraproject.dev.bugzilla.bug.update",
        "msg": {
            "bug": {
                "attachments": [],
                "classification": "Fedora",
                "creator": "puiterwijk@gmail.com",
                "cc": [
                    "package-review@lists.fedoraproject.org",
                    "puiterwijk@gmail.com",
                    "rbean@redhat.com"
                ],
                "depends_on": [],
                "weburl": "https://bugzilla.redhat.com/show_bug.cgi?id=968947",
                "creation_time": 1369924680.0,
                "actual_time": 0.0,
                "docs_contact": "",
                "is_open": True,
                "keywords": [],
                "target_release": [
                    "---"
                ],
                "external_bugs": [],
                "id": 968947,
                "description": "\nSpec URL: http://puiterwijk.fedorapeople..",
                "severity": "unspecified",
                "is_confirmed": True,
                "is_creator_accessible": True,
                "comments": [
                    {
                        "count": 0,
                        "author": "puiterwijk@gmail.com",
                        "text": "\nSpec URL: http://puiterwijk.fedorapeople..",
                        "creator": "puiterwijk@gmail.com",
                        "creation_time": 1369924708.0,
                        "bug_id": 968947,
                        "creator_id": 330125,
                        "time": 1369924708.0,
                        "id": 5962818,
                        "is_private": False
                    },
                    {
                        "count": 1,
                        "author": "puiterwijk@gmail.com",
                        "text": "This package built on koji:    http://koj...",
                        "creator": "puiterwijk@gmail.com",
                        "creation_time": 1369924717.0,
                        "bug_id": 968947,
                        "creator_id": 330125,
                        "time": 1369924717.0,
                        "id": 5962819,
                        "is_private": False
                    },
                    {
                        "count": 2,
                        "author": "rbean@redhat.com",
                        "text": "Some preliminary comments:\n\n* The ...",
                        "creator": "rbean@redhat.com",
                        "creation_time": 1369950294.0,
                        "bug_id": 968947,
                        "creator_id": 269108,
                        "time": 1369950294.0,
                        "id": 5964283,
                        "is_private": False
                    }
                ],
                "priority": "unspecified",
                "platform": "Unspecified",
                "version": "rawhide",
                "fixed_in": "",
                "status": "ASSIGNED",
                "product": "Fedora",
                "blocks": [],
                "qa_contact": "extras-qa@fedoraproject.org",
                "see_also": [],
                "component": "Package Review",
                "remaining_time": 0.0,
                "groups": [],
                "estimated_time": 0.0,
                "target_milestone": "---",
                "is_cc_accessible": True,
                "versions": [
                    "rawhide"
                ],
                "url": "",
                "whiteboard": "",
                "summary": "Review Request: gallery3-openid - OpenID "
                "authentication for Gallery3",
                "alias": [],
                "op_sys": "Unspecified",
                "flags": [
                    {
                        "requestee": "puiterwijk@gmail.com",
                        "status": "?",
                        "name": "needinfo",
                        "modification_date": 1392337756.0,
                        "type_id": 16,
                        "is_active": 1,
                        "creation_date": 1392337756.0,
                        "id": 1703755,
                        "setter": "rbean@redhat.com"
                    }
                ],
                "components": [
                    "Package Review"
                ],
                "assigned_to": "rbean@redhat.com",
                "resolution": "",
                "last_change_time": 1392337756.0
            },
            "event": {
                "changes": [
                    {
                        "removed": "NEW",
                        "field_name": "status",
                        "added": "ASSIGNED"
                    },
                    {
                        "removed": "",
                        "field_name": "cc",
                        "added": "rbean@redhat.com"
                    },
                    {
                        "removed": "nobody@fedoraproject.org",
                        "field_name": "assigned_to",
                        "added": "rbean@redhat.com"
                    }
                ],
                "who": "rbean@redhat.com",
                "when": 1369949333.0
            }
        }
    }


class TestBugzillaNew(Base):
    """ Even `Red Hat's Bugzilla instance <https://bugzilla.redhat.com>`_ is
    hooked into fedmsg.

    Messages of *this* type are published whenever someone **files a new bug**
    on the *Fedora* or *Fedora EPEL* products.

    Note that the ``event`` field is left empty (``{}``) for new bug events.
    """

    expected_title = "bugzilla.bug.new"
    expected_subti = "puiterwijk filed a new bug " + \
        "RHBZ#968947 'Review Request: gallery3-openid - OpenID...'"
    expected_link = "https://bugzilla.redhat.com/show_bug.cgi?id=968947"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bugzilla.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "983782d075ab4e1fb02a7e7c7ca4d7096f6769bc9fe51b50e80eb012ddebc9ce"
        "?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['puiterwijk'])
    expected_objects = set([
        'Fedora/Package Review/968947',
    ])

    msg = {
        "username": "threebean",
        "i": 1,
        "timestamp": 1395760459,
        "msg_id": "2014-0bc98222-a864-4aea-bc6b-e3b090d2cc3d",
        "topic": "org.fedoraproject.dev.bugzilla.bug.new",
        "msg": {
            "bug": {
                "attachments": [],
                "classification": "Fedora",
                "creator": "puiterwijk@gmail.com",
                "cc": [
                    "package-review@lists.fedoraproject.org",
                    "puiterwijk@gmail.com",
                ],
                "depends_on": [],
                "weburl": "https://bugzilla.redhat.com/show_bug.cgi?id=968947",
                "creation_time": 1369924680.0,
                "actual_time": 0.0,
                "docs_contact": "",
                "is_open": True,
                "keywords": [],
                "target_release": [
                    "---"
                ],
                "external_bugs": [],
                "id": 968947,
                "description": "\nSpec URL: http://puiterwijk.fedorapeople..",
                "severity": "unspecified",
                "is_confirmed": True,
                "is_creator_accessible": True,
                "comments": [
                    {
                        "count": 0,
                        "author": "puiterwijk@gmail.com",
                        "text": "\nSpec URL: http://puiterwijk.fedorapeople..",
                        "creator": "puiterwijk@gmail.com",
                        "creation_time": 1369924708.0,
                        "bug_id": 968947,
                        "creator_id": 330125,
                        "time": 1369924708.0,
                        "id": 5962818,
                        "is_private": False
                    },
                ],
                "priority": "unspecified",
                "platform": "Unspecified",
                "version": "rawhide",
                "fixed_in": "",
                "status": "ASSIGNED",
                "product": "Fedora",
                "blocks": [],
                "qa_contact": "extras-qa@fedoraproject.org",
                "see_also": [],
                "component": "Package Review",
                "remaining_time": 0.0,
                "groups": [],
                "estimated_time": 0.0,
                "target_milestone": "---",
                "is_cc_accessible": True,
                "versions": [
                    "rawhide"
                ],
                "url": "",
                "whiteboard": "",
                "summary": "Review Request: gallery3-openid - OpenID "
                "authentication for Gallery3",
                "alias": [],
                "op_sys": "Unspecified",
                "flags": [
                    {
                        "requestee": "puiterwijk@gmail.com",
                        "status": "?",
                        "name": "needinfo",
                        "modification_date": 1392337756.0,
                        "type_id": 16,
                        "is_active": 1,
                        "creation_date": 1392337756.0,
                        "id": 1703755,
                        "setter": "rbean@redhat.com"
                    }
                ],
                "components": [
                    "Package Review"
                ],
                "assigned_to": "",
                "resolution": "",
                "last_change_time": 1392337756.0
            },
            "event": {},
        }
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
