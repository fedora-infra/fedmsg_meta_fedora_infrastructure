# This file is part of fedmsg.
# Copyright (C) 2017 Red Hat, Inc.
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
""" Tests for waiverdb messages """

import unittest

from fedmsg.tests.test_meta import Base

from .common import add_doc


class TestNewWaiver(Base):
    """ `WaiverDB
    <http://fedoraproject.org/wiki/Infrastructure/Factory2/Focus/WaiverDB>`_ is
    a service that allows humans to override test failures and influence gating
    decisions made by `Greenwave
    <http://fedoraproject.org/wiki/Infrastructure/Factory2/Focus/Greenwave>`_.

    It publishes messages like this whenever someone **records a new waiver**.
    """

    expected_title = "waiverdb.waiver.new"
    expected_subti = "ralph waived result 123 (fedora-26): \"This is fine.\""
    expected_link = (
        'https://waiverdb-web-waiverdb.app.os.fedoraproject.org/'
        'api/v1.0/waivers/8')
    expected_icon = 'https://apps.fedoraproject.org/img/icons/waiverdb.png'
    expected_secondary_icon = (
        'https://seccdn.libravatar.org/avatar/'
        '9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c'
        '?s=64&d=retro')
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    msg = {
        "username": "openshift",
        "i": 2,
        "timestamp": 1510020810.0,
        "msg_id": "2017-b173d0d1-a119-40e6-9e85-c6178468d9ff",
        "topic": "org.fedoraproject.stg.waiverdb.waiver.new",
        "headers": {},
        "msg": {
          "comment": "This is fine.",
          "username": "ralph",
          "waived": True,
          "timestamp": "2017-11-07T02:13:30.466388",
          "product_version": "fedora-26",
          "result_id": 123,
          "id": 8
        }
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
