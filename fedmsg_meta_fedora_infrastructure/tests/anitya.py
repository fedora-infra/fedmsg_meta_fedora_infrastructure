# This file is part of fedmsg.
# Copyright (C) 2012-2016 Red Hat, Inc.
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

from .common import add_doc


class TestNewDistro(Base):
    """ These messages are published when a new Linux distribution is added
    to the database of `anitya <https://release-monitoring.org>`_.
    """
    expected_title = "anitya.distro.add"
    expected_subti = 'foobar added the distro named' + \
        ' "CentOS" to anitya'
    expected_link = "https://release-monitoring.org/distros"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "8d504e09d5ad44ac17e7c872c30d2e4b679a5fdcf0616e825af39466d4b14383" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['foobar'])
    expected_objects = set(['distros/CentOS'])
    msg = {
        'username': 'apache',
        'i': 4,
        'timestamp': 1467814080,
        'msg_id': u'2016-55d13473-2e48-4b6e-9542-3bc1882152ef',
        'topic': u'org.release-monitoring.prod.anitya.distro.add',
        'msg': {
            'project': None,
            'message': {
                'agent': 'foobar',
                'distro': u'CentOS'
            },
            'distro': {
                'name': 'CentOS'
            }
        }
    }


class LegacyTestNewDistro(Base):
    """ These messages are published when a new Linux distribution is added
    to the database of `anitya <https://release-monitoring.org>`_.
    """
    expected_title = "anitya.distro.add"
    expected_subti = 'olasd@debian.org added the distro named' + \
        ' "CentOS" to anitya'
    expected_link = "https://release-monitoring.org/distros"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
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
    edited in the `anitya <https://release-monitoring.org>`_ database.
    """
    expected_title = "anitya.distro.edit"
    expected_subti = 'pingou changed a distro name' + \
        ' from "Debia" to "Debian"'
    expected_link = "https://release-monitoring.org/distros"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
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
                'agent': 'http://pingou.id.fedoraproject.org/',
            },
            "distro": {
                "name": "Debia"
            }
        }
    }


class LegacyTestEditDistro(Base):
    """ These messages are published when a Linux distribution's entry is
    edited in the `anitya <https://release-monitoring.org>`_ database.
    """
    expected_title = "anitya.distro.edit"
    expected_subti = 'pingou changed a distro name' + \
        ' from "Debia" to "Debian"'
    expected_link = "https://release-monitoring.org/distros"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
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
    `anitya's <https://release-monitoring.org>`_ database.
    """
    expected_title = "anitya.project.add"
    expected_subti = 'ralph added the project "arrow" to anitya'
    expected_link = "https://release-monitoring.org/project/5314/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
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
                "regex": None,
                "name": "arrow",
                "created_on": 1412328939.0,
                "version": None,
                "versions": [],
                "version_url": None,
                "updated_on": 1412328939.0,
                "homepage": "https://pypi.python.org/pypi/arrow",
                "id": 5314,
                "backend": "PyPI"
            },
            "message": {
                "project": "arrow",
                'agent': 'http://ralph.id.fedoraproject.org/',
            },
            "distro": None
        }
    }


class LegacyTestAddProject(Base):
    """ These messages are published when someone adds a new project to
    `anitya's <https://release-monitoring.org>`_ database.
    """
    expected_title = "anitya.project.add"
    expected_subti = 'ralph added the project "arrow" to anitya'
    expected_link = "https://release-monitoring.org/project/5314/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
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
    to `anitya's <https://release-monitoring.org>`_ database, but that project
    was already present.
    """
    expected_title = "anitya.project.add.tried"
    expected_subti = 'ralph tried to add the project "ansi2html" to anitya' + \
        ' (but it already exists there)'
    expected_link = "https://release-monitoring.org/project/4/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
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
                "version": [],
                "version_url": "PYPI-DEFAULT:ansi2html",
                "updated_on": 1386839688.0,
                "packages": [],
                "homepage": "https://github.com/ralphbean/ansi2html",
                "name": "ansi2html"
            },
            "message": {
                "project": "ansi2html",
                "agent": 'http://ralph.id.fedoraproject.org/'
            },
            "distro": None,
        }
    }


class LegacyTestAddProjectTried(Base):
    """ These messages are published when someone *tries* to add a new project
    to `anitya's <https://release-monitoring.org>`_ database, but that project
    was already present.
    """
    expected_title = "anitya.project.add.tried"
    expected_subti = 'ralph tried to add the project "ansi2html" to anitya' + \
        ' (but it already exists there)'
    expected_link = "https://release-monitoring.org/project/4/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
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
    project in `anitya's <https://release-monitoring.org>`_ database.
    """
    expected_title = "anitya.project.edit"
    expected_subti = 'ralph edited the following ' + \
        'fields of the "arrow" project: homepage'
    expected_link = "https://release-monitoring.org/project/5314/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
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
                "regex": None,
                "name": "arrow",
                "created_on": 1412328939.0,
                "version": None,
                "versions": [],
                "version_url": None,
                "updated_on": 1412328939.0,
                "homepage": "http://crsmithdev.com/arrow",
                "id": 5314,
                "backend": "PyPI"
            },
            "message": {
                "project": "arrow",
                "fields": [
                    "homepage"
                ],
                "agent": "http://ralph.id.fedoraproject.org/"
            },
            "distro": None
        }
    }


class LegacyTestEditProject(Base):
    """ These messages are published when someone edits the details of a
    project in `anitya's <https://release-monitoring.org>`_ database.
    """
    expected_title = "anitya.project.edit"
    expected_subti = 'ralph edited the following ' + \
        'fields of the "arrow" project: homepage'
    expected_link = "https://release-monitoring.org/project/5314/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
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
    `anitya's <https://release-monitoring.org>`_ database.
    """
    expected_title = "anitya.project.remove"
    expected_subti = 'ralph deleted the "guake" project'
    expected_link = "https://release-monitoring.org/project/5311/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
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
                "regex": None,
                "name": "guake",
                "created_on": 1412237149.0,
                "version": "0.5.0",
                "versions": [],
                "version_url": "guake/guake",
                "updated_on": 1412237231.0,
                "homepage": "http://guake.org",
                "id": 5311,
                "backend": "GitHub"
            },
            "message": {
                "project": "guake",
                "agent": "http://ralph.id.fedoraproject.org/"
            },
            "distro": None
        }
    }


class LegacyTestRemoveProject(Base):
    """ These messages are published when someone *removes* a project from
    `anitya's <https://release-monitoring.org>`_ database.
    """
    expected_title = "anitya.project.remove"
    expected_subti = 'ralph deleted the "guake" project'
    expected_link = "https://release-monitoring.org/project/5311/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
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
    <https://release-monitoring.org>`_ database...)
    """
    expected_title = "anitya.project.map.new"
    expected_subti = 'ralph mapped the name of "arrow"' + \
        ' in Fedora to "python-arrow"'
    expected_link = "https://release-monitoring.org/project/5314/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
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
                "regex": None,
                "name": "arrow",
                "created_on": 1412328939.0,
                "version": None,
                "versions": [],
                "version_url": None,
                "updated_on": 1412329027.0,
                "homepage": "http://crsmithdev.com/arrow",
                "id": 5314,
                "backend": "PyPI"
            },
            "message": {
                "project": "arrow",
                "new": "python-arrow",
                "agent": "http://ralph.id.fedoraproject.org/",
                "distro": "Fedora"
            },
            "distro": {
                "name": "Fedora"
            }
        }
    }


class LegacyTestNewMappingProject(Base):
    """ These messages are published when someone maps an upstream project to a
    package name in a particular distribution (in the `anitya
    <https://release-monitoring.org>`_ database...)
    """
    expected_title = "anitya.project.map.new"
    expected_subti = 'ralph mapped the name of "arrow"' + \
        ' in Fedora to "python-arrow"'
    expected_link = "https://release-monitoring.org/project/5314/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
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
    (in the `anitya <https://release-monitoring.org>`_ database...)
    """
    expected_title = "anitya.project.map.update"
    expected_subti = 'ralph updated the name of ' + \
        '"guake" in "Fedora" from "guake2" to "guake"'
    expected_link = "https://release-monitoring.org/project/5311/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
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
                "regex": None,
                "name": "guake",
                "created_on": 1412237149.0,
                "version": "0.5.0",
                "versions": [],
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
                "agent": "http://ralph.id.fedoraproject.org/",
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


class LegacyTestUpdatedMappingProject(Base):
    """ These messages are published when someone updates the mapping between
    an upstream project and a package name in a particular distribution
    (in the `anitya <https://release-monitoring.org>`_ database...)
    """
    expected_title = "anitya.project.map.update"
    expected_subti = 'ralph updated the name of ' + \
        '"guake" in "Fedora" from "guake2" to "guake"'
    expected_link = "https://release-monitoring.org/project/5311/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
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


class TestFirstNewUpstreamVersionLegacy(Base):
    expected_title = "anitya.project.version.update"
    expected_subti = ('A new version of "Accanthis-Std" has been detected:  "20101124", '
        'packaged as "adf-accanthis-fonts"')
    expected_link = "https://release-monitoring.org/project/22/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    #expected_secondary_icon = None
    expected_packages = set([
        'adf-accanthis-fonts',
    ])
    expected_usernames = set(['anitya'])
    expected_objects = set([
        'projects/Accanthis-Std',
    ])
    msg = {
        "username": "anitya",
        "i": 1,
        "timestamp": 1412790624,
        "msg_id": "2014-3120499f-993b-4526-81c7-8abc39207f9e",
        "topic": "org.release-monitoring.prod.anitya.project.version.update",
        "msg": {
            "project": {
                "regex": "",
                "name": "Accanthis-Std",
                "created_on": 1412174945.0,
                "version": "20101124",
                "version_url": "http://arkandis.tuxfamily.org/adffonts.html",
                "updated_on": 1412697102.0,
                "homepage": "http://arkandis.tuxfamily.org/adffonts.html",
                "id": 22,
                "backend": "custom"
            },
            "packages": [
                {
                    "package_name": "adf-accanthis-fonts",
                    "distro": "Fedora"
                }
            ],
            "old_version": "",
            "upstream_version": "20101124",
            "versions": [
                "20101124"
            ]
        }
    }


class TestNewUpstreamVersion(Base):
    """ The purpose of anitya is to monitor upstream projects and to
    try and detect when they release new tarballs.

    *These* messages are the ones that get published when a tarball is found
    that is newer than the one last seen in the `anitya
    <https://release-monitoring.org>`_ database.
    """
    expected_title = "anitya.project.version.update"
    expected_subti = ('A new version of "2ping" has been detected:  "2.1.1" '
        'newer than "2.1.0", packaged as "2ping"')
    expected_link = "https://release-monitoring.org/project/2/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    #expected_secondary_icon = None
    expected_packages = set([
        '2ping',
    ])
    expected_usernames = set(['anitya'])
    expected_objects = set([
        'projects/2ping',
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
                "regex": None,
                "name": "2ping",
                "created_on": 1412174944.0,
                "version": "2.1.1",
                "version_url": "http://www.finnie.org/software/2ping/",
                "updated_on": 1412179539.0,
                "homepage": "http://www.finnie.org/software/2ping/",
                "id": 2,
                "backend": "custom"
            },
            "message": {
                "versions": [
                    "2.1.1"
                ],
                "old_version": "2.1.0",
                "upstream_version": "2.1.1",
                "project": {
                    "regex": None,
                    "name": "2ping",
                    "created_on": 1412174944.0,
                    "version": "2.1.1",
                    "version_url": "http://www.finnie.org/software/2ping/",
                    "updated_on": 1412179539.0,
                    "homepage": "http://www.finnie.org/software/2ping/",
                    "id": 2,
                    "backend": "custom"
                },
                "agent": "anitya",
                "packages": [
                    {
                        "package_name": "2ping",
                        "distro": "Fedora"
                    }
                ]
            },
            "distro": None
          }
    }


class TestOddNewUpstreamVersion(Base):
    """ The purpose of anitya is to monitor upstream projects and to
    try and detect when they release new tarballs.

    *These* messages are the ones that get published when a tarball is found
    that is older than the one last seen in the `anitya
    <https://release-monitoring.org>`_ database.
    """
    expected_title = "anitya.project.version.update"
    expected_subti = ('A new version of "2ping" has been detected:  '
        '"2.1.0", packaged as "2ping"')
    expected_link = "https://release-monitoring.org/project/2/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    #expected_secondary_icon = None
    expected_packages = set([
        '2ping',
    ])
    expected_usernames = set(['anitya'])
    expected_objects = set([
        'projects/2ping',
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
                "regex": None,
                "name": "2ping",
                "created_on": 1412174944.0,
                "version": "2.1.1",
                "version_url": "http://www.finnie.org/software/2ping/",
                "updated_on": 1412179539.0,
                "homepage": "http://www.finnie.org/software/2ping/",
                "id": 2,
                "backend": "custom"
            },
            "message": {
                "versions": [
                    "2.1.1"
                ],
                "old_version": "2.1.1",
                "upstream_version": "2.1.0",
                "project": {
                    "regex": None,
                    "name": "2ping",
                    "created_on": 1412174944.0,
                    "version": "2.1.1",
                    "version_url": "http://www.finnie.org/software/2ping/",
                    "updated_on": 1412179539.0,
                    "homepage": "http://www.finnie.org/software/2ping/",
                    "id": 2,
                    "backend": "custom"
                },
                "odd_change": True,
                "agent": "anitya",
                "packages": [
                    {
                        "package_name": "2ping",
                        "distro": "Fedora"
                    }
                ]
            },
            "distro": None
          }
    }


class TestNewUpstreamVersionMutiMap(Base):
    """ The purpose of anitya is to monitor upstream projects and to
    try and detect when they release new tarballs.

    *These* messages are the ones that get published when a tarball is found
    that is newer than the one last seen in the `anitya
    <https://release-monitoring.org>`_ database.
    """
    expected_title = "anitya.project.version.update"
    expected_subti = ('A new version of "SQLAlchemy" has been detected:  '
        '"1.0.0b1" newer than "0.9.9", packaged as '
        '"python-sqlalchemy and python-sqlalchemy0.5"')
    expected_link = "https://release-monitoring.org/project/4034/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    #expected_secondary_icon = None
    expected_packages = set(['python-sqlalchemy', 'python-sqlalchemy0.5'])
    expected_usernames = set(['anitya'])
    expected_objects = set([
        'projects/SQLAlchemy',
    ])
    msg = {
      "source_name": "datanommer",
      "i": 17,
      "timestamp": 1426296431.0,
      "msg_id": "2015-b2e3fab5-12a6-47b0-9ffc-c21d5789a2d0",
      "topic": "org.release-monitoring.prod.anitya.project.version.update",
      "source_version": "0.6.4",
      "msg": {
            "project": {
            "regex": None,
            "name": "SQLAlchemy",
            "versions": [
                "1.0.0b1",
                "0.9.9",
                "0.9.8",
                "0.9.7"
                ],
            "created_on": 1412175085.0,
            "version": "1.0.0b1",
            "version_url": None,
            "updated_on": 1426296430.0,
            "homepage": "https://pypi.python.org/pypi/SQLAlchemy",
            "id": 4034,
            "backend": "pypi"
            },
            "message": {
                "versions": [
                    "1.0.0b1",
                    "0.9.9",
                    "0.9.8",
                    "0.9.7"
                    ],
                "old_version": "0.9.9",
                "upstream_version": "1.0.0b1",
                "project": {
                    "regex": None,
                    "name": "SQLAlchemy",
                    "versions": [
                    "1.0.0b1",
                    "0.9.9",
                    "0.9.8",
                    "0.9.7"
                    ],
                "created_on": 1412175085.0,
                "version": "1.0.0b1",
                "version_url": None,
                "updated_on": 1426167440.0,
                "homepage": "https://pypi.python.org/pypi/SQLAlchemy",
                "id": 4034,
                "backend": "pypi"
                 },
                "agent": "anitya",
                "packages": [
                    {
                        "package_name": "python-sqlalchemy",
                        "distro": "Fedora"
                    },
                    {
                        "package_name": "python-sqlalchemy0.5",
                        "distro": "Fedora"
                    }
                ]
            },
            "distro": None
        }
    }


class TestFirstNewUpstreamVersion(Base):
    """ The purpose of anitya is to monitor upstream projects and to
    try and detect when they release new tarballs.

    *This* message is an example of what gets published when **the first
    tarball of a project is ever seen** by `anitya
    <https://release-monitoring.org>`_.
    """
    expected_title = "anitya.project.version.update"
    expected_subti = ('A new version of "2ping" has been detected:  "2.1.1", '
        'packaged as "2ping"')
    expected_link = "https://release-monitoring.org/project/2/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    #expected_secondary_icon = None
    expected_packages = set([
        '2ping',
    ])
    expected_usernames = set(['anitya'])
    expected_objects = set([
        'projects/2ping',
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
                "regex": None,
                "name": "2ping",
                "created_on": 1412174944.0,
                "version": "2.1.1",
                "version_url": "http://www.finnie.org/software/2ping/",
                "updated_on": 1412179539.0,
                "homepage": "http://www.finnie.org/software/2ping/",
                "id": 2,
                "backend": "custom"
            },
            "message": {
                "versions": [
                    "2.1.1"
                ],
                "old_version": "",
                "upstream_version": "2.1.1",
                "project": {
                    "regex": None,
                    "name": "2ping",
                    "created_on": 1412174944.0,
                    "version": "2.1.1",
                    "version_url": "http://www.finnie.org/software/2ping/",
                    "updated_on": 1412179539.0,
                    "homepage": "http://www.finnie.org/software/2ping/",
                    "id": 2,
                    "backend": "custom"
                },
                "agent": "anitya",
                "packages": [
                    {
                        "package_name": "2ping",
                        "distro": "Fedora"
                    }
                ]
            },
            "distro": None
          }
    }


class TestRemoveMappingProject(Base):
    """ These messages are published when someone *removes* a mapping
    between an upstream project and a package name in a particular
    distribution (in the `anitya <https://release-monitoring.org>`_
    database...)
    """
    expected_title = "anitya.project.map.remove"
    expected_subti = 'pingou deleted the mapping of ' + \
        '"guake" project on "Fedora"'
    expected_link = "https://release-monitoring.org/project/5311/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
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
                "agent": "http://pingou.id.fedoraproject.org/",
                "distro": "Fedora"
            },
            "distro": None
        }
    }


class LegacyTestRemoveMappingProject(Base):
    """ These messages are published when someone *removes* a mapping
    between an upstream project and a package name in a particular
    distribution (in the `anitya <https://release-monitoring.org>`_
    database...)
    """
    expected_title = "anitya.project.map.remove"
    expected_subti = 'pingou deleted the mapping of ' + \
        '"guake" project on "Fedora"'
    expected_link = "https://release-monitoring.org/project/5311/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
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


class TestRemoveVersionProject(Base):
    """ These messages are published when an admin *removes* a version
    from a particular project (in the `anitya <https://release-monitoring.org>`_
    database...)
    """
    expected_title = "anitya.project.version.remove"
    expected_subti = 'pingou deleted the version 0.7.1.1 of "3proxy"'
    expected_link = "https://release-monitoring.org/project/3/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['projects/3proxy'])
    msg = {
        "username": "pingou",
        "i": 1,
        "timestamp": 1415118527,
        "msg_id": "2014-7926f638-1d0c-470c-b589-de84f5d34fad",
        "topic": "org.release-monitoring.prod.anitya.project.version.remove",
        "msg": {
            "project": {
                "regex": None,
                "name": "3proxy",
                "created_on": 1409917223.0,
                "version": "0.7.1.1",
                "versions": [],
                "version_url": "http://www.3proxy.ru/download/",
                "updated_on": 1412690620.0,
                "homepage": "http://www.3proxy.ru/download/",
                "id": 3,
                "backend": "custom"
            },
            "message": {
                "project": "3proxy",
                "version": "0.7.1.1",
                "agent": "http://pingou.id.fedoraproject.org/"
            },
            "distro": None
        }
    }


class LegacyTestRemoveVersionProject(Base):
    """ These messages are published when an admin *removes* a version
    from a particular project (in the `anitya <https://release-monitoring.org>`_
    database...)
    """
    expected_title = "anitya.project.version.remove"
    expected_subti = 'pingou deleted the version 0.7.1.1 of "3proxy"'
    expected_link = "https://release-monitoring.org/project/3/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['projects/3proxy'])
    msg = {
        "username": "pingou",
        "i": 1,
        "timestamp": 1415118527,
        "msg_id": "2014-7926f638-1d0c-470c-b589-de84f5d34fad",
        "topic": "org.release-monitoring.prod.anitya.project.version.remove",
        "msg": {
            "project": {
                "regex": None,
                "name": "3proxy",
                "created_on": 1409917223.0,
                "version": "0.7.1.1",
                "version_url": "http://www.3proxy.ru/download/",
                "updated_on": 1412690620.0,
                "homepage": "http://www.3proxy.ru/download/",
                "id": 3,
                "backend": "custom"
            },
            "message": {
                "project": "3proxy",
                "version": "0.7.1.1",
                "agent": "pingou@fedoraproject.org"
            },
            "distro": None
        }
    }


class TestRemoveDistro(Base):
    """ These messages are published when an admin *removes* a distribution
    (in the `anitya <https://release-monitoring.org>`_ database...)
    """
    expected_title = "anitya.distro.remove"
    expected_subti = 'pingou deleted the distro "Arch"'
    expected_link = "https://release-monitoring.org/distros"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['distros/Arch'])
    msg = {
        "username": "pierrey",
        "i": 4,
        "timestamp": 1418315977,
        "msg_id": "2014-745132e5-17eb-4785-8663-fa89801a08ee",
        "topic": "org.release-monitoring.dev.anitya.distro.remove",
        "msg": {
            "project": None,
            "message": {
                "agent": "http://pingou.id.fedoraproject.org/",
                "distro": "Arch"
            },
            "distro": {
                "name": "Arch"
            }
        }
    }


class LegacyTestRemoveDistro(Base):
    """ These messages are published when an admin *removes* a distribution
    (in the `anitya <https://release-monitoring.org>`_ database...)
    """
    expected_title = "anitya.distro.remove"
    expected_subti = 'pingou deleted the distro "Arch"'
    expected_link = "https://release-monitoring.org/distros"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['distros/Arch'])
    msg = {
        "username": "pierrey",
        "i": 4,
        "timestamp": 1418315977,
        "msg_id": "2014-745132e5-17eb-4785-8663-fa89801a08ee",
        "topic": "org.release-monitoring.dev.anitya.distro.remove",
        "msg": {
            "project": None,
            "message": {
                "agent": "pingou@fedoraproject.org",
                "distro": "Arch"
            },
            "distro": {
                "name": "Arch"
            }
        }
    }


class TestProjectFlag(Base):
    """ These messages are published when an user *flags* a project
    in the `anitya <https://release-monitoring.org>`_ database to ask an
    admin to do something on a project.
    """
    expected_title = "anitya.project.flag"
    expected_subti = 'pingou flagged the project "generic-colouriser"'
    expected_link = "https://release-monitoring.org/project/5777/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['projects/generic-colouriser'])
    msg = {
          "source_name": "datanommer",
          "i": 4,
          "timestamp": 1445900487.0,
          "msg_id": "2015-7b2fca29-7409-43f2-949f-c688437ba5d4",
          "topic": "org.release-monitoring.prod.anitya.project.flag",
          "source_version": "0.6.5",
          "msg": {
            "project": {
              "regex": None,
              "name": "generic-colouriser",
              "versions": [
                "v1.9",
                "v1.7"
              ],
              "created_on": 1425912743.0,
              "version": "v1.9",
              "version_url": "garabik/grc",
              "updated_on": 1427848695.0,
              "homepage": "http://kassiopeia.juls.savba.sk/~garabik/software/grc.html",
              "id": 5777,
              "backend": "Github"
            },
            "message": {
              "project": "generic-colouriser",
              "reason": "Delete in favor of the correctly configured 7894.",
              "agent": "http://pingou.id.fedoraproject.org/"
            },
            "distro": None
          }
        }


class LegacyTestProjectFlag(Base):
    """ These messages are published when an user *flags* a project
    in the `anitya <https://release-monitoring.org>`_ database to ask an
    admin to do something on a project.
    """
    expected_title = "anitya.project.flag"
    expected_subti = 'pingou flagged the project "generic-colouriser"'
    expected_link = "https://release-monitoring.org/project/5777/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['projects/generic-colouriser'])
    msg = {
          "source_name": "datanommer",
          "i": 4,
          "timestamp": 1445900487.0,
          "msg_id": "2015-7b2fca29-7409-43f2-949f-c688437ba5d4",
          "topic": "org.release-monitoring.prod.anitya.project.flag",
          "source_version": "0.6.5",
          "msg": {
            "project": {
              "regex": "",
              "name": "generic-colouriser",
              "versions": [
                "v1.9",
                "v1.7"
              ],
              "created_on": 1425912743.0,
              "version": "v1.9",
              "version_url": "garabik/grc",
              "updated_on": 1427848695.0,
              "homepage": "http://kassiopeia.juls.savba.sk/~garabik/software/grc.html",
              "id": 5777,
              "backend": "Github"
            },
            "message": {
              "project": "generic-colouriser",
              "reason": "Delete in favor of the correctly configured 7894.",
              "agent": "pingou@fedoraproject.org"
            },
            "distro": None
          }
        }


class TestProjectFlag_WithPackages(Base):
    """ These messages are published when an user *flags* a project
    in the `anitya <https://release-monitoring.org>`_ database to ask an
    admin to do something on a project.
    """
    expected_title = "anitya.project.flag"
    expected_subti = 'pingou flagged the project "generic-colouriser"'
    expected_link = "https://release-monitoring.org/project/5777/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set(['generic-colouriser'])
    expected_usernames = set(['pingou'])
    expected_objects = set(['projects/generic-colouriser'])
    msg = {
          "source_name": "datanommer",
          "i": 4,
          "timestamp": 1445900487.0,
          "msg_id": "2015-7b2fca29-7409-43f2-949f-c688437ba5d4",
          "topic": "org.release-monitoring.prod.anitya.project.flag",
          "source_version": "0.6.5",
          "msg": {
            "project": {
              "regex": None,
              "name": "generic-colouriser",
              "versions": [
                "v1.9",
                "v1.7"
              ],
              "created_on": 1425912743.0,
              "version": "v1.9",
              "version_url": "garabik/grc",
              "updated_on": 1427848695.0,
              "homepage": "http://kassiopeia.juls.savba.sk/~garabik/software/grc.html",
              "id": 5777,
              "backend": "GitHub"
            },
            "message": {
              "project": "generic-colouriser",
              "reason": "Delete in favor of the correctly configured 7894.",
              "agent": "http://pingou.id.fedoraproject.org/"
            },
            "distro": None,
            "packages": [
                {"package_name": "generic-colouriser", "distro": "Fedora"}
            ]
          }
        }


class LegacyTestProjectFlag_WithPackages(Base):
    """ These messages are published when an user *flags* a project
    in the `anitya <https://release-monitoring.org>`_ database to ask an
    admin to do something on a project.
    """
    expected_title = "anitya.project.flag"
    expected_subti = 'pingou flagged the project "generic-colouriser"'
    expected_link = "https://release-monitoring.org/project/5777/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set(['generic-colouriser'])
    expected_usernames = set(['pingou'])
    expected_objects = set(['projects/generic-colouriser'])
    msg = {
          "source_name": "datanommer",
          "i": 4,
          "timestamp": 1445900487.0,
          "msg_id": "2015-7b2fca29-7409-43f2-949f-c688437ba5d4",
          "topic": "org.release-monitoring.prod.anitya.project.flag",
          "source_version": "0.6.5",
          "msg": {
            "project": {
              "regex": "",
              "name": "generic-colouriser",
              "versions": [
                "v1.9",
                "v1.7"
              ],
              "created_on": 1425912743.0,
              "version": "v1.9",
              "version_url": "garabik/grc",
              "updated_on": 1427848695.0,
              "homepage": "http://kassiopeia.juls.savba.sk/~garabik/software/grc.html",
              "id": 5777,
              "backend": "Github"
            },
            "message": {
              "project": "generic-colouriser",
              "reason": "Delete in favor of the correctly configured 7894.",
              "agent": "pingou@fedoraproject.org"
            },
            "distro": None,
            "packages": [
                {"package_name": "generic-colouriser", "distro": "Fedora"}
            ]
          }
        }


class TestFlagSet(Base):
    """ These messages are published when an user change the status of a
    flag in the `anitya <https://release-monitoring.org>`_ database.
    """
    expected_title = "anitya.project.flag.set"
    expected_subti = 'pingou closed flag "184"'
    expected_link = "https://release-monitoring.org/"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c" + \
        "?s=64&d=retro"
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    expected_objects = set(['flag/184'])
    msg = {
          "source_name": "datanommer",
          "i": 4,
          "timestamp": 1468318351.0,
          "msg_id": "2016-fc73c74c-fc5a-4f65-8ae9-87145bae82e4",
          "topic": "org.release-monitoring.prod.anitya.project.flag.set",
          "source_version": "0.6.5",
          "msg": {
            "project": None,
            "message": {
              "flag": 184,
              "state": "closed",
              "agent": "pingou@fedoraproject.org"
            },
            "distro": None
          }
        }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
