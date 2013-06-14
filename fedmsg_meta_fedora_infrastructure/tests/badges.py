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
""" Tests for badges messages """

import unittest

from fedmsg.tests.test_meta import Base


class TestNewBadge(Base):
    """ These messages are published when `Open Badges
    <https://fedoraproject.org/wiki/Open_Badges>`_ are awarded to Fedora
    Contributors by the fedbadges backend.
    """

    expected_title = "fedbadges.badge.award (unsigned)"
    expected_subti = 'ralph has been awarded the ' + \
        '"Something on your Mind?" badge'
    expected_link = "https://apps.fedoraproject.org/badges/users/ralph"
    expected_secondary_icon = "http://example.com/image.png"
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['something-on-your-mind'])

    msg = {
        "i": 1,
        "msg": {
            "username": "ralph",
            "badge_id": "something-on-your-mind",
            "badge_name": "Something on your Mind?",
            "badge_image": "http://example.com/image.png",
        },
        "topic": "org.fedoraproject.stg.fedbadges.badge.award",
        "username": "fedmsg",
        "timestamp": 1371185561.01757
    }


if __name__ == '__main__':
    unittest.main()
