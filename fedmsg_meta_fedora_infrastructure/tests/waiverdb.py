# This file is part of fedmsg.
# Copyright (C) 2017 Red Hat, Inc.
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
""" Tests for waiverdb messages """

import unittest

from fedmsg.tests.test_meta import Base

from .common import add_doc


class TestLegacyNewWaiverV1(Base):
    """ `WaiverDB
    <https://pagure.io/waiverdb>`_ is a service that allows humans to override
    test failures and influence gating decisions made by `Greenwave
    <https://pagure.io/greenwave>`_.

    It published messages like this whenever someone **recorded a new waiver**,
    until version 0.6.0.
    """

    expected_title = "waiverdb.waiver.new"
    expected_subti = "ralph waived result 123 (fedora-26): \"This is fine.\""
    expected_link = (
        'https://waiverdb-web-waiverdb.app.os.fedoraproject.org/'
        'api/v1.0/waivers/8')
    expected_icon = 'https://apps.fedoraproject.org/img/icons/waiverdb.png'
    expected_secondary_icon = (
        'https://seccdn.libravatar.org/avatar/'
        '9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c'
        '?s=64&d=retro')
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    msg = {
        "username": "openshift",
        "i": 2,
        "timestamp": 1510020810.0,
        "msg_id": "2017-b173d0d1-a119-40e6-9e85-c6178468d9ff",
        "topic": "org.fedoraproject.stg.waiverdb.waiver.new",
        "headers": {},
        "msg": {
          "comment": "This is fine.",
          "username": "ralph",
          "waived": True,
          "timestamp": "2017-11-07T02:13:30.466388",
          "product_version": "fedora-26",
          "result_id": 123,
          "id": 8
        }
    }


class TestLegacyNewWaiverV2(Base):
    """ `WaiverDB
    <https://pagure.io/waiverdb>`_ is a service that allows humans to override
    test failures and influence gating decisions made by `Greenwave
    <https://pagure.io/greenwave>`_.

    It published messages like this whenever someone **recorded a new waiver**
    between versions 0.6.0 and 0.11.0. Compared to V1, result_id was replaced
    with the subject/testcase pair in this version.

    Note this message is faked up (based on a real waiver) as datagrepper
    doesn't seem to have recorded any real messages from the relevant time
    period.
    """

    expected_title = "waiverdb.waiver.new"
    expected_subti = (
        "ralph waived dist.abicheck for koji_build libsavitar-3.2.1-2.fc28: "
        "\"This is fine.\""
    )
    expected_link = (
        'https://waiverdb-web-waiverdb.app.os.fedoraproject.org/'
        'api/v1.0/waivers/50')
    expected_icon = 'https://apps.fedoraproject.org/img/icons/waiverdb.png'
    expected_secondary_icon = (
        'https://seccdn.libravatar.org/avatar/'
        '9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c'
        '?s=64&d=retro')
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    msg = {
        "username": "openshift",
        "i": 2,
        "timestamp": 1521550889.0,
        "msg_id": "2018-b173d0d1-a119-40e6-9e85-c6178468d9ef",
        "topic": "org.fedoraproject.stg.waiverdb.waiver.new",
        "headers": {},
        "msg": {
          "comment": "This is fine.",
          "username": "ralph",
          "waived": True,
          "timestamp": "2018-03-20T13:01:29.423251",
          "product_version": "fedora-28",
          "testcase": "dist.abicheck",
          "id": 50,
          "subject": {
            "item": "libsavitar-3.2.1-2.fc28",
            "type": "koji_build"
          }
        }
    }


class TestLegacyNewWaiverV3(Base):
    """ `WaiverDB
    <https://pagure.io/waiverdb>`_ is a service that allows humans to override
    test failures and influence gating decisions made by `Greenwave
    <https://pagure.io/greenwave>`_.

    It published messages like this whenever someone **recorded a new waiver**
    between versions 0.11.0 and 1.2.0. Compared to V2, subject_identifier and
    subject_type were added to the messages in this version.
    """

    expected_title = "waiverdb.waiver.new"
    expected_subti = (
        "ralph waived fedora-ci.koji-build.tier0.functional for koji_build "
        "dummy-test-package-gloster-0-548.fc33: \"This is fine.\""
    )
    expected_link = (
        'https://waiverdb-web-waiverdb.app.os.fedoraproject.org/'
        'api/v1.0/waivers/1638')
    expected_icon = 'https://apps.fedoraproject.org/img/icons/waiverdb.png'
    expected_secondary_icon = (
        'https://seccdn.libravatar.org/avatar/'
        '9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c'
        '?s=64&d=retro')
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    msg = {
        "username": "amqp-bridge",
        "i": 1586979,
        "timestamp": 1589928493.0,
        "msg_id": "2020-d0ad83e1-b0ec-459b-ba42-8500de1cb9c9",
        "topic": "org.fedoraproject.prod.waiverdb.waiver.new",
        "headers": {},
        "msg": {
          "comment": "This is fine.",
          "username": "ralph",
          "subject_type": "koji_build",
          "waived": True,
          "timestamp": "2017-11-07T02:13:30.466388",
          "product_version": "fedora-33",
          "testcase": "fedora-ci.koji-build.tier0.functional",
          "subject_identifier": "dummy-test-package-gloster-0-548.fc33",
          "proxied_by": "bodhi@service",
          "id": 1638,
          "subject": {
            "item": "dummy-test-package-gloster-0-548.fc33",
            "type": "koji_build"
          }
        }
    }


class TestNewWaiverV4(Base):
    """ `WaiverDB
    <https://pagure.io/waiverdb>`_ is a service that allows humans to override
    test failures and influence gating decisions made by `Greenwave
    <https://pagure.io/greenwave>`_.

    It publishes messages like this whenever someone **records a new waiver**
    since version 1.2.0. Compared to V3, scenario was added to the messages
    in this version.
    """

    expected_title = "waiverdb.waiver.new"
    expected_subti = (
        "ralph waived fedora-ci.koji-build.tier0.functional for koji_build "
        "dummy-test-package-gloster-0-5608.fc36: \"This is fine.\""
    )
    expected_link = (
        'https://waiverdb-web-waiverdb.app.os.fedoraproject.org/'
        'api/v1.0/waivers/9204')
    expected_icon = 'https://apps.fedoraproject.org/img/icons/waiverdb.png'
    expected_secondary_icon = (
        'https://seccdn.libravatar.org/avatar/'
        '9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c'
        '?s=64&d=retro')
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    msg = {
        "username": "amqp-bridge",
        "i": 6001918,
        "timestamp": 1635966233.0,
        "msg_id": "2021-d394924e-a1d9-4820-afbc-21c329e925fe",
        "topic": "org.fedoraproject.prod.waiverdb.waiver.new",
        "headers": {},
        "msg": {
          "comment": "This is fine.",
          "username": "ralph",
          "subject_type": "koji_build",
          "scenario": None,
          "waived": True,
          "timestamp": "2021-11-03T19:03:53.694763",
          "product_version": "fedora-36",
          "testcase": "fedora-ci.koji-build.tier0.functional",
          "subject_identifier": "dummy-test-package-gloster-0-5608.fc36",
          "proxied_by": "bodhi@service",
          "id": 9204,
          "subject": {
            "item": "dummy-test-package-gloster-0-5608.fc36",
            "type": "koji_build"
          }
        }
    }


class TestNewWaiverV4Scenario(Base):
    """ This is the same as V4, but with a non-null scenario and a different
    subject type, just to test some alternative paths. Note the scenario was
    null in the real message here due to a Bodhi bug.
    """

    nodoc = True
    expected_title = "waiverdb.waiver.new"
    expected_subti = (
        "ralph waived update.install_default_update_live (scenario "
        "fedora.updates-kde-live-iso.x86_64.64bit) for bodhi_update "
        "FEDORA-2021-1d24845e93: \"The previous waiver might have been invalidated.\""
    )
    expected_link = (
        'https://waiverdb-web-waiverdb.app.os.fedoraproject.org/'
        'api/v1.0/waivers/9181')
    expected_icon = 'https://apps.fedoraproject.org/img/icons/waiverdb.png'
    expected_secondary_icon = (
        'https://seccdn.libravatar.org/avatar/'
        '9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c'
        '?s=64&d=retro')
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    msg = {
        "username": "amqp-bridge",
        "i": 5844997,
        "timestamp": 1635864214.0,
        "msg_id": "2021-06787606-6fdd-411a-b575-c818135bd01a",
        "topic": "org.fedoraproject.prod.waiverdb.waiver.new",
        "headers": {},
        "msg": {
          "comment": "The previous waiver might have been invalidated.",
          "username": "ralph",
          "subject_type": "bodhi_update",
          "scenario": "fedora.updates-kde-live-iso.x86_64.64bit",
          "waived": True,
          "timestamp": "2021-11-02T14:43:34.162360",
          "product_version": "fedora-35",
          "testcase": "update.install_default_update_live",
          "subject_identifier": "FEDORA-2021-1d24845e93",
          "proxied_by": "bodhi@service",
          "id": 9181,
          "subject": {
            "item": "FEDORA-2021-1d24845e93",
            "type": "bodhi_update"
          }
        }
    }



add_doc(locals())

if __name__ == '__main__':
    unittest.main()
