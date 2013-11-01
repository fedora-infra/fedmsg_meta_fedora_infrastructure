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
""" Tests for badges messages """

import unittest

from fedmsg.tests.test_meta import Base

from common import add_doc


class TestNuancierElectionOpen(Base):
    """ These messages are published when a new election is opened for voting
    on "Nuancier", the wallpaper voting app.
    """

    expected_title = "nuancier.open.toggle.on"
    expected_subti = 'ralph opened the "awesome" election for voting'
    expected_link = "https://apps.fedoraproject.org/nuancier/election/1"
    expected_secondary_icon = ("http://www.gravatar.com/avatar/"
                               "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F"
                               "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png")
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['2013/awesome/open/on'])
    msg = {
        "username": "threebean",
        "i": 1,
        "timestamp": 1380303298.212,
        "msg_id": "2013-86c25e1b-1ea7-4202-8bf0-7d6c76131e37",
        "topic": "org.fedoraproject.dev.nuancier.open.toggle.on",
        "msg": {
            "state": True,
            "election": {
                "id": 1,
                "name": "awesome",
                "year": 2013,
            },
            "agent": "ralph"
        }
    }


class TestNuancierElectionClose(Base):
    """ These messages are published when an election is closed for voting on
    "Nuancier", the wallpaper voting app.
    """

    expected_title = "nuancier.open.toggle.off"
    expected_subti = 'ralph closed the "awesome" election for voting'
    expected_link = "https://apps.fedoraproject.org/nuancier/election/1"
    expected_secondary_icon = ("http://www.gravatar.com/avatar/"
                               "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F"
                               "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png")
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['2013/awesome/open/off'])
    msg = {
        "username": "threebean",
        "i": 4,
        "timestamp": 1380303306.041,
        "msg_id": "2013-3c985048-b82f-4836-b581-363bc9466e6e",
        "topic": "org.fedoraproject.dev.nuancier.open.toggle.off",
        "msg": {
            "state": False,
            "election": {
                "id": 1,
                "name": "awesome",
                "year": 2013
            },
            "agent": "ralph"
        }
    }


class TestNuancierResultsPublish(Base):
    """ These messages are published when the results of an election have been
    published on "Nuancier", the wallpaper voting app.
    """

    expected_title = "nuancier.publish.toggle.on"
    expected_subti = 'ralph published the results of the "awesome" election'
    expected_link = "https://apps.fedoraproject.org/nuancier/results/1"
    expected_secondary_icon = ("http://www.gravatar.com/avatar/"
                               "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F"
                               "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png")
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['2013/awesome/publish/on'])
    msg = {
        "username": "threebean",
        "i": 2,
        "timestamp": 1380303299.5,
        "msg_id": "2013-eb5b7306-2dfb-4040-a26e-6aa12b1fd3a2",
        "topic": "org.fedoraproject.dev.nuancier.publish.toggle.on",
        "msg": {
            "state": True,
            "election": {
                "id": 1,
                "name": "awesome",
                "year": 2013
            },
            "agent": "ralph"
        }
    }


class TestNuancierResultsRescind(Base):
    """ These messages are published when the results of an election have been
    rescinded on "Nuancier", the wallpaper voting app.
    """

    expected_title = "nuancier.publish.toggle.off"
    expected_subti = 'ralph rescinded the results of the "awesome" election'
    expected_link = "https://apps.fedoraproject.org/nuancier/results/1"
    expected_secondary_icon = ("http://www.gravatar.com/avatar/"
                               "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F"
                               "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png")
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['2013/awesome/publish/off'])
    msg = {
        "username": "threebean",
        "i": 3,
        "timestamp": 1380303304.667,
        "msg_id": "2013-9929bc11-d161-45d8-b9fe-45cef5d6acfe",
        "topic": "org.fedoraproject.dev.nuancier.publish.toggle.off",
        "msg": {
            "state": False,
            "election": {
                "id": 1,
                "name": "awesome",
                "year": 2013
            },
            "agent": "ralph"
        }
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
