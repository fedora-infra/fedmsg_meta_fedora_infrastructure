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

    expected_title = "fedbadges.badge.award"
    expected_subti = 'ralph has been awarded the ' + \
        '"Something on your mind" badge'
    expected_link = "https://badges.fedoraproject.org/user/ralph"
    expected_icon = "http://example.com/image.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
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


if __name__ == '__main__':
    unittest.main()
