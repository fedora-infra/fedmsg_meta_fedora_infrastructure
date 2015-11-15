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

import unittest

from fedmsg.tests.test_meta import Base

from .common import add_doc


class TestTwoWeekAtomicBegin(Base):
    """ As one of the final steps in the `two week atomic
    <https://fedoraproject.org/wiki/Changes/Two_Week_Atomic>`_ process, there
    is a release engineering script (the green box in `this diagram
    <https://fedoraproject.org/wiki/File:TwoWeekAtomic-Overview-v2.png>`_) that
    determines if the builds of Fedora Atomic Host are fit for release.

    If it determines that the builds are ready (usually by cross-referencing
    test results from `autocloud <https://apps.fedoraproject.org/autocloud>`_),
    then it publishes one of these messages, indicating that the website should
    be updated to link to the new builds.
    """

    expected_title = "releng.atomic.twoweek.begin"
    expected_subti = "Release engineering scripts started evaluating a " + \
        "new set of builds for a Fedora 22 Atomic Host release"
    expected_icon = "https://apps.fedoraproject.org/img/icons/atomic.png"
    expected_secondary_icon = "https://apps.fedoraproject.org/img/icons/atomic.png"
    expected_link = "https://download.fedoraproject.org/pub/alt/atomic/stable/"
    expected_objects = set(['22/atomic_qcow2', '22/atomic_raw'])

    msg = {
        "timestamp": 1444939709.0,
        "topic": "org.fedoraproject.prod.releng.atomic.twoweek.begin",
        "msg": {
            "atomic_qcow2": {
                "release": "22",
                "image_url": "https://kojipkgs.fedoraproject.org//work/tasks/"
                "3513/11453513/Fedora-Cloud-Atomic-22-20151015.x86_64.qcow2",
                "image_name": "Fedora-Cloud-Atomic-22-20151015.x86_64.qcow2",
                "name": "Fedora-Cloud-Atomic"
            },
            "atomic_raw": {
                "release": "22",
                "image_url": "https://kojipkgs.fedoraproject.org//work/tasks/"
                "3513/11453513/Fedora-Cloud-Atomic-22-20151015.x86_64.raw.xz",
                "image_name": "Fedora-Cloud-Atomic-22-20151015.x86_64.raw.xz",
                "name": "Fedora-Cloud-Atomic-Raw"
            }
        }
    }


class TestTwoWeekAtomicComplete(Base):
    """ As one of the final steps in the `two week atomic
    <https://fedoraproject.org/wiki/Changes/Two_Week_Atomic>`_ process, there
    is a release engineering script (the green box in `this diagram
    <https://fedoraproject.org/wiki/File:TwoWeekAtomic-Overview-v2.png>`_) that
    determines if the builds of Fedora Atomic Host are fit for release.

    If it determines that the builds are ready (usually by cross-referencing
    test results from `autocloud <https://apps.fedoraproject.org/autocloud>`_),
    then it publishes one of these messages, indicating that the website should
    be updated to link to the new builds.
    """

    expected_title = "releng.atomic.twoweek.complete"
    expected_subti = "A new release of Fedora 22 Atomic Host is ready"
    expected_icon = "https://apps.fedoraproject.org/img/icons/atomic.png"
    expected_secondary_icon = "https://apps.fedoraproject.org/img/icons/atomic.png"
    expected_link = "https://download.fedoraproject.org/pub/alt/atomic/stable/"
    expected_objects = set(['22/atomic_qcow2', '22/atomic_raw'])

    msg = {
        "timestamp": 1444939709.0,
        "topic": "org.fedoraproject.prod.releng.atomic.twoweek.complete",
        "msg": {
            "atomic_qcow2": {
                "release": "22",
                "image_url": "https://kojipkgs.fedoraproject.org//work/tasks/"
                "3513/11453513/Fedora-Cloud-Atomic-22-20151015.x86_64.qcow2",
                "image_name": "Fedora-Cloud-Atomic-22-20151015.x86_64.qcow2",
                "name": "Fedora-Cloud-Atomic"
            },
            "atomic_raw": {
                "release": "22",
                "image_url": "https://kojipkgs.fedoraproject.org//work/tasks/"
                "3513/11453513/Fedora-Cloud-Atomic-22-20151015.x86_64.raw.xz",
                "image_name": "Fedora-Cloud-Atomic-22-20151015.x86_64.raw.xz",
                "name": "Fedora-Cloud-Atomic-Raw"
            }
        }
    }


add_doc(locals())
