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
""" Tests for fedocal/calendar messages """

import unittest
import datetime

from fedmsg.tests.test_meta import Base


class TestCalendarCreate(Base):
    """ These messages are published when someone creates a whole calendar from
    `fedocal <https://apps.fedoraproject.org/calendar>`_.
    """

    expected_title = "fedocal.calendar.new"
    expected_subti = 'ralph created a whole new "awesome" calendar'
    expected_link = "https://apps.fedoraproject.org/calendar/awesome/"
    expected_icon = "https://apps.fedoraproject.org/calendar/" + \
        "static/calendar.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['awesome/new'])
    msg = {
        "username": "threebean",
        "i": 1,
        "timestamp": 1379638157.759283,
        "msg_id": "2013-96f9ca0e-c7c6-43f0-9de7-7a268c7f1cef",
        "topic": "org.fedoraproject.dev.fedocal.calendar.new",
        "msg": {
            "calendar": {
                "calendar_manager_group": "sysadmin-main",
                "calendar_name": "awesome",
                "calendar_regional_meetings": False,
                "calendar_multiple_meetings": False,
                "calendar_description": "cool deal",
                "calendar_admin_group": "sysadmin-badges",
                "calendar_contact": "ralph@fedoraproject.org"
            },
            "agent": "ralph"
        }
    }


class TestCalendarDelete(Base):
    """ These messages are published when someone deletes a whole calendar from
    `fedocal <https://apps.fedoraproject.org/calendar>`_.
    """

    expected_title = "fedocal.calendar.delete"
    expected_subti = 'ralph deleted the "awesome" calendar'
    expected_link = "https://apps.fedoraproject.org/calendar/awesome/"
    expected_icon = "https://apps.fedoraproject.org/calendar/" + \
        "static/calendar.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['awesome/delete'])
    msg = {
        "username": "threebean",
        "i": 1,
        "timestamp": 1379638157.759283,
        "msg_id": "2013-96f9ca0e-c7c6-43f0-9de7-7a268c7f1cef",
        "topic": "org.fedoraproject.dev.fedocal.calendar.delete",
        "msg": {
            "calendar": {
                "calendar_manager_group": "sysadmin-main",
                "calendar_name": "awesome",
                "calendar_regional_meetings": False,
                "calendar_multiple_meetings": False,
                "calendar_description": "cool deal",
                "calendar_admin_group": "sysadmin-badges",
                "calendar_contact": "ralph@fedoraproject.org"
            },
            "agent": "ralph"
        }
    }


class TestCalendarUpdate(Base):
    """ These messages are published when someone updates a whole calendar from
    `fedocal <https://apps.fedoraproject.org/calendar>`_.
    """

    expected_title = "fedocal.calendar.update"
    expected_subti = 'ralph updated the "awesome" calendar'
    expected_link = "https://apps.fedoraproject.org/calendar/awesome/"
    expected_icon = "https://apps.fedoraproject.org/calendar/" + \
        "static/calendar.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['awesome/update'])
    msg = {
        "username": "threebean",
        "i": 1,
        "timestamp": 1379638157.759283,
        "msg_id": "2013-96f9ca0e-c7c6-43f0-9de7-7a268c7f1cef",
        "topic": "org.fedoraproject.dev.fedocal.calendar.update",
        "msg": {
            "calendar": {
                "calendar_manager_group": "sysadmin-main",
                "calendar_name": "awesome",
                "calendar_regional_meetings": False,
                "calendar_multiple_meetings": False,
                "calendar_description": "cool deal",
                "calendar_admin_group": "sysadmin-badges",
                "calendar_contact": "ralph@fedoraproject.org"
            },
            "agent": "ralph"
        }
    }


class TestMeetingCreate(Base):
    """ These messages are published when someone creates a meeting from
    `fedocal <https://apps.fedoraproject.org/calendar>`_.
    """

    expected_title = "fedocal.meeting.new"
    expected_subti = 'ralph created a "wat" meeting in ' + \
        'the "awesome" calendar'
    expected_link = "https://apps.fedoraproject.org/calendar/meeting/42/"
    expected_icon = "https://apps.fedoraproject.org/calendar/" + \
        "static/calendar.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['awesome/meetings/wat/new'])
    msg = {
        "username": "threebean",
        "i": 1,
        "timestamp": 1379638613.767245,
        "msg_id": "2013-8d60e263-5c5f-40bb-86e0-241dc3965ba4",
        "topic": "org.fedoraproject.dev.fedocal.meeting.new",
        "msg": {
            "calendar": {
                "calendar_manager_group": "sysadmin-main",
                "calendar_name": "awesome",
                "calendar_regional_meetings": False,
                "calendar_multiple_meetings": False,
                "calendar_description": "cool deal",
                "calendar_admin_group": "sysadmin-badges",
                "calendar_contact": "ralph@fedoraproject.org"
            },
            "meeting": {
                "meeting_time_start": "12:00:00",
                "meeting_name": "wat",
                "meeting_id": 42,
                "meeting_time_stop": "12:00:00",
                "calendar_name": "awesome",
                "meeting_date_end": "2013-09-21",
                "meeting_manager": "ralph,",
                "meeting_date": "2013-09-20",
                "meeting_information": "awesome",
                "meeting_region": None
            },
            "agent": "ralph"
        }
    }


class TestMeetingUpdate(Base):
    """ These messages are published when someone updates a meeting from
    `fedocal <https://apps.fedoraproject.org/calendar>`_.
    """

    expected_title = "fedocal.meeting.update"
    expected_subti = 'ralph updated the "wat" meeting from ' + \
        'the "awesome" calendar'
    expected_link = "https://apps.fedoraproject.org/calendar/meeting/42/"
    expected_icon = "https://apps.fedoraproject.org/calendar/" + \
        "static/calendar.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['awesome/meetings/wat/update'])
    msg = {
        "username": "threebean",
        "i": 1,
        "timestamp": 1379638613.767245,
        "msg_id": "2013-8d60e263-5c5f-40bb-86e0-241dc3965ba4",
        "topic": "org.fedoraproject.dev.fedocal.meeting.update",
        "msg": {
            "calendar": {
                "calendar_manager_group": "sysadmin-main",
                "calendar_name": "awesome",
                "calendar_regional_meetings": False,
                "calendar_multiple_meetings": False,
                "calendar_description": "cool deal",
                "calendar_admin_group": "sysadmin-badges",
                "calendar_contact": "ralph@fedoraproject.org"
            },
            "meeting": {
                "meeting_time_start": "12:00:00",
                "meeting_name": "wat",
                "meeting_id": 42,
                "meeting_time_stop": "12:00:00",
                "calendar_name": "awesome",
                "meeting_date_end": "2013-09-21",
                "meeting_manager": "ralph,",
                "meeting_date": "2013-09-20",
                "meeting_information": "awesome",
                "meeting_region": None
            },
            "agent": "ralph"
        }
    }


class TestMeetingDelete(Base):
    """ These messages are published when someone deletes a meeting from
    `fedocal <https://apps.fedoraproject.org/calendar>`_.
    """

    expected_title = "fedocal.meeting.delete"
    expected_subti = 'ralph deleted the "wat" meeting from ' + \
        'the "awesome" calendar'
    expected_link = "https://apps.fedoraproject.org/calendar/meeting/42/"
    expected_icon = "https://apps.fedoraproject.org/calendar/" + \
        "static/calendar.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['awesome/meetings/wat/delete'])
    msg = {
        "username": "threebean",
        "i": 1,
        "timestamp": 1379638613.767245,
        "msg_id": "2013-8d60e263-5c5f-40bb-86e0-241dc3965ba4",
        "topic": "org.fedoraproject.dev.fedocal.meeting.delete",
        "msg": {
            "calendar": {
                "calendar_manager_group": "sysadmin-main",
                "calendar_name": "awesome",
                "calendar_regional_meetings": False,
                "calendar_multiple_meetings": False,
                "calendar_description": "cool deal",
                "calendar_admin_group": "sysadmin-badges",
                "calendar_contact": "ralph@fedoraproject.org"
            },
            "meeting": {
                "meeting_time_start": "12:00:00",
                "meeting_name": "wat",
                "meeting_id": 42,
                "meeting_time_stop": "12:00:00",
                "calendar_name": "awesome",
                "meeting_date_end": "2013-09-21",
                "meeting_manager": "ralph,",
                "meeting_date": "2013-09-20",
                "meeting_information": "awesome",
                "meeting_region": None
            },
            "agent": "ralph"
        }
    }


now = datetime.datetime.utcnow() + datetime.timedelta(hours=1)


class TestMeetingReminder(Base):
    """ These messages are published by a cronjob when time gets close to
    certain meetings scheduled in the `fedocal
    <https://apps.fedoraproject.org/calendar>`_ calendaring system.
    """

    expected_title = "fedocal.meeting.reminder"
    expected_subti = 'Friendly reminder!  The "wat" meeting from the ' + \
        '"awesome" calendar starts in 59 minutes'
    expected_link = "https://apps.fedoraproject.org/calendar/meeting/42/"
    expected_icon = "https://apps.fedoraproject.org/calendar/" + \
        "static/calendar.png"
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set(['awesome/meetings/wat/reminder'])
    msg = {
        "username": "threebean",
        "i": 1,
        "timestamp": 1379638613.767245,
        "msg_id": "2013-8d60e263-5c5f-40bb-86e0-241dc3965ba4",
        "topic": "org.fedoraproject.dev.fedocal.meeting.reminder",
        "msg": {
            "calendar": {
                "calendar_manager_group": "sysadmin-main",
                "calendar_name": "awesome",
                "calendar_regional_meetings": False,
                "calendar_multiple_meetings": False,
                "calendar_description": "cool deal",
                "calendar_admin_group": "sysadmin-badges",
                "calendar_contact": "ralph@fedoraproject.org"
            },
            "meeting": {
                "meeting_time_start": now.time().strftime("%H:%M:%S"),
                "meeting_name": "wat",
                "meeting_id": 42,
                "meeting_time_stop": "12:00:00",
                "calendar_name": "awesome",
                "meeting_date_end": "2013-09-21",
                "meeting_manager": "ralph,",
                "meeting_date": now.date().isoformat(),
                "meeting_information": "awesome",
                "meeting_region": None
            },
        }
    }


if __name__ == '__main__':
    unittest.main()
