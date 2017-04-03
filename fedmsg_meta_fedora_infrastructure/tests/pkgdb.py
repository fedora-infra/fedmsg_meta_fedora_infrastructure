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

from .common import add_doc


class TestPkgdbACLUpdate(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    publishes these messages when an ACL changes on a package.
    """

    expected_title = "pkgdb.acl.update"
    expected_subti = ("ralph changed ralph's 'watchbugzilla' permission on "
                      "rpms/python-sh (EL-6) to 'Awaiting Review'")
    expected_link = "https://admin.fedoraproject.org/pkgdb/package/rpms/python-sh/"
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
    expected_packages = set(['python-sh'])
    expected_usernames = set(['ralph'])
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
    expected_subti = "ralph added a new package 'rpms/php-zmq' (devel)"
    expected_link = "https://admin.fedoraproject.org/pkgdb/package/rpms/php-zmq/"
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
    expected_packages = set(['php-zmq'])
    expected_usernames = set(['ralph'])
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
    expected_subti = "ralph changed owner of rpms/php-zmq (EL-6) to 'orphan'"
    expected_link = "https://admin.fedoraproject.org/pkgdb/package/rpms/php-zmq/"
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
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
    expected_subti = "ralph has requested 'commit' on rpms/php-zmq (EL-6)"
    expected_link = "https://admin.fedoraproject.org/pkgdb/package/rpms/php-zmq/"
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
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
    expected_subti = "ralph made some updates to rpms/php-zmq"
    expected_link = "https://admin.fedoraproject.org/pkgdb/package/rpms/php-zmq/"
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
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


class TestPkgdbPackageUpdateStatus(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    publishes this message when the status of a package is updated.
    """
    expected_title = "pkgdb.package.update.status"
    expected_subti = "ralph unretired rpms/guake in F-18"
    expected_link = "https://admin.fedoraproject.org/pkgdb/package/rpms/guake/"
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
    expected_packages = set(['guake'])
    expected_usernames = set(['ralph'])
    expected_objects = set(['guake/update'])
    msg = {
        "username": "apache",
        "i": 144,
        "timestamp": 1379605523.496933,
        "msg_id": "2013-c131fb95-0a2e-4426-95c3-09766e017d29",
        "topic": "org.fedoraproject.dev.pkgdb.package.update.status",
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


class TestPkgdbPackageUpdate(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    publishes this message when metadata for a package is updated.
    """
    expected_title = "pkgdb.package.update"
    expected_subti = "pkgdb_updater updated: summary, description of rpms/guake"
    expected_link = "https://admin.fedoraproject.org/pkgdb/package/rpms/guake/"
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "1ff483b03adb34142ac55a5efecfa71b0149d57566f86d969905005b0ab98def"
        "?s=64&d=retro")
    expected_packages = set(['guake'])
    expected_usernames = set(['pkgdb_updater'])
    expected_objects = set(['guake/update'])
    msg = {
        "username": "apache",
        "i": 144,
        "timestamp": 1379605523.496933,
        "msg_id": "2013-c131fb95-0a2e-4426-95c3-09766e017d29",
        "topic": "org.fedoraproject.dev.pkgdb.package.update",
        "msg": {
            "package": {
                    "status": "Approved",
                    "upstream_url": "http://guake.org",
                    "name": "guake",
                    "creation_date": 1379619917.0,
                    "summary": "Top down terminal for GNOME",
                    "review_url": "https://bugzilla.redhat.com/450189"
                },
            "agent": "pkgdb_updater",
            "fields": ["summary", "description"],
        }
    }


class LegacyTestPkgdbBranchClone(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    publishes messages on this topic when a new branch is cloned for a
    package.
    """
    expected_title = "pkgdb.branch.clone"
    expected_subti = "ralph branched rpms/php-zmq f18 from devel"
    expected_link = "https://admin.fedoraproject.org/pkgdb/package/rpms/php-zmq/"
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
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


class TestLegacyPkgdbCritpathUpdate(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    publishes messages on this topic when the critical path status of a
    package changes (when it is either added, or removed from the critical
    path).  For example:
    """
    expected_title = "pkgdb.critpath.update"
    expected_subti = "ralph altered the critpath status for some packages"
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
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


class TestPkgdbPackageUpdateStatus2(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    publishes this message when the status of a package is updated.
    Here's an example of a package being retired:
    """
    expected_title = "pkgdb.package.update.status"
    expected_subti = "till retired rpms/libvmime07 in master"
    expected_link = "https://admin.fedoraproject.org/pkgdb/package/rpms/libvmime07/"
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "272bbf32f26ca494a78673f873bb62e8f3deb9f9b53213ceac3c2a144de4784a"
        "?s=64&d=retro")
    expected_packages = set(['libvmime07'])
    expected_usernames = set(['till'])
    expected_objects = set(['libvmime07/update'])
    msg = {
        "source_name": "datanommer",
        "i": 7,
        "timestamp": 1412710605.0,
        "msg_id": "2014-78aa26ee-d2e5-4446-b4a4-73948704d73e",
        "topic": "org.fedoraproject.prod.pkgdb.package.update.status",
        "source_version": "0.6.4",
        "msg": {
            "status": "Retired",
            "package_listing": {
                "status": "Retired",
                "point_of_contact": "orphan",
                "package": {
                    "status": "Approved",
                    "upstream_url": "http://www.zarafa.com/wiki/index.php/Libvmime_patches",
                    "description": "VMime is a powerful C++ class ...",
                    "creation_date": 1400070978.0,
                    "acls": [],
                    "summary": "A powerful C++ class ...",
                    "review_url": None,
                    "name": "libvmime07"
                },
                "collection": {
                    "status": "Under Development",
                    "dist_tag": ".fc22",
                    "koji_name": "rawhide",
                    "name": "Fedora",
                    "version": "devel",
                    "branchname": "master"
                },
                "acls": [
                    {
                        "fas_name": "robert",
                        "status": "Approved",
                        "acl": "watchcommits"
                    },
                    {
                        "fas_name": "robert",
                        "status": "Approved",
                        "acl": "watchbugzilla"
                    },
                    {
                        "fas_name": "robert",
                        "status": "Obsolete",
                        "acl": "commit"
                    },
                    {
                        "fas_name": "robert",
                        "status": "Obsolete",
                        "acl": "approveacls"
                    }
                ],
                "critpath": False,
                "status_change": 1412710603.0
            },
            "prev_status": "Orphaned",
            "package_name": "libvmime07",
            "agent": "till"
        }
    }


class TestLegacyPkgdbPackageRetire(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    publishes messages on this topic when a package is retired.  For example:
    """
    expected_title = "pkgdb.package.retire"
    expected_subti = "ralph retired rpms/php-zmq (EL-6)!"
    expected_link = "https://admin.fedoraproject.org/pkgdb/package/rpms/php-zmq/"
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
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


class LegacyTestPkgdbUserRemove(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    when a user is removed from a package ACL.
    """
    expected_title = "pkgdb.acl.user.remove"
    expected_subti = "ralph removed ralph from rpms/php-zmq (EL-6, F18)"
    expected_link = "https://admin.fedoraproject.org/pkgdb/package/rpms/php-zmq/"
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
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
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
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


class TestLegacyPkgdbBranchStart(Base):
    """ This just tests a funny case where 'agent' is a list.. """
    expected_title = "pkgdb.branch.start"
    expected_subti = "ralph started a branch of F-19 from devel"
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
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
            u'agent': [u'ralph'],
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
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
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
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
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
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
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


class TestPkgdbDeletePackage(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    publishes messages like these when an admin **deletes a package** all
    together.
    """
    expected_title = "pkgdb.package.delete"
    expected_subti = ("ausil deleted the 'rpms/pipelight' package from the pkgdb")
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "a89b57d99dcf12d40ec2b9fb05910b90293b13b0b87415208bedc897bc18a354"
        "?s=64&d=retro")
    expected_packages = set(['pipelight'])
    expected_usernames = set(['ausil'])
    expected_objects = set(['pipelight/package/delete'])
    msg = {
        "i": 46,
        "msg_id": "2014-9372bf63-8e32-4257-82ec-38fb5226763a",
        "source_name": "datanommer",
        "source_version": "0.6.4",
        "timestamp": 1408377920.0,
        "topic": "org.fedoraproject.prod.pkgdb.package.delete",
        "msg": {
            "agent": "ausil",
            "package": {
                "acls": [
                    {
                        "acls": [
                            {
                                "acl": "commit",
                                "fas_name": "besser82",
                                "status": "Approved"
                            },
                            {
                                "acl": "watchbugzilla",
                                "fas_name": "besser82",
                                "status": "Approved"
                            },
                            {
                                "acl": "watchcommits",
                                "fas_name": "besser82",
                                "status": "Approved"
                            },
                            {
                                "acl": "approveacls",
                                "fas_name": "besser82",
                                "status": "Approved"
                            },
                            {
                                "acl": "watchcommits",
                                "fas_name": "awjb",
                                "status": "Approved"
                            },
                            {
                                "acl": "watchbugzilla",
                                "fas_name": "awjb",
                                "status": "Approved"
                            },
                            {
                                "acl": "approveacls",
                                "fas_name": "awjb",
                                "status": "Approved"
                            },
                            {
                                "acl": "commit",
                                "fas_name": "awjb",
                                "status": "Approved"
                            }
                        ],
                        "collection": {
                            "branchname": "master",
                            "dist_tag": ".fc22",
                            "koji_name": "rawhide",
                            "name": "Fedora",
                            "status": "Under Development",
                            "version": "devel"
                        },
                        "critpath": False,
                        "package": {
                            "acls": [],
                            "creation_date": 1404850009.0,
                            "description": "",
                            "name": "pipelight",
                            "review_url": "https://bugzilla.redhat.com/"
                            "1117403",
                            "status": "Approved",
                            "summary": "NPAPI Wrapper Plugin for using "
                            "Windows plugins in Linux browsers",
                            "upstream_url": "http://pipelight.net/"
                        },
                        "point_of_contact": "besser82",
                        "status": "Approved",
                        "status_change": 1404850010.0
                    },
                    {
                        "acls": [
                            {
                                "acl": "commit",
                                "fas_name": "besser82",
                                "status": "Approved"
                            },
                            {
                                "acl": "watchbugzilla",
                                "fas_name": "besser82",
                                "status": "Approved"
                            },
                            {
                                "acl": "watchcommits",
                                "fas_name": "besser82",
                                "status": "Approved"
                            },
                            {
                                "acl": "approveacls",
                                "fas_name": "besser82",
                                "status": "Approved"
                            },
                            {
                                "acl": "watchcommits",
                                "fas_name": "awjb",
                                "status": "Approved"
                            },
                            {
                                "acl": "watchbugzilla",
                                "fas_name": "awjb",
                                "status": "Approved"
                            },
                            {
                                "acl": "approveacls",
                                "fas_name": "awjb",
                                "status": "Approved"
                            },
                            {
                                "acl": "commit",
                                "fas_name": "awjb",
                                "status": "Approved"
                            }
                        ],
                        "collection": {
                            "branchname": "f19",
                            "dist_tag": ".fc19",
                            "koji_name": "f19",
                            "name": "Fedora",
                            "status": "Active",
                            "version": "19"
                        },
                        "critpath": False,
                        "package": {
                            "acls": [],
                            "creation_date": 1404850009.0,
                            "description": "",
                            "name": "pipelight",
                            "review_url": "https://bugzilla.redhat.com/"
                            "1117403",
                            "status": "Approved",
                            "summary": "NPAPI Wrapper Plugin for using "
                            "Windows plugins in Linux browsers",
                            "upstream_url": "http://pipelight.net/"
                        },
                        "point_of_contact": "besser82",
                        "status": "Approved",
                        "status_change": 1404850009.0
                    },
                    {
                        "acls": [
                            {
                                "acl": "commit",
                                "fas_name": "besser82",
                                "status": "Approved"
                            },
                            {
                                "acl": "watchbugzilla",
                                "fas_name": "besser82",
                                "status": "Approved"
                            },
                            {
                                "acl": "watchcommits",
                                "fas_name": "besser82",
                                "status": "Approved"
                            },
                            {
                                "acl": "approveacls",
                                "fas_name": "besser82",
                                "status": "Approved"
                            },
                            {
                                "acl": "watchcommits",
                                "fas_name": "awjb",
                                "status": "Approved"
                            },
                            {
                                "acl": "watchbugzilla",
                                "fas_name": "awjb",
                                "status": "Approved"
                            },
                            {
                                "acl": "approveacls",
                                "fas_name": "awjb",
                                "status": "Approved"
                            },
                            {
                                "acl": "commit",
                                "fas_name": "awjb",
                                "status": "Approved"
                            }
                        ],
                        "collection": {
                            "branchname": "f20",
                            "dist_tag": ".fc20",
                            "koji_name": "f20",
                            "name": "Fedora",
                            "status": "Active",
                            "version": "20"
                        },
                        "critpath": False,
                        "package": {
                            "acls": [],
                            "creation_date": 1404850009.0,
                            "description": "",
                            "name": "pipelight",
                            "review_url": "https://bugzilla.redhat.com/"
                            "1117403",
                            "status": "Approved",
                            "summary": "NPAPI Wrapper Plugin for using "
                            "Windows plugins in Linux browsers",
                            "upstream_url": "http://pipelight.net/"
                        },
                        "point_of_contact": "besser82",
                        "status": "Approved",
                        "status_change": 1404850010.0
                    },
                    {
                        "acls": [
                            {
                                "acl": "commit",
                                "fas_name": "besser82",
                                "status": "Approved"
                            },
                            {
                                "acl": "watchbugzilla",
                                "fas_name": "besser82",
                                "status": "Approved"
                            },
                            {
                                "acl": "watchcommits",
                                "fas_name": "besser82",
                                "status": "Approved"
                            },
                            {
                                "acl": "approveacls",
                                "fas_name": "besser82",
                                "status": "Approved"
                            },
                            {
                                "acl": "watchcommits",
                                "fas_name": "awjb",
                                "status": "Approved"
                            },
                            {
                                "acl": "watchbugzilla",
                                "fas_name": "awjb",
                                "status": "Approved"
                            },
                            {
                                "acl": "approveacls",
                                "fas_name": "awjb",
                                "status": "Approved"
                            },
                            {
                                "acl": "commit",
                                "fas_name": "awjb",
                                "status": "Approved"
                            }
                        ],
                        "collection": {
                            "branchname": "epel7",
                            "dist_tag": ".el7",
                            "koji_name": "epel7",
                            "name": "Fedora EPEL",
                            "status": "Under Development",
                            "version": "7"
                        },
                        "critpath": False,
                        "package": {
                            "acls": [],
                            "creation_date": 1404850009.0,
                            "description": "",
                            "name": "pipelight",
                            "review_url": "https://bugzilla.redhat.com/"
                            "1117403",
                            "status": "Approved",
                            "summary": "NPAPI Wrapper Plugin for using "
                            "Windows plugins in Linux browsers",
                            "upstream_url": "http://pipelight.net/"
                        },
                        "point_of_contact": "besser82",
                        "status": "Approved",
                        "status_change": 1404850009.0
                    },
                    {
                        "acls": [
                            {
                                "acl": "watchcommits",
                                "fas_name": "besser82",
                                "status": "Approved"
                            },
                            {
                                "acl": "watchbugzilla",
                                "fas_name": "besser82",
                                "status": "Approved"
                            },
                            {
                                "acl": "approveacls",
                                "fas_name": "besser82",
                                "status": "Approved"
                            },
                            {
                                "acl": "commit",
                                "fas_name": "besser82",
                                "status": "Approved"
                            },
                            {
                                "acl": "watchcommits",
                                "fas_name": "awjb",
                                "status": "Approved"
                            },
                            {
                                "acl": "watchbugzilla",
                                "fas_name": "awjb",
                                "status": "Approved"
                            },
                            {
                                "acl": "approveacls",
                                "fas_name": "awjb",
                                "status": "Approved"
                            },
                            {
                                "acl": "commit",
                                "fas_name": "awjb",
                                "status": "Approved"
                            }
                        ],
                        "collection": {
                            "branchname": "f21",
                            "dist_tag": ".fc21",
                            "koji_name": "f21",
                            "name": "Fedora",
                            "status": "Under Development",
                            "version": "21"
                        },
                        "critpath": False,
                        "package": {
                            "acls": [],
                            "creation_date": 1404850009.0,
                            "description": "",
                            "name": "pipelight",
                            "review_url": "https://bugzilla.redhat.com/"
                            "1117403",
                            "status": "Approved",
                            "summary": "NPAPI Wrapper Plugin for using "
                            "Windows plugins in Linux browsers",
                            "upstream_url": "http://pipelight.net/"
                        },
                        "point_of_contact": "besser82",
                        "status": "Approved",
                        "status_change": 1404997736.0
                    }
                ],
                "creation_date": 1404850009.0,
                "description": "",
                "name": "pipelight",
                "review_url": "https://bugzilla.redhat.com/1117403",
                "status": "Approved",
                "summary": "NPAPI Wrapper Plugin for using "
                "Windows plugins in Linux browsers",
                "upstream_url": "http://pipelight.net/"
            }
        },
    }


class TestPkgdbDeleteBranch(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    publishes messages like these when an admin **deletes a branch** of a
    particular package.
    """
    expected_title = "pkgdb.package.branch.delete"
    expected_subti = "ausil deleted the f21 branch of the 'rpms/pipelight' package"
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "a89b57d99dcf12d40ec2b9fb05910b90293b13b0b87415208bedc897bc18a354"
        "?s=64&d=retro")
    expected_packages = set(['pipelight'])
    expected_usernames = set(['ausil'])
    expected_objects = set(['pipelight/f21/delete'])
    msg = {
        "i": 45,
        "msg_id": "2014-fba4c0ac-f5ba-446f-bf70-94200e2d286f",
        "source_name": "datanommer",
        "source_version": "0.6.4",
        "timestamp": 1408377920.0,
        "topic": "org.fedoraproject.prod.pkgdb.package.branch.delete",
        "msg": {
            "agent": "ausil",
            "package_listing": {
                "acls": [
                    {
                        "acl": "watchcommits",
                        "fas_name": "besser82",
                        "status": "Approved"
                    },
                    {
                        "acl": "watchbugzilla",
                        "fas_name": "besser82",
                        "status": "Approved"
                    },
                    {
                        "acl": "approveacls",
                        "fas_name": "besser82",
                        "status": "Approved"
                    },
                    {
                        "acl": "commit",
                        "fas_name": "besser82",
                        "status": "Approved"
                    },
                    {
                        "acl": "watchcommits",
                        "fas_name": "awjb",
                        "status": "Approved"
                    },
                    {
                        "acl": "watchbugzilla",
                        "fas_name": "awjb",
                        "status": "Approved"
                    },
                    {
                        "acl": "approveacls",
                        "fas_name": "awjb",
                        "status": "Approved"
                    },
                    {
                        "acl": "commit",
                        "fas_name": "awjb",
                        "status": "Approved"
                    }
                ],
                "collection": {
                    "branchname": "f21",
                    "dist_tag": ".fc21",
                    "koji_name": "f21",
                    "name": "Fedora",
                    "status": "Under Development",
                    "version": "21"
                },
                "critpath": False,
                "package": {
                    "acls": [],
                    "creation_date": 1404850009.0,
                    "description": "",
                    "name": "pipelight",
                    "review_url": "https://bugzilla.redhat.com/1117403",
                    "status": "Approved",
                    "summary": "NPAPI Wrapper Plugin for using Windows "
                    "plugins in Linux browsers",
                    "upstream_url": "http://pipelight.net/"
                },
                "point_of_contact": "besser82",
                "status": "Approved",
                "status_change": 1404997736.0
            }
        },
    }


class TestPkgdbDeleteAcl(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    publishes messages like these when an admin **deletes a branch** of a
    particular package.
    """
    expected_title = "pkgdb.acl.delete"
    expected_subti = ("ausil deleted awjb's watchcommits "
                      "rights from rpms/pipelight (f20)")
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "a89b57d99dcf12d40ec2b9fb05910b90293b13b0b87415208bedc897bc18a354"
        "?s=64&d=retro")
    expected_packages = set(['pipelight'])
    expected_usernames = set(['ausil', 'awjb'])
    expected_objects = set(['pipelight/acls/f20/watchcommits/awjb'])
    msg = {
        "i": 23,
        "msg_id": "2014-f46f0993-ea29-4fe1-af44-807b863a12de",
        "source_name": "datanommer",
        "source_version": "0.6.4",
        "timestamp": 1408377918.0,
        "topic": "org.fedoraproject.prod.pkgdb.acl.delete",
        "msg": {
            "acl": {
                "acl": "watchcommits",
                "fas_name": "awjb",
                "packagelist": {
                    "collection": {
                        "branchname": "f20",
                        "dist_tag": ".fc20",
                        "koji_name": "f20",
                        "name": "Fedora",
                        "status": "Active",
                        "version": "20"
                    },
                    "critpath": False,
                    "package": {
                        "acls": [],
                        "creation_date": 1404850009.0,
                        "description": "",
                        "name": "pipelight",
                        "review_url": "https://bugzilla.redhat.com/1117403",
                        "status": "Approved",
                        "summary": "NPAPI Wrapper Plugin for using Windows "
                        "plugins in Linux browsers",
                        "upstream_url": "http://pipelight.net/"
                    },
                    "point_of_contact": "besser82",
                    "status": "Approved",
                    "status_change": 1404850010.0
                },
                "status": "Approved"
            },
            "agent": "ausil"
        },
    }


class TestPkgdbBranchRequest(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    publishes messages like these when an user **requests a new branch** for
    a particular package.
    """
    expected_title = "pkgdb.package.branch.request"
    expected_subti = ("pingou requested branch epel7 for package rpms/R-BiocGenerics")
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c"
        "?s=64&d=retro")
    expected_packages = set(['R-BiocGenerics'])
    expected_usernames = set(['pingou'])
    expected_objects = set(['R-BiocGenerics/branch/request/epel7/pingou'])
    msg = {
        "i": 1,
        "timestamp": 1408440084,
        "msg_id": "2014-250329a1-1ccf-4fc4-ad0c-e24365f89c0f",
        "topic": "org.fedoraproject.dev.pkgdb.package.branch.request",
        "msg": {
            "collection_to": {
              "status": "Under Development",
                "dist_tag": ".el7",
                "koji_name": "epel7",
                "name": "Fedora EPEL",
                "version": "7",
                "branchname": "epel7"
            },
            "package": {
                "status": "Approved",
                "upstream_url": None,
                "description": None,
                "summary": "Generic functions for Bioconductor",
                "acls": [],
                "creation_date": 1400063778.0,
                "review_url": None,
                "name": "R-BiocGenerics"
            },
            "agent": "pingou",
        },
    }


class TestPkgdbPackageRequest(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    publishes messages like these when an user **requests a new package**
    to be added into Package DB.
    """
    expected_title = "pkgdb.package.new.request"
    expected_subti = ("pingou requested package rpms/guake on branch master")
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_link = "https://admin.fedoraproject.org/pkgdb/package/rpms/guake/"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c"
        "?s=64&d=retro")
    expected_packages = set(['guake'])
    expected_usernames = set(['pingou'])
    expected_objects = set(['new/package/request/guake/master/pingou'])
    msg = {
        "i": 3,
        "timestamp": 1408440927,
        "msg_id": "2014-40c33929-8fa1-4cfb-9559-231af6d809aa",
        "topic": "org.fedoraproject.dev.pkgdb.package.new.request",
        "msg": {
            "info": {
                "pkg_summary": "A drop-down terminal for GNOME",
                "pkg_collection": "master",
                "pkg_review_url": "https://bugzilla.redhat.com/123",
                "pkg_upstream_url": "http://guake.org",
                "pkg_poc": "pingou",
                "pkg_status": "Approved",
                "pkg_name": "guake",
                "pkg_description": "",
                "pkg_critpath": False
            },
            "agent": "pingou",
            "collection": {
                "status": "Under Development",
                "dist_tag": ".fc22",
                "koji_name": "rawhide",
                "name": "Fedora",
                "version": "devel",
                "branchname": "master"
            },
            "package": None
        },
    }


class TestPkgdbAdminActionUpdate(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    publishes messages like these when an admin **update the status of an
    Admin Action**.
    """
    expected_title = "pkgdb.admin.action.status.update"
    expected_subti = ("pingou changed pingou's package request for rpms/guake "
                      "in master from Awaiting Review to Approved")
    expected_link = "https://admin.fedoraproject.org/pkgdb/package/rpms/guake/"
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c"
        "?s=64&d=retro")
    expected_packages = set(['guake'])
    expected_usernames = set(['pingou'])
    expected_objects = set(['action/18/status/guake/master/pingou'])
    msg = {
        "i": 6,
        "timestamp": 1408441710,
        "msg_id": "2014-3a9cba3d-a1d0-4187-9fa0-995d54bf826d",
        "topic": "org.fedoraproject.dev.pkgdb.admin.action.status.update",
        "msg": {
            "action": {
                "info": {
                    'pkg_summary': u'A drop-down terminal for GNOME',
                    'pkg_status': u'Approved',
                    'pkg_collection': u'master',
                    'pkg_name': u'guake',
                    'pkg_review_url': u'https://bugzilla.redhat.com/123',
                    'pkg_description': u'',
                    'pkg_upstream_url': u'http://guake.org',
                    'pkg_poc': u'pingou',
                    'pkg_critpath': False
                },
                "status": "Approved",
                "package": None,
                "date_updated": 1408441710.0,
                "collection": {
                    "status": "Under Development",
                    "dist_tag": ".fc22",
                    "koji_name": "rawhide",
                    "name": "Fedora",
                    "version": "devel",
                    "branchname": "master"
                },
                "user": "pingou",
                "action": "request.package",
                "date_created": 1408433727.0,
                "from_collection": None,
                "id": 18
            },
            "old_status": "Awaiting Review",
            "new_status": "Approved",
            "agent": "pingou"
        },
    }

class TestPkgdbAdminActionUpdate_Denied(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    publishes messages like these when a request for a new branch/package is
    **denied/blocked**.
    """
    expected_title = "pkgdb.admin.action.status.update"
    expected_subti = ("pingou changed pingou's branch request for rpms/R-Biobase "
                      "in epel7 from Awaiting Review to Denied "
                      "with message: "
                      "This package should not be branched for EPEL7")
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c"
        "?s=64&d=retro")
    expected_packages = set(['R-Biobase'])
    expected_usernames = set(['pingou'])
    expected_objects = set(['action/2/status/R-Biobase/epel7/pingou'])
    msg = {
        "i": 1,
        "timestamp": 1421830060,
        "msg_id": "2015-1acdeda2-e571-4071-a893-cc2b7ba46b02",
        "topic": "org.fedoraproject.dev.pkgdb.admin.action.status.update",
        "msg": {
          "action": {
            "info": {},
            "status": "Denied",
            "package": {
              "status": "Approved",
              "upstream_url": "http://bioconductor.org/packages/release/bioc/html/Biobase.html",
              "monitor": False,
              "description": "Base functions for Bioconductor (bioconductor.org). Biobase provides\nfunctions that are needed by many other Bioconductor packages or which\nreplace R functions.",
              "summary": "Base functions for Bioconductor",
              "acls": [],
              "creation_date": 1400063778.0,
              "review_url": None,
              "name": "R-Biobase"
            },
            "date_updated": 1421830060.0,
            "collection": {
              "status": "Under Development",
              "dist_tag": ".el7",
              "koji_name": "epel7",
              "name": "Fedora EPEL",
              "version": "7",
              "branchname": "epel7"
            },
            "user": "pingou",
            "action": "request.branch",
            "date_created": 1421227282.0,
            "message": "This package should not be branched for EPEL7",
            "id": 2
          },
          "old_status": "Awaiting Review",
          "new_status": "Denied",
          "agent": "pingou"
        }
      }


class TestPkgdbCritpathUpdate(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    publishes messages like these when an admin **updates the critpath flag on
    a package**.
    """
    expected_title = "pkgdb.package.critpath.update"
    expected_subti = ("pingou set the critpath flag on the "
                      "rpms/openbox package (f21)")
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c"
        "?s=64&d=retro")
    expected_packages = set(['openbox'])
    expected_usernames = set(['pingou'])
    expected_objects = set(['openbox/critpath'])
    msg = {
        "msg_id": "2014-dbb1c4d3-2ffa-4212-9daa-1479bf11e8a4",
        "source_name": "datanommer",
        "source_version": "0.6.4",
        "timestamp": 1408557412.0,
        "topic": "org.fedoraproject.prod.pkgdb.package.critpath.update",
        "i": 35,
        "msg": {
            "agent": "pingou",
            "branches": [
                "f21"
            ],
            "critpath": True,
            "package": {
                "acls": [
                    {
                        "acls": [
                            {
                                "acl": "watchcommits",
                                "fas_name": "mlichvar",
                                "status": "Approved"
                            },
                            {
                                "acl": "watchbugzilla",
                                "fas_name": "mlichvar",
                                "status": "Approved"
                            },
                            {
                                "acl": "commit",
                                "fas_name": "mlichvar",
                                "status": "Approved"
                            },
                            {
                                "acl": "approveacls",
                                "fas_name": "mlichvar",
                                "status": "Approved"
                            }
                        ],
                        "collection": {
                            "branchname": "FC-5",
                            "dist_tag": ".fc5",
                            "koji_name": None,
                            "name": "Fedora",
                            "status": "EOL",
                            "version": "5"
                        },
                        "critpath": False,
                        "package": {
                            "acls": [],
                            "creation_date": 1400070978.0,
                            "name": "openbox",
                            "review_url": None,
                            "status": "Approved",
                            "summary": "A highly configurable and "
                            "standards-compliant X11 window manager",
                            "upstream_url": None
                        },
                        "point_of_contact": "mlichvar",
                        "status": "Approved",
                        "status_change": 1400071632.0
                    },
                    {
                        "acls": [
                            {
                                "acl": "watchcommits",
                                "fas_name": "mlichvar",
                                "status": "Approved"
                            },
                            {
                                "acl": "watchbugzilla",
                                "fas_name": "mlichvar",
                                "status": "Approved"
                            },
                            {
                                "acl": "commit",
                                "fas_name": "mlichvar",
                                "status": "Approved"
                            },
                            {
                                "acl": "approveacls",
                                "fas_name": "mlichvar",
                                "status": "Approved"
                            }
                        ],
                        "collection": {
                            "branchname": "FC-4",
                            "dist_tag": ".fc4",
                            "koji_name": None,
                            "name": "Fedora",
                            "status": "EOL",
                            "version": "4"
                        },
                        "critpath": False,
                        "package": {
                            "acls": [],
                            "creation_date": 1400070978.0,
                            "name": "openbox",
                            "review_url": None,
                            "status": "Approved",
                            "summary": "A highly configurable and "
                            "standards-compliant X11 window manager",
                            "upstream_url": None
                        },
                        "point_of_contact": "mlichvar",
                        "status": "Approved",
                        "status_change": 1400071632.0
                    },
                    {
                        "acls": [
                            {
                                "acl": "watchcommits",
                                "fas_name": "mlichvar",
                                "status": "Approved"
                            },
                            {
                                "acl": "watchbugzilla",
                                "fas_name": "mlichvar",
                                "status": "Approved"
                            },
                            {
                                "acl": "commit",
                                "fas_name": "mlichvar",
                                "status": "Approved"
                            },
                            {
                                "acl": "approveacls",
                                "fas_name": "mlichvar",
                                "status": "Approved"
                            },
                            {
                                "acl": "watchbugzilla",
                                "fas_name": "cwickert",
                                "status": "Approved"
                            },
                            {
                                "acl": "watchcommits",
                                "fas_name": "cwickert",
                                "status": "Approved"
                            },
                            {
                                "acl": "commit",
                                "fas_name": "cwickert",
                                "status": "Approved"
                            },
                            {
                                "acl": "watchcommits",
                                "fas_name": "athmane",
                                "status": "Obsolete"
                            },
                            {
                                "acl": "watchbugzilla",
                                "fas_name": "athmane",
                                "status": "Obsolete"
                            }
                        ],
                        "collection": {
                            "branchname": "f21",
                            "dist_tag": ".fc21",
                            "koji_name": "f21",
                            "name": "Fedora",
                            "status": "Under Development",
                            "version": "21"
                        },
                        "critpath": True,
                        "package": {
                            "acls": [],
                            "creation_date": 1400070978.0,
                            "name": "openbox",
                            "review_url": None,
                            "status": "Approved",
                            "summary": "A highly configurable and "
                            "standards-compliant X11 window manager",
                            "upstream_url": None
                        },
                        "point_of_contact": "mlichvar",
                        "status": "Approved",
                        "status_change": 1408557402.0
                    }
                ],
                "creation_date": 1400070978.0,
                "description": "Openbox is a window manager designed ...",
                "name": "openbox",
                "review_url": None,
                "status": "Approved",
                "summary": "A highly configurable and "
                "standards-compliant X11 window manager",
                "upstream_url": None
            }
        },
    }

    def setUp(self):
        super(TestPkgdbCritpathUpdate, self).setUp()
        self.config['namespace'] = 'docker'


class TestPkgdbPackageBranchNewCustomNamespace(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    publishes messages like these when a **new branch** is created for a
    package.
    """
    expected_title = "pkgdb.package.branch.new"
    expected_subti = ("pingou created the branch 'epel7' for the package "
                "'docker/R-BSgenome'")
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c"
        "?s=64&d=retro")
    expected_packages = set(['R-BSgenome'])
    expected_usernames = set(['pingou'])
    expected_objects = set(['R-BSgenome/epel7/new'])
    msg = {
        "i": 1,
        "timestamp": 1408957258,
        "msg_id": "2014-645038a7-1f95-4a81-aa68-489c0ae55803",
        "topic": "org.fedoraproject.dev.pkgdb.package.branch.new",
        "msg": {
            "package_listing": {
                "status": "Approved",
                "package": {
                    "status": "Approved",
                    "upstream_url": None,
                    "description": None,
                    "summary": "Infrastructure shared by all the "
                    "Biostrings-based genome",
                    "acls": [],
                    "creation_date": 1400063778.0,
                    "review_url": None,
                    "name": "R-BSgenome",
                    "namespace": "docker",
                },
                "point_of_contact": "pingou",
                "collection": {
                    "status": "Under Development",
                    "dist_tag": ".el7",
                    "koji_name": "epel7",
                    "name": "Fedora EPEL",
                    "version": "7",
                    "branchname": "epel7"
                },
                "critpath": False,
                "status_change": 1408950057.0
            },
            "agent": "pingou",
            "package": {
                "status": "Approved",
                "upstream_url": None,
                "description": None,
                "summary": "Infrastructure shared by all the "
                "Biostrings-based genome",
                "acls": [],
                "creation_date": 1400063778.0,
                "review_url": None,
                "name": "R-BSgenome",
                "namespace": "docker",
            }
        }
    }

    def setUp(self):
        super(TestPkgdbPackageBranchNewCustomNamespace, self).setUp()
        self.config['namespace'] = 'docker'


class TestPkgdbPackageBranchNew(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    publishes messages like these when a **new branch** is created for a
    package.
    """
    expected_title = "pkgdb.package.branch.new"
    expected_subti = ("pingou created the branch 'epel7' for the package "
                "'rpms/R-BSgenome'")
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c"
        "?s=64&d=retro")
    expected_packages = set(['R-BSgenome'])
    expected_usernames = set(['pingou'])
    expected_objects = set(['R-BSgenome/epel7/new'])
    msg = {
        "i": 1,
        "timestamp": 1408957258,
        "msg_id": "2014-645038a7-1f95-4a81-aa68-489c0ae55803",
        "topic": "org.fedoraproject.dev.pkgdb.package.branch.new",
        "msg": {
            "package_listing": {
                "status": "Approved",
                "package": {
                    "status": "Approved",
                    "upstream_url": None,
                    "description": None,
                    "summary": "Infrastructure shared by all the "
                    "Biostrings-based genome",
                    "acls": [],
                    "creation_date": 1400063778.0,
                    "review_url": None,
                    "name": "R-BSgenome",
                    "namespace": "rpms",
                },
                "point_of_contact": "pingou",
                "collection": {
                    "status": "Under Development",
                    "dist_tag": ".el7",
                    "koji_name": "epel7",
                    "name": "Fedora EPEL",
                    "version": "7",
                    "branchname": "epel7"
                },
                "critpath": False,
                "status_change": 1408950057.0
            },
            "agent": "pingou",
            "package": {
                "status": "Approved",
                "upstream_url": None,
                "description": None,
                "summary": "Infrastructure shared by all the "
                "Biostrings-based genome",
                "acls": [],
                "creation_date": 1400063778.0,
                "review_url": None,
                "name": "R-BSgenome",
                "namespace": "rpms",
            }
        }
    }


class TestPkgdbPackageMonitorUpdate(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    publishes messages like these when someone changes the
    `monitoring <https://fedoraproject.org/wiki/Upstream_release_monitoring>`_
    status of a package.
    """
    expected_title = "pkgdb.package.monitor.update"
    expected_subti = ("pingou set the monitor flag of rpms/guake to False")
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c"
        "?s=64&d=retro")
    expected_packages = set(['guake'])
    expected_usernames = set(['pingou'])
    expected_objects = set(['guake/monitor/false'])
    msg = {
        "username": "pingou",
        "i": 3,
        "timestamp": 1412957736,
        "msg_id": "2014-905aaa3c-483d-4923-95f7-56a8da38da62",
        "topic": "org.fedoraproject.dev.pkgdb.package.monitor.update",
        "msg": {
            "status": False,
            "agent": "pingou",
            "package": {
                "status": "Approved",
                "upstream_url": "http://www.guake.org/",
                "description": "Guake is a drop-down terminal for Gnome Desktop Environment,\nso you just need to press a key to invoke him,\nand press again to hide.",
                "summary": "Drop-down terminal for GNOME",
                "acls": [],
                "creation_date": 1397204290.0,
                "review_url": None,
                "name": "guake"
            }
        }
    }


class TestPkgdbPackageUnretireRequest(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    publishes messages like these when someone asks that a package is
    **unretired**.
    """
    expected_title = "pkgdb.package.unretire.request"
    expected_subti = ("moceap asks that rpms/netbeans-platform8 be unretired on "
        "master")
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "360e1873c56312ea5866123f5ffaf4e07d419570b03af7f475c0d20c7501db06"
        "?s=64&d=retro")
    expected_packages = set(['netbeans-platform8'])
    expected_usernames = set(['moceap'])
    expected_objects = set(['netbeans-platform8/unretire/master'])
    msg = {
        'i': 1,
        'timestamp': 1427823120,
        'msg_id': '2015-bb28a398-e638-4509-9fa0-57d41c2ae0a4',
        'topic': 'org.fedoraproject.prod.pkgdb.package.unretire.request',
        'msg': {
            'collection': {
                'status': 'UnderDevelopment',
                'dist_tag': '.fc23',
                'koji_name': 'rawhide',
                'name': 'Fedora',
                'version': 'devel',
                'branchname': 'master'
            },
            'agent': 'moceap',
            'package': {
                'status': 'Approved',
                'upstream_url': None,
                'monitor': False,
                'summary': 'NetBeansPlatform8',
                'name': 'netbeans-platform8',
                'acls': [
                    {
                        'status': 'Retired',
                        'point_of_contact': 'orphan',
                        'package': {
                            'status': 'Approved',
                            'upstream_url': None,
                            'monitor': False,
                            'summary': 'NetBeansPlatform8',
                            'name': 'netbeans-platform8',
                            'acls': [],
                            'creation_date': 1400070978.0,
                            'review_url': None,
                            'description': 'NetBeansPlatformisaframeworkfordevelopmentof\nRichClientSwingApplications.Itcontainspowerful\nmodulesystemandasetofmodulesprovidingvarious\nfunctionalitiesneededforsimplificationof\ndevelopmentofmodulardesktopapplications.'
                        },
                        'collection': {
                            'status': 'UnderDevelopment',
                            'dist_tag': '.fc23',
                            'koji_name': 'rawhide',
                            'name': 'Fedora',
                            'version': 'devel',
                            'branchname': 'master'
                        },
                        'critpath': False,
                        'status_change': 1400071169.0
                    },
                    {
                        'status': 'Approved',
                        'point_of_contact': 'victorv',
                        'package': {
                            'status': 'Approved',
                            'upstream_url': None,
                            'monitor': False,
                            'summary': 'NetBeansPlatform8',
                            'name': 'netbeans-platform8',
                            'acls': [],
                            'creation_date': 1400070978.0,
                            'review_url': None,
                            'description': 'NetBeansPlatformisaframeworkfordevelopmentof\nRichClientSwingApplications.Itcontainspowerful\nmodulesystemandasetofmodulesprovidingvarious\nfunctionalitiesneededforsimplificationof\ndevelopmentofmodulardesktopapplications.'
                        },
                        'collection': {
                            'status': 'EOL',
                            'dist_tag': '.fc10',
                            'koji_name': 'dist-f10',
                            'name': 'Fedora',
                            'version': '10',
                            'branchname': 'f10'
                        },
                        'acls': [
                            {
                                'fas_name': 'victorv',
                                'status': 'Approved',
                                'acl': 'watchcommits'
                            },
                            {
                                'fas_name': 'victorv',
                                'status': 'Approved',
                                'acl': 'watchbugzilla'
                            },
                            {
                                'fas_name': 'victorv',
                                'status': 'Approved',
                                'acl': 'commit'
                            },
                            {
                                'fas_name': 'victorv',
                                'status': 'Approved',
                                'acl': 'approveacls'
                            }
                        ],
                        'critpath': False,
                        'status_change': 1400071253.0
                    },
                    {
                        'status': 'Approved',
                        'point_of_contact': 'victorv',
                        'package': {
                            'status': 'Approved',
                            'upstream_url': None,
                            'monitor': False,
                            'summary': 'NetBeansPlatform8',
                            'name': 'netbeans-platform8',
                            'acls': [

                            ],
                            'creation_date': 1400070978.0,
                            'review_url': None,
                            'description': 'NetBeansPlatformisaframeworkfordevelopmentof\nRichClientSwingApplications.Itcontainspowerful\nmodulesystemandasetofmodulesprovidingvarious\nfunctionalitiesneededforsimplificationof\ndevelopmentofmodulardesktopapplications.'
                        },
                        'collection': {
                            'status': 'EOL',
                            'dist_tag': '.fc11',
                            'koji_name': 'dist-f11',
                            'name': 'Fedora',
                            'version': '11',
                            'branchname': 'f11'
                        },
                        'acls': [
                            {
                                'fas_name': 'victorv',
                                'status': 'Approved',
                                'acl': 'watchcommits'
                            },
                            {
                                'fas_name': 'victorv',
                                'status': 'Approved',
                                'acl': 'watchbugzilla'
                            },
                            {
                                'fas_name': 'victorv',
                                'status': 'Approved',
                                'acl': 'commit'
                            },
                            {
                                'fas_name': 'victorv',
                                'status': 'Approved',
                                'acl': 'approveacls'
                            }
                        ],
                        'critpath': False,
                        'status_change': 1400071427.0
                    },
                    {
                        'status': 'Orphaned',
                        'point_of_contact': 'orphan',
                        'package': {
                            'status': 'Approved',
                            'upstream_url': None,
                            'monitor': False,
                            'summary': 'NetBeansPlatform8',
                            'name': 'netbeans-platform8',
                            'acls': [

                            ],
                            'creation_date': 1400070978.0,
                            'review_url': None,
                            'description': 'NetBeansPlatformisaframeworkfordevelopmentof\nRichClientSwingApplications.Itcontainspowerful\nmodulesystemandasetofmodulesprovidingvarious\nfunctionalitiesneededforsimplificationof\ndevelopmentofmodulardesktopapplications.'
                        },
                        'collection': {
                            'status': 'EOL',
                            'dist_tag': '.fc12',
                            'koji_name': 'dist-f12',
                            'name': 'Fedora',
                            'version': '12',
                            'branchname': 'f12'
                        },
                        'critpath': False,
                        'status_change': 1400071659.0
                    }
                ],
                'creation_date': 1400070978.0,
                'review_url': None,
                'description': 'NetBeansPlatformisaframeworkfordevelopmentof\nRichClientSwingApplications.Itcontainspowerful\nmodulesystemandasetofmodulesprovidingvarious\nfunctionalitiesneededforsimplificationof\ndevelopmentofmodulardesktopapplications.'
            }
        }
    }


class TestPkgdbPackageKoscheiUpdate(Base):
    """ The Fedora `Package DB <https://admin.fedoraproject.org/pkgdb>`_
    publishes messages like these when someone changes the
    `koschei <https://apps.fedoraproject.org/koschei>`_ status of a package.
    """
    expected_title = "pkgdb.package.koschei.update"
    expected_subti = ("pingou set the koschei monitoring flag of rpms/guake to True")
    expected_icon = ("https://apps.fedoraproject.org/packages/images/icons/"
                     "package_128x128.png")
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c"
        "?s=64&d=retro")
    expected_packages = set(['guake'])
    expected_usernames = set(['pingou'])
    expected_objects = set(['guake/koschei/true'])
    msg = {
        'username': u'pierrey',
        'i': 3,
        'timestamp': 1435313134,
        'msg_id': u'2015-7d0ecbd6-6892-4b34-98ff-b212d1fef74e',
        'topic': u'org.fedoraproject.dev.pkgdb.package.koschei.update',
        'msg': {
            'status': True,
            'agent': u'pingou',
            'package': {
                'status': u'Approved',
                'upstream_url': u'http: //www.guake.org/',
                'koschei_monitor': True,
                'monitor': False,
                'summary': u'Drop-downterminalforGNOME',
                'name': u'guake',
                    'acls': [
                ],
                'creation_date': 1400063778.0,
                'review_url': None,
                'description': 'Guake is a drop-down terminal for Gnome'
            }
        }
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
