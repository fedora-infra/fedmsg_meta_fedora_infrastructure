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
""" Tests for koji messages """

import os
import unittest

from fedmsg.tests.test_meta import Base

from .common import add_doc


## This works... but the state from koji changes all the time so we can't write
## tests reliably for it without mocking til the cows come home.
#_build_long_form_cancel = """Package:    plasma-systemsettings-5.2.1-1.fc23
#Status:     canceled
#Built by:   dvratil
#ID:         614503
#Started:    Tue, 24 Feb 2015 14:50:21 UTC
#Finished:   Tue, 24 Feb 2015 14:53:47 UTC
#
#Closed tasks:
#-------------
#Task 9053697 on arm04-builder11.arm.fedoraproject.org
#Task Type: build (noarch)
#Link: https://koji.fedoraproject.org/koji/taskinfo?taskID=9053697
#
#Task 9053697 is canceled
#"""

## Same here.  the state in koji changes which makes this test change often.
#_build_long_form_fail = """Package:    64tass-1.51.727-1.fc22
#Status:     failed
#Built by:   sharkcz
#ID:         288888
#Started:    Sat, 14 Mar 2015 19:09:10 UTC
#Finished:   Sat, 14 Mar 2015 19:11:02 UTC
#
#Closed tasks:
#-------------
#Task 1755171 on fedora3.s390.bos.redhat.com
#Task Type: build (noarch)
#Link: http://s390.koji.fedoraproject.org/koji/taskinfo?taskID=1755171
#
#error building package (arch s390), mock exited with status 1; see build.log for more information
#
#Task 1755172 on fedora3.s390.bos.redhat.com
#Task Type: buildArch (s390)
#Link: http://s390.koji.fedoraproject.org/koji/taskinfo?taskID=1755172
#
#error building package (arch s390), mock exited with status 1; see build.log for more information
#
#Task 1755173 on fedora2.s390.bos.redhat.com
#Task Type: buildArch (s390x)
#Link: http://s390.koji.fedoraproject.org/koji/taskinfo?taskID=1755173
#
#error building package (arch s390x), mock exited with status 1; see build.log for more information
#"""


_build_long_form_complete = """Package:    ansible-1.8.3-1.el7
Status:     deleted
Built by:   kevin
ID:         612324
Started:    Tue, 17 Feb 2015 23:39:49 UTC
Finished:   Tue, 17 Feb 2015 23:41:56 UTC

Closed tasks:
-------------
Task 8973154 on arm02-builder15.arm.fedoraproject.org
Task Type: build (noarch)
Link: https://koji.fedoraproject.org/koji/taskinfo?taskID=8973154

Task 8973158 on buildhw-11.phx2.fedoraproject.org
Task Type: buildSRPMFromSCM (noarch)
Link: https://koji.fedoraproject.org/koji/taskinfo?taskID=8973158
logs:
  https://kojipkgs.fedoraproject.org/work/tasks/3158/8973158/root.log
  https://kojipkgs.fedoraproject.org/work/tasks/3158/8973158/build.log
  https://kojipkgs.fedoraproject.org/work/tasks/3158/8973158/state.log
srpm:
  https://kojipkgs.fedoraproject.org/work/tasks/3158/8973158/ansible-1.8.3-1.el7.src.rpm

Task 8973189 on buildhw-04.phx2.fedoraproject.org
Task Type: buildArch (noarch)
Link: https://koji.fedoraproject.org/koji/taskinfo?taskID=8973189
logs:
  https://kojipkgs.fedoraproject.org/work/tasks/3189/8973189/root.log
  https://kojipkgs.fedoraproject.org/work/tasks/3189/8973189/build.log
  https://kojipkgs.fedoraproject.org/work/tasks/3189/8973189/state.log
rpms:
  https://kojipkgs.fedoraproject.org/work/tasks/3189/8973189/ansible-1.8.3-1.el7.noarch.rpm
srpms:
  https://kojipkgs.fedoraproject.org/work/tasks/3189/8973189/ansible-1.8.3-1.el7.src.rpm

Task 8973199 on arm02-builder15.arm.fedoraproject.org
Task Type: tagBuild (noarch)
Link: https://koji.fedoraproject.org/koji/taskinfo?taskID=8973199
"""

_scratch_long_form_fail = """Task 6380373 on arm02-builder22.arm.fedoraproject.org
Task Type: build (noarch)
Link: https://koji.fedoraproject.org/koji/taskinfo?taskID=6380373

error building package (arch noarch), mock exited with status 1; see build.log for more information

Task 6380374 on buildvm-17.phx2.fedoraproject.org
Task Type: buildArch (noarch)
Link: https://koji.fedoraproject.org/koji/taskinfo?taskID=6380374

error building package (arch noarch), mock exited with status 1; see build.log for more information
"""


class TestKojiTaskStateChangeStart(Base):
    """ Koji emits messages on this topic anytime the state of a **scratch**
    build changes.

    For reasons internal to koji itself, the state codes for **scratch** builds
    are not as cryptic as the ones for regular builds.  It is worth noting that
    the `task` state codes are different from the `build` state codes.  If you
    wanted to know the numeric equivalents, you could check with koji itself:

        >>> import koji
        >>> koji.TASK_STATES
        {
            'FREE': 0,
            'OPEN': 1,
            'CLOSED': 2,
            'CANCELED': 3,
            'ASSIGNED': 4,
            'FAILED': 5,
        }

    Here's an example message of a new **scratch build starting**.
    """
    expected_title = "buildsys.task.state.change"
    expected_subti = "ralph's scratch build of " + \
        "python-websocket-client-0.12.0-1.fc20.src.rpm started"
    expected_icon = ("https://fedoraproject.org/w/uploads/2/20/"
                     "Artwork_DesignService_koji-icon-48.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
    expected_usernames = set(['ralph'])
    expected_packages = set([])
    expected_objects = set([
        'primary/scratch_builds/python-websocket-client-0.12.0-1.fc20.src.rpm',
    ])
    expected_link = ("http://koji.stg.fedoraproject.org/koji/"
                     "taskinfo?taskID=6380373")
    msg = {
        u'username': u'root',
        u'i': 1,
        u'timestamp': 1389298195,
        u'msg_id': u'2014-10b5b1b6-42c7-4d64-aeae-5029b9515d47',
        u'topic': u'org.fedoraproject.stg.buildsys.task.state.change',
        u'msg': {
            u'old': u'FREE',
            u'attribute': u'state',
            u'method': u'build',
            u'owner': u'ralph',
            u'new': u'OPEN',
            u'srpm': 'python-websocket-client-0.12.0-1.fc20.src.rpm',
            u'id': 6380373,
        }
    }


class TestKojiTaskStateChangeFail(Base):
    """ Koji emits messages on this topic anytime the state of a **scratch**
    build changes.

    For reasons internal to koji itself, the state codes for **scratch** builds
    are not as cryptic as the ones for regular builds.  It is worth noting that
    the `task` state codes are different from the `build` state codes.  If you
    wanted to know the numeric equivalents, you could check with koji itself:

        >>> import koji
        >>> koji.TASK_STATES
        {
            'FREE': 0,
            'OPEN': 1,
            'CLOSED': 2,
            'CANCELED': 3,
            'ASSIGNED': 4,
            'FAILED': 5,
        }

    Here's an example message of a **scratch build failing**.
    """
    expected_title = "buildsys.task.state.change"
    expected_subti = "ralph's scratch build of " + \
        "python-websocket-client-0.12.0-1.fc20.src.rpm failed"
    expected_icon = ("https://fedoraproject.org/w/uploads/2/20/"
                     "Artwork_DesignService_koji-icon-48.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
    expected_usernames = set(['ralph'])
    expected_packages = set([])
    expected_objects = set([
        'primary/scratch_builds/python-websocket-client-0.12.0-1.fc20.src.rpm',
    ])
    expected_link = ("http://koji.fedoraproject.org/koji/"
                     "taskinfo?taskID=6380373")
    msg = {
        "username": "root",
        "i": 1,
        "timestamp": 1389298512,
        "msg_id": "2014-991dbbad-b5f5-4f62-b889-d3b637d0cb49",
        "topic": "org.fedoraproject.prod.buildsys.task.state.change",
        "msg": {
            "old": "OPEN",
            "attribute": "state",
            "method": "build",
            "owner": "ralph",
            "srpm": "python-websocket-client-0.12.0-1.fc20.src.rpm",
            "new": "FAILED",
            "id": 6380373,
        }
    }


class TestKojiTaskStateChangeFailWithTarget(Base):
    """ Koji emits messages on this topic anytime the state of a **scratch**
    build changes.

    For reasons internal to koji itself, the state codes for **scratch** builds
    are not as cryptic as the ones for regular builds.  It is worth noting that
    the `task` state codes are different from the `build` state codes.  If you
    wanted to know the numeric equivalents, you could check with koji itself:

        >>> import koji
        >>> koji.TASK_STATES
        {
            'FREE': 0,
            'OPEN': 1,
            'CLOSED': 2,
            'CANCELED': 3,
            'ASSIGNED': 4,
            'FAILED': 5,
        }

    Here's an example message of a **scratch build failing**.
    """
    expected_title = "buildsys.task.state.change"
    expected_subti = "ralph's scratch build of " + \
        "python-websocket-client-0.12.0-1.fc20.src.rpm for epel7-candidate failed"
    expected_icon = ("https://fedoraproject.org/w/uploads/2/20/"
                     "Artwork_DesignService_koji-icon-48.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
    expected_usernames = set(['ralph'])
    expected_packages = set([])
    expected_objects = set([
        'primary/scratch_builds/python-websocket-client-0.12.0-1.fc20.src.rpm',
    ])
    expected_link = ("http://koji.fedoraproject.org/koji/"
                     "taskinfo?taskID=6380373")
    msg = {
        "username": "root",
        "i": 1,
        "timestamp": 1389298512,
        "msg_id": "2014-991dbbad-b5f5-4f62-b889-d3b637d0cb49",
        "topic": "org.fedoraproject.prod.buildsys.task.state.change",
        "msg": {
            "old": "OPEN",
            "attribute": "state",
            "method": "build",
            "owner": "ralph",
            "srpm": "python-websocket-client-0.12.0-1.fc20.src.rpm",
            "new": "FAILED",
            "id": 6380373,
            "info": {
                "parent": None,
                "completion_time": None,
                "start_time": "2015-06-22 14:04:41.44985",
                "request": [
                    "cli-build/1434981816.694115.CAAulQZy/pagure-0.1.18-1.fc21.src.rpm",
                    "epel7-candidate",
                    {
                        "scratch": True
                    }
                ],
                "waiting": None,
                "awaited": None,
                "id": 10177586,
                "priority": 20,
                "channel_id": 1,
                "state": 1,
                "create_time": "2015-06-22 14:04:40.523486",
                "owner": 456,
                "host_id": 60,
                "method": "build",
                "label": None,
                "arch": "noarch",
                "children": []
            },
        }
    }


class TestKojiBuildTag(Base):
    """ Koji emits these messages when a build has a certain tag added to it.
    """
    expected_title = "buildsys.tag"
    expected_subti = ("ralph's stage-4.1.1-3.fc18 tagged into "
                      "f18-updates-testing-pending by bodhi")
    expected_icon = ("https://fedoraproject.org/w/uploads/2/20/"
                     "Artwork_DesignService_koji-icon-48.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
    expected_packages = set(['stage'])
    expected_usernames = set(['ralph', 'bodhi'])
    expected_objects = set([
        'primary/builds/stage/4.1.1/3.fc18',
        'primary/tags/f18-updates-testing-pending',
    ])
    expected_link = ("http://koji.fedoraproject.org/koji/"
                     "taginfo?tagID=216")
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
            "user": "bodhi",
            "owner": "ralph",
            "tag_id": 216,
        }
    }


class TestKojiBuildUnTag(Base):
    """ Koji emits these messages anytime a tag is removed from a build. """
    expected_title = "buildsys.untag"
    expected_subti = ("ralph's globus-gram-job-manager-sge-1.5-2.fc16 "
                      "untagged from f16-updates-pending by bodhi")
    expected_icon = ("https://fedoraproject.org/w/uploads/2/20/"
                     "Artwork_DesignService_koji-icon-48.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
    expected_packages = set(['globus-gram-job-manager-sge'])
    expected_usernames = set(['ralph', 'bodhi'])
    expected_objects = set([
        'primary/builds/globus-gram-job-manager-sge/1.5/2.fc16',
        'primary/tags/f16-updates-pending',
    ])
    expected_link = ("http://koji.fedoraproject.org/koji/"
                     "taginfo?tagID=216")
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
            "user": "bodhi",
            "owner": "ralph",
            "tag_id": 216,
        }
    }


class TestKojiBuildStateChangeStart(Base):
    """ Koji emits messages on this topic anytime the state of a build changes.

    The state codes can be pretty cryptic (they are just integers and are the
    enums used by koji internally):

        >>> import koji
        >>> koji.BUILD_STATES
        {
            'BUILDING': 0,
            'COMPLETE': 1,
            'DELETED': 2,
            'FAILED': 3,
            'CANCELED': 4,
        }

    The example here is one of a new build **starting**.
    """
    expected_title = "buildsys.build.state.change"
    expected_subti = "ralph's eclipse-ptp-6.0.3-1.fc19 started building"
    expected_icon = ("https://fedoraproject.org/w/uploads/2/20/"
                     "Artwork_DesignService_koji-icon-48.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
    expected_usernames = set(['ralph'])
    expected_packages = set(['eclipse-ptp'])
    expected_objects = set([
        'primary/builds/eclipse-ptp/6.0.3/1.fc19'
    ])
    expected_link = ("http://koji.fedoraproject.org/koji/"
                     "buildinfo?buildID=12345")
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
            "new": 0,
            "owner": "ralph",
            "build_id": 12345,
            "task_id": 4642,
            "instance": "primary",
        }
    }


class TestKojiBuildStateChangeStartNoOwner(Base):
    """ Koji emits messages on this topic anytime the state of a build changes.

    The state codes can be tricky, (they're the ones used internally by koji).

        >>> import koji
        >>> koji.BUILD_STATES
        {
            'BUILDING': 0,
            'COMPLETE': 1,
            'DELETED': 2,
            'FAILED': 3,
            'CANCELED': 4,
        }

    *This* example message shows one where for some reason or another, koji
    was unable to publish the name of the owner of a build.  The 'owner' field
    is set to None.
    """
    expected_title = "buildsys.build.state.change"
    expected_subti = "eclipse-ptp-6.0.3-1.fc19 started building"
    expected_icon = ("https://fedoraproject.org/w/uploads/2/20/"
                     "Artwork_DesignService_koji-icon-48.png")
    expected_secondary_icon = expected_icon
    expected_usernames = set([])
    expected_packages = set(['eclipse-ptp'])
    expected_objects = set([
        'primary/builds/eclipse-ptp/6.0.3/1.fc19'
    ])
    expected_link = ("http://koji.fedoraproject.org/koji/"
                     "buildinfo?buildID=12345")
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
            "new": 0,
            "owner": None,
            "build_id": 12345,
            "task_id": 4642,
            "instance": "primary",
        }
    }


class TestKojiBuildStateChangeCancel(Base):
    """ Koji emits messages on this topic anytime the state of a build changes.

    The state codes can be pretty cryptic (they are just integers and are the
    enums used by koji internally):

        >>> import koji
        >>> koji.BUILD_STATES
        {
            'BUILDING': 0,
            'COMPLETE': 1,
            'DELETED': 2,
            'FAILED': 3,
            'CANCELED': 4,
        }

    The example here is one of a build **being cancelled** on the **primary**
    koji instance.
    """
    expected_title = "buildsys.build.state.change"
    expected_subti = "dvratil's plasma-systemsettings-5.2.1-1.fc23 " + \
        "was cancelled"
    expected_icon = ("https://fedoraproject.org/w/uploads/2/20/"
                     "Artwork_DesignService_koji-icon-48.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "1d952f7f249f4cd4d2929e09ad616ccdd87b4c2f3418a01ea6e6396ac41edd6a"
        "?s=64&d=retro")
    expected_packages = set(['plasma-systemsettings'])
    expected_usernames = set(['dvratil'])
    expected_objects = set([
        'primary/builds/plasma-systemsettings/5.2.1/1.fc23',
    ])
    expected_link = ("http://koji.fedoraproject.org/koji/"
                     "buildinfo?buildID=614503")
    msg = {
        "timestamp": 1424789698.0,
        "msg_id": "2015-51be4c8e-8ab6-4dcb-ac0d-37b257765c71",
        "topic": "org.fedoraproject.prod.buildsys.build.state.change",
        "msg": {
            "build_id": 614503,
            "old": 4,
            "name": "plasma-systemsettings",
            "task_id": 9053697,
            "attribute": "state",
            "instance": "primary",
            "version": "5.2.1",
            "owner": "dvratil",
            "new": 4,
            "release": "1.fc23"
        }
    }


class TestKojiBuildStateChangeFail(Base):
    """ Koji emits messages on this topic anytime the state of a build changes.

    The state codes can be pretty cryptic (they are just integers and are the
    enums used by koji internally):

        >>> import koji
        >>> koji.BUILD_STATES
        {
            'BUILDING': 0,
            'COMPLETE': 1,
            'DELETED': 2,
            'FAILED': 3,
            'CANCELED': 4,
        }

    The example here is one of a build **failing** on a **secondary arch** koji
    instance.
    """
    expected_title = "buildsys.build.state.change"
    expected_subti = "sharkcz's 64tass-1.51.727-1.fc22 failed to build (s390)"
    expected_icon = ("https://fedoraproject.org/w/uploads/2/20/"
                     "Artwork_DesignService_koji-icon-48.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "0d6309f7bbfbf2bca3fc0fea5151b48895a2735481e4a38fce599fd5f24c546a"
        "?s=64&d=retro")
    expected_packages = set(['64tass'])
    expected_usernames = set(['sharkcz'])
    expected_objects = set([
        's390/builds/64tass/1.51.727/1.fc22',
    ])
    expected_link = ("http://s390.koji.fedoraproject.org/koji/"
                     "buildinfo?buildID=288888")
    msg = {
        "timestamp": 1424787586.0,
        "msg_id": "2015-e3483831-5f88-401b-b20d-05537e6a010d",
        "topic": "org.fedoraproject.prod.buildsys.build.state.change",
        "msg": {
            "build_id": 288888,
            "old": 0,
            "name": "64tass",
            "task_id": 1739950,
            "attribute": "state",
            "instance": "s390",
            "version": "1.51.727",
            "owner": "sharkcz",
            "new": 3,
            "release": "1.fc22"
        }
    }


class TestKojiBuildStateChangeComplete(Base):
    """ Koji emits messages on this topic anytime the state of a build changes.

    The state codes can be pretty cryptic (they are just integers and are the
    enums used by koji internally):

        >>> import koji
        >>> koji.BUILD_STATES
        {
            'BUILDING': 0,
            'COMPLETE': 1,
            'DELETED': 2,
            'FAILED': 3,
            'CANCELED': 4,
        }

    The example here is one of a build **succeeding** on the **primary**
    koji instance.
    """
    expected_title = "buildsys.build.state.change"
    expected_subti = "kevin's ansible-1.8.3-1.el7 completed"
    expected_icon = ("https://fedoraproject.org/w/uploads/2/20/"
                     "Artwork_DesignService_koji-icon-48.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "1a7d8c43c8b89789a33a3266b0e20be7759a502ff38b74ff724a4db6aa33ede8"
        "?s=64&d=retro")
    expected_packages = set(['ansible'])
    expected_usernames = set(['kevin'])
    expected_objects = set([
        'primary/builds/ansible/1.8.3/1.el7',
    ])
    expected_link = ("http://koji.fedoraproject.org/koji/"
                     "buildinfo?buildID=612324")
    msg = {
        "timestamp": 1424216566.0,
        "msg_id": "2015-6395fb7a-e5a7-4b95-858a-ff7b80410e7f",
        "topic": "org.fedoraproject.prod.buildsys.build.state.change",
        "msg": {
            "build_id": 612324,
            "old": 0,
            "name": "ansible",
            "task_id": 8973154,
            "attribute": "state",
            "instance": "primary",
            "version": "1.8.3",
            "owner": "kevin",
            "new": 1,
            "release": "1.el7"
        }
    }


koji = None
try:
    import koji
except ImportError:
    pass

if koji and not (
    'FEDMSG_META_NO_NETWORK' in os.environ or 'TRAVIS_CI' in os.environ):

    TestKojiBuildStateChangeComplete.expected_long_form = \
        _build_long_form_complete
    #TestKojiBuildStateChangeFail.expected_long_form = \
    #    _build_long_form_fail
    #TestKojiBuildStateChangeCancel.expected_long_form = \
    #    _build_long_form_cancel
    TestKojiTaskStateChangeFail.expected_long_form = \
        _scratch_long_form_fail

class TestKojiRepoInit(Base):
    """ Koji emits these messages when a repository begins initializing. """
    expected_title = "buildsys.repo.init"
    expected_subti = 'Repo initialized:  f19-build'
    expected_icon = ("https://fedoraproject.org/w/uploads/2/20/"
                     "Artwork_DesignService_koji-icon-48.png")
    expected_secondary_icon = expected_icon
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set([
        'primary/repos/f19-build',
    ])
    expected_link = ("http://koji.fedoraproject.org/koji/"
                     "taginfo?tagID=12345")
    msg = {
        "username": "apache",
        "i": 2,
        "timestamp": 1359655886.353586,
        "topic": "org.fedoraproject.prod.buildsys.repo.init",
        "msg": {
            "tag": "f19-build",
            "tag_id": 12345,
            "repo_id": 23456,
        }
    }


class TestKojiRepoDone(Base):
    """ Koji emits these messages when repo initialization finishes. """
    expected_title = "buildsys.repo.done"
    expected_subti = 'Repo done:  f19-build'
    expected_icon = ("https://fedoraproject.org/w/uploads/2/20/"
                     "Artwork_DesignService_koji-icon-48.png")
    expected_secondary_icon = expected_icon
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set([
        'primary/repos/f19-build',
    ])
    expected_link = ("http://koji.fedoraproject.org/koji/"
                     "taginfo?tagID=12345")
    msg = {
        "username": "apache",
        "i": 2,
        "timestamp": 1359655886.353586,
        "topic": "org.fedoraproject.prod.buildsys.repo.done",
        "msg": {
            "tag": "f19-build",
            "tag_id": 12345,
            "repo_id": 23456,
        }
    }


class LegacyTestKojiRepoDone(Base):
    """ Some old repo messages do not include any information at all.
    For instance:  2014-31fb32e5-f45b-477e-8458-03a5792dabeb
    """
    expected_title = "buildsys.repo.done"
    expected_subti = 'Repo done:  unknown (arm)'
    expected_icon = ("https://fedoraproject.org/w/uploads/2/20/"
                     "Artwork_DesignService_koji-icon-48.png")
    expected_secondary_icon = expected_icon
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set([
        'arm/repos/unknown',
    ])
    expected_link = "http://arm.koji.fedoraproject.org/koji"
    msg = {
        "username": "apache",
        "i": 2,
        "timestamp": 1359655886.353586,
        "topic": "org.fedoraproject.prod.buildsys.repo.done",
        "msg": {
            "instance": "arm",
        }
    }


class TestKojiPackageListChange(Base):
    """ Koji emits these messages a package listing changes. """
    expected_title = "buildsys.package.list.change"
    expected_subti = "Package list change for almanah:  'f17'"
    expected_icon = ("https://fedoraproject.org/w/uploads/2/20/"
                     "Artwork_DesignService_koji-icon-48.png")
    expected_secondary_icon = expected_icon
    expected_packages = set(["almanah"])
    expected_usernames = set([])
    expected_objects = set([
        'primary/tags/f17',
    ])
    msg = {
        "topic": "org.fedoraproject.prod.buildsys.package.list.change",
        "msg": {
            "tag": "f17",
            "package": "almanah"
        },
        "i": 2,
        "timestamp": 1361903735.0
    }


class LegacyTestKojiRPMSign(Base):
    """ The format of the rpm.sign message changed in 2016:
    https://pagure.io/koji/pull-request/188
    """
    expected_title = "buildsys.rpm.sign"
    expected_subti = "Koji build " + \
        "gstreamer1-plugins-base-devel-1.4.5-1.fc21.i686.rpm signed " + \
        "with sigkey 'ab845621'"
    expected_icon = ("https://fedoraproject.org/w/uploads/2/20/"
                     "Artwork_DesignService_koji-icon-48.png")
    expected_link = ("http://koji.fedoraproject.org/koji/"
                     "buildinfo?buildID=607658")
    expected_secondary_icon = expected_icon
    expected_packages = set(["gstreamer1-plugins-base-devel"])
    expected_usernames = set([])
    expected_objects = set([
        'signatures/gstreamer1-plugins-base-devel',
    ])

    msg = {
        "username": "apache",
        "i": 15,
        "timestamp": 1422465977,
        "msg_id": "2015-271fd050-3198-46f8-b0b1-4bcf6e70bdd0",
        "crypto": "x509",
        "topic": "org.fedoraproject.prod.buildsys.rpm.sign",
        "msg": {
            "info": {
                "build_id": 607658,
                "name": "gstreamer1-plugins-base-devel",
                "buildroot_id": 2877398,
                "buildtime": 1422465286,
                "sighash": "8f84058e6bbcae89701271e8b0c43d1d",
                "sigkey": "ab845621",
                "id": 5928874,
                "epoch": None,
                "version": "1.4.5",
                "arch": "i686",
                "release": "1.fc21",
                "external_repo_id": 0,
                "payloadhash": "05bc945666248817e0b5346f811bbac0",
                "external_repo_name": "INTERNAL",
                "size": 266720
            },
            "attribute": "sighash",
            "old": None,
            "new": "8f84058e6bbcae89701271e8b0c43d1d",
            "instance": "primary"
        }
    }


class TestKojiRPMSign(Base):
    """ Koji emits these messages a package is signed with GPG.

    For more information, see the `sigul project
    <https://fedorahosted.org/sigul/>`_.
    """
    expected_title = "buildsys.rpm.sign"
    expected_subti = "Koji build " + \
        "gstreamer1-plugins-base-devel-1.4.5-1.fc21.i686.rpm signed " + \
        "with sigkey 'ab845621'"
    expected_icon = ("https://fedoraproject.org/w/uploads/2/20/"
                     "Artwork_DesignService_koji-icon-48.png")
    expected_link = ("http://koji.fedoraproject.org/koji/"
                     "buildinfo?buildID=607658")
    expected_secondary_icon = expected_icon
    expected_packages = set(["gstreamer1-plugins-base-devel"])
    expected_usernames = set([])
    expected_objects = set([
        'signatures/gstreamer1-plugins-base-devel',
    ])

    msg = {
        "username": "apache",
        "i": 15,
        "timestamp": 1422465977,
        "msg_id": "2015-271fd050-3198-46f8-b0b1-4bcf6e70bdd0",
        "crypto": "x509",
        "topic": "org.fedoraproject.prod.buildsys.rpm.sign",
        "msg": {
            "build": {
                "id": 607658,
                # ...
            },
            "rpm": {
                "build_id": 607658,
                "name": "gstreamer1-plugins-base-devel",
                "buildroot_id": 2877398,
                "buildtime": 1422465286,
                "id": 5928874,
                "epoch": None,
                "version": "1.4.5",
                "arch": "i686",
                "release": "1.fc21",
                "external_repo_id": 0,
                "payloadhash": "05bc945666248817e0b5346f811bbac0",
                "external_repo_name": "INTERNAL",
                "size": 266720
            },
            "sigkey": "ab845621",
            "sighash": "8f84058e6bbcae89701271e8b0c43d1d",
            "instance": "primary"
        }
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
