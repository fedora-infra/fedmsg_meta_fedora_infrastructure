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
""" Tests for fedmsg.meta """

import unittest

from fedmsg.tests.test_meta import Base


class TestTaggerVoteAnonymous(Base):
    """ `Fedora Tagger <https://apps.fedoraproject.org/tagger>`_
    publishes messages like this one when a user votes on a tag.
    Users may upvote or downvote a tag and they may do so either
    anonymously or authenticated.  Here's an example of a
    anonymous upvote:
    """

    expected_title = "fedoratagger.tag.update (unsigned)"
    expected_subti = 'anonymous upvoted "unittest" on perl-Test-Fatal'
    expected_link = 'https://apps.fedoraproject.org/tagger/perl-Test-Fatal'
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


class TestTaggerCreate(Base):
    """ `Fedora Tagger <https://apps.fedoraproject.org/tagger>`_
    publishes messages like this one when a user **creates** a new tag.
    """
    expected_title = "fedoratagger.tag.create (unsigned)"
    expected_subti = 'ralph added tag "unittest" to perl-Test-Fatal'
    expected_link = 'https://apps.fedoraproject.org/tagger/perl-Test-Fatal'
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
