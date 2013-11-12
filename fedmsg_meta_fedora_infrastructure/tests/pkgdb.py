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
""" Tests for pkgdb messages """

import unittest

from fedmsg.tests.test_meta import Base

from common import add_doc


class TestPkgdbACLUpdate(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    publishes these messages when an ACL changes on a package.
    """

    expected_title = "pkgdb.acl.update"
    expected_subti = ("ralph changed ralph's 'watchbugzilla' permission on "
                      "python-sh (EL-6) to 'Awaiting Review'")
    expected_link = "https://admin.fedoraproject.org/pkgdb/acls/name/python-sh"
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = ("http://www.gravatar.com/avatar/"
                               "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F"
                               "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png")
    expected_packages = set(['python-sh'])
    expected_usernames = set(['ralph', 'grover'])
    expected_objects = set(['python-sh/acls/EL-6/watchbugzilla/ralph'])
    msg = {
        "username": "apache",
        "i": 2,
        "timestamp": 1357576703.125622,
        "topic": "org.fedoraproject.stg.pkgdb.acl.update",
        "msg": {
            "status": "Awaiting Review",
            "username": "ralph",
            "package_listing": {
                "point_of_contact": "grover",
                "package": {
                    "upstreamurl": None,
                    "name": "python-sh",
                    "description": None,
                    "reviewurl": None,
                    "summary": "Python module to simplify calling "
                    "shell commands"
                },
                "qacontact": None,
                "collection": {
                    "pendingurltemplate": None,
                    "name": "Fedora EPEL",
                    "publishurltemplate": None,
                    "version": "6",
                    "disttag": ".el6",
                    "branchname": "EL-6"
                },
                "specfile": None
            },
            "agent": "ralph",
            "acl": "watchbugzilla"
        }
    }


class TestPkgdbPackageNew(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    publishes this message when a new package is added to the DB.  This
    typically happens near the end of the Package Review Process as a
    result of a `SCM Admin Request
    <http://fedoraproject.org/wiki/Package_SCM_admin_requests>`_.
    """
    expected_title = "pkgdb.package.new"
    expected_subti = "ralph added a new package 'php-zmq' (devel)"
    expected_link = "https://admin.fedoraproject.org/pkgdb/acls/name/php-zmq"
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = ("http://www.gravatar.com/avatar/"
                               "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F"
                               "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png")
    expected_packages = set(['php-zmq'])
    expected_usernames = set(['ralph', 'lmacken'])
    expected_objects = set(['php-zmq/create'])
    msg = {
        "username": "apache",
        "i": 3,
        "timestamp": 1357580533.5999,
        "topic": "org.fedoraproject.stg.pkgdb.package.new",
        "msg": {
            "package_listing": {
                "point_of_contact": "lmacken",
                "package": {
                    "upstreamurl": None,
                    "name": "php-zmq",
                    "description": None,
                    "reviewurl": None,
                    "summary": "PHP 0MQ/zmq/zeromq extension"
                },
                "qacontact": None,
                "collection": {
                    "pendingurltemplate": None,
                    "name": "Fedora",
                    "publishurltemplate": None,
                    "version": "19",
                    "disttag": ".f19",
                    "branchname": "devel"
                },
                "specfile": None
            },
            "agent": "ralph"
        }
    }


class TestPkgdbOwnerUpdate(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    publishes this message when a package gets an new owner.  (It is
    also published when a package is orphaned; the 'owner' field will have
    the string 'orphan' as its value.)
    """
    expected_title = "pkgdb.owner.update"
    expected_subti = "ralph changed owner of php-zmq (EL-6) to 'orphan'"
    expected_link = "https://admin.fedoraproject.org/pkgdb/acls/name/php-zmq"
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = ("http://www.gravatar.com/avatar/"
                               "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F"
                               "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png")
    expected_packages = set(['php-zmq'])
    expected_usernames = set(['ralph'])
    expected_objects = set(['php-zmq/owner/EL-6'])
    msg = {
        "username": "apache",
        "i": 3,
        "timestamp": 1357580533.5999,
        "topic": "org.fedoraproject.stg.pkgdb.owner.update",
        "msg": {
            "package_listing": {
                "point_of_contact": "orphan",
                "package": {
                    "upstreamurl": None,
                    "name": "php-zmq",
                    "description": None,
                    "reviewurl": None,
                    "summary": "PHP 0MQ/zmq/zeromq extension"
                },
                "qacontact": None,
                "collection": {
                    "pendingurltemplate": None,
                    "name": "Fedora EPEL",
                    "publishurltemplate": None,
                    "version": "6",
                    "disttag": ".el6",
                    "branchname": "EL-6"
                },
                "specfile": None
            },
            "agent": "ralph"
        }
    }


class TestLegacyPkgdbACLRequestToggle(Base):
    """ The old Fedora Package DB1 published this message when an ACL request
    was toggled on a package.
    """
    expected_title = "pkgdb.acl.request.toggle"
    expected_subti = "ralph has requested 'commit' on php-zmq (EL-6)"
    expected_link = "https://admin.fedoraproject.org/pkgdb/acls/name/php-zmq"
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = ("http://www.gravatar.com/avatar/"
                               "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F"
                               "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png")
    expected_packages = set(['php-zmq'])
    expected_usernames = set(['ralph'])
    expected_objects = set(['php-zmq/acls/EL-6/commit/ralph'])
    msg = {
        "username": "apache",
        "i": 2,
        "timestamp": 1357581512.006664,
        "topic": "org.fedoraproject.stg.pkgdb.acl.request.toggle",
        "msg": {
            "acl_action": "requested",
            "package_listing": {
                "owner": "orphan",
                "package": {
                    "upstreamurl": None,
                    "name": "php-zmq",
                    "description": None,
                    "reviewurl": None,
                    "summary": "PHP 0MQ/zmq/zeromq extension"
                },
                "qacontact": None,
                "collection": {
                    "pendingurltemplate": None,
                    "name": "Fedora EPEL",
                    "publishurltemplate": None,
                    "version": "6",
                    "disttag": ".el6",
                    "branchname": "EL-6"
                },
                "specfile": None
            },
            "acl_status": "Awaiting Review",
            "agent": "ralph",
            "acl": "commit"
        }
    }


class TestLegacyPkgdbPackageUpdate(Base):
    """ Test old school messages. """
    expected_title = "pkgdb.package.update"
    expected_subti = "ralph made some updates to php-zmq"
    expected_link = "https://admin.fedoraproject.org/pkgdb/acls/name/php-zmq"
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = ("http://www.gravatar.com/avatar/"
                              "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F"
                              "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png")
    expected_packages = set(['php-zmq'])
    expected_usernames = set(['ralph'])
    expected_objects = set(['php-zmq/update'])
    msg = {
        "username": "apache",
        "i": 2,
        "timestamp": 1357581512.006664,
        "topic": "org.fedoraproject.stg.pkgdb.package.update",
        "msg": {
            "acl_action": "requested",
            "package": "php-zmq",
            "agent": "ralph",
        },
    }


class TestPkgdbPackageUpdate(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    publishes this message when metadata for a package is updated.
    """
    expected_title = "pkgdb.package.update"
    expected_subti = "ralph made some updates to guake"
    expected_link = "https://admin.fedoraproject.org/pkgdb/acls/name/guake"
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = ("http://www.gravatar.com/avatar/"
                               "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F"
                               "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png")
    expected_packages = set(['guake'])
    expected_usernames = set(['ralph', 'pingou'])
    expected_objects = set(['guake/update'])
    msg = {
        "username": "apache",
        "i": 144,
        "timestamp": 1379605523.496933,
        "msg_id": "2013-c131fb95-0a2e-4426-95c3-09766e017d29",
        "topic": "org.fedoraproject.dev.pkgdb.package.update",
        "msg": {
            "status": "Approved",
            "package_listing": {
                "package": {
                    "status": "Approved",
                    "upstream_url": "http://guake.org",
                    "name": "guake",
                    "creation_date": 1379619917.0,
                    "summary": "Top down terminal for GNOME",
                    "review_url": "https://bugzilla.redhat.com/450189"
                },
                "collection": {
                    "pendingurltemplate": None,
                    "publishurltemplate": None,
                    "branchname": "F-18",
                    "name": "Fedora",
                    "version": "18"
                },
                "point_of_contact": "pingou"
            },
            "prev_status": "Retired",
            "agent": "ralph",
            "package_name": "guake"
        }
    }


class TestPkgdbBranchClone(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    publishes messages on this topic when a new branch is cloned for a
    package.
    """
    expected_title = "pkgdb.branch.clone"
    expected_subti = "ralph branched php-zmq f18 from devel"
    expected_link = "https://admin.fedoraproject.org/pkgdb/acls/name/php-zmq"
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = ("http://www.gravatar.com/avatar/"
                               "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F"
                               "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png")
    expected_packages = set(['php-zmq'])
    expected_usernames = set(['ralph'])
    expected_objects = set(['php-zmq/branch'])

    msg = {
        "username": "apache",
        "i": 2,
        "timestamp": 1357581512.006664,
        "topic": "org.fedoraproject.stg.pkgdb.branch.clone",
        "msg": {
            "package": "php-zmq",
            "branch": "f18",
            "master": "devel",
            "agent": "ralph",
        },
    }


class TestPkgdbCritpathUpdate(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    publishes messages on this topic when the critical path status of a
    package changes (when it is either added, or removed from the critical
    path).  For example:
    """
    expected_title = "pkgdb.critpath.update"
    expected_subti = "ralph altered the critpath status for some packages"
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = ("http://www.gravatar.com/avatar/"
                               "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F"
                               "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png")
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set([])

    msg = {
        "username": "apache",
        "i": 2,
        "timestamp": 1357581512.006664,
        "topic": "org.fedoraproject.stg.pkgdb.critpath.update",
        "msg": {
            "package_listing_ids": [],
            "agent": "ralph",
            "critpath": True,
        },
    }


class TestPkgdbPackageRetire(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    publishes messages on this topic when a package is retired.  For example:
    """
    expected_title = "pkgdb.package.retire"
    expected_subti = "ralph retired php-zmq (EL-6)!"
    expected_link = "https://admin.fedoraproject.org/pkgdb/acls/name/php-zmq"
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = ("http://www.gravatar.com/avatar/"
                               "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F"
                               "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png")
    expected_packages = set(['php-zmq'])
    expected_usernames = set(['ralph'])
    expected_objects = set(['php-zmq/retire'])
    msg = {
        "username": "apache",
        "i": 2,
        "timestamp": 1357583297.886945,
        "topic": "org.fedoraproject.stg.pkgdb.package.retire",
        "msg": {
            "package_listing": {
                "owner": "orphan",
                "package": {
                    "upstreamurl": None,
                    "name": "php-zmq",
                    "description": None,
                    "reviewurl": None,
                    "summary": "PHP 0MQ/zmq/zeromq extension"
                },
                "qacontact": None,
                "collection": {
                    "pendingurltemplate": None,
                    "name": "Fedora EPEL",
                    "publishurltemplate": None,
                    "version": "6",
                    "disttag": ".el6",
                    "branchname": "EL-6"
                },
                "specfile": None
            },
            "retirement": "retired",
            "agent": "ralph"
        }
    }


class TestPkgdbUserRemove(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    when a user is removed from a package ACL.
    """
    expected_title = "pkgdb.acl.user.remove"
    expected_subti = "ralph removed ralph from php-zmq (EL-6, F18)"
    expected_link = "https://admin.fedoraproject.org/pkgdb/acls/name/php-zmq"
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = ("http://www.gravatar.com/avatar/"
                               "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F"
                               "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png")
    expected_packages = set(['php-zmq'])
    expected_usernames = set(['ralph'])
    expected_objects = set(['php-zmq/remove/ralph'])
    msg = {
        "username": "apache",
        "i": 2,
        "timestamp": 1357583297.886945,
        "topic": "org.fedoraproject.stg.pkgdb.acl.user.remove",
        "msg": {
            "package_listings": [{
                "owner": "orphan",
                "package": {
                    "upstreamurl": None,
                    "name": "php-zmq",
                    "description": None,
                    "reviewurl": None,
                    "summary": "PHP 0MQ/zmq/zeromq extension"
                },
                "qacontact": None,
                "collection": {
                    "pendingurltemplate": None,
                    "name": "Fedora EPEL",
                    "publishurltemplate": None,
                    "version": "6",
                    "disttag": ".el6",
                    "branchname": "EL-6"
                },
                "specfile": None
            }, {
                "owner": "orphan",
                "package": {
                    "upstreamurl": None,
                    "name": "php-zmq",
                    "description": None,
                    "reviewurl": None,
                    "summary": "PHP 0MQ/zmq/zeromq extension"
                },
                "qacontact": None,
                "collection": {
                    "pendingurltemplate": None,
                    "name": "Fedora",
                    "publishurltemplate": None,
                    "version": "18",
                    "disttag": ".f18",
                    "branchname": "F18"
                },
                "specfile": None
            }],
            "collections": [
                # This actually has stuff in it in prod.
            ],
            "username": "ralph",
            "agent": "ralph",
        }
    }


class TestPkgdbBranchStart(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    publishes messages like these when branching starts.
    """
    expected_title = "pkgdb.branch.start"
    expected_subti = "ralph started a branch of F-19 from devel"
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = ("http://www.gravatar.com/avatar/"
                               "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F"
                               "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png")
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_objects = set()
    msg = {
        u'username': u'threebean',
        u'i': 1,
        u'timestamp': 1379606342.105066,
        u'msg_id': u'2013-0eaf6d98-6259-4e1c-a113-e2c9284a6082',
        u'topic':
        u'org.fedoraproject.dev.pkgdb.branch.start',
        u'msg': {
            u'collection_from': {
                u'pendingurltemplate': None,
                u'publishurltemplate': None,
                u'branchname': u'devel',
                u'name': u'Fedora',
                u'version': u'devel'
            },
            u'collection_to': {
                u'pendingurltemplate': None,
                u'publishurltemplate': None,
                u'branchname': u'F-19',
                u'name': u'Fedora',
                u'version': u'19'
            },
            u'agent': u'ralph',
        },
    }


class TestPkgdbBranchComplete(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    publishes messages like these when branching completes.
    """
    expected_title = "pkgdb.branch.complete"
    expected_subti = "ralph's branch of F-19 from devel completed"
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = ("http://www.gravatar.com/avatar/"
                               "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F"
                               "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png")
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_objects = set()
    msg = {
        u'username': u'threebean',
        u'i': 1,
        u'timestamp': 1379606342.105066,
        u'msg_id': u'2013-0eaf6d98-6259-4e1c-a113-e2c9284a6082',
        u'topic':
        u'org.fedoraproject.dev.pkgdb.branch.complete',
        u'msg': {
            u'collection_from': {
                u'pendingurltemplate': None,
                u'publishurltemplate': None,
                u'branchname': u'devel',
                u'name': u'Fedora',
                u'version': u'devel'
            },
            u'collection_to': {
                u'pendingurltemplate': None,
                u'publishurltemplate': None,
                u'branchname': u'F-19',
                u'name': u'Fedora',
                u'version': u'19'
            },
            u'agent': u'ralph',
        },
    }


class TestPkgdbCollectionNew(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    publishes messages like these when an admin creates a new collection.
    """
    expected_title = "pkgdb.collection.new"
    expected_subti = "ralph created a new collection for Fedora 19"
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = ("http://www.gravatar.com/avatar/"
                               "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F"
                               "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png")
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_objects = set()
    msg = {
        u'username': u'threebean',
        u'i': 3,
        u'timestamp': 1379607327.474346,
        u'msg_id': u'2013-68fd388e-60ca-4cf6-888d-b51161798496',
        u'topic': u'org.fedoraproject.dev.pkgdb.collection.new',
        u'msg': {
            u'collection': {
                u'pendingurltemplate': None,
                u'publishurltemplate': None,
                u'branchname': u'F-19',
                u'name': u'Fedora',
                u'version': u'19',
            },
            u'agent': u'ralph',
        }
    }


class TestPkgdbCollectionUpdate(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    publishes messages like these when an admin creates a new collection.
    """
    expected_title = "pkgdb.collection.update"
    expected_subti = ("ralph updated the following fields of the Fedora 18 "
                      "collection: name, version")
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = ("http://www.gravatar.com/avatar/"
                               "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F"
                               "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png")
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_objects = set()
    msg = {
        u'username': u'threebean',
        u'i': 27,
        u'timestamp': 1379607692.198447,
        u'msg_id': u'2013-478a321f-ddfc-4d4c-adeb-c777619da15a',
        u'topic': u'org.fedoraproject.dev.pkgdb.collection.update',
        u'msg': {
            u'fields': [
                u'name',
                u'version',
            ],
            u'collection': {
                u'pendingurltemplate': u'http://.....',
                u'publishurltemplate': u'http://.....',
                u'branchname': u'f18_b',
                u'name': u'Fedora',
                u'version': u'18'
            },
            u'agent': u'ralph',
        }
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
