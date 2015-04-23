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
""" Tests for summershum messages """

import unittest

from fedmsg_meta_fedora_infrastructure.tests.base import Base

from .common import add_doc


class TestSummershumComplete(Base):
    """ Fedora Infrastructure runs a background service called `summershum
    <https://github.com/fedora-infra/summershum>`_, the role of which is to
    compute and store hashes of every file of every tarball of every package in
    Fedora.  This data is then to later be used in tests and analysis.

    This message type is published by the summershum backend when it has
    completed processing of a new tarball.
    """

    expected_title = "summershum.ingest.complete"
    expected_subti = "summershum ingested " + \
        "gnome-online-accounts-3.11.90.tar.xz" + \
        " for gnome-online-accounts"
    expected_icon = (
        "https://raw.githubusercontent.com/"
        "fedora-infra/summershum/develop/summershum.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "2a5dd5a2f8e889c4384449a208402945a9cddaf5ce9bba0c57851ca54d46c769"
        "?s=64&d=retro")
    expected_link = 'http://pkgs.fedoraproject.org/lookaside/pkgs/' + \
        'gnome-online-accounts/gnome-online-accounts-3.11.90.tar.xz/' + \
        '7d32a7ed3653fe4c3de1fd3e9d1e1367/' + \
        'gnome-online-accounts-3.11.90.tar.xz'
    expected_packages = set(['gnome-online-accounts'])
    expected_usernames = set(['rhughes'])
    expected_objects = set([
        'digests/gnome-online-accounts/'
        'gnome-online-accounts-3.11.90.tar.xz/'
        '7d32a7ed3653fe4c3de1fd3e9d1e1367',
    ])

    msg = {
        "username": "threebean",
        "i": 14,
        "timestamp": 1392749080,
        "msg_id": "2014-c5565d9f-edbe-4ec3-9d3a-d2005b32a817",
        "topic": "org.fedoraproject.dev.summershum.ingest.complete",
        "msg": {
            "original": {
                "md5sum": "7d32a7ed3653fe4c3de1fd3e9d1e1367",
                "name": "gnome-online-accounts",
                "agent": "rhughes",
                "filename": "gnome-online-accounts-3.11.90.tar.xz"
            }
        }
    }


class TestSummershumStart(Base):
    """ Fedora Infrastructure runs a background service called `summershum
    <https://github.com/fedora-infra/summershum>`_, the role of which is to
    compute and store hashes of every file of every tarball of every package in
    Fedora.  This data is then to later be used in tests and analysis.

    This message type is published by the summershum backend when **begins
    processing** a new tarball.
    """

    expected_title = "summershum.ingest.start"
    expected_subti = "summershum started working on " + \
        "glibc-2.19-58-ga4fb786.tar.gz for glibc"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "6d069809dd6f854ea67299617954ffe913778b72e08a73ba85ec1c5859a3038f"
        "?s=64&d=retro")
    expected_link = 'http://pkgs.fedoraproject.org/lookaside/pkgs/' + \
        'glibc/glibc-2.19-58-ga4fb786.tar.gz/' + \
        '5f636f8001d1397fa6e233a1009df6c1/' + \
        'glibc-2.19-58-ga4fb786.tar.gz'
    expected_packages = set(['glibc'])
    expected_usernames = set(['siddhesh'])
    expected_objects = set([
        'digests/glibc/'
        'glibc-2.19-58-ga4fb786.tar.gz/'
        '5f636f8001d1397fa6e233a1009df6c1'
    ])
    msg = {
        "username": "threebean",
        "i": 15,
        "timestamp": 1392749080,
        "msg_id": "2014-53a77b4a-637e-4b98-a84e-90febb65ab80",
        "topic": "org.fedoraproject.dev.summershum.ingest.start",
        "msg": {
            "original": {
                "md5sum": "5f636f8001d1397fa6e233a1009df6c1",
                "name": "glibc",
                "agent": "siddhesh",
                "filename": "glibc-2.19-58-ga4fb786.tar.gz"
            }
        }
    }


class TestSummershumFail(Base):
    """ Fedora Infrastructure runs a background service called `summershum
    <https://github.com/fedora-infra/summershum>`_, the role of which is to
    compute and store hashes of every file of every tarball of every package in
    Fedora.  This data is then to later be used in tests and analysis.

    This message type is published by the summershum backend when it
    **encounters some error** and cannot process a tarball.
    """

    expected_title = "summershum.ingest.fail"
    expected_subti = "yikes!  summershum failed to process " + \
        "glibc-2.19-58-ga4fb786.tar.gz for glibc"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "6d069809dd6f854ea67299617954ffe913778b72e08a73ba85ec1c5859a3038f"
        "?s=64&d=retro")
    expected_link = 'http://pkgs.fedoraproject.org/lookaside/pkgs/' + \
        'glibc/glibc-2.19-58-ga4fb786.tar.gz/' + \
        '5f636f8001d1397fa6e233a1009df6c1/' + \
        'glibc-2.19-58-ga4fb786.tar.gz'
    expected_packages = set(['glibc'])
    expected_usernames = set(['siddhesh'])
    expected_objects = set([
        'digests/glibc/'
        'glibc-2.19-58-ga4fb786.tar.gz/'
        '5f636f8001d1397fa6e233a1009df6c1'
    ])
    msg = {
        "username": "threebean",
        "i": 15,
        "timestamp": 1392749080,
        "msg_id": "2014-53a77b4a-637e-4b98-a84e-90febb65ab80",
        "topic": "org.fedoraproject.dev.summershum.ingest.fail",
        "msg": {
            "original": {
                "md5sum": "5f636f8001d1397fa6e233a1009df6c1",
                "name": "glibc",
                "agent": "siddhesh",
                "filename": "glibc-2.19-58-ga4fb786.tar.gz"
            }
        }
    }


add_doc(locals())


if __name__ == '__main__':
    unittest.main()
