# This file is part of fedmsg.
# Copyright (C) 2012 Red Hat, Inc.
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
""" Tests for pkgdb messages """

import unittest

from fedmsg.tests.test_meta import Base


class TestKojiBuildTag(Base):
    expected_title = "buildsys.tag (unsigned)"
    expected_subti = 'stage-4.1.1-3.fc18 tagged f18-updates-testing-pending'
    expected_link = "http://threebean.org/blog/test-post-6"
    expected_packages = set(['stage'])
    expected_usernames = set(['rmattes'])
    expected_objects = set(['builds/stage/4.1.1/3.fc18'])
    expected_link = "http://koji.fedoraproject.org/koji/" + \
        "buildinfo?buildID=342074"
    msg = {
        "username": "apache",
        "i": 1,
        "timestamp": 1359603469.2116399,
        "topic": "org.fedoraproject.prod.buildsys.tag",
        "msg": {
            "release": "3.fc18",
            "tag": "f18-updates-testing-pending",
            "name": "stage",
            "version": "4.1.1",
            "user": "bodhi"
        }
    }


if __name__ == '__main__':
    unittest.main()
