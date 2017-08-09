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
# Authors:  Ian Weller <ianweller@fedoraproject.org>
#           Ralph Bean <rbean@redhat.com>
#
""" Tests for git messages """

import os
import unittest

from fedmsg.tests.test_meta import Base

from .common import add_doc


here = os.path.dirname(os.path.abspath(__file__))
with open(here + '/example.patch', 'r') as f:
    full_patch = f.read()


class TestGitReceiveLegacyModified(Base):
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
    expected_link = ("https://src.fedoraproject.org/rpms/datanommer/c/"
                     "66abdea4014eb2f0745fc38f86e20c7d7009237e?branch=master")

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

class TestSCMSuperLegacy(Base):
    """ Support super-duper oldschool git messages.  :(:( """

    expected_title = "git.receive.valgrind.master"
    expected_subti = 'mjw pushed to valgrind (master).  ' + \
        '"Clear CFLAGS CXXFLAGS LDFLAGS. (..more)"'
    expected_link = "https://src.fedoraproject.org/rpms/" + \
        "valgrind/c/" + \
        "7a98f80d9b61ce167e4ef8129c81ed9284ecf4e1?branch=master"
    expected_icon = "https://apps.fedoraproject.org/img/icons/git-logo.png"
    expected_secondary_icon = ("https://seccdn.libravatar.org/avatar/"
        "0f32874b1ae3083205c874c83cd2d21715c89b8645483f353e90ae499c67c944"
        "?s=64&d=retro")
    expected_usernames = set(['mjw'])
    expected_packages = set(['valgrind'])
    expected_objects = set(['valgrind/valgrind.spec'])

    msg = {
        "i": 1,
        "timestamp": 1344350850.8867381,
        "topic": "org.fedoraproject.prod.git.receive.valgrind.master",
        "msg": {
            "commit": {
                "stats": {
                    "files": {
                        "valgrind.spec": {
                            "deletions": 2,
                            "lines": 3,
                            "insertions": 1
                        }
                    },
                    "total": {
                        "deletions": 2,
                        "files": 1,
                        "insertions": 1,
                        "lines": 3
                    }
                },
                "name": "Mark Wielaard",
                "rev": "7a98f80d9b61ce167e4ef8129c81ed9284ecf4e1",
                "summary": "Clear CFLAGS CXXFLAGS LDFLAGS.",
                "message": """Clear CFLAGS CXXFLAGS LDFLAGS.
                This is a bit of a hammer.""",
                "email": "mjw@redhat.com",
                "username": "mjw",
                "branch": "master",
            }
        }
    }


class TestSCMLegacy(Base):
    """ Support oldschool "fedpkg push" messages.  :( """

    expected_title = "git.receive.valgrind.master"
    expected_subti = 'mjw pushed to valgrind (master).  ' + \
        '"Clear CFLAGS CXXFLAGS LDFLAGS. (..more)"'
    expected_link = "https://src.fedoraproject.org/rpms/" + \
        "valgrind/c/" + \
        "7a98f80d9b61ce167e4ef8129c81ed9284ecf4e1?branch=master"
    expected_icon = "https://apps.fedoraproject.org/img/icons/git-logo.png"
    expected_secondary_icon = ("https://seccdn.libravatar.org/avatar/"
        "0f32874b1ae3083205c874c83cd2d21715c89b8645483f353e90ae499c67c944"
        "?s=64&d=retro")
    expected_usernames = set(['mjw'])
    expected_packages = set(['valgrind'])
    expected_objects = set(['valgrind/valgrind.spec'])

    msg = {
        "i": 1,
        "timestamp": 1344350850.8867381,
        "topic": "org.fedoraproject.prod.git.receive.valgrind.master",
        "msg": {
            "commit": {
                "stats": {
                    "files": {
                        "valgrind.spec": {
                            "deletions": 2,
                            "lines": 3,
                            "insertions": 1
                        }
                    },
                    "total": {
                        "deletions": 2,
                        "files": 1,
                        "insertions": 1,
                        "lines": 3
                    }
                },
                "name": "Mark Wielaard",
                "rev": "7a98f80d9b61ce167e4ef8129c81ed9284ecf4e1",
                "summary": "Clear CFLAGS CXXFLAGS LDFLAGS.",
                "message": """Clear CFLAGS CXXFLAGS LDFLAGS.
                This is a bit of a hammer.""",
                "email": "mjw@redhat.com",
                "username": "mjw",
                "branch": "master",
                "repo": "valgrind",
            }
        }
    }


class TestSCM(Base):
    """ Messages like this one are published when somebody runs "fedpkg push"
    on a package.  Sometimes, the git message may be multiple lines long like:
    """
    expected_title = "git.receive"
    expected_subti = 'mjw pushed to valgrind (master).  ' + \
        '"Clear CFLAGS CXXFLAGS LDFLAGS. (..more)"'
    expected_link = "https://src.fedoraproject.org/rpms/" + \
        "valgrind/c/" + \
        "7a98f80d9b61ce167e4ef8129c81ed9284ecf4e1?branch=master"
    expected_long_form = "This commit already existed in another branch."
    expected_icon = "https://apps.fedoraproject.org/img/icons/git-logo.png"
    expected_secondary_icon = ("https://seccdn.libravatar.org/avatar/"
        "0f32874b1ae3083205c874c83cd2d21715c89b8645483f353e90ae499c67c944"
        "?s=64&d=retro")
    expected_usernames = set(['mjw'])
    expected_packages = set(['valgrind'])
    expected_objects = set(['valgrind/valgrind.spec'])

    msg = {
        "i": 1,
        "timestamp": 1344350850.8867381,
        "topic": "org.fedoraproject.prod.git.receive",
        "msg": {
            "commit": {
                "seen": True,
                "stats": {
                    "files": {
                        "valgrind.spec": {
                            "deletions": 2,
                            "lines": 3,
                            "insertions": 1
                        }
                    },
                    "total": {
                        "deletions": 2,
                        "files": 1,
                        "insertions": 1,
                        "lines": 3
                    }
                },
                "name": "Mark Wielaard",
                "rev": "7a98f80d9b61ce167e4ef8129c81ed9284ecf4e1",
                "summary": "Clear CFLAGS CXXFLAGS LDFLAGS.",
                "message": """Clear CFLAGS CXXFLAGS LDFLAGS.
                This is a bit of a hammer.""",
                "email": "mjw@redhat.com",
                "username": "mjw",
                "branch": "master",
                "repo": "valgrind",
            }
        }
    }


class TestSCMSingleLine(Base):
    """ Messages like this one are published when somebody runs "fedpkg push"
    on a package.  The whole git message is included for each commit.
    """
    expected_title = "git.receive"
    expected_subti = 'spot pushed to ember (master).  ' + \
        '"another missing patch? ridiculous."'
    expected_link = "https://src.fedoraproject.org/rpms/" + \
        "ember/c/" + \
        "aa2df80f3d8dd217c7cbfe2d3451190028f3fe14?branch=master"
    expected_icon = "https://apps.fedoraproject.org/img/icons/git-logo.png"
    expected_secondary_icon = ("https://seccdn.libravatar.org/avatar/"
        "1e232310ef80ec8b34b0bc216864efd0d837f419e6988997cda8e98a28be48dd"
        "?s=64&d=retro")
    expected_usernames = set(['spot'])
    expected_packages = set(['ember'])
    expected_objects = set(['ember/ember-0.6.3-gcc47.patch'])

    msg = {
        "i": 1,
        "timestamp": 1352998154.368305,
        "topic": "org.fedoraproject.prod.git.receive",
        "msg": {
            "commit": {
                "username": "spot",
                "stats": {
                    "files": {
                        "ember-0.6.3-gcc47.patch": {
                            "deletions": 0,
                            "lines": 26,
                            "insertions": 26
                        }
                    },
                    "total": {
                        "deletions": 0,
                        "files": 1,
                        "insertions": 26,
                        "lines": 26
                    }
                },
                "name": "Tom Callaway",
                "rev": "aa2df80f3d8dd217c7cbfe2d3451190028f3fe14",
                "summary": "another missing patch? ridiculous.",
                "branch": "master",
                "repo": "ember",
                "message": "another missing patch? ridiculous.\n",
                "email": "spot@fedoraproject.org"
            }
        }
    }

if not 'FEDMSG_META_NO_NETWORK' in os.environ:
    TestGitReceiveLegacyModified.expected_long_form = full_patch


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
