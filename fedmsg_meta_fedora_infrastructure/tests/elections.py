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
#
""" Tests for elections/voting messages """

import unittest
import datetime

from fedmsg.tests.test_meta import Base

from common import add_doc


class TestElectionsNew(Base):
    """ These messages are published when someone creates a new elections
    in `elections <https://apps.fedoraproject.org/voting/>`_.
    """

    expected_title = "fedora_elections.election.new"
    expected_subti = 'pingou created election "test"'
    expected_link = "https://apps.fedoraproject.org/voting/about/test"
    expected_icon = (None)
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c"
        "?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['test/test/election/new'])
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
    `elections <https://apps.fedoraproject.org/voting/>`_.
    """

    expected_title = "fedora_elections.election.edit"
    expected_subti = 'pingou edited election "test"'
    expected_link = "https://apps.fedoraproject.org/voting/about/test"
    expected_icon = (None)
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c"
        "?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['test/test/election/edit'])
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
    elections in `elections <https://apps.fedoraproject.org/voting/>`_.
    """

    expected_title = "fedora_elections.candidate.new"
    expected_subti = 'pingou added candidate "Toshio" to election "test"'
    expected_link = "https://apps.fedoraproject.org/voting/about/test"
    expected_icon = (None)
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c"
        "?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['test/test/candidate/new'])
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
    elections in `elections <https://apps.fedoraproject.org/voting/>`_.
    """

    expected_title = "fedora_elections.candidate.edit"
    expected_subti = 'pingou edited candidate "Toshio" of election "test"'
    expected_link = "https://apps.fedoraproject.org/voting/about/test"
    expected_icon = (None)
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c"
        "?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['test/test/candidate/edit'])
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
    elections in `elections <https://apps.fedoraproject.org/voting/>`_.
    """

    expected_title = "fedora_elections.candidate.delete"
    expected_subti = 'pingou deleted candidate "Toshio" of election "test"'
    expected_link = "https://apps.fedoraproject.org/voting/about/test"
    expected_icon = (None)
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c"
        "?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['test/test/candidate/delete'])
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


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
