# This file is part of fedmsg.
# Copyright (C) 2015 Red Hat, Inc.
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
# Authors: Ralph Bean <rbean@redhat.com>
#
""" Tests for infra git messages (ansible, dns, etc..) """

import unittest

from fedmsg_meta_fedora_infrastructure.tests.base import Base

from .common import add_doc


class TestInfraGitPuppet(Base):
    """ These messages get published by git repos owned by the Fedora
    Infrastructure team.  These are the repos we use to manage the systems that
    run fedoraproject.org.

    In particular, this message is an example of a message from our "puppet"
    repo, which is older and being retired in favor of our ansible repo.
    """
    expected_title = "infragit.receive"
    expected_subti = 'ralph pushed a commit to the fedora-infra puppet ' + \
        'repo (master):  "Testing again for fedmsg."'
    expected_link = ''  # No links for puppet
    expected_icon = "https://apps.fedoraproject.org/img/icons/git-logo.png"
    expected_secondary_icon = ("https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c"
        "?s=64&d=retro")
    expected_usernames = set(['ralph'])
    expected_agent = 'ralph'
    expected_packages = set()
    expected_objects = set(['puppet/test'])
    msg = {
        "i": 1,
        "timestamp": 1439584387.0,
        "msg_id": "2015-ee126d0a-a89b-4a09-ba15-4ca3382eb8fe",
        "topic": "org.fedoraproject.prod.infragit.receive",
        "source_version": "0.6.5",
        "msg": {
            "commit": {
                "username": "ralph",
                "stats": {
                    "files": {
                        "test": {
                            "deletions": 0,
                            "additions": 0,
                            "lines": 0
                        }
                    },
                    "total": {
                        "deletions": 0,
                        "files": 1,
                        "additions": 0,
                        "lines": 0
                    }
                },
                "name": "Ralph Bean",
                "rev": "6e7177a1d5fd712cb53ce70acb17b92c5f791f08",
                "agent": "ralph",
                "summary": "Testing again for fedmsg.",
                "repo": "",
                "branch": "master",
                "seen": False,
                "path": "/git/puppet",
                "message": "Testing again for fedmsg.\n",
                "email": "rbean@redhat.com"
            }
        }
    }


class TestInfraGitAnsible(Base):
    """ These messages get published by git repos owned by the Fedora
    Infrastructure team.  These are the repos we use to manage the systems that
    run fedoraproject.org.

    In particular, this message is an example of a message from our "ansible"
    repo, which is where we do most of our work.
    """
    expected_title = "infragit.receive"
    expected_subti = 'ralph pushed a commit to the fedora-infra ansible ' + \
        'repo (master):  "Testing again for fedmsg."'
    expected_link = "https://infrastructure.fedoraproject.org/cgit/" + \
        "ansible.git/commit/" + \
        "?h=master&id=6e7177a1d5fd712cb53ce70acb17b92c5f791f08"
    expected_icon = "https://apps.fedoraproject.org/img/icons/git-logo.png"
    expected_secondary_icon = ("https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c"
        "?s=64&d=retro")
    expected_usernames = set(['ralph'])
    expected_agent = 'ralph'
    expected_packages = set()
    expected_objects = set(['ansible/test'])
    msg = {
        "i": 1,
        "timestamp": 1439584387.0,
        "msg_id": "2015-ee126d0a-a89b-4a09-ba15-4ca3382eb8fe",
        "topic": "org.fedoraproject.prod.infragit.receive",
        "source_version": "0.6.5",
        "msg": {
            "commit": {
                "username": "ralph",
                "stats": {
                    "files": {
                        "test": {
                            "deletions": 0,
                            "additions": 0,
                            "lines": 0
                        }
                    },
                    "total": {
                        "deletions": 0,
                        "files": 1,
                        "additions": 0,
                        "lines": 0
                    }
                },
                "name": "Ralph Bean",
                "rev": "6e7177a1d5fd712cb53ce70acb17b92c5f791f08",
                "agent": "ralph",
                "summary": "Testing again for fedmsg.",
                "repo": "",
                "branch": "master",
                "seen": False,
                "path": "/git/ansible",
                "message": "Testing again for fedmsg.\n",
                "email": "rbean@redhat.com"
            }
        }
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
