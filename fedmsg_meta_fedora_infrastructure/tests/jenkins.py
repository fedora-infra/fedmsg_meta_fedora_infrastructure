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
# Authors:  Ricky Elrod <codeblock@fedoraproject.org>
#
""" Tests for jenkins messages """

import unittest

from fedmsg_meta_fedora_infrastructure.tests import Base

from .common import add_doc


class TestJenkinsBuildStart(Base):
    """ `Jenkins <http://jenkins.cloud.fedoraproject.org/>`_ publishes these
    messages when a build starts.
    """
    expected_title = "jenkins.build.start"
    expected_subti = ("Jenkins project 'fedora-mobile' started building")
    expected_secondary_icon = ''
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set([
        'jenkins/fedora-mobile/build.start',
    ])
    expected_link = (
        "http://jenkins.cloud.fedoraproject.org/job/fedora-mobile/174/")
    msg = {
        u'i': 1,
        u'timestamp': 1392150202.0,
        u'msg_id': u'2014-2ffb842d-7868-47e8-bfb6-910fb93d9aa9',
        u'topic': u'org.fedoraproject.prod.jenkins.build.start',
        u'msg': {
            u'project': 'fedora-mobile',
            u'build': 174,
        },
    }


class TestJenkinsBuildPassed(Base):
    """ `Jenkins <http://jenkins.cloud.fedoraproject.org/>`_ publishes these
    messages when a build completes successfully.
    """
    expected_title = "jenkins.build.passed"
    expected_subti = ("Jenkins project 'fedora-mobile' built successfully")
    expected_secondary_icon = ''
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set([
        'jenkins/fedora-mobile/build.passed',
    ])
    expected_link = (
        "http://jenkins.cloud.fedoraproject.org/job/fedora-mobile/174/")
    msg = {
        u'i': 1,
        u'timestamp': 1392150202.0,
        u'msg_id': u'2014-b035a3d4-078b-4733-9df6-be4f5da911bd',
        u'topic': u'org.fedoraproject.prod.jenkins.build.passed',
        u'msg': {
            u'project': 'fedora-mobile',
            u'took': u'1 min 28 sec',
            u'build': 174,
        },
    }


class TestJenkinsBuildFailed(Base):
    """ `Jenkins <http://jenkins.cloud.fedoraproject.org/>`_ publishes these
    messages when a build completes with a failure.
    """
    expected_title = "jenkins.build.failed"
    expected_subti = ("Jenkins project 'fedora-mobile' failed to build")
    expected_secondary_icon = ''
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set([
        'jenkins/fedora-mobile/build.failed',
    ])
    expected_link = (
        "http://jenkins.cloud.fedoraproject.org/job/fedora-mobile/165/")
    msg = {
        u'i': 1,
        u'timestamp': 1390982532.0,
        u'msg_id': u'2014-851eb465-56f2-4f3f-bf8a-2b86c95d1246',
        u'topic': u'org.fedoraproject.prod.jenkins.build.failed',
        u'msg': {
            u'project': 'fedora-mobile',
            u'took': u'9.4 sec',
            u'build': 165,
        },
    }

class TestJenkinsBuildAborted(Base):
    """ `Jenkins <http://jenkins.cloud.fedoraproject.org/>`_ publishes these
    messages when a build is aborted.
    """
    expected_title = "jenkins.build.aborted"
    expected_subti = ("Jenkins project 'fedora-mobile' build aborted")
    expected_secondary_icon = ''
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set([
        'jenkins/fedora-mobile/build.aborted',
    ])
    expected_link = (
        "http://jenkins.cloud.fedoraproject.org/job/fedora-mobile/165/")
    msg = {
        u'i': 1,
        u'timestamp': 1390982532.0,
        u'msg_id': u'2014-851eb465-56f2-4f3f-bf8a-2b86c95d1246',
        u'topic': u'org.fedoraproject.prod.jenkins.build.aborted',
        u'msg': {
            u'project': 'fedora-mobile',
            u'took': u'9.4 sec',
            u'build': 165,
        },
    }

class TestJenkinsBuildNotBuilt(Base):
    """ `Jenkins <http://jenkins.cloud.fedoraproject.org/>`_ publishes these
    messages when a build doesn't actually build (wat?).
    """
    expected_title = "jenkins.build.notbuilt"
    expected_subti = ("Jenkins project 'fedora-mobile' did not build")
    expected_secondary_icon = ''
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set([
        'jenkins/fedora-mobile/build.notbuilt',
    ])
    expected_link = (
        "http://jenkins.cloud.fedoraproject.org/job/fedora-mobile/165/")
    msg = {
        u'i': 1,
        u'timestamp': 1390982532.0,
        u'msg_id': u'2014-851eb465-56f2-4f3f-bf8a-2b86c95d1246',
        u'topic': u'org.fedoraproject.prod.jenkins.build.notbuilt',
        u'msg': {
            u'project': 'fedora-mobile',
            u'took': u'9.4 sec',
            u'build': 165,
        },
    }

class TestJenkinsBuildUnstable(Base):
    """ `Jenkins <http://jenkins.cloud.fedoraproject.org/>`_ publishes these
    messages when a build completes with warnings.
    """
    expected_title = "jenkins.build.unstable"
    expected_subti = ("Jenkins project 'fedora-mobile' built with warnings")
    expected_secondary_icon = ''
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set([
        'jenkins/fedora-mobile/build.unstable',
    ])
    expected_link = (
        "http://jenkins.cloud.fedoraproject.org/job/fedora-mobile/165/")
    msg = {
        u'i': 1,
        u'timestamp': 1390982532.0,
        u'msg_id': u'2014-851eb465-56f2-4f3f-bf8a-2b86c95d1246',
        u'topic': u'org.fedoraproject.prod.jenkins.build.unstable',
        u'msg': {
            u'project': 'fedora-mobile',
            u'took': u'9.4 sec',
            u'build': 165,
        },
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
