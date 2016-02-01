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
""" Tests for compose messages """

from fedmsg.tests.test_meta import Base

from .common import add_doc


class TestLegacyComposeBranchedComplete(Base):
    """ This tests "old school" compose messages.

    :mod:`fedmsg.meta` needs to be able to handle them because they are
    stored, forever, in datanommer.
    """
    expected_title = "compose.branched.complete"
    expected_subti = "f18 compose completed"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora/linux/development/f18"
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
    expected_title = "compose.branched.start"
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
    expected_title = "compose.branched.mash.start"
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
    expected_title = "compose.branched.mash.complete"
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
    expected_title = "compose.branched.pungify.start"
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
    expected_title = "compose.branched.pungify.complete"
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
    expected_title = "compose.branched.rsync.start"
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
    expected_title = "compose.branched.rsync.complete"
    expected_subti = \
        "finished rsync of f18 compose"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora/linux/development/f18"
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
    expected_title = "compose.rawhide.complete"
    expected_subti = "rawhide compose completed"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora/linux/development/rawhide"
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
    expected_title = "compose.rawhide.start"
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
    expected_title = "compose.rawhide.mash.start"
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
    expected_title = "compose.rawhide.mash.complete"
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
    expected_title = "compose.rawhide.rsync.start"
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
    expected_title = "compose.rawhide.rsync.complete"
    expected_subti = "finished rsync of rawhide compose"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora/linux/development/rawhide"
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
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **finished composing**
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary).
    """
    expected_title = "compose.branched.complete"
    expected_subti = "f18 compose completed"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora/linux/development/f18"
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


class TestComposeEPELBetaComplete(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have **finished composing** the EPEL beta.
    """
    expected_title = "compose.epelbeta.complete"
    expected_subti = "epelbeta compose completed"
    expected_link = "https://dl.fedoraproject.org/pub/epel/beta/7/"
    expected_objects = set(['epelbeta/primary'])
    msg = {
        "i": 1,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.compose.epelbeta.complete",
        "msg": {
            "log": "done",
        },
    }


class TestComposeBranchedStart(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **begun composing**
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary).
    """
    expected_title = "compose.branched.start"
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
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **begun mashing** for
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary).
    """
    expected_title = "compose.branched.mash.start"
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
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **finished mashing**
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary).
    """
    expected_title = "compose.branched.mash.complete"
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
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    started the `pungify <https://fedorahosted.org/pungi/>`_ process for
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary).
    """
    expected_title = "compose.branched.pungify.start"
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
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    completed the `pungify <https://fedorahosted.org/pungi/>`_ process for
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary).
    """
    expected_title = "compose.branched.pungify.complete"
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
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    begun **rsyncing**
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary).
    """
    expected_title = "compose.branched.rsync.start"
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
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    finished **rsyncing**
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary).
    """
    expected_title = "compose.branched.rsync.complete"
    expected_subti = \
        "finished rsync of f18 compose"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora/linux/development/f18"
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
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **finished** the rawhide compose.  They are published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary).
    """
    expected_title = "compose.rawhide.complete"
    expected_subti = "rawhide compose completed"
    expected_objects = set(['rawhide/primary'])
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora/linux/development/rawhide"
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
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **started** the rawhide compose.  They are published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary).
    """
    expected_title = "compose.rawhide.start"
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
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **started mashing** the rawhide compose.  They are published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary).
    """
    expected_title = "compose.rawhide.mash.start"
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
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **finished mashing** the rawhide compose.  They are published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary).
    """
    expected_title = "compose.rawhide.mash.complete"
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
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **started rsyncing** the rawhide compose.  They are published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary).
    """
    expected_title = "compose.rawhide.rsync.start"
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
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **finished rsyncing** the rawhide compose.  They are published
    for both primary and secondary architectures.  The example here is of a
    **primary** arch message (the empty string signifies primary).
    """
    expected_title = "compose.rawhide.rsync.complete"
    expected_subti = "finished rsync of rawhide compose"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora/linux/development/rawhide"
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
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **finished composing**
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **secondary** arch message.
    """
    expected_title = "compose.branched.complete"
    expected_subti = "f18 compose (arm) completed"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora-secondary/" + \
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
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **started composing**
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **secondary** arch message.
    """
    expected_title = "compose.branched.start"
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
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **started mashing**
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **secondary** arch message.
    """
    expected_title = "compose.branched.mash.start"
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
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **finished mashing**
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **secondary** arch message.
    """
    expected_title = "compose.branched.mash.complete"
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
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    started the `pungify <https://fedorahosted.org/pungi/>`_ process for
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **secondary** arch message.
    """
    expected_title = "compose.branched.pungify.start"
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
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    completed the `pungify <https://fedorahosted.org/pungi/>`_ process for
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **secondary** arch message.
    """
    expected_title = "compose.branched.pungify.complete"
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
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **started rsyncing**
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **secondary** arch message.
    """
    expected_title = "compose.branched.rsync.start"
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
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **finished rsyncing**
    whatever the current branched distribution version is.  They are published
    for both primary and secondary architectures.  The example here is of a
    **secondary** arch message.
    """
    expected_title = "compose.branched.rsync.complete"
    expected_subti = \
        "finished rsync of f18 compose (arm)"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora-secondary/" + \
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
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **finished** the rawhide compose.  They are published
    for both primary and secondary architectures.  The example here is of a
    **secondary** arch message.
    """
    expected_title = "compose.rawhide.complete"
    expected_subti = "rawhide compose (arm) completed"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora-secondary/" + \
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
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **started** the rawhide compose.  They are published
    for both primary and secondary architectures.  The example here is of a
    **secondary** arch message.
    """
    expected_title = "compose.rawhide.start"
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
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **started mashing** the rawhide compose.  They are published
    for both primary and secondary architectures.  The example here is of a
    **secondary** arch message.
    """
    expected_title = "compose.rawhide.mash.start"
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
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **finished mashing** the rawhide compose.  They are published
    for both primary and secondary architectures.  The example here is of a
    **secondary** arch message.
    """
    expected_title = "compose.rawhide.mash.complete"
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
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **started rsyncing** the rawhide compose.  They are published
    for both primary and secondary architectures.  The example here is of a
    **secondary** arch message.
    """
    expected_title = "compose.rawhide.rsync.start"
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
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have
    **finished rsyncing** the rawhide compose.  They are published
    for both primary and secondary architectures.  The example here is of a
    **secondary** arch message.
    """
    expected_title = "compose.rawhide.rsync.complete"
    expected_subti = \
        "finished rsync of rawhide compose (arm)"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora-secondary/" + \
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


class TestMakeUpdatesStarted(Base):
    """ The `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ "compose" scripts
    produce these messages when they have **started** the make-updates process
    (which is how we do periodic re-spins of our cloud, atomic, and docker
    images).  Here's an example of a message from F23:
    """
    expected_title = "compose.23.make-updates.start"
    expected_subti = \
        "started a run of F23 make-updates"
    expected_link = \
        "https://dl.fedoraproject.org/pub/fedora/linux/releases/23"
    expected_objects = set(['23/primary'])
    msg = {
        "i": 1,
        "msg": {
            "branch": "23",
            "log": "start"
        },
        "timestamp": 1454303707.0,
        "topic": "org.fedoraproject.prod.compose.23.make-updates.start"
    }


add_doc(locals())
