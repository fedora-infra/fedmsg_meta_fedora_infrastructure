# This file is part of fedmsg.
# Copyright (C) 2014 Red Hat, Inc.
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
""" Tests for github2fedmsg messages """

import unittest
import datetime

from fedmsg_meta_fedora_infrastructure.tests.base import Base

from common import add_doc


class TestGithubWebhook(Base):
    """ There exists `a service
    <https://apps.fedoraproject.org/github2fedmsg>`_ to link the select github
    repos of fedora contributors with the fedmsg bus.

    Messages of *this* type are published whenever someone **enables a new
    repository for fedmsg broadcast**.  It, unfortunately, contains very little
    information.
    """

    expected_title = "github.webhook"
    expected_subti = 'A new github repository has been added to fedmsg'
    expected_icon = "https://apps.fedoraproject.org/img/icons/github.png"
    expected_secondary_icon = expected_icon
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set([])

    msg = {
        "username": "root",
        "i": 1,
        "timestamp": 1395167225,
        "msg_id": "2014-185bc51e-ad8e-4906-a623-445f3dbe794a",
        "topic": "org.fedoraproject.prod.github.webhook",
        "msg": {
            "hook_id": 1966604,
            "zen": "Responsive is better than fast.",
            "fas_usernames": {}
        }
    }


class TestGithubPush(Base):
    """ There exists `a service
    <https://apps.fedoraproject.org/github2fedmsg>`_ to link the select github
    repos of fedora contributors with the fedmsg bus.

    Messages of *this* type are published whenever someone **pushes to a
    so-enabled github repository**.
    """

    expected_title = "github.push"
    expected_subti = 'ralph pushed 1 commit(s) to fedora-infra/github2fedmsg'
    expected_link = "https://github.com/fedora-infra/github2fedmsg/" + \
        "compare/60a6d3eb508c...404a417299f8"
    expected_icon = "https://apps.fedoraproject.org/img/icons/github.png"
    expected_secondary_icon = (
        "http://www.gravatar.com/avatar/"
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F"
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png")
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'git/fedora-infra/github2fedmsg/README.rst'
    ])

    msg = {
        "username": "apache",
        "i": 1,
        "timestamp": 1395164717,
        "msg_id": "2014-f00946a5-2e26-4638-aa9f-ab3dffd9b4c2",
        "topic": "org.fedoraproject.prod.github.push",
        "msg": {
            "fas_usernames": {
                "ralphbean": "ralph",
            },
            "forced": False,
            "compare": "https://github.com/fedora-infra/github2fedmsg/" +
            "compare/60a6d3eb508c...404a417299f8",
            "after": "404a417299f85eadb72457e94c08ac8ba39d53e8",
            "repository": {
                "fork": False,
                "has_wiki": False,
                "description": "A pubsubhubbub application that rebroadcasts "
                "github events on the fedmsg bus",
                "language": "Python",
                "has_downloads": True,
                "url": "https://github.com/fedora-infra/github2fedmsg",
                "master_branch": "develop",
                "created_at": 1395065396,
                "private": False,
                "name": "github2fedmsg",
                "pushed_at": 1395164716,
                "open_issues": 0,
                "watchers": 2,
                "has_issues": True,
                "owner": {
                    "email": None,
                    "name": "fedora-infra"
                },
                "organization": "fedora-infra",
                "forks": 0,
                "stargazers": 2,
                "id": 17830164,
                "size": 804
            },
            "created": False,
            "deleted": False,
            "commits": [
                {
                    "committer": {
                        "username": "ralphbean",
                        "email": "rbean@redhat.com",
                        "name": "Ralph Bean"
                    },
                    "added": [],
                    "author": {
                        "username": "ralphbean",
                        "email": "rbean@redhat.com",
                        "name": "Ralph Bean"
                    },
                    "distinct": True,
                    "timestamp": "2014-03-18T13:45:12-04:00",
                    "modified": [
                        "README.rst"
                    ],
                    "url": "https://github.com/fedora-infra/github2fedmsg/"
                    "commit/404a417299f85eadb72457e94c08ac8ba39d53e8",
                    "message": "Updates to the README.",
                    "removed": [],
                    "id": "404a417299f85eadb72457e94c08ac8ba39d53e8"
                }
            ],
            "pusher": {
                "email": "ralph.bean@gmail.com",
                "name": "ralphbean"
            },
            "head_commit": {
                "committer": {
                    "username": "ralphbean",
                    "email": "rbean@redhat.com",
                    "name": "Ralph Bean"
                },
                "added": [],
                "author": {
                    "username": "ralphbean",
                    "email": "rbean@redhat.com",
                    "name": "Ralph Bean"
                },
                "distinct": True,
                "timestamp": "2014-03-18T13:45:12-04:00",
                "modified": [
                    "README.rst"
                ],
                "url": "https://github.com/fedora-infra/github2fedmsg/"
                "commit/404a417299f85eadb72457e94c08ac8ba39d53e8",
                "message": "Updates to the README.",
                "removed": [],
                "id": "404a417299f85eadb72457e94c08ac8ba39d53e8"
            },
            "ref": "refs/heads/develop",
            "before": "60a6d3eb508ca45a0740de90628abf5b59c0e698"
        }
    }


class TestGithubIssue(Base):
    """ There exists `a service
    <https://apps.fedoraproject.org/github2fedmsg>`_ to link the select github
    repos of fedora contributors with the fedmsg bus.

    Messages of *this* type are published whenever someone **changes an issue
    on an enabled github repository**.  This includes closing, opening,
    re-opening issues.

    Here's an example of re-opening:
    """

    expected_title = "github.issue.reopened"
    expected_subti = 'ralph reopened issue #3 on fedora-infra/github2fedmsg'
    expected_link = "https://github.com/fedora-infra/github2fedmsg/issues/3"
    expected_icon = "https://apps.fedoraproject.org/img/icons/github.png"
    expected_secondary_icon = (
        "http://www.gravatar.com/avatar/"
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F"
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png")
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'issue/fedora-infra/github2fedmsg/3',
    ])
    msg = {
        "username": "root",
        "i": 2,
        "timestamp": 1395166113,
        "msg_id": "2014-cbf1c4bc-6e87-47d2-8421-3f415b247781",
        "topic": "org.fedoraproject.dev.github.issue.reopened",
        "msg": {
            "action": "reopened",
            "fas_usernames": {
                "ralphbean": "ralph"
            },
            "issue": {
                "body": "Testing stuff.",
                "number": 3,
                "title": "Testing",
                "url": "https://api.github.com/repos/fedora-infra/"
                "github2fedmsg/issues/3",
                "created_at": "2014-03-17T20:48:13Z",
                "labels": [],
                "updated_at": "2014-03-18T18:08:32Z",
                "comments": 4,
                "html_url": "https://github.com/fedora-infra/"
                "github2fedmsg/issues/3",
                "assignee": None,
                "state": "open",
                "user": {
                    "url": "https://api.github.com/users/ralphbean",
                    "html_url": "https://github.com/ralphbean",
                    "gravatar_id": "ba940b433c2695635d32d2c4aec00540",
                    "site_admin": False,
                    "login": "ralphbean",
                    "type": "User",
                    "id": 331338,
                },
                "milestone": None,
                "closed_at": None,
                "pull_request": {
                    "html_url": None,
                },
                "id": 29597314
            },
            "sender": {
                "url": "https://api.github.com/users/ralphbean",
                "html_url": "https://github.com/ralphbean",
                "gravatar_id": "ba940b433c2695635d32d2c4aec00540",
                "site_admin": False,
                "login": "ralphbean",
                "type": "User",
                "id": 331338,
            },
            "repository": {
                "has_wiki": False,
                "updated_at": "2014-03-18T17:45:15Z",
                "owner": {
                    "url": "https://api.github.com/users/fedora-infra",
                    "html_url": "https://github.com/fedora-infra",
                    "gravatar_id": "ebdef1eaaa4b1c1cb01f5570efbb3cc4",
                    "site_admin": False,
                    "login": "fedora-infra",
                    "type": "Organization",
                    "id": 3316637,
                },
                "full_name": "fedora-infra/github2fedmsg",
                "id": 17830164,
                "size": 804,
                "has_downloads": True,
                "description": "A pubsubhubbub application that rebroadcasts "
                "github events on the fedmsg bus",
                "watchers_count": 2,
                "stargazers_count": 2,
                "homepage": None,
                "fork": False,
                "html_url": "https://github.com/fedora-infra/github2fedmsg",
                "open_issues": 1,
                "private": False,
                "forks_count": 0,
                "has_issues": True,
                "master_branch": "develop",
                "forks": 0,
                "open_issues_count": 1,
                "watchers": 2,
                "name": "github2fedmsg",
                "language": "Python",
                "url": "https://api.github.com/repos/fedora-infra/"
                "github2fedmsg",
                "created_at": "2014-03-17T14:09:56Z",
                "pushed_at": "2014-03-18T17:45:16Z",
                "default_branch": "develop",
            }
        }
    }


class TestGithubIssueComment(Base):
    """ There exists `a service
    <https://apps.fedoraproject.org/github2fedmsg>`_ to link the select github
    repos of fedora contributors with the fedmsg bus.

    Messages of *this* type are published whenever someone **comment on an
    issue on an enabled github repository**.
    """

    expected_title = "github.issue.comment"
    expected_subti = 'ralph commented on issue #3 on ' + \
        'fedora-infra/github2fedmsg'
    expected_link = "https://github.com/fedora-infra/github2fedmsg/" + \
        "issues/3#issuecomment-37971221"
    expected_icon = "https://apps.fedoraproject.org/img/icons/github.png"
    expected_secondary_icon = (
        "http://www.gravatar.com/avatar/"
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F"
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png")
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'issue/fedora-infra/github2fedmsg/3',
    ])
    msg = {
        "username": "root",
        "i": 1,
        "timestamp": 1395167817,
        "msg_id": "2014-573a1443-bb14-4891-bf6a-120827d8f24c",
        "topic": "org.fedoraproject.dev.github.issue.comment",
        "msg": {
            "comment": {
                "body": "This issue is super great!",
                "url": "https://api.github.com/repos/fedora-infra/"
                "github2fedmsg/issues/comments/37971221",
                "created_at": "2014-03-18T18:36:56Z",
                "html_url": "https://github.com/fedora-infra/"
                "github2fedmsg/issues/3#issuecomment-37971221",
                "updated_at": "2014-03-18T18:36:56Z",
                "user": {
                    "url": "https://api.github.com/users/ralphbean",
                    "site_admin": False,
                    "html_url": "https://github.com/ralphbean",
                    "gravatar_id": "ba940b433c2695635d32d2c4aec00540",
                    "login": "ralphbean",
                    "type": "User",
                    "id": 331338
                },
                "id": 37971221
            },
            "sender": {
                "url": "https://api.github.com/users/ralphbean",
                "site_admin": False,
                "html_url": "https://github.com/ralphbean",
                "gravatar_id": "ba940b433c2695635d32d2c4aec00540",
                "login": "ralphbean",
                "type": "User",
                "id": 331338
            },
            "repository": {
                "has_wiki": False,
                "forks_count": 0,
                "updated_at": "2014-03-18T18:36:30Z",
                "private": False,
                "full_name": "fedora-infra/github2fedmsg",
                "owner": {
                    "url": "https://api.github.com/users/fedora-infra",
                    "site_admin": False,
                    "html_url": "https://github.com/fedora-infra",
                    "gravatar_id": "ebdef1eaaa4b1c1cb01f5570efbb3cc4",
                    "login": "fedora-infra",
                    "type": "Organization",
                    "id": 3316637
                },
                "id": 17830164,
                "size": 804,
                "watchers_count": 2,
                "stargazers_count": 2,
                "homepage": None,
                "fork": False,
                "description": "A pubsubhubbub application that rebroadcasts "
                "github events on the fedmsg bus",
                "has_downloads": True,
                "default_branch": "develop",
                "html_url": "https://github.com/fedora-infra/github2fedmsg",
                "has_issues": True,
                "master_branch": "develop",
                "forks": 0,
                "open_issues_count": 1,
                "watchers": 2,
                "name": "github2fedmsg",
                "language": "Python",
                "url": "https://api.github.com/repos/fedora-infra/"
                "github2fedmsg",
                "created_at": "2014-03-17T14:09:56Z",
                "pushed_at": "2014-03-18T18:36:30Z",
                "open_issues": 1
            },
            "fas_usernames": {
                "ralphbean": "ralph"
            },
            "action": "created",
            "issue": {
                "body": "Testing stuff.",
                "number": 3,
                "title": "Testing",
                "url": "https://api.github.com/repos/fedora-infra/"
                "github2fedmsg/issues/3",
                "created_at": "2014-03-17T20:48:13Z",
                "labels": [],
                "updated_at": "2014-03-18T18:36:56Z",
                "comments": 6,
                "html_url": "https://github.com/fedora-infra/"
                "github2fedmsg/issues/3",
                "assignee": None,
                "state": "open",
                "user": {
                    "url": "https://api.github.com/users/ralphbean",
                    "site_admin": False,
                    "html_url": "https://github.com/ralphbean",
                    "gravatar_id": "ba940b433c2695635d32d2c4aec00540",
                    "login": "ralphbean",
                    "type": "User",
                    "id": 331338
                },
                "milestone": None,
                "closed_at": None,
                "pull_request": {
                    "html_url": None
                },
                "id": 29597314
            }
        }
    }


class TestGithubCreate(Base):
    """ There exists `a service
    <https://apps.fedoraproject.org/github2fedmsg>`_ to link the select github
    repos of fedora contributors with the fedmsg bus.

    Messages of *this* type are published whenever someone **creates a new tag
    or branch**.
    """

    expected_title = "github.create"
    expected_subti = 'ralph created a new branch "feature/testing-stuff" ' + \
        'at fedora-infra/github2fedmsg'
    expected_link = "https://github.com/fedora-infra/github2fedmsg"
    expected_icon = "https://apps.fedoraproject.org/img/icons/github.png"
    expected_secondary_icon = (
        "http://www.gravatar.com/avatar/"
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F"
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png")
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'create/fedora-infra/github2fedmsg/branch/feature/testing-stuff',
    ])
    msg = {
        "username": "root",
        "i": 1,
        "timestamp": 1395168693,
        "msg_id": "2014-eed312f7-7bb2-471c-acb6-afaaf8f097ba",
        "topic": "org.fedoraproject.dev.github.create",
        "msg": {
            "sender": {
                "url": "https://api.github.com/users/ralphbean",
                "site_admin": False,
                "html_url": "https://github.com/ralphbean",
                "gravatar_id": "ba940b433c2695635d32d2c4aec00540",
                "login": "ralphbean",
                "type": "User",
                "id": 331338
            },
            "repository": {
                "has_wiki": False,
                "forks_count": 0,
                "updated_at": "2014-03-18T18:36:30Z",
                "private": False,
                "full_name": "fedora-infra/github2fedmsg",
                "owner": {
                    "url": "https://api.github.com/users/fedora-infra",
                    "site_admin": False,
                    "html_url": "https://github.com/fedora-infra",
                    "gravatar_id": "ebdef1eaaa4b1c1cb01f5570efbb3cc4",
                    "login": "fedora-infra",
                    "type": "Organization",
                    "id": 3316637
                },
                "id": 17830164,
                "size": 804,
                "watchers_count": 2,
                "stargazers_count": 2,
                "homepage": None,
                "fork": False,
                "description": "A pubsubhubbub application that rebroadcasts "
                "github events on the fedmsg bus",
                "has_downloads": True,
                "default_branch": "develop",
                "html_url": "https://github.com/fedora-infra/github2fedmsg",
                "has_issues": True,
                "master_branch": "develop",
                "forks": 0,
                "open_issues_count": 1,
                "watchers": 2,
                "name": "github2fedmsg",
                "language": "Python",
                "url": "https://api.github.com/repos/fedora-infra/"
                "github2fedmsg",
                "created_at": "2014-03-17T14:09:56Z",
                "pushed_at": "2014-03-18T18:51:32Z",
                "open_issues": 1
            },
            "ref": "feature/testing-stuff",
            "fas_usernames": {
                "ralphbean": "ralph"
            },
            "ref_type": "branch",
            "pusher_type": "user",
            "master_branch": "develop",
            "description": "A pubsubhubbub application that rebroadcasts "
            "github events on the fedmsg bus"
        }
    }


class TestGithubPullRequestClosed(Base):
    """ There exists `a service
    <https://apps.fedoraproject.org/github2fedmsg>`_ to link the select github
    repos of fedora contributors with the fedmsg bus.

    Messages of *this* type are published whenever someone **closes an existing
    pull request**.  There are similar messages for opening one.
    """

    expected_title = "github.pull_request.closed"
    expected_subti = 'ralph closed pull request #6 ' + \
        'on fedora-infra/github2fedmsg'
    expected_link = "https://github.com/fedora-infra/github2fedmsg/pull/6"
    expected_icon = "https://apps.fedoraproject.org/img/icons/github.png"
    expected_secondary_icon = (
        "http://www.gravatar.com/avatar/"
        "2f933f4364baaabd2d3ab8f0664faef2?s=64&d=http%3A%2F%2F"
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png")
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set([
        'pull_request/fedora-infra/github2fedmsg/6',
    ])
    msg = {
        "username": "root",
        "i": 1,
        "timestamp": 1395169657,
        "msg_id": "2014-0ebb72ca-bc13-493e-9b1b-687d94ff11e3",
        "topic": "org.fedoraproject.dev.github.pull_request.closed",
        "msg": {
            "sender": {
                "url": "https://api.github.com/users/ralphbean",
                "site_admin": False,
                "html_url": "https://github.com/ralphbean",
                "gravatar_id": "ba940b433c2695635d32d2c4aec00540",
                "login": "ralphbean",
                "type": "User",
                "id": 331338
            },
            "repository": {
                "has_wiki": False,
                "forks_count": 0,
                "updated_at": "2014-03-18T19:07:35Z",
                "private": False,
                "full_name": "fedora-infra/github2fedmsg",
                "owner": {
                    "url": "https://api.github.com/users/fedora-infra",
                    "site_admin": False,
                    "html_url": "https://github.com/fedora-infra",
                    "gravatar_id": "ebdef1eaaa4b1c1cb01f5570efbb3cc4",
                    "login": "fedora-infra",
                    "type": "Organization",
                    "id": 3316637
                },
                "id": 17830164,
                "size": 804,
                "watchers_count": 2,
                "stargazers_count": 2,
                "homepage": None,
                "fork": False,
                "description": "A pubsubhubbub application that rebroadcasts "
                "github events on the fedmsg bus",
                "has_downloads": True,
                "default_branch": "develop",
                "html_url": "https://github.com/fedora-infra/github2fedmsg",
                "has_issues": True,
                "master_branch": "develop",
                "forks": 0,
                "open_issues_count": 1,
                "watchers": 2,
                "name": "github2fedmsg",
                "language": "Python",
                "url": "https://api.github.com/repos/fedora-infra/"
                "github2fedmsg",
                "created_at": "2014-03-17T14:09:56Z",
                "pushed_at": "2014-03-18T19:07:22Z",
                "open_issues": 1
            },
            "number": 6,
            "fas_usernames": {
                "ralphbean": "ralph"
            },
            "pull_request": {
                "body": "This is just a test.",
                "merge_commit_sha": "8b5898c780f41baf41de624fd47988b29ac42ecb",
                "updated_at": "2014-03-18T19:07:35Z",
                "assignee": None,
                "mergeable": None,
                "closed_at": "2014-03-18T19:07:35Z",
                "additions": 2,
                "id": 13701851,
                "title": "No more retask.",
                "comments": 0,
                "merged_at": None,
                "state": "closed",
                "changed_files": 1,
                "merged": False,
                "deletions": 2,
                "head": {
                    "repo": {
                        "has_wiki": False,
                        "forks_count": 0,
                        "updated_at": "2014-03-18T19:07:35Z",
                        "private": False,
                        "full_name": "fedora-infra/github2fedmsg",
                        "owner": {
                            "url": "https://api.github.com/users/fedora-infra",
                            "site_admin": False,
                            "html_url": "https://github.com/fedora-infra",
                            "gravatar_id": "ebdef1eaaa4b1c1cb01f5570efbb3cc4",
                            "login": "fedora-infra",
                            "type": "Organization",
                            "id": 3316637
                        },
                        "id": 17830164,
                        "size": 804,
                        "watchers_count": 2,
                        "stargazers_count": 2,
                        "homepage": None,
                        "fork": False,
                        "description": "A pubsubhubbub application that "
                        "rebroadcasts github events on the fedmsg bus",
                        "has_downloads": True,
                        "default_branch": "develop",
                        "html_url": "https://github.com/fedora-infra/"
                        "github2fedmsg",
                        "has_issues": True,
                        "master_branch": "develop",
                        "forks": 0,
                        "open_issues_count": 1,
                        "watchers": 2,
                        "name": "github2fedmsg",
                        "language": "Python",
                        "url": "https://api.github.com/repos/fedora-infra/"
                        "github2fedmsg",
                        "created_at": "2014-03-17T14:09:56Z",
                        "pushed_at": "2014-03-18T19:07:22Z",
                        "open_issues": 1
                    },
                    "sha": "54c80f816ed992a3a43c823e11cfce0a69f64d6d",
                    "ref": "feature/no-more-retask",
                    "user": {
                        "url": "https://api.github.com/users/fedora-infra",
                        "site_admin": False,
                        "html_url": "https://github.com/fedora-infra",
                        "gravatar_id": "ebdef1eaaa4b1c1cb01f5570efbb3cc4",
                        "login": "fedora-infra",
                        "type": "Organization",
                        "id": 3316637
                    },
                    "label": "fedora-infra:feature/no-more-retask"
                },
                "commits": 1,
                "html_url": "https://github.com/fedora-infra/"
                "github2fedmsg/pull/6",
                "number": 6,
                "base": {
                    "repo": {
                        "has_wiki": False,
                        "forks_count": 0,
                        "updated_at": "2014-03-18T19:07:35Z",
                        "private": False,
                        "full_name": "fedora-infra/github2fedmsg",
                        "owner": {
                            "url": "https://api.github.com/users/fedora-infra",
                            "site_admin": False,
                            "html_url": "https://github.com/fedora-infra",
                            "gravatar_id": "ebdef1eaaa4b1c1cb01f5570efbb3cc4",
                            "login": "fedora-infra",
                            "type": "Organization",
                            "id": 3316637
                        },
                        "id": 17830164,
                        "size": 804,
                        "watchers_count": 2,
                        "stargazers_count": 2,
                        "homepage": None,
                        "fork": False,
                        "description": "A pubsubhubbub application that "
                        "rebroadcasts github events on the fedmsg bus",
                        "has_downloads": True,
                        "default_branch": "develop",
                        "html_url": "https://github.com/fedora-infra/"
                        "github2fedmsg",
                        "has_issues": True,
                        "master_branch": "develop",
                        "forks": 0,
                        "open_issues_count": 1,
                        "watchers": 2,
                        "name": "github2fedmsg",
                        "language": "Python",
                        "url": "https://api.github.com/repos/fedora-infra/"
                        "github2fedmsg",
                        "created_at": "2014-03-17T14:09:56Z",
                        "pushed_at": "2014-03-18T19:07:22Z",
                        "open_issues": 1
                    },
                    "sha": "e6ee4b6d136e3897c00b6904becc29bacfa139e8",
                    "ref": "develop",
                    "user": {
                        "url": "https://api.github.com/users/fedora-infra",
                        "site_admin": False,
                        "html_url": "https://github.com/fedora-infra",
                        "gravatar_id": "ebdef1eaaa4b1c1cb01f5570efbb3cc4",
                        "login": "fedora-infra",
                        "type": "Organization",
                        "id": 3316637
                    },
                    "label": "fedora-infra:develop"
                },
                "user": {
                    "url": "https://api.github.com/users/ralphbean",
                    "site_admin": False,
                    "html_url": "https://github.com/ralphbean",
                    "gravatar_id": "ba940b433c2695635d32d2c4aec00540",
                    "login": "ralphbean",
                    "type": "User",
                    "id": 331338
                },
                "milestone": None,
                "merged_by": None,
                "url": "https://api.github.com/repos/fedora-infra/"
                "github2fedmsg/pulls/6",
                "mergeable_state": "unknown",
                "created_at": "2014-03-18T19:05:44Z",
                "review_comments": 0
            },
            "action": "closed"
        }
    }


class TestGithubFork(Base):
    """ There exists `a service
    <https://apps.fedoraproject.org/github2fedmsg>`_ to link the select github
    repos of fedora contributors with the fedmsg bus.

    Messages of *this* type are published whenever someone **forks a repo**.
    """

    expected_title = "github.fork"
    expected_subti = 'kushal124 forked fedora-infra/github2fedmsg'
    expected_link = "https://github.com/kushal124/github2fedmsg"
    expected_icon = "https://apps.fedoraproject.org/img/icons/github.png"
    expected_secondary_icon = (
        "http://www.gravatar.com/avatar/"
        "afc63e66e6cf1a3b1de1ed0be4ab503f?s=64&d=http%3A%2F%2F"
        "fedoraproject.org%2Fstatic%2Fimages%2Ffedora_infinity_64x64.png")
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set([
        'forks/fedora-infra/github2fedmsg/kushal124',
    ])
    msg = {
        "username": "root",
        "i": 2,
        "timestamp": 1395170248,
        "msg_id": "2014-8134c58d-fe22-4296-ada9-047e4156a29a",
        "topic": "org.fedoraproject.dev.github.fork",
        "msg": {
            "forkee": {
                "has_wiki": False,
                "forks_count": 0,
                "updated_at": "2014-03-18T19:17:12Z",
                "private": False,
                "full_name": "kushal124/github2fedmsg",
                "owner": {
                    "url": "https://api.github.com/users/kushal124",
                    "site_admin": False,
                    "html_url": "https://github.com/kushal124",
                    "gravatar_id": "c53aaf0b0f0633d6d82571b92985b6f3",
                    "login": "kushal124",
                    "type": "User",
                    "id": 871398
                },
                "id": 17878694,
                "size": 804,
                "watchers_count": 0,
                "stargazers_count": 0,
                "homepage": None,
                "public": True,
                "fork": True,
                "description": "A pubsubhubbub application that rebroadcasts "
                "github events on the fedmsg bus",
                "has_downloads": True,
                "default_branch": "develop",
                "html_url": "https://github.com/kushal124/github2fedmsg",
                "has_issues": False,
                "master_branch": "develop",
                "forks": 0,
                "open_issues_count": 0,
                "watchers": 0,
                "name": "github2fedmsg",
                "language": "Python",
                "url": "https://api.github.com/repos/kushal124/github2fedmsg",
                "created_at": "2014-03-18T19:17:28Z",
                "pushed_at": "2014-03-18T19:17:12Z",
                "open_issues": 0
            },
            "fas_usernames": {},
            "repository": {
                "has_wiki": False,
                "forks_count": 1,
                "updated_at": "2014-03-18T19:17:12Z",
                "private": False,
                "full_name": "fedora-infra/github2fedmsg",
                "owner": {
                    "url": "https://api.github.com/users/fedora-infra",
                    "site_admin": False,
                    "html_url": "https://github.com/fedora-infra",
                    "gravatar_id": "ebdef1eaaa4b1c1cb01f5570efbb3cc4",
                    "login": "fedora-infra",
                    "type": "Organization",
                    "id": 3316637
                },
                "id": 17830164,
                "size": 804,
                "watchers_count": 2,
                "stargazers_count": 2,
                "homepage": None,
                "fork": False,
                "description": "A pubsubhubbub application that rebroadcasts "
                "github events on the fedmsg bus",
                "has_downloads": True,
                "default_branch": "develop",
                "html_url": "https://github.com/fedora-infra/github2fedmsg",
                "has_issues": True,
                "master_branch": "develop",
                "forks": 1,
                "open_issues_count": 1,
                "watchers": 2,
                "name": "github2fedmsg",
                "language": "Python",
                "url": "https://api.github.com/repos/fedora-infra/"
                "github2fedmsg",
                "created_at": "2014-03-17T14:09:56Z",
                "pushed_at": "2014-03-18T19:17:12Z",
                "open_issues": 1
            },
            "sender": {
                "url": "https://api.github.com/users/kushal124",
                "site_admin": False,
                "html_url": "https://github.com/kushal124",
                "gravatar_id": "c53aaf0b0f0633d6d82571b92985b6f3",
                "login": "kushal124",
                "type": "User",
                "id": 871398
            }
        }
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
