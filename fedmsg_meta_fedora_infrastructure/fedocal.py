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

import datetime
import dateutil.relativedelta

from fedmsg_meta_fedora_infrastructure import BaseProcessor

from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url


def _get_common_attrs(msg):
    try:
        user = msg['msg']['agent']
    except KeyError:
        user = None

    try:
        calendar = msg['msg']['calendar']['calendar_name']
    except KeyError:
        calendar = None

    try:
        meeting = msg['msg']['meeting']['meeting_name']
    except KeyError:
        meeting = None

    return user, calendar, meeting


def _casual_timedelta_string(meeting):
    """ Return a casual timedelta string.

    If a meeting starts in 2 hours, 15 minutes, and 32 seconds from now, then
    return just "in 2 hours".

    If a meeting starts in 7 minutes and 40 seconds from now, return just "in 7
    minutes".

    If a meeting starts 56 seconds from now, just return "right now".

    """

    now = datetime.datetime.utcnow()
    mdate = meeting['meeting_date']
    mtime = meeting['meeting_time_start']
    dt_string = "%s %s" % (mdate, mtime)
    meeting_dt = datetime.datetime.strptime(dt_string, "%Y-%m-%d %H:%M:%S")
    relative_td = dateutil.relativedelta.relativedelta(meeting_dt, now)

    denominations = ['years', 'months', 'days', 'hours', 'minutes']
    for denomination in denominations:
        value = getattr(relative_td, denomination)
        if value:
            # If the value is only one, then strip off the plural suffix.
            if value == 1:
                denomination = denomination[:-1]
            return "in %i %s" % (value, denomination)

    return "right now"


class FedocalProcessor(BaseProcessor):
    __name__ = "fedocal"
    __description__ = "The Fedora Calendaring System"
    __link__ = "https://apps.fedoraproject.org/calendar"
    __icon__ = "https://apps.fedoraproject.org/calendar/static/calendar.png"
    __docs__ = "https://github.com/fedora-infra/fedocal"
    __obj__ = "Calendar Events"

    def subtitle(self, msg, **config):
        user, calendar, meeting = _get_common_attrs(msg)
        timestring = None
        if 'fedocal.meeting.reminder' in msg['topic']:
            timestring = _casual_timedelta_string(msg['msg']['meeting'])
            tmpl = self._(
                'Friendly reminder!  The "{meeting}" meeting from '
                'the "{calendar}" calendar starts {timestring}')
        elif 'fedocal.meeting.update' in msg['topic']:
            tmpl = self._(
                '{user} updated the "{meeting}" meeting from '
                'the "{calendar}" calendar')
        elif 'fedocal.meeting.delete' in msg['topic']:
            tmpl = self._(
                '{user} deleted the "{meeting}" meeting from '
                'the "{calendar}" calendar')
        elif 'fedocal.meeting.new' in msg['topic']:
            tmpl = self._(
                '{user} created a "{meeting}" meeting in '
                'the "{calendar}" calendar')
        elif 'fedocal.calendar.new' in msg['topic']:
            tmpl = self._('{user} created a whole new "{calendar}" calendar')
        elif 'fedocal.calendar.update' in msg['topic']:
            tmpl = self._('{user} updated the "{calendar}" calendar')
        elif 'fedocal.calendar.delete' in msg['topic']:
            tmpl = self._('{user} deleted the "{calendar}" calendar')
        elif 'fedocal.calendar.clear' in msg['topic']:
            tmpl = self._(
                '{user} cleared the "{calendar}" calendar of all its meetings')
        elif 'fedocal.calendar.upload' in msg['topic']:
            tmpl = self._(
                '{user} uploaded an iCalendar file into the calendar '
                '"{calendar}"')
        else:
            tmpl = ""

        return tmpl.format(
            user=user,
            calendar=calendar,
            meeting=meeting,
            timestring=timestring,
        )

    def secondary_icon(self, msg, **config):
        try:
            user = msg['msg']['agent']
            return avatar_url(user)
        except KeyError:
            return None

    def link(self, msg, **config):
        base = "https://apps.fedoraproject.org/calendar/"
        try:
            meeting_id = msg['msg']['meeting']['meeting_id']
            return base + "meeting/%i/" % meeting_id
        except KeyError:
            return base + msg['msg']['calendar']['calendar_name'] + "/"

    def usernames(self, msg, **config):
        try:
            return set([msg['msg']['agent']])
        except KeyError:
            return set()

    def objects(self, msg, **config):
        user, calendar, meeting = _get_common_attrs(msg)
        action = msg['topic'].split('.')[-1]

        if not meeting:
            items = [calendar, action]
        else:
            items = [calendar, 'meetings', meeting, action]

        return set(['/'.join(items)])
