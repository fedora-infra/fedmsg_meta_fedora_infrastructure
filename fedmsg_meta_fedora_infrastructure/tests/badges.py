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

from .common import add_doc


class TestNewBadge(Base):
    """ These messages are published when `Open Badges
    <https://fedoraproject.org/wiki/Open_Badges>`_ are awarded to Fedora
    Contributors by the fedbadges backend.
    """

    expected_title = "fedbadges.badge.award"
    expected_subti = 'ralph has been awarded the ' + \
        '"Something on your mind" badge'
    expected_long_form = "You have commented on 2 or more bodhi updates."
    expected_link = "https://badges.fedoraproject.org/user/ralph"
    expected_icon = "http://example.com/image.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['something-on-your-mind'])
    msg = {
        u'i': 1,
        u'msg': {
            u'badge': {
                u'description': u'You have commented on 2 or more bodhi '
                'updates.',
                u'creator': u'ralph',
                u'discussion': u'http://github.com/fedora-infra/badges/'
                'pull/SOME_NUMBER',
                u'issuer_id': u'fedora-project',
                u'trigger': {
                    u'topic': u'org.fedoraproject.stg.bodhi.update.comment'
                },
                u'image_url': u'http://example.com/image.png',
                u'criteria': {
                    u'datanommer': {
                        u'filter': {
                            u'topics': [
                                u'{topic}'
                            ]
                        },
                        u'operation': u'count',
                        u'condition': {
                            u'greater than or equal to': 2
                        }
                    }
                },
                u'name': u'Something on your mind'
            },
            u'user': {
                u'badges_user_id': 1,
                u'username': u'ralph',
            }
        },
        u'topic': u'org.fedoraproject.stg.fedbadges.badge.award',
        u'username': u'fedmsg',
        u'timestamp': 1371498303.125771,
    }


class TestRankAdvance(Base):
    """ When a user's rank on the leaderboard of the `Fedora Badges
    <https://badges.fedoraproject.org>`_ system increases, this message gets
    published.
    """
    expected_title = "fedbadges.person.rank.advance"
    expected_subti = "ralph moved to position 1500 on the badges leaderboard"
    expected_link = "https://badges.fedoraproject.org/user/ralph"
    expected_icon = "https://apps.fedoraproject.org/img/icons/badges.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set([])
    msg = {
        "username": "fedmsg",
        "i": 4,
        "timestamp": 1377701575.214381,
        "topic": "org.fedoraproject.prod.fedbadges.person.rank.advance",
        "msg": {
            "old_rank": None,
            "person": {
                "website": None,
                "bio": None,
                "rank": 1500,
                "email": "ralph@fedoraproject.org",
                "nickname": "ralph",
                "id": 1600
            }
        }
    }


class TestFirstLogin(Base):
    """ When a user logs in to the `Fedora Badges
    <https://badges.fedoraproject.org>`_ site for the very first time, we
    publish a message like this one.
    """
    expected_title = "fedbadges.person.login.first"
    expected_subti = "ralph logged in to badges.fedoraproject.org " + \
        "for the first time"
    expected_link = "https://badges.fedoraproject.org/user/ralph"
    expected_icon = "https://apps.fedoraproject.org/img/icons/badges.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set([])
    msg = {
        "i": 2,
        "msg": {
            "user": {
                "badges_user_id": 2,
                "username": "ralph"
            }
        },
        "msg_id": "2013-be88d409-cdd7-47f0-9edd-87088f8505d2",
        "source_name": "datanommer",
        "source_version": "0.6.0",
        "timestamp": 1382804277.0,
        "topic": "org.fedoraproject.prod.fedbadges.person.login.first"
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
