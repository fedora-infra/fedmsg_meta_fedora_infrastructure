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

from .common import add_doc


_long_copr_end = """Package:  mutt-kz-1.5.23.1-1.20150203.git.c8504a8a.fc21
COPR:     fatka/mutt-kz
Built by: fatka
Status:   success
ID:       00000100

Logs:
  Build:     https://copr-be.cloud.fedoraproject.org/results/fatka/mutt-kz/fedora-20-x86_64/00000100-mutt-kz/build.log.gz
  Root:      https://copr-be.cloud.fedoraproject.org/results/fatka/mutt-kz/fedora-20-x86_64/00000100-mutt-kz/root.log.gz
  Copr:      https://copr-be.cloud.fedoraproject.org/results/fatka/mutt-kz/fedora-20-x86_64/build-00000100.log
  Mockchain: https://copr-be.cloud.fedoraproject.org/results/fatka/mutt-kz/fedora-20-x86_64/00000100-mutt-kz/mockchain.log.gz
Results:     https://copr-be.cloud.fedoraproject.org/results/fatka/mutt-kz/fedora-20-x86_64/00000100-mutt-kz/
Repodata:    https://copr-be.cloud.fedoraproject.org/results/fatka/mutt-kz/fedora-20-x86_64/repodata/
"""


_long_copr_end_broken = """Package:  mutt-kz-1.5.23.1
COPR:     fatka/mutt-kz
Built by: fatka
Status:   success
ID:       00000100

Logs:
  Build:     https://copr-be.cloud.fedoraproject.org/results/fatka/mutt-kz/fedora-20-x86_64/00000100-?? WHO KNOWS ??/build.log.gz
  Root:      https://copr-be.cloud.fedoraproject.org/results/fatka/mutt-kz/fedora-20-x86_64/00000100-?? WHO KNOWS ??/root.log.gz
  Copr:      https://copr-be.cloud.fedoraproject.org/results/fatka/mutt-kz/fedora-20-x86_64/build-00000100.log
  Mockchain: https://copr-be.cloud.fedoraproject.org/results/fatka/mutt-kz/fedora-20-x86_64/00000100-?? WHO KNOWS ??/mockchain.log.gz
Results:     https://copr-be.cloud.fedoraproject.org/results/fatka/mutt-kz/fedora-20-x86_64/00000100-?? WHO KNOWS ??/
Repodata:    https://copr-be.cloud.fedoraproject.org/results/fatka/mutt-kz/fedora-20-x86_64/repodata/
"""


_long_copr_end_fail = """Package:  glib2-2.42.2-1.01.fc21
COPR:     brianjmurrell/glib2
Built by: brianjmurrell
Status:   failed
ID:       00080794

Logs:
  Build:     https://copr-be.cloud.fedoraproject.org/results/brianjmurrell/glib2/fedora-21-x86_64/00080794-glib2/build.log.gz
  Root:      https://copr-be.cloud.fedoraproject.org/results/brianjmurrell/glib2/fedora-21-x86_64/00080794-glib2/root.log.gz
  Copr:      https://copr-be.cloud.fedoraproject.org/results/brianjmurrell/glib2/fedora-21-x86_64/build-00080794.log
  Mockchain: https://copr-be.cloud.fedoraproject.org/results/brianjmurrell/glib2/fedora-21-x86_64/00080794-glib2/mockchain.log.gz
Results:     https://copr-be.cloud.fedoraproject.org/results/brianjmurrell/glib2/fedora-21-x86_64/00080794-glib2/
Repodata:    https://copr-be.cloud.fedoraproject.org/results/brianjmurrell/glib2/fedora-21-x86_64/repodata/
"""


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
        "https://copr.fedoraproject.org/coprs/fatka/mutt-kz/build/100/")
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
    when a build has completed.  This is an example of a build that **completed
    successfully**.
    """
    expected_title = "copr.build.end"
    expected_subti = (
        "fatka's mutt-kz copr build of "
        "mutt-kz-1.5.23.1-1.20150203.git.c8504a8a.fc21 "
        "for fedora-20-x86_64 finished with 'success'")
    expected_long_form = _long_copr_end
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
        "https://copr.fedoraproject.org/coprs/fatka/mutt-kz/build/100/")
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
            u'version': '1.5.23.1-1.20150203.git.c8504a8a.fc21',
            u'pkg': 'mutt-kz-1.5.23.1-1.20150203.git.c8504a8a.fc21',
            u'build': 100,
            u'user': u'fatka',
        },
    }


class TestCoprsBuildEndBrokenNOVR(Base):
    """ `Copr <https://fedorahosted.org/copr/>`_ publishes these messages
    when a build has completed.  This is an example of a build that **completed
    successfully**.
    """
    expected_title = "copr.build.end"
    expected_subti = (
        "fatka's mutt-kz copr build of "
        "mutt-kz-1.5.23.1 "
        "for fedora-20-x86_64 finished with 'success'")
    expected_long_form = _long_copr_end_broken
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
        "https://copr.fedoraproject.org/coprs/fatka/mutt-kz/build/100/")
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
            u'version': '1.5.23.1',
            u'pkg': 'mutt-kz',
            u'build': 100,
            u'user': u'fatka',
        },
    }


class TestCoprsBuildFailure(Base):
    """ `Copr <https://fedorahosted.org/copr/>`_ publishes these messages
    when a build has completed.  This is an example of a build that **failed**.
    """
    expected_title = "copr.build.end"
    expected_subti = (
        "brianjmurrell's glib2 copr build of "
        "glib2-2.42.2-1.01.fc21 "
        "for fedora-21-x86_64 finished with 'failed'")
    expected_long_form = _long_copr_end_fail
    expected_secondary_icon = (
        'https://seccdn.libravatar.org/avatar/'
        '7de251444538e68ddf2e83d67749c5f09583ae7b3fd638df3490c7e672c148d8?'
        's=64&d=retro')
    expected_packages = set([])
    expected_usernames = set(['brianjmurrell'])
    expected_objects = set([
        'coprs/glib2/build.end',
    ])
    expected_link = ("https://copr.fedoraproject.org/coprs/"
                     "brianjmurrell/glib2/build/80794/")

    msg = {
        "timestamp": 1425653769.0,
        "msg_id": "2015-f3152f3c-5075-422e-af94-96c692454c81",
        "topic": "org.fedoraproject.prod.copr.build.end",
        "msg": {
            "status": 0,
            "what": "build end: user:brianjmurrell copr:glib2 build:80794    "
            "pkg: glib2-2.42.2-1.01.fc21    version: 2.42.2-1.01.fc21 "
            "ip:172.16.3.5    pid:9363 status:0",
            "chroot": "fedora-21-x86_64",
            "ip": "172.16.3.5",
            "user": "brianjmurrell",
            "who": "worker-4",
            "pid": 9363,
            "copr": "glib2",
            "version": "2.42.2-1.01.fc21",
            "build": 80794,
            "owner": "brianjmurrell",
            "pkg": "glib2",
        }
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


class TestCoprsGroupLink(Base):
    """ `Copr <https://fedorahosted.org/copr/>`_ publishes these messages
    when a build has completed.  This is an example of a group repo.
    """
    expected_title = "copr.build.end"
    expected_subti = (
        "churchyard's python26 copr build of python26-2.6.9-1.fc26 for "
        "fedora-23-i386 finished with 'failed'")
    expected_link = ("https://copr.fedoraproject.org/coprs/"
                     "g/python/python26/build/450811/")

    msg = {
        u'source_name': u'datanommer',
        u'i': 3,
        u'timestamp': 1473355790.0,
        u'msg_id': u'2016-31e1e282-c176-4a9e-94bc-e4ae34536d47',
        u'topic': u'org.fedoraproject.prod.copr.build.end',
        u'source_version': u'0.6.5',
        u'msg': {
            u'status': 0,
            u'what': u'build end: user:churchyard copr:python26 build:450811'
            '  pkg: python26  version: 2.6.9-1.fc26 ip:172.25.83.110'
            '  pid:7513 status:0',
            u'chroot': u'fedora-23-i386',
            u'ip': u'172.25.83.110',
            u'user': u'churchyard',
            u'who': u'backend.worker-6023-PC',
            u'pid': 7513,
            u'copr': u'python26',
            u'version': u'2.6.9-1.fc26',
            u'build': 450811,
            u'owner': u'@python',
            u'pkg': u'python26',
        },
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
