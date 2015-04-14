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
""" Tests for ftpsync messages """

from fedmsg_meta_fedora_infrastructure.tests.base import Base

from .common import add_doc


class TestFTPSyncAtomic(Base):
    """ These messages are published when a new compose of Fedora Atomic
    is synced out to the master mirror.
    """
    expected_title = "bodhi.updates.fedora.sync"
    expected_subti = "New Fedora 21 atomic content synced out " + \
        "(60.38M changed with 0 files deleted)"
    expected_link = \
        "https://download.fedoraproject.org/pub/fedora/linux/atomic/21/"
    expected_objects = set(['fedora/atomic/21'])

    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.bodhi.updates.fedora.sync",
        "msg": {
            "bytes": "60.38M",
            "deleted": "0",
            "repo": "atomic",
            "release": "21",
        },
    }


class TestFTPSyncFedora(Base):
    """ These messages are published when new updates (fresh out of the "mash"
    process) are synced out to the master mirror.

    Here's an example for the fedora 20 stable repos:
    """
    expected_title = "bodhi.updates.fedora.sync"
    expected_subti = "New Fedora 20 updates content synced out " + \
        "(2.8M changed with 0 files deleted)"
    expected_link = \
        "https://download.fedoraproject.org/pub/fedora/linux/updates/20/"
    expected_objects = set(['fedora/updates/20'])

    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.bodhi.updates.fedora.sync",
        "msg": {
            "bytes": "2.8M",
            "deleted": "0",
            "repo": "updates",
            "release": "20",
        },
    }


class TestFTPSyncEPELTesting(Base):
    """ These messages are published when new updates (fresh out of the "mash"
    process) are synced out to the master mirror.

    Here's an example for the epel 6 testing repos:
    """
    expected_title = "bodhi.updates.epel.sync"
    expected_subti = "New EPEL 6 epel-testing content synced out " + \
        "(28493k changed with 0 files deleted)"
    expected_link = \
        "https://download.fedoraproject.org/pub/epel/testing/6/"
    expected_objects = set(['epel/epel-testing/6'])

    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.bodhi.updates.epel.sync",
        "msg": {
            "bytes": "28493k",
            "deleted": "0",
            "repo": "epel-testing",
            "release": "6",
        },
    }


add_doc(locals())
