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
# Authors: Michael Simacek <msimacek@redhat.com>
#
""" Tests for Koschei messages """

from fedmsg_meta_fedora_infrastructure.tests.base import Base

from .common import add_doc


class TestKoscheiPackageStateChange(Base):
    """ Koschei is a continuous integration system for RPM packages. It tracks
        dependency changes done in Koji repositories and rebuilds packages whose
        build dependencies change too much.

    This message type is published by Koschei when package's build or resolution
    state changes.
    """

    expected_title = "koschei.package.state.change"
    expected_subti = "rnv's builds started to fail in Fedora 22 (arm)"
    expected_link = 'https://apps.fedoraproject.org/koschei/package/rnv?collection=f22'
    expected_secondary_icon = \
        'https://apps.fedoraproject.org/packages/images/icons/rnv.png'
    expected_packages = set(['rnv'])

    msg = {
        "username": "msimacek",
        "i": 2,
        "timestamp": 1412260063,
        "msg_id": "2014-45d99116-f93e-45ef-8611-04fa2eabbb82",
        "topic": "org.fedoraproject.dev.koschei.package.state.change",
        "msg": {
            "name": "rnv",
            "old": "ok",
            "new": "failing",
            "koji_instance": "arm",
            "repo": "f22",
            "collection": "f22",
            "collection_name": "Fedora 22",
            "groups": ["c", "xml"]
        }
    }


class TestKoscheiCollectionStateChange(Base):
    """ Koschei is a continuous integration system for RPM packages. It tracks
        dependency changes done in Koji repositories and rebuilds packages whose
        build dependencies change too much.

    This message type is published by Koschei when collection resolution
    state changes.
    """

    expected_title = "koschei.collection.state.change"
    expected_subti = "Fedora 26 buildroot was broken"
    expected_link = 'https://apps.fedoraproject.org/koschei/collection/f26'

    msg = {
        "username": "msimacek",
        "i": 2,
        "timestamp": 1412260063,
        "msg_id": "2014-45d99116-f93e-45ef-8611-04fa2eabbb82",
        "topic": "org.fedoraproject.dev.koschei.collection.state.change",
        "msg": {
            "name": "rnv",
            "old": "ok",
            "new": "unresolved",
            "koji_instance": "primary",
            "collection": "f26",
            "collection_name": "Fedora 26"
        }
    }


add_doc(locals())
