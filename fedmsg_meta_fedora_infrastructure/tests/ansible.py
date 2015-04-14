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
""" Tests for ansible messages """

import unittest

from fedmsg.tests.test_meta import Base

from .common import add_doc


class TestAnsiblePlaybookStart(Base):
    """ These messages are published when an admin begins an ansible
    playbook run.  We use that system to manage the servers that
    run fedoraproject.org.
    """

    expected_title = "ansible.playbook.start"
    expected_subti = ('ralph started an ansible run of '
                      'playbooks/groups/badges-backend.yml')
    expected_link = ("http://infrastructure.fedoraproject.org/cgit/"
                     "ansible.git/tree/playbooks/groups/badges-backend.yml")
    expected_icon = "https://apps.fedoraproject.org/img/icons/ansible.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['playbooks/groups/badges-backend.yml'])
    msg = {
        "username": "root",
        "i": 1,
        "timestamp": 1375753735.32427,
        "topic": "org.fedoraproject.prod.ansible.playbook.start",
        "msg": {
            "playbook_checksum": False,
            "extra_vars": {},
            "userid": "ralph",
            "playbook": "/srv/web/infra/ansible/playbooks/groups/"
            "badges-backend.yml",
            "check": False,
            "inventory": "/srv/web/infra/ansible/inventory/"
        }
    }


class TestAnsiblePlaybookComplete(Base):
    """ These messages are published when an admin finishes an ansible
    playbook run.  We use that system to manage the servers that
    run fedoraproject.org.  Here's an example with a playbook that has been
    checked into our SCM repo.
    """
    expected_title = "ansible.playbook.complete"
    expected_subti = ("ralph's playbooks/groups/badges-backend.yml playbook"
                      " run completed")
    expected_link = ("http://infrastructure.fedoraproject.org/cgit/"
                     "ansible.git/tree/playbooks/groups/badges-backend.yml")
    expected_icon = "https://apps.fedoraproject.org/img/icons/ansible.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'playbooks/groups/badges-backend.yml',
        'inventory/badges-backend01.phx2.fedoraproject.org',
        'inventory/badges-backend01.stg.phx2.fedoraproject.org',
    ])
    msg = {
        "username": "root",
        "i": 2,
        "timestamp": 1375753955.771203,
        "topic": "org.fedoraproject.prod.ansible.playbook.complete",
        "msg": {
            "userid": "ralph",
            "playbook": "/srv/web/infra/ansible/playbooks/groups/"
            "badges-backend.yml",
            "results": {
                "badges-backend01.phx2.fedoraproject.org": {
                    "failures": 0,
                    "skipped": 9,
                    "ok": 56,
                    "changed": 1,
                    "unreachable": 0
                },
                "badges-backend01.stg.phx2.fedoraproject.org": {
                    "failures": 0,
                    "skipped": 9,
                    "ok": 56,
                    "changed": 1,
                    "unreachable": 0
                }
            }
        }
    }


class TestAnsiblePlaybookCompleteNotCheckIn(Base):
    """ These messages are published when an admin finishes an ansible
    playbook run.  We use that system to manage the servers that
    run fedoraproject.org.  Here's an example with a playbook that is not
    actually checked into our SCM repo.
    """

    expected_title = "ansible.playbook.complete"
    expected_subti = "ralph's badges-backend.yml playbook run completed"
    expected_link = None
    expected_icon = "https://apps.fedoraproject.org/img/icons/ansible.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'uncontrolled-playbooks/badges-backend.yml',
        'inventory/badges-backend01.phx2.fedoraproject.org',
        'inventory/badges-backend01.stg.phx2.fedoraproject.org',
    ])
    msg = {
        "username": "root",
        "i": 2,
        "timestamp": 1375753955.771203,
        "topic": "org.fedoraproject.prod.ansible.playbook.complete",
        "msg": {
            "userid": "ralph",
            "playbook": "/home/fedora/ralph/ansible/playbooks/groups/"
            "badges-backend.yml",
            "results": {
                "badges-backend01.phx2.fedoraproject.org": {
                    "failures": 0,
                    "skipped": 9,
                    "ok": 56,
                    "changed": 1,
                    "unreachable": 0
                },
                "badges-backend01.stg.phx2.fedoraproject.org": {
                    "failures": 0,
                    "skipped": 9,
                    "ok": 56,
                    "changed": 1,
                    "unreachable": 0
                }
            }
        }
    }


add_doc(locals())


if __name__ == '__main__':
    unittest.main()
