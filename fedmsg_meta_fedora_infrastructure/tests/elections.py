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
# Authors:  Pierre-Yves Chibon <pingou@pingoured.fr>
#           Ralph Bean <rbean@redhat.com>
#
""" Tests for elections/voting messages """

import unittest

from fedmsg.tests.test_meta import Base

from .common import add_doc


class TestLegacyElectionsNew(Base):
    """ Old style... """

    expected_title = "fedora_elections.election.new"
    expected_subti = 'pingou created election "test"'
    expected_link = "https://admin.fedoraproject.org/voting/about/test"
    expected_icon = (None)
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c"
        "?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['test/election/new'])
    msg = {
        "username": "pingou",
        "i": 1,
        "timestamp": 1379638157.759283,
        "msg_id": "2013-96f9ca0e-c7c6-43f0-9de7-7a268c7f1cef",
        "topic": "org.fedoraproject.dev.fedora_elections.election.new",
        "msg": {
            "election": {
                "description": "test desc",
                "end_date": 1397080800.0,
                "url": "http: //giuakle.org",
                "embargoed": 1,
                "alias": "test",
                "shortdesc": "test",
                "voting_type": "range",
                "start_date": 1396994400.0
            },
            "agent": "pingou"
        }
    }


class TestElectionsEdit(Base):
    """ These messages are published when someone edit an elections in
    `elections <https://admin.fedoraproject.org/voting/>`_.
    """

    expected_title = "fedora_elections.election.edit"
    expected_subti = 'pingou edited election "test"'
    expected_link = "https://admin.fedoraproject.org/voting/about/test"
    expected_icon = (None)
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c"
        "?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['test/election/edit'])
    msg = {
        "username": "pingou",
        "i": 1,
        "timestamp": 1379638157.759283,
        "msg_id": "2013-96f9ca0e-c7c6-43f0-9de7-7a268c7f1cef",
        "topic": "org.fedoraproject.dev.fedora_elections.election.edit",
        "msg": {
            "election": {
                "description": "test desc",
                "end_date": 1397080800.0,
                "url": "http: //giuakle.org",
                "embargoed": 1,
                "alias": "test",
                "shortdesc": "test",
                "voting_type": "range",
                "start_date": 1396994400.0
            },
            "agent": "pingou"
        }
    }


class TestElectionsCandidateNew(Base):
    """ These messages are published when someone added a candidate to an
    elections in `elections <https://admin.fedoraproject.org/voting/>`_.
    """

    expected_title = "fedora_elections.candidate.new"
    expected_subti = 'pingou added candidate "Toshio" to election "test"'
    expected_link = "https://admin.fedoraproject.org/voting/about/test"
    expected_icon = (None)
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c"
        "?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['test/candidate/new'])
    msg = {
        "username": "pingou",
        "i": 1,
        "timestamp": 1379638157.759283,
        "msg_id": "2013-96f9ca0e-c7c6-43f0-9de7-7a268c7f1cef",
        "topic": "org.fedoraproject.dev.fedora_elections.candidate.new",
        "msg": {
            "election": {
                "description": "test desc",
                "end_date": 1397080800.0,
                "url": "http: //giuakle.org",
                "embargoed": 1,
                "alias": "test",
                "shortdesc": "test",
                "voting_type": "range",
                "start_date": 1396994400.0
            },
            'candidate': {
                'url': '',
                'name': 'Toshio'
            },
            "agent": "pingou"
        }
    }


class TestElectionsCandidateEdit(Base):
    """ These messages are published when someone edited a candidate of an
    elections in `elections <https://admin.fedoraproject.org/voting/>`_.
    """

    expected_title = "fedora_elections.candidate.edit"
    expected_subti = 'pingou edited candidate "Toshio" of election "test"'
    expected_link = "https://admin.fedoraproject.org/voting/about/test"
    expected_icon = (None)
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c"
        "?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['test/candidate/edit'])
    msg = {
        "username": "pingou",
        "i": 1,
        "timestamp": 1379638157.759283,
        "msg_id": "2013-96f9ca0e-c7c6-43f0-9de7-7a268c7f1cef",
        "topic": "org.fedoraproject.dev.fedora_elections.candidate.edit",
        "msg": {
            "election": {
                "description": "test desc",
                "end_date": 1397080800.0,
                "url": "http: //giuakle.org",
                "embargoed": 1,
                "alias": "test",
                "shortdesc": "test",
                "voting_type": "range",
                "start_date": 1396994400.0
            },
            'candidate': {
                'url': '',
                'name': 'Toshio'
            },
            "agent": "pingou"
        }
    }


class TestElectionsCandidateDelete(Base):
    """ These messages are published when someone add a candidate to an
    elections in `elections <https://admin.fedoraproject.org/voting/>`_.
    """

    expected_title = "fedora_elections.candidate.delete"
    expected_subti = 'pingou deleted candidate "Toshio" of election "test"'
    expected_link = "https://admin.fedoraproject.org/voting/about/test"
    expected_icon = (None)
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c"
        "?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['test/candidate/delete'])
    msg = {
        "username": "pingou",
        "i": 1,
        "timestamp": 1379638157.759283,
        "msg_id": "2013-96f9ca0e-c7c6-43f0-9de7-7a268c7f1cef",
        "topic": "org.fedoraproject.dev.fedora_elections.candidate.delete",
        "msg": {
            "election": {
                "description": "test desc",
                "end_date": 1397080800.0,
                "url": "http: //giuakle.org",
                "embargoed": 1,
                "alias": "test",
                "shortdesc": "test",
                "voting_type": "range",
                "start_date": 1396994400.0
            },
            'candidate': {
                'url': '',
                'name': 'Toshio'
            },
            "agent": "pingou"
        }
    }


class TestElectionsNew(Base):
    """ These messages are published when someone creates a new elections
    in `elections <https://admin.fedoraproject.org/voting/>`_.
    """

    expected_title = "fedora_elections.election.new"
    expected_subti = 'jreznik created election "council-nov14"'
    expected_link = "https://admin.fedoraproject.org/voting/about/council-nov14"
    expected_icon = (None)
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "6a345b20c10f890075dab7cc5ac70fdc93167bfd40a4f9299bc77f5a0238a5cc"
        "?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['jreznik'])
    expected_objects = set(['council-nov14/election/new'])
    msg = {
        "i": 2,
        "msg": {
            "admin_groups": [],
            "alias": "council-nov14",
            "candidates": [],
            "candidates_are_fasusers": 1,
            "description": "The Fedora Council is our top-level community ...",
            "embargoed": 1,
            "end_date": 1417046399.0,
            "fas_user": "jreznik",
            "id": 65,
            "legal_voters": [{
                "election": 65,
                "election_id": 65,
                "group_name": "anycla",
                "id": 67
            }],
            "max_votes": None,
            "seats_elected": 2,
            "shortdesc": "Council - November 2014",
            "start_date": 1416268800.0,
            "url": "http://fedoraproject.org/wiki/Council/Nominations",
            "votes": [],
            "voting_type": "range"
        },
        "msg_id": "2014-6a4e287c-a65f-488f-8ba7-5b454a50642c",
        "source_name": "datanommer",
        "source_version": "0.6.4",
        "timestamp": 1416208425.0,
        "topic": "org.fedoraproject.prod.fedora_elections.election.new",
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
