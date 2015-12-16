# This file is part of fedmsg.
# Copyright (C) 2015 Red Hat, Inc.
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
""" Tests for coprs messages """

import unittest

from fedmsg.tests.test_meta import Base

from .common import add_doc


class TestLegacyNagiosHostStateChange(Base):
    expected_title = "nagios.host.state.change"
    expected_subti = "proxy04.fedoraproject.org is down"
    expected_icon = 'https://apps.fedoraproject.org/img/icons/nagios-logo.png'
    expected_secondary_icon = expected_icon
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set([
        'proxy04.fedoraproject.org/state',
    ])
    expected_link = "https://admin.fedoraproject.org/nagios/cgi-bin/" + \
        "status.cgi?navbarsearch=1&host=proxy04.fedoraproject.org"
    msg = {
        "i": 1,
        "timestamp": 1450127478.0,
        "msg_id": "2015-c29fd2e7-b4f3-4ac0-8eed-9aa2f6d0d675",
        "topic": "org.fedoraproject.prod.nagios.host.state.change",
        "msg": {
            "host": "proxy04.fedoraproject.org",
            "type": "PROBLEM",
            "state": "CRITICAL",
            "host_ack_author": "",
            "service_ack_author": "",
        }
    }


class TestLegacyNagiosServiceStateChange(Base):
    expected_title = "nagios.service.state.change"
    expected_subti = "some service is down on mm-frontend02.phx2.fedoraproject.org"
    expected_icon = 'https://apps.fedoraproject.org/img/icons/nagios-logo.png'
    expected_secondary_icon = expected_icon
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set([
        'mm-frontend02.phx2.fedoraproject.org/unknown',
    ])
    expected_link = "https://admin.fedoraproject.org/nagios/cgi-bin/" + \
        "status.cgi?navbarsearch=1&host=mm-frontend02.phx2.fedoraproject.org"
    msg = {
        "i": 1,
        "timestamp": 1450202769.0,
        "msg_id": "2015-071873c7-9635-48f4-bba3-1d97d87b0a76",
        "topic": "org.fedoraproject.prod.nagios.service.state.change",
        "msg": {
            "service_ack_author": "",
            "host": "mm-frontend02.phx2.fedoraproject.org",
            "type": "PROBLEM",
            "host_ack_author": "",
            "state": "CRITICAL"
        }
    }


class TestNagiosHostStateChange(Base):
    """ It might not be a good idea... but we hooked our `nagios instance
    <https://admin.fedoraproject.org/nagios>`_ because "open infrastructure".
    Note that, you shouldn't really rely on this stream for alerts about
    systems, because if you're expecting to get an alert about fedmsg being
    down, via fedmsg... well, it's just not going to work, friend.

    Here's an example message sent when a **host** changes state.
    """
    expected_title = "nagios.host.state.change"
    expected_subti = "proxy04.fedoraproject.org is down: \"ZOMG!\""
    expected_icon = 'https://apps.fedoraproject.org/img/icons/nagios-logo.png'
    expected_secondary_icon = expected_icon
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set([
        'proxy04.fedoraproject.org/state',
    ])
    expected_link = "https://admin.fedoraproject.org/nagios/cgi-bin/" + \
        "status.cgi?navbarsearch=1&host=proxy04.fedoraproject.org"
    msg = {
        "i": 1,
        "timestamp": 1450127478.0,
        "msg_id": "2015-c29fd2e7-b4f3-4ac0-8eed-9aa2f6d0d675",
        "topic": "org.fedoraproject.prod.nagios.host.state.change",
        "msg": {
            "host": "proxy04.fedoraproject.org",
            "type": "PROBLEM",
            "state": "CRITICAL",
            "output": "ZOMG!",
            "host_ack_author": "",
            "service_ack_author": "",
        }
    }


class TestNagiosServiceStateChange(Base):
    """ It might not be a good idea... but we hooked our `nagios instance
    <https://admin.fedoraproject.org/nagios>`_ because "open infrastructure".
    Note that, you shouldn't really rely on this stream for alerts about
    systems, because if you're expecting to get an alert about fedmsg being
    down, via fedmsg... well, it's just not going to work, friend.

    Here's an example message sent when a **service** changes state.
    """
    expected_title = "nagios.service.state.change"
    expected_subti = "mm-publiclist-internal is back up on " + \
        "mm-frontend02.phx2.fedoraproject.org: " + \
        "\"HTTP OK: HTTP/1.1 200 OK - 438 bytes " + \
        "in 0.536 second response time\""
    expected_icon = 'https://apps.fedoraproject.org/img/icons/nagios-logo.png'
    expected_secondary_icon = expected_icon
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set([
        'mm-frontend02.phx2.fedoraproject.org/mm-publiclist-internal',
    ])
    expected_link = "https://admin.fedoraproject.org/nagios/cgi-bin/" + \
        "status.cgi?navbarsearch=1&host=mm-frontend02.phx2.fedoraproject.org"
    msg = {
        "i": 1,
        "timestamp": 1450204405.0,
        "msg_id": "2015-6b240c0f-c946-40ea-b9d7-34237c3268fc",
        "topic": "org.fedoraproject.prod.nagios.service.state.change",
        "msg": {
            "service": "mm-publiclist-internal",
            "state": "OK",
            "host": "mm-frontend02.phx2.fedoraproject.org",
            "output": "HTTP OK: HTTP/1.1 200 OK - 438 bytes in 0.536 second response time",
            "type": "RECOVERY",
            "service_ack_author": "",
            "host_ack_author": ""
        }
    }


class TestNagiosServiceAck(Base):
    """ It might not be a good idea... but we hooked our `nagios instance
    <https://admin.fedoraproject.org/nagios>`_ because "open infrastructure".
    Note that, you shouldn't really rely on this stream for alerts about
    systems, because if you're expecting to get an alert about fedmsg being
    down, via fedmsg... well, it's just not going to work, friend.

    Here's an example message sent when an admin **acknowledges** a problem.
    """
    expected_title = "nagios.service.state.change"
    expected_subti = "kevin acknowledged that some service is having " + \
        "problems on packages03.phx2.fedoraproject.org"
    expected_icon = 'https://apps.fedoraproject.org/img/icons/nagios-logo.png'
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/' + \
        '1a7d8c43c8b89789a33a3266b0e20be7759a502ff38b74ff724a4db6aa33ede8' + \
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['kevin'])
    expected_objects = set([
        'packages03.phx2.fedoraproject.org/unknown',
    ])
    expected_link = "https://admin.fedoraproject.org/nagios/cgi-bin/" + \
        "status.cgi?navbarsearch=1&host=packages03.phx2.fedoraproject.org"
    msg = {
        "i": 1,
        "timestamp": 1450195509.0,
        "msg_id": "2015-e80ad530-8f35-473d-b90d-26b61de2f51d",
        "topic": "org.fedoraproject.prod.nagios.service.state.change",
        "msg": {
            "service_ack_author": "http://kevin.id.fedoraproject.org/",
            "host": "packages03.phx2.fedoraproject.org",
            "type": "ACKNOWLEDGEMENT",
            "host_ack_author": "",
            "state": "WARNING"
        }
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
