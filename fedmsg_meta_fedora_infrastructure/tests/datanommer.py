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
""" Tests for that one datanommer message """

import unittest

from fedmsg.tests.test_meta import Base

from .common import add_doc


class TestDatanommerWat(Base):
    """ Generally speaking, the `datanommer
    <https://github.com/fedora-infra/datanommer>`_ consumer does not publish
    its own fedmsg messages.  There is one exception to this rule.

    As of fedmsg-0.7.0, every fedmsg carries its own uuid, prefixed with the
    year it was published.   There is a very low risk of creating a duplicate
    uuid.  To quote wikipedia::

        "The annual risk of someone being hit by a meteorite is estimated to be
        one chance in 17 billion, which means the probability is about
        ``0.00000000006 (6 * 10**-11)``, equivalent to the odds of creating a
        few tens of trillions of UUIDs in a year and having one duplicate"

    It is highly unlikely that datanommer will ever try to store a fedmsg
    message that carries a uuid that already exists in its database.  In the
    event that it does, it will publish the following message; a momentous
    occasion.
    """

    expected_title = "datanommer.wat"
    expected_subti = 'datanommer encountered a duplicate uuid'
    expected_link = "https://www.destroyallsoftware.com/talks/wat"
    expected_icon = "https://i.imgur.com/4g9NZu1.png"
    expected_secondary_icon = "https://i.imgur.com/58oJkOr.gif"
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set(['wat'])
    msg = {
        "username": "fedmsg",
        "i": 1,
        "timestamp": 1375753735.32427,
        "topic": "org.fedoraproject.prod.datanommer.wat",
        "msg": {
            "uuid": "2013-3bf0ec8f-03d3-40be-9ad5-5effdc6e4c06",
        }
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
