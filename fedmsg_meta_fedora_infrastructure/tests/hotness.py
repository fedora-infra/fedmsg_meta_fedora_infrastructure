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

from .common import add_doc


class TestHotnessBugFollowupScratchBuild(Base):
    """ These messages are published by a backend service called
    `the-new-hotness <https://github.com/fedora-infra/the-new-hotness>`_.
    It watches for new upstream release notifications from
    `release-monitoring.org <https://release-monitoring.org>`_ and in response
    it files bugs in `bugzilla <https://bugzilla.redhat.com>`_ and kicks off
    scratch builds in `koji <https://koji.fedoraproject.org/koji>`_.

    These kinds of messages get published in a couple different scenarios:

    - After having filed a bug and kicked off a scratch build, the-new-hotness
      **notices that one of its scratch builds completes** and follows up on a
      ticket.
    - After having filed a bug, the-new-hotness **notices that the package
      owner has completed a real build of the package** and follows up on a
      ticket.

    The message here is an example of the **first case** where the daemon
    notices **one of its own scratch builds**:
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
    expected_objects = set([
        'bugs/1143475',
    ])
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


class TestHotnessBugFollowupRealBuild(Base):
    """ These messages are published by a backend service called
    `the-new-hotness <https://github.com/fedora-infra/the-new-hotness>`_.
    It watches for new upstream release notifications from
    `release-monitoring.org <https://release-monitoring.org>`_ and in response
    it files bugs in `bugzilla <https://bugzilla.redhat.com>`_ and kicks off
    scratch builds in `koji <https://koji.fedoraproject.org/koji>`_.

    These kinds of messages get published in a couple different scenarios:

    - After having filed a bug and kicked off a scratch build, the-new-hotness
      **notices that one of its scratch builds completes** and follows up on a
      ticket.
    - After having filed a bug, the-new-hotness **notices that the package
      owner has completed a real build of the package** and follows up on a
      ticket.

    The message here is an example of the **second case**, where the daemon
    notices a **real build**:
    """

    expected_title = "hotness.update.bug.followup"
    expected_subti = "jmlich's real build of " + \
        "gd-2.1.1-1.fc22 for RHBZ#1144231 completed"
    expected_link = "https://partner-bugzilla.redhat.com/show_bug.cgi?id=1144231"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://apps.fedoraproject.org/packages" + \
        "/images/icons/gd.png"
    expected_packages = set(['gd'])
    expected_usernames = set(['jmlich'])
    expected_objects = set(['bugs/1144231'])
    msg = {
        u'username': u'fedmsg',
        u'msg_id': u'2015-f6b6e30c-bdf7-4200-8d53-7d9c54ce1749',
        u'topic': u'org.fedoraproject.stg.hotness.update.bug.followup',
        u'msg': {
            u'trigger': {
                u'username ': u'apache',
                u'msg_id': u'2015-a4653ee6-2ec7-42af-91a9-57c54ef9448c',
                u'topic': u'org.fedoraproject.prod.buildsys.build.state.change',
                u'msg': {
                    u'build_id': 603868,
                    u'old': 0,
                    u'name': u'gd',
                    u'task_id': 8615864,
                    u'attribute': u'state',
                    u'instance': u'primary',
                    u'version': u'2.1.1',
                    u'owner': u'jmlich',
                    u'new': 1,
                    u'release': u'1.fc22',
                },
            },
            u'bug': {u'bug_id': 1144231},
        },
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
    expected_secondary_icon = "https://apps.fedoraproject.org/packages" + \
        "/images/icons/perl-Makefile-DOM.png"
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
        "pkgdb says the maintainers are not interested in bugs being filed"
    expected_link = "https://release-monitoring.org/project/3772/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://apps.fedoraproject.org/packages" + \
        "/images/icons/python-apsw.png"
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
    expected_secondary_icon = "https://apps.fedoraproject.org/packages" + \
        "/images/icons/python-apsw.png"
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
                "topic": "org.release-monitoring.prod.anitya.project.version.update",
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


class TestHotnessMapFailAmbiguous(Base):
    """ These messages are published by a backend service called
    `the-new-hotness <https://github.com/fedora-infra/the-new-hotness>`_.
    It watches for new upstream release notifications from
    `release-monitoring.org <https://release-monitoring.org>`_ and in response
    it files bugs in `bugzilla <https://bugzilla.redhat.com>`_ and kicks off
    scratch builds in `koji <https://koji.fedoraproject.org/koji>`_.

    These kinds of messages get published when a new package gets added to
    Fedora and the-new-hotness **tries to add that package to
    release-monitoring.org**, but fails.
    """

    expected_title = "hotness.project.map"
    expected_subti = "hotness tried to map python-django-angular to an " + \
        "upstream project, but failed due to ambiguity.  3 other projects " + \
        "share the same homepage"
    expected_link = "https://bugzilla.redhat.com/1182533"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://apps.fedoraproject.org/packages" + \
        "/images/icons/python-django-angular.png"
    expected_packages = set(['python-django-angular'])
    expected_usernames = set([])
    expected_objects = set(['packages/python-django-angular'])
    msg = {
        'msg_id': '2015-30c4b30d-ca69-4c95-bad9-8e4c0b5d8fdb',
        'timestamp': 1421445401,
        'topic': u'org.fedoraproject.prod.hotness.project.map',
        'msg': {
            'success': False,
            'total': 3,
            'trigger': {
                u'msg_id': u'2015-b5cb92c6-9bdf-4807-ab29-2604ee93b407',
                u'timestamp': 1421445385,
                u'topic': u'org.fedoraproject.prod.pkgdb.package.new',
                u'msg': {
                    u'agent': u'limb',
                    u'package_listing': {
                        u'collection': {
                            u'branchname': u'master',
                            u'dist_tag': u'.fc22',
                            u'koji_name': u'rawhide',
                            u'name': u'Fedora',
                            u'status': u'Under Development',
                            u'version': u'devel'
                        },
                        u'critpath': False,
                        u'package': {
                            u'acls': [],
                            u'creation_date': 1421329015.0,
                            u'description': u'',
                            u'monitor': False,
                            u'name': u'python-django-angular',
                            u'review_url': u'https://bugzilla.redhat.com/'
                            '1182533',
                            u'status': u'Approved',
                            u'summary': u'Classes and utility functions to '
                            'integrate AngularJS with Django',
                            u'upstream_url': u'https://github.com/jrief/'
                            'django-angular',
                        },
                        u'point_of_contact': u'mrunge',
                        u'status': u'Approved',
                        u'status_change': 1421329016.0,
                    },
                    u'package_name': u'python-django-angular',
                },
            },
        },
    }


class TestHotnessMapMonitorToggle(Base):
    """ These messages are published by a backend service called
    `the-new-hotness <https://github.com/fedora-infra/the-new-hotness>`_.
    It watches for new upstream release notifications from
    `release-monitoring.org <https://release-monitoring.org>`_ and in response
    it files bugs in `bugzilla <https://bugzilla.redhat.com>`_ and kicks off
    scratch builds in `koji <https://koji.fedoraproject.org/koji>`_.

    These kinds of messages get published when a package has its monitoring
    flag toggled in pkgdb and the-new-hotness **tries to map that package in
    release-monitoring.org**, but fails.
    """

    expected_title = "hotness.project.map"
    expected_subti = "hotness tried to map perl-Digest-Perl-MD5 to an " + \
        "upstream project, but failed:  \"Could not determine backend for " + \
        "http://search.cpan.org/dist/Digest-Perl-MD5/\""
    expected_link = "http://search.cpan.org/dist/Digest-Perl-MD5/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://apps.fedoraproject.org/packages" + \
        "/images/icons/perl-Digest-Perl-MD5.png"
    expected_packages = set(['perl-Digest-Perl-MD5'])
    expected_usernames = set([])
    expected_objects = set(['packages/perl-Digest-Perl-MD5'])
    msg = {
        "i": 20,
        "msg": {
        "reason": "Could not determine backend for "
        "http://search.cpan.org/dist/Digest-Perl-MD5/",
        "success": False,
        "trigger": {
            "crypto": "x509",
            "i": 1,
            "msg": {
                "agent": "fale",
                "package": {
                    "acls": [],
                    "creation_date": 1400070978.0,
                    "description": "A pure-perl implementation of Ron "
                    "Rivest's MD5 Algorithm.",
                    "monitor": True,
                    "name": "perl-Digest-Perl-MD5",
                    "review_url": "https://bugzilla.redhat.com/732484",
                    "status": "Approved",
                    "summary": "Perl implementation of Ron "
                    "Rivest's MD5 Algorithm",
                    "upstream_url": "http://search.cpan.org/"
                    "dist/Digest-Perl-MD5/"},
                    "status": True
                },
                "msg_id": "2015-364c5f35-c5c8-4d25-a367-29f34cd5418e",
                "timestamp": 1427635611,
                "topic": "org.fedoraproject.prod.pkgdb.package.monitor.update",
                "username": "apache"
            }
        },
        "msg_id": "2015-122c5e1a-b1f4-4403-8703-7b12f07456c0",
        "timestamp": 1427635619.0,
        "topic": "org.fedoraproject.prod.hotness.project.map"
    }


class TestHotnessMapFailJustOne(Base):
    """ These messages are published by a backend service called
    `the-new-hotness <https://github.com/fedora-infra/the-new-hotness>`_.
    It watches for new upstream release notifications from
    `release-monitoring.org <https://release-monitoring.org>`_ and in response
    it files bugs in `bugzilla <https://bugzilla.redhat.com>`_ and kicks off
    scratch builds in `koji <https://koji.fedoraproject.org/koji>`_.

    These kinds of messages get published when a new package gets added to
    Fedora and the-new-hotness **tries to add that package to
    release-monitoring.org**, but fails.
    """

    expected_title = "hotness.project.map"
    expected_subti = "hotness tried to map python-django-angular to the " + \
        "pre-existing upstream project django-angular, " + \
        "but failed for unknown reasons"
    expected_link = "https://release-monitoring.org/project/5510/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://apps.fedoraproject.org/packages" + \
        "/images/icons/python-django-angular.png"
    expected_packages = set(['python-django-angular'])
    expected_usernames = set([])
    expected_objects = set([
        'projects/django-angular', 'packages/python-django-angular'])
    msg = {
        'msg_id': '2015-30c4b30d-ca69-4c95-bad9-8e4c0b5d8fdb',
        'timestamp': 1421445401,
        'topic': u'org.fedoraproject.prod.hotness.project.map',
        'msg': {
            'success': False,
            'project': {
                "backend": "PyPI",
                "created_on": 1421442402.0,
                "homepage": "https://pypi.python.org/pypi/django-angular",
                "id": 5510,
                "name": "django-angular",
                "regex": "",
                "updated_on": 1421442470.0,
                "version": "0.7.10",
                "version_url": "",
                "versions": [
                    "0.7.10"
                ]
            },
            'trigger': {
                u'msg_id': u'2015-b5cb92c6-9bdf-4807-ab29-2604ee93b407',
                u'timestamp': 1421445385,
                u'topic': u'org.fedoraproject.prod.pkgdb.package.new',
                u'msg': {
                    u'agent': u'limb',
                    u'package_listing': {
                        u'collection': {
                            u'branchname': u'master',
                            u'dist_tag': u'.fc22',
                            u'koji_name': u'rawhide',
                            u'name': u'Fedora',
                            u'status': u'Under Development',
                            u'version': u'devel'
                        },
                        u'critpath': False,
                        u'package': {
                            u'acls': [],
                            u'creation_date': 1421329015.0,
                            u'description': u'',
                            u'monitor': False,
                            u'name': u'python-django-angular',
                            u'review_url': u'https://bugzilla.redhat.com/'
                            '1182533',
                            u'status': u'Approved',
                            u'summary': u'Classes and utility functions to '
                            'integrate AngularJS with Django',
                            u'upstream_url': u'https://github.com/jrief/'
                            'django-angular',
                        },
                        u'point_of_contact': u'mrunge',
                        u'status': u'Approved',
                        u'status_change': 1421329016.0,
                    },
                    u'package_name': u'python-django-angular',
                },
            },
        },
    }


class TestHotnessMapSucceedJustOne(Base):
    """ These messages are published by a backend service called
    `the-new-hotness <https://github.com/fedora-infra/the-new-hotness>`_.
    It watches for new upstream release notifications from
    `release-monitoring.org <https://release-monitoring.org>`_ and in response
    it files bugs in `bugzilla <https://bugzilla.redhat.com>`_ and kicks off
    scratch builds in `koji <https://koji.fedoraproject.org/koji>`_.

    These kinds of messages get published when a new package gets added to
    Fedora and the-new-hotness **adds that package to
    release-monitoring.org**.
    """

    expected_title = "hotness.project.map"
    expected_subti = "hotness mapped python-django-angular to the " + \
        "pre-existing upstream project django-angular"
    expected_link = "https://release-monitoring.org/project/5510/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://apps.fedoraproject.org/packages" + \
        "/images/icons/python-django-angular.png"
    expected_packages = set(['python-django-angular'])
    expected_usernames = set([])
    expected_objects = set([
        'projects/django-angular', 'packages/python-django-angular'])
    msg = {
        'msg_id': '2015-30c4b30d-ca69-4c95-bad9-8e4c0b5d8fdb',
        'timestamp': 1421445401,
        'topic': u'org.fedoraproject.prod.hotness.project.map',
        'msg': {
            'success': True,
            'project': {
                "backend": "PyPI",
                "created_on": 1421442402.0,
                "homepage": "https://pypi.python.org/pypi/django-angular",
                "id": 5510,
                "name": "django-angular",
                "regex": "",
                "updated_on": 1421442470.0,
                "version": "0.7.10",
                "version_url": "",
                "versions": [
                    "0.7.10"
                ]
            },
            'trigger': {
                u'msg_id': u'2015-b5cb92c6-9bdf-4807-ab29-2604ee93b407',
                u'timestamp': 1421445385,
                u'topic': u'org.fedoraproject.prod.pkgdb.package.new',
                u'msg': {
                    u'agent': u'limb',
                    u'package_listing': {
                        u'collection': {
                            u'branchname': u'master',
                            u'dist_tag': u'.fc22',
                            u'koji_name': u'rawhide',
                            u'name': u'Fedora',
                            u'status': u'Under Development',
                            u'version': u'devel'
                        },
                        u'critpath': False,
                        u'package': {
                            u'acls': [],
                            u'creation_date': 1421329015.0,
                            u'description': u'',
                            u'monitor': False,
                            u'name': u'python-django-angular',
                            u'review_url': u'https://bugzilla.redhat.com/'
                            '1182533',
                            u'status': u'Approved',
                            u'summary': u'Classes and utility functions to '
                            'integrate AngularJS with Django',
                            u'upstream_url': u'https://github.com/jrief/'
                            'django-angular',
                        },
                        u'point_of_contact': u'mrunge',
                        u'status': u'Approved',
                        u'status_change': 1421329016.0,
                    },
                    u'package_name': u'python-django-angular',
                },
            },
        },
    }


class TestHotnessMapSucceedBrandNew(Base):
    """ These messages are published by a backend service called
    `the-new-hotness <https://github.com/fedora-infra/the-new-hotness>`_.
    It watches for new upstream release notifications from
    `release-monitoring.org <https://release-monitoring.org>`_ and in response
    it files bugs in `bugzilla <https://bugzilla.redhat.com>`_ and kicks off
    scratch builds in `koji <https://koji.fedoraproject.org/koji>`_.

    These kinds of messages get published when a new package gets added to
    Fedora and the-new-hotness **adds that package to
    release-monitoring.org**.
    """

    expected_title = "hotness.project.map"
    expected_subti = "hotness mapped python-django-angular to a " + \
        "brand-new upstream project"
    expected_link = u'https://bugzilla.redhat.com/1182533'
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://apps.fedoraproject.org/packages" + \
        "/images/icons/python-django-angular.png"
    expected_packages = set(['python-django-angular'])
    expected_usernames = set([])
    expected_objects = set(['packages/python-django-angular'])
    msg = {
        'msg_id': '2015-30c4b30d-ca69-4c95-bad9-8e4c0b5d8fdb',
        'timestamp': 1421445401,
        'topic': u'org.fedoraproject.prod.hotness.project.map',
        'msg': {
            'success': True,
            'trigger': {
                u'msg_id': u'2015-b5cb92c6-9bdf-4807-ab29-2604ee93b407',
                u'timestamp': 1421445385,
                u'topic': u'org.fedoraproject.prod.pkgdb.package.new',
                u'msg': {
                    u'agent': u'limb',
                    u'package_listing': {
                        u'collection': {
                            u'branchname': u'master',
                            u'dist_tag': u'.fc22',
                            u'koji_name': u'rawhide',
                            u'name': u'Fedora',
                            u'status': u'Under Development',
                            u'version': u'devel'
                        },
                        u'critpath': False,
                        u'package': {
                            u'acls': [],
                            u'creation_date': 1421329015.0,
                            u'description': u'',
                            u'monitor': False,
                            u'name': u'python-django-angular',
                            u'review_url': u'https://bugzilla.redhat.com/'
                            '1182533',
                            u'status': u'Approved',
                            u'summary': u'Classes and utility functions to '
                            'integrate AngularJS with Django',
                            u'upstream_url': u'https://github.com/jrief/'
                            'django-angular',
                        },
                        u'point_of_contact': u'mrunge',
                        u'status': u'Approved',
                        u'status_change': 1421329016.0,
                    },
                    u'package_name': u'python-django-angular',
                },
            },
        },
    }


class TestHotnessMapFailBrandNew(Base):
    """ These messages are published by a backend service called
    `the-new-hotness <https://github.com/fedora-infra/the-new-hotness>`_.
    It watches for new upstream release notifications from
    `release-monitoring.org <https://release-monitoring.org>`_ and in response
    it files bugs in `bugzilla <https://bugzilla.redhat.com>`_ and kicks off
    scratch builds in `koji <https://koji.fedoraproject.org/koji>`_.

    These kinds of messages get published when a new package gets added to
    Fedora and the-new-hotness **tries to add that package to
    release-monitoring.org** but fails for unknown reasons.
    """

    expected_title = "hotness.project.map"
    expected_subti = "hotness tried to map python-django-angular to a " + \
        "brand-new upstream project, but failed for unknown reasons"
    expected_link = u'https://bugzilla.redhat.com/1182533'
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://apps.fedoraproject.org/packages" + \
        "/images/icons/python-django-angular.png"
    expected_packages = set(['python-django-angular'])
    expected_usernames = set([])
    expected_objects = set(['packages/python-django-angular'])
    msg = {
        'msg_id': '2015-30c4b30d-ca69-4c95-bad9-8e4c0b5d8fdb',
        'timestamp': 1421445401,
        'topic': u'org.fedoraproject.prod.hotness.project.map',
        'msg': {
            'success': False,
            'trigger': {
                u'msg_id': u'2015-b5cb92c6-9bdf-4807-ab29-2604ee93b407',
                u'timestamp': 1421445385,
                u'topic': u'org.fedoraproject.prod.pkgdb.package.new',
                u'msg': {
                    u'agent': u'limb',
                    u'package_listing': {
                        u'collection': {
                            u'branchname': u'master',
                            u'dist_tag': u'.fc22',
                            u'koji_name': u'rawhide',
                            u'name': u'Fedora',
                            u'status': u'Under Development',
                            u'version': u'devel'
                        },
                        u'critpath': False,
                        u'package': {
                            u'acls': [],
                            u'creation_date': 1421329015.0,
                            u'description': u'',
                            u'monitor': False,
                            u'name': u'python-django-angular',
                            u'review_url': u'https://bugzilla.redhat.com/'
                            '1182533',
                            u'status': u'Approved',
                            u'summary': u'Classes and utility functions to '
                            'integrate AngularJS with Django',
                            u'upstream_url': u'https://github.com/jrief/'
                            'django-angular',
                        },
                        u'point_of_contact': u'mrunge',
                        u'status': u'Approved',
                        u'status_change': 1421329016.0,
                    },
                    u'package_name': u'python-django-angular',
                },
            },
        },
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
