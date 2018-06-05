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
    is a `release engineering script
    <https://pagure.io/releng/blob/master/f/scripts/push-two-week-atomic.py>`_ that
    runs to perform the release.

    During the two week script run, it fetches AtomicHost artifacts detail
    for given pungi compose ID using `fedfind
    <https://pagure.io/fedora-qa/fedfind/>`_ . After getting image
    artifacts and ostree commit information successfully for all supported
    architectures, it sends this fedmsg indicating that Two Week release process has started.
    """

    expected_title = "releng.atomic.twoweek.begin"
    expected_subti = "Release engineering scripts started evaluating a " + \
        "new set of builds for a Fedora 28 Atomic Host release"
    expected_icon = "https://apps.fedoraproject.org/img/icons/atomic.png"
    expected_secondary_icon = "https://apps.fedoraproject.org/img/icons/atomic.png"
    expected_link = "https://download.fedoraproject.org/pub/alt/atomic/stable/"
    expected_objects = set([u'aarch64', u'x86_64', u'ppc64le'])

    msg = {
        u'timestamp': 1444939709.0,
        u'topic': u'org.fedoraproject.prod.releng.atomic.twoweek.begin',
        u'msg': {
            u'aarch64': {
                u'atomic_dvd_ostree': {
                    u'name': u'Fedora-AtomicHost-ostree-aarch64-28-20180515.1.iso',
                    u'image_name': u'Fedora-AtomicHost-ostree-aarch64-28-20180515.1.iso',
                    u'image_url': u'/pub/alt/atomic/stable/Fedora-Atomic-28-20180515.1/AtomicHost/'
                    'aarch64/iso/Fedora-AtomicHost-ostree-aarch64-28-20180515.1.iso',
                    u'release': u'28',
                    u'compose_id': u'Fedora-Atomic-28-20180515.1',
                    u'size': 988649472
                },
                u'atomic_qcow2': {
                    u'name': u'Fedora-AtomicHost-28-20180515.1',
                    u'image_name': u'Fedora-AtomicHost-28-20180515.1.aarch64.qcow2',
                    u'image_url': u'/pub/alt/atomic/stable/Fedora-Atomic-28-20180515.1/'
                    'AtomicHost/aarch64/images/Fedora-AtomicHost-28-20180515.1.aarch64.qcow2',
                    u'release': u'28',
                    u'compose_id': u'Fedora-Atomic-28-20180515.1',
                    u'size': 621911040
                },
                u'atomic_raw': {
                    u'name': u'Fedora-AtomicHost-28-20180515.1',
                    u'image_name': u'Fedora-AtomicHost-28-20180515.1.aarch64.raw.xz',
                    u'image_url': u'/pub/alt/atomic/stable/Fedora-Atomic-28-20180515.1/'
                    'AtomicHost/aarch64/images/Fedora-AtomicHost-28-20180515.1.aarch64.raw.xz',
                    u'release': u'28',
                    u'compose_id': u'Fedora-Atomic-28-20180515.1',
                    u'size': 396619232
                }
            },
            u'x86_64': {
                u'atomic_dvd_ostree': {
                    u'name': u'Fedora-AtomicHost-ostree-x86_64-28-20180515.1.iso',
                    u'image_name': u'Fedora-AtomicHost-ostree-x86_64-28-20180515.1.iso',
                    u'image_url': u'/pub/alt/atomic/stable/Fedora-Atomic-28-20180515.1/AtomicHost/'
                    'x86_64/iso/Fedora-AtomicHost-ostree-x86_64-28-20180515.1.iso',
                    u'release': u'28',
                    u'compose_id': u'Fedora-Atomic-28-20180515.1',
                    u'size': 1034944512
                },
                u'atomic_qcow2': {
                    u'name': u'Fedora-AtomicHost-28-20180515.1',
                    u'image_name': u'Fedora-AtomicHost-28-20180515.1.x86_64.qcow2',
                    u'image_url': u'/pub/alt/atomic/stable/Fedora-Atomic-28-20180515.1/'
                    'AtomicHost/x86_64/images/Fedora-AtomicHost-28-20180515.1.x86_64.qcow2',
                    u'release': u'28',
                    u'compose_id': u'Fedora-Atomic-28-20180515.1',
                    u'size': 635537920
                },
                u'atomic_raw': {
                    u'name': u'Fedora-AtomicHost-28-20180515.1',
                    u'image_name': u'Fedora-AtomicHost-28-20180515.1.x86_64.raw.xz',
                    u'image_url': u'/pub/alt/atomic/stable/Fedora-Atomic-28-20180515.1/'
                    'AtomicHost/x86_64/images/Fedora-AtomicHost-28-20180515.1.x86_64.raw.xz',
                    u'release': u'28',
                    u'compose_id': u'Fedora-Atomic-28-20180515.1',
                    u'size': 457994952
                },
                u'atomic_vagrant_libvirt': {
                    u'name': u'Fedora-AtomicHost-Vagrant-28-20180515.1',
                    u'image_name': u'Fedora-AtomicHost-Vagrant-28-20180515.1.x86_64.vagrant-libvirt.box',
                    u'image_url': u'/pub/alt/atomic/stable/Fedora-Atomic-28-20180515.1/AtomicHost/'
                    'x86_64/images/Fedora-AtomicHost-Vagrant-28-20180515.1.x86_64.vagrant-libvirt.box',
                    u'release': u'28',
                    u'compose_id': u'Fedora-Atomic-28-20180515.1',
                    u'size': 603786982
                },
                u'atomic_vagrant_virtualbox': {
                    u'name': u'Fedora-AtomicHost-Vagrant-28-20180515.1',
                    u'image_name': u'Fedora-AtomicHost-Vagrant-28-20180515.1.x86_64.vagrant-virtualbox.box',
                    u'image_url': u'/pub/alt/atomic/stable/Fedora-Atomic-28-20180515.1/AtomicHost/'
                    'x86_64/images/Fedora-AtomicHost-Vagrant-28-20180515.1.x86_64.vagrant-virtualbox.box',
                    u'release': u'28',
                    u'compose_id': u'Fedora-Atomic-28-20180515.1',
                    u'size': 617984000
                }
            },
            u'ppc64le': {
                u'atomic_dvd_ostree': {
                    u'name': u'Fedora-AtomicHost-ostree-ppc64le-28-20180515.1.iso',
                    u'image_name': u'Fedora-AtomicHost-ostree-ppc64le-28-20180515.1.iso',
                    u'image_url': u'/pub/alt/atomic/stable/Fedora-Atomic-28-20180515.1/AtomicHost/'
                    'ppc64le/iso/Fedora-AtomicHost-ostree-ppc64le-28-20180515.1.iso',
                    u'release': u'28',
                    u'compose_id': u'Fedora-Atomic-28-20180515.1',
                    u'size': 1036103680
                },
                u'atomic_qcow2': {
                    u'name': u'Fedora-AtomicHost-28-20180515.1',
                    u'image_name': u'Fedora-AtomicHost-28-20180515.1.ppc64le.qcow2',
                    u'image_url': u'/pub/alt/atomic/stable/Fedora-Atomic-28-20180515.1/AtomicHost/'
                    'ppc64le/images/Fedora-AtomicHost-28-20180515.1.ppc64le.qcow2',
                    u'release': u'28',
                    u'compose_id': u'Fedora-Atomic-28-20180515.1',
                    u'size': 636539904
                },
                u'atomic_raw': {
                    u'name': u'Fedora-AtomicHost-28-20180515.1',
                    u'image_name': u'Fedora-AtomicHost-28-20180515.1.ppc64le.raw.xz',
                    u'image_url': u'/pub/alt/atomic/stable/Fedora-Atomic-28-20180515.1/AtomicHost/'
                    'ppc64le/images/Fedora-AtomicHost-28-20180515.1.ppc64le.raw.xz',
                    u'release': u'28',
                    u'compose_id': u'Fedora-Atomic-28-20180515.1',
                    u'size': 411513572
                }
            }
        }
    }


class TestTwoWeekAtomicComplete(Base):
    """ As one of the final steps in the `two week atomic
    <https://fedoraproject.org/wiki/Changes/Two_Week_Atomic>`_ process, there
    is a `release engineering script
    <https://pagure.io/releng/blob/master/f/scripts/push-two-week-atomic.py>`_ that
    runs to perform the release.

    During this phase of two week script run, static delta gets generated
    from previous Two Week release. Later ref in repo gets updated with
    latest ostree commit information for each arch, followed by Two Week
    release announcement email.
    On successful completion of all steps, it sends this fedmsg indicating that
    Two Week release process has completed and fedora website atomic page
    should be updated with latest download links.
    """

    expected_title = "releng.atomic.twoweek.complete"
    expected_subti = "A new release of Fedora 28 Atomic Host is ready"
    expected_icon = "https://apps.fedoraproject.org/img/icons/atomic.png"
    expected_secondary_icon = "https://apps.fedoraproject.org/img/icons/atomic.png"
    expected_link = "https://download.fedoraproject.org/pub/alt/atomic/stable/"
    expected_objects = set([u'aarch64', u'x86_64', u'ppc64le'])

    msg = {
        u'timestamp': 1444939709.0,
        u'topic': u'org.fedoraproject.prod.releng.atomic.twoweek.complete',
        u'msg': {
            u'aarch64': {
                u'atomic_dvd_ostree': {
                    u'name': u'Fedora-AtomicHost-ostree-aarch64-28-20180515.1.iso',
                    u'image_name': u'Fedora-AtomicHost-ostree-aarch64-28-20180515.1.iso',
                    u'image_url': u'/pub/alt/atomic/stable/Fedora-Atomic-28-20180515.1/AtomicHost/'
                    'aarch64/iso/Fedora-AtomicHost-ostree-aarch64-28-20180515.1.iso',
                    u'release': u'28',
                    u'compose_id': u'Fedora-Atomic-28-20180515.1',
                    u'size': 988649472
                },
                u'atomic_qcow2': {
                    u'name': u'Fedora-AtomicHost-28-20180515.1',
                    u'image_name': u'Fedora-AtomicHost-28-20180515.1.aarch64.qcow2',
                    u'image_url': u'/pub/alt/atomic/stable/Fedora-Atomic-28-20180515.1/'
                    'AtomicHost/aarch64/images/Fedora-AtomicHost-28-20180515.1.aarch64.qcow2',
                    u'release': u'28',
                    u'compose_id': u'Fedora-Atomic-28-20180515.1',
                    u'size': 621911040
                },
                u'atomic_raw': {
                    u'name': u'Fedora-AtomicHost-28-20180515.1',
                    u'image_name': u'Fedora-AtomicHost-28-20180515.1.aarch64.raw.xz',
                    u'image_url': u'/pub/alt/atomic/stable/Fedora-Atomic-28-20180515.1/'
                    'AtomicHost/aarch64/images/Fedora-AtomicHost-28-20180515.1.aarch64.raw.xz',
                    u'release': u'28',
                    u'compose_id': u'Fedora-Atomic-28-20180515.1',
                    u'size': 396619232
                }
            },
            u'x86_64': {
                u'atomic_dvd_ostree': {
                    u'name': u'Fedora-AtomicHost-ostree-x86_64-28-20180515.1.iso',
                    u'image_name': u'Fedora-AtomicHost-ostree-x86_64-28-20180515.1.iso',
                    u'image_url': u'/pub/alt/atomic/stable/Fedora-Atomic-28-20180515.1/AtomicHost/'
                    'x86_64/iso/Fedora-AtomicHost-ostree-x86_64-28-20180515.1.iso',
                    u'release': u'28',
                    u'compose_id': u'Fedora-Atomic-28-20180515.1',
                    u'size': 1034944512
                },
                u'atomic_qcow2': {
                    u'name': u'Fedora-AtomicHost-28-20180515.1',
                    u'image_name': u'Fedora-AtomicHost-28-20180515.1.x86_64.qcow2',
                    u'image_url': u'/pub/alt/atomic/stable/Fedora-Atomic-28-20180515.1/'
                    'AtomicHost/x86_64/images/Fedora-AtomicHost-28-20180515.1.x86_64.qcow2',
                    u'release': u'28',
                    u'compose_id': u'Fedora-Atomic-28-20180515.1',
                    u'size': 635537920
                },
                u'atomic_raw': {
                    u'name': u'Fedora-AtomicHost-28-20180515.1',
                    u'image_name': u'Fedora-AtomicHost-28-20180515.1.x86_64.raw.xz',
                    u'image_url': u'/pub/alt/atomic/stable/Fedora-Atomic-28-20180515.1/'
                    'AtomicHost/x86_64/images/Fedora-AtomicHost-28-20180515.1.x86_64.raw.xz',
                    u'release': u'28',
                    u'compose_id': u'Fedora-Atomic-28-20180515.1',
                    u'size': 457994952
                },
                u'atomic_vagrant_libvirt': {
                    u'name': u'Fedora-AtomicHost-Vagrant-28-20180515.1',
                    u'image_name': u'Fedora-AtomicHost-Vagrant-28-20180515.1.x86_64.vagrant-libvirt.box',
                    u'image_url': u'/pub/alt/atomic/stable/Fedora-Atomic-28-20180515.1/AtomicHost/'
                    'x86_64/images/Fedora-AtomicHost-Vagrant-28-20180515.1.x86_64.vagrant-libvirt.box',
                    u'release': u'28',
                    u'compose_id': u'Fedora-Atomic-28-20180515.1',
                    u'size': 603786982
                },
                u'atomic_vagrant_virtualbox': {
                    u'name': u'Fedora-AtomicHost-Vagrant-28-20180515.1',
                    u'image_name': u'Fedora-AtomicHost-Vagrant-28-20180515.1.x86_64.vagrant-virtualbox.box',
                    u'image_url': u'/pub/alt/atomic/stable/Fedora-Atomic-28-20180515.1/AtomicHost/'
                    'x86_64/images/Fedora-AtomicHost-Vagrant-28-20180515.1.x86_64.vagrant-virtualbox.box',
                    u'release': u'28',
                    u'compose_id': u'Fedora-Atomic-28-20180515.1',
                    u'size': 617984000
                }
            },
            u'ppc64le': {
                u'atomic_dvd_ostree': {
                    u'name': u'Fedora-AtomicHost-ostree-ppc64le-28-20180515.1.iso',
                    u'image_name': u'Fedora-AtomicHost-ostree-ppc64le-28-20180515.1.iso',
                    u'image_url': u'/pub/alt/atomic/stable/Fedora-Atomic-28-20180515.1/AtomicHost/'
                    'ppc64le/iso/Fedora-AtomicHost-ostree-ppc64le-28-20180515.1.iso',
                    u'release': u'28',
                    u'compose_id': u'Fedora-Atomic-28-20180515.1',
                    u'size': 1036103680
                },
                u'atomic_qcow2': {
                    u'name': u'Fedora-AtomicHost-28-20180515.1',
                    u'image_name': u'Fedora-AtomicHost-28-20180515.1.ppc64le.qcow2',
                    u'image_url': u'/pub/alt/atomic/stable/Fedora-Atomic-28-20180515.1/AtomicHost/'
                    'ppc64le/images/Fedora-AtomicHost-28-20180515.1.ppc64le.qcow2',
                    u'release': u'28',
                    u'compose_id': u'Fedora-Atomic-28-20180515.1',
                    u'size': 636539904
                },
                u'atomic_raw': {
                    u'name': u'Fedora-AtomicHost-28-20180515.1',
                    u'image_name': u'Fedora-AtomicHost-28-20180515.1.ppc64le.raw.xz',
                    u'image_url': u'/pub/alt/atomic/stable/Fedora-Atomic-28-20180515.1/AtomicHost/'
                    'ppc64le/images/Fedora-AtomicHost-28-20180515.1.ppc64le.raw.xz',
                    u'release': u'28',
                    u'compose_id': u'Fedora-Atomic-28-20180515.1',
                    u'size': 411513572
                }
            }
        }
    }


class LegacyTestTwoWeekAtomicBegin(Base):
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


class LegacyTestTwoWeekAtomicComplete(Base):
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
