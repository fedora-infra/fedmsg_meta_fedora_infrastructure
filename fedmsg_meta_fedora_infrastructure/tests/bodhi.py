# This file is part of fedmsg.
# Copyright (C) 2012-2014 Red Hat, Inc.
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
""" Tests for fedmsg.meta """

import unittest

from fedmsg_meta_fedora_infrastructure.tests.base import Base

from fedmsg_meta_fedora_infrastructure.tests.common import add_doc


class LegacyTestBodhiUpdateComplete(Base):
    """ The `Bodhi Updates System <https://bodhi.fedoraproject.org>`_
    publishes messages on this topic whenever an update
    **completes it's push to the testing repository**.  Here's a
    straightforward example:

    .. note:: We *used* to have this message in our system, but it got removed
       when we found that fedmsg caused the bodhi1 masher to segfault in
       certain circumstances.  This message, or one like it will likely return
       with the advent of bodhi2.
    """
    expected_title = "bodhi.update.complete.testing"
    expected_subti = "ralph's fedmsg-0.2.7-2.el6 bodhi update " + \
        "completed push to testing"
    expected_link = "https://bodhi.fedoraproject.org/updates/" + \
        "fedmsg-0.2.7-2.el6"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c" + \
        "?s=64&d=retro"
    expected_usernames = set(['ralph'])
    expected_packages = set(['fedmsg'])
    expected_objects = set(['packages/fedmsg'])

    msg = {
        "i": 88,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.bodhi.update.complete.testing",
        "msg": {
            "update": {
                "close_bugs": True,
                "critpath": False,
                "stable_karma": 3,
                "date_pushed": 1344447839.0,
                "title": "fedmsg-0.2.7-2.el6",
                "nagged": None,
                "comments": [
                    {
                        "group": None,
                        "author": "bodhi",
                        "text": "This update has been submitted for " +
                        "testing by ralph. ",
                        "karma": 0,
                        "anonymous": False,
                        "timestamp": 1344266157.0
                    },
                    {
                        "group": None,
                        "author": "bodhi",
                        "text": "This update is currently being pushed " +
                        "to the Fedora EPEL 6 testing updates " +
                        "repository.",
                        "karma": 0,
                        "anonymous": False,
                        "timestamp": 1344443927.0
                    }
                ],
                "updateid": "FEDORA-EPEL-2012-6650",
                "type": "bugfix",
                "status": "testing",
                "date_submitted": 1344266152.0,
                "unstable_karma": -3,
                "release": {
                    "dist_tag": "dist-6E-epel",
                    "id_prefix": "FEDORA-EPEL",
                    "locked": False,
                    "name": "EL-6",
                    "long_name": "Fedora EPEL 6"
                },
                "approved": None,
                "builds": [
                    {
                        "nvr": "fedmsg-0.2.7-2.el6",
                        "package": {
                            "suggest_reboot": False,
                            "committers": [
                                "ralph"
                            ],
                            "name": "fedmsg"
                        }
                    }
                ],
                "date_modified": None,
                "notes": "Bugfix - Added a forgotten new " +
                "requirement on python-requests.",
                "request": None,
                "bugs": [],
                "critpath_approved": False,
                "karma": 0,
                "submitter": "ralph",
            }
        }
    }


class LegacyTestBodhiRequestMultiplePackagesPerUpdate(Base):
    """ The `Bodhi Updates System <https://bodhi.fedoraproject.org>`_
    publishes messages on this topic whenever a *user* requests that an update
    be pushed to the testing repository. Some updates may contain *multiple
    packages*, which can be a little tricky if you're not ready for it.  Here's
    an example of that:

    .. note:: This is the old format used for specifying multiple packages.
    """
    expected_title = "bodhi.update.request.testing"
    expected_subti = "lmacken submitted " + \
        "gnome-settings-daemon-3.6.1-1.fc18,contr..." + \
        " to testing"
    expected_link = "https://bodhi.fedoraproject.org/updates/" + \
        "gnome-settings-daemon-3.6.1-1.fc18,control-center-3.6.1-1.fc18"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "0d574577afa8deac19df2673cdea9aef45549ff8fac798ddaba61541c69e185a?s=64&d=retro"
    expected_usernames = set(['lmacken', 'hadess'])
    expected_packages = set(['gnome-settings-daemon', 'control-center'])
    expected_objects = set([
        'packages/gnome-settings-daemon',
        'packages/control-center',
    ])

    msg = {
        "topic": "org.fedoraproject.prod.bodhi.update.request.testing",
        "msg": {
            'agent': 'lmacken',
            "update": {
                "status": "pending",
                "critpath": False,
                "stable_karma": 3,
                "date_pushed": None,
                "title": "gnome-settings-daemon-3.6.1-1.fc18," +
                "control-center-3.6.1-1.fc18",
                "nagged": None,
                "comments": [
                    {
                        "group": None,
                        "author": "bodhi",
                        "text": "This update has been submitted for "
                        "testing by hadess. ",
                        "karma": 0,
                        "anonymous": False,
                        "timestamp": 1349718539.0,
                        "update_title": "gnome-settings-daemon-3.6.1-1.fc18," +
                        "control-center-3.6.1-1.fc18"
                    }
                ],
                "updateid": None,
                "type": "bugfix",
                "close_bugs": True,
                "date_submitted": 1349718534.0,
                "unstable_karma": -3,
                "release": {
                    "dist_tag": "f18",
                    "locked": True,
                    "long_name": "Fedora 18",
                    "name": "F18",
                    "id_prefix": "FEDORA"
                },
                "approved": None,
                "builds": [
                    {
                        "nvr": "gnome-settings-daemon-3.6.1-1.fc18",
                        "package": {
                            "suggest_reboot": False,
                            "committers": [
                                "hadess",
                                "ofourdan",
                                "mkasik",
                                "cosimoc"
                            ],
                            "name": "gnome-settings-daemon"
                        }
                    }, {
                        "nvr": "control-center-3.6.1-1.fc18",
                        "package": {
                            "suggest_reboot": False,
                            "committers": [
                                "ctrl-center-team",
                                "ofourdan",
                                "ssp",
                                "ajax",
                                "alexl",
                                "jrb",
                                "mbarnes",
                                "caolanm",
                                "davidz",
                                "mclasen",
                                "rhughes",
                                "hadess",
                                "johnp",
                                "caillon",
                                "whot",
                                "rstrode"
                            ],
                            "name": "control-center"
                        }
                    }
                ],
                "date_modified": None,
                "notes": "This update fixes numerous bugs in the new Input " +
                "Sources support, the Network panel and adds a help " +
                "screen accessible via Wacom tablets's buttons.",
                "request": "testing",
                "bugs": [],
                "critpath_approved": False,
                "karma": 0,
                "submitter": "hadess"
            }
        },
        "i": 2,
        "timestamp": 1349718539.0,
    }


class TestBodhiUpdateEject(Base):
    """ The `Bodhi Updates System <https://bodhi.fedoraproject.org>`_
    publishes messages on this topic whenever an update
    **is ejected from the mash** due to some failure:
    """
    expected_title = "bodhi.update.eject"
    expected_subti = "ralph's fedmsg-0.2.7-2.el6 bodhi update " + \
        "was ejected from the test_repo mash.  Reason: \"some reason\""
    expected_link = "https://bodhi.fedoraproject.org/updates/" + \
        "fedmsg-0.2.7-2.el6"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c" + \
        "?s=64&d=retro"
    expected_usernames = set(['ralph'])
    expected_packages = set(['fedmsg'])
    expected_objects = set(['packages/fedmsg'])

    msg = {
        "i": 88,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.bodhi.update.eject",
        "msg": {
            "update": {
                "title": "fedmsg-0.2.7-2.el6",
                "submitter": {
                    "name": "ralph",
                },
                "status": "testing",
            },
            "reason": "some reason",
            "release": {
                "dist_tag": "el6",
                "locked": True,
                "long_name": "Fedora EPEL 6",
                "name": "EL6",
            },
            "request": "testing",
            "repo": "test_repo",
        }
    }


class TestLegacy2015BodhiUpdateComplete(Base):
    """ The `Bodhi Updates System <https://bodhi.fedoraproject.org>`_
    publishes messages on this topic whenever an update
    **completes it's push to the testing repository**.  Here's a
    straightforward example from 2015:
    """
    expected_title = "bodhi.update.complete.testing"
    expected_subti = "ralph's fedmsg-0.2.7-2.el6 bodhi update " + \
        "completed push to testing"
    expected_link = "https://bodhi.fedoraproject.org/updates/" + \
        "fedmsg-0.2.7-2.el6"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c" + \
        "?s=64&d=retro"
    expected_usernames = set(['ralph'])
    expected_packages = set(['fedmsg'])
    expected_objects = set(['packages/fedmsg'])

    msg = {
        "i": 88,
        "timestamp": 1344447839.891876,
        "topic": "org.fedoraproject.prod.bodhi.update.complete.testing",
        "msg": {
            "update": {
                "title": "fedmsg-0.2.7-2.el6",
                "submitter": {
                    "name": "ralph",
                },
                "status": "testing",
            }
        }
    }


class TestBodhi4UpdateComplete(Base):
    """ The `Bodhi Updates System <https://bodhi.fedoraproject.org>`_
    publishes messages on this topic whenever an update
    **completes its push to the testing repository**.
    """
    expected_title = "bodhi.update.complete.testing"
    expected_subti = "kkeithle's nfs-ganesha-2.7.4-1.fc29 bodhi update " + \
        "completed push to testing"
    expected_link = "https://bodhi.fedoraproject.org/updates/" + \
        "FEDORA-2019-02cd019281"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "d5ddbcc278179315e29a84b4b8f77b055f4d745c5091a3b7460edbf02b5ce810" + \
        "?s=64&d=retro"
    expected_usernames = set(['kkeithle', 'composer'])
    expected_packages = set(['nfs-ganesha'])
    expected_objects = set(['packages/nfs-ganesha'])

    msg = {
      "username": "amqp-bridge",
      "source_name": "datanommer",
      "i": 184693,
      "timestamp": 1559791912.0,
      "msg_id": "2019-92fe5e1a-2c84-4251-ba4b-e06ccea43204",
      "crypto": "x509",
      "topic": "org.fedoraproject.prod.bodhi.update.complete.testing",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "update": {
          "date_testing": "2019-06-06 03:31:44",
          "pushed": True,
          "require_testcases": True,
          "date_stable": None,
          "critpath": False,
          "date_approved": None,
          "stable_karma": 3,
          "compose": {
            "release_id": 23,
            "checkpoints": "{\"determine_and_perform_tag_actions\": true, \"completed_repo\": \"/mnt/koji/compose/updates/Fedora-29-updates-testing-20190606.0\", \"compose_done\": true}",
            "update_summary": [
              {
                "alias": "FEDORA-2019-33649e2e64",
                "title": "phpMyAdmin-4.9.0.1-1.fc29 and php-phpmyadmin-sql-parser-4.3.2-1.fc29"
              },
              {
                "alias": "FEDORA-2019-22afc255f6",
                "title": "python-metakernel-0.24.2-1.fc29"
              },
              {
                "alias": "FEDORA-2019-9b446c7753",
                "title": "container-exception-logger-1.0.3-1.fc29"
              },
              {
                "alias": "FEDORA-2019-e0e0f86a69",
                "title": "compose-utils-0.1.31-1.fc29"
              },
              {
                "alias": "FEDORA-2019-3082237808",
                "title": "earlyoom-1.3-2.fc29"
              },
              {
                "alias": "FEDORA-2019-6dd7e722b7",
                "title": "php-twig2-2.11.2-1.fc29"
              },
              {
                "alias": "FEDORA-2019-82ce29e885",
                "title": "quilter-1.9.0-1.20190605git076ac9e.fc29"
              },
              {
                "alias": "FEDORA-2019-847fc9fe3d",
                "title": "perl-PPIx-QuoteLike-0.007-1.fc29"
              },
              {
                "alias": "FEDORA-2019-e0b72241c2",
                "title": "perl-podlators-4.12-1.fc29"
              },
              {
                "alias": "FEDORA-2019-cd8f4b9568",
                "title": "pam-u2f-1.0.8-1.fc29"
              },
              {
                "alias": "FEDORA-2019-ef33a4a25e",
                "title": "python-alembic-1.0.10-1.fc29"
              },
              {
                "alias": "FEDORA-2019-5acf586a26",
                "title": "js-jquery-file-upload-9.31.0-1.fc29"
              },
              {
                "alias": "FEDORA-2019-a171291a47",
                "title": "js-jquery-jstree-3.3.8-1.fc29"
              },
              {
                "alias": "FEDORA-2019-dadaa4c756",
                "title": "flat-remix-theme-0.0.20190604-1.fc29"
              },
              {
                "alias": "FEDORA-2019-5b2fcc8f10",
                "title": "gnome-chemistry-utils-0.14.17-17.fc29, gnumeric-1.12.45-1.fc29, and 1 more"
              },
              {
                "alias": "FEDORA-2019-492d24f0ef",
                "title": "kernel-5.1.7-200.fc29 and kernel-headers-5.1.7-200.fc29"
              },
              {
                "alias": "FEDORA-2019-24ba1d4ba0",
                "title": "mozilla-iot-gateway-0.8.1-2.fc29"
              },
              {
                "alias": "FEDORA-2019-909d49ad06",
                "title": "flrig-1.3.45-1.fc29"
              },
              {
                "alias": "FEDORA-2019-e77f7dbb32",
                "title": "python38-3.8.0~b1-1.fc29"
              },
              {
                "alias": "FEDORA-2019-dbe5dc1939",
                "title": "python-giacpy-0.6.8-1.fc29"
              },
              {
                "alias": "FEDORA-2019-6bc7635438",
                "title": "libntirpc-1.7.4-1.fc29"
              },
              {
                "alias": "FEDORA-2019-02cd019281",
                "title": "nfs-ganesha-2.7.4-1.fc29"
              }
            ],
            "error_message": None,
            "request": "testing",
            "state": "notifying",
            "state_date": "2019-06-06 03:31:44",
            "content_type": "rpm",
            "release": {
              "dist_tag": "f29",
              "name": "F29",
              "composed_by_bodhi": True,
              "pending_stable_tag": "f29-updates-pending",
              "mail_template": "fedora_errata_template",
              "long_name": "Fedora 29",
              "state": "current",
              "version": "29",
              "override_tag": "f29-override",
              "branch": "f29",
              "id_prefix": "FEDORA",
              "pending_signing_tag": "f29-signing-pending",
              "pending_testing_tag": "f29-updates-testing-pending",
              "testing_tag": "f29-updates-testing",
              "stable_tag": "f29-updates",
              "candidate_tag": "f29-updates-candidate"
            },
            "date_created": "2019-06-06 00:00:04",
            "security": True
          },
          "display_name": "",
          "severity": "unspecified",
          "autokarma": True,
          "title": "nfs-ganesha-2.7.4-1.fc29",
          "suggest": "unspecified",
          "require_bugs": True,
          "comments": [
            {
              "bug_feedback": [],
              "user_id": 91,
              "timestamp": "2019-06-05 22:27:12",
              "text": "This update has been submitted for testing by kkeithle. ",
              "karma_critpath": 0,
              "update_id": 140681,
              "karma": 0,
              "testcase_feedback": [],
              "id": 955821,
              "user": {
                "openid": None,
                "name": "bodhi",
                "email": None,
                "avatar": None,
                "groups": [],
                "id": 91
              }
            },
            {
              "bug_feedback": [],
              "user_id": 91,
              "timestamp": "2019-06-05 22:27:12",
              "text": "This update test gating status has been changed to 'waiting'.",
              "karma_critpath": 0,
              "update_id": 140681,
              "karma": 0,
              "testcase_feedback": [],
              "id": 955822,
              "user": {
                "openid": None,
                "name": "bodhi",
                "email": None,
                "avatar": None,
                "groups": [],
                "id": 91
              }
            },
            {
              "bug_feedback": [],
              "user_id": 91,
              "timestamp": "2019-06-05 22:27:14",
              "text": "This update test gating status has been changed to 'ignored'.",
              "karma_critpath": 0,
              "update_id": 140681,
              "karma": 0,
              "testcase_feedback": [],
              "id": 955823,
              "user": {
                "openid": None,
                "name": "bodhi",
                "email": None,
                "avatar": None,
                "groups": [],
                "id": 91
              }
            }
          ],
          "test_gating_status": "ignored",
          "updateid": "FEDORA-2019-02cd019281",
          "test_cases": [],
          "close_bugs": False,
          "meets_testing_requirements": False,
          "date_submitted": "2019-06-05 22:27:12",
          "unstable_karma": -3,
          "date_pushed": "2019-06-06 03:31:44",
          "user": {
            "openid": None,
            "name": "kkeithle",
            "email": "kkeithle@redhat.com",
            "avatar": None,
            "groups": [
              {
                "name": "packager"
              }
            ],
            "id": 380
          },
          "content_type": "rpm",
          "requirements": "",
          "locked": True,
          "builds": [
            {
              "epoch": 0,
              "release_id": 23,
              "type": "rpm",
              "nvr": "nfs-ganesha-2.7.4-1.fc29",
              "signed": True
            }
          ],
          "date_modified": None,
          "url": "https://bodhi.fedoraproject.org/updates/FEDORA-2019-02cd019281",
          "type": "bugfix",
          "notes": "nfs-ganesha 2.7.4 GA",
          "request": "testing",
          "bugs": [],
          "alias": "FEDORA-2019-02cd019281",
          "status": "testing",
          "karma": 0,
          "release": {
            "dist_tag": "f29",
            "mail_template": "fedora_errata_template",
            "name": "F29",
            "composed_by_bodhi": True,
            "pending_stable_tag": "f29-updates-pending",
            "composes": [
              {
                "release_id": 23,
                "checkpoints": "{\"determine_and_perform_tag_actions\": true, \"completed_repo\": \"/mnt/koji/compose/updates/Fedora-29-updates-testing-20190606.0\", \"compose_done\": true}",
                "update_summary": [
                  {
                    "alias": "FEDORA-2019-33649e2e64",
                    "title": "phpMyAdmin-4.9.0.1-1.fc29 and php-phpmyadmin-sql-parser-4.3.2-1.fc29"
                  },
                  {
                    "alias": "FEDORA-2019-22afc255f6",
                    "title": "python-metakernel-0.24.2-1.fc29"
                  },
                  {
                    "alias": "FEDORA-2019-9b446c7753",
                    "title": "container-exception-logger-1.0.3-1.fc29"
                  },
                  {
                    "alias": "FEDORA-2019-e0e0f86a69",
                    "title": "compose-utils-0.1.31-1.fc29"
                  },
                  {
                    "alias": "FEDORA-2019-3082237808",
                    "title": "earlyoom-1.3-2.fc29"
                  },
                  {
                    "alias": "FEDORA-2019-6dd7e722b7",
                    "title": "php-twig2-2.11.2-1.fc29"
                  },
                  {
                    "alias": "FEDORA-2019-82ce29e885",
                    "title": "quilter-1.9.0-1.20190605git076ac9e.fc29"
                  },
                  {
                    "alias": "FEDORA-2019-847fc9fe3d",
                    "title": "perl-PPIx-QuoteLike-0.007-1.fc29"
                  },
                  {
                    "alias": "FEDORA-2019-e0b72241c2",
                    "title": "perl-podlators-4.12-1.fc29"
                  },
                  {
                    "alias": "FEDORA-2019-cd8f4b9568",
                    "title": "pam-u2f-1.0.8-1.fc29"
                  },
                  {
                    "alias": "FEDORA-2019-ef33a4a25e",
                    "title": "python-alembic-1.0.10-1.fc29"
                  },
                  {
                    "alias": "FEDORA-2019-5acf586a26",
                    "title": "js-jquery-file-upload-9.31.0-1.fc29"
                  },
                  {
                    "alias": "FEDORA-2019-a171291a47",
                    "title": "js-jquery-jstree-3.3.8-1.fc29"
                  },
                  {
                    "alias": "FEDORA-2019-dadaa4c756",
                    "title": "flat-remix-theme-0.0.20190604-1.fc29"
                  },
                  {
                    "alias": "FEDORA-2019-5b2fcc8f10",
                    "title": "gnome-chemistry-utils-0.14.17-17.fc29, gnumeric-1.12.45-1.fc29, and 1 more"
                  },
                  {
                    "alias": "FEDORA-2019-492d24f0ef",
                    "title": "kernel-5.1.7-200.fc29 and kernel-headers-5.1.7-200.fc29"
                  },
                  {
                    "alias": "FEDORA-2019-24ba1d4ba0",
                    "title": "mozilla-iot-gateway-0.8.1-2.fc29"
                  },
                  {
                    "alias": "FEDORA-2019-909d49ad06",
                    "title": "flrig-1.3.45-1.fc29"
                  },
                  {
                    "alias": "FEDORA-2019-e77f7dbb32",
                    "title": "python38-3.8.0~b1-1.fc29"
                  },
                  {
                    "alias": "FEDORA-2019-dbe5dc1939",
                    "title": "python-giacpy-0.6.8-1.fc29"
                  },
                  {
                    "alias": "FEDORA-2019-6bc7635438",
                    "title": "libntirpc-1.7.4-1.fc29"
                  },
                  {
                    "alias": "FEDORA-2019-02cd019281",
                    "title": "nfs-ganesha-2.7.4-1.fc29"
                  }
                ],
                "error_message": None,
                "request": "testing",
                "state": "notifying",
                "state_date": "2019-06-06 03:31:44",
                "content_type": "rpm",
                "date_created": "2019-06-06 00:00:04",
                "security": True
              }
            ],
            "long_name": "Fedora 29",
            "state": "current",
            "version": "29",
            "override_tag": "f29-override",
            "branch": "f29",
            "id_prefix": "FEDORA",
            "pending_signing_tag": "f29-signing-pending",
            "pending_testing_tag": "f29-updates-testing-pending",
            "testing_tag": "f29-updates-testing",
            "stable_tag": "f29-updates",
            "candidate_tag": "f29-updates-candidate"
          }
        },
        "agent": "composer"
      }
    }

class TestBodhiRequestMultiplePackagesPerUpdate(Base):
    """ The `Bodhi Updates System <https://bodhi.fedoraproject.org>`_
    publishes messages on this topic whenever a *user* requests that an update
    be pushed to the testing repository. Some updates may contain *multiple
    packages*, which can be a little tricky if you're not ready for it.  Here's
    an example of that:
    """
    expected_title = "bodhi.update.request.testing"
    expected_subti = "lmacken submitted " + \
        "gnome-settings-daemon-3.6.1-1.fc18 contr..." + \
        " to testing"
    expected_link = "https://bodhi.fedoraproject.org/updates/" + \
        "gnome-settings-daemon-3.6.1-1.fc18 control-center-3.6.1-1.fc18"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "0d574577afa8deac19df2673cdea9aef45549ff8fac798ddaba61541c69e185a?s=64&d=retro"
    expected_usernames = set(['lmacken', 'hadess'])
    expected_packages = set(['gnome-settings-daemon', 'control-center'])
    expected_objects = set([
        'packages/gnome-settings-daemon',
        'packages/control-center',
    ])

    msg = {
        "topic": "org.fedoraproject.prod.bodhi.update.request.testing",
        "msg": {
            'agent': 'lmacken',
            "update": {
                "status": "pending",
                "critpath": False,
                "stable_karma": 3,
                "date_pushed": None,
                "title": "gnome-settings-daemon-3.6.1-1.fc18 " +
                "control-center-3.6.1-1.fc18",
                "nagged": None,
                "comments": [
                    {
                        "group": None,
                        "author": "bodhi",
                        "text": "This update has been submitted for "
                        "testing by hadess. ",
                        "karma": 0,
                        "anonymous": False,
                        "timestamp": 1349718539.0,
                        "update_title": "gnome-settings-daemon-3.6.1-1.fc18 " +
                        "control-center-3.6.1-1.fc18"
                    }
                ],
                "updateid": None,
                "type": "bugfix",
                "close_bugs": True,
                "date_submitted": 1349718534.0,
                "unstable_karma": -3,
                "release": {
                    "dist_tag": "f18",
                    "locked": True,
                    "long_name": "Fedora 18",
                    "name": "F18",
                    "id_prefix": "FEDORA"
                },
                "approved": None,
                "builds": [
                    {
                        "nvr": "gnome-settings-daemon-3.6.1-1.fc18",
                        "package": {
                            "suggest_reboot": False,
                            "committers": [
                                "hadess",
                                "ofourdan",
                                "mkasik",
                                "cosimoc"
                            ],
                            "name": "gnome-settings-daemon"
                        }
                    }, {
                        "nvr": "control-center-3.6.1-1.fc18",
                        "package": {
                            "suggest_reboot": False,
                            "committers": [
                                "ctrl-center-team",
                                "ofourdan",
                                "ssp",
                                "ajax",
                                "alexl",
                                "jrb",
                                "mbarnes",
                                "caolanm",
                                "davidz",
                                "mclasen",
                                "rhughes",
                                "hadess",
                                "johnp",
                                "caillon",
                                "whot",
                                "rstrode"
                            ],
                            "name": "control-center"
                        }
                    }
                ],
                "date_modified": None,
                "notes": "This update fixes numerous bugs in the new Input " +
                "Sources support, the Network panel and adds a help " +
                "screen accessible via Wacom tablets's buttons.",
                "request": "testing",
                "bugs": [],
                "critpath_approved": False,
                "karma": 0,
                "submitter": "hadess"
            }
        },
        "i": 2,
        "timestamp": 1349718539.0,
    }


class TestLegacyBodhi2MashTaskStart(Base):
    """ The `Bodhi 2 Masher <https://bodhi.fedoraproject.org>`_
    published messages on this topic whenever it **began** its work.
    Since Bodhi 4.0, this topic is replaced by compose.start.
    """
    expected_title = "bodhi.mashtask.start"
    expected_subti = "bodhi masher started a push"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = expected_icon
    expected_packages = set([])

    msg = {
        'topic': "org.fedoraproject.prod.bodhi.mashtask.start",
        'msg': {}
    }


class TestLegacyBodhi2MashTaskMashing(Base):
    """ The `Bodhi 2 Masher <https://bodhi.fedoraproject.org>`_
    published messages on this topic whenever it started mashing
    a particular repository. Since Bodhi 4.0, this topic is replaced
    by compose.composing.
    """
    expected_title = "bodhi.mashtask.mashing"
    expected_subti = "bodhi masher started mashing test_repo"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = expected_icon
    expected_packages = set([])
    expected_objects = set(['repos/test_repo'])

    msg = {
        'topic': "org.fedoraproject.prod.bodhi.mashtask.mashing",
        'msg': {
            'repo': 'test_repo',
            'updates': [
            ],
        },
    }


class TestLegacyBodhi2MashTaskSyncWaitStart(Base):
    """ The `Bodhi 2 Masher <https://bodhi.fedoraproject.org>`_
    publishes messages on this topic when it began **waiting to sync**.
    Since Bodhi 4.0, this topic is replaced by compose.sync.wait.
    """
    expected_title = "bodhi.mashtask.sync.wait"
    expected_subti = "bodhi masher is waiting for test_repo " + \
        "to hit the master mirror"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = expected_icon
    expected_packages = set([])
    expected_objects = set(['repos/test_repo'])

    msg = {
        'topic': "org.fedoraproject.prod.bodhi.mashtask.sync.wait",
        'msg': {'repo': 'test_repo'}
    }


class TestLegacyBodhi2MashTaskSyncWaitDone(Base):
    """ The `Bodhi 2 Masher <https://bodhi.fedoraproject.org>`_
    published messages on this topic when it finished syncing. Since
    Bodhi 4.0, this topic is replaced by compose.sync.done.
    """
    expected_title = "bodhi.mashtask.sync.done"
    expected_subti = "bodhi masher finished waiting for test_repo " + \
        "to hit the master mirror"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = expected_icon
    expected_packages = set([])
    expected_objects = set(['repos/test_repo'])

    msg = {
        'topic': "org.fedoraproject.prod.bodhi.mashtask.sync.done",
        'msg': {'repo': 'test_repo'}
    }


class TestLegacyBodhi2MashTaskComplete(Base):
    """ The `Bodhi 2 Masher <https://bodhi.fedoraproject.org>`_
    published messages on this topic whenever it **finished** its work.
    Since Bodhi 4.0, this topic is replaced by compose.complete.
    """
    expected_title = "bodhi.mashtask.complete"
    expected_subti = "bodhi masher failed to mash test_repo"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = expected_icon
    expected_packages = set([])
    expected_objects = set(['repos/test_repo'])

    msg = {
        'topic': "org.fedoraproject.prod.bodhi.mashtask.complete",
        'msg': {'success': False, 'repo': 'test_repo'}
    }


class TestLegacyBodhi3MashTaskStart(Base):
    """ The `Bodhi 3 Masher <https://bodhi.fedoraproject.org>`_
    published messages on this topic whenever it **began** its work.
    Since Bodhi 4.0, this topic is replaced by compose.start.
    """
    expected_title = "bodhi.mashtask.start"
    expected_subti = "bodhi masher started a push"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "05b5fce36707d3f962a8dc03094e41028ac3e765c8c2e182eab96228013ec9c9" + \
        "?s=64&d=retro"
    expected_usernames = set(['releng'])
    expected_packages = set([])

    msg = {
      "username": "apache",
      "source_name": "datanommer",
      "i": 6,
      "timestamp": 1559001608.0,
      "msg_id": "2019-1139e89d-ca7e-4ec1-933f-3bbf47323cf3",
      "crypto": "x509",
      "topic": "org.fedoraproject.prod.bodhi.mashtask.start",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "agent": "releng"
      }
    }


class TestLegacyBodhi3MashTaskMashing(Base):
    """ The `Bodhi 3 Masher <https://bodhi.fedoraproject.org>`_
    published messages on this topic whenever it started mashing
    a particular repository. Since Bodhi 4.0, this topic is replaced
    by compose.composing.
    """
    expected_title = "bodhi.mashtask.mashing"
    expected_subti = "bodhi masher started mashing f29-modular-updates-testing"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "05b5fce36707d3f962a8dc03094e41028ac3e765c8c2e182eab96228013ec9c9" + \
        "?s=64&d=retro"
    expected_usernames = set(['releng'])
    expected_packages = set([])
    expected_objects = set(['repos/f29-modular-updates-testing'])

    msg = {
      "username": "apache",
      "source_name": "datanommer",
      "i": 1,
      "timestamp": 1559011832.0,
      "msg_id": "2019-aa0f318e-667a-4119-ba16-ac7433244a39",
      "crypto": "x509",
      "topic": "org.fedoraproject.prod.bodhi.mashtask.mashing",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "repo": "f29-modular-updates-testing",
        "ctype": "module",
        "agent": "releng",
        "updates": [
          "nodejs-12-2920190525130817.6c81f848",
          "cri-o-1.14-2920190527085840.6c81f848"
        ]
      }
    }


class TestLegacyBodhi3MashTaskSyncWaitStart(Base):
    """ The `Bodhi 3 Masher <https://bodhi.fedoraproject.org>`_
    publishes messages on this topic when it began **waiting to sync**.
    Since Bodhi 4.0, this topic is replaced by compose.sync.wait.
    """
    expected_title = "bodhi.mashtask.sync.wait"
    expected_subti = "bodhi masher is waiting for f29-updates-testing " + \
        "to hit the master mirror"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "05b5fce36707d3f962a8dc03094e41028ac3e765c8c2e182eab96228013ec9c9" + \
        "?s=64&d=retro"
    expected_usernames = set(['releng'])
    expected_packages = set([])
    expected_objects = set(['repos/f29-updates-testing'])

    msg = {
      "username": "apache",
      "source_name": "datanommer",
      "i": 3,
      "timestamp": 1559015188.0,
      "msg_id": "2019-85429560-ab56-41b7-9c3d-2004630974ed",
      "crypto": "x509",
      "topic": "org.fedoraproject.prod.bodhi.mashtask.sync.wait",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "repo": "f29-updates-testing",
        "agent": "releng"
      }
    }


class TestLegacyBodhi3MashTaskSyncWaitDone(Base):
    """ The `Bodhi 3 Masher <https://bodhi.fedoraproject.org>`_
    published messages on this topic when it finished syncing. Since
    Bodhi 4.0, this topic is replaced by compose.sync.done.
    """
    expected_title = "bodhi.mashtask.sync.done"
    expected_subti = "bodhi masher finished waiting for f29-updates-testing " + \
        "to hit the master mirror"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "05b5fce36707d3f962a8dc03094e41028ac3e765c8c2e182eab96228013ec9c9" + \
        "?s=64&d=retro"
    expected_usernames = set(['releng'])
    expected_packages = set([])
    expected_objects = set(['repos/f29-updates-testing'])

    msg = {
      "username": "apache",
      "source_name": "datanommer",
      "i": 4,
      "timestamp": 1559015388.0,
      "msg_id": "2019-022e4d9a-7af2-41bb-901d-14e0808718cc",
      "crypto": "x509",
      "topic": "org.fedoraproject.prod.bodhi.mashtask.sync.done",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "repo": "f29-updates-testing",
        "agent": "releng"
      }
    }


class TestLegacyBodhi3MashTaskComplete(Base):
    """ The `Bodhi 3 Masher <https://bodhi.fedoraproject.org>`_
    published messages on this topic whenever it **finished** its work.
    Since Bodhi 4.0, this topic is replaced by compose.complete.
    """
    expected_title = "bodhi.mashtask.complete"
    expected_subti = "bodhi masher successfully mashed f29-updates-testing"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "05b5fce36707d3f962a8dc03094e41028ac3e765c8c2e182eab96228013ec9c9" + \
        "?s=64&d=retro"
    expected_usernames = set(['releng'])
    expected_packages = set([])
    expected_objects = set(['repos/f29-updates-testing'])

    msg = {
      "username": "apache",
      "source_name": "datanommer",
      "i": 37,
      "timestamp": 1559015442.0,
      "msg_id": "2019-dc8c2696-cddc-4e40-87cc-ea5fe25396dd",
      "crypto": "x509",
      "topic": "org.fedoraproject.prod.bodhi.mashtask.complete",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "repo": "f29-updates-testing",
        "success": True,
        "ctype": "rpm",
        "agent": "releng"
      }
    }


class TestBodhi4ComposeStart(Base):
    """ `Bodhi <https://bodhi.fedoraproject.org>`_ publishes messages
    on this topic whenever it **begins** a compose run.
    """
    expected_title = "bodhi.compose.start"
    expected_subti = "bodhi composer started a run"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "05b5fce36707d3f962a8dc03094e41028ac3e765c8c2e182eab96228013ec9c9" + \
        "?s=64&d=retro"
    expected_usernames = set(['releng'])
    expected_packages = set([])

    msg = {
      "username": "amqp-bridge",
      "source_name": "datanommer",
      "i": 185446,
      "timestamp": 1559865606.0,
      "msg_id": "2019-6724c4b9-b954-4263-b305-7dcdd69c361b",
      "crypto": "x509",
      "topic": "org.fedoraproject.prod.bodhi.compose.start",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "agent": "releng"
      }
    }


class TestBodhi4ComposeComposing(Base):
    """ `Bodhi <https://bodhi.fedoraproject.org>`_ publishes messages
    on this topic whenever it starts composing a particular repository.
    """
    expected_title = "bodhi.compose.composing"
    expected_subti = "bodhi rpm compose of repo dist-6E-epel-testing started"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "05b5fce36707d3f962a8dc03094e41028ac3e765c8c2e182eab96228013ec9c9" + \
        "?s=64&d=retro"
    expected_usernames = set(['releng'])
    expected_packages = set([])
    expected_objects = set(['repos/dist-6E-epel-testing'])

    msg = {
      "username": "amqp-bridge",
      "source_name": "datanommer",
      "i": 185680,
      "timestamp": 1559871419.0,
      "msg_id": "2019-9fbd5994-15d2-40f6-a4f3-8d0bc0e37c08",
      "crypto": "x509",
      "topic": "org.fedoraproject.prod.bodhi.compose.composing",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "repo": "dist-6E-epel-testing",
        "ctype": "rpm",
        "agent": "releng",
        "updates": [
          "sec-2.8.2-1.el6"
        ]
      }
    }


class TestBodhi4ComposeSyncWait(Base):
    """ `Bodhi <https://bodhi.fedoraproject.org>`_ publishes messages
    on this topic when it begins waiting for a completed repo to sync.
    """
    expected_title = "bodhi.compose.sync.wait"
    expected_subti = "bodhi composer is waiting for dist-6E-epel-testing " + \
        "to hit the master mirror"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "05b5fce36707d3f962a8dc03094e41028ac3e765c8c2e182eab96228013ec9c9" + \
        "?s=64&d=retro"
    expected_usernames = set(['releng'])
    expected_packages = set([])
    expected_objects = set(['repos/dist-6E-epel-testing'])

    msg = {
      "username": "amqp-bridge",
      "source_name": "datanommer",
      "i": 185683,
      "timestamp": 1559871586.0,
      "msg_id": "2019-39734cc4-d3bd-4961-8303-502e45e6777b",
      "crypto": "x509",
      "topic": "org.fedoraproject.prod.bodhi.compose.sync.wait",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "repo": "dist-6E-epel-testing",
        "agent": "releng"
      }
    }


class TestBodhi4ComposeSyncDone(Base):
    """ `Bodhi <https://bodhi.fedoraproject.org>`_ publishes messages
    on this topic when a completed repo finishes syncing.
    """
    expected_title = "bodhi.compose.sync.done"
    expected_subti = "bodhi composer finished waiting for dist-6E-epel-testing " + \
        "to hit the master mirror"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "05b5fce36707d3f962a8dc03094e41028ac3e765c8c2e182eab96228013ec9c9" + \
        "?s=64&d=retro"
    expected_usernames = set(['releng'])
    expected_packages = set([])
    expected_objects = set(['repos/dist-6E-epel-testing'])

    msg = {
      "username": "amqp-bridge",
      "source_name": "datanommer",
      "i": 185684,
      "timestamp": 1559871787.0,
      "msg_id": "2019-ab499c10-4665-475b-b4b5-483c81a61a60",
      "crypto": "x509",
      "topic": "org.fedoraproject.prod.bodhi.compose.sync.done",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "repo": "dist-6E-epel-testing",
        "agent": "releng"
      }
    }


class TestBodhi4ComposeComplete(Base):
    """ `Bodhi <https://bodhi.fedoraproject.org>`_ publishes this kind
    of message when it completes the full compose run for a repository.
    """
    expected_title = "bodhi.compose.complete"
    expected_subti = "bodhi rpm compose of repo f29-updates-testing succeeded"
    expected_link = "https://bodhi.fedoraproject.org"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "05b5fce36707d3f962a8dc03094e41028ac3e765c8c2e182eab96228013ec9c9" + \
        "?s=64&d=retro"
    expected_usernames = set(['releng'])
    expected_packages = set([])
    expected_objects = set(['repos/f29-updates-testing'])

    msg = {
      "username": "amqp-bridge",
      "source_name": "datanommer",
      "i": 184694,
      "timestamp": 1559791936.0,
      "msg_id": "2019-e43eb49a-b0da-4fb9-88e9-ef3f5eebc97d",
      "crypto": "x509",
      "topic": "org.fedoraproject.prod.bodhi.compose.complete",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "repo": "f29-updates-testing",
        "success": True,
        "ctype": "rpm",
        "agent": "releng"
      }
    }


class TestBodhiRepoDone(Base):
    """ `Bodhi <https://bodhi.fedoraproject.org>`_ publishes this kind
    of message when a repo is created and ready to be signed or
    otherwise processed. It actually occurs between compose.composing
    and compose.sync.wait in the overall compose workflow. The format
    has not changed between Bodhi 3 and Bodhi 4; the Bodhi 1/2 version
    likely didn't have an 'agent' but was otherwise the same.
    """
    expected_title = "bodhi.repo.done"
    expected_subti = "bodhi repo f29-updates-testing created"
    expected_link = "https://bodhi.fedoraproject.org"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "05b5fce36707d3f962a8dc03094e41028ac3e765c8c2e182eab96228013ec9c9" + \
        "?s=64&d=retro"
    expected_usernames = set(['releng'])
    expected_packages = set([])
    expected_objects = set(['repos/f29-updates-testing'])

    msg = {
      "username": "amqp-bridge",
      "source_name": "datanommer",
      "i": 185742,
      "timestamp": 1559883894.0,
      "msg_id": "2019-139ee383-4b15-4ba5-87c1-e366c182bb64",
      "crypto": "x509",
      "topic": "org.fedoraproject.prod.bodhi.repo.done",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "repo": "f29-updates-testing",
        "path": "/mnt/koji/compose/updates/Fedora-29-updates-testing-20190607.0",
        "agent": "releng"
      }
    }


class TestBodhiRequestUnpush(Base):
    """ The `Bodhi Updates System <https://bodhi.fedoraproject.org>`_
    publishes messages on this topic whenever a *user* requests that an update
    be **unpushed**.
    """
    expected_title = "bodhi.update.request.unpush"
    expected_subti = "lmacken unpushed foo"
    expected_link = "https://bodhi.fedoraproject.org/updates/foo"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "203f6cb95b44b5d38aa21425b066dd522d3e19d8919cf4b339f29e0ea7f03e9b" + \
        "?s=64&d=retro"
    expected_usernames = set(['lmacken'])
    expected_packages = set(['foo'])
    expected_objects = set(['packages/foo'])

    msg = {
        'topic': "org.fedoraproject.dev.bodhi.update.request.unpush",
        'msg': {
            'agent': 'lmacken',
            'update': {
                'title': 'foo',
                'submitter': 'lmacken',
            },
        },
    }


class TestBodhiRequestObsolete(Base):
    """ The `Bodhi Updates System <https://bodhi.fedoraproject.org>`_
    publishes messages on this topic whenever a *user* requests that an update
    be **obsoleted**.
    """
    expected_title = "bodhi.update.request.obsolete"
    expected_subti = "lmacken obsoleted foo"
    expected_link = "https://bodhi.fedoraproject.org/updates/foo"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "203f6cb95b44b5d38aa21425b066dd522d3e19d8919cf4b339f29e0ea7f03e9b?s=64&d=retro"
    expected_usernames = set(['lmacken'])
    expected_packages = set(['foo'])
    expected_objects = set(['packages/foo'])

    msg = {
        'topic': "org.fedoraproject.dev.bodhi.update.request.obsolete",
        'msg': {
            'agent': 'lmacken',
            'update': {
                'title': 'foo',
                'submitter': 'lmacken',
            },
        },
    }


class TestBodhiRequestStable(Base):
    """ The `Bodhi Updates System <https://bodhi.fedoraproject.org>`_
    publishes messages on this topic whenever a *user* requests that an update
    be marked as **stable**.
    """
    expected_title = "bodhi.update.request.stable"
    expected_subti = "lmacken submitted foo to stable"
    expected_link = "https://bodhi.fedoraproject.org/updates/foo"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "203f6cb95b44b5d38aa21425b066dd522d3e19d8919cf4b339f29e0ea7f03e9b?s=64&d=retro"
    expected_usernames = set(['lmacken'])
    expected_packages = set(['foo'])
    expected_objects = set(['packages/foo'])

    msg = {
        'topic': "org.fedoraproject.dev.bodhi.update.request.stable",
        'msg': {
            'agent': 'lmacken',
            'update': {
                'title': 'foo',
                'submitter': 'lmacken',
            },
        },
    }


class TestBodhiRequestRevoke(Base):
    """ The `Bodhi Updates System <https://bodhi.fedoraproject.org>`_
    publishes messages on this topic whenever a *user* revokes a prior
    request on an update.
    """
    expected_title = "bodhi.update.request.revoke"
    expected_subti = "lmacken revoked foo"
    expected_link = "https://bodhi.fedoraproject.org/updates/foo"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "203f6cb95b44b5d38aa21425b066dd522d3e19d8919cf4b339f29e0ea7f03e9b?s=64&d=retro"
    expected_usernames = set(['lmacken'])
    expected_packages = set(['foo'])
    expected_objects = set(['packages/foo'])

    msg = {
        'topic': "org.fedoraproject.dev.bodhi.update.request.revoke",
        'msg': {
            'agent': 'lmacken',
            'update': {
                'title': 'foo',
                'submitter': 'lmacken',
            },
        },
    }


class TestBodhiRequestTesting(Base):
    """ The `Bodhi Updates System <https://bodhi.fedoraproject.org>`_
    publishes messages on this topic whenever a *user* requests that an
    update be pushed to the testing repository.
    """
    expected_title = "bodhi.update.request.testing"
    expected_subti = "lmacken submitted foo to testing"
    expected_link = "https://bodhi.fedoraproject.org/updates/foo"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "203f6cb95b44b5d38aa21425b066dd522d3e19d8919cf4b339f29e0ea7f03e9b?s=64&d=retro"
    expected_usernames = set(['lmacken'])
    expected_packages = set(['foo'])
    expected_objects = set(['packages/foo'])

    msg = {
        'topic': "org.fedoraproject.dev.bodhi.update.request.testing",
        'msg': {
            'agent': 'lmacken',
            'update': {
                'title': 'foo',
                'submitter': 'lmacken',
            },
        },
    }


class TestLegacy2015BodhiComment(Base):
    """ The `Bodhi Updates System <https://bodhi.fedoraproject.org>`_
    publishes messages on this topic whenever a user **comments** on a bodhi
    update. This is a 2015-era legacy message; I'm not sure precisely what
    Bodhi version would've emitted a message that looks exactly like this.
    """
    expected_title = "bodhi.update.comment"
    expected_subti = "ralph commented on bodhi update fedmsg-1.0-1 (karma: -1)"
    expected_long_form = "Can you believe how much testing we're doing? " + \
        "/cc @codeblock."
    expected_link = "https://bodhi.fedoraproject.org/updates/fedmsg-1.0-1"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro"
    expected_usernames = set(['ralph', 'codeblock'])
    expected_packages = set(['fedmsg'])
    expected_objects = set(['packages/fedmsg'])

    msg = {
        "i": 1,
        "timestamp": 1344344053.2337201,
        "topic": "org.fedoraproject.stg.bodhi.update.comment",
        "msg": {
            "comment": {
                "update_title": "fedmsg-1.0-1",
                "group": None,
                "author": "ralph",
                "text": "Can you believe how much testing we're doing?"
                " /cc @codeblock.",
                "karma": -1,
                "anonymous": False,
                "timestamp": 1344344050.0
            }
        }
    }


class TestBodhi4Comment(Base):
    """ The `Bodhi Updates System <https://bodhi.fedoraproject.org>`_
    publishes messages on this topic whenever a user **comments** on a bodhi
    update.
    """
    expected_title = "bodhi.update.comment"
    expected_subti = "kalev commented on bodhi update xdg-desktop-portal-1.4.2-1.fc30 (karma: 0)"
    expected_long_form = "Note that this depends on pipewire-0.2.6-1.fc30 which is submitted " + \
        "separately. I've turned off autopush so that it doesn't go stable before the " + \
        "required pipewire update."
    expected_link = "https://bodhi.fedoraproject.org/updates/FEDORA-2019-46910daf41"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "e66f540a8e2d93d96cbba97628e82213a8eed237c744f2ce5184d7c9588a8d18?s=64&d=retro"
    expected_usernames = set(['kalev'])
    expected_packages = set(['xdg-desktop-portal'])
    expected_objects = set(['packages/xdg-desktop-portal'])

    msg = {
      "username": "amqp-bridge",
      "source_name": "datanommer",
      "i": 37779,
      "timestamp": 1559062463.0,
      "msg_id": "2019-509f817a-b6d4-4071-909c-a899f8f2002c",
      "crypto": "x509",
      "topic": "org.fedoraproject.prod.bodhi.update.comment",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "comment": {
          "bug_feedback": [],
          "user_id": 285,
          "timestamp": "2019-05-28 16:54:22",
          "author": "kalev",
          "text": "Note that this depends on pipewire-0.2.6-1.fc30 which is submitted separately. I've turned off autopush so that it doesn't go stable before the required pipewire update.",
          "karma_critpath": 0,
          "update": {
            "date_testing": None,
            "pushed": False,
            "require_testcases": True,
            "date_stable": None,
            "critpath": False,
            "date_approved": None,
            "stable_karma": 3,
            "compose": None,
            "display_name": "",
            "severity": "unspecified",
            "autokarma": False,
            "title": "xdg-desktop-portal-1.4.2-1.fc30",
            "suggest": "unspecified",
            "require_bugs": True,
            "test_gating_status": "ignored",
            "type": "enhancement",
            "close_bugs": True,
            "meets_testing_requirements": False,
            "date_submitted": "2019-05-28 16:53:22",
            "unstable_karma": -3,
            "date_pushed": None,
            "user": {
              "openid": None,
              "name": "kalev",
              "email": "klember@redhat.com",
              "avatar": None,
              "groups": [
                {
                  "name": "provenpackager"
                },
                {
                  "name": "packager"
                },
                {
                  "name": "gnome-sig"
                }
              ],
              "id": 285
            },
            "requirements": "",
            "locked": False,
            "builds": [
              {
                "epoch": 0,
                "release_id": 28,
                "type": "rpm",
                "nvr": "xdg-desktop-portal-1.4.2-1.fc30",
                "signed": False
              }
            ],
            "date_modified": None,
            "url": "https://bodhi.fedoraproject.org/updates/FEDORA-2019-46910daf41",
            "notes": "xdg-desktop-portal 1.4.2 release:\n\n - Translation updates\n - inhibit: Implement session state tracking\n - screencast: Allow selecting source types\n - screencast: Support cursor modes\n - Add a background & autostart portal",
            "request": "testing",
            "bugs": [],
            "alias": "FEDORA-2019-46910daf41",
            "status": "pending",
            "karma": 0,
            "release": {
              "dist_tag": "f30",
              "mail_template": "fedora_errata_template",
              "name": "F30",
              "composed_by_bodhi": True,
              "pending_stable_tag": "f30-updates-pending",
              "composes": [],
              "long_name": "Fedora 30",
              "state": "current",
              "version": "30",
              "override_tag": "f30-override",
              "branch": "f30",
              "id_prefix": "FEDORA",
              "pending_signing_tag": "f30-signing-pending",
              "pending_testing_tag": "f30-updates-testing-pending",
              "testing_tag": "f30-updates-testing",
              "stable_tag": "f30-updates",
              "candidate_tag": "f30-updates-candidate"
            }
          },
          "update_alias": "FEDORA-2019-46910daf41",
          "update_id": 140188,
          "karma": 0,
          "testcase_feedback": [],
          "id": 952088,
          "user": {
            "openid": None,
            "name": "kalev",
            "email": "klember@redhat.com",
            "avatar": None,
            "groups": [
              {
                "name": "provenpackager"
              },
              {
                "name": "packager"
              },
              {
                "name": "gnome-sig"
              }
            ],
            "id": 285
          }
        },
        "agent": "kalev"
      }
    }


class TestBodhiOverrideTagged(Base):
    """ The `Bodhi Updates System <https://bodhi.fedoraproject.org>`_
    publishes messages on this topic whenever a user **requests a buildroot
    override** for an update.
    """
    expected_title = "bodhi.buildroot_override.tag"
    expected_subti = "lmacken submitted a buildroot override for fedmsg-1.0-1"
    expected_link = "https://bodhi.fedoraproject.org/overrides/fedmsg-1.0-1"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "203f6cb95b44b5d38aa21425b066dd522d3e19d8919cf4b339f29e0ea7f03e9b?s=64&d=retro"
    expected_usernames = set(['lmacken'])
    expected_packages = set(['fedmsg'])
    expected_objects = set(['packages/fedmsg'])

    msg = {
        "i": 1,
        "timestamp": 1344344053.2337201,
        "topic": "org.fedoraproject.stg.bodhi.buildroot_override.tag",
        "msg": {
            "override": {
                "build": {
                    "nvr": "fedmsg-1.0-1",
                    "override": 1,
                },
                "submitter": {
                    "name": "lmacken",
                },
            }
        }
    }


class LegacyTestBodhiOverrideTagged(Base):
    """ The `Bodhi Updates System <https://bodhi.fedoraproject.org>`_
    publishes messages on this topic whenever a user **requests a buildroot
    override** for an update.
    """
    expected_title = "bodhi.buildroot_override.tag"
    expected_subti = "lmacken submitted a buildroot override for fedmsg-1.0-1"
    expected_link = "https://bodhi.fedoraproject.org/overrides/fedmsg-1.0-1"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "203f6cb95b44b5d38aa21425b066dd522d3e19d8919cf4b339f29e0ea7f03e9b?s=64&d=retro"
    expected_usernames = set(['lmacken'])
    expected_packages = set(['fedmsg'])
    expected_objects = set(['packages/fedmsg'])

    msg = {
        "i": 1,
        "timestamp": 1344344053.2337201,
        "topic": "org.fedoraproject.stg.bodhi.buildroot_override.tag",
        "msg": {
            "override": {
                "build": "fedmsg-1.0-1",
                "submitter": "lmacken",
            }
        }
    }


class TestBodhiOverrideUntagged(Base):
    """ The `Bodhi Updates System <https://bodhi.fedoraproject.org>`_
    publishes messages on this topic whenever a user explicitly removes a
    previously requested buildroot override.
    """
    expected_title = "bodhi.buildroot_override.untag"
    expected_subti = "lmacken expired a buildroot override for fedmsg-1.0-1"
    expected_link = "https://bodhi.fedoraproject.org/overrides/fedmsg-1.0-1"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "203f6cb95b44b5d38aa21425b066dd522d3e19d8919cf4b339f29e0ea7f03e9b?s=64&d=retro"
    expected_usernames = set(['lmacken'])
    expected_packages = set(['fedmsg'])
    expected_objects = set(['packages/fedmsg'])

    msg = {
        "i": 1,
        "timestamp": 1344964395.207541,
        "topic": "org.fedoraproject.stg.bodhi.buildroot_override.untag",
        "msg": {
            "override": {
                "build": {
                    "nvr": "fedmsg-1.0-1",
                    "override": 1,
                },
                "submitter": {
                    "name": "lmacken",
                },
            }
        }
    }



class LegacyTestBodhiOverrideUntagged(Base):
    """ The `Bodhi Updates System <https://bodhi.fedoraproject.org>`_
    publishes messages on this topic whenever a user explicitly removes a
    previously requested buildroot override.
    """
    expected_title = "bodhi.buildroot_override.untag"
    expected_subti = "lmacken expired a buildroot override for fedmsg-1.0-1"
    expected_link = "https://bodhi.fedoraproject.org/overrides/fedmsg-1.0-1"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "203f6cb95b44b5d38aa21425b066dd522d3e19d8919cf4b339f29e0ea7f03e9b?s=64&d=retro"
    expected_usernames = set(['lmacken'])
    expected_packages = set(['fedmsg'])
    expected_objects = set(['packages/fedmsg'])

    msg = {
        "i": 1,
        "timestamp": 1344964395.207541,
        "topic": "org.fedoraproject.stg.bodhi.buildroot_override.untag",
        "msg": {
            "override": {
                "build": "fedmsg-1.0-1",
                "submitter": "lmacken",
            }
        }
    }


class TestLegacyBodhiStackSave(Base):
    """ `Bodhi2 <https://bodhi.fedoraproject.org>`_ introduced the
    concept of *stacks* of packages that can be grouped for to share
    requirements.  That system published messages like this anytime a user
    **modified or created a new stack**. This mechanism was removed from
    Bodhi in January 2019 and exactly one message of this type was ever
    published in production.
    """
    expected_title = "bodhi.stack.save"
    expected_subti = "ralph updated the \"hacking\" stack"
    expected_link = "https://bodhi.fedoraproject.org/stacks/hacking"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c" + \
        "?s=64&d=retro"
    expected_usernames = set(['ralph'])
    expected_packages = set(['nethack'])
    expected_objects = set(['packages/nethack', 'stacks/hacking'])

    msg = {
        "username": "threebean",
        "i": 2,
        "timestamp": 1422302779,
        "msg_id": "2015-21b9ae33-3fdf-42ab-aecb-5717d0d76018",
        "topic": "org.fedoraproject.dev.bodhi.stack.save",
        "msg": {
            "stack": {
                "requirements": "depcheck upgradepath",
                "description": "the greatest game you will ever play",
                "name": "hacking",
                "groups": [],
                "packages": [
                    {
                        "committers": [],
                        "requirements": "depcheck upgradepath",
                        "builds": [],
                        "stack_id": 9,
                        "test_cases": [],
                        "stack": 9,
                        "name": "nethack"
                    }
                ],
                "users": [
                    {
                        "buildroot_overrides": [],
                        "stacks": [
                            1,
                            8,
                            9
                        ],
                        "name": "ralph",
                        "avatar": None
                    }
                ]
            },
            "agent": "ralph"
        }
    }


class TestLegacyBodhiStackDelete(Base):
    """ `Bodhi2 <https://bodhi.fedoraproject.org>`_ introduced the
    concept of *stacks* of packages that can be grouped for to share
    requirements.  That system published messages like this anytime a user
    **deleted a stack**. This mechanism was removed from Bodhi in January
    2019 and no messages of this type were ever published in production.
    """
    expected_title = "bodhi.stack.delete"
    expected_subti = "ralph deleted the \"hacking\" stack"
    expected_link = "https://bodhi.fedoraproject.org/stacks/hacking"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c" + \
        "?s=64&d=retro"
    expected_usernames = set(['ralph'])
    expected_packages = set(['nethack'])
    expected_objects = set(['packages/nethack', 'stacks/hacking'])

    msg = {
        "username": "threebean",
        "i": 2,
        "timestamp": 1422302779,
        "msg_id": "2015-21b9ae33-3fdf-42ab-aecb-5717d0d76018",
        "topic": "org.fedoraproject.dev.bodhi.stack.delete",
        "msg": {
            "stack": {
                "requirements": "depcheck upgradepath",
                "description": "the greatest game you will ever play",
                "name": "hacking",
                "groups": [],
                "packages": [
                    {
                        "committers": [],
                        "requirements": "depcheck upgradepath",
                        "builds": [],
                        "stack_id": 9,
                        "test_cases": [],
                        "stack": 9,
                        "name": "nethack"
                    }
                ],
                "users": [
                    {
                        "buildroot_overrides": [],
                        "stacks": [
                            1,
                            8,
                            9
                        ],
                        "name": "ralph",
                        "avatar": None
                    }
                ]
            },
            "agent": "ralph"
        }
    }


class TestBodhiUpdateEdit(Base):
    """ `Bodhi2 <https://bodhi.fedoraproject.org>`_ publishes
    this kind of message when a package maintainer **edits a pre-existing
    update**.
    """
    expected_title = "bodhi.update.edit"
    expected_subti = "ralph edited tzdata-2014i-1.fc19"
    expected_link = "https://bodhi.fedoraproject.org/updates/" + \
        "tzdata-2014i-1.fc19"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c" + \
        "?s=64&d=retro"
    expected_usernames = set(['ralph'])
    expected_packages = set(['tzdata'])
    expected_objects = set(['packages/tzdata'])
    msg = {
        "username": "apache",
        "timestamp": 1422414175,
        "msg_id": "2015-2b398e44-8012-455f-bfeb-195b9dda18f6",
        "topic": "org.fedoraproject.dev.bodhi.update.edit",
        "msg": {
            "update": {
                "close_bugs": True,
                "old_updateid": None,
                "pushed": False,
                "require_testcases": True,
                "critpath": False,
                "cves": [],
                "stable_karma": 3,
                "date_pushed": None,
                "requirements": "rpmlint",
                "severity": "unspecified",
                "title": "tzdata-2014i-1.fc19",
                "suggest": "unspecified",
                "require_bugs": True,
                "comments": [
                    {
                        "bug_feedback": [],
                        "user_id": 1681,
                        "timestamp": "2015-01-28 03:02:44",
                        "testcase_feedback": [],
                        "karma_critpath": 0,
                        "update": 54046,
                        "update_id": 54046,
                        "karma": 0,
                        "anonymous": False,
                        "text": "ralph edited this update. ",
                        "id": 484236,
                        "user": {
                            "buildroot_overrides": [],
                            "stacks": [],
                            "name": "bodhi",
                            "avatar": None
                        }
                    }
                ],
                "date_approved": None,
                "type": "enhancement",
                "status": "pending",
                "date_submitted": "2014-10-29 20:02:57",
                "unstable_karma": -3,
                "user": {
                    "buildroot_overrides": [],
                    "stacks": [
                        {
                            "requirements": "depcheck upgradepath",
                            "description": "This stack is so hack!",
                            "name": "Hackey",
                            "groups": [],
                            "packages": [],
                            "users": [
                                1711
                            ]
                        },
                    ],
                    "name": "ralph",
                    "avatar": None
                },
                "locked": False,
                "builds": [
                    {
                        "override": None,
                        "nvr": "tzdata-2014i-1.fc19"
                    }
                ],
                "date_modified": "2015-01-28 03:02:55",
                "notes": "the update notes go here...",
                "request": "testing",
                "bugs": [],
                "alias": None,
                "karma": 0,
                "release": {
                    "dist_tag": "f19",
                    "name": "F19",
                    "testing_tag": "f19-updates-testing",
                    "pending_stable_tag": "f19-updates-pending",
                    "long_name": "Fedora 19",
                    "state": "disabled",
                    "version": None,
                    "override_tag": "f19-override",
                    "branch": None,
                    "id_prefix": "FEDORA",
                    "pending_testing_tag": "f19-updates-testing-pending",
                    "stable_tag": "f19-updates",
                    "candidate_tag": "f19-updates-candidate"
                }
            },
            "agent": "ralph"
        }
    }


class TestBodhiKarmaThresholdStable(Base):
    """ `Bodhi2 <https://bodhi.fedoraproject.org>`_ publishes these
    messages when an update reaches the stable or unstable karma thresholds.
    """
    expected_title = "bodhi.update.karma.threshold"
    expected_subti = "tzdata-2014i-1.fc19 reached the stable karma threshold"
    expected_link = "https://bodhi.fedoraproject.org/updates/" + \
        "FEDORA-EPEL-2015-0238"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c" + \
        "?s=64&d=retro"
    expected_usernames = set(['ralph'])
    expected_packages = set(['tzdata'])
    expected_objects = set(['packages/tzdata'])
    msg = {
        "username": "threebean",
        "i": 2,
        "timestamp": 1422302779,
        "msg_id": "2015-21b9ae33-3fdf-42ab-aecb-5717d0d76018",
        "topic": "org.fedoraproject.dev.bodhi.update.karma.threshold",
        "msg": {
            "status": "stable",
            "update": {
                "close_bugs": True,
                "old_updateid": None,
                "pushed": False,
                "require_testcases": True,
                "critpath": False,
                "cves": [],
                "stable_karma": 3,
                "date_pushed": None,
                "requirements": "rpmlint",
                "severity": "unspecified",
                "title": "tzdata-2014i-1.fc19",
                "suggest": "unspecified",
                "require_bugs": True,
                "comments": [
                    {
                        "bug_feedback": [],
                        "user_id": 1681,
                        "timestamp": "2015-01-28 03:02:44",
                        "testcase_feedback": [],
                        "karma_critpath": 0,
                        "update": 54046,
                        "update_id": 54046,
                        "karma": 0,
                        "anonymous": False,
                        "text": "ralph edited this update. ",
                        "id": 484236,
                        "user": {
                            "buildroot_overrides": [],
                            "stacks": [],
                            "name": "bodhi",
                            "avatar": None
                        }
                    }
                ],
                "date_approved": None,
                "type": "enhancement",
                "status": "pending",
                "date_submitted": "2014-10-29 20:02:57",
                "unstable_karma": -3,
                "user": {
                    "buildroot_overrides": [],
                    "stacks": [
                        {
                            "requirements": "depcheck upgradepath",
                            "description": "This stack is so hack!",
                            "name": "Hackey",
                            "groups": [],
                            "packages": [],
                            "users": [
                                1711
                            ]
                        },
                    ],
                    "name": "ralph",
                    "avatar": None
                },
                "locked": False,
                "builds": [
                    {
                        "override": None,
                        "nvr": "tzdata-2014i-1.fc19"
                    }
                ],
                "date_modified": "2015-01-28 03:02:55",
                "notes": "the update notes go here...",
                "request": "testing",
                "bugs": [],
                "alias": "FEDORA-EPEL-2015-0238",
                "karma": 0,
                "release": {
                    "dist_tag": "f19",
                    "name": "F19",
                    "testing_tag": "f19-updates-testing",
                    "pending_stable_tag": "f19-updates-pending",
                    "long_name": "Fedora 19",
                    "state": "disabled",
                    "version": None,
                    "override_tag": "f19-override",
                    "branch": None,
                    "id_prefix": "FEDORA",
                    "pending_testing_tag": "f19-updates-testing-pending",
                    "stable_tag": "f19-updates",
                    "candidate_tag": "f19-updates-candidate"
                }
            },
        }
    }


class TestBodhiUpdateRequirementsMetStable(Base):
    """ `Bodhi2 <https://bodhi.fedoraproject.org>`_ publishes these
    messages when an update reaches the stable testing threshold.
    """
    expected_title = "bodhi.update.requirements_met.stable"
    expected_subti = "python-josepy-1.1.0-1.fc28 reached the stable " + \
        "testing threshold"
    expected_link = "https://bodhi.fedoraproject.org/updates/" + \
        "FEDORA-2018-e1f68e9766"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "c183d834af77a3a5f71c9fc16ee1ce3aba3a279a1fea9a814a5cad4c641a3cdd" + \
        "?s=64&d=retro"
    expected_usernames = set(['elyscape'])
    expected_packages = set(['python-josepy'])
    expected_objects = set(['packages/python-josepy'])
    msg = {
        "username": "bodhi",
        "i": 1,
        "timestamp": 1524333630,
        "msg_id": "2018-a3a06a6c-77da-4093-aafe-1e96a26a74bc",
        "topic": "org.fedoraproject.dev.bodhi.update.requirements_met.stable",
        "msg": {
            "update": {
                "alias": "FEDORA-2018-e1f68e9766",
                "autokarma": True,
                "bugs": [],
                "builds": [
                    {
                        "ci_url": None,
                        "epoch": 0,
                        "nvr": "python-josepy-1.1.0-1.fc28",
                        "release_id": 21,
                        "signed": True,
                        "type": "rpm"
                    }
                ],
                "close_bugs": False,
                "comments": [
                    {
                        "anonymous": False,
                        "bug_feedback": [],
                        "id": 771029,
                        "karma": 0,
                        "karma_critpath": 0,
                        "testcase_feedback": [],
                        "text": "This update has reached 3 days in testing " +
                        "and can be pushed to stable now if the maintainer " +
                        "wishes",
                        "timestamp": "2018-04-21 18:00:24",
                        "update_id": 112982,
                        "user": {
                            "avatar": None,
                            "email": None,
                            "groups": [],
                            "id": 91,
                            "name": "bodhi",
                            "openid": None,
                            "show_popups": True},
                            "user_id": 91
                    }
                ],
                "compose": None,
                "content_type": "rpm",
                "critpath": False,
                "date_approved": None,
                "date_modified": None,
                "date_pushed": "2018-04-18 16:19:48",
                "date_stable": None,
                "date_submitted": "2018-04-17 18:20:04",
                "date_testing": "2018-04-18 16:19:48",
                "greenwave_summary_string": "all required tests passed",
                "karma": 0,
                "locked": False,
                "meets_testing_requirements": True,
                "notes": "Update to 1.1.0.",
                "old_updateid": None,
                "pushed": True,
                "release": {
                    "branch": "f28",
                    "candidate_tag": "f28-updates-candidate",
                    "composes": [
                        {
                            "content_type": "rpm",
                            "release_id": 21,
                            "request": "testing",
                            "security": True
                        }
                    ],
                    "dist_tag": "f28",
                    "id_prefix": "FEDORA",
                    "long_name": "Fedora 28",
                    "name": "F28",
                    "override_tag": "f28-override",
                    "pending_signing_tag": "f28-signing-pending",
                    "pending_stable_tag": "f28-updates-pending",
                    "pending_testing_tag": "f28-updates-testing-pending",
                    "stable_tag": "f28-updates",
                    "state": "current",
                    "testing_tag": "f28-updates-testing",
                    "version": "28"
                },
                "request": None,
                "require_bugs": True,
                "require_testcases": True,
                "requirements": "",
                "severity": "unspecified",
                "stable_karma": 1,
                "status": "testing",
                "submitter": "elyscape",
                "suggest": "unspecified",
                "test_cases": [],
                "test_gating_status": "passed",
                "title": "python-josepy-1.1.0-1.fc28",
                "type": "enhancement",
                "unstable_karma": -1,
                "updateid": "FEDORA-2018-e1f68e9766",
                "url": "https://bodhi.fedoraproject.org/updates/" +
                "FEDORA-2018-e1f68e9766",
                "user": {
                    "avatar": None,
                    "groups": [
                        {
                            "name": "packager"
                        }
                    ],
                    "id": 3225,
                    "name": "elyscape",
                    "openid": None,
                    "show_popups": True
                }
            }
        }
    }


class TestBodhiErrataPublish(Base):
    """ `Bodhi2 <https://bodhi.fedoraproject.org>`_, along with many
    other services, moved away from sending its own email notifications to
    instead publish fedmsg messages that the `FMN system
    <https://apps.fedoraproject.org/notifications>`_ would be responsible for
    forwarding.

    This message type comes from that move.  It represents the "errata" for a
    package when it it mashed into a repository.
    """
    expected_title = "bodhi.errata.publish"
    expected_subti = "This is the subject of the errata email"
    expected_long_form = "This is the body of the errata email"
    expected_link = "https://bodhi.fedoraproject.org/updates/" + \
        "tzdata-2014i-1.fc19"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c" + \
        "?s=64&d=retro"
    expected_usernames = set(['ralph'])
    expected_packages = set(['tzdata'])
    expected_objects = set(['packages/tzdata'])
    msg = {
        "username": "threebean",
        "i": 2,
        "timestamp": 1422302779,
        "msg_id": "2015-21b9ae33-3fdf-42ab-aecb-5717d0d76018",
        "topic": "org.fedoraproject.dev.bodhi.errata.publish",
        "msg": {
            "subject": "This is the subject of the errata email",
            "body": "This is the body of the errata email",
            "update": {
                "close_bugs": True,
                "old_updateid": None,
                "pushed": False,
                "require_testcases": True,
                "critpath": False,
                "cves": [],
                "stable_karma": 3,
                "date_pushed": None,
                "requirements": "rpmlint",
                "severity": "unspecified",
                "title": "tzdata-2014i-1.fc19",
                "suggest": "unspecified",
                "require_bugs": True,
                "comments": [
                    {
                        "bug_feedback": [],
                        "user_id": 1681,
                        "timestamp": "2015-01-28 03:02:44",
                        "testcase_feedback": [],
                        "karma_critpath": 0,
                        "update": 54046,
                        "update_id": 54046,
                        "karma": 0,
                        "anonymous": False,
                        "text": "ralph edited this update. ",
                        "id": 484236,
                        "user": {
                            "buildroot_overrides": [],
                            "stacks": [],
                            "name": "bodhi",
                            "avatar": None
                        }
                    }
                ],
                "date_approved": None,
                "type": "enhancement",
                "status": "pending",
                "date_submitted": "2014-10-29 20:02:57",
                "unstable_karma": -3,
                "user": {
                    "buildroot_overrides": [],
                    "stacks": [
                        {
                            "requirements": "depcheck upgradepath",
                            "description": "This stack is so hack!",
                            "name": "Hackey",
                            "groups": [],
                            "packages": [],
                            "users": [
                                1711
                            ]
                        },
                    ],
                    "name": "ralph",
                    "avatar": None
                },
                "locked": False,
                "builds": [
                    {
                        "override": None,
                        "nvr": "tzdata-2014i-1.fc19"
                    }
                ],
                "date_modified": "2015-01-28 03:02:55",
                "notes": "the update notes go here...",
                "request": "testing",
                "bugs": [],
                "alias": None,
                "karma": 0,
                "release": {
                    "dist_tag": "f19",
                    "name": "F19",
                    "testing_tag": "f19-updates-testing",
                    "pending_stable_tag": "f19-updates-pending",
                    "long_name": "Fedora 19",
                    "state": "disabled",
                    "version": None,
                    "override_tag": "f19-override",
                    "branch": None,
                    "id_prefix": "FEDORA",
                    "pending_testing_tag": "f19-updates-testing-pending",
                    "stable_tag": "f19-updates",
                    "candidate_tag": "f19-updates-candidate"
                }
            },
        }
    }


mash_list = """
- qt-creator-3.4.1-3.fc23
- rakudo-star-0.0.2015.06-1.fc21
- rakudo-star-0.0.2015.06-1.fc22
- nqp-0.0.2015.06-1.fc21
- nqp-0.0.2015.06-1.fc22
- moarvm-0.2015.06-1.fc21
- moarvm-0.2015.06-1.fc22
- libetonyek-0.1.3-1.fc22
- bind-9.10.2-2.P1.fc22,bind-dyndb-ldap-7.0-5.fc22,dnsperf-2.0.0.0-16.fc22
- gap-pkg-autodoc-2015.04.29-2.fc22
- hawaii-widget-styles-0.5.0-1.fc21
- php-pear-PHP-CodeSniffer-2.3.3-1.fc21
- php-pear-PHP-CodeSniffer-2.3.3-1.fc22
- hawaii-widget-styles-0.5.0-1.fc22
- MySQL-python-1.3.6-3.fc22
- xdg-app-0.3.5-1.fc21
- linux-firmware-20150521-53.git3161bfa4.fc22,ivtv-firmware-20080701-28
- xdg-app-0.3.5-1.fc22
- selinux-policy-3.13.1-105.18.fc21
- dnf-plugins-core-0.1.9-1.fc22
"""

class TestLegacyBodhi2MasherStart(Base):
    """ This message is published by an admin when they send a request to
    the `Bodhi2 <https://bodhi.fedoraproject.org>`_ backend, telling it
    to start a mash. This is how messages looked before Bodhi commit
    3b655f23 , which changed the message from including a dict of updates
    to including a dict of composes. The first release with the change
    was 3.2.0.
    """
    expected_title = "bodhi.masher.start"
    expected_subti = "ralph requested a mash of 20 updates"
    expected_long_form = mash_list
    expected_link = "https://bodhi.fedoraproject.org"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c" + \
        "?s=64&d=retro"
    expected_usernames = set(['ralph'])
    expected_packages = set([
        "qt-creator",
        "rakudo-star",
        "nqp",
        "moarvm",
        "libetonyek",
        "bind",
        "bind-dyndb-ldap",
        "dnsperf",
        "gap-pkg-autodoc",
        "hawaii-widget-styles",
        "php-pear-PHP-CodeSniffer",
        "hawaii-widget-styles",
        "MySQL-python",
        "xdg-app",
        "linux-firmware",
        "ivtv-firmware",
        "xdg-app",
        "selinux-policy",
        "dnf-plugins-core",
    ])
    expected_objects = set([
        "packages/qt-creator",
        "packages/rakudo-star",
        "packages/nqp",
        "packages/moarvm",
        "packages/libetonyek",
        "packages/bind",
        "packages/bind-dyndb-ldap",
        "packages/dnsperf",
        "packages/gap-pkg-autodoc",
        "packages/hawaii-widget-styles",
        "packages/php-pear-PHP-CodeSniffer",
        "packages/hawaii-widget-styles",
        "packages/MySQL-python",
        "packages/xdg-app",
        "packages/linux-firmware",
        "packages/ivtv-firmware",
        "packages/xdg-app",
        "packages/selinux-policy",
        "packages/dnf-plugins-core",
    ])
    msg = {
        "username": "threebean",
        "i": 1,
        "timestamp": 1439929069,
        "msg_id": "2015-d370d1cd-4015-4c30-a249-792605db003f",
        "topic": "org.fedoraproject.dev.bodhi.masher.start",
        "msg": {
            "updates": [
                "qt-creator-3.4.1-3.fc23",
                "rakudo-star-0.0.2015.06-1.fc21",
                "rakudo-star-0.0.2015.06-1.fc22",
                "nqp-0.0.2015.06-1.fc21",
                "nqp-0.0.2015.06-1.fc22",
                "moarvm-0.2015.06-1.fc21",
                "moarvm-0.2015.06-1.fc22",
                "libetonyek-0.1.3-1.fc22",
                "bind-9.10.2-2.P1.fc22,bind-dyndb-ldap-7.0-5.fc22,"
                "dnsperf-2.0.0.0-16.fc22",
                "gap-pkg-autodoc-2015.04.29-2.fc22",
                "hawaii-widget-styles-0.5.0-1.fc21",
                "php-pear-PHP-CodeSniffer-2.3.3-1.fc21",
                "php-pear-PHP-CodeSniffer-2.3.3-1.fc22",
                "hawaii-widget-styles-0.5.0-1.fc22",
                "MySQL-python-1.3.6-3.fc22",
                "xdg-app-0.3.5-1.fc21",
                "linux-firmware-20150521-53.git3161bfa4.fc22,"
                "ivtv-firmware-20080701-28",
                "xdg-app-0.3.5-1.fc22",
                "selinux-policy-3.13.1-105.18.fc21",
                "dnf-plugins-core-0.1.9-1.fc22"
            ],
            "agent": "ralph"
        }
    }


class TestLegacyBodhi320MasherStart(Base):
    """ This message is published by an admin when they send a request to
    the `Bodhi 3.2.0+ <https://bodhi.fedoraproject.org>`_ backend, telling it
    to start a mash.
    """
    expected_title = "bodhi.masher.start"
    expected_subti = "releng requested a mash of some updates"
    expected_link = "https://bodhi.fedoraproject.org"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "05b5fce36707d3f962a8dc03094e41028ac3e765c8c2e182eab96228013ec9c9" + \
        "?s=64&d=retro"
    expected_usernames = set(['releng'])
    expected_packages = set([])
    expected_objects = set([])
    msg = {
      "username": "apache",
      "source_name": "datanommer",
      "i": 1,
      "timestamp": 1559001608.0,
      "msg_id": "2019-13d8e80d-34a3-49d6-9d46-b465d891535d",
      "crypto": "x509",
      "topic": "org.fedoraproject.prod.bodhi.masher.start",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "resume": False,
        "api_version": 2,
        "agent": "releng",
        "composes": [
          {
            "security": True,
            "release_id": 28,
            "request": "stable",
            "content_type": "rpm"
          },
          {
            "security": True,
            "release_id": 23,
            "request": "stable",
            "content_type": "rpm"
          },
          {
            "security": False,
            "release_id": 21,
            "request": "stable",
            "content_type": "rpm"
          },
          {
            "security": False,
            "release_id": 8,
            "request": "stable",
            "content_type": "rpm"
          },
          {
            "security": False,
            "release_id": 28,
            "request": "testing",
            "content_type": "rpm"
          },
          {
            "security": False,
            "release_id": 8,
            "request": "testing",
            "content_type": "rpm"
          },
          {
            "security": False,
            "release_id": 23,
            "request": "testing",
            "content_type": "rpm"
          },
          {
            "security": False,
            "release_id": 21,
            "request": "testing",
            "content_type": "rpm"
          },
          {
            "security": False,
            "release_id": 10,
            "request": "testing",
            "content_type": "rpm"
          },
          {
            "security": False,
            "release_id": 29,
            "request": "testing",
            "content_type": "module"
          },
          {
            "security": False,
            "release_id": 24,
            "request": "testing",
            "content_type": "module"
          }
        ]
      }
    }


class TestBodhi4ComposerStart(Base):
    """ This message is published by an admin when they send a request to
    the `Bodhi 4+ <https://bodhi.fedoraproject.org>`_ backend, telling it
    to start a mash. It is exactly like bodhi.masher.start from Bodhi
    3.2.0+, just with the name changed to bodhi.composer.start.
    """
    expected_title = "bodhi.composer.start"
    expected_subti = "releng requested a mash of some updates"
    expected_link = "https://bodhi.fedoraproject.org"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "05b5fce36707d3f962a8dc03094e41028ac3e765c8c2e182eab96228013ec9c9" + \
        "?s=64&d=retro"
    expected_usernames = set(['releng'])
    expected_packages = set([])
    expected_objects = set([])
    msg = {
      "username": "amqp-bridge",
      "source_name": "datanommer",
      "i": 226693,
      "timestamp": 1561593605.0,
      "msg_id": "2019-d3041ae5-2b13-4269-944e-cee4d8238c87",
      "crypto": "x509",
      "topic": "org.fedoraproject.prod.bodhi.composer.start",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "resume": False,
        "api_version": 2,
        "agent": "releng",
        "composes": [
          {
            "security": True,
            "release_id": 8,
            "request": "stable",
            "content_type": "rpm"
          },
          {
            "security": True,
            "release_id": 23,
            "request": "stable",
            "content_type": "rpm"
          },
          {
            "security": True,
            "release_id": 28,
            "request": "stable",
            "content_type": "rpm"
          },
          {
            "security": False,
            "release_id": 29,
            "request": "stable",
            "content_type": "module"
          },
          {
            "security": False,
            "release_id": 24,
            "request": "stable",
            "content_type": "module"
          },
          {
            "security": False,
            "release_id": 28,
            "request": "testing",
            "content_type": "rpm"
          },
          {
            "security": False,
            "release_id": 23,
            "request": "testing",
            "content_type": "rpm"
          },
          {
            "security": False,
            "release_id": 31,
            "request": "testing",
            "content_type": "flatpak"
          },
          {
            "security": False,
            "release_id": 8,
            "request": "testing",
            "content_type": "rpm"
          }
        ]
      }
    }


class TestBodhiUpdateFedoraSync(Base):
    """These messages are published by the new-updates-sync script,
    which lives in the ansible infra repo in the bodhi backend role,
    after it syncs the packages from a Fedora updates compose to the
    master mirror.
    """
    expected_title = "bodhi.updates.fedora.sync"
    expected_subti = "New Fedora 29 updates-testing content synced out " + \
        "(1 GiB changed with 1259 files deleted)"
    expected_link = "https://download.fedoraproject.org/pub/fedora/linux/updates/testing/29/Everything/"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_usernames = set([])
    expected_objects = set(['fedora/updates-testing/29'])
    msg = {
      "username": "ftpsync",
      "source_name": "datanommer",
      "i": 1,
      "timestamp": 1561603095.0,
      "msg_id": "2019-2656349c-2c41-48bd-9b66-31b3cd9a5aa9",
      "crypto": "x509",
      "topic": "org.fedoraproject.prod.bodhi.updates.fedora.sync",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "deleted": "1259",
        "release": "29",
        "raw_bytes": "2116251621",
        "bytes": "1 GiB",
        "repo": "updates-testing"
      }
    }


class TestBodhiUpdateFedoraSyncModular(Base):
    """These messages are published by the new-updates-sync script,
    which lives in the ansible infra repo in the bodhi backend role,
    after it syncs the packages from a Fedora updates compose to the
    master mirror. This is how the messages for modular update
    composes look.
    """
    nodoc = True
    expected_title = "bodhi.updates.fedora.sync"
    expected_subti = "New Fedora 30 updates modular content synced out " + \
        "(404 MiB changed with 412 files deleted)"
    expected_link = "https://download.fedoraproject.org/pub/fedora/linux/updates/30/Modular/"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_usernames = set([])
    expected_objects = set(['fedora/updates/30'])
    msg = {
      "username": "ftpsync",
      "source_name": "datanommer",
      "i": 1,
      "timestamp": 1561595377.0,
      "msg_id": "2019-b7ddfebc-cff4-4dc1-a078-bcf50379b875",
      "crypto": "x509",
      "topic": "org.fedoraproject.prod.bodhi.updates.fedora.sync",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "deleted": "412",
        "release": "30m",
        "raw_bytes": "424030490",
        "bytes": "404 MiB",
        "repo": "updates"
      }
    }


class TestBodhiUpdateEPELSync(Base):
    """These messages are published by the new-updates-sync script,
    which lives in the ansible infra repo in the bodhi backend role,
    after it syncs the packages from an EPEL updates compose to the
    master mirror.
    """
    expected_title = "bodhi.updates.epel.sync"
    expected_subti = "New EPEL 7 epel-testing content synced out " + \
        "(505 MiB changed with 74 files deleted)"
    expected_link = "https://download.fedoraproject.org/pub/epel/testing/7/"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_usernames = set([])
    expected_objects = set(['epel/epel-testing/7'])
    msg = {
      "username": "ftpsync",
      "source_name": "datanommer",
      "i": 3,
      "timestamp": 1561597841.0,
      "msg_id": "2019-a31ad980-b626-4685-8aa5-fd4a61a85fb4",
      "crypto": "x509",
      "topic": "org.fedoraproject.prod.bodhi.updates.epel.sync",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "deleted": "74",
        "release": "7",
        "raw_bytes": "530049354",
        "bytes": "505 MiB",
        "repo": "epel-testing"
      }
    }

add_doc(locals())

if __name__ == '__main__':
    unittest.main()
