# This file is part of fedmsg.
# Copyright (C) 2017 Red Hat, Inc.
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
""" Tests for MBS messages """

import unittest

from fedmsg_meta_fedora_infrastructure.tests.base import Base

from .common import add_doc


class TestModuleBuildStateChange(Base):
    """ These messages are published by the `module build service
    <https://fedoraproject.org/wiki/Changes/ModuleBuildService>`_ when a module
    build transitions between states (like starting, or completing).
    """
    expected_title = "mbs.module.state.change"
    expected_subti = "ralph's build of modules/testmodule " + \
        "entered the wait state."
    expected_link = "https://mbs.fedoraproject.org/module-build-service/1/module-builds/2"
    expected_icon = "https://apps.fedoraproject.org/img/icons/modularity.png"
    expected_secondary_icon = "https://seccdn.libravatar.org/avatar/" + \
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c" + \
        "?s=64&d=retro"
    expected_packages = set([
        # TODO -- we'll eventually have to think about how to show all relevant
        # packages here.  Are "modules" really a package, from this PoV?
    ])
    expected_usernames = set(['ralph'])
    expected_objects = set(['testmodule'])
    msg = {
        "source_name": "datanommer",
        "i": 1,
        "timestamp": 1487188431.0,
        "msg_id": "2017-859a8cfb-6d95-43f4-9c0b-897e833b06b5",
        "topic": "org.fedoraproject.stg.mbs.module.state.change",
        "source_version": "0.6.5",
        "msg": {
            "state_reason": None,
            "component_builds": [
                19,
                20,
                21
            ],
            "name": "testmodule",
            "stream": "master",
            "time_submitted": 1487178787.0,
            "state_url": "/module-build-service/1/module-builds/2",
            "time_modified": 1487188430.0,
            "scmurl": "git://pkgs.stg.fedoraproject.org/modules/testmodule.git?#620ec77",
            "state": 1,
            "modulemd": "full modulemd text goes here...",
            "time_completed": None,
            "version": "20161115001755",
            "owner": "ralph",
            "id": 2,
            "state_name": "wait"
        }
    }



add_doc(locals())

if __name__ == '__main__':
    unittest.main()
