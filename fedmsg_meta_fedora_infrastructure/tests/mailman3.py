# This file is part of fedmsg
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
""" Tests for mailman3 messages """

import unittest

from fedmsg_meta_fedora_infrastructure.tests.base import Base

from .common import add_doc


class TestMailman3NewReply(Base):
    """ `Discussion lists for the Fedora Project
    <https://lists.fedoraproject.org>`_ run on mailman3.  When a new
    message is published on a list, fedmsg will pop out one of these messages.
    The following is an example of a reply to a thread.
    """

    expected_title = "mailman.receive"
    expected_subti = ("On the devel list, nim replied to "
                      "'[Devel] Re:Software Management call for RFEs'")
    expected_link = ("https://lists.fedoraproject.org/archives/list/"
                     "devel@mm3test.fedoraproject.org/message/"
                     "S3PHLMD7PGWXXLBN3GENHVK7JJ37UWLJ/")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "e13c266c61de5e79cf37a99b94d4d4462d6857fe8a5dbdde9e041ae01b14a7db"
        "?s=64&d=retro")

    expected_packages = set([])
    expected_usernames = set([
        # We convert emails to fas usernames if we can.
        'nim',
    ])
    expected_objects = set([
        # There is only one item in this set, not four.  It's just long.
        "devel/5de4f14ae46cce6de03cf68ca06526a9.squirrel@arekh.dyndns.org/"
        "519DFB93.1060502@laiskiainen.org/"
        "d4f0cefb4a7b845451ecab2c4026fe4d.squirrel@arekh.dyndns.org/"
        "message",
    ])
    msg = {
        "i": 4,
        "msg": {
            "mlist": {
                "list_name": "devel"
            },
            "msg": {
                "delivered-to": "devel@lists.fedoraproject.org",
                "from": "\"Nicolas Mailhot\" <nicolas.mailhot@laposte.net>",
                "x-mailman-rule-hits": "nonmember-moderation",
                "to": "\"Development discussions related to Fedora\" "
                "<devel@lists.fedoraproject.org>",
                "cc": None,
                "in-reply-to": "<519DFB93.1060502@laiskiainen.org>",
                "x-message-id-hash": "S3PHLMD7PGWXXLBN3GENHVK7JJ37UWLJ",
                "x-mailman-rule-misses": "approved; emergency; loop; "
                "member-moderation; administrivia; implicit-dest; "
                "max-recipients; max-size; news-moderation; no-subject; "
                "suspicious-header",
                "references": "<5de4f14ae46cce6de03cf68ca06526a9.squirrel@"
                "arekh.dyndns.org>\n\t<519DFB93.1060502@laiskiainen.org>",
                "archived-at": "<https://lists.fedoraproject.org/archives/"
                "list/devel@mm3test.fedoraproject.org/message/"
                "S3PHLMD7PGWXXLBN3GENHVK7JJ37UWLJ/>",
                "message-id": "<d4f0cefb4a7b845451ecab2c4026fe4d.squirrel@"
                "arekh.dyndns.org>",
                "subject": "[Devel] Re:Software Management call for RFEs"
            }
        },
        "topic": "org.fedoraproject.dev.mailman.receive",
        "username": "mailman",
        "timestamp": 1369322289.6794021
    }


class TestMailman3NewMail(Base):
    """ `Discussion lists for the Fedora Project
    <https://lists.fedoraproject.org>`_ run on mailman3.  When a new
    message is published on a list, fedmsg will pop out one of these messages.
    The following is an example of a new thread being started.
    """

    expected_title = "mailman.receive"
    expected_subti = ("jreznik@redhat.com wrote '[Devel] Fedora 19 Beta status"
                      " is Go, release on May 28, 2013' to the devel list")
    expected_link = ("https://lists.fedoraproject.org/archives/list/"
                     "devel@mm3test.fedoraproject.org/message/"
                     "HDMTECNRNUHZTSDGM2FDK6LGCMAS2PZ4/")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "35012533ff5290bd2231c7133bd07896?s=64&d=retro")

    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set([
        "devel/306436886.6773069.1369333725371.JavaMail.root@redhat.com/message",
    ])
    msg = {
        "i": 1,
        "msg": {
            "mlist": {
                "list_name": "devel"
            },
            "msg": {
                "delivered-to": "devel@lists.fedoraproject.org",
                "from": "Jaroslav Reznik <jreznik@redhat.com>",
                "x-mailman-rule-hits": "nonmember-moderation",
                "to": "devel-announce@lists.fedoraproject.org,\n\t"
                "test-announce@lists.fedoraproject.org,\n\t"
                "Fedora Logistics List <logistics@lists.fedoraproject.org>",
                "cc": None,
                "in-reply-to": None,
                "x-message-id-hash": "HDMTECNRNUHZTSDGM2FDK6LGCMAS2PZ4",
                "x-mailman-rule-misses": "approved; emergency; loop; "
                "member-moderation; administrivia; implicit-dest; "
                "max-recipients; max-size; news-moderation; no-subject; "
                "suspicious-header",
                "references": None,
                "archived-at": "/list/devel@mm3test.fedoraproject.org/"
                "message/HDMTECNRNUHZTSDGM2FDK6LGCMAS2PZ4/",
                "message-id": "<306436886.6773069.1369333725371.JavaMail."
                "root@redhat.com>",
                "subject": "[Devel] Fedora 19 Beta status is Go, release on "
                "May 28, 2013"
            }
        },
        "topic": "org.fedoraproject.dev.mailman.receive",
        "username": "mailman",
        "timestamp": 1369334087.9298041
    }


add_doc(locals())
