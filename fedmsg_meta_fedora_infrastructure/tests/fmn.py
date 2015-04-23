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
# Authors:  Ralph Bean <rbean@redhat.com>
""" Tests for messages from FMN """

import unittest

from fedmsg.tests.test_meta import Base

from .common import add_doc


class TestFilterUpdateRules(Base):
    """ Messages of this type are published whenever someone **updates
    one of their notification rules** in the `Fedora Notifications
    <https://apps.fedoraproject.org/notifications>`_ app.
    """
    expected_title = "fmn.filter.update"
    expected_subti = "ralph updated the rules on a fmn irc filter"
    expected_link = "https://apps.fedoraproject.org/notifications/"
    expected_icon = "https://apps.fedoraproject.org/img/icons/fedmsg.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c"
        "?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['ralph/irc/filter/rules'])
    msg = {
        "username": "apache",
        "i": 1,
        "timestamp": 1379638157.759283,
        "msg_id": "2013-96f9ca0e-c7c6-43f0-9de7-7a268c7f1cef",
        "topic": "org.fedoraproject.prod.fmn.filter.update",
        "msg": {
            'openid': 'ralph.id.fedoraproject.org',
            'context': 'irc',
            'changed': 'rules',
        }
    }


class TestPreferenceUpdateBatchValues(Base):
    """ Messages of this type are published whenever someone **updates
    their batch values** in the `Fedora Notifications
    <https://apps.fedoraproject.org/notifications>`_ app.

    Batch values are the parameters used to determine how to send notification
    digests like "how many messages should we accumulate before forwarding them
    to you" or "how many days should we wait before forwarding you a digest".
    """
    expected_title = "fmn.preference.update"
    expected_subti = "ralph updated their email digest options"
    expected_link = "https://apps.fedoraproject.org/notifications/"
    expected_icon = "https://apps.fedoraproject.org/img/icons/fedmsg.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c"
        "?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['ralph/email/preference/batch_values'])
    msg = {
        "username": "apache",
        "i": 1,
        "timestamp": 1379638157.759283,
        "msg_id": "2013-96f9ca0e-c7c6-43f0-9de7-7a268c7f1cef",
        "topic": "org.fedoraproject.prod.fmn.preference.update",
        "msg": {
            'openid': 'ralph.id.fedoraproject.org',
            'context': 'email',
            'changed': 'batch_values',
        }
    }


class TestPreferenceUpdateDetails(Base):
    """ Messages of this type are published whenever someone **updates
    their delivery details** in the `Fedora Notifications
    <https://apps.fedoraproject.org/notifications>`_ app.

    Delivery details are the values used to figure out how to deliver messages,
    like "email address" or "irc nick".
    """
    expected_title = "fmn.preference.update"
    expected_subti = "ralph updated their email delivery details"
    expected_link = "https://apps.fedoraproject.org/notifications/"
    expected_icon = "https://apps.fedoraproject.org/img/icons/fedmsg.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c"
        "?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['ralph/email/preference/details'])
    msg = {
        "username": "apache",
        "i": 1,
        "timestamp": 1379638157.759283,
        "msg_id": "2013-96f9ca0e-c7c6-43f0-9de7-7a268c7f1cef",
        "topic": "org.fedoraproject.prod.fmn.preference.update",
        "msg": {
            'openid': 'ralph.id.fedoraproject.org',
            'context': 'email',
            'changed': 'details',
        }
    }


class TestPreferenceUpdateEnabled(Base):
    """ Messages of this type are published whenever someone **toggles
    delivery of messages** in the `Fedora Notifications
    <https://apps.fedoraproject.org/notifications>`_ app.
    """
    expected_title = "fmn.preference.update"
    expected_subti = "ralph toggled their flow of android messages"
    expected_link = "https://apps.fedoraproject.org/notifications/"
    expected_icon = "https://apps.fedoraproject.org/img/icons/fedmsg.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c"
        "?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['ralph/android/preference/enabled'])
    msg = {
        "username": "apache",
        "i": 1,
        "timestamp": 1379638157.759283,
        "msg_id": "2013-96f9ca0e-c7c6-43f0-9de7-7a268c7f1cef",
        "topic": "org.fedoraproject.prod.fmn.preference.update",
        "msg": {
            'openid': 'ralph.id.fedoraproject.org',
            'context': 'android',
            'changed': 'enabled',
        }
    }


class TestPreferenceUpdateFilters(Base):
    """ Messages of this type are published whenever someone **toggles
    delivery of messages** in the `Fedora Notifications
    <https://apps.fedoraproject.org/notifications>`_ app.
    """
    expected_title = "fmn.preference.update"
    expected_subti = "ralph updated their irc filters"
    expected_link = "https://apps.fedoraproject.org/notifications/"
    expected_icon = "https://apps.fedoraproject.org/img/icons/fedmsg.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c"
        "?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['ralph/irc/preference/filters'])
    msg = {
        "username": "apache",
        "i": 1,
        "timestamp": 1379638157.759283,
        "msg_id": "2013-96f9ca0e-c7c6-43f0-9de7-7a268c7f1cef",
        "topic": "org.fedoraproject.prod.fmn.preference.update",
        "msg": {
            'openid': 'ralph.id.fedoraproject.org',
            'context': 'irc',
            'changed': 'filters',
        }
    }


class TestConfirmationUpdateValue(Base):
    """ Messages of this type are published whenever **a confirmation value
    changes** in the `Fedora Notifications
    <https://apps.fedoraproject.org/notifications>`_ app.
    """
    expected_title = "fmn.confirmation.update"
    expected_subti = "the value of one of ralph's pending " + \
        "confirmations changed"
    expected_link = "https://apps.fedoraproject.org/notifications/"
    expected_icon = "https://apps.fedoraproject.org/img/icons/fedmsg.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c"
        "?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['ralph/irc/confirmation/value'])
    msg = {
        "username": "apache",
        "i": 1,
        "timestamp": 1379638157.759283,
        "msg_id": "2013-96f9ca0e-c7c6-43f0-9de7-7a268c7f1cef",
        "topic": "org.fedoraproject.prod.fmn.confirmation.update",
        "msg": {
            'openid': 'ralph.id.fedoraproject.org',
            'context': 'irc',
            'changed': 'value',
        }
    }


class TestConfirmationUpdateStatus(Base):
    """ Messages of this type are published whenever **the status of a
    confirmation changes** in the `Fedora Notifications
    <https://apps.fedoraproject.org/notifications>`_ app.
    """
    expected_title = "fmn.confirmation.update"
    expected_subti = "the status of one of ralph's pending " + \
        "confirmations changed"
    expected_link = "https://apps.fedoraproject.org/notifications/"
    expected_icon = "https://apps.fedoraproject.org/img/icons/fedmsg.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c"
        "?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['ralph/irc/confirmation/status'])
    msg = {
        "username": "apache",
        "i": 1,
        "timestamp": 1379638157.759283,
        "msg_id": "2013-96f9ca0e-c7c6-43f0-9de7-7a268c7f1cef",
        "topic": "org.fedoraproject.prod.fmn.confirmation.update",
        "msg": {
            'openid': 'ralph.id.fedoraproject.org',
            'context': 'irc',
            'changed': 'status',
        }
    }

class TestRuleUpdate(Base):
    """ Messages of this type are published whenever **a rule
    is updated** in the `Fedora Notifications
    <https://apps.fedoraproject.org/notifications>`_ app.
    """
    expected_title = "fmn.rule.update"
    expected_subti = "raveit65 updated the filters on a fmn email rule"
    expected_link = "https://apps.fedoraproject.org/notifications/"
    expected_icon = "https://apps.fedoraproject.org/img/icons/fedmsg.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "15321e38b8a94a429e68a68a0f5029371b987c3aa7a0072326538b65ae54ec7e"
        "?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['raveit65'])
    expected_objects = set(['raveit65/email/rule/filters'])
    msg = {
        "i": 1, 
        "timestamp": 1427936259.0, 
        "msg_id": "2015-ca011930-b7ba-4355-a75d-079ffbe88fd2", 
        "topic": "org.fedoraproject.prod.fmn.rule.update", 
        "source_version": "0.6.5", 
        "msg": {
            "openid": "raveit65.id.fedoraproject.org", 
            "changed": "filters", 
            "context": "email"
        }
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
