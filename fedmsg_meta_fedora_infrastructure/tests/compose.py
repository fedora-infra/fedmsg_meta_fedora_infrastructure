# This file is part of fedmsg.
# Copyright (C) 2013 Red Hat, Inc.
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
""" Tests for fedmsg.meta """

import unittest

from fedmsg.tests.test_meta import Base


class TestComposeBranchedComplete(Base):
    expected_title = "compose.branched.complete (unsigned)"
    expected_subti = "branched compose completed"
    expected_link = \
        "https://alt.fedoraproject.org/pub/fedora/linux/development"
    expected_objects = set(['branched'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.complete",
    }


class TestComposeBranchedStart(Base):
    expected_title = "compose.branched.start (unsigned)"
    expected_subti = "branched compose started"
    expected_objects = set(['branched'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.start",
    }


class TestComposeBranchedMashStart(Base):
    expected_title = "compose.branched.mash.start (unsigned)"
    expected_subti = "branched compose started mashing"
    expected_objects = set(['branched'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.mash.start",
    }


class TestComposeBranchedMashComplete(Base):
    expected_title = "compose.branched.mash.complete (unsigned)"
    expected_subti = "branched compose finished mashing"
    expected_objects = set(['branched'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.mash.complete",
    }


class TestComposeBranchedPungifyStart(Base):
    expected_title = "compose.branched.pungify.start (unsigned)"
    expected_subti = "started building boot.iso for branched"
    expected_objects = set(['branched'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.pungify.start",
    }


class TestComposeBranchedPungifyComplete(Base):
    expected_title = "compose.branched.pungify.complete (unsigned)"
    expected_subti = "finished building boot.iso for branched"
    expected_objects = set(['branched'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.pungify.complete",
    }


class TestComposeBranchedRsyncStart(Base):
    expected_title = "compose.branched.rsync.start (unsigned)"
    expected_subti = "started rsyncing branched compose for public consumption"
    expected_objects = set(['branched'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.rsync.start",
    }


class TestComposeBranchedRsyncComplete(Base):
    expected_title = "compose.branched.rsync.complete (unsigned)"
    expected_subti = \
        "finished rsync of branched compose for public consumption"
    expected_link = \
        "https://alt.fedoraproject.org/pub/fedora/linux/development"
    expected_objects = set(['branched'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.rsync.complete",
    }


class TestComposeRawhideComplete(Base):
    expected_title = "compose.rawhide.complete (unsigned)"
    expected_subti = "rawhide compose completed"
    expected_link = \
        "https://alt.fedoraproject.org/pub/fedora/linux/development/rawhide"
    expected_objects = set(['rawhide'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.complete",
    }


class TestComposeRawhideStart(Base):
    expected_title = "compose.rawhide.start (unsigned)"
    expected_subti = "rawhide compose started"
    expected_objects = set(['rawhide'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.start",
    }


class TestComposeRawhideMashStart(Base):
    expected_title = "compose.rawhide.mash.start (unsigned)"
    expected_subti = "rawhide compose started mashing"
    expected_objects = set(['rawhide'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.mash.start",
    }


class TestComposeRawhideMashComplete(Base):
    expected_title = "compose.rawhide.mash.complete (unsigned)"
    expected_subti = "rawhide compose finished mashing"
    expected_objects = set(['rawhide'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.mash.complete",
    }


class TestComposeRawhideRsyncStart(Base):
    expected_title = "compose.rawhide.rsync.start (unsigned)"
    expected_subti = "started rsyncing rawhide compose for public consumption"
    expected_objects = set(['rawhide'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.rsync.start",
    }


class TestComposeRawhideRsyncComplete(Base):
    expected_title = "compose.rawhide.rsync.complete (unsigned)"
    expected_subti = "finished rsync of rawhide compose for public consumption"
    expected_link = \
        "https://alt.fedoraproject.org/pub/fedora/linux/development/rawhide"
    expected_objects = set(['rawhide'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.rsync.complete",
    }
