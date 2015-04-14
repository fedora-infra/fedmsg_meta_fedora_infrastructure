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
""" Tests for mirrormanager2 messages """

import unittest

from fedmsg_meta_fedora_infrastructure.tests.base import Base

from .common import add_doc


class TestCrawlerStart(Base):
    """ `Mirrormanager <https://mirrors.fedoraproject.org>`_ is the system that
    (surprise) manages the mirror network for Fedora (and others).  To
    accomplish this task, it does lots of things.

    One of those things is to regularly crawl the list of mirrors and determine
    who has up-to-date content and who has stale content. *This* message is one
    that gets published by its backend crawler when it **starts** its task.
    """

    expected_title = "mirrormanager.crawler.start"
    expected_subti = "mirrormanager's crawler started a crawl of 1 mirrors"
    expected_link = "https://mirrors.fedoraproject.org"
    expected_icon = "https://apps.fedoraproject.org/img/icons/downloads.png"
    expected_secondary_icon = expected_icon
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set(['mirrors/mirror.fpt-telecom.fpt.net'])

    msg = {
        "username": "apache",
        "i": 3,
        "timestamp": 1412327834,
        "msg_id": "2014-1f52337a-8dbe-48f1-baad-f2c770c60640",
        "crypto": "x509",
        "topic": "org.fedoraproject.prod.mirrormanager.crawler.start",
        "msg": {
            "hosts": [{
                "comment": "Mirror FPT Telecom",
                "name": "mirror.fpt-telecom.fpt.net",
                "internet2": True,
                "asn_clients": True,
                "country": "VN",
                "admin_active": True,
                "bandwidth_int": 1000,
                "site": {
                    "id": 1043,
                    "name": "mirror.fpt-telecom.fpt.net"
                },
                "private": False,
                "last_crawled": 1374957440.0,
                "internet2_clients": False,
                "id": 1432,
                "user_active": False,
                "last_checked_in": None,
                "last_crawl_duration": 9,
                "asn": None,
                "max_connections": 1
            }]
        }
    }


class TestCrawlerComplete(Base):
    """ `Mirrormanager <https://mirrors.fedoraproject.org>`_ is the system that
    (surprise) manages the mirror network for Fedora (and others).  To
    accomplish this task, it does lots of things.

    One of those things is to regularly crawl the list of mirrors and determine
    who has up-to-date content and who has stale content. *This* message is one
    that gets published by its backend crawler when it **completes** its task.
    """

    expected_title = "mirrormanager.crawler.complete"
    expected_subti = "mirrormanager's crawler finished a crawl of " + \
        "1 mirrors (1 succeeded, 0 failed)"
    expected_link = "https://mirrors.fedoraproject.org"
    expected_icon = "https://apps.fedoraproject.org/img/icons/downloads.png"
    expected_secondary_icon = expected_icon
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set(['mirrors/mirror.fpt-telecom.fpt.net'])

    msg = {
        "username": "apache",
        "i": 3,
        "timestamp": 1412327834,
        "msg_id": "2014-1f52337a-8dbe-48f1-baad-f2c770c60640",
        "crypto": "x509",
        "topic": "org.fedoraproject.prod.mirrormanager.crawler.complete",
        "msg": {
            "results": [{
                "rc": 0,
                "host": {
                    "comment": "Mirror FPT Telecom",
                    "name": "mirror.fpt-telecom.fpt.net",
                    "internet2": True,
                    "asn_clients": True,
                    "country": "VN",
                    "admin_active": True,
                    "bandwidth_int": 1000,
                    "site": {
                        "id": 1043,
                        "name": "mirror.fpt-telecom.fpt.net"
                    },
                    "private": False,
                    "last_crawled": 1374957440.0,
                    "internet2_clients": False,
                    "id": 1432,
                    "user_active": False,
                    "last_checked_in": None,
                    "last_crawl_duration": 9,
                    "asn": None,
                    "max_connections": 1
                },
            }]
        }
    }


class TestNetblocksSuccess(Base):
    """ `Mirrormanager <https://mirrors.fedoraproject.org>`_ is the system that
    (surprise) manages the mirror network for Fedora (and others).  To
    accomplish this task, it does lots of things.

    One of those things is to pull in mappings of ASN numbers from publicly
    accessible BGP tables.  It uses this information as part of a larger
    process to try and route clients to mirrors that are close to them.

    *This* message is one that gets published by a backend cronjob when it
    **successfully rebuilds one of its netblocks tables**.
    """

    expected_title = "mirrormanager.netblocks.get"
    expected_subti = "mirrormanager's backend successfully updated its " + \
        "global netblocks file"
    expected_link = "https://mirrors.fedoraproject.org"
    expected_icon = "https://apps.fedoraproject.org/img/icons/downloads.png"
    expected_secondary_icon = expected_icon
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set(['netblocks/global'])

    msg = {
        "username": "apache",
        "i": 3,
        "timestamp": 1412327834,
        "msg_id": "2014-1f52337a-8dbe-48f1-baad-f2c770c60640",
        "crypto": "x509",
        "topic": "org.fedoraproject.prod.mirrormanager.netblocks.get",
        "msg": {
            "type": "global",
            "success": True,
        }
    }


class TestNetblocksFailure(Base):
    """ `Mirrormanager <https://mirrors.fedoraproject.org>`_ is the system that
    (surprise) manages the mirror network for Fedora (and others).  To
    accomplish this task, it does lots of things.

    One of those things is to pull in mappings of ASN numbers from publicly
    accessible BGP tables.  It uses this information as part of a larger
    process to try and route clients to mirrors that are close to them.

    *This* message is one that gets published by a backend cronjob when it
    **fails to rebuild one of its netblocks tables**.
    """

    expected_title = "mirrormanager.netblocks.get"
    expected_subti = "mirrormanager's backend failed to update its " + \
        "internet2 netblocks file"
    expected_link = "https://mirrors.fedoraproject.org"
    expected_icon = "https://apps.fedoraproject.org/img/icons/downloads.png"
    expected_secondary_icon = expected_icon
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set(['netblocks/internet2'])

    msg = {
        "username": "apache",
        "i": 3,
        "timestamp": 1412327834,
        "msg_id": "2014-1f52337a-8dbe-48f1-baad-f2c770c60640",
        "crypto": "x509",
        "topic": "org.fedoraproject.prod.mirrormanager.netblocks.get",
        "msg": {
            "type": "internet2",
            "success": False,
        }
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
