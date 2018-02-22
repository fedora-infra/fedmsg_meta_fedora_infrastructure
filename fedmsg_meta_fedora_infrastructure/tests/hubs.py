# This file is part of fedmsg.
# Copyright (C) 2018 Red Hat, Inc.
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
# Authors:  Aurelien Bompard <abompard@fedoraproject.org>
#
""" Tests for Hubs messages. """

import unittest

from fedmsg_meta_fedora_infrastructure.tests.base import Base

from fedmsg_meta_fedora_infrastructure.tests.common import add_doc


HUBS_ICON = "https://hubs.fedoraproject.org/static/img/favicon.png"


class TestHubsUserCreated(Base):
    """
    `Fedora Hubs <https://hubs.fedoraproject.org>`_ publishes messages on
    this topic whenever a new user account is created.
    """
    expected_title = "hubs.user.created"
    expected_subti = "New Hubs user: ralph"
    expected_icon = HUBS_ICON
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c" + \
        "?s=64&d=retro"
    expected_usernames = set(['ralph'])
    expected_objects = set(['users/ralph'])
    expected_link = "https://hubs.fedoraproject.org/u/ralph/"
    msg = {
        u'i': 1,
        u'timestamp': 1344432054.8098609,
        u'topic': u'org.fedoraproject.stg.hubs.user.created',
        u'msg': {
            u'username': u'ralph',
        }
    }


class TestHubsUserRoleAdded(Base):
    """
    `Fedora Hubs <https://hubs.fedoraproject.org>`_ publishes messages on
    this topic whenever a user role is added.
    For example:
    """
    expected_title = "hubs.user.role.added"
    expected_subti = "ralph has joined hub infra as member"
    expected_icon = HUBS_ICON
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c" + \
        "?s=64&d=retro"
    expected_usernames = set(['ralph'])
    expected_objects = set(['users/ralph', 'hubs/infra'])
    expected_link = "https://hubs.fedoraproject.org/t/infra/"
    msg = {
        u'topic': u'org.fedoraproject.stg.hubs.user.role.added',
        u'msg': {
            u'username': u'ralph',
            u'hub_name': u'infra',
            u'hub_url': u"https://hubs.fedoraproject.org/t/infra/",
            u'role': u'member',
        }
    }


class TestHubsUserRoleChanged(Base):
    """
    `Fedora Hubs <https://hubs.fedoraproject.org>`_ publishes messages on
    this topic whenever a user role is modified.
    For example:
    """
    expected_title = "hubs.user.role.changed"
    expected_subti = "ralph's role on hub infra changed from member to owner"
    expected_icon = HUBS_ICON
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c" + \
        "?s=64&d=retro"
    expected_usernames = set(['ralph'])
    expected_objects = set(['users/ralph', 'hubs/infra'])
    expected_link = "https://hubs.fedoraproject.org/t/infra/"
    msg = {
        u'topic': u'org.fedoraproject.stg.hubs.user.role.changed',
        u'msg': {
            u'username': u'ralph',
            u'hub_name': u'infra',
            u'hub_url': u"https://hubs.fedoraproject.org/t/infra/",
            u'old_role': u'member',
            u'role': u'owner',
        }
    }


class TestHubsUserRoleRemoved(Base):
    """
    `Fedora Hubs <https://hubs.fedoraproject.org>`_ publishes messages on
    this topic whenever a user role is removed.
    For example:
    """
    expected_title = "hubs.user.role.removed"
    expected_subti = "ralph's role owner on hub infra was removed"
    expected_icon = HUBS_ICON
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c" + \
        "?s=64&d=retro"
    expected_usernames = set(['ralph'])
    expected_objects = set(['users/ralph', 'hubs/infra'])
    expected_link = "https://hubs.fedoraproject.org/t/infra/"
    msg = {
        u'topic': u'org.fedoraproject.stg.hubs.user.role.removed',
        u'msg': {
            u'username': u'ralph',
            u'hub_name': u'infra',
            u'hub_url': u"https://hubs.fedoraproject.org/t/infra/",
            u'role': u'owner',
        }
    }


class TestHubsHubCreated(Base):
    """
    `Fedora Hubs <https://hubs.fedoraproject.org>`_ publishes messages on
    this topic whenever a new hub is created.
    """
    expected_title = "hubs.hub.created"
    expected_subti = "New hub: infra"
    expected_icon = HUBS_ICON
    expected_secondary_icon = expected_icon
    expected_objects = set(['hubs/infra'])
    expected_link = "https://hubs.fedoraproject.org/t/infra/"
    msg = {
        u'i': 1,
        u'timestamp': 1344432054.8098609,
        u'topic': u'org.fedoraproject.stg.hubs.hub.created',
        u'msg': {
            u'hub_name': u'infra',
            u'hub_url': u"https://hubs.fedoraproject.org/t/infra/",
        }
    }


class TestHubsHubUpdated(Base):
    """
    `Fedora Hubs <https://hubs.fedoraproject.org>`_ publishes messages on
    this topic whenever a hub configuration is modified.
    """
    expected_title = "hubs.hub.updated"
    expected_subti = "Hub infra's configuration was changed"
    expected_icon = HUBS_ICON
    expected_secondary_icon = expected_icon
    expected_objects = set(['hubs/infra'])
    expected_link = "https://hubs.fedoraproject.org/t/infra/"
    msg = {
        u'i': 1,
        u'timestamp': 1344432054.8098609,
        u'topic': u'org.fedoraproject.stg.hubs.hub.updated',
        u'msg': {
            u'hub_name': u'infra',
            u'hub_url': u"https://hubs.fedoraproject.org/t/infra/",
        }
    }


class TestHubsWidgetUpdated(Base):
    """
    `Fedora Hubs <https://hubs.fedoraproject.org>`_ publishes messages on
    this topic whenever a widget configuration is modified.
    """
    expected_title = "hubs.widget.updated"
    expected_subti = "On hub infra, the configuration for widget " + \
        "\"Issues\" was changed"
    expected_icon = HUBS_ICON
    expected_secondary_icon = expected_icon
    expected_objects = set(['hubs/infra'])
    expected_link = "https://hubs.fedoraproject.org/t/infra/"
    msg = {
        u'i': 1,
        u'timestamp': 1344432054.8098609,
        u'topic': u'org.fedoraproject.stg.hubs.widget.updated',
        u'msg': {
            u'hub_name': u'infra',
            u'hub_url': u"https://hubs.fedoraproject.org/t/infra/",
            u'widget_label': u'Issues',
        }
    }


add_doc(locals())


if __name__ == '__main__':
    unittest.main()
