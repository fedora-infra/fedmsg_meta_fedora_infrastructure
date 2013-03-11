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
""" Tests for fedmsg.meta """

import unittest

from fedmsg.tests.test_meta import Base

from fedmsg_meta_fedora_infrastructure.tests.compose import *
from fedmsg_meta_fedora_infrastructure.tests.pkgdb import *
from fedmsg_meta_fedora_infrastructure.tests.planet import *
from fedmsg_meta_fedora_infrastructure.tests.buildsys import *
from fedmsg_meta_fedora_infrastructure.tests.askbot import *


class TestFASUserCreateOldStyle(Base):
    expected_title = "fas.user.create (unsigned)"
    expected_subti = "New FAS account:  'ralph'  (created by 'ralph')"
    expected_icon = "https://admin.fedoraproject.org/accounts/static" + \
        "/theme/fas/images/account.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_usernames = set(['ralph'])
    expected_objects = set(['users/ralph'])
    msg = {
        u'i': 1,
        u'timestamp': 1344432054.8098609,
        u'topic': u'org.fedoraproject.stg.fas.user.create',
        u'msg': {
            u'user': {
                u'username': u'ralph'
            },
            u'agent': {
                u'username': u'ralph'
            }
        }
    }


class TestFASUserCreate(Base):
    expected_title = "fas.user.create (unsigned)"
    expected_subti = "New FAS account:  'ralph'  (created by 'ralph')"
    expected_icon = "https://admin.fedoraproject.org/accounts/static" + \
        "/theme/fas/images/account.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_usernames = set(['ralph'])
    expected_objects = set(['users/ralph'])
    msg = {
        u'i': 1,
        u'timestamp': 1344432054.8098609,
        u'topic': u'org.fedoraproject.stg.fas.user.create',
        u'msg': {
            u'user': u'ralph',
            u'agent': u'ralph',
        }
    }


class TestFASEditProfile(Base):
    expected_title = "fas.user.update (unsigned)"
    expected_subti = "ralph edited the following fields of ralph's " + \
        "FAS profile:  comments"
    expected_icon = "https://admin.fedoraproject.org/accounts/static" + \
        "/theme/fas/images/account.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_usernames = set(['ralph'])
    expected_objects = set(['users/ralph'])
    msg = {
        u'topic': u'org.fedoraproject.stg.fas.user.update',
        u'msg': {
            u'fields': [u'comments'],
            u'user': {u'username': u'ralph'},
            u'agent': {u'username': u'ralph'},
        }
    }


class TestFASEditGroupOldStyle(Base):
    expected_title = "fas.group.update (unsigned)"
    expected_subti = "ralph edited the following fields of the " + \
        "ambassadors FAS group:  display_name"
    expected_icon = "https://admin.fedoraproject.org/accounts/static" + \
        "/theme/fas/images/account.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_usernames = set(['ralph'])
    expected_objects = set(['groups/ambassadors'])
    msg = {
        u'topic': u'org.fedoraproject.stg.fas.group.update',
        u'msg': {
            u'fields': [u'display_name'],
            u'group': {u'name': u'ambassadors'},
            u'agent': {u'username': u'ralph'},
        }
    }


class TestFASEditGroup(Base):
    expected_title = "fas.group.update (unsigned)"
    expected_subti = "ralph edited the following fields of the " + \
        "ambassadors FAS group:  display_name"
    expected_icon = "https://admin.fedoraproject.org/accounts/static" + \
        "/theme/fas/images/account.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_usernames = set(['ralph'])
    expected_objects = set(['groups/ambassadors'])
    msg = {
        u'topic': u'org.fedoraproject.stg.fas.group.update',
        u'msg': {
            u'fields': [u'display_name'],
            u'group': u'ambassadors',
            u'agent': u'ralph',
        }
    }


class TestFASGroupCreate(Base):
    expected_title = "fas.group.create (unsigned)"
    expected_subti = "ralph created new FAS group ambassadors"
    expected_icon = "https://admin.fedoraproject.org/accounts/static" + \
        "/theme/fas/images/account.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_usernames = set(['ralph'])
    expected_objects = set(['groups/ambassadors'])
    msg = {
        u'topic': u'org.fedoraproject.stg.fas.group.create',
        u'msg': {
            u'group': {u'name': u'ambassadors'},
            u'agent': {u'username': u'ralph'},
        }
    }


class TestFASRoleUpdate(Base):
    expected_title = "fas.role.update (unsigned)"
    expected_subti = "toshio changed ralph's role in the ambassadors group"
    expected_icon = "https://admin.fedoraproject.org/accounts/static" + \
        "/theme/fas/images/account.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "8128b4c81d09ada7f95ac9dbf888fbea?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_usernames = set(['ralph', 'toshio'])
    expected_objects = set(['users/ralph', 'groups/ambassadors'])
    msg = {
        u'topic': u'org.fedoraproject.stg.fas.role.update',
        u'msg': {
            u'group': {u'name': u'ambassadors'},
            u'user': {u'username': u'ralph'},
            u'agent': {u'username': u'toshio'},
        }
    }


class TestFASGroupRemove(Base):
    expected_title = "fas.group.member.remove (unsigned)"
    expected_subti = "toshio removed ralph from the ambassadors group"
    expected_icon = "https://admin.fedoraproject.org/accounts/static" + \
        "/theme/fas/images/account.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "8128b4c81d09ada7f95ac9dbf888fbea?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_usernames = set(['ralph', 'toshio'])
    expected_objects = set(['users/ralph', 'groups/ambassadors'])
    msg = {
        u'topic': u'org.fedoraproject.stg.fas.group.member.remove',
        u'msg': {
            u'group': {u'name': u'ambassadors'},
            u'user': {u'username': u'ralph'},
            u'agent': {u'username': u'toshio'},
        }
    }


class TestFASGroupSponsor(Base):
    expected_title = "fas.group.member.sponsor (unsigned)"
    expected_subti = "toshio sponsored ralph's membership " + \
        "in the ambassadors group"
    expected_icon = "https://admin.fedoraproject.org/accounts/static" + \
        "/theme/fas/images/account.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "8128b4c81d09ada7f95ac9dbf888fbea?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_usernames = set(['ralph', 'toshio'])
    expected_objects = set(['users/ralph', 'groups/ambassadors'])
    msg = {
        u'topic': u'org.fedoraproject.stg.fas.group.member.sponsor',
        u'msg': {
            u'group': {u'name': u'ambassadors'},
            u'user': {u'username': u'ralph'},
            u'agent': {u'username': u'toshio'},
        }
    }


class TestFASGroupApply(Base):
    expected_title = "fas.group.member.apply (unsigned)"
    expected_subti = "ralph applied for ralph's membership " + \
        "in the ambassadors group"
    expected_icon = "https://admin.fedoraproject.org/accounts/static" + \
        "/theme/fas/images/account.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_usernames = set(['ralph'])
    expected_objects = set(['users/ralph', 'groups/ambassadors'])
    msg = {
        u'topic': u'org.fedoraproject.stg.fas.group.member.apply',
        u'msg': {
            u'group': {u'name': u'ambassadors'},
            u'user': {u'username': u'ralph'},
            u'agent': {u'username': u'ralph'},
        }
    }


class TestBodhiUpdateComplete(Base):
    expected_title = "bodhi.update.complete.testing (unsigned)"
    expected_subti = "ralph's fedmsg-0.2.7-2.el6 bodhi update " + \
        "completed push to testing"
    expected_link = "https://admin.fedoraproject.org/updates/" + \
        "fedmsg-0.2.7-2.el6"
    expected_icon = "https://admin.fedoraproject.org/updates" + \
        "/static/images/bodhi-icon-48.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
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


class TestBodhiRequestMultiplePackagesPerUpdate(Base):
    expected_title = "bodhi.update.request.testing (unsigned)"
    expected_subti = "lmacken submitted " + \
        "gnome-settings-daemon-3.6.1-1.fc18,control-center-3.6.1-1.fc18" + \
        " to testing"
    expected_link = "https://admin.fedoraproject.org/updates/" + \
        "gnome-settings-daemon-3.6.1-1.fc18,control-center-3.6.1-1.fc18"
    expected_icon = "https://admin.fedoraproject.org/updates" + \
        "/static/images/bodhi-icon-48.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "9d953fa825bd80dfa6e45660b03adc2d?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_usernames = set(['hadess'])
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


class TestBodhiMashTaskMashing(Base):
    expected_title = "bodhi.mashtask.mashing (unsigned)"
    expected_subti = "bodhi masher is mashing test_repo"
    expected_icon = "https://admin.fedoraproject.org/updates" + \
        "/static/images/bodhi-icon-48.png"
    expected_secondary_icon = ''
    expected_objects = set(['repos/test_repo'])

    msg = {
        'topic': "org.fedoraproject.prod.bodhi.mashtask.mashing",
        'msg': {
            'repo': 'test_repo',
        },
    }


class TestBodhiMashTaskStart(Base):
    expected_title = "bodhi.mashtask.start (unsigned)"
    expected_subti = "bodhi masher started its mashtask"
    expected_icon = "https://admin.fedoraproject.org/updates" + \
        "/static/images/bodhi-icon-48.png"
    expected_secondary_icon = ''
    msg = {
        'topic': "org.fedoraproject.prod.bodhi.mashtask.start",
        'msg': {}
    }


class TestBodhiMashTaskComplete(Base):
    expected_title = "bodhi.mashtask.complete (unsigned)"
    expected_subti = "bodhi masher failed to complete its mashtask!"
    expected_icon = "https://admin.fedoraproject.org/updates" + \
        "/static/images/bodhi-icon-48.png"
    expected_secondary_icon = ''
    msg = {
        'topic': "org.fedoraproject.prod.bodhi.mashtask.complete",
        'msg': {'success': False}
    }


class TestBodhiMashTaskSyncWait(Base):
    expected_title = "bodhi.mashtask.sync.wait (unsigned)"
    expected_subti = "bodhi masher is waiting on mirror repos to sync"
    expected_icon = "https://admin.fedoraproject.org/updates" + \
        "/static/images/bodhi-icon-48.png"
    expected_secondary_icon = ''
    msg = {
        'topic': "org.fedoraproject.prod.bodhi.mashtask.sync.wait",
        'msg': {}
    }


class TestBodhiMashTaskSyncWait(Base):
    expected_title = "bodhi.mashtask.sync.done (unsigned)"
    expected_subti = "bodhi masher finished waiting on mirror repos to sync"
    expected_icon = "https://admin.fedoraproject.org/updates" + \
        "/static/images/bodhi-icon-48.png"
    expected_secondary_icon = ''

    msg = {
        'topic': "org.fedoraproject.prod.bodhi.mashtask.sync.done",
        'msg': {}
    }


class TestBodhiRequestUnpush(Base):
    expected_title = "bodhi.update.request.unpush (unsigned)"
    expected_subti = "lmacken unpushed foo"
    expected_link = "https://admin.fedoraproject.org/updates/foo"
    expected_icon = "https://admin.fedoraproject.org/updates" + \
        "/static/images/bodhi-icon-48.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "0c35a75019e58e54fb58202db20d2c24?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
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
    expected_title = "bodhi.update.request.obsolete (unsigned)"
    expected_subti = "lmacken obsoleted foo"
    expected_link = "https://admin.fedoraproject.org/updates/foo"
    expected_icon = "https://admin.fedoraproject.org/updates" + \
        "/static/images/bodhi-icon-48.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "0c35a75019e58e54fb58202db20d2c24?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
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
    expected_title = "bodhi.update.request.stable (unsigned)"
    expected_subti = "lmacken submitted foo to stable"
    expected_link = "https://admin.fedoraproject.org/updates/foo"
    expected_icon = "https://admin.fedoraproject.org/updates" + \
        "/static/images/bodhi-icon-48.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "0c35a75019e58e54fb58202db20d2c24?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
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
    expected_title = "bodhi.update.request.revoke (unsigned)"
    expected_subti = "lmacken revoked foo"
    expected_link = "https://admin.fedoraproject.org/updates/foo"
    expected_icon = "https://admin.fedoraproject.org/updates" + \
        "/static/images/bodhi-icon-48.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "0c35a75019e58e54fb58202db20d2c24?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
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
    expected_title = "bodhi.update.request.testing (unsigned)"
    expected_subti = "lmacken submitted foo to testing"
    expected_link = "https://admin.fedoraproject.org/updates/foo"
    expected_icon = "https://admin.fedoraproject.org/updates" + \
        "/static/images/bodhi-icon-48.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "0c35a75019e58e54fb58202db20d2c24?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
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


class TestBodhiComment(Base):
    expected_title = "bodhi.update.comment (unsigned)"
    expected_subti = "ralph commented on bodhi update fedmsg-1.0-1 (karma: -1)"
    expected_link = "https://admin.fedoraproject.org/updates/fedmsg-1.0-1"
    expected_icon = "https://admin.fedoraproject.org/updates" + \
        "/static/images/bodhi-icon-48.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_usernames = set(['ralph'])
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
                "text": "Can you believe how much testing we're doing?",
                "karma": -1,
                "anonymous": False,
                "timestamp": 1344344050.0
            }
        }
    }


class TestBodhiOverrideTagged(Base):
    expected_title = "bodhi.buildroot_override.tag (unsigned)"
    expected_subti = "lmacken submitted a buildroot override for fedmsg-1.0-1"
    expected_icon = "https://admin.fedoraproject.org/updates" + \
        "/static/images/bodhi-icon-48.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "0c35a75019e58e54fb58202db20d2c24?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
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
    expected_title = "bodhi.buildroot_override.untag (unsigned)"
    expected_subti = "lmacken expired a buildroot override for fedmsg-1.0-1"
    expected_icon = "https://admin.fedoraproject.org/updates" + \
        "/static/images/bodhi-icon-48.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "0c35a75019e58e54fb58202db20d2c24?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
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


class TestSupybotStartMeetingNoName(Base):
    expected_title = "meetbot.meeting.start (unsigned)"
    expected_subti = 'threebean started a meeting in #channel'
    expected_usernames = set(['threebean', 'fedmsg-test-bot'])
    expected_objects = set([
        'attendees/fedmsg-test-bot',
        'attendees/threebean',
        'channels/#channel',
    ])

    msg = {
        "i": 16,
        "msg": {
            "meeting_topic": None,
            "attendees": {
                "fedmsg-test-bot": 2,
                "threebean": 2
            },
            "chairs": {},
            "url": "http://logs.com/awesome",
            "owner": "threebean",
            "channel": "#channel"
        },
        "topic": "org.fedoraproject.dev.meetbot.meeting.start",
        "timestamp": 1345572862.556145
    }


class TestSupybotStartMeeting(Base):
    expected_title = "meetbot.meeting.start (unsigned)"
    expected_subti = 'threebean started meeting "title" in #channel'
    expected_usernames = set(['threebean', 'fedmsg-test-bot'])
    expected_objects = set([
        'attendees/fedmsg-test-bot',
        'attendees/threebean',
        'channels/#channel',
        'titles/title',
    ])

    msg = {
        "i": 16,
        "msg": {
            "meeting_topic": "title",
            "attendees": {
                "fedmsg-test-bot": 2,
                "threebean": 2
            },
            "chairs": {},
            "url": "http://logs.com/awesome",
            "owner": "threebean",
            "channel": "#channel"
        },
        "topic": "org.fedoraproject.dev.meetbot.meeting.start",
        "timestamp": 1345572862.556145
    }


class TestSupybotEndMeeting(Base):
    expected_title = "meetbot.meeting.complete (unsigned)"
    expected_subti = 'threebean ended meeting "title" in #channel'
    expected_link = 'http://logs.com/awesome.html'
    expected_usernames = set(['threebean', 'fedmsg-test-bot'])
    expected_objects = set([
        'attendees/fedmsg-test-bot',
        'attendees/threebean',
        'channels/#channel',
        'titles/title',
    ])

    msg = {
        "i": 16,
        "msg": {
            "meeting_topic": "title",
            "attendees": {
                "fedmsg-test-bot": 2,
                "threebean": 2
            },
            "chairs": {},
            "url": "http://logs.com/awesome",
            "owner": "threebean",
            "channel": "#channel"
        },
        "topic": "org.fedoraproject.dev.meetbot.meeting.complete",
        "timestamp": 1345572862.556145
    }


class TestSupybotEndMeetingNoTitle(Base):
    expected_title = "meetbot.meeting.complete (unsigned)"
    expected_subti = 'threebean ended a meeting in #channel'
    expected_link = 'http://logs.com/awesome.html'
    expected_usernames = set(['threebean', 'fedmsg-test-bot'])
    expected_objects = set([
        'attendees/fedmsg-test-bot',
        'attendees/threebean',
        'channels/#channel',
    ])

    msg = {
        "i": 16,
        "msg": {
            "meeting_topic": None,
            "attendees": {
                "fedmsg-test-bot": 2,
                "threebean": 2
            },
            "chairs": {},
            "url": "http://logs.com/awesome",
            "owner": "threebean",
            "channel": "#channel"
        },
        "topic": "org.fedoraproject.dev.meetbot.meeting.complete",
        "timestamp": 1345572862.556145
    }


class TestTaggerVoteAnonymous(Base):
    expected_title = "fedoratagger.tag.update (unsigned)"
    expected_subti = 'anonymous upvoted "unittest" on perl-Test-Fatal'
    expected_link = 'https://apps.fedoraproject.org/tagger/perl-Test-Fatal'
    expected_usernames = set([])
    expected_packages = set(['perl-Test-Fatal'])
    expected_objects = set(['packages/perl-Test-Fatal', 'labels/unittest'])

    msg = {
        "i": 1,
        "timestamp": 1345220838.2775879,
        "topic": "org.fedoraproject.stg.fedoratagger.tag.update",
        "msg": {
            "vote": {
                "tag": {
                    "votes": 2,
                    "like": 2,
                    "package": {
                        "perl-Test-Fatal": [
                            {
                                "dislike": 0,
                                "total": 1,
                                "tag": "perl",
                                "votes": 1,
                                "like": 1
                            },
                            {
                                "dislike": 0,
                                "total": 2,
                                "tag": "unittest",
                                "votes": 2,
                                "like": 2
                            }
                        ]
                    },
                    "label": {
                        "label": "unittest",
                        "tags": [
                            {
                                "dislike": 0,
                                "total": 2,
                                "tag": "unittest",
                                "votes": 2,
                                "like": 2
                            }
                        ]
                    },
                    "tag": "unittest",
                    "dislike": 0,
                    "total": 2
                },
                "like": True,
                "user": {
                    "username": "anonymous",
                    "all_votes": [],
                    "votes": 0,
                    "rank": -1
                }
            }
        }
    }


class TestTaggerCreate(Base):
    expected_title = "fedoratagger.tag.create (unsigned)"
    expected_subti = 'ralph added tag "unittest" to perl-Test-Fatal'
    expected_link = 'https://apps.fedoraproject.org/tagger/perl-Test-Fatal'
    expected_usernames = set(['ralph'])
    expected_packages = set(['perl-Test-Fatal'])
    expected_objects = set(['packages/perl-Test-Fatal', 'labels/unittest'])

    msg = {
        "i": 1,
        "timestamp": 1345220073.4948981,
        "topic": "org.fedoraproject.stg.fedoratagger.tag.create",
        "msg": {
            "vote": {
                "tag": {
                    "votes": 1,
                    "like": 1,
                    "package": {
                        "perl-Test-Fatal": [
                            {
                                "dislike": 0,
                                "total": 1,
                                "tag": "unittest",
                                "votes": 1,
                                "like": 1
                            },
                            {
                                "dislike": 0,
                                "total": 1,
                                "tag": "perl",
                                "votes": 1,
                                "like": 1
                            }
                        ]
                    },
                    "label": {
                        "label": "unittest",
                        "tags": [
                            {
                                "dislike": 0,
                                "total": 1,
                                "tag": "unittest",
                                "votes": 1,
                                "like": 1
                            }
                        ]
                    },
                    "tag": "unittest",
                    "dislike": 0,
                    "total": 1
                },
                "like": True,
                "user": {
                    "username": "ralph",
                    "votes": 28,
                    "rank": 1
                }
            }
        }
    }


class TestMediaWikiEdit(Base):
    expected_title = "wiki.article.edit (unsigned)"
    expected_subti = 'Ralph made a wiki edit to "Messaging SIG".'
    expected_link = "http://this-is-a-link.org"
    expected_icon = "https://fedoraproject.org/w/skins/common/" + \
        "images/mediawiki.png"
    expected_usernames = set(['ralph'])
    expected_objects = set(['Messaging SIG-page'])

    msg = {
        "topic": "org.fedoraproject.stg.wiki.article.edit",
        "msg": {
            "watch_this": None,
            "base_rev_id": False,
            "title": "Messaging SIG",
            "minor_edit": 0,
            "text": "The diff goes here...",
            "section_anchor": None,
            "summary": "/* Mission */ ",
            "user": "Ralph",
            "revision": None,
            "url": "http://this-is-a-link.org"
        },
        "timestamp": 1344350200
    }


class TestMediaWikiUpload(Base):
    expected_title = "wiki.upload.complete (unsigned)"
    expected_subti = 'Ralph uploaded File:Cat.jpg to the wiki: ' + \
        '"This is a beautiful cat..."'
    expected_icon = "https://fedoraproject.org/w/skins/common/" + \
        "images/mediawiki.png"
    expected_usernames = set(['ralph'])
    expected_objects = set(['w/uploads/d/d1/Cat.jpg'])

    msg = {
        "topic": "org.fedoraproject.stg.wiki.upload.complete",
        "msg": {
            "user_id": 8306,
            "description": "This is a beautiful cat",
            "title": {
                "mCascadeSources": [],
                "mLength": -1,
                "mInterwiki": "",
                "mNotificationTimestamp": [],
                "mCascadeRestriction": None,
                "mRedirect": None,
                "mArticleID": 46586,
                "mTextform": "Cat.jpg",
                "mWatched": None,
                "mDbkeyform": "Cat.jpg",
                "mCascadingRestrictions": [],
                "mDefaultNamespace": 0,
                "mRestrictions": [],
                "mUrlform": "Cat.jpg",
                "mLatestID": False,
                "mBacklinkCache": {},
                "mNamespace": 6,
                "mUserCaseDBKey": "Cat.jpg",
                "mTitleProtection": False,
                "mOldRestrictions": False,
                "mFragment": "",
                "mHasCascadingRestrictions": None,
                "mPrefixedText": "File:Cat.jpg",
                "mRestrictionsExpiry": {
                    "create": "infinity"
                },
                "mRestrictionsLoaded": False
            },
            "user_text": "Ralph",
            "minor_mime": "jpeg",
            "url": "/w/uploads/d/d1/Cat.jpg",
            "file_exists": True,
            "mime": "image/jpeg",
            "major_mime": "image",
            "media_type": "BITMAP",
            "size": 295667
        },
        "timestamp": 1344361406
    }


class TestPkgdb2BrMassStart(Base):
    expected_title = "git.mass_branch.start (unsigned)"
    expected_subti = "dgilmore started a mass branch"
    expected_usernames = set(['dgilmore'])

    msg = {
        "i": 1,
        "timestamp": 1344350850.8867381,
        "topic": "org.fedoraproject.prod.git.mass_branch.start",
        "msg": {
            "agent": "dgilmore",
        },
    }


class TestPkgdb2BrMassComplete(Base):
    expected_title = "git.mass_branch.complete (unsigned)"
    expected_subti = "mass branch started by dgilmore completed"
    expected_usernames = set(['dgilmore'])

    msg = {
        "i": 1,
        "timestamp": 1344350850.8867381,
        "topic": "org.fedoraproject.prod.git.mass_branch.complete",
        "msg": {
            "agent": "dgilmore",
        },
    }


class TestPkgdb2BrRunStart(Base):
    expected_title = "git.pkgdb2branch.start (unsigned)"
    expected_subti = "limburgher started a run of pkgdb2branch"
    expected_usernames = set(['limburgher'])

    msg = {
        "i": 1,
        "timestamp": 1344350850.8867381,
        "topic": "org.fedoraproject.prod.git.pkgdb2branch.start",
        "msg": {
            "agent": "limburgher",
        },
    }


class TestPkgdb2BrRunComplete(Base):
    expected_title = "git.pkgdb2branch.complete (unsigned)"
    expected_subti = "run of pkgdb2branch started by limburgher completed"
    expected_usernames = set(['limburgher'])
    expected_packages = set(['nethack'])
    expected_objects = set(['nethack/__git__'])

    msg = {
        "i": 1,
        "timestamp": 1344350850.8867381,
        "topic": "org.fedoraproject.prod.git.pkgdb2branch.complete",
        "msg": {
            "agent": "limburgher",
            "unbranchedPackages": [],
            "branchedPackages": ["nethack"],
        },
    }


class TestPkgdb2BrRunCompleteWithError(Base):
    expected_title = "git.pkgdb2branch.complete (unsigned)"
    expected_subti = "run of pkgdb2branch started by limburgher completed" + \
        " with 1 error"
    expected_usernames = set(['limburgher'])
    expected_packages = set(['foo'])
    expected_objects = set(['foo/__git__'])

    msg = {
        "i": 1,
        "timestamp": 1344350850.8867381,
        "topic": "org.fedoraproject.prod.git.pkgdb2branch.complete",
        "msg": {
            "agent": "limburgher",
            "unbranchedPackages": ['foo'],
            "branchedPackages": [],
        },
    }


class TestPkgdb2BrRunCompleteWithErrors(Base):
    expected_title = "git.pkgdb2branch.complete (unsigned)"
    expected_subti = "run of pkgdb2branch started by limburgher completed" + \
        " with 2 errors"
    expected_usernames = set(['limburgher'])
    expected_packages = set(['foo', 'bar'])
    expected_objects = set(['foo/__git__', 'bar/__git__'])

    msg = {
        "i": 1,
        "timestamp": 1344350850.8867381,
        "topic": "org.fedoraproject.prod.git.pkgdb2branch.complete",
        "msg": {
            "agent": "limburgher",
            "unbranchedPackages": ['foo', 'bar'],
            "branchedPackages": [],
        },
    }


class TestPkgdb2BrCreateLegacy(Base):
    expected_title = "git.branch.valgrind.master (unsigned)"
    expected_subti = \
        "limburgher created branch 'master' for the 'valgrind' package"
    expected_link = \
        "http://pkgs.fedoraproject.org/cgit/valgrind.git/log/?h=master"
    expected_usernames = set(['limburgher'])
    expected_packages = set(['valgrind'])
    expected_objects = set(['valgrind/__git__'])

    msg = {
        "i": 1,
        "timestamp": 1344350850.8867381,
        "topic": "org.fedoraproject.prod.git.branch.valgrind.master",
        "msg": {
            "agent": "limburgher",
        },
    }


class TestPkgdb2BrCreate(Base):
    expected_title = "git.branch (unsigned)"
    expected_subti = \
        "limburgher created branch 'master' for the 'valgrind' package"
    expected_link = \
        "http://pkgs.fedoraproject.org/cgit/valgrind.git/log/?h=master"
    expected_usernames = set(['limburgher'])
    expected_packages = set(['valgrind'])
    expected_objects = set(['valgrind/__git__'])

    msg = {
        "i": 1,
        "timestamp": 1344350850.8867381,
        "topic": "org.fedoraproject.prod.git.branch",
        "msg": {
            "agent": "limburgher",
            "name": "valgrind",
            "branch": "master",
        },
    }


class TestLookaside(Base):
    expected_title = "git.lookaside.new (unsigned)"
    expected_subti = 'jnovy uploaded pst-diffraction.doc.tar.xz for texlive'
    expected_link = 'http://pkgs.fedoraproject.org/lookaside/pkgs/' + \
        'texlive/pst-diffraction.doc.tar.xz/' + \
        'dacad985394b3977f9dcf0c75f51a357/' + \
        'pst-diffraction.doc.tar.xz'
    expected_usernames = set(['jnovy'])
    expected_packages = set(['texlive'])
    expected_objects = set(['texlive/pst-diffraction.doc.tar.xz'])

    msg = {
        "i": 1,
        "timestamp": 1349197866.215465,
        "topic": "org.fedoraproject.prod.git.lookaside.new",
        "msg": {
            "agent": "jnovy",
            "md5sum": "dacad985394b3977f9dcf0c75f51a357",
            "name": "texlive",
            "filename": "pst-diffraction.doc.tar.xz"
        }
    }


class TestLookasideLegacy(Base):
    expected_title = "git.lookaside.texlive.new (unsigned)"
    expected_subti = 'jnovy uploaded pst-diffraction.doc.tar.xz for texlive'
    expected_link = 'http://pkgs.fedoraproject.org/lookaside/pkgs/' + \
        'texlive/pst-diffraction.doc.tar.xz/' + \
        'dacad985394b3977f9dcf0c75f51a357/' + \
        'pst-diffraction.doc.tar.xz'
    expected_usernames = set(['jnovy'])
    expected_packages = set(['texlive'])
    expected_objects = set(['texlive/pst-diffraction.doc.tar.xz'])

    msg = {
        "i": 1,
        "timestamp": 1349197866.215465,
        "topic": "org.fedoraproject.prod.git.lookaside.texlive.new",
        "msg": {
            "agent": "jnovy",
            "md5sum": "dacad985394b3977f9dcf0c75f51a357",
            "name": "texlive",
            "filename": "pst-diffraction.doc.tar.xz"
        }
    }


class TestSCMSuperLegacy(Base):
    expected_title = "git.receive.valgrind.master (unsigned)"
    expected_subti = 'mjw pushed to valgrind (master).  ' + \
        '"Clear CFLAGS CXXFLAGS LDFLAGS. (..more)"'
    expected_link = "http://pkgs.fedoraproject.org/cgit/" + \
        "valgrind.git/commit/" + \
        "?h=master&id=7a98f80d9b61ce167e4ef8129c81ed9284ecf4e1"
    expected_icon = "http://git-scm.com/images/logo.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "923419d315c8f23eface39852bf32a5f?s=64&" + \
        "d=http%3A%2F%2Fgit-scm.com%2Fimages%2Flogo.png"
    expected_usernames = set(['mjw'])
    expected_packages = set(['valgrind'])
    expected_objects = set(['valgrind/valgrind.spec'])

    msg = {
        "i": 1,
        "timestamp": 1344350850.8867381,
        "topic": "org.fedoraproject.prod.git.receive.valgrind.master",
        "msg": {
            "commit": {
                "stats": {
                    "files": {
                        "valgrind.spec": {
                            "deletions": 2,
                            "lines": 3,
                            "insertions": 1
                        }
                    },
                    "total": {
                        "deletions": 2,
                        "files": 1,
                        "insertions": 1,
                        "lines": 3
                    }
                },
                "name": "Mark Wielaard",
                "rev": "7a98f80d9b61ce167e4ef8129c81ed9284ecf4e1",
                "summary": "Clear CFLAGS CXXFLAGS LDFLAGS.",
                "message": """Clear CFLAGS CXXFLAGS LDFLAGS.
                This is a bit of a hammer.""",
                "email": "mjw@redhat.com",
                "username": "mjw",
                "branch": "master",
            }
        }
    }


class TestSCMLegacy(Base):
    expected_title = "git.receive.valgrind.master (unsigned)"
    expected_subti = 'mjw pushed to valgrind (master).  ' + \
        '"Clear CFLAGS CXXFLAGS LDFLAGS. (..more)"'
    expected_link = "http://pkgs.fedoraproject.org/cgit/" + \
        "valgrind.git/commit/" + \
        "?h=master&id=7a98f80d9b61ce167e4ef8129c81ed9284ecf4e1"
    expected_icon = "http://git-scm.com/images/logo.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "923419d315c8f23eface39852bf32a5f?s=64&" + \
        "d=http%3A%2F%2Fgit-scm.com%2Fimages%2Flogo.png"
    expected_usernames = set(['mjw'])
    expected_packages = set(['valgrind'])
    expected_objects = set(['valgrind/valgrind.spec'])

    msg = {
        "i": 1,
        "timestamp": 1344350850.8867381,
        "topic": "org.fedoraproject.prod.git.receive.valgrind.master",
        "msg": {
            "commit": {
                "stats": {
                    "files": {
                        "valgrind.spec": {
                            "deletions": 2,
                            "lines": 3,
                            "insertions": 1
                        }
                    },
                    "total": {
                        "deletions": 2,
                        "files": 1,
                        "insertions": 1,
                        "lines": 3
                    }
                },
                "name": "Mark Wielaard",
                "rev": "7a98f80d9b61ce167e4ef8129c81ed9284ecf4e1",
                "summary": "Clear CFLAGS CXXFLAGS LDFLAGS.",
                "message": """Clear CFLAGS CXXFLAGS LDFLAGS.
                This is a bit of a hammer.""",
                "email": "mjw@redhat.com",
                "username": "mjw",
                "branch": "master",
                "repo": "valgrind",
            }
        }
    }


class TestSCM(Base):
    expected_title = "git.receive (unsigned)"
    expected_subti = 'mjw pushed to valgrind (master).  ' + \
        '"Clear CFLAGS CXXFLAGS LDFLAGS. (..more)"'
    expected_link = "http://pkgs.fedoraproject.org/cgit/" + \
        "valgrind.git/commit/" + \
        "?h=master&id=7a98f80d9b61ce167e4ef8129c81ed9284ecf4e1"
    expected_icon = "http://git-scm.com/images/logo.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "923419d315c8f23eface39852bf32a5f?s=64&" + \
        "d=http%3A%2F%2Fgit-scm.com%2Fimages%2Flogo.png"
    expected_usernames = set(['mjw'])
    expected_packages = set(['valgrind'])
    expected_objects = set(['valgrind/valgrind.spec'])

    msg = {
        "i": 1,
        "timestamp": 1344350850.8867381,
        "topic": "org.fedoraproject.prod.git.receive",
        "msg": {
            "commit": {
                "stats": {
                    "files": {
                        "valgrind.spec": {
                            "deletions": 2,
                            "lines": 3,
                            "insertions": 1
                        }
                    },
                    "total": {
                        "deletions": 2,
                        "files": 1,
                        "insertions": 1,
                        "lines": 3
                    }
                },
                "name": "Mark Wielaard",
                "rev": "7a98f80d9b61ce167e4ef8129c81ed9284ecf4e1",
                "summary": "Clear CFLAGS CXXFLAGS LDFLAGS.",
                "message": """Clear CFLAGS CXXFLAGS LDFLAGS.
                This is a bit of a hammer.""",
                "email": "mjw@redhat.com",
                "username": "mjw",
                "branch": "master",
                "repo": "valgrind",
            }
        }
    }


class TestSCMSingleLine(Base):
    expected_title = "git.receive (unsigned)"
    expected_subti = 'spot pushed to ember (master).  ' + \
        '"another missing patch? ridiculous."'
    expected_link = "http://pkgs.fedoraproject.org/cgit/" + \
        "ember.git/commit/" + \
        "?h=master&id=aa2df80f3d8dd217c7cbfe2d3451190028f3fe14"
    expected_icon = "http://git-scm.com/images/logo.png"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "461761d9572bdc1d04925a1125a41797?s=64&" + \
        "d=http%3A%2F%2Fgit-scm.com%2Fimages%2Flogo.png"
    expected_usernames = set(['spot'])
    expected_packages = set(['ember'])
    expected_objects = set(['ember/ember-0.6.3-gcc47.patch'])

    msg = {
        "i": 1,
        "timestamp": 1352998154.368305,
        "topic": "org.fedoraproject.prod.git.receive",
        "msg": {
            "commit": {
                "username": "spot",
                "stats": {
                    "files": {
                        "ember-0.6.3-gcc47.patch": {
                            "deletions": 0,
                            "lines": 26,
                            "insertions": 26
                        }
                    },
                    "total": {
                        "deletions": 0,
                        "files": 1,
                        "insertions": 26,
                        "lines": 26
                    }
                },
                "name": "Tom Callaway",
                "rev": "aa2df80f3d8dd217c7cbfe2d3451190028f3fe14",
                "summary": "another missing patch? ridiculous.",
                "branch": "master",
                "repo": "ember",
                "message": "another missing patch? ridiculous.\n",
                "email": "spot@fedoraproject.org"
            }
        }
    }


if __name__ == '__main__':
    unittest.main()
