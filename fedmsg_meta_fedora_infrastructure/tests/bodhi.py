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


class TestBodhiUpdateComplete(Base):
    """ The `Bodhi Updates System <https://bodhi.fedoraproject.org>`_
    publishes messages on this topic whenever an update
    **completes it's push to the testing repository**.  Here's a
    straightforward example:
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


class TestBodhiMashTaskMashing(Base):
    """ The `Bodhi Masher <https://bodhi.fedoraproject.org>`_
    publishes messages on this topic whenever it starts mashing
    a particular repository.

    Note that, these messages are broken (serverside) due to `this
    issue <https://github.com/fedora-infra/fedmsg/issues/115>`_.
    """
    expected_title = "bodhi.mashtask.mashing"
    expected_subti = "bodhi masher started mashing test_repo"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = expected_icon
    expected_objects = set(['repos/test_repo'])

    msg = {
        'topic': "org.fedoraproject.prod.bodhi.mashtask.mashing",
        'msg': {
            'repo': 'test_repo',
            'updates': [
            ],
        },
    }


class TestBodhiMashTaskStart(Base):
    """ The `Bodhi Masher <https://bodhi.fedoraproject.org>`_
    publishes messages on this topic whenever it **begins** its work.

    Note that, these messages are broken (serverside) due to `this
    issue <https://github.com/fedora-infra/fedmsg/issues/115>`_.
    """
    expected_title = "bodhi.mashtask.start"
    expected_subti = "bodhi masher started a push"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = expected_icon
    msg = {
        'topic': "org.fedoraproject.prod.bodhi.mashtask.start",
        'msg': {}
    }


class TestBodhiMashTaskComplete(Base):
    """ The `Bodhi Masher <https://bodhi.fedoraproject.org>`_
    publishes messages on this topic whenever it **finishes** its work.

    Note that, these messages are broken (serverside) due to `this
    issue <https://github.com/fedora-infra/fedmsg/issues/115>`_.
    """
    expected_title = "bodhi.mashtask.complete"
    expected_subti = "bodhi masher failed to mash test_repo"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = expected_icon
    msg = {
        'topic': "org.fedoraproject.prod.bodhi.mashtask.complete",
        'msg': {'success': False, 'repo': 'test_repo'}
    }


class TestBodhiMashTaskSyncWaitStart(Base):
    """ The `Bodhi Masher <https://bodhi.fedoraproject.org>`_
    publishes messages on this topic when it begins **waiting to sync**.

    Note that, these messages are broken (serverside) due to `this
    issue <https://github.com/fedora-infra/fedmsg/issues/115>`_.
    """
    expected_title = "bodhi.mashtask.sync.wait"
    expected_subti = "bodhi masher is waiting for test_repo " + \
        "to hit the master mirror"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = expected_icon
    msg = {
        'topic': "org.fedoraproject.prod.bodhi.mashtask.sync.wait",
        'msg': {'repo': 'test_repo'}
    }


class TestBodhiMashTaskSyncWaitDone(Base):
    """ The `Bodhi Masher <https://bodhi.fedoraproject.org>`_
    publishes messages on this topic when it finishes syncing.

    Note that, these messages are broken (serverside) due to `this
    issue <https://github.com/fedora-infra/fedmsg/issues/115>`_.
    """
    expected_title = "bodhi.mashtask.sync.done"
    expected_subti = "bodhi masher finished waiting for test_repo " + \
        "to hit the master mirror"
    expected_icon = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    expected_secondary_icon = expected_icon

    msg = {
        'topic': "org.fedoraproject.prod.bodhi.mashtask.sync.done",
        'msg': {'repo': 'test_repo'}
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


class TestBodhiComment(Base):
    """ The `Bodhi Updates System <https://bodhi.fedoraproject.org>`_
    publishes messages on this topic whenever a user **comments** on a bodhi
    update.
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


class TestBodhiStackSave(Base):
    """ `Bodhi2 <https://bodhi.fedoraproject.org>`_ introduced the
    concept of *stacks* of packages that can be grouped for to share
    requirements.  That system publishes messages like this anytime a user
    **modifies or creates a new stack**.
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


class TestBodhiStackDelete(Base):
    """ `Bodhi2 <https://bodhi.fedoraproject.org>`_ introduced the
    concept of *stacks* of packages that can be grouped for to share
    requirements.  That system publishes messages like this anytime a user
    **deletes a stack**.
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
    expected_secondary_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/tzdata.png"
    expected_usernames = set([])
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
    expected_secondary_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/tzdata.png"
    expected_usernames = set([])
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

class TestBodhiMashKickooff(Base):
    """ This message is published by an admin when they send a request to
    the `Bodhi2 <https://bodhi.fedoraproject.org>`_ backend, telling it
    to start a mash.
    """
    expected_title = "bodhi.masher.start"
    expected_subti = "ralph requested a mash of 20 updates"
    expected_long_form = mash_list
    expected_link = None
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


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
