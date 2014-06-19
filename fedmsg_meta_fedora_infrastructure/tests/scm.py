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
# Authors:  Ian Weller <ianweller@fedoraproject.org>
#
""" Tests for git messages """

import unittest

from fedmsg.tests.test_meta import Base

from common import add_doc


class TestGitReceiveOldModified(Base):
    """ Sample message from the first generation of git-category messages that
    have been modified in datanommer to match the new topics.
    """

    expected_title = "git.receive"
    expected_subti = ('rbean@redhat.com pushed to datanommer (master).  "Try '
                      'removing requirement on python-bunch."')
    expected_secondary_icon = (
        'https://seccdn.libravatar.org/avatar/'
        '1a0d2acfddb1911ecf55da42cfa34710'
        '?s=64&d=retro')
    expected_packages = set(['datanommer'])
    expected_usernames = set()
    expected_objects = set(['datanommer/datanommer.spec'])
    expected_link = ("http://pkgs.fedoraproject.org/cgit/datanommer.git/commit"
                     "/?h=master&id=66abdea4014eb2f0745fc38f86e20c7d7009237e")

    msg = {
        "i": 1,
        "msg": {
            "commit": {
                "branch": "master",
                "email": "rbean@redhat.com",
                "message": "Try removing requirement on python-bunch.\n",
                "name": "Ralph Bean",
                "repo": "datanommer",
                "rev": "66abdea4014eb2f0745fc38f86e20c7d7009237e",
                "stats": {
                    "files": {
                        "datanommer.spec": {
                            "deletions": 6,
                            "insertions": 4,
                            "lines": 10
                        }
                    },
                    "total": {
                        "deletions": 6,
                        "files": 1,
                        "insertions": 4,
                        "lines": 10
                    }
                },
                "summary": "Try removing requirement on python-bunch."
            }
        },
        "timestamp": 1349735155.0,
        "topic": "org.fedoraproject.prod.git.receive"
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
