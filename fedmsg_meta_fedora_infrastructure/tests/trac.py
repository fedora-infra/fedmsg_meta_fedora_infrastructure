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
""" Tests for trac messages """

import unittest

from fedmsg.tests.test_meta import Base

from .common import add_doc

_long_form_new = """Summary: test fedmsg
Description: just testing fedmsg.
"""

_long_form_comment = """Summary: Test ticket for fedmsg plugin
Comment: Testing.
"""

_long_form_reopen = """Summary: Test ticket for fedmsg plugin
Description: I installed the fedmsg plugin.
"""

_long_form_closed = """Summary: Test ticket for fedmsg plugin
Comment: Closing.
"""


class TestTracTicketCreate(Base):
    """ Messages are published on this topic when a user opens a new ticket
    on a `fedorahosted <https://fedorahosted.org/>`_ trac instance.
    """

    expected_title = "trac.ticket.new"
    expected_subti = "ralph opened a new ticket on the moksha trac instance"
    expected_long_form = _long_form_new
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c"
        "?s=64&d=retro")
    expected_packages = set()
    expected_usernames = set(['ralph', 'lmacken'])
    expected_objects = set([
        'moksha/ticket/249',
    ])
    expected_link = "https://fedorahosted.org/moksha/ticket/249"

    msg = {
        "username": "apache",
        "i": 1,
        "timestamp": 1368043636.2942779,
        "topic": "org.fedoraproject.prod.trac.ticket.new",
        "msg": {
            "agent": "ralph",
            "instance": {
                "project_url": "http://moksha.fedorahosted.org",
                "project_name": "moksha",
                "base_url": "https://fedorahosted.org/moksha/",
                "project_description": "Moksha is an opensource plugin-based "
                "web framework that aims to simplify the creation of live "
                "widget dashboards.",
                "project_icon": "common/trac.ico"
            },
            "ticket": {
                "id": 249,
                "status": "new",
                "changetime": 1368043635.0,
                "description": "just testing fedmsg.",
                "reporter": "ralph",
                "cc": "",
                "milestone": "__unclassified__",
                "component": "moksha",
                "blockedby": "",
                "summary": "test fedmsg",
                "priority": "major",
                "keywords": "",
                "time": 1368043635.0,
                "owner": "lmacken",
                "type": "defect",
                "blocking": ""
            }
        }
    }


class TestTracTicketChange(Base):
    """ Messages get emitted on this topic when someone updates a trac ticket
    on a `fedorahosted <https://fedorahosted.org>`_ trac instance.
    """

    expected_title = "trac.ticket.update"
    expected_subti = "ralph updated a ticket on the moksha trac instance"
    expected_long_form = _long_form_comment
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c"
        "?s=64&d=retro")
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'moksha/ticket/249',
    ])
    expected_link = "https://fedorahosted.org/moksha/ticket/249"

    msg = {
        "username": "apache",
        "i": 1,
        "timestamp": 1368040146.688652,
        "topic": "org.fedoraproject.prod.trac.ticket.update",
        "msg": {
            "agent": "ralph",
            "comment": "Testing.",
            "instance": {
                "project_url": "http://moksha.fedorahosted.org",
                "project_name": "moksha",
                "base_url": "https://fedorahosted.org/moksha/",
                "project_description": "Moksha is an opensource plugin-based "
                "web framework that aims to simplify the creation of live "
                "widget dashboards.",
                "project_icon": "common/trac.ico"
            },
            "ticket": {
                "id": 249,
                "status": "new",
                "changetime": 1368040146.0,
                "description": "I installed the fedmsg plugin.",
                "reporter": "ralph",
                "cc": "",
                "resolution": "",
                "milestone": "__unclassified__",
                "component": "moksha",
                "blockedby": "",
                "summary": "Test ticket for fedmsg plugin",
                "priority": "major",
                "keywords": "",
                "time": 1368039807.0,
                "owner": "",
                "type": "defect",
                "blocking": ""
            },
            "old_values": {},
            "author": "ralph"
        }
    }


class TestTracTicketChangeReopen(Base):
    """ Here's another example of an edit to a trac ticket.  Here's one where
    the ticket was originally closed and then was re-opened.
    """

    expected_title = "trac.ticket.update"
    expected_subti = "ralph reopened a ticket on the moksha trac instance"
    expected_long_form = _long_form_reopen
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c"
        "?s=64&d=retro")
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'moksha/ticket/249',
    ])
    expected_link = "https://fedorahosted.org/moksha/ticket/249"

    msg = {
        "username": "apache",
        "i": 1,
        "timestamp": 1368040591.046669,
        "topic": "org.fedoraproject.prod.trac.ticket.update",
        "msg": {
            "agent": "ralph",
            "comment": "",
            "instance": {
                "project_url": "http://moksha.fedorahosted.org",
                "project_name": "moksha",
                "base_url": "https://fedorahosted.org/moksha/",
                "project_description": "Moksha is an opensource plugin-based "
                "web framework that aims to simplify the creation of live "
                "widget dashboards.",
                "project_icon": "common/trac.ico"
            },
            "ticket": {
                "id": 249,
                "status": "reopened",
                "changetime": 1368040591.0,
                "description": "I installed the fedmsg plugin.",
                "reporter": "ralph",
                "cc": "",
                "resolution": "",
                "milestone": "__unclassified__",
                "component": "moksha",
                "blockedby": "",
                "summary": "Test ticket for fedmsg plugin",
                "priority": "major",
                "keywords": "",
                "time": 1368039807.0,
                "owner": "",
                "type": "defect",
                "blocking": ""
            },
            "old_values": {
                "status": "closed",
                "resolution": "wontfix"
            },
            "author": "ralph"
        }
    }


class TestTracTicketChangeClosed(Base):
    """ Here's yet another example of an edit to a trac ticket.
    In this one, the user has *closed* a ticket.
    """

    expected_title = "trac.ticket.update"
    expected_subti = ("ralph closed a ticket on the moksha trac "
                      "instance as 'wontfix'")
    expected_long_form = _long_form_closed
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c"
        "?s=64&d=retro")
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'moksha/ticket/249',
    ])
    expected_link = "https://fedorahosted.org/moksha/ticket/249"

    msg = {
        "username": "apache",
        "i": 1,
        "timestamp": 1368040802.7476659,
        "topic": "org.fedoraproject.prod.trac.ticket.update",
        "msg": {
            "agent": "ralph",
            "comment": "Closing.",
            "instance": {
                "project_url": "http://moksha.fedorahosted.org",
                "project_name": "moksha",
                "base_url": "https://fedorahosted.org/moksha/",
                "project_description": "Moksha is an opensource plugin-based "
                "web framework that aims to simplify the creation of live "
                "widget dashboards.",
                "project_icon": "common/trac.ico"
            },
            "ticket": {
                "id": 249,
                "status": "closed",
                "changetime": 1368040802.0,
                "description": "I installed the fedmsg plugin.",
                "reporter": "ralph",
                "cc": "",
                "resolution": "wontfix",
                "milestone": "__unclassified__",
                "component": "moksha",
                "blockedby": "",
                "summary": "Test ticket for fedmsg plugin",
                "priority": "major",
                "keywords": "",
                "time": 1368039807.0,
                "owner": "",
                "type": "defect",
                "blocking": ""
            },
            "old_values": {
                "status": "reopened",
                "resolution": ""
            },
            "author": "ralph"
        }
    }


class TestTracTicketDelete(Base):
    """ You can actually permanently delete trac tickets, which is kind of
    crazy.  If you do, a message looking something like this will be published.
    """

    expected_title = "trac.ticket.delete"
    expected_subti = ("ralph straight-up deleted a ticket on the moksha "
                      "trac instance")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c"
        "?s=64&d=retro")
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'moksha/ticket/249',
    ])
    expected_link = "https://fedorahosted.org/moksha/ticket/249"

    msg = {
        "username": "apache",
        "i": 1,
        "timestamp": 1368042385.176218,
        "topic": "org.fedoraproject.prod.trac.ticket.delete",
        "msg": {
            "agent": "ralph",
            "instance": {
                "project_url": "http://moksha.fedorahosted.org",
                "project_name": "moksha",
                "base_url": "https://fedorahosted.org/moksha/",
                "project_description": "Moksha is an opensource plugin-based "
                "web framework that aims to simplify the creation of live "
                "widget dashboards.",
                "project_icon": "common/trac.ico"
            },
            "ticket": {
                "id": 249,
                "status": "closed",
                "changetime": 1368042301.0,
                "description": "I installed the fedmsg plugin.",
                "reporter": "ralph",
                "cc": "",
                "resolution": "fixed",
                "milestone": "__unclassified__",
                "component": "moksha",
                "blockedby": "",
                "summary": "Test ticket for fedmsg plugin",
                "priority": "major",
                "keywords": "",
                "time": 1368039807.0,
                "owner": "",
                "type": "defect",
                "blocking": ""
            }
        }
    }


class TestTracWikiCreate(Base):
    """ Messages of this topic get published when someone creates a new wiki
    page on a `fedorahosted <https://fedorahosted.org>`_ trac instance.
    """

    expected_title = "trac.wiki.page.new"
    expected_subti = ("ralph created a new 'watwat' wiki page on the "
                      "moksha trac instance")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c"
        "?s=64&d=retro")
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'moksha/wiki/watwat',
    ])
    expected_link = "https://fedorahosted.org/moksha/wiki/watwat"

    msg = {
        "username": "apache",
        "i": 1,
        "timestamp": 1368042663.078511,
        "topic": "org.fedoraproject.prod.trac.wiki.page.new",
        "msg": {
            "agent": "ralph",
            "instance": {
                "project_url": "http://moksha.fedorahosted.org",
                "project_name": "moksha",
                "base_url": "https://fedorahosted.org/moksha/",
                "project_description": "Moksha is an opensource plugin-based "
                "web framework that aims to simplify the creation of live "
                "widget dashboards.",
                "project_icon": "common/trac.ico"
            },
            "page": {
                "name": "watwat",
                "comment": "",
                "author": "ralph",
                "text": "This is a test wiki page for fedmsg.",
                "version": 1,
                "time": 1368042662.0
            }
        }
    }


class TestTracWikiEdit(Base):
    """ Messages get emitted on this topic when someone updates a wiki page
    on a `fedorahosted <https://fedorahosted.org>`_ trac instance.
    """

    expected_title = "trac.wiki.page.update"
    expected_subti = ("ralph updated the 'WikiStart' wiki page on the "
                      "moksha trac instance")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c"
        "?s=64&d=retro")
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'moksha/wiki/WikiStart',
    ])
    expected_link = ("https://fedorahosted.org/moksha/wiki/WikiStart"
                     "?action=diff&version=47")

    msg = {
        "username": "apache",
        "i": 1,
        "timestamp": 1368038919.389492,
        "topic": "org.fedoraproject.prod.trac.wiki.page.update",
        "msg": {
            "agent": "ralph",
            "comment": "",
            "author": "ralph",
            "instance": {
                "project_url": "http://moksha.fedorahosted.org",
                "project_name": "moksha",
                "base_url": "https://fedorahosted.org/moksha/",
                "project_description": "Moksha is an opensource plugin-based "
                "web framework that aims to simplify the creation of live "
                "widget dashboards.",
                "project_icon": "common/trac.ico"
            },
            "version": 47,
            "t": 1368038919.0,
            "page": {
                "name": "WikiStart",
                "comment": "",
                "author": "ralph",
                "text": " ... the full text of the wiki page goes here .. ",
                "version": 47,
                "time": 1368038919.0
            }
        }
    }


class TestTracWikiDelete(Base):
    """ These messages are fired off whenever a user *deletes* a wiki article
    on a `fedorahosted <https://fedorahosted.org>`_ trac instance.
    """
    expected_title = "trac.wiki.page.delete"
    expected_subti = ("ralph straight-up deleted the 'watwat' wiki page "
                      "on the moksha trac instance")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c"
        "?s=64&d=retro")
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'moksha/wiki/watwat',
    ])
    expected_link = "https://fedorahosted.org/moksha/wiki/watwat"

    msg = {
        "username": "apache",
        "i": 2,
        "timestamp": 1368043573.12363,
        "topic": "org.fedoraproject.prod.trac.wiki.page.delete",
        "msg": {
            "agent": "ralph",
            "instance": {
                "project_url": "http://moksha.fedorahosted.org",
                "project_name": "moksha",
                "base_url": "https://fedorahosted.org/moksha/",
                "project_description": "Moksha is an opensource plugin-based "
                "web framework that aims to simplify the creation of live "
                "widget dashboards.",
                "project_icon": "common/trac.ico"
            },
            "page": {
                "comment": "",
                "name": "watwat",
                "author": "",
                "text": "",
                "version": 0,
                "time": None,
            }
        }
    }


class TestTracWikiVersionDelete(Base):
    """ Messages are published on this topic when a user deletes a
    particular *version* of a page on a `fedorahosted
    <https://fedorahosted.org>`_ trac instance.
    """

    expected_title = "trac.wiki.page.version.delete"
    expected_subti = ("ralph deleted a version of the 'WikiStart' "
                      "wiki page on the moksha trac instance")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c"
        "?s=64&d=retro")
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'moksha/wiki/WikiStart',
    ])
    expected_link = ("https://fedorahosted.org/moksha/wiki/WikiStart"
                     "?action=diff&version=47")

    msg = {
        "username": "apache",
        "i": 2,
        "timestamp": 1368043436.1444981,
        "topic": "org.fedoraproject.prod.trac.wiki.page.version.delete",
        "msg": {
            "agent": "ralph",
            "instance": {
                "project_url": "http://moksha.fedorahosted.org",
                "project_name": "moksha",
                "base_url": "https://fedorahosted.org/moksha/",
                "project_description": "Moksha is an opensource plugin-based "
                "web framework that aims to simplify the creation of live "
                "widget dashboards.",
                "project_icon": "common/trac.ico"
            },
            "page": {
                "comment": "",
                "name": "WikiStart",
                "author": "ralph",
                "text": " .. wiki page text goes here. ..",
                "version": 47,
                "time": 1368038919.0
            },
        }
    }


class TestTracWikiRename(Base):
    """ Messages are published on this topic when a user renames a wiki
    page on a `fedorahosted <https://fedorahosted.org>_` trac instance.
    """

    expected_title = "trac.wiki.page.rename"
    expected_subti = ("ralph renamed the wiki page 'watwat' to 'watwat2' "
                      "on the moksha trac instance")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c"
        "?s=64&d=retro")
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'moksha/wiki/watwat',
        'moksha/wiki/watwat2',
    ])
    expected_link = "https://fedorahosted.org/moksha/wiki/watwat2"

    msg = {
        "username": "apache",
        "i": 1,
        "timestamp": 1368043322.1105361,
        "topic": "org.fedoraproject.prod.trac.wiki.page.rename",
        "msg": {
            "agent": "ralph",
            "instance": {
                "project_url": "http://moksha.fedorahosted.org",
                "project_name": "moksha",
                "base_url": "https://fedorahosted.org/moksha/",
                "project_description": "Moksha is an opensource plugin-based "
                "web framework that aims to simplify the creation of live "
                "widget dashboards.",
                "project_icon": "common/trac.ico"
            },
            "page": {
                "comment": "",
                "name": "watwat2",
                "author": "ralph",
                "text": "This is a test wiki page for fedmsg.",
                "version": 1,
                "time": 1368042662.0
            },
            "old_name": "watwat"
        }
    }


class TestTracChangesetCreate(Base):
    """ Messages are published on this topic when a users pushes commits
    to a `fedorahosted <https://fedorahosted.org>`_ git repository.

    The message format is very similar to the ``git.receive`` message type
    for Fedora packages.
    """

    expected_title = "trac.git.receive"
    expected_subti = ("ralph pushed some commits to the 'moksha' "
                      "fedorahosted git repository")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c"
        "?s=64&d=retro")
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'moksha/git/README.rst',
    ])
    expected_link = ("https://git.fedorahosted.org/cgit/moksha.git/"
                     "commit/?id=24bcd20d08a68320f82951ce20959bc6a1a6e79c")

    msg = {
        "username": "ralph",
        "i": 1,
        "timestamp": 1368046115.802794,
        "topic": "org.fedoraproject.prod.trac.git.receive",
        "msg": {
            "commit": {
                "username": "ralph",
                "stats": {
                    "files": {
                        "README.rst": {
                            "deletions": 0,
                            "lines": 1,
                            "insertions": 1
                        }
                    },
                    "total": {
                        "deletions": 0,
                        "files": 1,
                        "insertions": 1,
                        "lines": 1
                    }
                },
                "name": "Ralph Bean",
                "rev": "24bcd20d08a68320f82951ce20959bc6a1a6e79c",
                "agent": "ralph",
                "summary": "Another commit to test fedorahosted fedmsg.",
                "repo": "moksha",
                "branch": "dev",
                "message": "Another commit to test fedorahosted fedmsg.\n",
                "email": "rbean@redhat.com"
            }
        }
    }


class TestTracDocsChangesetCreate(Base):
    """ Messages are published on this topic when a users pushes commits
    to a `fedorahosted <https://fedorahosted.org>`_ git repository.

    The message format is very similar to the ``git.receive`` message type
    for Fedora packages.
    """

    expected_title = "trac.git.receive"
    expected_subti = ("ralph pushed some commits to the "
                      "'docs/about-fedora' fedorahosted git repository")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c"
        "?s=64&d=retro")
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'docs/about-fedora/git/README.rst',
    ])
    expected_link = (
        "https://git.fedorahosted.org/cgit/docs/"
        "about-fedora.git/commit/?id="
        "24bcd20d08a68320f82951ce20959bc6a1a6e79c"
    )

    msg = {
        "username": "ralph",
        "i": 1,
        "timestamp": 1368046115.802794,
        "topic": "org.fedoraproject.prod.trac.git.receive",
        "msg": {
            "commit": {
                "username": "ralph",
                "stats": {
                    "files": {
                        "README.rst": {
                            "deletions": 0,
                            "lines": 1,
                            "insertions": 1
                        }
                    },
                    "total": {
                        "deletions": 0,
                        "files": 1,
                        "insertions": 1,
                        "lines": 1
                    }
                },
                "name": "Ralph Bean",
                "rev": "24bcd20d08a68320f82951ce20959bc6a1a6e79c",
                "agent": "ralph",
                "summary": "Another commit to test fedorahosted fedmsg.",
                "repo": "about-fedora",
                "path": "/srv/git/docs/about-fedora.git",
                "branch": "dev",
                "message": "Another commit to test fedorahosted fedmsg.\n",
                "email": "rbean@redhat.com"
            }
        }
    }

add_doc(locals())

if __name__ == '__main__':
    unittest.main()
