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

from fedmsg_meta_fedora_infrastructure.tests.bodhi import *
from fedmsg_meta_fedora_infrastructure.tests.compose import *
from fedmsg_meta_fedora_infrastructure.tests.pkgdb import *
from fedmsg_meta_fedora_infrastructure.tests.planet import *
from fedmsg_meta_fedora_infrastructure.tests.buildsys import *
from fedmsg_meta_fedora_infrastructure.tests.askbot import *
from fedmsg_meta_fedora_infrastructure.tests.tagger import *
from fedmsg_meta_fedora_infrastructure.tests.trac import *
from fedmsg_meta_fedora_infrastructure.tests.mailman3 import *
from fedmsg_meta_fedora_infrastructure.tests.badges import *
from fedmsg_meta_fedora_infrastructure.tests.ansible import *
from fedmsg_meta_fedora_infrastructure.tests.scm import *
from fedmsg_meta_fedora_infrastructure.tests.datanommer import *
from fedmsg_meta_fedora_infrastructure.tests.nuancier import *
from fedmsg_meta_fedora_infrastructure.tests.fedocal import *
from fedmsg_meta_fedora_infrastructure.tests.coprs import *
from fedmsg_meta_fedora_infrastructure.tests.anitya import *
from fedmsg_meta_fedora_infrastructure.tests.summershum import *
from fedmsg_meta_fedora_infrastructure.tests.jenkins import *
from fedmsg_meta_fedora_infrastructure.tests.github import *
from fedmsg_meta_fedora_infrastructure.tests.ftpsync import *
from fedmsg_meta_fedora_infrastructure.tests.bz import *
from fedmsg_meta_fedora_infrastructure.tests.elections import *
from fedmsg_meta_fedora_infrastructure.tests.fmn import *
from fedmsg_meta_fedora_infrastructure.tests.fedimg import *
from fedmsg_meta_fedora_infrastructure.tests.kerneltest import *
from fedmsg_meta_fedora_infrastructure.tests.koschei import *
from fedmsg_meta_fedora_infrastructure.tests.fas import *
from fedmsg_meta_fedora_infrastructure.tests.hotness import *
from fedmsg_meta_fedora_infrastructure.tests.mm2 import *

from fedmsg_meta_fedora_infrastructure.tests.base import Base

from fedmsg_meta_fedora_infrastructure.tests.common import add_doc


full_irc_logs = """======================================
#fedora-meeting-1: RELENG (2015-02-09)
======================================


Meeting started by dgilmore at 16:31:17 UTC. The full logs are available
at
http://meetbot.fedoraproject.org/fedora-meeting-1/2015-02-09/releng.2015-02-09-16.31.log.html
.



Meeting summary
---------------
* init process  (dgilmore, 16:31:30)

* Secondary Architectures updates  (dgilmore, 16:33:42)

* Secondary Architectures update - ppc  (dgilmore, 16:33:43)

* Secondary Architectures update - s390  (dgilmore, 16:36:35)

* Secondary Architectures update - arm  (dgilmore, 16:37:12)

* #6016 Use fedpkg-minimal in Fedora buildroots  (dgilmore, 16:39:22)
  * LINK: https://fedorahosted.org/rel-eng/ticket/6016   (dgilmore,
    16:39:38)
  * LINK: https://koji.fedoraproject.org/koji/buildinfo?buildID=609961
    (bochecha, 16:40:40)

* #5959 Enable keep-alive connections for koji (primary and secondaries)
  (dgilmore, 16:41:44)
  * LINK: https://fedorahosted.org/rel-eng/ticket/5959   (dgilmore,
    16:41:56)
  * ACTION: pbrobinson to send patch to infra list enabling keepalive
    (dgilmore, 16:43:08)

* #6023 allow Peter Robinson to restart sigul bridges  (dgilmore,
  16:43:39)
  * LINK: https://fedorahosted.org/rel-eng/ticket/6023   (dgilmore,
    16:43:48)

* #6027 secondary arch old mash trees cleanup  (dgilmore, 16:45:31)
  * LINK: https://fedorahosted.org/rel-eng/ticket/6027   (dgilmore,
    16:45:47)

* #6096 add individual email addressses to Fedoras GPG keys  (dgilmore,
  16:52:06)
  * LINK: https://fedorahosted.org/rel-eng/ticket/6096   (dgilmore,
    16:52:20)
  * ACTION: dgilmore will make a choice when making the keys  (dgilmore,
    16:58:51)

* #6100 create bsd-style checksum files for CHECKSUM files  (dgilmore,
  16:59:11)
  * LINK: https://fedorahosted.org/rel-eng/ticket/6100   (dgilmore,
    16:59:22)
  * ACTION: dgilmore to make this happen  (dgilmore, 17:03:13)

* open floor  (dgilmore, 17:03:21)

Meeting ended at 17:58:27 UTC.




Action Items
------------
* pbrobinson to send patch to infra list enabling keepalive
* dgilmore will make a choice when making the keys
* dgilmore to make this happen




Action Items, by person
-----------------------
* dgilmore
  * dgilmore will make a choice when making the keys
  * dgilmore to make this happen
* pbrobinson
  * pbrobinson to send patch to infra list enabling keepalive
* **UNASSIGNED**
  * (none)




People Present (lines said)
---------------------------
* dgilmore (116)
* bochecha (33)
* tyll (16)
* pbrobinson (16)
* zodbot (5)
* janeznemanic (1)
* masta (1)
* nirik (0)
* sharkcz (0)




Generated by `MeetBot`_ 0.1.4

.. _`MeetBot`: http://wiki.debian.org/MeetBot
"""

class TestSupybotStartMeetingNoName(Base):
    """ Trusty old `zodbot <https://meetbot.fedoraproject.org/>`_ publishes
    messages too!  Messages on this topic get published (somewhat obviously)
    when a new IRC meeting is started.  The user starting the meeting may
    specify a meeting title, but doesn't have to.  Here's an example
    message with no meeting title specified:
    """
    expected_title = "meetbot.meeting.start"
    expected_subti = 'ralph started a meeting in #channel'
    expected_icon = 'https://apps.fedoraproject.org/img/icons/meetbot.png'
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro"
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'attendees/ralph',
        'channels/#channel',
    ])

    msg = {
        "i": 16,
        "msg": {
            "meeting_topic": None,
            "attendees": {
                "zodbot": 2,
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
    """ Trusty old `zodbot <https://meetbot.fedoraproject.org/>`_ publishes
    messages too!  Messages on this topic get published (somewhat obviously)
    when a new IRC meeting is started.  The user starting the meeting may
    specify a meeting title, but doesn't have to.  Here's an example
    message with a specified meeting title:
    """
    expected_title = "meetbot.meeting.start"
    expected_subti = 'ralph started meeting "title" in #channel'
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'attendees/ralph',
        'channels/#channel',
        'titles/title',
    ])

    msg = {
        "i": 16,
        "msg": {
            "meeting_topic": "title",
            "attendees": {
                "zodbot": 2,
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
    """ Trusty old `zodbot <https://meetbot.fedoraproject.org/>`_ publishes
    messages too!  Messages on this topic get published when an IRC meeting
    ends.  Meetings may or may not have a title (which can be tricky).
    Here's an example message where the title is specified:
    """
    expected_title = "meetbot.meeting.complete"
    expected_subti = 'dgilmore\'s meeting titled "RELENG (2015-02-09)" ' + \
        'ended in #fedora-meeting-1'
    expected_long_form = expected_subti + "\n\n" + full_irc_logs
    expected_link = 'https://meetbot.fedoraproject.org/fedora-meeting-1/' + \
        '2015-02-09/releng.2015-02-09-16.31.html'
    expected_usernames = set([
        'masta',
        'nirik',
        'tyll',
        'bochecha',
        'pbrobinson',
        'sharkcz',
        'janeznemanic',
        'dgilmore',
    ])
    expected_objects = set([
        'attendees/masta',
        'attendees/nirik',
        'attendees/tyll',
        'attendees/bochecha',
        'attendees/pbrobinson',
        'attendees/sharkcz',
        'attendees/janeznemanic',
        'attendees/dgilmore',
        'channels/#fedora-meeting-1',
        'titles/RELENG (2015-02-09)',
        'topics/open floor',
    ])

    msg = {
        "source_name": "datanommer",
        "i": 94,
        "timestamp": 1423504707.0,
        "msg_id": "2015-ff043996-5aaa-471b-bc87-b8551f7fd3b6",
        "topic": "org.fedoraproject.prod.meetbot.meeting.complete",
        "source_version": "0.6.4",
        "msg": {
            "meeting_topic": "RELENG (2015-02-09)",
            "attendees": {
                "masta": 1,
                "nirik": 0,
                "tyll": 16,
                "zodbot": 5,
                "bochecha": 33,
                "pbrobinson": 16,
                "sharkcz": 0,
                "janeznemanic": 1,
                "dgilmore": 116
            },
            "chairs": {
                "masta": True,
                "nirik": True,
                "tyll": True,
                "bochecha": True,
                "pbrobinson": True,
                "dgilmore": True,
                "sharkcz": True
            },
            "topic": "open floor",
            "url": "http://meetbot.fedoraproject.org/fedora-meeting-1/2015-02-09/releng.2015-02-09-16.31",
            "owner": "dgilmore",
            "channel": "#fedora-meeting-1"
        }
    }


class TestSupybotEndMeetingNoTitle(Base):
    """ Trusty old `zodbot <https://meetbot.fedoraproject.org/>`_ publishes
    messages too!  Messages on this topic get published when an IRC meeting
    ends.  Meetings may or may not have a title (which can be tricky).
    Here's an example message where the title is **not** specified:
    """
    expected_title = "meetbot.meeting.complete"
    expected_subti = 'ralph\'s meeting ended in #channel'
    expected_link = 'https://logs.com/awesome.html'
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'attendees/ralph',
        'channels/#channel',
    ])

    msg = {
        "i": 16,
        "msg": {
            "meeting_topic": None,
            "attendees": {
                "zodbot": 2,
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


class TestSupybotChangeTopic(Base):
    """ As IRC meetings chug along, the chairperson may change the meeting;
    zodbot publishes message for that!  An example **with** a title specified:
    """
    expected_title = "meetbot.meeting.topic.update"
    expected_subti = 'The topic of ralph\'s "title" meeting changed ' +\
        'to "Food" in #channel'
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'attendees/ralph',
        'channels/#channel',
        'titles/title',
        'topics/Food',
    ])

    msg = {
        "i": 16,
        "msg": {
            "meeting_topic": "title",
            "attendees": {
                "zodbot": 2,
                "threebean": 2
            },
            "chairs": {},
            "url": "http://logs.com/awesome",
            "owner": "threebean",
            "channel": "#channel",
            "topic": "Food",
        },
        "topic": "org.fedoraproject.dev.meetbot.meeting.topic.update",
        "timestamp": 1345572862.556145
    }


class TestSupybotChangeTopicNoTitle(Base):
    """ As IRC meetings chug along, the chairperson may change the meeting;
    zodbot publishes message for that!  An example **without** a title
    specified:
    """
    expected_title = "meetbot.meeting.topic.update"
    expected_subti = 'The topic of ralph\'s meeting changed ' +\
        'to "Food" in #channel'
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'attendees/ralph',
        'channels/#channel',
        'topics/Food'
    ])

    msg = {
        "i": 16,
        "msg": {
            "meeting_topic": None,
            "attendees": {
                "zodbot": 2,
                "threebean": 2
            },
            "chairs": {},
            "url": "http://logs.com/awesome",
            "owner": "threebean",
            "channel": "#channel",
            "topic": "Food",
        },
        "topic": "org.fedoraproject.dev.meetbot.meeting.topic.update",
        "timestamp": 1345572862.556145
    }


class TestMediaWikiEdit(Base):
    """ Fedora's `Wiki <https://fedoraproject.org/wiki>`_ has a fedmsg hook
    that publishes messages like this one when a user edits a page.
    """
    expected_title = "wiki.article.edit"
    expected_subti = 'Ralph made a wiki edit to "Messaging SIG"'
    expected_link = "https://this-is-a-link.org"
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
    """ Fedora's `Wiki <https://fedoraproject.org/wiki>`_ hook also publishes
    messages when a user upload some media (like a video or a picture).
    """
    expected_title = "wiki.upload.complete"
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
                "mPrefixedText": "File:Cat.jpg",
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
    """ There is a script called ``pkgdb2branch`` that gets run by an SCM
    admin as part of the new package process.  Messages on this topic are
    emitted from that script when it is instructed to carry out a "mass
    branch" of all packages.
    """
    expected_title = "git.mass_branch.start"
    expected_subti = "dgilmore started a mass branch"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "168a37a06ac9b4dbcf4f2e0e11de6a1332c7aead2313b04016cea0c5a848263e" + \
        "?s=64&d=retro"
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
    """ There is a script called ``pkgdb2branch`` that gets run by an SCM
    admin as part of the new package process.  Messages on this topic are
    emitted from that script when it **finishes** a "mass branch".
    """
    expected_title = "git.mass_branch.complete"
    expected_subti = "mass branch started by dgilmore completed"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "168a37a06ac9b4dbcf4f2e0e11de6a1332c7aead2313b04016cea0c5a848263e" + \
        "?s=64&d=retro"
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
    """ There is a script called ``pkgdb2branch`` that gets run by an SCM
    admin as part of the new package process.  Typically, when an `SCM Admin
    Request <https://fedoraproject.org/wiki/Package_SCM_admin_requests>`_ is
    approved, the scm admin will add the new package or branch to the package
    database.  *After that*, the scm admin will run ``pkgdb2branch`` to create
    the branch in git on the file system.  Messages of **this** topic are
    published when that process **begins**.
    """
    expected_title = "git.pkgdb2branch.start"
    expected_subti = "limburgher started a run of pkgdb2branch"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "67fc36d5974ea45ec922a650dc117d83acf0a1f646cd17ba80e9e0fe6e2ed164" + \
        "?s=64&d=retro"
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
    """ There is a script called ``pkgdb2branch`` that gets run by an SCM
    admin as part of the new package process.  Typically, when an `SCM Admin
    Request <https://fedoraproject.org/wiki/Package_SCM_admin_requests>`_ is
    approved, the scm admin will add the new package or branch to the package
    database.  *After that*, the scm admin will run ``pkgdb2branch`` to create
    the branch in git on the file system.  Messages of **this** topic are
    published when that process **completes**.
    """
    expected_title = "git.pkgdb2branch.complete"
    expected_subti = "run of pkgdb2branch started by limburgher completed"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "67fc36d5974ea45ec922a650dc117d83acf0a1f646cd17ba80e9e0fe6e2ed164" + \
        "?s=64&d=retro"
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
    """ There is a script called ``pkgdb2branch`` that gets run by an SCM
    admin as part of the new package process.  Typically, when an `SCM Admin
    Request <https://fedoraproject.org/wiki/Package_SCM_admin_requests>`_ is
    approved, the scm admin will add the new package or branch to the package
    database.  *After that*, the scm admin will run ``pkgdb2branch`` to create
    the branch in git on the file system.  Messages of **this** topic are
    published when that process **completes**.

    *Sometimes* that process can produce errors.  Here's an example of a
    message from a failed ``pkgdb2branch`` run.
    """
    expected_title = "git.pkgdb2branch.complete"
    expected_subti = "run of pkgdb2branch started by limburgher completed" + \
        " with 1 error"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "67fc36d5974ea45ec922a650dc117d83acf0a1f646cd17ba80e9e0fe6e2ed164" + \
        "?s=64&d=retro"
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
            "branchedPackages": None,
        },
    }


class TestPkgdb2BrRunCompleteWithErrors(Base):
    """ There is a script called ``pkgdb2branch`` that gets run by an SCM
    admin as part of the new package process.  Typically, when an `SCM Admin
    Request <https://fedoraproject.org/wiki/Package_SCM_admin_requests>`_ is
    approved, the scm admin will add the new package or branch to the package
    database.  *After that*, the scm admin will run ``pkgdb2branch`` to create
    the branch in git on the file system.  Messages of **this** topic are
    published when that process **completes**.

    *Sometimes* that process can produce errors.  Here's an example of a
    message from a failed ``pkgdb2branch`` run (on multiple packages)
    """
    expected_title = "git.pkgdb2branch.complete"
    expected_subti = "run of pkgdb2branch started by limburgher completed" + \
        " with 2 errors"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "67fc36d5974ea45ec922a650dc117d83acf0a1f646cd17ba80e9e0fe6e2ed164" + \
        "?s=64&d=retro"
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
    """ Support old school pkgdb2branch messages.  This don't get published
    anymore, but :mod:`fedmsg.meta` needs to support them since they are
    stored *forever* in datanommer.
    """

    expected_title = "git.branch.valgrind.master"
    expected_subti = \
        "limburgher created branch 'master' for the 'valgrind' package"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "67fc36d5974ea45ec922a650dc117d83acf0a1f646cd17ba80e9e0fe6e2ed164" + \
        "?s=64&d=retro"
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
    """ There is a script called ``pkgdb2branch`` that gets run by an SCM
    admin as part of the new package process.  Typically, when an `SCM Admin
    Request <https://fedoraproject.org/wiki/Package_SCM_admin_requests>`_ is
    approved, the scm admin will add the new package or branch to the package
    database.  *After that*, the scm admin will run ``pkgdb2branch`` to create
    the branch in git on the file system.  Messages of **this** topic are
    published `for each new branch` that that process **creates**.
    """
    expected_title = "git.branch"
    expected_subti = \
        "limburgher created branch 'master' for the 'valgrind' package"
    expected_link = \
        "http://pkgs.fedoraproject.org/cgit/valgrind.git/log/?h=master"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "67fc36d5974ea45ec922a650dc117d83acf0a1f646cd17ba80e9e0fe6e2ed164" + \
        "?s=64&d=retro"
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
    """ Messages like this one are published when **new sources** are
    uploaded to the "lookaside cache".
    """

    expected_title = "git.lookaside.new"
    expected_subti = 'jnovy uploaded pst-diffraction.doc.tar.xz for texlive'
    expected_icon = "https://apps.fedoraproject.org/img/icons/git-logo.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "e0e8e0c4d995109cdac8ae4eb5766a73cf09c7a8d2d8bac57f761e6223ca094b?s=64&" + \
        "d=retro"
    expected_link = 'http://pkgs.fedoraproject.org/lookaside/pkgs/' + \
        'texlive/pst-diffraction.doc.tar.xz/' + \
        'dacad985394b3977f9dcf0c75f51a357/' + \
        'pst-diffraction.doc.tar.xz'
    expected_long_form = 'jnovy uploaded a file to the lookaside cache ' + \
    'for texlive\n\ndacad985394b3977f9dcf0c75f51a357  pst-diffraction.doc.tar.xz'
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
    """ Support oldschool lookaside messages.  :( """

    expected_title = "git.lookaside.texlive.new"
    expected_subti = 'jnovy uploaded pst-diffraction.doc.tar.xz for texlive'
    expected_icon = "https://apps.fedoraproject.org/img/icons/git-logo.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "e0e8e0c4d995109cdac8ae4eb5766a73cf09c7a8d2d8bac57f761e6223ca094b?s=64&" + \
        "d=retro"
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
    """ Support super-duper oldschool git messages.  :(:( """

    expected_title = "git.receive.valgrind.master"
    expected_subti = 'mjw pushed to valgrind (master).  ' + \
        '"Clear CFLAGS CXXFLAGS LDFLAGS. (..more)"'
    expected_link = "http://pkgs.fedoraproject.org/cgit/" + \
        "valgrind.git/commit/" + \
        "?h=master&id=7a98f80d9b61ce167e4ef8129c81ed9284ecf4e1"
    expected_icon = "https://apps.fedoraproject.org/img/icons/git-logo.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "923419d315c8f23eface39852bf32a5f?s=64&" + \
        "d=retro"
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
    """ Support oldschool "fedpkg push" messages.  :( """

    expected_title = "git.receive.valgrind.master"
    expected_subti = 'mjw pushed to valgrind (master).  ' + \
        '"Clear CFLAGS CXXFLAGS LDFLAGS. (..more)"'
    expected_link = "http://pkgs.fedoraproject.org/cgit/" + \
        "valgrind.git/commit/" + \
        "?h=master&id=7a98f80d9b61ce167e4ef8129c81ed9284ecf4e1"
    expected_icon = "https://apps.fedoraproject.org/img/icons/git-logo.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "923419d315c8f23eface39852bf32a5f?s=64&" + \
        "d=retro"
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
    """ Messages like this one are published when somebody runs "fedpkg push"
    on a package.  Sometimes, the git message may be multiple lines long like:
    """
    expected_title = "git.receive"
    expected_subti = 'mjw pushed to valgrind (master).  ' + \
        '"Clear CFLAGS CXXFLAGS LDFLAGS. (..more)"'
    expected_link = "http://pkgs.fedoraproject.org/cgit/" + \
        "valgrind.git/commit/" + \
        "?h=master&id=7a98f80d9b61ce167e4ef8129c81ed9284ecf4e1"
    expected_icon = "https://apps.fedoraproject.org/img/icons/git-logo.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "923419d315c8f23eface39852bf32a5f?s=64&" + \
        "d=retro"
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
    """ Messages like this one are published when somebody runs "fedpkg push"
    on a package.  The whole git message is included for each commit.
    """
    expected_title = "git.receive"
    expected_subti = 'spot pushed to ember (master).  ' + \
        '"another missing patch? ridiculous."'
    expected_link = "http://pkgs.fedoraproject.org/cgit/" + \
        "ember.git/commit/" + \
        "?h=master&id=aa2df80f3d8dd217c7cbfe2d3451190028f3fe14"
    expected_icon = "https://apps.fedoraproject.org/img/icons/git-logo.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "461761d9572bdc1d04925a1125a41797?s=64&" + \
        "d=retro"
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


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
