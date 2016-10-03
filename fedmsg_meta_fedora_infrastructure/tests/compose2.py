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


class TestPungiKojiStart(Base):
    """ In 2016, the `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ team started moving
    the compose process to ``pungi4``, which emits messages like this as it
    does its composition work.

    Here's an example message published when a compose starts.
    """
    expected_title = "pungi.compose.status.change"
    expected_subti = "pungi-koji compose of Fedora-24-20151208.n.7 started"
    expected_link = "http://kojipkgs.fedoraproject.org/" + \
        "compose//rawhide/Fedora-24-20151208.n.7"
    expected_objects = set(['rawhide/Fedora-24-20151208/n/7'])
    msg = {
        "msg": {
            "compose_id": "Fedora-24-20151208.n.7",
            "location": "http://kojipkgs.fedoraproject.org/compose/"
            "/rawhide/Fedora-24-20151208.n.7/compose",
            "status": "STARTED"
        },
        "timestamp": 1449600728.0,
        "topic": "org.fedoraproject.prod.pungi.compose.status.change"
    }


class TestPungiKojiComplete(Base):
    """ In 2016, the `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ team started moving
    the compose process to ``pungi4``, which emits messages like this as it
    does its composition work.

    Here's an example message published when a compose starts.
    """
    expected_title = "pungi.compose.status.change"
    expected_subti = "pungi-koji compose of Fedora-24-20151208.n.7 just finished"
    expected_link = "http://kojipkgs.fedoraproject.org/" + \
        "compose//rawhide/Fedora-24-20151208.n.7"
    expected_objects = set(['rawhide/Fedora-24-20151208/n/7'])
    msg = {
        "msg": {
            "compose_id": "Fedora-24-20151208.n.7",
            "location": "http://kojipkgs.fedoraproject.org/compose/"
            "/rawhide/Fedora-24-20151208.n.7/compose",
            "status": "FINISHED"
        },
        "timestamp": 1449600728.0,
        "topic": "org.fedoraproject.prod.pungi.compose.status.change"
    }


class TestPungiPhaseStart(Base):
    """ In 2016, the `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ team started moving
    the compose process to ``pungi4``, which emits messages like this as it
    does its composition work.

    Here's an example message published when the ``createrepo`` phase of a
    compose starts.
    """
    expected_title = "pungi.compose.phase.start"
    expected_subti = "pungi-koji started the createrepo phase of the " + \
        "Fedora-24-20151208.n.7 compose"
    expected_link = "http://kojipkgs.fedoraproject.org/" + \
        "compose//rawhide/Fedora-24-20151208.n.7"
    expected_objects = set(['rawhide/Fedora-24-20151208/n/7'])
    msg = {
        "i": 1,
        "timestamp": 1449605930.0,
        "msg_id": "2015-05ea75ce-f648-41b5-9e29-da56202a2ba5",
        "topic": "org.fedoraproject.prod.pungi.compose.phase.start",
        "msg": {
            "phase_name": "createrepo",
            "compose_id": "Fedora-24-20151208.n.7",
            "location": "http://kojipkgs.fedoraproject.org/compose/"
            "/rawhide/Fedora-24-20151208.n.7/compose",
        }
    }


class TestPungiCreateISOTargets(Base):
    """ In 2016, the `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ team started moving
    the compose process to ``pungi4``, which emits messages like this as it
    does its composition work.

    Here's an example message published when createiso targets are assigned.
    """
    expected_title = "pungi.compose.createiso.targets"
    expected_subti = "pungi-koji assigned 3 createiso targets"
    expected_link = "http://kojipkgs.fedoraproject.org/" + \
        "compose//rawhide/Fedora-24-20151208.n.7"
    expected_objects = set([
        "mnt/koji/compose/rawhide/Fedora-24-20151208.n.7/compose/Server/"
        "armhfp/iso/Fedora-24-20151208.n.7-Server-armhfp-dvd1.iso",
        "mnt/koji/compose/rawhide/Fedora-24-20151208.n.7/compose/Server/"
        "i386/iso/Fedora-24-20151208.n.7-Server-i386-dvd1.iso",
        "mnt/koji/compose/rawhide/Fedora-24-20151208.n.7/compose/Server/"
        "x86_64/iso/Fedora-24-20151208.n.7-Server-x86_64-dvd1.iso",
    ])
    msg = {
        "i": 1,
        "timestamp": 1449605930.0,
        "msg_id": "2015-05ea75ce-f648-41b5-9e29-da56202a2ba5",
        "topic": "org.fedoraproject.prod.pungi.compose.createiso.targets",
        "msg": {
            "deliverables": [
                "/mnt/koji/compose/rawhide/Fedora-24-20151208.n.7/compose/Server/armhfp/iso/Fedora-24-20151208.n.7-Server-armhfp-dvd1.iso",
                "/mnt/koji/compose/rawhide/Fedora-24-20151208.n.7/compose/Server/i386/iso/Fedora-24-20151208.n.7-Server-i386-dvd1.iso",
                "/mnt/koji/compose/rawhide/Fedora-24-20151208.n.7/compose/Server/x86_64/iso/Fedora-24-20151208.n.7-Server-x86_64-dvd1.iso"
            ],
            "compose_id": "Fedora-24-20151208.n.7",
            "location": "http://kojipkgs.fedoraproject.org/compose/"
            "/rawhide/Fedora-24-20151208.n.7/compose",
        }
    }


class TestPungiCreateISOWin(Base):
    """ In 2016, the `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ team started moving
    the compose process to ``pungi4``, which emits messages like this as it
    does its composition work.

    Here's an example message published when a createiso target completes.
    """
    expected_title = "pungi.compose.createiso.imagedone"
    expected_subti = "pungi-koji finished createiso for " + \
            "Server/i386/iso/Fedora-24-20151208.n.7-Server-i386-dvd1.iso"
    expected_link = "http://kojipkgs.fedoraproject.org/" + \
        "compose//rawhide/Fedora-24-20151208.n.7"
    expected_objects = set([
        "mnt/koji/compose/rawhide/Fedora-24-20151208.n.7/compose/Server/"
        "i386/iso/Fedora-24-20151208.n.7-Server-i386-dvd1.iso",
    ])
    msg = {
        "i": 1,
        "timestamp": 1449605930.0,
        "msg_id": "2015-05ea75ce-f648-41b5-9e29-da56202a2ba5",
        "topic": "org.fedoraproject.prod.pungi.compose.createiso.imagedone",
        "msg": {
            "variant": "Server",
            "arch": "i386",
            "file": "/mnt/koji/compose/rawhide/Fedora-24-20151208.n.7/compose"
            "/Server/i386/iso/Fedora-24-20151208.n.7-Server-i386-dvd1.iso",
            "compose_id": "Fedora-24-20151208.n.7",
            "location": "http://kojipkgs.fedoraproject.org/compose/"
            "/rawhide/Fedora-24-20151208.n.7/compose",
        }
    }


class TestPungiOstree(Base):
    """ In 2016, the `release engineering
    <https://fedoraproject.org/wiki/ReleaseEngineering>`_ team started moving
    the compose process to ``pungi4``, which emits messages like this as it
    does its composition work.

    Here's an example message published when an ostree phase completed
    succesfully.
    """
    cid = 'f99114401ffce2753bd7cd5401bff056a029bb80474859ab769f68586978248d'
    expected_title = "pungi.compose.ostree"
    expected_subti = "pungi-koji ostree compose Fedora-25-20161002.n.0 " + \
        "produced ostree commit %s for x86_64 " % cid + \
        "fedora-atomic/25/x86_64/docker-host"
    expected_link = "http://kojipkgs.fedoraproject.org/" + \
        "compose//branched/Fedora-25-20161002.n.0"
    expected_objects = set([
        "rawhide/Fedora-25-20161002/n/0"
    ])
    msg = {
        "i": 1, 
        "timestamp": 1475402944.0, 
        "msg_id": "2016-7e49afa4-c85b-424b-90d8-da36bed006b5", 
        "topic": "org.fedoraproject.prod.pungi.compose.ostree", 
        "msg": {
            "arch": "x86_64", 
            "variant": "Atomic", 
            "commitid": "f99114401ffce2753bd7cd5401bff056a029bb80474859ab769f68586978248d", 
            "location": "http://kojipkgs.fedoraproject.org/compose//branched/Fedora-25-20161002.n.0/compose", 
            "ref": "fedora-atomic/25/x86_64/docker-host", 
            "compose_id": "Fedora-25-20161002.n.0"
        }
    }


add_doc(locals())
