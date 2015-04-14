# This file is part of fedmsg.
# Copyright (C) 2013 Red Hat, Inc.
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
""" Tests for tagger messages """

import unittest

from fedmsg.tests.test_meta import Base

from .common import add_doc


class TestTaggerVoteAuthenticated(Base):
    """ `Fedora Tagger <https://apps.fedoraproject.org/tagger>`_
    publishes messages like this one when a user votes on a tag.
    Users may upvote or downvote a tag and they may do so either
    anonymously or authenticated.  Here's an example of an
    authenticated downvote:
    """

    expected_title = "fedoratagger.tag.update"
    expected_subti = 'ralph downvoted "stupid" on mattd'
    expected_link = 'https://apps.fedoraproject.org/tagger/mattd'
    expected_icon = 'https://apps.fedoraproject.org/img/icons/tagger.png'
    expected_secondary_icon = (
        'https://seccdn.libravatar.org/avatar/'
        '9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c'
        '?s=64&d=retro')
    expected_usernames = set(['ralph'])
    expected_packages = set(['mattd'])
    expected_objects = set(['packages/mattd', 'labels/stupid'])
    msg = {
        "i": 3,
        "msg": {
            "vote": {
                "tag": {
                    "votes": 1,
                    "like": 0,
                    "package": "mattd",
                    "tag": "stupid",
                    "dislike": 1,
                    "total": -1
                },
                "like": False,
                "user": {
                    "username": "ralph",
                    "votes": 4,
                    "rank": -1,
                    "anonymous": False
                }
            },
            "tag": {
                "votes": 1,
                "like": 0,
                "package": "mattd",
                "tag": "stupid",
                "dislike": 1,
                "total": -1
            },
            "user": {
                "username": "ralph",
                "votes": 4,
                "rank": -1,
                "anonymous": False
            }
        },
        "topic": "org.fedoraproject.dev.fedoratagger.tag.update",
        "username": "threebean",
        "timestamp": 1365444503.627384
    }


class TestTaggerRatingUpdateAnonymous(Base):
    """ `Fedora Tagger <https://apps.fedoraproject.org/tagger>`_
    doesn't just do tagging of packages, in new versions it also
    allows users to rate packages.  It publishes messages like this
    one when an anonymous user updates their rating of a package.
    """
    expected_title = "fedoratagger.rating.update"
    expected_subti = 'An anonymous user gave nethack a rating of 15'
    expected_link = 'https://apps.fedoraproject.org/tagger/nethack'
    expected_icon = 'https://apps.fedoraproject.org/img/icons/tagger.png'
    expected_usernames = set([])
    expected_packages = set(['nethack'])
    expected_objects = set(['packages/nethack'])

    msg = {
        "i": 1,
        "msg": {
            "rating": {
                "rating": 15,
                "user": {
                    "username": "anonymous",
                    "votes": 0,
                    "anonymous": True,
                    "rank": -1
                },
                "package": {
                    "rating": 15.0,
                    "tags": [
                        {
                            "votes": 1,
                            "like": 1,
                            "package": "nethack",
                            "tag": "awesome",
                            "dislike": 0,
                            "total": 1
                        }
                    ],
                    "name": "nethack",
                    "icon": "https://apps.fedoraproject.org/packages/images/"
                    "icons/package_128x128.png",
                    "summary": ""
                }
            }
        },
        "topic": "org.fedoraproject.dev.fedoratagger.rating.update",
        "username": "threebean",
        "timestamp": 1365514895.61764
    }


class TestTaggerCreate(Base):
    """ `Fedora Tagger <https://apps.fedoraproject.org/tagger>`_
    publishes messages like this one when a user **creates** a new tag.
    """
    expected_title = "fedoratagger.tag.create"
    expected_subti = 'ralph added tag "awesome" to mattd'
    expected_link = 'https://apps.fedoraproject.org/tagger/mattd'
    expected_icon = 'https://apps.fedoraproject.org/img/icons/tagger.png'
    expected_secondary_icon = (
        'https://seccdn.libravatar.org/avatar/'
        '9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c'
        '?s=64&d=retro')
    expected_usernames = set(['ralph'])
    expected_packages = set(['mattd'])
    expected_objects = set(['packages/mattd', 'labels/awesome'])
    msg = {
        "i": 2,
        "msg": {
            "vote": {
                "tag": {
                    "votes": 1,
                    "like": 1,
                    "package": "mattd",
                    "tag": "awesome",
                    "dislike": 0,
                    "total": 1
                },
                "like": True,
                "user": {
                    "username": "ralph",
                    "votes": 4,
                    "rank": -1,
                    "anonymous": False,
                }
            },
            "tag": {
                "votes": 1,
                "like": 1,
                "package": "mattd",
                "tag": "awesome",
                "dislike": 0,
                "total": 1
            },
            "user": {
                "username": "ralph",
                "votes": 4,
                "rank": -1,
                "anonymous": False,
            }
        },
        "topic": "org.fedoraproject.dev.fedoratagger.tag.create",
        "username": "threebean",
        "timestamp": 1365444411.924043
    }


class TestTaggerVoteAnonymousLegacy(Base):
    """ Support old legacy tagger messages. """
    expected_title = "fedoratagger.tag.update"
    expected_subti = 'anonymous upvoted "unittest" on perl-Test-Fatal'
    expected_link = 'https://apps.fedoraproject.org/tagger/perl-Test-Fatal'
    expected_icon = 'https://apps.fedoraproject.org/img/icons/tagger.png'
    expected_usernames = set([])
    expected_packages = set(['perl-Test-Fatal'])
    expected_objects = set(['packages/perl-Test-Fatal', 'labels/unittest'])

    msg = {
        "i": 1,
        "timestamp": 1345220838.2775879,
        "topic": "org.fedoraproject.stg.fedoratagger.tag.update",
        "msg": {
            "vote": {
                "tag": {
                    "votes": 2,
                    "like": 2,
                    "package": {
                        "perl-Test-Fatal": [
                            {
                                "dislike": 0,
                                "total": 1,
                                "tag": "perl",
                                "votes": 1,
                                "like": 1
                            },
                            {
                                "dislike": 0,
                                "total": 2,
                                "tag": "unittest",
                                "votes": 2,
                                "like": 2
                            }
                        ]
                    },
                    "label": {
                        "label": "unittest",
                        "tags": [
                            {
                                "dislike": 0,
                                "total": 2,
                                "tag": "unittest",
                                "votes": 2,
                                "like": 2
                            }
                        ]
                    },
                    "tag": "unittest",
                    "dislike": 0,
                    "total": 2
                },
                "like": True,
                "user": {
                    "username": "anonymous",
                    "all_votes": [],
                    "votes": 0,
                    "rank": -1
                }
            }
        }
    }


class TestTaggerCreateLegacy(Base):
    """ Support old TG2 version of tagger messages. """
    expected_title = "fedoratagger.tag.create"
    expected_subti = 'ralph added tag "unittest" to perl-Test-Fatal'
    expected_link = 'https://apps.fedoraproject.org/tagger/perl-Test-Fatal'
    expected_icon = 'https://apps.fedoraproject.org/img/icons/tagger.png'
    expected_secondary_icon = (
        'https://seccdn.libravatar.org/avatar/'
        '9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c'
        '?s=64&d=retro')
    expected_usernames = set(['ralph'])
    expected_packages = set(['perl-Test-Fatal'])
    expected_objects = set(['packages/perl-Test-Fatal', 'labels/unittest'])

    msg = {
        "i": 1,
        "timestamp": 1345220073.4948981,
        "topic": "org.fedoraproject.stg.fedoratagger.tag.create",
        "msg": {
            "vote": {
                "tag": {
                    "votes": 1,
                    "like": 1,
                    "package": {
                        "perl-Test-Fatal": [
                            {
                                "dislike": 0,
                                "total": 1,
                                "tag": "unittest",
                                "votes": 1,
                                "like": 1
                            },
                            {
                                "dislike": 0,
                                "total": 1,
                                "tag": "perl",
                                "votes": 1,
                                "like": 1
                            }
                        ]
                    },
                    "label": {
                        "label": "unittest",
                        "tags": [
                            {
                                "dislike": 0,
                                "total": 1,
                                "tag": "unittest",
                                "votes": 1,
                                "like": 1
                            }
                        ]
                    },
                    "tag": "unittest",
                    "dislike": 0,
                    "total": 1
                },
                "like": True,
                "user": {
                    "username": "ralph",
                    "votes": 28,
                    "rank": 1
                }
            }
        }
    }


class TestTaggerToggleUsageOn(Base):
    """ `Fedora Tagger <https://apps.fedoraproject.org/tagger>`_
    publishes messages like this one when a user **toggles** their usage status
    for a package.

    Here is an example of ralph declaring that he uses *passwd*.
    """
    expected_title = "fedoratagger.usage.toggle"
    expected_subti = 'ralph declared that they use passwd'
    expected_link = 'https://apps.fedoraproject.org/tagger/passwd'
    expected_icon = 'https://apps.fedoraproject.org/img/icons/tagger.png'
    expected_secondary_icon = (
        'https://seccdn.libravatar.org/avatar/'
        '9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c'
        '?s=64&d=retro')
    expected_usernames = set(['ralph'])
    expected_packages = set(['passwd'])
    expected_objects = set(['packages/passwd'])
    msg = {
        "username": "apache",
        "i": 1,
        "timestamp": 1391107443,
        "msg_id": "2014-8b4ffffc-4854-4da5-92b1-d266b4e7f52f",
        "topic": "org.fedoraproject.prod.fedoratagger.usage.toggle",
        "msg": {
            "usage": True,
            "user": {
                "username": "ralph",
                "votes": 859,
                "score": 949,
                "anonymous": False,
                "rank": 6
            },
            "package": {
                "rating": -1.0,
                "name": "passwd",
                "tags": [],
                "summary": "An utility for setting or changing passwords",
                "usage": 1,
                "icon": "https://apps.fedoraproject.org/packages/images/"
                "icons/package_128x128.png"
            }
        }
    }


class TestTaggerToggleUsageOff(Base):
    """ `Fedora Tagger <https://apps.fedoraproject.org/tagger>`_
    publishes messages like this one when a user **toggles** their usage status
    for a package.

    Here is an example of ralph declaring that he *no longer* uses *passwd*.
    """
    expected_title = "fedoratagger.usage.toggle"
    expected_subti = 'ralph declared that they no longer use passwd'
    expected_link = 'https://apps.fedoraproject.org/tagger/passwd'
    expected_icon = 'https://apps.fedoraproject.org/img/icons/tagger.png'
    expected_secondary_icon = (
        'https://seccdn.libravatar.org/avatar/'
        '9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c'
        '?s=64&d=retro')
    expected_usernames = set(['ralph'])
    expected_packages = set(['passwd'])
    expected_objects = set(['packages/passwd'])
    msg = {
        "username": "apache",
        "i": 1,
        "timestamp": 1391107443,
        "msg_id": "2014-8b4ffffc-4854-4da5-92b1-d266b4e7f52f",
        "topic": "org.fedoraproject.prod.fedoratagger.usage.toggle",
        "msg": {
            "usage": False,
            "user": {
                "username": "ralph",
                "votes": 859,
                "score": 949,
                "anonymous": False,
                "rank": 6
            },
            "package": {
                "rating": -1.0,
                "name": "passwd",
                "tags": [],
                "summary": "An utility for setting or changing passwords",
                "usage": 0,
                "icon": "https://apps.fedoraproject.org/packages/images/"
                "icons/package_128x128.png"
            }
        }
    }


class TestTaggerRankUpdate(Base):
    """ `Fedora Tagger <https://apps.fedoraproject.org/tagger>`_
    publishes messages like this one when a user's rank on the Fedora Tagger
    leaderboard changes.
    """

    expected_title = "fedoratagger.user.rank.update"
    expected_subti = "immanetize's rank changed to 59"
    expected_icon = 'https://apps.fedoraproject.org/img/icons/tagger.png'
    expected_secondary_icon = (
        'https://seccdn.libravatar.org/avatar/'
        '75aba49c572a4319af1792ba0dbe2a0d80de4dc1f602c43a360d9b0fc347ae0f'
        '?s=64&d=retro')
    expected_usernames = set(['immanetize'])
    expected_packages = set()
    expected_objects = set()
    msg = {
        "msg": {
            "user": {
                "anonymous": False,
                "votes": 176,
                "rank": 59,
                "username": "immanetize",
                "score": 275
            }
        },
        "source_name": "datanommer",
        "timestamp": 1396074860.0,
        "topic": "org.fedoraproject.prod.fedoratagger.user.rank.update",
        "source_version": "0.6.1",
        "i": 1,
        "msg_id": "2014-3893d29a-e9a1-43e0-90f0-333feebb766c"
    }


add_doc(locals())
