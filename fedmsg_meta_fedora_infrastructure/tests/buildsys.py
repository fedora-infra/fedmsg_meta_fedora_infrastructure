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
""" Tests for pkgdb messages """

import unittest

from fedmsg.tests.test_meta import Base


class TestKojiBuildTag(Base):
    expected_title = "buildsys.tag (unsigned)"
    expected_subti = 'stage-4.1.1-3.fc18 tagged f18-updates-testing-pending'
    expected_icon = "http://fedoraproject.org/w/uploads/2/20/" + \
        "Artwork_DesignService_koji-icon-48.png"
    expected_packages = set(['stage'])
    expected_objects = set(['builds/stage/4.1.1/3.fc18'])
    #expected_link = "http://koji.fedoraproject.org/koji/" + \
    #    "buildinfo?buildID=342074"
    msg = {
        "username": "apache",
        "i": 1,
        "timestamp": 1359603469.2116399,
        "topic": "org.fedoraproject.prod.buildsys.tag",
        "msg": {
            "release": "3.fc18",
            "tag": "f18-updates-testing-pending",
            "name": "stage",
            "version": "4.1.1",
            "user": "bodhi"
        }
    }

class TestKojiBuildUnTag(Base):
    expected_title = "buildsys.untag (unsigned)"
    expected_subti = 'globus-gram-job-manager-sge-1.5-2.fc16 untagged from f16-updates-pending'
    expected_icon = "http://fedoraproject.org/w/uploads/2/20/" + \
        "Artwork_DesignService_koji-icon-48.png"
    expected_packages = set(['globus-gram-job-manager-sge'])
    expected_objects = set(['builds/globus-gram-job-manager-sge/1.5/2.fc16'])
    #expected_link = "http://koji.fedoraproject.org/koji/" + \
    #    "buildinfo?buildID=342074"
    msg = {
        "username": "apache",
        "i": 85,
        "timestamp": 1359655345.774982,
        "topic": "org.fedoraproject.prod.buildsys.untag",
        "msg": {
            "release": "2.fc16",
            "tag": "f16-updates-pending",
            "name": "globus-gram-job-manager-sge",
            "version": "1.5",
            "user": "bodhi"
        }
    }

class TestKojiBuildStateChangeStart(Base):
    expected_title = "buildsys.build.state.change (unsigned)"
    expected_subti = 'eclipse-ptp-6.0.3-1.fc19 started building'
    expected_icon = "http://fedoraproject.org/w/uploads/2/20/" + \
        "Artwork_DesignService_koji-icon-48.png"
    expected_packages = set(['eclipse-ptp'])
    expected_objects = set(['builds/eclipse-ptp/6.0.3/1.fc19'])
    #expected_link = "http://koji.fedoraproject.org/koji/" + \
    #    "buildinfo?buildID=342074"
    msg = {
        "username": "apache",
        "i": 1,
        "timestamp": 1359604772.1788671,
        "topic": "org.fedoraproject.prod.buildsys.build.state.change",
        "msg": {
            "old": 3,
            "name": "eclipse-ptp",
            "attribute": "state",
            "version": "6.0.3",
            "release": "1.fc19",
            "new": 0
        }
    }


class TestKojiBuildStateChangeFail(Base):
    expected_title = "buildsys.build.state.change (unsigned)"
    expected_subti = 'eclipse-ptp-6.0.3-1.fc19 failed to build'
    expected_icon = "http://fedoraproject.org/w/uploads/2/20/" + \
        "Artwork_DesignService_koji-icon-48.png"
    expected_packages = set(['eclipse-ptp'])
    #expected_usernames = set(['rmattes'])
    expected_objects = set(['builds/eclipse-ptp/6.0.3/1.fc19'])
    #expected_link = "http://koji.fedoraproject.org/koji/" + \
    #    "buildinfo?buildID=342074"
    msg = {
        "username": "apache",
        "i": 1,
        "timestamp": 1359604772.1788671,
        "topic": "org.fedoraproject.prod.buildsys.build.state.change",
        "msg": {
            "old": 0,
            "name": "eclipse-ptp",
            "attribute": "state",
            "version": "6.0.3",
            "release": "1.fc19",
            "new": 3
        }
    }


class TestKojiRepoInit(Base):
    expected_title = "buildsys.repo.init (unsigned)"
    expected_subti = 'Repo initialized:  f19-build'
    expected_icon = "http://fedoraproject.org/w/uploads/2/20/" + \
        "Artwork_DesignService_koji-icon-48.png"
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set(['repos/f19-build'])
    msg = {
        "username": "apache",
        "i": 2,
        "timestamp": 1359655886.353586,
        "topic": "org.fedoraproject.prod.buildsys.repo.init",
        "msg": {
            "tag": "f19-build"
        }
    }


class TestKojiRepoDone(Base):
    expected_title = "buildsys.repo.done (unsigned)"
    expected_subti = 'Repo done:  f19-build'
    expected_icon = "http://fedoraproject.org/w/uploads/2/20/" + \
        "Artwork_DesignService_koji-icon-48.png"
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set(['repos/f19-build'])
    msg = {
        "username": "apache",
        "i": 2,
        "timestamp": 1359655886.353586,
        "topic": "org.fedoraproject.prod.buildsys.repo.done",
        "msg": {
            "tag": "f19-build"
        }
    }

if __name__ == '__main__':
    unittest.main()
