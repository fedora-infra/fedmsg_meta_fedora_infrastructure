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
#
""" Tests for the-new-hotness messages """

import unittest

from fedmsg_meta_fedora_infrastructure.tests.base import Base

from common import add_doc


class TestHotnessBugFollowup(Base):
    """ These messages are published by a backend service called
    `the-new-hotness <https://github.com/fedora-infra/the-new-hotness>`_.
    It watches for new upstream release notifications from
    `release-monitoring.org <https://release-monitoring.org>`_ and in response
    it files bugs in `bugzilla <https://bugzilla.redhat.com>`_ and kicks off
    scratch builds in `koji <https://koji.fedoraproject.org/koji>`_.

    These kinds of messages get published when, after having filed a bug and
    kicked off a scratch build, the-new-hotness **notices that one of its
    scratch builds completes** and follows up on a ticket.
    """

    expected_title = "hotness.update.bug.followup"
    expected_subti = "scratch build of " + \
        "perl-Makefile-DOM-0.007-1.el7.src.rpm " + \
        "for RHBZ#1143475 completed"
    expected_link = "https://partner-bugzilla.redhat.com/show_bug.cgi?id=1143475"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = expected_icon
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set(['bugs/1143475'])
    msg = {
        "username": "fedmsg",
        "i": 5,
        "timestamp": 1416513240,
        "msg_id": "2014-c1fc1501-a043-4e5a-9a50-3076bb6d5089",
        "crypto": "x509",
        "topic": "org.fedoraproject.stg.hotness.update.bug.followup",
        "msg": {
            "trigger": {
                "username": "apache",
                "i": 1,
                "timestamp": 1416513251,
                "msg_id": "2014-786f6cfc-c76f-4cef-a791-6a6166861ab1",
                "crypto": "x509",
                "topic": "org.fedoraproject.stg.buildsys.task.state.change",
                "msg": {
                    "info": {
                        "parent": None,
                        "completion_time": None,
                        "start_time": "2014-11-20 19:54:11.737219",
                        "request": [
                            "cli-build/1416513248.864099.haYhDKay/"
                            "perl-Makefile-DOM-0.007-1.el7.src.rpm",
                            "rawhide",
                            { "scratch": True }
                        ],
                        "waiting": None,
                        "awaited": None,
                        "method": "build",
                        "priority": 50,
                        "channel_id": 1,
                        "state": 1,
                        "create_time": "2014-11-20 19:54:09.028052",
                        "id": 174,
                        "owner": 1127,
                        "host_id": 3,
                        "label": None,
                        "arch": "noarch",
                        "children": []
                    },
                    "old": "OPEN",
                    "attribute": "state",
                    "id": 174,
                    "instance": "primary",
                    "owner": "hotness",
                    "new": "CLOSED",
                    "srpm": "perl-Makefile-DOM-0.007-1.el7.src.rpm",
                    "method": "build"
                }
            },
            "bug": { "bug_id": 1143475 },
        }
    }


class TestHotnessBugFile(Base):
    """ These messages are published by a backend service called
    `the-new-hotness <https://github.com/fedora-infra/the-new-hotness>`_.
    It watches for new upstream release notifications from
    `release-monitoring.org <https://release-monitoring.org>`_ and in response
    it files bugs in `bugzilla <https://bugzilla.redhat.com>`_ and kicks off
    scratch builds in `koji <https://koji.fedoraproject.org/koji>`_.

    These kinds of messages get published when a **bug gets filed** notifying
    packager owners that they should update their packages in rawhide.
    """

    expected_title = "hotness.update.bug.file"
    expected_subti = "the-new-hotness filed a bug on perl-Makefile-DOM"
    expected_link = "https://bugzilla.redhat.com/show_bug.cgi?id=1143475"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = expected_icon
    expected_packages = set(['perl-Makefile-DOM'])
    expected_usernames = set([])
    expected_objects = set([
        'bugs/1143475',
        'projects/Makefile-DOM',
        'packages/perl-Makefile-DOM',
    ])
    msg = {
        "username": "fedmsg",
        "i": 5,
        "timestamp": 1416513240,
        "msg_id": "2014-c1fc1501-a043-4e5a-9a50-3076bb6d5089",
        "crypto": "x509",
        "topic": "org.fedoraproject.prod.hotness.update.bug.file",
        "msg": {
            "trigger": {
                "username": "ralph",
                "i": 1,
                "timestamp": 1416513232,
                "msg_id": "2014-7c19ff86-e6ef-4ccb-91b7-e836f33c7350",
                "crypto": "x509",
                "topic": "org.fedoraproject.stg.anitya.project.version.update",
                "msg": {
                    "project": {
                        "regex": None,
                        "name": "Makefile-DOM",
                        "created_on": 1412175050.0,
                        "version": "0.007",
                        "version_url": None,
                        "updated_on": 1416358331.0,
                        "homepage": "http://search.cpan.org/dist/"
                        "Makefile-DOM/",
                        "id": 3052,
                        "backend": "CPAN (perl)"
                    },
                    "message": {
                        "versions": [
                            "0.006",
                            "0.007"
                        ],
                        "old_version": "0.006",
                        "agent": "anitya",
                        "project": {
                            "regex": None,
                            "name": "Makefile-DOM",
                            "created_on": 1412175050.0,
                            "version": "0.007",
                            "version_url": None,
                            "updated_on": 1414068821.0,
                            "homepage": "http://search.cpan.org/dist/"
                            "Makefile-DOM/",
                            "id": 3052,
                            "backend": "CPAN (perl)"
                        },
                        "upstream_version": "0.007",
                        "packages": [
                            {
                                "package_name": "perl-Makefile-DOM",
                                "distro": "Fedora"
                            }
                        ]
                    },
                    "distro": None
                }
            },
            "bug": { "bug_id": 1143475 }
        }
    }


class TestHotnessDropAnitya(Base):
    """ These messages are published by a backend service called
    `the-new-hotness <https://github.com/fedora-infra/the-new-hotness>`_.
    It watches for new upstream release notifications from
    `release-monitoring.org <https://release-monitoring.org>`_ and in response
    it files bugs in `bugzilla <https://bugzilla.redhat.com>`_ and kicks off
    scratch builds in `koji <https://koji.fedoraproject.org/koji>`_.

    Sometimes, there is a new upstream release of something, but there is no
    explicit mapping in `release-monitoring.org
    <https://release-monitoring.org>`_ between that upstream project and a
    Fedora package.  In that event, no bugzilla bugs can be filed -- we don't
    know the **package name**.

    These kinds of messages get published when a new notification arrives, but
    **the upstream mapping for Fedora is absent** -- so the-new-hotness doesn't
    know what to do and just drops the event (but tells us about it via these
    messages).
    """

    expected_title = "hotness.update.drop"
    expected_subti = "the-new-hotness saw an update for apsw, but " + \
        "release-monitoring.org doesn't know what that project is called " + \
        "in Fedora land"
    expected_link = "https://release-monitoring.org/project/3772/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = expected_icon
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set(['projects/apsw'])
    msg = {
        "username": "fedmsg",
        "i": 2,
        "timestamp": 1416510033,
        "msg_id": "2014-187a78cc-83cf-476d-be91-2b8e6b0befbf",
        "crypto": "x509",
        "topic": "org.fedoraproject.stg.hotness.update.drop",
        "msg": {
            "reason": "anitya",
            "trigger": {
                "username": "anitya",
                "i": 1,
                "timestamp": 1416510031,
                "msg_id": "2014-86d41c9d-3ea0-4ee3-888b-ccf4e2544189",
                "crypto": "x509",
                "topic": "org.fedoraproject.stg.anitya.project.version.update",
                "msg": {
                    "project": {
                        "regex": None,
                        "name": "apsw",
                        "created_on": 1412175076.0,
                        "version": "3.8.7.1-r1",
                        "version_url": "rogerbinns/apsw",
                        "updated_on": 1416504528.0,
                        "homepage": "https://github.com/rogerbinns/apsw",
                        "id": 3772,
                        "backend": "Github"
                    },
                    "message": {
                        "versions": [
                            "3.8.7.1-r1"
                        ],
                        "old_version": "",
                        "agent": "anitya",
                        "project": {
                            "regex": None,
                            "name": "apsw",
                            "created_on": 1412175076.0,
                            "version": "3.8.7.1-r1",
                            "version_url": "rogerbinns/apsw",
                            "updated_on": 1416504528.0,
                            "homepage": "https://github.com/rogerbinns/apsw",
                            "id": 3772,
                            "backend": "Github"
                        },
                        "upstream_version": "3.8.7.1-r1",
                        "packages": []
                    },
                    "distro": None
                }
            }
        }
    }


class TestHotnessDropPkgdb(Base):
    """ These messages are published by a backend service called
    `the-new-hotness <https://github.com/fedora-infra/the-new-hotness>`_.
    It watches for new upstream release notifications from
    `release-monitoring.org <https://release-monitoring.org>`_ and in response
    it files bugs in `bugzilla <https://bugzilla.redhat.com>`_ and kicks off
    scratch builds in `koji <https://koji.fedoraproject.org/koji>`_.

    Before it tries to file a bugzilla ticket, it checks to see if the
    ``'monitor'`` setting is ``True`` for this package in the `Fedora PkgDB
    <https://admin.fedoraproject.org/pkgdb>`_.

    These kinds of messages get published when a new notification arrives, but
    **that monitor boolean was set to False for the given package** -- so
    the-new-hotness respects that and just drops the event (but tells us about
    it via these messages).
    """

    expected_title = "hotness.update.drop"
    expected_subti = "the-new-hotness saw an update for python-apsw, but " + \
        "pkgdb says the package owner is not interested in bugs being filed"
    expected_link = "https://release-monitoring.org/project/3772/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = expected_icon
    expected_packages = set(['python-apsw'])
    expected_usernames = set([])
    expected_objects = set(['projects/apsw', 'packages/python-apsw'])
    msg = {
        "username": "fedmsg",
        "i": 2,
        "timestamp": 1416510033,
        "msg_id": "2014-187a78cc-83cf-476d-be91-2b8e6b0befbf",
        "crypto": "x509",
        "topic": "org.fedoraproject.stg.hotness.update.drop",
        "msg": {
            "reason": "pkgdb",
            "trigger": {
                "username": "anitya",
                "i": 1,
                "timestamp": 1416510031,
                "msg_id": "2014-86d41c9d-3ea0-4ee3-888b-ccf4e2544189",
                "crypto": "x509",
                "topic": "org.fedoraproject.stg.anitya.project.version.update",
                "msg": {
                    "project": {
                        "regex": None,
                        "name": "apsw",
                        "created_on": 1412175076.0,
                        "version": "3.8.7.1-r1",
                        "version_url": "rogerbinns/apsw",
                        "updated_on": 1416504528.0,
                        "homepage": "https://github.com/rogerbinns/apsw",
                        "id": 3772,
                        "backend": "Github"
                    },
                    "message": {
                        "versions": [
                            "3.8.7.1-r1"
                        ],
                        "old_version": "",
                        "agent": "anitya",
                        "project": {
                            "regex": None,
                            "name": "apsw",
                            "created_on": 1412175076.0,
                            "version": "3.8.7.1-r1",
                            "version_url": "rogerbinns/apsw",
                            "updated_on": 1416504528.0,
                            "homepage": "https://github.com/rogerbinns/apsw",
                            "id": 3772,
                            "backend": "Github"
                        },
                        "upstream_version": "3.8.7.1-r1",
                        "packages": [
                            {
                                "package_name": "python-apsw",
                                "distro": "Fedora"
                            }
                        ]
                    },
                    "distro": None
                }
            }
        }
    }


class TestHotnessDropBugzilla(Base):
    """ These messages are published by a backend service called
    `the-new-hotness <https://github.com/fedora-infra/the-new-hotness>`_.
    It watches for new upstream release notifications from
    `release-monitoring.org <https://release-monitoring.org>`_ and in response
    it files bugs in `bugzilla <https://bugzilla.redhat.com>`_ and kicks off
    scratch builds in `koji <https://koji.fedoraproject.org/koji>`_.

    These kinds of messages get published when a new notification arrives, but
    **a bugzilla ticket has already been filed for that update** -- so
    the-new-hotness just drops the event (but tells us about it via these
    messages).
    """

    expected_title = "hotness.update.drop"
    expected_subti = "the-new-hotness saw an update for python-apsw, but " + \
        "a bugzilla ticket had already been filed"
    expected_link = "https://release-monitoring.org/project/3772/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = expected_icon
    expected_packages = set(['python-apsw'])
    expected_usernames = set([])
    expected_objects = set(['projects/apsw', 'packages/python-apsw'])
    msg = {
        "username": "fedmsg",
        "i": 2,
        "timestamp": 1416510033,
        "msg_id": "2014-187a78cc-83cf-476d-be91-2b8e6b0befbf",
        "crypto": "x509",
        "topic": "org.fedoraproject.stg.hotness.update.drop",
        "msg": {
            "reason": "bugzilla",
            "trigger": {
                "username": "anitya",
                "i": 1,
                "timestamp": 1416510031,
                "msg_id": "2014-86d41c9d-3ea0-4ee3-888b-ccf4e2544189",
                "crypto": "x509",
                "topic": "org.fedoraproject.stg.anitya.project.version.update",
                "msg": {
                    "project": {
                        "regex": None,
                        "name": "apsw",
                        "created_on": 1412175076.0,
                        "version": "3.8.7.1-r1",
                        "version_url": "rogerbinns/apsw",
                        "updated_on": 1416504528.0,
                        "homepage": "https://github.com/rogerbinns/apsw",
                        "id": 3772,
                        "backend": "Github"
                    },
                    "message": {
                        "versions": [
                            "3.8.7.1-r1"
                        ],
                        "old_version": "",
                        "agent": "anitya",
                        "project": {
                            "regex": None,
                            "name": "apsw",
                            "created_on": 1412175076.0,
                            "version": "3.8.7.1-r1",
                            "version_url": "rogerbinns/apsw",
                            "updated_on": 1416504528.0,
                            "homepage": "https://github.com/rogerbinns/apsw",
                            "id": 3772,
                            "backend": "Github"
                        },
                        "upstream_version": "3.8.7.1-r1",
                        "packages": [
                            {
                                "package_name": "python-apsw",
                                "distro": "Fedora"
                            }
                        ]
                    },
                    "distro": None
                }
            }
        }
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
