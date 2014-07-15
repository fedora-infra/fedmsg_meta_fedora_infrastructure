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
""" Tests for coprs messages """

import unittest

from fedmsg.tests.test_meta import Base

from common import add_doc


class TestCoprsBuildStart(Base):
    """ `Copr <https://fedorahosted.org/copr/>`_ publishes these messages
    when a new build starts.
    """
    expected_title = "copr.build.start"
    expected_subti = ("fatka started a new build of the mutt-kz copr")
    expected_icon = 'https://apps.fedoraproject.org/img/icons/copr.png'
    expected_secondary_icon = (
        'https://seccdn.libravatar.org/avatar/'
        'b9d974c03597da48d9c3b11d4423bf30c6e0c01c23bcd3a192167a95f7c506bc?'
        's=64&d=retro')
    expected_packages = set([])
    expected_usernames = set(['fatka'])
    expected_objects = set([
        'coprs/mutt-kz/build.start',
    ])
    expected_link = (
        "https://copr.fedoraproject.org/coprs/fatka/mutt-kz/")
    msg = {
        u'username': u'copr',
        u'i': 1,
        u'timestamp': 1383956077.2320001,
        u'msg_id': u'2013-675e7b1e-9b7f-4d11-be2f-2b3845817d60',
        u'topic': u'org.fedoraproject.prod.copr.build.start',
        u'msg': {
            u'what': u'build start: user:fatka copr:mutt-kz '
            'build:100 ip:172.16.3.3  pid:12010',
            u'ip': u'172.16.3.3',
            u'who': u'worker-2',
            u'pid': 12010,
            u'copr': u'mutt-kz',
            u'build': 100,
            u'user': u'fatka',
        },
    }


class TestCoprsBuildEnd(Base):
    """ `Copr <https://fedorahosted.org/copr/>`_ publishes these messages
    when a build has completed.
    """
    expected_title = "copr.build.end"
    expected_subti = (
        "fatka's mutt-kz copr build finished fedora-20-x86_64 with 'success'")
    expected_secondary_icon = (
        'https://seccdn.libravatar.org/avatar/'
        'b9d974c03597da48d9c3b11d4423bf30c6e0c01c23bcd3a192167a95f7c506bc?'
        's=64&d=retro')
    expected_packages = set([])
    expected_usernames = set(['fatka'])
    expected_objects = set([
        'coprs/mutt-kz/build.end',
    ])
    expected_link = (
        "https://copr.fedoraproject.org/coprs/fatka/mutt-kz/")
    msg = {
        u'username': u'copr',
        u'i': 4,
        u'timestamp': 1383956707.6340001,
        u'msg_id': u'2013-b05a323d-37ee-4396-9635-7b5dfaf5441b',
        u'topic': u'org.fedoraproject.prod.copr.build.end',
        u'msg': {
            u'status': 1,
            u'chroot': u'fedora-20-x86_64',
            u'what': u'build end: user:fatka copr:mutt-kz build:100 '
            'ip:172.16.3.3  pid:12010 status:1',
            u'ip': u'172.16.3.3',
            u'who': u'worker-2',
            u'pid': 12010,
            u'copr': u'mutt-kz',
            u'build': 100,
            u'user': u'fatka',
        },
    }


class TestCoprsChrootStart(Base):
    """ `Copr <https://fedorahosted.org/copr/>`_ publishes these messages
    when a copr start a new chroot.
    """
    expected_title = "copr.chroot.start"
    expected_subti = (
        "fatka's mutt-kz copr started a new fedora-20-x86_64 chroot")
    expected_secondary_icon = (
        'https://seccdn.libravatar.org/avatar/'
        'b9d974c03597da48d9c3b11d4423bf30c6e0c01c23bcd3a192167a95f7c506bc?'
        's=64&d=retro')
    expected_packages = set([])
    expected_usernames = set(['fatka'])
    expected_objects = set([
        'coprs/mutt-kz/chroot.start/fedora-20-x86_64',
    ])
    expected_link = (
        "https://copr-be.cloud.fedoraproject.org/results/"
        "fatka/mutt-kz/fedora-20-x86_64/")
    msg = {
        u'username': u'copr',
        u'i': 3,
        u'timestamp': 1383956378.4679999,
        u'msg_id': u'2013-833cca09-2dba-42ad-9863-4f6c3c29a30d',
        u'topic': u'org.fedoraproject.prod.copr.chroot.start',
        u'msg': {
            u'what': u'chroot start: chroot:fedora-20-x86_64 user:fatka '
            'copr:mutt-kz build:100 ip:172.16.3.3  pid:12010',
            u'chroot': u'fedora-20-x86_64',
            u'ip': u'172.16.3.3',
            u'who': u'worker-2',
            u'pid': 12010,
            u'copr': u'mutt-kz',
            u'build': 100,
            u'user': u'fatka',
        },
    }


class TestCoprsWorkerCreate(Base):
    """ `Copr <https://fedorahosted.org/copr/>`_ publishes these messages
    when a new worker is spun up.
    """
    expected_title = "copr.worker.create"
    expected_subti = "a new worker was created"
    expected_link = "https://copr.fedoraproject.org"
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set([
        'coprs/worker.create',
    ])
    msg = {
        u'username': u'copr',
        u'i': 1,
        u'timestamp': 1383956077.2320001,
        u'msg_id': u'2013-675e7b1e-9b7f-4d11-be2f-2b3845817d60',
        u'topic': u'org.fedoraproject.prod.copr.worker.create',
        u'msg': {
            u'what': u'creating worker: 172.16.3.3',
            u'ip': u'172.16.3.3',
        },
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
