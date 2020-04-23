# This file is part of fedmsg.
# Copyright (C) 2020 Red Hat, Inc.
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
# Authors:  Jan Kaluza <jkaluza@redhat.com>
#
""" Tests for ODCS messages """

import unittest

from fedmsg_meta_fedora_infrastructure.tests.base import Base

from .common import add_doc


class TestComposeStateChanged(Base):
    """ These messages are published by the `module build service
    <https://fedoraproject.org/wiki/Changes/ModuleBuildService>`_ when a module
    build transitions between states (like starting, or completing).
    """
    expected_title = "odcs.compose.state-changed"
    expected_subti = "jkaluza's compose 378 " + \
        "entered the generating state."
    expected_link = "https://odcs.fedoraproject.org/api/1/composes/378"
    expected_icon = "https://apps.fedoraproject.org/img/icons/odcs.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "1ecc757d81ddcab5c53f2d5741595dece34d1e6519a39d57a8fa4af6b8b12b11" + \
        "?s=64&d=retro"
    expected_usernames = set(['jkaluza'])
    expected_objects = set([378])
    msg = {
        "username": "amqp-bridge", 
        "source_name": "datanommer", 
        "i": 1, 
        "timestamp": 1587619319.0, 
        "msg_id": "2020-e857c141-3a16-411c-932c-bd16fc354e7a", 
        "crypto": "x509", 
        "topic": "org.fedoraproject.stg.odcs.compose.state-changed", 
        "source_version": "0.9.0", 
        "msg": {
            "compose": {
                "state_name": "generating", 
                "sigkeys": "", 
                "target_dir": "default", 
                "results": [
                    "repository"
                ], 
                "time_removed": None, 
                "owner": "jkaluza", 
                "toplevel_url": "https://odcs.stg.fedoraproject.org/composes/odcs-378", 
                "id": 378, 
                "state_reason": "Compose thread started", 
                "multilib_method": 0, 
                "multilib_arches": "", 
                "modular_koji_tags": None, 
                "lookaside_repos": "", 
                "label": None, 
                "source": "eln#eln", 
                "state": 1, 
                "compose_type": "test", 
                "flags": [], 
                "module_defaults_url": None, 
                "koji_event": None, 
                "source_type": 5, 
                "koji_task_id": None, 
                "packages": None, 
                "time_started": "2020-04-23T05:21:58Z", 
                "builds": None, 
                "time_submitted": "2020-04-23T05:21:58Z", 
                "arches": "x86_64", 
                "time_to_expire": "2020-04-24T05:21:58Z", 
                "pungi_compose_id": None, 
                "time_done": None, 
                "removed_by": None, 
            }, 
            "event": "state-changed"
        }
    }



add_doc(locals())

if __name__ == '__main__':
    unittest.main()
