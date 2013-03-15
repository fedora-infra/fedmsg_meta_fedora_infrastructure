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


class TestLegacyComposeBranchedComplete(Base):
    """ This tests "old school" compose messages.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.branched.complete (unsigned)"
    expected_subti = "f18 compose completed"
    expected_link = \
        "https://alt.fedoraproject.org/pub/fedora/linux/development/f18"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.complete",
        "msg": {
            "log": "done",
            "branch": "f18",
        },
    }


class TestLegacyComposeBranchedStart(Base):
    """ This tests "old school" compose messages.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.branched.start (unsigned)"
    expected_subti = "f18 compose started"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.start",
        "msg": {
            "log": "start",
            "branch": "f18",
        },
    }


class TestLegacyComposeBranchedMashStart(Base):
    """ This tests "old school" compose messages.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.branched.mash.start (unsigned)"
    expected_subti = "f18 compose started mashing"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.mash.start",
        "msg": {
            "log": "start",
            "branch": "f18",
        },
    }


class TestLegacyComposeBranchedMashComplete(Base):
    """ This tests "old school" compose messages.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.branched.mash.complete (unsigned)"
    expected_subti = "f18 compose finished mashing"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.mash.complete",
        "msg": {
            "log": "done",
            "branch": "f18",
        },
    }


class TestLegacyComposeBranchedPungifyStart(Base):
    """ This tests "old school" compose messages.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.branched.pungify.start (unsigned)"
    expected_subti = "started building boot.iso for f18"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.pungify.start",
        "msg": {
            "log": "start",
            "branch": "f18",
        },
    }


class TestLegacyComposeBranchedPungifyComplete(Base):
    """ This tests "old school" compose messages.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.branched.pungify.complete (unsigned)"
    expected_subti = "finished building boot.iso for f18"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.pungify.complete",
        "msg": {
            "log": "done",
            "branch": "f18",
        },
    }


class TestLegacyComposeBranchedRsyncStart(Base):
    """ This tests "old school" compose messages.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.branched.rsync.start (unsigned)"
    expected_subti = "started rsyncing f18 compose"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.rsync.start",
        "msg": {
            "log": "start",
            "branch": "f18",
        },
    }


class TestLegacyComposeBranchedRsyncComplete(Base):
    """ This tests "old school" compose messages.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.branched.rsync.complete (unsigned)"
    expected_subti = \
        "finished rsync of f18 compose"
    expected_link = \
        "https://alt.fedoraproject.org/pub/fedora/linux/development/f18"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.rsync.complete",
        "msg": {
            "log": "done",
            "branch": "f18",
        },
    }


class TestLegacyComposeRawhideComplete(Base):
    """ This tests "old school" compose messages.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.rawhide.complete (unsigned)"
    expected_subti = "rawhide compose completed"
    expected_link = \
        "https://alt.fedoraproject.org/pub/fedora/linux/development/rawhide"
    expected_objects = set(['rawhide/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.complete",
        "msg": {
            "log": "done",
            "branch": "rawhide",
        },
    }


class TestLegacyComposeRawhideStart(Base):
    """ This tests "old school" compose messages.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.rawhide.start (unsigned)"
    expected_subti = "rawhide compose started"
    expected_objects = set(['rawhide/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.start",
        "msg": {
            "log": "start",
            "branch": "rawhide",
        },
    }


class TestLegacyComposeRawhideMashStart(Base):
    """ This tests "old school" compose messages.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.rawhide.mash.start (unsigned)"
    expected_subti = "rawhide compose started mashing"
    expected_objects = set(['rawhide/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.mash.start",
        "msg": {
            "log": "start",
            "branch": "rawhide",
        },
    }


class TestLegacyComposeRawhideMashComplete(Base):
    """ This tests "old school" compose messages.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.rawhide.mash.complete (unsigned)"
    expected_subti = "rawhide compose finished mashing"
    expected_objects = set(['rawhide/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.mash.complete",
        "msg": {
            "log": "done",
            "branch": "rawhide",
        },
    }


class TestLegacyComposeRawhideRsyncStart(Base):
    """ This tests "old school" compose messages.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.rawhide.rsync.start (unsigned)"
    expected_subti = "started rsyncing rawhide compose"
    expected_objects = set(['rawhide/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.rsync.start",
        "msg": {
            "log": "start",
            "branch": "rawhide",
        },
    }


class TestLegacyComposeRawhideRsyncComplete(Base):
    """ This tests "old school" compose messages.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.rawhide.rsync.complete (unsigned)"
    expected_subti = "finished rsync of rawhide compose"
    expected_link = \
        "https://alt.fedoraproject.org/pub/fedora/linux/development/rawhide"
    expected_objects = set(['rawhide/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.rsync.complete",
        "msg": {
            "log": "done",
            "branch": "rawhide",
        },
    }


class TestComposeBranchedComplete(Base):
    """ The `release engineering
    <http://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **finished composing**
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary).
    """
    expected_title = "compose.branched.complete (unsigned)"
    expected_subti = "f18 compose completed"
    expected_link = \
        "https://alt.fedoraproject.org/pub/fedora/linux/development/f18"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.complete",
        "msg": {
            "log": "done",
            "branch": "f18",
            "arch": "",
        },
    }


class TestComposeBranchedStart(Base):
    """ The `release engineering
    <http://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **begun composing**
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary).
    """
    expected_title = "compose.branched.start (unsigned)"
    expected_subti = "f18 compose started"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.start",
        "msg": {
            "log": "start",
            "branch": "f18",
            "arch": "",
        },
    }


class TestComposeBranchedMashStart(Base):
    """ The `release engineering
    <http://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **begun mashing** for
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary).
    """
    expected_title = "compose.branched.mash.start (unsigned)"
    expected_subti = "f18 compose started mashing"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.mash.start",
        "msg": {
            "log": "start",
            "branch": "f18",
            "arch": "",
        },
    }


class TestComposeBranchedMashComplete(Base):
    """ The `release engineering
    <http://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **finished mashing**
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary).
    """
    expected_title = "compose.branched.mash.complete (unsigned)"
    expected_subti = "f18 compose finished mashing"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.mash.complete",
        "msg": {
            "log": "done",
            "branch": "f18",
            "arch": "",
        },
    }


class TestComposeBranchedPungifyStart(Base):
    """ The `release engineering
    <http://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    started the `pungify <https://fedorahosted.org/pungi/>`_ process for
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary).
    """
    expected_title = "compose.branched.pungify.start (unsigned)"
    expected_subti = "started building boot.iso for f18"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.pungify.start",
        "msg": {
            "log": "start",
            "branch": "f18",
            "arch": "",
        },
    }


class TestComposeBranchedPungifyComplete(Base):
    """ The `release engineering
    <http://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    completed the `pungify <https://fedorahosted.org/pungi/>`_ process for
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary).
    """
    expected_title = "compose.branched.pungify.complete (unsigned)"
    expected_subti = "finished building boot.iso for f18"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.pungify.complete",
        "msg": {
            "log": "done",
            "branch": "f18",
            "arch": "",
        },
    }


class TestComposeBranchedRsyncStart(Base):
    """ The `release engineering
    <http://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    begun **rsyncing**
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary).
    """
    expected_title = "compose.branched.rsync.start (unsigned)"
    expected_subti = "started rsyncing f18 compose"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.rsync.start",
        "msg": {
            "log": "start",
            "branch": "f18",
            "arch": "",
        },
    }


class TestComposeBranchedRsyncComplete(Base):
    """ The `release engineering
    <http://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    finished **rsyncing**
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary).
    """
    expected_title = "compose.branched.rsync.complete (unsigned)"
    expected_subti = \
        "finished rsync of f18 compose"
    expected_link = \
        "https://alt.fedoraproject.org/pub/fedora/linux/development/f18"
    expected_objects = set(['branched/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.rsync.complete",
        "msg": {
            "log": "done",
            "branch": "f18",
            "arch": "",
        },
    }


class TestComposeRawhideComplete(Base):
    """ The `release engineering
    <http://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **finished** the rawhide compose.  They are published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary).
    """
    expected_title = "compose.rawhide.complete (unsigned)"
    expected_subti = "rawhide compose completed"
    expected_link = \
        "https://alt.fedoraproject.org/pub/fedora/linux/development/rawhide"
    expected_objects = set(['rawhide/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.complete",
        "msg": {
            "log": "done",
            "branch": "rawhide",
            "arch": "",
        },
    }


class TestComposeRawhideStart(Base):
    """ The `release engineering
    <http://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **started** the rawhide compose.  They are published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary).
    """
    expected_title = "compose.rawhide.start (unsigned)"
    expected_subti = "rawhide compose started"
    expected_objects = set(['rawhide/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.start",
        "msg": {
            "log": "start",
            "branch": "rawhide",
            "arch": "",
        },
    }


class TestComposeRawhideMashStart(Base):
    """ The `release engineering
    <http://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **started mashing** the rawhide compose.  They are published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary).
    """
    expected_title = "compose.rawhide.mash.start (unsigned)"
    expected_subti = "rawhide compose started mashing"
    expected_objects = set(['rawhide/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.mash.start",
        "msg": {
            "log": "start",
            "branch": "rawhide",
            "arch": "",
        },
    }


class TestComposeRawhideMashComplete(Base):
    """ The `release engineering
    <http://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **finished mashing** the rawhide compose.  They are published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary).
    """
    expected_title = "compose.rawhide.mash.complete (unsigned)"
    expected_subti = "rawhide compose finished mashing"
    expected_objects = set(['rawhide/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.mash.complete",
        "msg": {
            "log": "done",
            "branch": "rawhide",
            "arch": "",
        },
    }


class TestComposeRawhideRsyncStart(Base):
    """ The `release engineering
    <http://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **started rsyncing** the rawhide compose.  They are published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary).
    """
    expected_title = "compose.rawhide.rsync.start (unsigned)"
    expected_subti = "started rsyncing rawhide compose"
    expected_objects = set(['rawhide/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.rsync.start",
        "msg": {
            "log": "start",
            "branch": "rawhide",
            "arch": "",
        },
    }


class TestComposeRawhideRsyncComplete(Base):
    """ The `release engineering
    <http://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **finished rsyncing** the rawhide compose.  They are published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary).
    """
    expected_title = "compose.rawhide.rsync.complete (unsigned)"
    expected_subti = "finished rsync of rawhide compose"
    expected_link = \
        "https://alt.fedoraproject.org/pub/fedora/linux/development/rawhide"
    expected_objects = set(['rawhide/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.rsync.complete",
        "msg": {
            "log": "done",
            "branch": "rawhide",
            "arch": "",
        },
    }


class TestSecondaryArchComposeBranchedComplete(Base):
    """ The `release engineering
    <http://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **finished composing**
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **secondary** arch message.
    """
    expected_title = "compose.branched.complete (unsigned)"
    expected_subti = "f18 compose (arm) completed"
    expected_link = \
        "https://secondary.fedoraproject.org/pub/fedora-secondary/" + \
        "development/f18"
    expected_objects = set(['branched/arm'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.complete",
        "msg": {
            "log": "done",
            "branch": "f18",
            "arch": "arm",
        },
    }


class TestSecondaryArchComposeBranchedStart(Base):
    """ The `release engineering
    <http://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **started composing**
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **secondary** arch message.
    """
    expected_title = "compose.branched.start (unsigned)"
    expected_subti = "f18 compose (arm) started"
    expected_objects = set(['branched/arm'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.start",
        "msg": {
            "log": "start",
            "branch": "f18",
            "arch": "arm",
        },
    }


class TestSecondaryArchComposeBranchedMashStart(Base):
    """ The `release engineering
    <http://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **started mashing**
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **secondary** arch message.
    """
    expected_title = "compose.branched.mash.start (unsigned)"
    expected_subti = "f18 compose (arm) started mashing"
    expected_objects = set(['branched/arm'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.mash.start",
        "msg": {
            "log": "start",
            "branch": "f18",
            "arch": "arm",
        },
    }


class TestSecondaryArchComposeBranchedMashComplete(Base):
    """ The `release engineering
    <http://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **finished mashing**
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **secondary** arch message.
    """
    expected_title = "compose.branched.mash.complete (unsigned)"
    expected_subti = "f18 compose (arm) finished mashing"
    expected_objects = set(['branched/arm'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.mash.complete",
        "msg": {
            "log": "done",
            "branch": "f18",
            "arch": "arm",
        },
    }


class TestSecondaryArchComposeBranchedPungifyStart(Base):
    """ The `release engineering
    <http://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    started the `pungify <https://fedorahosted.org/pungi/>`_ process for
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **secondary** arch message.
    """
    expected_title = "compose.branched.pungify.start (unsigned)"
    expected_subti = "started building boot.iso for f18 (arm)"
    expected_objects = set(['branched/arm'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.pungify.start",
        "msg": {
            "log": "start",
            "branch": "f18",
            "arch": "arm",
        },
    }


class TestSecondaryArchComposeBranchedPungifyComplete(Base):
    """ The `release engineering
    <http://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    completed the `pungify <https://fedorahosted.org/pungi/>`_ process for
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **secondary** arch message.
    """
    expected_title = "compose.branched.pungify.complete (unsigned)"
    expected_subti = "finished building boot.iso for f18 (arm)"
    expected_objects = set(['branched/arm'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.pungify.complete",
        "msg": {
            "log": "done",
            "branch": "f18",
            "arch": "arm",
        },
    }


class TestSecondaryArchComposeBranchedRsyncStart(Base):
    """ The `release engineering
    <http://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **started rsyncing**
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **secondary** arch message.
    """
    expected_title = "compose.branched.rsync.start (unsigned)"
    expected_subti = "started rsyncing f18 compose (arm)"
    expected_objects = set(['branched/arm'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.rsync.start",
        "msg": {
            "log": "start",
            "branch": "f18",
            "arch": "arm",
        },
    }


class TestSecondaryArchComposeBranchedRsyncComplete(Base):
    """ The `release engineering
    <http://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **finished rsyncing**
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **secondary** arch message.
    """
    expected_title = "compose.branched.rsync.complete (unsigned)"
    expected_subti = \
        "finished rsync of f18 compose (arm)"
    expected_link = \
        "https://secondary.fedoraproject.org/pub/fedora-secondary/" + \
        "development/f18"
    expected_objects = set(['branched/arm'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.branched.rsync.complete",
        "msg": {
            "log": "done",
            "branch": "f18",
            "arch": "arm",
        },
    }


class TestSecondaryArchComposeRawhideComplete(Base):
    """ The `release engineering
    <http://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **finished** the rawhide compose.  They are published
    for both primary and secondary architectures.  The example here is of a
    **secondary** arch message.
    """
    expected_title = "compose.rawhide.complete (unsigned)"
    expected_subti = "rawhide compose (arm) completed"
    expected_link = \
        "https://secondary.fedoraproject.org/pub/fedora-secondary/" + \
        "development/rawhide"
    expected_objects = set(['rawhide/arm'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.complete",
        "msg": {
            "log": "done",
            "branch": "rawhide",
            "arch": "arm",
        },
    }


class TestSecondaryArchComposeRawhideStart(Base):
    """ The `release engineering
    <http://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **started** the rawhide compose.  They are published
    for both primary and secondary architectures.  The example here is of a
    **secondary** arch message.
    """
    expected_title = "compose.rawhide.start (unsigned)"
    expected_subti = "rawhide compose (arm) started"
    expected_objects = set(['rawhide/arm'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.start",
        "msg": {
            "log": "start",
            "branch": "rawhide",
            "arch": "arm",
        },
    }


class TestSecondaryArchComposeRawhideMashStart(Base):
    """ The `release engineering
    <http://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **started mashing** the rawhide compose.  They are published
    for both primary and secondary architectures.  The example here is of a
    **secondary** arch message.
    """
    expected_title = "compose.rawhide.mash.start (unsigned)"
    expected_subti = "rawhide compose (arm) started mashing"
    expected_objects = set(['rawhide/arm'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.mash.start",
        "msg": {
            "log": "start",
            "branch": "rawhide",
            "arch": "arm",
        },
    }


class TestSecondaryArchComposeRawhideMashComplete(Base):
    """ The `release engineering
    <http://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **finished mashing** the rawhide compose.  They are published
    for both primary and secondary architectures.  The example here is of a
    **secondary** arch message.
    """
    expected_title = "compose.rawhide.mash.complete (unsigned)"
    expected_subti = "rawhide compose (arm) finished mashing"
    expected_objects = set(['rawhide/arm'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.mash.complete",
        "msg": {
            "log": "done",
            "branch": "rawhide",
            "arch": "arm",
        },
    }


class TestSecondaryArchComposeRawhideRsyncStart(Base):
    """ The `release engineering
    <http://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **started rsyncing** the rawhide compose.  They are published
    for both primary and secondary architectures.  The example here is of a
    **secondary** arch message.
    """
    expected_title = "compose.rawhide.rsync.start (unsigned)"
    expected_subti = "started rsyncing rawhide compose (arm)"
    expected_objects = set(['rawhide/arm'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.rsync.start",
        "msg": {
            "log": "start",
            "branch": "rawhide",
            "arch": "arm",
        },
    }


class TestSecondaryArchComposeRawhideRsyncComplete(Base):
    """ The `release engineering
    <http://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **finished rsyncing** the rawhide compose.  They are published
    for both primary and secondary architectures.  The example here is of a
    **secondary** arch message.
    """
    expected_title = "compose.rawhide.rsync.complete (unsigned)"
    expected_subti = \
        "finished rsync of rawhide compose (arm)"
    expected_link = \
        "https://secondary.fedoraproject.org/pub/fedora-secondary/" + \
        "development/rawhide"
    expected_objects = set(['rawhide/arm'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.rawhide.rsync.complete",
        "msg": {
            "log": "done",
            "branch": "rawhide",
            "arch": "arm",
        },
    }
