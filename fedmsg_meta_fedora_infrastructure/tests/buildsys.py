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

import unittest

from fedmsg.tests.test_meta import Base

from common import add_doc


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

    The example here is one of a build **failing** on one of the **secondary
    arch** koji instances.
    """
    expected_title = "buildsys.build.state.change"
    expected_subti = "rmattes's eclipse-ptp-6.0.3-1.fc19 failed to build (ppc)"
    expected_icon = ("https://fedoraproject.org/w/uploads/2/20/"
                     "Artwork_DesignService_koji-icon-48.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "22c039c6c057741e96345ba5e160fe742c70273394bc566828a98e3bb071e838?s=64&d=retro")
    expected_packages = set(['eclipse-ptp'])
    expected_usernames = set(['rmattes'])
    expected_objects = set([
        'ppc/builds/eclipse-ptp/6.0.3/1.fc19',
    ])
    expected_link = ("http://ppc.koji.fedoraproject.org/koji/"
                     "buildinfo?buildID=12345")
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
            "new": 3,
            "owner": "rmattes",
            "build_id": 12345,
            "task_id": 4642,
            "instance": "ppc",
        }
    }


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



add_doc(locals())

if __name__ == '__main__':
    unittest.main()
