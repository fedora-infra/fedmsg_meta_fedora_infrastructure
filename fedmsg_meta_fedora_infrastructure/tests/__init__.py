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
from fedmsg_meta_fedora_infrastructure.tests.compose2 import *
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
from fedmsg_meta_fedora_infrastructure.tests.zanata import *
from fedmsg_meta_fedora_infrastructure.tests.zodbot import *
from fedmsg_meta_fedora_infrastructure.tests.faf import *
from fedmsg_meta_fedora_infrastructure.tests.pagure import *
from fedmsg_meta_fedora_infrastructure.tests.autocloud import *
from fedmsg_meta_fedora_infrastructure.tests.infragit import *
from fedmsg_meta_fedora_infrastructure.tests.taskotron import *
from fedmsg_meta_fedora_infrastructure.tests.releng import *
from fedmsg_meta_fedora_infrastructure.tests.mdapi import *
from fedmsg_meta_fedora_infrastructure.tests.nagios import *
from fedmsg_meta_fedora_infrastructure.tests.openqa import *
from fedmsg_meta_fedora_infrastructure.tests.pdc import *
from fedmsg_meta_fedora_infrastructure.tests.mbs import *
from fedmsg_meta_fedora_infrastructure.tests.centos_ci import *
from fedmsg_meta_fedora_infrastructure.tests.waiverdb import *
from fedmsg_meta_fedora_infrastructure.tests.greenwave import *
from fedmsg_meta_fedora_infrastructure.tests.rats import *

from fedmsg_meta_fedora_infrastructure.tests.base import Base

from fedmsg_meta_fedora_infrastructure.tests.common import add_doc


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
        "https://src.fedoraproject.org/rpms/valgrind/commits/master"
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
        "https://src.fedoraproject.org/rpms/valgrind/commits/master"
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
    expected_link = 'https://src.fedoraproject.org/lookaside/pkgs/' + \
        'texlive/pst-diffraction.doc.tar.xz/' + \
        'dacad985394b3977f9dcf0c75f51a357/' + \
        'pst-diffraction.doc.tar.xz'
    expected_long_form = \
        'dacad985394b3977f9dcf0c75f51a357  pst-diffraction.doc.tar.xz'
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
    expected_link = 'https://src.fedoraproject.org/lookaside/pkgs/' + \
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


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
