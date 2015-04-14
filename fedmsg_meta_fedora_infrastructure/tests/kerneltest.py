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
""" Tests for kerneltest-harness messages """

import unittest

from fedmsg_meta_fedora_infrastructure.tests.base import Base

from .common import add_doc


class TestKerneltestNew(Base):
    """ As part of the `kernel testing initiative
    <https://fedoraproject.org/wiki/KernelTestingInitiative>`_, we built an
    `app <https://apps.fedoraproject.org/kerneltest>`_ that lets both real
    users and automated systems provide test feedback on new kernel builds and
    releases.

    *These* kinds of messages are published whenever either an automated system
    or a real user **uploads a new test result**.
    """
    expected_title = "kerneltest.upload.new"
    expected_subti = "jforbes ran a test of " + \
        "3.16.0-0.rc3.git3.1.fc21.x86_64 (PASS)"
    expected_link = "https://apps.fedoraproject.org/kerneltest/kernel/" + \
        "3.16.0-0.rc3.git3.1.fc21.x86_64"
    expected_icon = "https://apps.fedoraproject.org/img/icons/tux.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "03ead14065750aad5e4eb5ee42f7c60fb1e50ea2f5ba2dc9a89639bc381796da"
        "?s=64&d=retro")
    expected_packages = set(['kernel'])
    expected_usernames = set(['jforbes'])
    expected_objects = set([
        'kernel/3.16.0-0.rc3.git3.1.fc21.x86_64',
    ])
    msg = {
        u'username': u'apache',
        u'i': 1,
        u'timestamp': 1404746131,
        u'msg_id': u'2014-4c25f684-c965-4003-b22d-57cda0e2e12c',
        u'crypto': u'x509',
        u'topic': u'org.fedoraproject.prod.kerneltest.upload.new',
        u'msg': {
            u'test': {
                u'testset': u'default',
                u'authenticated': True,
                u'tester': u'jforbes',
                u'kernel_version': u'3.16.0-0.rc3.git3.1.fc21.x86_64',
                u'testdate': u'Mon Jul  7 11:15:23 EDT 2014',
                u'result': u'PASS',
                u'failed_tests': u'None',
                u'release': u'Fedora release 21 (Rawhide)',
                u'fedora_version': u'21',
                u'arch': u'x86_64',
            },
            u'agent': u'jforbes',
        }
    }


class TestKerneltestNewRelease(Base):
    """ As part of the `kernel testing initiative
    <https://fedoraproject.org/wiki/KernelTestingInitiative>`_, we built an
    `app <https://apps.fedoraproject.org/kerneltest>`_ that lets both real
    users and automated systems provide test feedback on new kernel builds and
    releases.

    *These* kinds of messages are published whenever an administrator sets up
    a new release for testing.
    """
    expected_title = "kerneltest.release.new"
    expected_subti = "jforbes added a new release for kerneltest: 21 TEST"
    expected_link = "https://apps.fedoraproject.org/kerneltest/stats"
    expected_icon = "https://apps.fedoraproject.org/img/icons/tux.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "03ead14065750aad5e4eb5ee42f7c60fb1e50ea2f5ba2dc9a89639bc381796da"
        "?s=64&d=retro")
    expected_packages = set(['kernel'])
    expected_usernames = set(['jforbes'])
    expected_objects = set([
        'release/21/TEST',
    ])
    msg = {
        u'username': u'apache',
        u'i': 1,
        u'timestamp': 1404746131,
        u'msg_id': u'2014-4c25f684-c965-4003-b22d-57cda0e2e12c',
        u'crypto': u'x509',
        u'topic': u'org.fedoraproject.prod.kerneltest.release.new',
        u'msg': {
            u'release': {
                u'releasenum': 21,
                u'support': 'TEST',
            },
            u'agent': u'jforbes',
        }
    }


class TestKerneltestEditRelease(Base):
    """ As part of the `kernel testing initiative
    <https://fedoraproject.org/wiki/KernelTestingInitiative>`_, we built an
    `app <https://apps.fedoraproject.org/kerneltest>`_ that lets both real
    users and automated systems provide test feedback on new kernel builds and
    releases.

    *These* kinds of messages are published whenever an administrator edits an
    existing release against which tests can be run.
    """
    expected_title = "kerneltest.release.edit"
    expected_subti = "jforbes edited the 21-TEST release for kerneltest"
    expected_link = "https://apps.fedoraproject.org/kerneltest/stats"
    expected_icon = "https://apps.fedoraproject.org/img/icons/tux.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "03ead14065750aad5e4eb5ee42f7c60fb1e50ea2f5ba2dc9a89639bc381796da"
        "?s=64&d=retro")
    expected_packages = set(['kernel'])
    expected_usernames = set(['jforbes'])
    expected_objects = set([
        'release/21/TEST',
    ])
    msg = {
        u'username': u'apache',
        u'i': 1,
        u'timestamp': 1404746131,
        u'msg_id': u'2014-4c25f684-c965-4003-b22d-57cda0e2e12c',
        u'crypto': u'x509',
        u'topic': u'org.fedoraproject.prod.kerneltest.release.edit',
        u'msg': {
            u'release': {
                u'releasenum': 21,
                u'support': 'TEST',
            },
            u'agent': u'jforbes',
        }
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
