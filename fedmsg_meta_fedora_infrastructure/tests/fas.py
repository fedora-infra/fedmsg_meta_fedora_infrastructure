# This file is part of fedmsg.
# Copyright (C) 2012-2014 Red Hat, Inc.
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
""" Tests for fas messages. """

import unittest

from fedmsg_meta_fedora_infrastructure.tests.base import Base

from fedmsg_meta_fedora_infrastructure.tests.common import add_doc


class TestFASUserCreateLegacy(Base):
    """ Support old fas messages (the new ones look different).

    :mod:`fedmsg.meta` needs to be able to handle these since they are stored
    *forever* in datanommer.
    """
    expected_title = "fas.user.create"
    expected_subti = "New FAS account:  'ralph'  (created by 'ralph')"
    expected_icon = "https://admin.fedoraproject.org/accounts/static" + \
        "/theme/fas/images/account.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c" + \
        "?s=64&d=retro"
    expected_usernames = set(['ralph'])
    expected_objects = set(['users/ralph'])
    msg = {
        u'i': 1,
        u'timestamp': 1344432054.8098609,
        u'topic': u'org.fedoraproject.stg.fas.user.create',
        u'msg': {
            u'user': {
                u'username': u'ralph'
            },
            u'agent': {
                u'username': u'ralph'
            }
        }
    }


class TestFASUserCreate(Base):
    """ The `Fedora Account System <https://admin.fedoraproject.org/accounts>`_
    publishes messages on this topic whenever a new user account is created.
    """
    expected_title = "fas.user.create"
    expected_subti = "New FAS account:  'ralph'  (created by 'ralph')"
    expected_icon = "https://admin.fedoraproject.org/accounts/static" + \
        "/theme/fas/images/account.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c" + \
        "?s=64&d=retro"
    expected_usernames = set(['ralph'])
    expected_objects = set(['users/ralph'])
    msg = {
        u'i': 1,
        u'timestamp': 1344432054.8098609,
        u'topic': u'org.fedoraproject.stg.fas.user.create',
        u'msg': {
            u'user': u'ralph',
            u'agent': u'ralph',
        }
    }


class TestFASEditProfile(Base):
    """ The `Fedora Account System <https://admin.fedoraproject.org/accounts>`_
    publishes messages on this topic whenever a user's account is modified.
    Information about which account, what fields changed, and who did the
    changing are included in the message body.  For example:
    """
    expected_title = "fas.user.update"
    expected_subti = "ralph edited the following fields of ralph's " + \
        "FAS profile:  comments"
    expected_icon = "https://admin.fedoraproject.org/accounts/static" + \
        "/theme/fas/images/account.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c" + \
        "?s=64&d=retro"
    expected_usernames = set(['ralph'])
    expected_objects = set(['users/ralph'])
    msg = {
        u'topic': u'org.fedoraproject.stg.fas.user.update',
        u'msg': {
            u'fields': [u'comments'],
            u'user': u'ralph',
            u'agent': u'ralph',
        }
    }


class TestFASEditGroupLegacy(Base):
    """ Support old fas messages (the new ones look different).

    :mod:`fedmsg.meta` needs to be able to handle these since they are stored
    *forever* in datanommer.
    """
    expected_title = "fas.group.update"
    expected_subti = "ralph edited the following fields of the " + \
        "ambassadors FAS group:  display_name"
    expected_icon = "https://admin.fedoraproject.org/accounts/static" + \
        "/theme/fas/images/account.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c" + \
        "?s=64&d=retro"
    expected_usernames = set(['ralph'])
    expected_objects = set(['groups/ambassadors'])
    msg = {
        u'topic': u'org.fedoraproject.stg.fas.group.update',
        u'msg': {
            u'fields': [u'display_name'],
            u'group': {u'name': u'ambassadors'},
            u'agent': {u'username': u'ralph'},
        }
    }


class TestFASEditGroup(Base):
    """ The `Fedora Account System <https://admin.fedoraproject.org/accounts>`_
    publishes messages on this topic whenever a group's properties are
    modified.  For example:
    """
    expected_title = "fas.group.update"
    expected_subti = "ralph edited the following fields of the " + \
        "ambassadors FAS group:  display_name"
    expected_icon = "https://admin.fedoraproject.org/accounts/static" + \
        "/theme/fas/images/account.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c" + \
        "?s=64&d=retro"
    expected_usernames = set(['ralph'])
    expected_objects = set(['groups/ambassadors'])
    msg = {
        u'topic': u'org.fedoraproject.stg.fas.group.update',
        u'msg': {
            u'fields': [u'display_name'],
            u'group': u'ambassadors',
            u'agent': u'ralph',
        }
    }


class TestFASGroupCreate(Base):
    """ The `Fedora Account System <https://admin.fedoraproject.org/accounts>`_
    publishes messages on this topic whenever a new group is created.
    """
    expected_title = "fas.group.create"
    expected_subti = "ralph created new FAS group ambassadors"
    expected_icon = "https://admin.fedoraproject.org/accounts/static" + \
        "/theme/fas/images/account.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c" + \
        "?s=64&d=retro"
    expected_usernames = set(['ralph'])
    expected_objects = set(['groups/ambassadors'])
    msg = {
        u'topic': u'org.fedoraproject.stg.fas.group.create',
        u'msg': {
            u'group': u'ambassadors',
            u'agent': u'ralph',
        }
    }


class TestFASGroupCreateLegacy(Base):
    """ The `Fedora Account System <https://admin.fedoraproject.org/accounts>`_
    publishes messages on this topic whenever a new group is created.
    """
    expected_title = "fas.group.create"
    expected_subti = "ralph created new FAS group ambassadors"
    expected_icon = "https://admin.fedoraproject.org/accounts/static" + \
        "/theme/fas/images/account.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c" + \
        "?s=64&d=retro"
    expected_usernames = set(['ralph'])
    expected_objects = set(['groups/ambassadors'])
    msg = {
        u'topic': u'org.fedoraproject.stg.fas.group.create',
        u'msg': {
            u'group': {u'name': u'ambassadors'},
            u'agent': {u'username': u'ralph'},
        }
    }


class TestFASRoleUpdate(Base):
    """ The `Fedora Account System <https://admin.fedoraproject.org/accounts>`_
    publishes messages on this topic whenever a user's role in a particular
    group changes.
    """
    expected_title = "fas.role.update"
    expected_subti = "toshio changed ralph's role in the ambassadors group to sponsor"
    expected_icon = "https://admin.fedoraproject.org/accounts/static" + \
        "/theme/fas/images/account.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "085a38b9cf600926924645b292f0b7121a98a5165e559e0ad1882cfe33c6b395" + \
        "?s=64&d=retro"
    expected_usernames = set(['ralph', 'toshio'])
    expected_objects = set(['users/ralph', 'groups/ambassadors'])
    msg = {
        u'topic': u'org.fedoraproject.stg.fas.role.update',
        u'msg': {
            u'group': u'ambassadors',
            u'user': u'ralph',
            u'agent': u'toshio',
            u'status': u'sponsor',
        }
    }


class TestLegacyFASRoleUpdate(Base):
    """ The `Fedora Account System <https://admin.fedoraproject.org/accounts>`_
    publishes messages on this topic whenever a user's role in a particular
    group changes.
    This is a test whether or not we can still handle messages without status.
    """
    expected_title = "fas.role.update"
    expected_subti = "toshio changed ralph's role in the ambassadors group"
    expected_icon = "https://admin.fedoraproject.org/accounts/static" + \
        "/theme/fas/images/account.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "085a38b9cf600926924645b292f0b7121a98a5165e559e0ad1882cfe33c6b395" + \
        "?s=64&d=retro"
    expected_usernames = set(['ralph', 'toshio'])
    expected_objects = set(['users/ralph', 'groups/ambassadors'])
    msg = {
        u'topic': u'org.fedoraproject.stg.fas.role.update',
        u'msg': {
            u'group': {u'name': u'ambassadors'},
            u'user': {u'username': u'ralph'},
            u'agent': {u'username': u'toshio'},
        }
    }


class TestLegacy2FASGroupRemove(Base):
    """ The `Fedora Account System <https://admin.fedoraproject.org/accounts>`_
    publishes messages on this topic whenever a user is **removed** from a
    particular group.
    """
    expected_title = "fas.group.member.remove"
    expected_subti = "toshio removed ralph from the ambassadors group"
    expected_icon = "https://admin.fedoraproject.org/accounts/static" + \
        "/theme/fas/images/account.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "085a38b9cf600926924645b292f0b7121a98a5165e559e0ad1882cfe33c6b395" + \
        "?s=64&d=retro"
    expected_usernames = set(['ralph', 'toshio'])
    expected_objects = set(['users/ralph', 'groups/ambassadors'])
    msg = {
        u'topic': u'org.fedoraproject.stg.fas.group.member.remove',
        u'msg': {
            u'group': {u'name': u'ambassadors'},
            u'user': {u'username': u'ralph'},
            u'agent': {u'username': u'toshio'},
        }
    }


class TestLegacy2FASGroupSponsor(Base):
    """ The `Fedora Account System <https://admin.fedoraproject.org/accounts>`_
    publishes messages on this topic whenever a user's request to join a
    restricted group is **sponsored** by an authorized user.
    """
    expected_title = "fas.group.member.sponsor"
    expected_subti = "toshio sponsored ralph's membership " + \
        "in the ambassadors group"
    expected_icon = "https://admin.fedoraproject.org/accounts/static" + \
        "/theme/fas/images/account.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "085a38b9cf600926924645b292f0b7121a98a5165e559e0ad1882cfe33c6b395" + \
        "?s=64&d=retro"
    expected_usernames = set(['ralph', 'toshio'])
    expected_objects = set(['users/ralph', 'groups/ambassadors'])
    msg = {
        u'topic': u'org.fedoraproject.stg.fas.group.member.sponsor',
        u'msg': {
            u'group': {u'name': u'ambassadors'},
            u'user': {u'username': u'ralph'},
            u'agent': {u'username': u'toshio'},
        }
    }


class TestLegacy2FASGroupApply(Base):
    """ The `Fedora Account System <https://admin.fedoraproject.org/accounts>`_
    publishes messages on this topic whenever a user **requests to join** a
    particular group.
    """
    expected_title = "fas.group.member.apply"
    expected_subti = "ralph applied for ralph's membership " + \
        "in the ambassadors group"
    expected_icon = "https://admin.fedoraproject.org/accounts/static" + \
        "/theme/fas/images/account.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c" + \
        "?s=64&d=retro"
    expected_usernames = set(['ralph'])
    expected_objects = set(['users/ralph', 'groups/ambassadors'])
    msg = {
        u'topic': u'org.fedoraproject.stg.fas.group.member.apply',
        u'msg': {
            u'group': {u'name': u'ambassadors'},
            u'user': {u'username': u'ralph'},
            u'agent': {u'username': u'ralph'},
        }
    }

class TestFASGroupRemove(Base):
    """ The `Fedora Account System <https://admin.fedoraproject.org/accounts>`_
    publishes messages on this topic whenever a user is **removed** from a
    particular group.
    """
    expected_title = "fas.group.member.remove"
    expected_subti = "toshio removed ralph from the ambassadors group"
    expected_icon = "https://admin.fedoraproject.org/accounts/static" + \
        "/theme/fas/images/account.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "085a38b9cf600926924645b292f0b7121a98a5165e559e0ad1882cfe33c6b395" + \
        "?s=64&d=retro"
    expected_usernames = set(['ralph', 'toshio'])
    expected_objects = set(['users/ralph', 'groups/ambassadors'])
    msg = {
        u'topic': u'org.fedoraproject.stg.fas.group.member.remove',
        u'msg': {
            u'group': u'ambassadors',
            u'user':  u'ralph',
            u'agent': u'toshio',
        }
    }


class TestFASGroupSponsor(Base):
    """ The `Fedora Account System <https://admin.fedoraproject.org/accounts>`_
    publishes messages on this topic whenever a user's request to join a
    restricted group is **sponsored** by an authorized user.
    """
    expected_title = "fas.group.member.sponsor"
    expected_subti = "toshio sponsored ralph's membership " + \
        "in the ambassadors group"
    expected_icon = "https://admin.fedoraproject.org/accounts/static" + \
        "/theme/fas/images/account.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "085a38b9cf600926924645b292f0b7121a98a5165e559e0ad1882cfe33c6b395" + \
        "?s=64&d=retro"
    expected_usernames = set(['ralph', 'toshio'])
    expected_objects = set(['users/ralph', 'groups/ambassadors'])
    msg = {
        u'topic': u'org.fedoraproject.stg.fas.group.member.sponsor',
        u'msg': {
            u'group': u'ambassadors',
            u'user': u'ralph',
            u'agent': u'toshio',
        }
    }


class TestFASGroupApply(Base):
    """ The `Fedora Account System <https://admin.fedoraproject.org/accounts>`_
    publishes messages on this topic whenever a user **requests to join** a
    particular group.
    """
    expected_title = "fas.group.member.apply"
    expected_subti = "ralph applied for ralph's membership " + \
        "in the ambassadors group"
    expected_icon = "https://admin.fedoraproject.org/accounts/static" + \
        "/theme/fas/images/account.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c" + \
        "?s=64&d=retro"
    expected_usernames = set(['ralph'])
    expected_objects = set(['users/ralph', 'groups/ambassadors'])
    msg = {
        u'topic': u'org.fedoraproject.stg.fas.group.member.apply',
        u'msg': {
            u'group': u'ambassadors',
            u'user': u'ralph',
            u'agent': u'ralph',
        }
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
