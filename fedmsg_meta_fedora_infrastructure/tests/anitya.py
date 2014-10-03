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
#           Pierre-Yves Chibon <pingou@pingoured.fr>
#
""" Tests for anitya messages """

import unittest

from fedmsg_meta_fedora_infrastructure.tests.base import Base

from common import add_doc


class TestNewDistro(Base):
    """ These messages are published when a new Linux distribution is added
    to the database of `anitya <http://release-monitoring.org>`_.
    """
    expected_title = "anitya.distro.add"
    expected_subti = 'olasd@debian.org added the distro named' + \
        ' "CentOS" to anitya'
    expected_link = "http://release-monitoring.org/distros"
    expected_icon = "https://todo.com/image.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "e202b61fca3f40ccc4c790d4ecf6ed42" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set(['distros/CentOS'])
    msg = {
        "username": "apache",
        "i": 3,
        "timestamp": 1412327834,
        "msg_id": "2014-1f52337a-8dbe-48f1-baad-f2c770c60640",
        "crypto": "x509",
        "topic": "org.release-monitoring.prod.anitya.distro.add",
        "msg": {
            "project": None,
            "message": {
                "agent": "olasd@debian.org",
                "distro": "CentOS"
            },
            "distro": {
                "name": "CentOS"
            }
        }
    }


class TestEditDistro(Base):
    """ These messages are published when a Linux distribution's entry is
    edited in the `anitya <http://release-monitoring.org>`_ database.
    """
    expected_title = "anitya.distro.edit"
    expected_subti = 'pingou changed a distro name' + \
        ' from "Debia" to "Debian"'
    expected_link = "http://release-monitoring.org/distros"
    expected_icon = "https://todo.com/image.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['distros/Debia', 'distros/Debian'])
    msg = {
        "username": "apache",
        "i": 5,
        "timestamp": 1412328814,
        "msg_id": "2014-746c39cf-9fb0-4ed1-a817-d57bc901e027",
        "crypto": "x509",
        "topic": "org.release-monitoring.prod.anitya.distro.edit",
        "msg": {
            "project": None,
            "message": {
                "new": "Debian",
                "old": "Debia",
                "agent": "pingou@fedoraproject.org"
            },
            "distro": {
                "name": "Debia"
            }
        }
    }


class TestAddProject(Base):
    """ These messages are published when someone adds a new project to
    `anitya's <http://release-monitoring.org>`_ database.
    """
    expected_title = "anitya.project.add"
    expected_subti = 'ralph added the project "arrow" to anitya'
    expected_link = "http://release-monitoring.org/project/5314/"
    expected_icon = "https://todo.com/image.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['projects/arrow'])
    msg = {
        "username": "apache",
        "i": 8,
        "timestamp": 1412328939,
        "msg_id": "2014-c95e6b4c-d033-43d9-9eb1-e1f92ac87c75",
        "crypto": "x509",
        "topic": "org.release-monitoring.prod.anitya.project.add",
        "msg": {
            "project": {
            "regex": "",
            "name": "arrow",
            "created_on": 1412328939.0,
            "version": None,
            "version_url": "",
            "updated_on": 1412328939.0,
            "homepage": "https://pypi.python.org/pypi/arrow",
            "id": 5314,
            "backend": "pypi"
            },
            "message": {
                "project": "arrow",
                "agent": "ralph@fedoraproject.org"
            },
            "distro": None
        }
    }


class TestAddProjectTried(Base):
    """ These messages are published when someone *tries* to add a new project
    to `anitya's <http://release-monitoring.org>`_ database.
    """
    expected_title = "anitya.project.add.tried"
    expected_subti = 'ralph tried to add the project "ansi2html" to anitya'
    expected_link = "http://release-monitoring.org/project/4/"
    expected_icon = "https://todo.com/image.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['projects/ansi2html'])
    msg = {
        "username": "apache",
        "i": 4,
        "timestamp": 1386821688,
        "msg_id": "2013-154429ec-842e-4d7f-acae-8d7434b4cbff",
        "topic": "org.release-monitoring.prod.anitya.project.add.tried",
        "msg": {
            "project": {
                "id": 4,
                "regex": "DEFAULT:ansi2html",
                "logs": None,
                "created_on": 1386839688.0,
                "version": None,
                "version_url": "PYPI-DEFAULT:ansi2html",
                "updated_on": 1386839688.0,
                "packages": [],
                "homepage": "https://github.com/ralphbean/ansi2html",
                "name": "ansi2html"
            },
            "message": {
                "project": "ansi2html",
                "agent": "rbean@redhat.com"
            },
            "distro": None,
        }
    }


class TestEditProject(Base):
    """ These messages are published when someone edits the details of a
    project in `anitya's <http://release-monitoring.org>`_ database.
    """
    expected_title = "anitya.project.edit"
    expected_subti = 'ralph edited the following ' + \
        'fields of the "arrow" project: homepage'
    expected_link = "http://release-monitoring.org/project/5314/"
    expected_icon = "https://todo.com/image.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['projects/arrow'])
    msg = {
        "username": "apache",
        "i": 6,
        "timestamp": 1412329027,
        "msg_id": "2014-f25b6634-d7b9-4f2d-9f93-23ef73034024",
        "crypto": "x509",
        "topic": "org.release-monitoring.prod.anitya.project.edit",
        "msg": {
            "project": {
                "regex": "",
                "name": "arrow",
                "created_on": 1412328939.0,
                "version": None,
                "version_url": "",
                "updated_on": 1412328939.0,
                "homepage": "http://crsmithdev.com/arrow",
                "id": 5314,
                "backend": "pypi"
            },
            "message": {
                "project": "arrow",
                "fields": [
                    "homepage"
                ],
                "agent": "ralph@fedoraproject.org"
            },
            "distro": None
        }
    }


class TestRemoveProject(Base):
    """ These messages are published when someone *removes* a project from
    `anitya's <http://release-monitoring.org>`_ database.
    """
    expected_title = "anitya.project.remove"
    expected_subti = 'ralph deleted the "guake" project'
    expected_link = "http://release-monitoring.org/project/5311/"
    expected_icon = "https://todo.com/image.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['projects/guake'])
    msg = {
        "username": "apache",
        "i": 11,
        "timestamp": 1412331340,
        "msg_id": "2014-94864be5-f649-4b3f-8694-32f238ac7174",
        "crypto": "x509",
        "topic": "org.release-monitoring.prod.anitya.project.remove",
        "msg": {
            "project": {
                "regex": "",
                "name": "guake",
                "created_on": 1412237149.0,
                "version": "0.5.0",
                "version_url": "guake/guake",
                "updated_on": 1412237231.0,
                "homepage": "http://guake.org",
                "id": 5311,
                "backend": "Github"
            },
            "message": {
                "project": "guake",
                "agent": "ralph@fedoraproject.org"
            },
            "distro": None
        }
    }


class TestNewMappingProject(Base):
    """ These messages are published when someone maps an upstream project to a
    package name in a particular distribution (in the `anitya
    <http://release-monitoring.org>`_ database...)
    """
    expected_title = "anitya.project.map.new"
    expected_subti = 'ralph mapped the name of "arrow"' + \
        ' in Fedora to "python-arrow"'
    expected_link = "http://release-monitoring.org/project/5314/"
    expected_icon = "https://todo.com/image.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c" + \
        "?s=64&d=retro"
    expected_packages = set(['python-arrow'])
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'projects/arrow',
        'mappings/Fedora/python-arrow',
        'distros/Fedora',
    ])
    msg = {
        "username": "apache",
        "i": 7,
        "timestamp": 1412329216,
        "msg_id": "2014-9ebf960a-115e-4568-a615-34cc7d8d462e",
        "crypto": "x509",
        "topic": "org.release-monitoring.prod.anitya.project.map.new",
        "msg": {
            "project": {
            "regex": "",
            "name": "arrow",
            "created_on": 1412328939.0,
            "version": None,
            "version_url": "",
            "updated_on": 1412329027.0,
            "homepage": "http://crsmithdev.com/arrow",
            "id": 5314,
            "backend": "pypi"
            },
            "message": {
                "project": "arrow",
                "new": "python-arrow",
                "agent": "ralph@fedoraproject.org",
                "distro": "Fedora"
            },
            "distro": {
                "name": "Fedora"
            }
        }
    }


class TestUpdatedMappingProject(Base):
    """ These messages are published when someone updates the mapping between
    an upstream project and a package name in a particular distribution
    (in the `anitya <http://release-monitoring.org>`_ database...)
    """
    expected_title = "anitya.project.map.update"
    expected_subti = 'ralph updated the name of ' + \
        '"guake" in "Fedora" from "guake2" to "guake"'
    expected_link = "http://release-monitoring.org/project/5311/"
    expected_icon = "https://todo.com/image.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c" + \
        "?s=64&d=retro"
    expected_packages = set([
        'guake',
        'guake2',
    ])
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'projects/guake',
        'mappings/Fedora/guake2',
        'mappings/Fedora/guake',
        'distros/Fedora',
    ])
    msg = {
        "username": "apache",
        "i": 8,
        "timestamp": 1412329667,
        "msg_id": "2014-5bd228ac-4ba1-452f-b6d2-b4df53c9af14",
        "crypto": "x509",
        "topic": "org.release-monitoring.prod.anitya.project.map.update",
        "msg": {
            "project": {
                "regex": "",
                "name": "guake",
                "created_on": 1412237149.0,
                "version": "0.5.0",
                "version_url": "guake/guake",
                "updated_on": 1412237231.0,
                "homepage": "http://guake.org",
                "id": 5311,
                "backend": "Github"
            },
            "message": {
                "edited": [
                    "package_name"
                ],
                "agent": "ralph@fedoraproject.org",
                "project": "guake",
                "new": "guake",
                "prev": "guake2",
                "distro": "Fedora"
            },
            "distro": {
                "name": "Fedora"
            }
        }
    }


class TestNewUpstreamVersion(Base):
    """ The purpose of anitya is to monitor upstream projects and to
    try and detect when they release new tarballs.  *These* messages are the
    ones that get published when a tarball is found that is newer than the
    one last seen in the `anitya <http://release-monitoring.org>`_ database.
    """
    expected_title = "anitya.project.version.update"
    expected_subti = 'A new version of "aspell" has been detected:  ' + \
        '"0.60.6.1" in advance of "0.60.6"'
    expected_link = "http://release-monitoring.org/project/5/"
    expected_icon = "https://todo.com/image.png"
    #expected_secondary_icon = None
    expected_packages = set([
        'aspell',
    ])
    expected_usernames = set([])
    expected_objects = set([
        'projects/aspell',
    ])
    msg = {
        "username": "fedmsg",
        "i": 1,
        "timestamp": 1412234961,
        "msg_id": "2014-f4dfc3e4-8909-45d7-b929-1862efb373cf",
        "crypto": "x509",
        "topic": "org.release-monitoring.prod.anitya.project.version.update",
        "msg": {
            "project": {
                "id": 5,
                "regex": None,
                "name": "aspell",
                "created_on": 1412174948.0,
                "version": "0.60.6.1",
                "version_url": None,
                "updated_on": 1412232860.0,
                "homepage": "http://www.gnu.org/software/aspell/",
                "backend": "GNU project"
            },
            "packages": [
                {
                    "package_name": "aspell",
                    "distro": "Fedora"
                }
            ],
            "old_version": "0.60.6",
            "upstream_version": "0.60.6.1",
            "versions": [
                "0.60.6.1"
            ]
        }
    }


class TestRemoveMappingProject(Base):
    """ These messages are published when someone *removes* a mapping
    between an upstream project and a package name in a particular
    distribution (in the `anitya <http://release-monitoring.org>`_
    database...)
    """
    expected_title = "anitya.project.map.remove"
    expected_subti = 'pingou deleted the mapping of ' + \
        '"guake" project on "Fedora"'
    expected_link = "http://release-monitoring.org/project/5311/"
    expected_icon = "https://todo.com/image.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['projects/guake'])
    msg = {
        "username": "apache",
        "i": 10,
        "timestamp": 1412330764,
        "msg_id": "2014-1d43e5ab-e398-4007-8269-26b4f209d55b",
        "crypto": "x509",
        "topic": "org.release-monitoring.prod.anitya.project.map.remove",
        "msg": {
            "project": {
                "regex": "",
                "name": "guake",
                "created_on": 1412237149.0,
                "version": "0.5.0",
                "version_url": "guake/guake",
                "updated_on": 1412237231.0,
                "homepage": "http://guake.org",
                "id": 5311,
                "backend": "Github"
            },
            "message": {
                "project": "guake",
                "agent": "pingou@fedoraproject.org",
                "distro": "Fedora"
            },
            "distro": None
        }
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
