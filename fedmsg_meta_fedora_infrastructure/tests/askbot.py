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
""" Tests for askbot messages """

import unittest

from fedmsg.tests.test_meta import Base


class TestAskbotRetag(Base):
    expected_title = "askbot.tag.update (unsigned)"
    expected_subti = "ralph altered tags on askbot question 'some title'"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'askbot/tags/asldkjfalskdjfalskj',
        'askbot/tags/asldkjf',
        'askbot/tags/asldkjfalskdjf',
        'askbot/threads/2',
    ])
    expected_link = "https://ask.fedoraproject.org/question/2/"
    msg = {
        "i": 1,
        "msg": {
            "topmost_post_id": 2,
            "timestamp": 1359945296.0,
            "agent": "ralph",
            "thread": {
                "tagnames": [
                    "town",
                    "ohok",
                    "asldkjfalskdjfalskj",
                    "asldkjf"
                ],
                "pk": 2,
                "title": "some title"
            },
            "tags": [
                "asldkjfalskdjfalskj",
                "asldkjf",
                "asldkjfalskdjf"
            ]
        },
        "topic": "org.fedoraproject.dev.askbot.tag.update",
        "username": "threebean",
        "timestamp": 1359945296.629136
    }


class TestAskbotNewQuestion(Base):
    expected_title = "askbot.post.edit (unsigned)"
    expected_subti = "ralph asked the question 'I have a new question'"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'askbot/tags/lolol',
        'askbot/threads/3',
    ])
    expected_link = "https://ask.fedoraproject.org/question/3/"
    msg = {
        "i": 2,
        "msg": {
            "thread": {
                "tagnames": [
                    "lolol"
                ],
                "pk": 3,
                "title": "I have a new question"
            },
            "topmost_post_id": 3,
            "created": True,
            "timestamp": 1359946267.0,
            "agent": "ralph",
            "newly_mentioned_users": [],
            "diff": "lololol\n\nthis is my entry, I hope that you "
            "like it so very much.\n ...",
            "post": {
                "vote_up_count": 0,
                "text": "lololol\r\n\r\nthis is my entry, I hope that "
                "you like it so very much.",
                "summary": "lololol\n\nthis is my entry, I hope that "
                "you like it so very much.\n ...",
                "comment_count": 0,
                "vote_down_count": 0,
                "pk": 4,
                "post_type": "question"
            }
        },
        "topic": "org.fedoraproject.dev.askbot.post.edit",
        "username": "threebean",
        "timestamp": 1359946267.401213
    }


class TestAskbotNewAnswer(Base):
    expected_title = "askbot.post.edit (unsigned)"
    expected_subti = "ralph suggested an answer " + \
        "to the question 'watwatwatwata'"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_packages = set()
    expected_usernames = set(['ralph', 'lmacken'])
    expected_objects = set([
        'askbot/tags/cool',
        'askbot/threads/1',
    ])
    expected_link = "https://ask.fedoraproject.org/question/1/"
    msg = {
        "i": 1,
        "msg": {
            "thread": {
                "tagnames": [
                    "cool"
                ],
                "pk": 1,
                "title": "watwatwatwata"
            },
            "topmost_post_id": 1,
            "created": True,
            "timestamp": 1359946481.0,
            "agent": "ralph",
            "newly_mentioned_users": ['lmacken'],
            "diff": "I know the answer\n\nlololololol I do!     "
            "I swear.\n ...",
            "post": {
                "vote_up_count": 0,
                "text": "I know the answer\r\n\r\nlololololol I do!     "
                "I swear.",
                "summary": "I know the answer\n\nlololololol I do!     "
                "I swear.\n ...",
                "comment_count": 0,
                "vote_down_count": 0,
                "pk": 5,
                "post_type": "answer"
            }
        },
        "topic": "org.fedoraproject.dev.askbot.post.edit",
        "username": "threebean",
        "timestamp": 1359946482.179817
    }


class TestAskbotFlagOffensiveAdd(Base):
    expected_title = "askbot.post.flag_offensive.add (unsigned)"
    expected_subti = "ralph flagged a question as offensive!"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'askbot/tags/town',
        'askbot/tags/ohok',
        'askbot/threads/2',
    ])
    expected_link = "https://ask.fedoraproject.org/question/2/"
    msg = {
        "i": 1,
        "msg": {
            "instance": {
                "vote_up_count": 1,
                "text": "I think I know... totally.    "
                "asldkj for sure.",
                "summary": "I think I know... totally.    "
                "asldkj for sure.\n ...",
                "comment_count": 0,
                "vote_down_count": 0,
                "pk": 3,
                "post_type": "question"
            },
            "agent": "ralph",
            "topmost_post_id": 2,
            "thread": {
                "tagnames": [
                    "town",
                    "ohok",
                ],
                "pk": 2,
                "title": "alskdjflaksjdf lakjsf a"
            }
        },
        "topic": "org.fedoraproject.dev.askbot.post.flag_offensive.add",
        "username": "threebean",
        "timestamp": 1359947156.346592
    }


class TestAskbotFlagOffensiveRemove(Base):
    expected_title = "askbot.post.flag_offensive.delete (unsigned)"
    expected_subti = "ralph unflagged an answer as offensive..."
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'askbot/tags/town',
        'askbot/tags/ohok',
        'askbot/threads/2',
    ])
    expected_link = "https://ask.fedoraproject.org/question/2/"
    msg = {
        "i": 1,
        "msg": {
            "instance": {
                "vote_up_count": 1,
                "text": "I think I know... totally.    "
                "asldkj for sure.",
                "summary": "I think I know... totally.    "
                "asldkj for sure.\n ...",
                "comment_count": 0,
                "vote_down_count": 0,
                "pk": 3,
                "post_type": "answer"
            },
            "agent": "ralph",
            "topmost_post_id": 2,
            "thread": {
                "tagnames": [
                    "town",
                    "ohok",
                ],
                "pk": 2,
                "title": "alskdjflaksjdf lakjsf a"
            }
        },
        "topic": "org.fedoraproject.dev.askbot.post.flag_offensive.delete",
        "username": "threebean",
        "timestamp": 1359947128.523792
    }


class TestAskbotUpdatedQuestion(Base):
    expected_title = "askbot.post.edit (unsigned)"
    expected_subti = "ralph updated the question 'alskdjflaksjdf lakjsf a'"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'askbot/tags/town',
        'askbot/threads/3',
    ])
    expected_link = "https://ask.fedoraproject.org/question/" + \
        "2/?answer=2#post-id-2"
    msg = {
        "i": 2,
        "msg": {
            "thread": {
                "tagnames": [
                    "town"
                ],
                "pk": 2,
                "title": "alskdjflaksjdf lakjsf a"
            },
            "created": False,
            "timestamp": 1359947640.0,
            "topmost_post_id": 2,
            "agent": "ralph",
            "newly_mentioned_users": [],
            "diff": "<p>alskdfj... the diff is actually here",
            "post": {
                "vote_up_count": 0,
                "text": "alskdfjalskdjf alkjasdalskdjf ...",
                "summary": "alskdfjalskdjf alkjasdalskdjf ...",
                "comment_count": 0,
                "vote_down_count": 0,
                "pk": 2,
                "post_type": "question"
            }
        },
        "topic": "org.fedoraproject.dev.askbot.post.edit",
        "username": "threebean",
        "timestamp": 1359947640.986208
    }


class TestAskbotUpdatedQuestion(Base):
    expected_title = "askbot.post.edit (unsigned)"
    expected_subti = "ralph updated an answer " + \
        "to the question 'I have a new question'"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'askbot/tags/lolol',
        'askbot/threads/3',
    ])
    expected_link = "https://ask.fedoraproject.org/question/3/"
    msg = {
        "i": 1,
        "msg": {
            "thread": {
                "tagnames": [
                    "lolol"
                ],
                "pk": 3,
                "title": "I have a new question"
            },
            "topmost_post_id": 3,
            "created": False,
            "timestamp": 1359947977.0,
            "agent": "ralph",
            "newly_mentioned_users": [],
            "diff": "<p>this is my test <del>answer</del><ins>answer."
            "ok?</ins></p>\n",
            "post": {
                "vote_up_count": 0,
                "text": "this is my test answer.    ok?",
                "summary": "this is my test answer.    ok?\n ...",
                "comment_count": 0,
                "vote_down_count": 0,
                "pk": 6,
                "post_type": "answer"
            }
        },
        "topic": "org.fedoraproject.dev.askbot.post.edit",
        "username": "threebean",
        "timestamp": 1359947978.125892
    }


class TestAskbotAnswerDeleted(Base):
    expected_title = "askbot.post.delete (unsigned)"
    expected_subti = "ralph deleted an answer on 'test 3 is a charm'"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'askbot/threads/7',
    ])
    expected_link = "https://ask.fedoraproject.org/question/10/"
    msg = {
        "i": 1,
        "msg": {
            "topmost_post_id": 10,
            "instance": {
                "vote_up_count": 0,
                "text": "oh, ok.. coolio",
                "summary": "oh, ok.. coolio\n ...",
                "comment_count": 0,
                "vote_down_count": 0,
                "pk": 12,
                "post_type": "answer"
            },
            "agent": "ralph",
            "thread": {
                "tagnames": [
                    ""
                ],
                "pk": 7,
                "title": "test 3 is a charm"
            }
        },
        "topic": "org.fedoraproject.dev.askbot.post.delete",
        "username": "threebean",
        "timestamp": 1359949257.459819
    }


class TestAskbotQuestionDeleted(Base):
    expected_title = "askbot.post.delete (unsigned)"
    expected_subti = "ralph deleted the question 'test 3 is a charm'"
    expected_secondary_icon = "http://www.gravatar.com/avatar/" + \
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F" + \
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png"
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'askbot/threads/7',
    ])
    expected_link = "https://ask.fedoraproject.org/question/10/"
    msg = {
        "i": 1,
        "msg": {
            "topmost_post_id": 10,
            "instance": {
                "vote_up_count": 0,
                "text": "this is a test message.",
                "summary": "this is a test message.\n ...",
                "comment_count": 1,
                "vote_down_count": 0,
                "pk": 10,
                "post_type": "question"
            },
            "agent": "ralph",
            "thread": {
                "tagnames": [
                    ""
                ],
                "pk": 7,
                "title": "test 3 is a charm"
            }
        },
        "topic": "org.fedoraproject.dev.askbot.post.delete",
        "username": "threebean",
        "timestamp": 1359949397.539748
    }


if __name__ == '__main__':
    unittest.main()
