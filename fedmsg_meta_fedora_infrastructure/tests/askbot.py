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

from .common import add_doc


class TestAskbotRetag(Base):
    """ Messages get emitted on this topic when a question on `Ask Fedora
    <https://ask.fedoraproject.org/questions>`_ changes tags.
    It includes information about what tags the package now has, what question
    the tags are for, and who did the changing.  The ``msg['msg']['tags']``
    field describes which tags changed while the
    ``msg['msg']['thread']['tagnames']`` field describes all tags on the
    thread in question.
    """

    expected_title = "askbot.tag.update"
    expected_subti = "ralph altered tags on askbot question 'some title'"
    expected_icon = "https://apps.fedoraproject.org/img/icons/ask_fedora.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'tags/asldkjfalskdjfalskj',
        'tags/asldkjf',
        'tags/asldkjfalskdjf',
        'threads/2',
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
    """ Messages get emitted on this topic anytime an `Ask Fedora
    <https://ask.fedoraproject.org/questions/>`_ question is updated.
    The snippet we have below is an example of a user posting a brand **new
    question** to `Ask Fedora <https://ask.fedoraproject.org/questions/>`_.
    """
    expected_title = "askbot.post.edit"
    expected_subti = "ralph asked the question 'I have a new question'"
    expected_icon = "https://apps.fedoraproject.org/img/icons/ask_fedora.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'tags/lolol',
        'threads/3',
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


class LegacyTestAskbotNewQuestionStg(Base):
    """ Messages get emitted on this topic anytime an `Ask Fedora
    <https://ask.stg.fedoraproject.org/questions/>`_ question is updated.
    The snippet we have below is an example of a user posting a brand **new
    question** to `Ask Fedora <https://ask.stg.fedoraproject.org/questions/>`_.
    """
    expected_title = "askbot.post.edit"
    expected_subti = "ralph asked the question 'I have a new question'"
    expected_icon = "https://apps.fedoraproject.org/img/icons/ask_fedora.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'tags/lolol',
        'threads/3',
    ])
    expected_link = "https://ask.stg.fedoraproject.org/question/3/"
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
        "topic": "org.fedoraproject.stg.askbot.post.edit",
        "username": "threebean",
        "timestamp": 1359946267.401213
    }


class TestAskbotNewAnswer(Base):
    """ Messages get emitted on this topic anytime a question is updated.
    An 'update' includes a new question, a new answer, and a modification
    to either.  *This* example is one of a **new answer** being posted to
    an `Ask Fedora <https://ask.fedoraproject.org/questions/>`_ question.
    """
    expected_title = "askbot.post.edit"
    expected_subti = ("ralph suggested an answer "
                      "to the question 'watwatwatwata'")
    expected_icon = "https://apps.fedoraproject.org/img/icons/ask_fedora.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
    expected_packages = set()
    expected_usernames = set(['ralph', 'lmacken'])
    expected_objects = set([
        'tags/cool',
        'threads/1',
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
    """ Sent when a user flags an `Ask Fedora
    <https://ask.fedoraproject.org/questions>`_ question or answer
    as "offensive".
    """
    expected_title = "askbot.post.flag_offensive.add"
    expected_subti = "ralph flagged a question as offensive!"
    expected_icon = "https://apps.fedoraproject.org/img/icons/ask_fedora.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'tags/town',
        'tags/ohok',
        'threads/2',
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
    """ Sent when a user *un*flags an `Ask Fedora
    <https://ask.fedoraproject.org/questions>`_ question or answer
    as "offensive".
    """
    expected_title = "askbot.post.flag_offensive.delete"
    expected_subti = "ralph unflagged an answer as offensive..."
    expected_icon = "https://apps.fedoraproject.org/img/icons/ask_fedora.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'tags/town',
        'tags/ohok',
        'threads/2',
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
    """ Messages get emitted on this topic anytime a question is updated.
    An 'update' includes a new question, a new answer, and a modification
    to either.  *This* example is one of a **question being modified** on
    `Ask Fedora <https://ask.fedoraproject.org/questions/>`_.
    """
    expected_title = "askbot.post.edit"
    expected_subti = "ralph updated the question 'alskdjflaksjdf lakjsf a'"
    expected_icon = "https://apps.fedoraproject.org/img/icons/ask_fedora.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_emails = {'ralph@fedoraproject.org': 'ralph'}
    expected_objects = set([
        'tags/town',
        'threads/2',
    ])
    expected_link = "https://ask.fedoraproject.org/question/2/"
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


class TestAskbotUpdatedAnswer(Base):
    """ Messages get emitted on this topic anytime a question is updated.
    An 'update' includes a new question, a new answer, and a modification
    to either.  *This* example is one of a **answer being modified** on
    `Ask Fedora <https://ask.fedoraproject.org/questions/>`_.
    """
    expected_title = "askbot.post.edit"
    expected_subti = ("ralph updated an answer "
                      "to the question 'I have a new question'")
    expected_icon = "https://apps.fedoraproject.org/img/icons/ask_fedora.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'tags/lolol',
        'threads/3',
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
    """ Messages with the ``askbot.post.delete`` topic get sent when either
    a question or an answer are deleted from `Ask Fedora
    <https://ask.fedoraproject.org/questions>`_.  The example here is one
    of an **answer** being deleted.
    """
    expected_title = "askbot.post.delete"
    expected_subti = "ralph deleted an answer on 'test 3 is a charm'"
    expected_icon = "https://apps.fedoraproject.org/img/icons/ask_fedora.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'threads/7',
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
    """ Messages with the ``askbot.post.delete`` topic get sent when either
    a question or an answer are deleted from `Ask Fedora
    <https://ask.fedoraproject.org/questions>`_.  The example here is one
    of an **question** being deleted.
    """
    expected_title = "askbot.post.delete"
    expected_subti = "ralph deleted the question 'test 3 is a charm'"
    expected_icon = "https://apps.fedoraproject.org/img/icons/ask_fedora.png"
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "9c9f7784935381befc302fe3c814f9136e7a33953d0318761669b8643f4df55c?s=64&d=retro")
    expected_packages = set()
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'threads/7',
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


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
