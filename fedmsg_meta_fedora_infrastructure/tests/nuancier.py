# This file is part of fedmsg.
# Copyright (C) 2012 Red Hat, Inc.
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
""" Tests for nuancier messages """

import unittest

from fedmsg.tests.test_meta import Base

from .common import add_doc


class TestNuancierElectionUpdated(Base):
    """ These messages are published when **an admin updates the details** of
    an existing election on the "Nuancier" wallpaper voting app.
    """

    expected_title = "nuancier.election.update"
    expected_subti = 'ralph changed the following details on the ' + \
        '"Fedora 21" election: election year, election name'
    expected_link = "https://apps.fedoraproject.org/nuancier/election/1"
    expected_icon = "https://apps.fedoraproject.org/img/icons/nuancier.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c"
        "?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['2014/Fedora 21/election/update'])
    msg = {
        "username": "threebean",
        "i": 2,
        "timestamp": 1392907947,
        "msg_id": "2014-a97d68bd-bc9e-49e0-b028-f10297f36767",
        "topic": "org.fedoraproject.dev.nuancier.election.update",
        "msg": {
            "updated": [
                "election year",
                "election name"
            ],
            "election": {
                "name": "Fedora 21",
                "submission_date_start": 1392958800.0,
                "date_end": 1393045200.0,
                "date_start": 1392958800.0,
                "year": "2014",
                "id": 1
            },
            "agent": "ralph"
        }
    }


class TestNuancierElectionCreate(Base):
    """ These messages are published when **an admin creates** a new election
    on the "Nuancier" wallpaper voting app.
    """

    expected_title = "nuancier.election.new"
    expected_subti = 'ralph created a new election "Fedora 22"'
    expected_link = "https://apps.fedoraproject.org/nuancier/election/4"
    expected_icon = "https://apps.fedoraproject.org/img/icons/nuancier.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c"
        "?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['2015/Fedora 22/election/new'])
    msg = {
        "username": "threebean",
        "i": 1,
        "timestamp": 1392908460,
        "msg_id": "2014-88577310-f466-4c88-8deb-dc98c8abc09e",
        "topic": "org.fedoraproject.dev.nuancier.election.new",
        "msg": {
            "election": {
                "name": "Fedora 22",
                "submission_date_start": 1392786000.0,
                "date_end": 1393045200.0,
                "date_start": 1392786000.0,
                "year": "2015",
                "id": 4
            },
            "agent": "ralph"
        }
    }


class TestNuancierCandidateNew(Base):
    """ These messages are published when **a contributor submits a new
    candidate** for an existing election on the "Nuancier" wallpaper voting
    app.
    """

    expected_title = "nuancier.candidate.new"
    expected_subti = 'ralph uploaded a new candidate for the ' + \
        '"Fedora 22" wallpaper election'
    expected_link = "http://www.cyclelicio.us/wp-content/" + \
        "uploads/2013/07/skvidal.jpg"
    expected_icon = "https://apps.fedoraproject.org/img/icons/nuancier.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c"
        "?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['2015/Fedora 22/Handsome/candidate/new'])
    msg = {
        "username": "threebean",
        "i": 2,
        "timestamp": 1392908853,
        "msg_id": "2014-0838ce6a-9f99-41d9-84a4-e076665d3b2b",
        "topic": "org.fedoraproject.dev.nuancier.candidate.new",
        "msg": {
            "agent": "ralph",
            "candidate": {
                "submitter": "ralph",
                "author": "ralph",
                "name": "Handsome",
                "license": "CC-BY-SA",
                "original_url": "http://www.cyclelicio.us/wp-content/"
                "uploads/2013/07/skvidal.jpg"
            },
            "election": {
                "name": "Fedora 22",
                "submission_date_start": 1392786000.0,
                "date_end": 1393045200.0,
                "date_start": 1392958800.0,
                "year": 2015,
                "id": 4
            }
        }
    }


class TestNuancierCandidateApprove(Base):
    """ These messages are published when **an admin approves** a candidate
    submission to the "Nuancier" wallpaper voting app.
    """

    expected_title = "nuancier.candidate.approved"
    expected_subti = 'gnokii approved ralph\'s "Handsome" submission ' + \
        'to the "Fedora 22" wallpaper election'
    expected_link = "http://www.cyclelicio.us/wp-content/" + \
        "uploads/2013/07/skvidal.jpg"
    expected_icon = "https://apps.fedoraproject.org/img/icons/nuancier.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "f0f0eef56d80913ec82275ed76dafe440ef8b4bba0228d97e7fb2ecb275d9591"
        "?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['ralph', 'gnokii'])
    expected_objects = set(['2015/Fedora 22/Handsome/candidate/approved'])
    msg = {
        "username": "threebean",
        "i": 1,
        "timestamp": 1392916813,
        "msg_id": "2014-32dce0de-5d80-4f9e-a445-d63b6f9e320f",
        "topic": "org.fedoraproject.dev.nuancier.candidate.approved",
        "msg": {
            "agent": "gnokii",
            "candidate": {
                "submitter": "ralph",
                "author": "ralph",
                "name": "Handsome",
                "license": "CC-BY-SA",
                "original_url": "http://www.cyclelicio.us/wp-content/"
                "uploads/2013/07/skvidal.jpg"
            },
            "election": {
                "name": "Fedora 22",
                "submission_date_start": 1392786000.0,
                "date_end": 1393045200.0,
                "date_start": 1392958800.0,
                "year": 2015,
                "id": 4
            }
        }
    }


class TestNuancierCandidateDeny(Base):
    """ These messages are published when **an admin denies** a candidate
    submission to the "Nuancier" wallpaper voting app.
    """

    expected_title = "nuancier.candidate.denied"
    expected_subti = 'gnokii denied ralph\'s "Handsome" submission ' + \
        'to the "Fedora 22" wallpaper election'
    expected_link = "http://www.cyclelicio.us/wp-content/" + \
        "uploads/2013/07/skvidal.jpg"
    expected_icon = "https://apps.fedoraproject.org/img/icons/nuancier.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "f0f0eef56d80913ec82275ed76dafe440ef8b4bba0228d97e7fb2ecb275d9591"
        "?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['ralph', 'gnokii'])
    expected_objects = set(['2015/Fedora 22/Handsome/candidate/denied'])
    msg = {
        "username": "threebean",
        "i": 1,
        "timestamp": 1392916813,
        "msg_id": "2014-32dce0de-5d80-4f9e-a445-d63b6f9e320f",
        "topic": "org.fedoraproject.dev.nuancier.candidate.denied",
        "msg": {
            "agent": "gnokii",
            "candidate": {
                "submitter": "ralph",
                "author": "ralph",
                "name": "Handsome",
                "license": "CC-BY-SA",
                "original_url": "http://www.cyclelicio.us/wp-content/"
                "uploads/2013/07/skvidal.jpg"
            },
            "election": {
                "name": "Fedora 22",
                "submission_date_start": 1392786000.0,
                "date_end": 1393045200.0,
                "date_start": 1392958800.0,
                "year": 2015,
                "id": 4
            }
        }
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
