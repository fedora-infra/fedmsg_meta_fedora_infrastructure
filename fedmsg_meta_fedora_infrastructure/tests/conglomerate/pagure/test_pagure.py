# -*- coding: utf-8 -*-

import fedmsg.tests.test_meta

import arrow


class TestPagureConglomeratorByIssueAndPR(
    fedmsg.tests.test_meta.ConglomerateBase):
    expected = [
        {
            'categories': set(['pagure']),
            'end_time': 1458308863.0,
            'human_time': arrow.get(1458307676).humanize(),
            'icon': 'https://apps.fedoraproject.org/packages/images/icons/package_128x128.png',
            'link': 'https://pagure.io/pungi/issue/231',
            'packages': set([]),
            'secondary_icon': 'https://seccdn.libravatar.org/avatar/a89b57d99dcf12d40ec2b9fb05910b90293b13b0b87415208bedc897bc18a354?s=64&d=retro',
            'start_time': 1458306489.0,
            'subjective': 'ausil and lsedlar interacted with issue #231 of project "pungi" 2 times',
            'subtitle': 'ausil and lsedlar interacted with issue #231 of project "pungi" 2 times',
            'timestamp': 1458307676.0,
            'topics': set(['io.pagure.prod.pagure.issue.comment.added']),
            'usernames': set(['ausil', 'lsedlar'])
        }, {
            'categories': set(['pagure']),
            'end_time': 1458307490.0,
            'human_time': arrow.get(1458307490).humanize(),
            'icon': 'https://apps.fedoraproject.org/packages/images/icons/package_128x128.png',
            'link': 'https://pagure.io/fork/bonnegent/pagure',
            'packages': set([]),
            'secondary_icon': 'https://seccdn.libravatar.org/avatar/1216fff466c9dbb6ce85ac95bf8f45b9e19421af97de67945852722b899a34ee?s=64&d=retro',
            'start_time': 1458307490.0,
            'subjective': u'bonnegent forked pagure to fork/bonnegent/pagure',
            'subtitle': u'bonnegent forked pagure to fork/bonnegent/pagure',
            'timestamp': 1458307490.0,
            'topics': set(['io.pagure.prod.pagure.project.forked']),
            'usernames': set(['bonnegent'])
        }, {
            'categories': set(['pagure']),
            'end_time': 1458307394.0,
            'human_time': arrow.get(1458307394).humanize(),
            'icon': 'https://apps.fedoraproject.org/packages/images/icons/package_128x128.png',
            'link': 'https://pagure.io/pungi-fedora/pull-request/19',
            'packages': set([]),
            'secondary_icon': 'https://seccdn.libravatar.org/avatar/0929fed032bd0a481ef74c46023fefe443f3d1b72dbe3efd293b25ed4fc843fd?s=64&d=retro',
            'start_time': 1458307394.0,
            'subjective': 'sgallagh interacted with pull-request #19 of project "pungi-fedora" 2 times',
            'subtitle': 'sgallagh interacted with pull-request #19 of project "pungi-fedora" 2 times',
            'timestamp': 1458307394.0,
            'topics': set(['io.pagure.prod.pagure.pull-request.comment.added',
                           'io.pagure.prod.pagure.pull-request.new']),
            'usernames': set(['sgallagh'])
        }, {
            'categories': set(['pagure']),
            'end_time': 1458307333.0,
            'human_time': arrow.get(1458307333).humanize(),
            'icon': 'https://apps.fedoraproject.org/packages/images/icons/package_128x128.png',
            'link': 'https://pagure.io/pungi-fedora/pull-request/18',
            'packages': set([]),
            'secondary_icon': 'https://seccdn.libravatar.org/avatar/0929fed032bd0a481ef74c46023fefe443f3d1b72dbe3efd293b25ed4fc843fd?s=64&d=retro',
            'start_time': 1458307333.0,
            'subjective': 'sgallagh interacted with pull-request #18 of project "pungi-fedora" 2 times',
            'subtitle': 'sgallagh interacted with pull-request #18 of project "pungi-fedora" 2 times',
            'timestamp': 1458307333.0,
            'topics': set(['io.pagure.prod.pagure.pull-request.comment.added',
                           'io.pagure.prod.pagure.pull-request.new']),
            'usernames': set(['sgallagh'])
        }, {
            'categories': set(['pagure']),
            'end_time': 1458306395.0,
            'human_time': arrow.get(1458306374.5).humanize(),
            'icon': 'https://apps.fedoraproject.org/packages/images/icons/package_128x128.png',
            'link': 'https://pagure.io/pungi/pull-request/235',
            'packages': set([]),
            'secondary_icon': 'https://seccdn.libravatar.org/avatar/e11f439e57cde0130fda04ad14b4f24376d56f6b0daae3e8f41fda1a05600651?s=64&d=retro',
            'start_time': 1458306354.0,
            'subjective': 'lsedlar interacted with pull-request #235 of project "pungi" 2 times',
            'subtitle': 'lsedlar interacted with pull-request #235 of project "pungi" 2 times',
            'timestamp': 1458306374.5,
            'topics': set(['io.pagure.prod.pagure.pull-request.flag.added',
                           'io.pagure.prod.pagure.pull-request.new']),
            'usernames': set(['lsedlar'])
        }, {
            'categories': set(['pagure']),
            'end_time': 1458306074.0,
            'human_time': arrow.get(1458305616.4).humanize(),
            'icon': 'https://apps.fedoraproject.org/packages/images/icons/package_128x128.png',
            'link': 'https://pagure.io/pungi/pull-request/234',
            'packages': set([]),
            'secondary_icon': 'https://seccdn.libravatar.org/avatar/e11f439e57cde0130fda04ad14b4f24376d56f6b0daae3e8f41fda1a05600651?s=64&d=retro',
            'start_time': 1458304911.0,
            'subjective': 'lsedlar interacted with pull-request #234 of project "pungi" 5 times',
            'subtitle': 'lsedlar interacted with pull-request #234 of project "pungi" 5 times',
            'timestamp': 1458305616.4,
            'topics': set(['io.pagure.prod.pagure.pull-request.closed',
                           'io.pagure.prod.pagure.pull-request.comment.added',
                           'io.pagure.prod.pagure.pull-request.flag.added',
                           'io.pagure.prod.pagure.pull-request.new']),
            'usernames': set(['lsedlar'])
        }, {
            'categories': set(['pagure']),
            'end_time': 1458305858.0,
            'human_time': arrow.get(1458305858.0).humanize(),
            'icon': 'https://apps.fedoraproject.org/packages/images/icons/package_128x128.png',
            'link': 'https://pagure.io/pagure/issue/849',
            'packages': set([]),
            'secondary_icon': 'https://seccdn.libravatar.org/avatar/1216fff466c9dbb6ce85ac95bf8f45b9e19421af97de67945852722b899a34ee?s=64&d=retro',
            'start_time': 1458305858.0,
            'subjective': u'bonnegent opened a new ticket pagure#849: "pagure on python3"',
            'subtitle': u'bonnegent opened a new ticket pagure#849: "pagure on python3"',
            'timestamp': 1458305858.0,
            'topics': set(['io.pagure.prod.pagure.issue.new']),
            'usernames': set(['bonnegent'])
        }, {
            'categories': set(['pagure']),
            'end_time': 1458303598.0,
            'human_time': arrow.get(1458299536.142857).humanize(),
            'icon': 'https://apps.fedoraproject.org/packages/images/icons/package_128x128.png',
            'link': 'https://pagure.io/pagure/pull-request/843',
            'packages': set([]),
            'secondary_icon': 'https://seccdn.libravatar.org/avatar/ad9e5c1cfd5d5180a6b9a8ebdc5fc91fbd899dd4d2fe780b4f9963598216d7f8?s=64&d=retro',
            'start_time': 1458298555.0,
            'subjective': 'aavrug and pingou interacted with pull-request #843 of project "pagure" 7 times',
            'subtitle': 'aavrug and pingou interacted with pull-request #843 of project "pagure" 7 times',
            'timestamp': 1458299536.142857,
            'topics': set(['io.pagure.prod.pagure.pull-request.comment.added']),
            'usernames': set(['aavrug', 'pingou']),
        }, {
            'categories': set(['pagure']),
            'end_time': 1458298137.0,
            'human_time': arrow.get(1458298005.5).humanize(),
            'icon': 'https://apps.fedoraproject.org/packages/images/icons/package_128x128.png',
            'link': 'https://pagure.io/pagure/issue/833',
            'packages': set([]),
            'secondary_icon': 'https://seccdn.libravatar.org/avatar/01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c?s=64&d=retro',
            'start_time': 1458297874.0,
            'subjective': 'pingou interacted with issue #833 of project "pagure" 2 times',
            'subtitle': 'pingou interacted with issue #833 of project "pagure" 2 times',
            'timestamp': 1458298005.5,
            'topics': set(['io.pagure.prod.pagure.issue.comment.added']),
            'usernames': set(['pingou']),
        }, {
            'categories': set(['pagure']),
            'end_time': 1458297187.0,
            'human_time': arrow.get(1458297187.0).humanize(),
            'icon': 'https://apps.fedoraproject.org/packages/images/icons/package_128x128.png',
            'link': 'https://pagure.io/pagure/pull-request/848#comment-3484',
            'packages': set([]),
            'secondary_icon': 'https://seccdn.libravatar.org/avatar/01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c?s=64&d=retro',
            'start_time': 1458297187.0,
            'subjective': u'pingou commented on PR #848 on pagure',
            'subtitle': u'pingou commented on PR #848 on pagure',
            'timestamp': 1458297187.0,
            'topics': set(['io.pagure.prod.pagure.pull-request.comment.added']),
            'usernames': set(['pingou'])}
    ]
    originals = [
        {
            "i": 2,
            "msg": {
                "agent": "ausil",
                "issue": {
                    "assignee": None,
                    "blocks": [],
                    "comments": [
                        {
                            "comment": "looking at the lorax code find_templates only exists in the f24-branch and master. ",
                            "date_created": "1458167951",
                            "edited_on": None,
                            "editor": None,
                            "id": 2021,
                            "parent": None,
                            "user": {
                                "fullname": "Dennis Gilmore",
                                "name": "ausil"
                            }
                        },
                        {
                            "comment": "pungi is actually doing terrible things here. it is making assumptions on the compose box where the templates will be in the runroot environment. we are going to have to run something in the chroot that will tell us or we need to move to making the DVD as part of the process that makes the install tree. which is what pungi cli does",
                            "date_created": "1458228506",
                            "edited_on": None,
                            "editor": None,
                            "id": 2030,
                            "parent": None,
                            "user": {
                                "fullname": "Dennis Gilmore",
                                "name": "ausil"
                            }
                        },
                        {
                            "comment": "In my opinion th best solution would be to add a configuration option to specify the path so that there is no guessing. See #235. For lack of better name I called it `iso_boot_option_map`, which is not really descriptive, but I don't know exactly what this path means.\r\n\r\nAnother solution would be to modify the command in `runroot` task to call pylorax, find the correct path and substitute that into proper place (with some fallback if pylorax is not available). This is not easy to implement as I can't bypass some of the quoting.\r\n\r\nTechnically, we could hack it and run a separate `runroot` task to find the directory ([example](http://koji.stg.fedoraproject.org/koji/taskinfo?taskID=90043678)), put it into the command on the compose box and then continue as usual. The code is not that difficult (#234), but it is not really a solution.",
                            "date_created": "1458306489",
                            "edited_on": None,
                            "editor": None,
                            "id": 2037,
                            "parent": None,
                            "user": {
                                "fullname": "Lubomír Sedlář",
                                "name": "lsedlar"
                            }
                        },
                        {
                            "comment": "I think if we write a command in pungi that makes the dvd iso and is able to figure it out is best. we then change the runroot call to install pungi, execute the command to make the dvd. its all then nicely contained. and we do not make any assumptions on the runroot environment ",
                            "date_created": "1458308858",
                            "edited_on": None,
                            "editor": None,
                            "id": 2038,
                            "parent": None,
                            "user": {
                                "fullname": "Dennis Gilmore",
                                "name": "ausil"
                            }
                        }
                    ],
    "content": "Related to PR #230 we need to be able to dynamically work out where the templates are located depending on the version of lorax so we don't need to hard code locations. ",
    "date_created": "1458167510",
    "depends": [],
    "id": 231,
    "private": False,
    "status": "Open",
    "tags": [],
    "title": "Use pylorax to locate templates",
    "user": {
        "fullname": "Peter Robinson",
        "name": "pbrobinson"
    }
    },
    "project": {
        "date_created": "1431529680",
        "description": "Distribution compose tool",
        "id": 8,
        "name": "pungi",
        "parent": None,
        "settings": {
            "Enforce_signed-off_commits_in_pull-request": True,
            "Minimum_score_to_merge_pull-request": -1,
            "Only_assignee_can_merge_pull-request": False,
            "Web-hooks": None,
            "always_merge": False,
            "issue_tracker": True,
            "project_documentation": True,
            "pull_requests": True
        },
        "tags": [
            "releng compose distribution"
        ],
        "user": {
            "fullname": "Dennis Gilmore",
            "name": "ausil"
        }
    }
    },
    "msg_id": "2016-f6837c28-7ae7-4417-8cdb-8b1017b114c3",
    "timestamp": 1458308863.0,
    "topic": "io.pagure.prod.pagure.issue.comment.added"
    },
    {
        "i": 2,
        "msg": {
            "agent": "bonnegent",
            "project": {
                "date_created": "1458307490",
                "description": "A git centered forge",
                "id": 429,
                "name": "pagure",
                "parent": {
                    "date_created": "1431549490",
                    "description": "A git centered forge",
                    "id": 10,
                    "name": "pagure",
                    "parent": None,
                    "settings": {
                        "Enforce_signed-off_commits_in_pull-request": False,
                        "Minimum_score_to_merge_pull-request": -1,
                        "Only_assignee_can_merge_pull-request": False,
                        "Web-hooks": None,
                        "always_merge": False,
                        "issue_tracker": True,
                        "project_documentation": True,
                        "pull_requests": True
                    },
                    "tags": [
                        "pagure",
                        "fedmsg",
                        "fedora-infra"
                    ],
                    "user": {
                        "fullname": "Pierre-YvesChibon",
                        "name": "pingou"
                    }
                },
                "settings": {
                    "Enforce_signed-off_commits_in_pull-request": False,
                    "Minimum_score_to_merge_pull-request": -1,
                    "Only_assignee_can_merge_pull-request": False,
                    "Web-hooks": None,
                    "always_merge": False,
                    "issue_tracker": False,
                    "project_documentation": True,
                    "pull_requests": False
                },
                "tags": [],
                "user": {
                    "fullname": "Sébastien Bonnegent",
                    "name": "bonnegent"
                }
            }
        },
    "msg_id": "2016-8801e2f4-42f1-45d5-8272-6457a3d85c4d",
    "timestamp": 1458307490.0,
    "topic": "io.pagure.prod.pagure.project.forked"
    },
    {
        "i": 2,
        "msg": {
            "agent": "sgallagh",
            "pullrequest": {
                "assignee": None,
                "branch": "f24",
                "branch_from": "f24",
                "closed_at": None,
                "closed_by": None,
                "comments": [],
                "commit_start": None,
                "commit_stop": None,
                "date_created": "1458307394",
                "id": 19,
                "project": {
                    "date_created": "1432928381",
                    "description": "fedora config files for pungi",
                    "id": 36,
                    "name": "pungi-fedora",
                    "parent": None,
                    "settings": {
                        "Enforce_signed-off_commits_in_pull-request": True,
                        "Minimum_score_to_merge_pull-request": -1,
                        "Only_assignee_can_merge_pull-request": False,
                        "Web-hooks": None,
                        "always_merge": False,
                        "issue_tracker": True,
                        "project_documentation": True,
                        "pull_requests": True
                    },
                    "tags": [
                        "releng"
                    ],
                    "user": {
                        "fullname": "Dennis Gilmore",
                        "name": "ausil"
                    }
                },
                "remote_git": None,
                "repo_from": {
                    "date_created": "1449595462",
                    "description": "fedora config files for pungi",
                    "id": 284,
                    "name": "pungi-fedora",
                    "parent": {
                        "date_created": "1432928381",
                        "description": "fedora config files for pungi",
                        "id": 36,
                        "name": "pungi-fedora",
                        "parent": None,
                        "settings": {
                            "Enforce_signed-off_commits_in_pull-request": True,
                            "Minimum_score_to_merge_pull-request": -1,
                            "Only_assignee_can_merge_pull-request": False,
                            "Web-hooks": None,
                            "always_merge": False,
                            "issue_tracker": True,
                            "project_documentation": True,
                            "pull_requests": True
                        },
                        "tags": [
                            "releng"
                        ],
                        "user": {
                            "fullname": "Dennis Gilmore",
                            "name": "ausil"
                        }
                    },
                    "settings": {
                        "Enforce_signed-off_commits_in_pull-request": False,
                        "Minimum_score_to_merge_pull-request": -1,
                        "Only_assignee_can_merge_pull-request": False,
                        "Web-hooks": None,
                        "always_merge": False,
                        "issue_tracker": True,
                        "project_documentation": True,
                        "pull_requests": True
                    },
                    "tags": [],
                    "user": {
                        "fullname": "Stephen Gallagher",
                        "name": "sgallagh"
                    }
                },
    "status": "Open",
    "title": "(F24) Server: Add \"Fedora Custom Operating System\" Environment",
    "uid": "8c6252b757ca4ff2a0f23cbc41e32ba7",
    "updated_on": "1458307394",
    "user": {
        "fullname": "Stephen Gallagher",
        "name": "sgallagh"
    }
    }
    },
    "msg_id": "2016-7e1ee254-ad19-4d8f-8568-867646aad2a0",
    "timestamp": 1458307394.0,
    "topic": "io.pagure.prod.pagure.pull-request.new"
    },
    {
        "i": 3,
        "msg": {
            "agent": "sgallagh",
            "pullrequest": {
                "assignee": None,
                "branch": "f24",
                "branch_from": "f24",
                "closed_at": None,
                "closed_by": None,
                "comments": [],
                "commit_start": None,
                "commit_stop": None,
                "date_created": "1458307394",
                "id": 19,
                "project": {
                    "date_created": "1432928381",
                    "description": "fedora config files for pungi",
                    "id": 36,
                    "name": "pungi-fedora",
                    "parent": None,
                    "settings": {
                        "Enforce_signed-off_commits_in_pull-request": True,
                        "Minimum_score_to_merge_pull-request": -1,
                        "Only_assignee_can_merge_pull-request": False,
                        "Web-hooks": None,
                        "always_merge": False,
                        "issue_tracker": True,
                        "project_documentation": True,
                        "pull_requests": True
                    },
                    "tags": [
                        "releng"
                    ],
                    "user": {
                        "fullname": "Dennis Gilmore",
                        "name": "ausil"
                    }
                },
                "remote_git": None,
                "repo_from": {
                    "date_created": "1449595462",
                    "description": "fedora config files for pungi",
                    "id": 284,
                    "name": "pungi-fedora",
                    "parent": {
                        "date_created": "1432928381",
                        "description": "fedora config files for pungi",
                        "id": 36,
                        "name": "pungi-fedora",
                        "parent": None,
                        "settings": {
                            "Enforce_signed-off_commits_in_pull-request": True,
                            "Minimum_score_to_merge_pull-request": -1,
                            "Only_assignee_can_merge_pull-request": False,
                            "Web-hooks": None,
                            "always_merge": False,
                            "issue_tracker": True,
                            "project_documentation": True,
                            "pull_requests": True
                        },
                        "tags": [
                            "releng"
                        ],
                        "user": {
                            "fullname": "Dennis Gilmore",
                            "name": "ausil"
                        }
                    },
                    "settings": {
                        "Enforce_signed-off_commits_in_pull-request": False,
                        "Minimum_score_to_merge_pull-request": -1,
                        "Only_assignee_can_merge_pull-request": False,
                        "Web-hooks": None,
                        "always_merge": False,
                        "issue_tracker": True,
                        "project_documentation": True,
                        "pull_requests": True
                    },
                    "tags": [],
                    "user": {
                        "fullname": "Stephen Gallagher",
                        "name": "sgallagh"
                    }
                },
    "status": "Open",
    "title": "(F24) Server: Add \"Fedora Custom Operating System\" Environment",
    "uid": "8c6252b757ca4ff2a0f23cbc41e32ba7",
    "updated_on": "1458307394",
    "user": {
        "fullname": "Stephen Gallagher",
        "name": "sgallagh"
    }
    }
    },
    "msg_id": "2016-0d5aa115-1f78-45d4-bde1-a3b73ac0fd2c",
    "timestamp": 1458307394.0,
    "topic": "io.pagure.prod.pagure.pull-request.comment.added"
    },
    {
        "i": 2,
        "msg": {
            "agent": "sgallagh",
            "pullrequest": {
                "assignee": None,
                "branch": "master",
                "branch_from": "master",
                "closed_at": None,
                "closed_by": None,
                "comments": [],
                "commit_start": None,
                "commit_stop": None,
                "date_created": "1458307332",
                "id": 18,
                "project": {
                    "date_created": "1432928381",
                    "description": "fedora config files for pungi",
                    "id": 36,
                    "name": "pungi-fedora",
                    "parent": None,
                    "settings": {
                        "Enforce_signed-off_commits_in_pull-request": True,
                        "Minimum_score_to_merge_pull-request": -1,
                        "Only_assignee_can_merge_pull-request": False,
                        "Web-hooks": None,
                        "always_merge": False,
                        "issue_tracker": True,
                        "project_documentation": True,
                        "pull_requests": True
                    },
                    "tags": [
                        "releng"
                    ],
                    "user": {
                        "fullname": "Dennis Gilmore",
                        "name": "ausil"
                    }
                },
                "remote_git": None,
                "repo_from": {
                    "date_created": "1449595462",
                    "description": "fedora config files for pungi",
                    "id": 284,
                    "name": "pungi-fedora",
                    "parent": {
                        "date_created": "1432928381",
                        "description": "fedora config files for pungi",
                        "id": 36,
                        "name": "pungi-fedora",
                        "parent": None,
                        "settings": {
                            "Enforce_signed-off_commits_in_pull-request": True,
                            "Minimum_score_to_merge_pull-request": -1,
                            "Only_assignee_can_merge_pull-request": False,
                            "Web-hooks": None,
                            "always_merge": False,
                            "issue_tracker": True,
                            "project_documentation": True,
                            "pull_requests": True
                        },
                        "tags": [
                            "releng"
                        ],
                        "user": {
                            "fullname": "Dennis Gilmore",
                            "name": "ausil"
                        }
                    },
                    "settings": {
                        "Enforce_signed-off_commits_in_pull-request": False,
                        "Minimum_score_to_merge_pull-request": -1,
                        "Only_assignee_can_merge_pull-request": False,
                        "Web-hooks": None,
                        "always_merge": False,
                        "issue_tracker": True,
                        "project_documentation": True,
                        "pull_requests": True
                    },
                    "tags": [],
                    "user": {
                        "fullname": "Stephen Gallagher",
                        "name": "sgallagh"
                    }
                },
    "status": "Open",
    "title": "(F25/Rawhide) Server: Add \"Fedora Custom Operating System\" Environment",
    "uid": "954179ff5f6a474aaaaccb5dc98116aa",
    "updated_on": "1458307332",
    "user": {
        "fullname": "Stephen Gallagher",
        "name": "sgallagh"
    }
    }
    },
    "msg_id": "2016-b58f6e52-dbc8-4082-8f2a-4d8aa6b4f988",
    "timestamp": 1458307333.0,
    "topic": "io.pagure.prod.pagure.pull-request.new"
    },
    {
        "i": 3,
        "msg": {
            "agent": "sgallagh",
            "pullrequest": {
                "assignee": None,
                "branch": "master",
                "branch_from": "master",
                "closed_at": None,
                "closed_by": None,
                "comments": [],
                "commit_start": None,
                "commit_stop": None,
                "date_created": "1458307332",
                "id": 18,
                "project": {
                    "date_created": "1432928381",
                    "description": "fedora config files for pungi",
                    "id": 36,
                    "name": "pungi-fedora",
                    "parent": None,
                    "settings": {
                        "Enforce_signed-off_commits_in_pull-request": True,
                        "Minimum_score_to_merge_pull-request": -1,
                        "Only_assignee_can_merge_pull-request": False,
                        "Web-hooks": None,
                        "always_merge": False,
                        "issue_tracker": True,
                        "project_documentation": True,
                        "pull_requests": True
                    },
                    "tags": [
                        "releng"
                    ],
                    "user": {
                        "fullname": "Dennis Gilmore",
                        "name": "ausil"
                    }
                },
                "remote_git": None,
                "repo_from": {
                    "date_created": "1449595462",
                    "description": "fedora config files for pungi",
                    "id": 284,
                    "name": "pungi-fedora",
                    "parent": {
                        "date_created": "1432928381",
                        "description": "fedora config files for pungi",
                        "id": 36,
                        "name": "pungi-fedora",
                        "parent": None,
                        "settings": {
                            "Enforce_signed-off_commits_in_pull-request": True,
                            "Minimum_score_to_merge_pull-request": -1,
                            "Only_assignee_can_merge_pull-request": False,
                            "Web-hooks": None,
                            "always_merge": False,
                            "issue_tracker": True,
                            "project_documentation": True,
                            "pull_requests": True
                        },
                        "tags": [
                            "releng"
                        ],
                        "user": {
                            "fullname": "Dennis Gilmore",
                            "name": "ausil"
                        }
                    },
                    "settings": {
                        "Enforce_signed-off_commits_in_pull-request": False,
                        "Minimum_score_to_merge_pull-request": -1,
                        "Only_assignee_can_merge_pull-request": False,
                        "Web-hooks": None,
                        "always_merge": False,
                        "issue_tracker": True,
                        "project_documentation": True,
                        "pull_requests": True
                    },
                    "tags": [],
                    "user": {
                        "fullname": "Stephen Gallagher",
                        "name": "sgallagh"
                    }
                },
    "status": "Open",
    "title": "(F25/Rawhide) Server: Add \"Fedora Custom Operating System\" Environment",
    "uid": "954179ff5f6a474aaaaccb5dc98116aa",
    "updated_on": "1458307332",
    "user": {
        "fullname": "Stephen Gallagher",
        "name": "sgallagh"
    }
    }
    },
    "msg_id": "2016-6bf8d983-75d0-484f-88ee-20575f1195d0",
    "timestamp": 1458307333.0,
    "topic": "io.pagure.prod.pagure.pull-request.comment.added"
    },
    {
        "i": 2,
        "msg": {
            "agent": "lsedlar",
            "issue": {
                "assignee": None,
                "blocks": [],
                "comments": [
                    {
                        "comment": "looking at the lorax code find_templates only exists in the f24-branch and master. ",
                        "date_created": "1458167951",
                        "edited_on": None,
                        "editor": None,
                        "id": 2021,
                        "parent": None,
                        "user": {
                            "fullname": "Dennis Gilmore",
                            "name": "ausil"
                        }
                    },
                    {
                        "comment": "pungi is actually doing terrible things here. it is making assumptions on the compose box where the templates will be in the runroot environment. we are going to have to run something in the chroot that will tell us or we need to move to making the DVD as part of the process that makes the install tree. which is what pungi cli does",
                        "date_created": "1458228506",
                        "edited_on": None,
                        "editor": None,
                        "id": 2030,
                        "parent": None,
                        "user": {
                            "fullname": "Dennis Gilmore",
                            "name": "ausil"
                        }
                    },
                    {
                        "comment": "In my opinion th best solution would be to add a configuration option to specify the path so that there is no guessing. See #235. For lack of better name I called it `iso_boot_option_map`, which is not really descriptive, but I don't know exactly what this path means.\r\n\r\nAnother solution would be to modify the command in `runroot` task to call pylorax, find the correct path and substitute that into proper place (with some fallback if pylorax is not available). This is not easy to implement as I can't bypass some of the quoting.\r\n\r\nTechnically, we could hack it and run a separate `runroot` task to find the directory ([example](http://koji.stg.fedoraproject.org/koji/taskinfo?taskID=90043678)), put it into the command on the compose box and then continue as usual. The code is not that difficult (#234), but it is not really a solution.",
                        "date_created": "1458306489",
                        "edited_on": None,
                        "editor": None,
                        "id": 2037,
                        "parent": None,
                        "user": {
                            "fullname": "Lubomír Sedlář",
                            "name": "lsedlar"
                        }
                    }
                ],
                "content": "Related to PR #230 we need to be able to dynamically work out where the templates are located depending on the version of lorax so we don't need to hard code locations. ",
                "date_created": "1458167510",
                "depends": [],
                "id": 231,
                "private": False,
                "status": "Open",
                "tags": [],
                "title": "Use pylorax to locate templates",
                "user": {
                    "fullname": "Peter Robinson",
                    "name": "pbrobinson"
                }
    },
    "project": {
        "date_created": "1431529680",
        "description": "Distribution compose tool",
        "id": 8,
        "name": "pungi",
        "parent": None,
        "settings": {
            "Enforce_signed-off_commits_in_pull-request": True,
            "Minimum_score_to_merge_pull-request": -1,
            "Only_assignee_can_merge_pull-request": False,
            "Web-hooks": None,
            "always_merge": False,
            "issue_tracker": True,
            "project_documentation": True,
            "pull_requests": True
        },
        "tags": [
            "releng compose distribution"
        ],
        "user": {
            "fullname": "Dennis Gilmore",
            "name": "ausil"
        }
    }
    },
    "msg_id": "2016-f887623c-481b-450c-8b1e-5445a85f5c53",
    "timestamp": 1458306489.0,
    "topic": "io.pagure.prod.pagure.issue.comment.added"
    },
    {
        "i": 1,
        "msg": {
            "agent": "lsedlar",
            "flag": {
                "comment": "Build successful",
                "date_created": "1458306394",
                "percent": "100",
                "pull_request_uid": "74df685a56804088aa9728684ba588bd",
                "uid": "32db8e8ab4fe43f3b217a7662c20c790",
                "url": "http://jenkins.fedorainfracloud.org/job/pungi/149/",
                "user": {
                    "fullname": "Lubomír Sedlář",
                    "name": "lsedlar"
                },
                "username": "Jenkins"
            },
            "pullrequest": {
                "assignee": None,
                "branch": "master",
                "branch_from": "lorax-dir",
                "closed_at": None,
                "closed_by": None,
                "comments": [],
                "commit_start": "6a8eed085c3693ad3d88b063dce363a0ce82d49d",
                "commit_stop": "6a8eed085c3693ad3d88b063dce363a0ce82d49d",
                "date_created": "1458306353",
                "id": 235,
                "project": {
                    "date_created": "1431529680",
                    "description": "Distribution compose tool",
                    "id": 8,
                    "name": "pungi",
                    "parent": None,
                    "settings": {
                        "Enforce_signed-off_commits_in_pull-request": True,
                        "Minimum_score_to_merge_pull-request": -1,
                        "Only_assignee_can_merge_pull-request": False,
                        "Web-hooks": None,
                        "always_merge": False,
                        "issue_tracker": True,
                        "project_documentation": True,
                        "pull_requests": True
                    },
                    "tags": [
                        "releng compose distribution"
                    ],
                    "user": {
                        "fullname": "Dennis Gilmore",
                        "name": "ausil"
                    }
                },
                "remote_git": None,
                "repo_from": {
                    "date_created": "1447057736",
                    "description": "Distribution compose tool",
                    "id": 244,
                    "name": "pungi",
                    "parent": {
                        "date_created": "1431529680",
                        "description": "Distribution compose tool",
                        "id": 8,
                        "name": "pungi",
                        "parent": None,
                        "settings": {
                            "Enforce_signed-off_commits_in_pull-request": True,
                            "Minimum_score_to_merge_pull-request": -1,
                            "Only_assignee_can_merge_pull-request": False,
                            "Web-hooks": None,
                            "always_merge": False,
                            "issue_tracker": True,
                            "project_documentation": True,
                            "pull_requests": True
                        },
                        "tags": [
                            "releng compose distribution"
                        ],
                        "user": {
                            "fullname": "Dennis Gilmore",
                            "name": "ausil"
                        }
                    },
                    "settings": {
                        "Enforce_signed-off_commits_in_pull-request": False,
                        "Minimum_score_to_merge_pull-request": -1,
                        "Only_assignee_can_merge_pull-request": False,
                        "Web-hooks": "http://46.101.221.203:8000/",
                        "always_merge": False,
                        "issue_tracker": False,
                        "project_documentation": True,
                        "pull_requests": False
                    },
                    "tags": [],
                    "user": {
                        "fullname": "Lubomír Sedlář",
                        "name": "lsedlar"
                    }
                },
    "status": "Open",
    "title": "Add option for lorax template dir",
    "uid": "74df685a56804088aa9728684ba588bd",
    "updated_on": "1458306356",
    "user": {
        "fullname": "Lubomír Sedlář",
        "name": "lsedlar"
    }
    }
    },
    "msg_id": "2016-f9b21316-6dad-4bdc-905b-c8ba6d9452a4",
    "timestamp": 1458306395.0,
    "topic": "io.pagure.prod.pagure.pull-request.flag.added"
    },
    {
        "i": 1,
        "msg": {
            "agent": "lsedlar",
            "pullrequest": {
                "assignee": None,
                "branch": "master",
                "branch_from": "lorax-dir",
                "closed_at": None,
                "closed_by": None,
                "comments": [],
                "commit_start": None,
                "commit_stop": None,
                "date_created": "1458306353",
                "id": 235,
                "project": {
                    "date_created": "1431529680",
                    "description": "Distribution compose tool",
                    "id": 8,
                    "name": "pungi",
                    "parent": None,
                    "settings": {
                        "Enforce_signed-off_commits_in_pull-request": True,
                        "Minimum_score_to_merge_pull-request": -1,
                        "Only_assignee_can_merge_pull-request": False,
                        "Web-hooks": None,
                        "always_merge": False,
                        "issue_tracker": True,
                        "project_documentation": True,
                        "pull_requests": True
                    },
                    "tags": [
                        "releng compose distribution"
                    ],
                    "user": {
                        "fullname": "Dennis Gilmore",
                        "name": "ausil"
                    }
                },
                "remote_git": None,
                "repo_from": {
                    "date_created": "1447057736",
                    "description": "Distribution compose tool",
                    "id": 244,
                    "name": "pungi",
                    "parent": {
                        "date_created": "1431529680",
                        "description": "Distribution compose tool",
                        "id": 8,
                        "name": "pungi",
                        "parent": None,
                        "settings": {
                            "Enforce_signed-off_commits_in_pull-request": True,
                            "Minimum_score_to_merge_pull-request": -1,
                            "Only_assignee_can_merge_pull-request": False,
                            "Web-hooks": None,
                            "always_merge": False,
                            "issue_tracker": True,
                            "project_documentation": True,
                            "pull_requests": True
                        },
                        "tags": [
                            "releng compose distribution"
                        ],
                        "user": {
                            "fullname": "Dennis Gilmore",
                            "name": "ausil"
                        }
                    },
                    "settings": {
                        "Enforce_signed-off_commits_in_pull-request": False,
                        "Minimum_score_to_merge_pull-request": -1,
                        "Only_assignee_can_merge_pull-request": False,
                        "Web-hooks": "http://46.101.221.203:8000/",
                        "always_merge": False,
                        "issue_tracker": False,
                        "project_documentation": True,
                        "pull_requests": False
                    },
                    "tags": [],
                    "user": {
                        "fullname": "Lubomír Sedlář",
                        "name": "lsedlar"
                    }
                },
    "status": "Open",
    "title": "Add option for lorax template dir",
    "uid": "74df685a56804088aa9728684ba588bd",
    "updated_on": "1458306353",
    "user": {
        "fullname": "Lubomír Sedlář",
        "name": "lsedlar"
    }
    }
    },
    "msg_id": "2016-4b71901b-5b39-4096-9c01-2e98efac7a37",
    "timestamp": 1458306354.0,
    "topic": "io.pagure.prod.pagure.pull-request.new"
    },
    {
        "i": 1,
        "msg": {
            "agent": "lsedlar",
            "pullrequest": {
                "assignee": None,
                "branch": "master",
                "branch_from": "lorax-find",
                "closed_at": "1458306073",
                "closed_by": {
                    "fullname": "Lubomír Sedlář",
                    "name": "lsedlar"
                },
                "comments": [
                    {
                        "comment": "Please don't merge this!\r\n\r\nIt's a really ugly hack. I'm just posting it here as a proof-of-concept.",
                        "commit": None,
                        "date_created": "1458306068",
                        "edited_on": None,
                        "editor": None,
                        "filename": None,
                        "id": 3493,
                        "line": None,
                        "notification": False,
                        "parent": None,
                        "tree": None,
                        "user": {
                            "fullname": "Lubomír Sedlář",
                            "name": "lsedlar"
                        }
                    }
                ],
                "commit_start": "6e2d96d15d0b386c64658707eacae42007c56504",
                "commit_stop": "6e2d96d15d0b386c64658707eacae42007c56504",
                "date_created": "1458304909",
                "id": 234,
                "project": {
                    "date_created": "1431529680",
                    "description": "Distribution compose tool",
                    "id": 8,
                    "name": "pungi",
                    "parent": None,
                    "settings": {
                        "Enforce_signed-off_commits_in_pull-request": True,
                        "Minimum_score_to_merge_pull-request": -1,
                        "Only_assignee_can_merge_pull-request": False,
                        "Web-hooks": None,
                        "always_merge": False,
                        "issue_tracker": True,
                        "project_documentation": True,
                        "pull_requests": True
                    },
                    "tags": [
                        "releng compose distribution"
                    ],
                    "user": {
                        "fullname": "Dennis Gilmore",
                        "name": "ausil"
                    }
                },
    "remote_git": None,
    "repo_from": {
        "date_created": "1447057736",
        "description": "Distribution compose tool",
        "id": 244,
        "name": "pungi",
        "parent": {
            "date_created": "1431529680",
            "description": "Distribution compose tool",
            "id": 8,
            "name": "pungi",
            "parent": None,
            "settings": {
                "Enforce_signed-off_commits_in_pull-request": True,
                "Minimum_score_to_merge_pull-request": -1,
                "Only_assignee_can_merge_pull-request": False,
                "Web-hooks": None,
                "always_merge": False,
                "issue_tracker": True,
                "project_documentation": True,
                "pull_requests": True
            },
            "tags": [
                "releng compose distribution"
            ],
            "user": {
                "fullname": "Dennis Gilmore",
                "name": "ausil"
            }
        },
        "settings": {
            "Enforce_signed-off_commits_in_pull-request": False,
            "Minimum_score_to_merge_pull-request": -1,
            "Only_assignee_can_merge_pull-request": False,
            "Web-hooks": "http://46.101.221.203:8000/",
            "always_merge": False,
            "issue_tracker": False,
            "project_documentation": True,
            "pull_requests": False
        },
        "tags": [],
        "user": {
            "fullname": "Lubomír Sedlář",
            "name": "lsedlar"
        }
    },
    "status": "Closed",
    "title": "[createiso] Add hack to get template dir from lorax",
    "uid": "08dcb7bf15574051ad1fef8af87cd3c7",
    "updated_on": "1458306073",
    "user": {
        "fullname": "Lubomír Sedlář",
        "name": "lsedlar"
    }
    }
    },
    "msg_id": "2016-4614f57c-b3c8-4ed3-ad8e-a4cefd716986",
    "timestamp": 1458306074.0,
    "topic": "io.pagure.prod.pagure.pull-request.comment.added"
    },
    {
        "i": 2,
        "msg": {
            "agent": "lsedlar",
            "merged": False,
            "pullrequest": {
                "assignee": None,
                "branch": "master",
                "branch_from": "lorax-find",
                "closed_at": "1458306073",
                "closed_by": {
                    "fullname": "Lubomír Sedlář",
                    "name": "lsedlar"
                },
                "comments": [
                    {
                        "comment": "Please don't merge this!\r\n\r\nIt's a really ugly hack. I'm just posting it here as a proof-of-concept.",
                        "commit": None,
                        "date_created": "1458306068",
                        "edited_on": None,
                        "editor": None,
                        "filename": None,
                        "id": 3493,
                        "line": None,
                        "notification": False,
                        "parent": None,
                        "tree": None,
                        "user": {
                            "fullname": "Lubomír Sedlář",
                            "name": "lsedlar"
                        }
                    }
                ],
                "commit_start": "6e2d96d15d0b386c64658707eacae42007c56504",
                "commit_stop": "6e2d96d15d0b386c64658707eacae42007c56504",
                "date_created": "1458304909",
                "id": 234,
                "project": {
                    "date_created": "1431529680",
                    "description": "Distribution compose tool",
                    "id": 8,
                    "name": "pungi",
                    "parent": None,
                    "settings": {
                        "Enforce_signed-off_commits_in_pull-request": True,
                        "Minimum_score_to_merge_pull-request": -1,
                        "Only_assignee_can_merge_pull-request": False,
                        "Web-hooks": None,
                        "always_merge": False,
                        "issue_tracker": True,
                        "project_documentation": True,
                        "pull_requests": True
                    },
                    "tags": [
                        "releng compose distribution"
                    ],
                    "user": {
                        "fullname": "Dennis Gilmore",
                        "name": "ausil"
                    }
                },
    "remote_git": None,
    "repo_from": {
        "date_created": "1447057736",
        "description": "Distribution compose tool",
        "id": 244,
        "name": "pungi",
        "parent": {
            "date_created": "1431529680",
            "description": "Distribution compose tool",
            "id": 8,
            "name": "pungi",
            "parent": None,
            "settings": {
                "Enforce_signed-off_commits_in_pull-request": True,
                "Minimum_score_to_merge_pull-request": -1,
                "Only_assignee_can_merge_pull-request": False,
                "Web-hooks": None,
                "always_merge": False,
                "issue_tracker": True,
                "project_documentation": True,
                "pull_requests": True
            },
            "tags": [
                "releng compose distribution"
            ],
            "user": {
                "fullname": "Dennis Gilmore",
                "name": "ausil"
            }
        },
        "settings": {
            "Enforce_signed-off_commits_in_pull-request": False,
            "Minimum_score_to_merge_pull-request": -1,
            "Only_assignee_can_merge_pull-request": False,
            "Web-hooks": "http://46.101.221.203:8000/",
            "always_merge": False,
            "issue_tracker": False,
            "project_documentation": True,
            "pull_requests": False
        },
        "tags": [],
        "user": {
            "fullname": "Lubomír Sedlář",
            "name": "lsedlar"
        }
    },
    "status": "Closed",
    "title": "[createiso] Add hack to get template dir from lorax",
    "uid": "08dcb7bf15574051ad1fef8af87cd3c7",
    "updated_on": "1458306073",
    "user": {
        "fullname": "Lubomír Sedlář",
        "name": "lsedlar"
    }
    }
    },
    "msg_id": "2016-07c4ccd5-e334-458f-a1bd-fdc1aebacbe6",
    "timestamp": 1458306074.0,
    "topic": "io.pagure.prod.pagure.pull-request.closed"
    },
    {
        "i": 1,
        "msg": {
            "agent": "lsedlar",
            "pullrequest": {
                "assignee": None,
                "branch": "master",
                "branch_from": "lorax-find",
                "closed_at": None,
                "closed_by": None,
                "comments": [
                    {
                        "comment": "Please don't merge this!\r\n\r\nIt's a really ugly hack. I'm just posting it here as a proof-of-concept.",
                        "commit": None,
                        "date_created": "1458306068",
                        "edited_on": None,
                        "editor": None,
                        "filename": None,
                        "id": 3493,
                        "line": None,
                        "notification": False,
                        "parent": None,
                        "tree": None,
                        "user": {
                            "fullname": "Lubomír Sedlář",
                            "name": "lsedlar"
                        }
                    }
                ],
                "commit_start": "6e2d96d15d0b386c64658707eacae42007c56504",
                "commit_stop": "6e2d96d15d0b386c64658707eacae42007c56504",
                "date_created": "1458304909",
                "id": 234,
                "project": {
                    "date_created": "1431529680",
                    "description": "Distribution compose tool",
                    "id": 8,
                    "name": "pungi",
                    "parent": None,
                    "settings": {
                        "Enforce_signed-off_commits_in_pull-request": True,
                        "Minimum_score_to_merge_pull-request": -1,
                        "Only_assignee_can_merge_pull-request": False,
                        "Web-hooks": None,
                        "always_merge": False,
                        "issue_tracker": True,
                        "project_documentation": True,
                        "pull_requests": True
                    },
                    "tags": [
                        "releng compose distribution"
                    ],
                    "user": {
                        "fullname": "Dennis Gilmore",
                        "name": "ausil"
                    }
                },
    "remote_git": None,
    "repo_from": {
        "date_created": "1447057736",
        "description": "Distribution compose tool",
        "id": 244,
        "name": "pungi",
        "parent": {
            "date_created": "1431529680",
            "description": "Distribution compose tool",
            "id": 8,
            "name": "pungi",
            "parent": None,
            "settings": {
                "Enforce_signed-off_commits_in_pull-request": True,
                "Minimum_score_to_merge_pull-request": -1,
                "Only_assignee_can_merge_pull-request": False,
                "Web-hooks": None,
                "always_merge": False,
                "issue_tracker": True,
                "project_documentation": True,
                "pull_requests": True
            },
            "tags": [
                "releng compose distribution"
            ],
            "user": {
                "fullname": "Dennis Gilmore",
                "name": "ausil"
            }
        },
        "settings": {
            "Enforce_signed-off_commits_in_pull-request": False,
            "Minimum_score_to_merge_pull-request": -1,
            "Only_assignee_can_merge_pull-request": False,
            "Web-hooks": "http://46.101.221.203:8000/",
            "always_merge": False,
            "issue_tracker": False,
            "project_documentation": True,
            "pull_requests": False
        },
        "tags": [],
        "user": {
            "fullname": "Lubomír Sedlář",
            "name": "lsedlar"
        }
    },
    "status": "Open",
    "title": "[createiso] Add hack to get template dir from lorax",
    "uid": "08dcb7bf15574051ad1fef8af87cd3c7",
    "updated_on": "1458304912",
    "user": {
        "fullname": "Lubomír Sedlář",
        "name": "lsedlar"
    }
    }
    },
    "msg_id": "2016-32b8d742-0b52-477a-99aa-b74aaa8d27c3",
    "timestamp": 1458306069.0,
    "topic": "io.pagure.prod.pagure.pull-request.comment.added"
    },
    {
        "i": 1,
        "msg": {
            "agent": "bonnegent",
            "issue": {
                "assignee": None,
                "blocks": [],
                "comments": [],
                "content": "Hi,\r\nI want to use Pagure with Python 3. Is it in roadmap ?\r\n\r\nI saw a branch 'py3_work' and I have some knowledge with python2/3, maybe I can help ?\r\n\r\nS.Bonnegent",
                "date_created": "1458305857",
                "depends": [],
                "id": 849,
                "private": False,
                "status": "Open",
                "tags": [],
                "title": "pagure on python3",
                "user": {
                    "fullname": "Sébastien Bonnegent",
                    "name": "bonnegent"
                }
            },
            "project": {
                "date_created": "1431549490",
                "description": "A git centered forge",
                "id": 10,
                "name": "pagure",
                "parent": None,
                "settings": {
                    "Enforce_signed-off_commits_in_pull-request": False,
                    "Minimum_score_to_merge_pull-request": -1,
                    "Only_assignee_can_merge_pull-request": False,
                    "Web-hooks": None,
                    "always_merge": False,
                    "issue_tracker": True,
                    "project_documentation": True,
                    "pull_requests": True
                },
                "tags": [
                    "pagure",
                    "fedmsg",
                    "fedora-infra"
                ],
                "user": {
                    "fullname": "Pierre-YvesChibon",
                    "name": "pingou"
                }
            }
        },
        "msg_id": "2016-42fc29b6-da18-4c69-aa04-85e510531ad0",
        "timestamp": 1458305858.0,
        "topic": "io.pagure.prod.pagure.issue.new"
    },
    {
        "i": 1,
        "msg": {
            "agent": "lsedlar",
            "flag": {
                "comment": "Build successful",
                "date_created": "1458304953",
                "percent": "100",
                "pull_request_uid": "08dcb7bf15574051ad1fef8af87cd3c7",
                "uid": "8881877e7d564cf0b9fc89964f709003",
                "url": "http://jenkins.fedorainfracloud.org/job/pungi/148/",
                "user": {
                    "fullname": "Lubomír Sedlář",
                    "name": "lsedlar"
                },
                "username": "Jenkins"
            },
            "pullrequest": {
                "assignee": None,
                "branch": "master",
                "branch_from": "lorax-find",
                "closed_at": None,
                "closed_by": None,
                "comments": [],
                "commit_start": "6e2d96d15d0b386c64658707eacae42007c56504",
                "commit_stop": "6e2d96d15d0b386c64658707eacae42007c56504",
                "date_created": "1458304909",
                "id": 234,
                "project": {
                    "date_created": "1431529680",
                    "description": "Distribution compose tool",
                    "id": 8,
                    "name": "pungi",
                    "parent": None,
                    "settings": {
                        "Enforce_signed-off_commits_in_pull-request": True,
                        "Minimum_score_to_merge_pull-request": -1,
                        "Only_assignee_can_merge_pull-request": False,
                        "Web-hooks": None,
                        "always_merge": False,
                        "issue_tracker": True,
                        "project_documentation": True,
                        "pull_requests": True
                    },
                    "tags": [
                        "releng compose distribution"
                    ],
                    "user": {
                        "fullname": "Dennis Gilmore",
                        "name": "ausil"
                    }
                },
                "remote_git": None,
                "repo_from": {
                    "date_created": "1447057736",
                    "description": "Distribution compose tool",
                    "id": 244,
                    "name": "pungi",
                    "parent": {
                        "date_created": "1431529680",
                        "description": "Distribution compose tool",
                        "id": 8,
                        "name": "pungi",
                        "parent": None,
                        "settings": {
                            "Enforce_signed-off_commits_in_pull-request": True,
                            "Minimum_score_to_merge_pull-request": -1,
                            "Only_assignee_can_merge_pull-request": False,
                            "Web-hooks": None,
                            "always_merge": False,
                            "issue_tracker": True,
                            "project_documentation": True,
                            "pull_requests": True
                        },
                        "tags": [
                            "releng compose distribution"
                        ],
                        "user": {
                            "fullname": "Dennis Gilmore",
                            "name": "ausil"
                        }
                    },
                    "settings": {
                        "Enforce_signed-off_commits_in_pull-request": False,
                        "Minimum_score_to_merge_pull-request": -1,
                        "Only_assignee_can_merge_pull-request": False,
                        "Web-hooks": "http://46.101.221.203:8000/",
                        "always_merge": False,
                        "issue_tracker": False,
                        "project_documentation": True,
                        "pull_requests": False
                    },
                    "tags": [],
                    "user": {
                        "fullname": "Lubomír Sedlář",
                        "name": "lsedlar"
                    }
                },
    "status": "Open",
    "title": "[createiso] Add hack to get template dir from lorax",
    "uid": "08dcb7bf15574051ad1fef8af87cd3c7",
    "updated_on": "1458304912",
    "user": {
        "fullname": "Lubomír Sedlář",
        "name": "lsedlar"
    }
    }
    },
    "msg_id": "2016-a7320bfb-67ce-4287-845b-55c3fd01d7da",
    "timestamp": 1458304954.0,
    "topic": "io.pagure.prod.pagure.pull-request.flag.added"
    },
    {
        "i": 1,
        "msg": {
            "agent": "lsedlar",
            "pullrequest": {
                "assignee": None,
                "branch": "master",
                "branch_from": "lorax-find",
                "closed_at": None,
                "closed_by": None,
                "comments": [],
                "commit_start": None,
                "commit_stop": None,
                "date_created": "1458304909",
                "id": 234,
                "project": {
                    "date_created": "1431529680",
                    "description": "Distribution compose tool",
                    "id": 8,
                    "name": "pungi",
                    "parent": None,
                    "settings": {
                        "Enforce_signed-off_commits_in_pull-request": True,
                        "Minimum_score_to_merge_pull-request": -1,
                        "Only_assignee_can_merge_pull-request": False,
                        "Web-hooks": None,
                        "always_merge": False,
                        "issue_tracker": True,
                        "project_documentation": True,
                        "pull_requests": True
                    },
                    "tags": [
                        "releng compose distribution"
                    ],
                    "user": {
                        "fullname": "Dennis Gilmore",
                        "name": "ausil"
                    }
                },
                "remote_git": None,
                "repo_from": {
                    "date_created": "1447057736",
                    "description": "Distribution compose tool",
                    "id": 244,
                    "name": "pungi",
                    "parent": {
                        "date_created": "1431529680",
                        "description": "Distribution compose tool",
                        "id": 8,
                        "name": "pungi",
                        "parent": None,
                        "settings": {
                            "Enforce_signed-off_commits_in_pull-request": True,
                            "Minimum_score_to_merge_pull-request": -1,
                            "Only_assignee_can_merge_pull-request": False,
                            "Web-hooks": None,
                            "always_merge": False,
                            "issue_tracker": True,
                            "project_documentation": True,
                            "pull_requests": True
                        },
                        "tags": [
                            "releng compose distribution"
                        ],
                        "user": {
                            "fullname": "Dennis Gilmore",
                            "name": "ausil"
                        }
                    },
                    "settings": {
                        "Enforce_signed-off_commits_in_pull-request": False,
                        "Minimum_score_to_merge_pull-request": -1,
                        "Only_assignee_can_merge_pull-request": False,
                        "Web-hooks": "http://46.101.221.203:8000/",
                        "always_merge": False,
                        "issue_tracker": False,
                        "project_documentation": True,
                        "pull_requests": False
                    },
                    "tags": [],
                    "user": {
                        "fullname": "Lubomír Sedlář",
                        "name": "lsedlar"
                    }
                },
    "status": "Open",
    "title": "[createiso] Add hack to get template dir from lorax",
    "uid": "08dcb7bf15574051ad1fef8af87cd3c7",
    "updated_on": "1458304909",
    "user": {
        "fullname": "Lubomír Sedlář",
        "name": "lsedlar"
    }
    }
    },
    "msg_id": "2016-25c5e4f7-ab6b-4f40-903d-35553ea0c9ca",
    "timestamp": 1458304911.0,
    "topic": "io.pagure.prod.pagure.pull-request.new"
    },
    {
        "i": 1,
        "msg": {
            "agent": "aavrug",
            "pullrequest": {
                "assignee": None,
                "branch": "master",
                "branch_from": "master",
                "closed_at": None,
                "closed_by": None,
                "comments": [
                    {
                        "comment": "Missing indentation for the content of the form :)",
                        "commit": "08d5e7567a6b1495be7d1da47ae8f5f5e0d079af",
                        "date_created": "1458228021",
                        "edited_on": None,
                        "editor": None,
                        "filename": "pagure/templates/repo_master.html",
                        "id": 3452,
                        "line": 13,
                        "notification": False,
                        "parent": None,
                        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
                        "user": {
                            "fullname": "Pierre-YvesChibon",
                            "name": "pingou"
                        }
                    },
                    {
                        "comment": "Pull-Request has been updated",
                        "commit": None,
                        "date_created": "1458228047",
                        "edited_on": None,
                        "editor": None,
                        "filename": None,
                        "id": 3453,
                        "line": None,
                        "notification": True,
                        "parent": None,
                        "tree": None,
                        "user": {
                            "fullname": "Gaurav Kumar",
                            "name": "aavrug"
                        }
                    },
                    {
                        "comment": "Instead of having these in the form w/ hidden fields, maybe we could place them in the URL as we do in other places",
                        "commit": "7ed981c2ce9e66f1637cba224455d45c611b660a",
                        "date_created": "1458228080",
                        "edited_on": None,
                        "editor": None,
                        "filename": "pagure/ui/repo.py",
                        "id": 3454,
                        "line": 16,
                        "notification": False,
                        "parent": None,
                        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
                        "user": {
                            "fullname": "Pierre-YvesChibon",
                            "name": "pingou"
                        }
                    },
    {
        "comment": "repo_user can be None, that's no problem, we just need to make sure it isn't ``''`` (ie: empty string)",
        "commit": "7ed981c2ce9e66f1637cba224455d45c611b660a",
        "date_created": "1458228121",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3455,
        "line": 21,
        "notification": False,
        "parent": None,
        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Could/Should we check the value of ``watch``?",
        "commit": "7ed981c2ce9e66f1637cba224455d45c611b660a",
        "date_created": "1458228145",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3456,
        "line": 14,
        "notification": False,
        "parent": None,
        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Well this doesn't tell us much since the URL doesn't exists whether a ``foo`` project exists or not :)",
        "commit": "9038eddfefdff0cf827a27ee38e05b8f638b2fe3",
        "date_created": "1458228184",
        "edited_on": None,
        "editor": None,
        "filename": "tests/test_pagure_flask_ui_repo.py",
        "id": 3457,
        "line": 8,
        "notification": False,
        "parent": None,
        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "It redirects you, but you're not checking the output, you should ``follow_redirects=True`` and see what's in the HTML. Did the ``Watch`` flag changed? Was there a message flashed? Did it redirect you to the right page?",
        "commit": "9038eddfefdff0cf827a27ee38e05b8f638b2fe3",
        "date_created": "1458228321",
        "edited_on": None,
        "editor": None,
        "filename": "tests/test_pagure_flask_ui_repo.py",
        "id": 3458,
        "line": 46,
        "notification": False,
        "parent": None,
        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458237791",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3464,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Pull-Request has been rebased",
        "commit": None,
        "date_created": "1458239574",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3465,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458240388",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3466,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Check the ConfirmationForm ;-)",
        "commit": "95df7c1b30c8288333a2d5247ddbcc3df7abf2a0",
        "date_created": "1458240462",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/forms.py",
        "id": 3467,
        "line": 5,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Check the login method, there is a way to check that the previous_url is sane",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240532",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3468,
        "line": 11,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "repo cannot be None, otherwise we would have a 404 since the URL wouldn't hit here :)",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240573",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3469,
        "line": 16,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Let's make this ``str(watch)`` to be sure :)",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240600",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3470,
        "line": 19,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "No need for the ``if user``, just specify it, if ``user`` is None, it'll know what to do, check the code ;-)",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240664",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3471,
        "line": 25,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "``rollback()`` shouldn't be needed for a ``PagureException`` but it would for a sqlalchemy error",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240714",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3472,
        "line": 38,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Split this string over two lines? (same below?)",
        "commit": "3c839ba86dcd909f4bc23d2ab7d9bc87d4442315",
        "date_created": "1458240771",
        "edited_on": None,
        "editor": None,
        "filename": "tests/test_pagure_flask_ui_repo.py",
        "id": 3473,
        "line": 42,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458275019",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3477,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458275207",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3478,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458281234",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3479,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Whenever you get time just review this. I have taken so much time for this issue, so now thinking that if this will merge then I will move to the next issue.",
        "commit": None,
        "date_created": "1458298555",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3486,
        "line": None,
        "notification": False,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "This should be taken care of in ``notify.py`` no?",
        "commit": "e9cd199e6d8e4e684b6d9b7440b7d8d3296699e4",
        "date_created": "1458298756",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/lib/model.py",
        "id": 3487,
        "line": 35,
        "notification": False,
        "parent": None,
        "tree": "00a6f09a5e31549784c6f61c48723942e7c108cf",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "No that is for the user is watching or not for watch/Unwatch button.",
        "commit": "e9cd199e6d8e4e684b6d9b7440b7d8d3296699e4",
        "date_created": "1458298870",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/lib/model.py",
        "id": 3488,
        "line": 35,
        "notification": False,
        "parent": None,
        "tree": "00a6f09a5e31549784c6f61c48723942e7c108cf",
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Let's be consistent about our URL schemas:\r\n\r\nI propose:\r\n\r\n    @APP.route('/<repo>/settings/watch', methods=['POST'])\r\n    @APP.route('/fork/<username>/<repo>/settings/watch', methods=['POST'])",
        "commit": "2158eb3ee1cafc26cd2632244efa655dc42c224b",
        "date_created": "1458298899",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3489,
        "line": 13,
        "notification": False,
        "parent": None,
        "tree": "00a6f09a5e31549784c6f61c48723942e7c108cf",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Yes but we remove all the users not watching in ``notify.py`` if I read the code correctly",
        "commit": "e9cd199e6d8e4e684b6d9b7440b7d8d3296699e4",
        "date_created": "1458298950",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/lib/model.py",
        "id": 3490,
        "line": 35,
        "notification": False,
        "parent": None,
        "tree": "00a6f09a5e31549784c6f61c48723942e7c108cf",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "https://pagure.io/pagure/pull-request/843#_5,15 that is for this and It is not related to notify.",
        "commit": "e9cd199e6d8e4e684b6d9b7440b7d8d3296699e4",
        "date_created": "1458299121",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/lib/model.py",
        "id": 3491,
        "line": 35,
        "notification": False,
        "parent": None,
        "tree": "00a6f09a5e31549784c6f61c48723942e7c108cf",
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Pull-Request has been rebased",
        "commit": None,
        "date_created": "1458303598",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3492,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    }
    ],
    "commit_start": "bbc08a4648aa96619823b1c7489c56d390b4934b",
    "commit_stop": "26b54098ac3024d7f799a13ceec5d04c1c6c35f7",
    "date_created": "1458226010",
    "id": 843,
    "project": {
        "date_created": "1431549490",
        "description": "A git centered forge",
        "id": 10,
        "name": "pagure",
        "parent": None,
        "settings": {
            "Enforce_signed-off_commits_in_pull-request": False,
            "Minimum_score_to_merge_pull-request": -1,
            "Only_assignee_can_merge_pull-request": False,
            "Web-hooks": None,
            "always_merge": False,
            "issue_tracker": True,
            "project_documentation": True,
            "pull_requests": True
        },
        "tags": [
            "pagure",
            "fedmsg",
            "fedora-infra"
        ],
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    "remote_git": None,
    "repo_from": {
        "date_created": "1449051695",
        "description": "A git centered forge",
        "id": 278,
        "name": "pagure",
        "parent": {
            "date_created": "1431549490",
            "description": "A git centered forge",
            "id": 10,
            "name": "pagure",
            "parent": None,
            "settings": {
                "Enforce_signed-off_commits_in_pull-request": False,
                "Minimum_score_to_merge_pull-request": -1,
                "Only_assignee_can_merge_pull-request": False,
                "Web-hooks": None,
                "always_merge": False,
                "issue_tracker": True,
                "project_documentation": True,
                "pull_requests": True
            },
            "tags": [
                "pagure",
                "fedmsg",
                "fedora-infra"
            ],
            "user": {
                "fullname": "Pierre-YvesChibon",
                "name": "pingou"
            }
        },
        "settings": {
            "Enforce_signed-off_commits_in_pull-request": False,
            "Minimum_score_to_merge_pull-request": -1,
            "Only_assignee_can_merge_pull-request": False,
            "Web-hooks": None,
            "always_merge": False,
            "issue_tracker": True,
            "project_documentation": True,
            "pull_requests": True
        },
        "tags": [],
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    "status": "Open",
    "title": "Added watch feature.",
    "uid": "53e47f3c13874c9eb39675973e21e711",
    "updated_on": "1458303597",
    "user": {
        "fullname": "Gaurav Kumar",
        "name": "aavrug"
    }
    }
    },
    "msg_id": "2016-0c9940a9-ef5b-47fc-a2e1-57bff4ecf064",
    "timestamp": 1458303598.0,
    "topic": "io.pagure.prod.pagure.pull-request.comment.added"
    },
    {
        "i": 2,
        "msg": {
            "agent": "aavrug",
            "pullrequest": {
                "assignee": None,
                "branch": "master",
                "branch_from": "master",
                "closed_at": None,
                "closed_by": None,
                "comments": [
                    {
                        "comment": "Missing indentation for the content of the form :)",
                        "commit": "08d5e7567a6b1495be7d1da47ae8f5f5e0d079af",
                        "date_created": "1458228021",
                        "edited_on": None,
                        "editor": None,
                        "filename": "pagure/templates/repo_master.html",
                        "id": 3452,
                        "line": 13,
                        "notification": False,
                        "parent": None,
                        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
                        "user": {
                            "fullname": "Pierre-YvesChibon",
                            "name": "pingou"
                        }
                    },
                    {
                        "comment": "Pull-Request has been updated",
                        "commit": None,
                        "date_created": "1458228047",
                        "edited_on": None,
                        "editor": None,
                        "filename": None,
                        "id": 3453,
                        "line": None,
                        "notification": True,
                        "parent": None,
                        "tree": None,
                        "user": {
                            "fullname": "Gaurav Kumar",
                            "name": "aavrug"
                        }
                    },
                    {
                        "comment": "Instead of having these in the form w/ hidden fields, maybe we could place them in the URL as we do in other places",
                        "commit": "7ed981c2ce9e66f1637cba224455d45c611b660a",
                        "date_created": "1458228080",
                        "edited_on": None,
                        "editor": None,
                        "filename": "pagure/ui/repo.py",
                        "id": 3454,
                        "line": 16,
                        "notification": False,
                        "parent": None,
                        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
                        "user": {
                            "fullname": "Pierre-YvesChibon",
                            "name": "pingou"
                        }
                    },
    {
        "comment": "repo_user can be None, that's no problem, we just need to make sure it isn't ``''`` (ie: empty string)",
        "commit": "7ed981c2ce9e66f1637cba224455d45c611b660a",
        "date_created": "1458228121",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3455,
        "line": 21,
        "notification": False,
        "parent": None,
        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Could/Should we check the value of ``watch``?",
        "commit": "7ed981c2ce9e66f1637cba224455d45c611b660a",
        "date_created": "1458228145",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3456,
        "line": 14,
        "notification": False,
        "parent": None,
        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Well this doesn't tell us much since the URL doesn't exists whether a ``foo`` project exists or not :)",
        "commit": "9038eddfefdff0cf827a27ee38e05b8f638b2fe3",
        "date_created": "1458228184",
        "edited_on": None,
        "editor": None,
        "filename": "tests/test_pagure_flask_ui_repo.py",
        "id": 3457,
        "line": 8,
        "notification": False,
        "parent": None,
        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "It redirects you, but you're not checking the output, you should ``follow_redirects=True`` and see what's in the HTML. Did the ``Watch`` flag changed? Was there a message flashed? Did it redirect you to the right page?",
        "commit": "9038eddfefdff0cf827a27ee38e05b8f638b2fe3",
        "date_created": "1458228321",
        "edited_on": None,
        "editor": None,
        "filename": "tests/test_pagure_flask_ui_repo.py",
        "id": 3458,
        "line": 46,
        "notification": False,
        "parent": None,
        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458237791",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3464,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Pull-Request has been rebased",
        "commit": None,
        "date_created": "1458239574",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3465,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458240388",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3466,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Check the ConfirmationForm ;-)",
        "commit": "95df7c1b30c8288333a2d5247ddbcc3df7abf2a0",
        "date_created": "1458240462",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/forms.py",
        "id": 3467,
        "line": 5,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Check the login method, there is a way to check that the previous_url is sane",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240532",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3468,
        "line": 11,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "repo cannot be None, otherwise we would have a 404 since the URL wouldn't hit here :)",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240573",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3469,
        "line": 16,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Let's make this ``str(watch)`` to be sure :)",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240600",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3470,
        "line": 19,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "No need for the ``if user``, just specify it, if ``user`` is None, it'll know what to do, check the code ;-)",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240664",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3471,
        "line": 25,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "``rollback()`` shouldn't be needed for a ``PagureException`` but it would for a sqlalchemy error",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240714",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3472,
        "line": 38,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Split this string over two lines? (same below?)",
        "commit": "3c839ba86dcd909f4bc23d2ab7d9bc87d4442315",
        "date_created": "1458240771",
        "edited_on": None,
        "editor": None,
        "filename": "tests/test_pagure_flask_ui_repo.py",
        "id": 3473,
        "line": 42,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458275019",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3477,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458275207",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3478,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458281234",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3479,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Whenever you get time just review this. I have taken so much time for this issue, so now thinking that if this will merge then I will move to the next issue.",
        "commit": None,
        "date_created": "1458298555",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3486,
        "line": None,
        "notification": False,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "This should be taken care of in ``notify.py`` no?",
        "commit": "e9cd199e6d8e4e684b6d9b7440b7d8d3296699e4",
        "date_created": "1458298756",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/lib/model.py",
        "id": 3487,
        "line": 35,
        "notification": False,
        "parent": None,
        "tree": "00a6f09a5e31549784c6f61c48723942e7c108cf",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "No that is for the user is watching or not for watch/Unwatch button.",
        "commit": "e9cd199e6d8e4e684b6d9b7440b7d8d3296699e4",
        "date_created": "1458298870",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/lib/model.py",
        "id": 3488,
        "line": 35,
        "notification": False,
        "parent": None,
        "tree": "00a6f09a5e31549784c6f61c48723942e7c108cf",
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Let's be consistent about our URL schemas:\r\n\r\nI propose:\r\n\r\n    @APP.route('/<repo>/settings/watch', methods=['POST'])\r\n    @APP.route('/fork/<username>/<repo>/settings/watch', methods=['POST'])",
        "commit": "2158eb3ee1cafc26cd2632244efa655dc42c224b",
        "date_created": "1458298899",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3489,
        "line": 13,
        "notification": False,
        "parent": None,
        "tree": "00a6f09a5e31549784c6f61c48723942e7c108cf",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Yes but we remove all the users not watching in ``notify.py`` if I read the code correctly",
        "commit": "e9cd199e6d8e4e684b6d9b7440b7d8d3296699e4",
        "date_created": "1458298950",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/lib/model.py",
        "id": 3490,
        "line": 35,
        "notification": False,
        "parent": None,
        "tree": "00a6f09a5e31549784c6f61c48723942e7c108cf",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "https://pagure.io/pagure/pull-request/843#_5,15 that is for this and It is not related to notify.",
        "commit": "e9cd199e6d8e4e684b6d9b7440b7d8d3296699e4",
        "date_created": "1458299121",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/lib/model.py",
        "id": 3491,
        "line": "35",
        "notification": False,
        "parent": None,
        "tree": "00a6f09a5e31549784c6f61c48723942e7c108cf",
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    }
    ],
    "commit_start": "498572b754599022f358b370bf66fe5c8c10db58",
    "commit_stop": "d3b1f21fed867629d541ec1c1537c65d06851d7d",
    "date_created": "1458226010",
    "id": 843,
    "project": {
        "date_created": "1431549490",
        "description": "A git centered forge",
        "id": 10,
        "name": "pagure",
        "parent": None,
        "settings": {
            "Enforce_signed-off_commits_in_pull-request": False,
            "Minimum_score_to_merge_pull-request": -1,
            "Only_assignee_can_merge_pull-request": False,
            "Web-hooks": None,
            "always_merge": False,
            "issue_tracker": True,
            "project_documentation": True,
            "pull_requests": True
        },
        "tags": [
            "pagure",
            "fedmsg",
            "fedora-infra"
        ],
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    "remote_git": None,
    "repo_from": {
        "date_created": "1449051695",
        "description": "A git centered forge",
        "id": 278,
        "name": "pagure",
        "parent": {
            "date_created": "1431549490",
            "description": "A git centered forge",
            "id": 10,
            "name": "pagure",
            "parent": None,
            "settings": {
                "Enforce_signed-off_commits_in_pull-request": False,
                "Minimum_score_to_merge_pull-request": -1,
                "Only_assignee_can_merge_pull-request": False,
                "Web-hooks": None,
                "always_merge": False,
                "issue_tracker": True,
                "project_documentation": True,
                "pull_requests": True
            },
            "tags": [
                "pagure",
                "fedmsg",
                "fedora-infra"
            ],
            "user": {
                "fullname": "Pierre-YvesChibon",
                "name": "pingou"
            }
        },
        "settings": {
            "Enforce_signed-off_commits_in_pull-request": False,
            "Minimum_score_to_merge_pull-request": -1,
            "Only_assignee_can_merge_pull-request": False,
            "Web-hooks": None,
            "always_merge": False,
            "issue_tracker": True,
            "project_documentation": True,
            "pull_requests": True
        },
        "tags": [],
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    "status": "Open",
    "title": "Added watch feature.",
    "uid": "53e47f3c13874c9eb39675973e21e711",
    "updated_on": "1458298091",
    "user": {
        "fullname": "Gaurav Kumar",
        "name": "aavrug"
    }
    }
    },
    "msg_id": "2016-7588d752-395c-408d-869a-967155cce0ab",
    "timestamp": 1458299121.0,
    "topic": "io.pagure.prod.pagure.pull-request.comment.added"
    },
    {
        "i": 1,
        "msg": {
            "agent": "pingou",
            "pullrequest": {
                "assignee": None,
                "branch": "master",
                "branch_from": "master",
                "closed_at": None,
                "closed_by": None,
                "comments": [
                    {
                        "comment": "Missing indentation for the content of the form :)",
                        "commit": "08d5e7567a6b1495be7d1da47ae8f5f5e0d079af",
                        "date_created": "1458228021",
                        "edited_on": None,
                        "editor": None,
                        "filename": "pagure/templates/repo_master.html",
                        "id": 3452,
                        "line": 13,
                        "notification": False,
                        "parent": None,
                        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
                        "user": {
                            "fullname": "Pierre-YvesChibon",
                            "name": "pingou"
                        }
                    },
                    {
                        "comment": "Pull-Request has been updated",
                        "commit": None,
                        "date_created": "1458228047",
                        "edited_on": None,
                        "editor": None,
                        "filename": None,
                        "id": 3453,
                        "line": None,
                        "notification": True,
                        "parent": None,
                        "tree": None,
                        "user": {
                            "fullname": "Gaurav Kumar",
                            "name": "aavrug"
                        }
                    },
                    {
                        "comment": "Instead of having these in the form w/ hidden fields, maybe we could place them in the URL as we do in other places",
                        "commit": "7ed981c2ce9e66f1637cba224455d45c611b660a",
                        "date_created": "1458228080",
                        "edited_on": None,
                        "editor": None,
                        "filename": "pagure/ui/repo.py",
                        "id": 3454,
                        "line": 16,
                        "notification": False,
                        "parent": None,
                        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
                        "user": {
                            "fullname": "Pierre-YvesChibon",
                            "name": "pingou"
                        }
                    },
    {
        "comment": "repo_user can be None, that's no problem, we just need to make sure it isn't ``''`` (ie: empty string)",
        "commit": "7ed981c2ce9e66f1637cba224455d45c611b660a",
        "date_created": "1458228121",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3455,
        "line": 21,
        "notification": False,
        "parent": None,
        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Could/Should we check the value of ``watch``?",
        "commit": "7ed981c2ce9e66f1637cba224455d45c611b660a",
        "date_created": "1458228145",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3456,
        "line": 14,
        "notification": False,
        "parent": None,
        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Well this doesn't tell us much since the URL doesn't exists whether a ``foo`` project exists or not :)",
        "commit": "9038eddfefdff0cf827a27ee38e05b8f638b2fe3",
        "date_created": "1458228184",
        "edited_on": None,
        "editor": None,
        "filename": "tests/test_pagure_flask_ui_repo.py",
        "id": 3457,
        "line": 8,
        "notification": False,
        "parent": None,
        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "It redirects you, but you're not checking the output, you should ``follow_redirects=True`` and see what's in the HTML. Did the ``Watch`` flag changed? Was there a message flashed? Did it redirect you to the right page?",
        "commit": "9038eddfefdff0cf827a27ee38e05b8f638b2fe3",
        "date_created": "1458228321",
        "edited_on": None,
        "editor": None,
        "filename": "tests/test_pagure_flask_ui_repo.py",
        "id": 3458,
        "line": 46,
        "notification": False,
        "parent": None,
        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458237791",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3464,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Pull-Request has been rebased",
        "commit": None,
        "date_created": "1458239574",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3465,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458240388",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3466,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Check the ConfirmationForm ;-)",
        "commit": "95df7c1b30c8288333a2d5247ddbcc3df7abf2a0",
        "date_created": "1458240462",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/forms.py",
        "id": 3467,
        "line": 5,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Check the login method, there is a way to check that the previous_url is sane",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240532",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3468,
        "line": 11,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "repo cannot be None, otherwise we would have a 404 since the URL wouldn't hit here :)",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240573",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3469,
        "line": 16,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Let's make this ``str(watch)`` to be sure :)",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240600",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3470,
        "line": 19,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "No need for the ``if user``, just specify it, if ``user`` is None, it'll know what to do, check the code ;-)",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240664",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3471,
        "line": 25,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "``rollback()`` shouldn't be needed for a ``PagureException`` but it would for a sqlalchemy error",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240714",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3472,
        "line": 38,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Split this string over two lines? (same below?)",
        "commit": "3c839ba86dcd909f4bc23d2ab7d9bc87d4442315",
        "date_created": "1458240771",
        "edited_on": None,
        "editor": None,
        "filename": "tests/test_pagure_flask_ui_repo.py",
        "id": 3473,
        "line": 42,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458275019",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3477,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458275207",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3478,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458281234",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3479,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Whenever you get time just review this. I have taken so much time for this issue, so now thinking that if this will merge then I will move to the next issue.",
        "commit": None,
        "date_created": "1458298555",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3486,
        "line": None,
        "notification": False,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "This should be taken care of in ``notify.py`` no?",
        "commit": "e9cd199e6d8e4e684b6d9b7440b7d8d3296699e4",
        "date_created": "1458298756",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/lib/model.py",
        "id": 3487,
        "line": 35,
        "notification": False,
        "parent": None,
        "tree": "00a6f09a5e31549784c6f61c48723942e7c108cf",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "No that is for the user is watching or not for watch/Unwatch button.",
        "commit": "e9cd199e6d8e4e684b6d9b7440b7d8d3296699e4",
        "date_created": "1458298870",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/lib/model.py",
        "id": 3488,
        "line": 35,
        "notification": False,
        "parent": None,
        "tree": "00a6f09a5e31549784c6f61c48723942e7c108cf",
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Let's be consistent about our URL schemas:\r\n\r\nI propose:\r\n\r\n    @APP.route('/<repo>/settings/watch', methods=['POST'])\r\n    @APP.route('/fork/<username>/<repo>/settings/watch', methods=['POST'])",
        "commit": "2158eb3ee1cafc26cd2632244efa655dc42c224b",
        "date_created": "1458298899",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3489,
        "line": 13,
        "notification": False,
        "parent": None,
        "tree": "00a6f09a5e31549784c6f61c48723942e7c108cf",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Yes but we remove all the users not watching in ``notify.py`` if I read the code correctly",
        "commit": "e9cd199e6d8e4e684b6d9b7440b7d8d3296699e4",
        "date_created": "1458298950",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/lib/model.py",
        "id": 3490,
        "line": "35",
        "notification": False,
        "parent": None,
        "tree": "00a6f09a5e31549784c6f61c48723942e7c108cf",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    }
    ],
    "commit_start": "498572b754599022f358b370bf66fe5c8c10db58",
    "commit_stop": "d3b1f21fed867629d541ec1c1537c65d06851d7d",
    "date_created": "1458226010",
    "id": 843,
    "project": {
        "date_created": "1431549490",
        "description": "A git centered forge",
        "id": 10,
        "name": "pagure",
        "parent": None,
        "settings": {
            "Enforce_signed-off_commits_in_pull-request": False,
            "Minimum_score_to_merge_pull-request": -1,
            "Only_assignee_can_merge_pull-request": False,
            "Web-hooks": None,
            "always_merge": False,
            "issue_tracker": True,
            "project_documentation": True,
            "pull_requests": True
        },
        "tags": [
            "pagure",
            "fedmsg",
            "fedora-infra"
        ],
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    "remote_git": None,
    "repo_from": {
        "date_created": "1449051695",
        "description": "A git centered forge",
        "id": 278,
        "name": "pagure",
        "parent": {
            "date_created": "1431549490",
            "description": "A git centered forge",
            "id": 10,
            "name": "pagure",
            "parent": None,
            "settings": {
                "Enforce_signed-off_commits_in_pull-request": False,
                "Minimum_score_to_merge_pull-request": -1,
                "Only_assignee_can_merge_pull-request": False,
                "Web-hooks": None,
                "always_merge": False,
                "issue_tracker": True,
                "project_documentation": True,
                "pull_requests": True
            },
            "tags": [
                "pagure",
                "fedmsg",
                "fedora-infra"
            ],
            "user": {
                "fullname": "Pierre-YvesChibon",
                "name": "pingou"
            }
        },
        "settings": {
            "Enforce_signed-off_commits_in_pull-request": False,
            "Minimum_score_to_merge_pull-request": -1,
            "Only_assignee_can_merge_pull-request": False,
            "Web-hooks": None,
            "always_merge": False,
            "issue_tracker": True,
            "project_documentation": True,
            "pull_requests": True
        },
        "tags": [],
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    "status": "Open",
    "title": "Added watch feature.",
    "uid": "53e47f3c13874c9eb39675973e21e711",
    "updated_on": "1458298091",
    "user": {
        "fullname": "Gaurav Kumar",
        "name": "aavrug"
    }
    }
    },
    "msg_id": "2016-d07f4b41-9b92-43f5-9dd9-013298bf0f50",
    "timestamp": 1458298951.0,
    "topic": "io.pagure.prod.pagure.pull-request.comment.added"
    },
    {
        "i": 5,
        "msg": {
            "agent": "pingou",
            "pullrequest": {
                "assignee": None,
                "branch": "master",
                "branch_from": "master",
                "closed_at": None,
                "closed_by": None,
                "comments": [
                    {
                        "comment": "Missing indentation for the content of the form :)",
                        "commit": "08d5e7567a6b1495be7d1da47ae8f5f5e0d079af",
                        "date_created": "1458228021",
                        "edited_on": None,
                        "editor": None,
                        "filename": "pagure/templates/repo_master.html",
                        "id": 3452,
                        "line": 13,
                        "notification": False,
                        "parent": None,
                        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
                        "user": {
                            "fullname": "Pierre-YvesChibon",
                            "name": "pingou"
                        }
                    },
                    {
                        "comment": "Pull-Request has been updated",
                        "commit": None,
                        "date_created": "1458228047",
                        "edited_on": None,
                        "editor": None,
                        "filename": None,
                        "id": 3453,
                        "line": None,
                        "notification": True,
                        "parent": None,
                        "tree": None,
                        "user": {
                            "fullname": "Gaurav Kumar",
                            "name": "aavrug"
                        }
                    },
                    {
                        "comment": "Instead of having these in the form w/ hidden fields, maybe we could place them in the URL as we do in other places",
                        "commit": "7ed981c2ce9e66f1637cba224455d45c611b660a",
                        "date_created": "1458228080",
                        "edited_on": None,
                        "editor": None,
                        "filename": "pagure/ui/repo.py",
                        "id": 3454,
                        "line": 16,
                        "notification": False,
                        "parent": None,
                        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
                        "user": {
                            "fullname": "Pierre-YvesChibon",
                            "name": "pingou"
                        }
                    },
    {
        "comment": "repo_user can be None, that's no problem, we just need to make sure it isn't ``''`` (ie: empty string)",
        "commit": "7ed981c2ce9e66f1637cba224455d45c611b660a",
        "date_created": "1458228121",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3455,
        "line": 21,
        "notification": False,
        "parent": None,
        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Could/Should we check the value of ``watch``?",
        "commit": "7ed981c2ce9e66f1637cba224455d45c611b660a",
        "date_created": "1458228145",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3456,
        "line": 14,
        "notification": False,
        "parent": None,
        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Well this doesn't tell us much since the URL doesn't exists whether a ``foo`` project exists or not :)",
        "commit": "9038eddfefdff0cf827a27ee38e05b8f638b2fe3",
        "date_created": "1458228184",
        "edited_on": None,
        "editor": None,
        "filename": "tests/test_pagure_flask_ui_repo.py",
        "id": 3457,
        "line": 8,
        "notification": False,
        "parent": None,
        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "It redirects you, but you're not checking the output, you should ``follow_redirects=True`` and see what's in the HTML. Did the ``Watch`` flag changed? Was there a message flashed? Did it redirect you to the right page?",
        "commit": "9038eddfefdff0cf827a27ee38e05b8f638b2fe3",
        "date_created": "1458228321",
        "edited_on": None,
        "editor": None,
        "filename": "tests/test_pagure_flask_ui_repo.py",
        "id": 3458,
        "line": 46,
        "notification": False,
        "parent": None,
        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458237791",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3464,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Pull-Request has been rebased",
        "commit": None,
        "date_created": "1458239574",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3465,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458240388",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3466,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Check the ConfirmationForm ;-)",
        "commit": "95df7c1b30c8288333a2d5247ddbcc3df7abf2a0",
        "date_created": "1458240462",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/forms.py",
        "id": 3467,
        "line": 5,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Check the login method, there is a way to check that the previous_url is sane",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240532",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3468,
        "line": 11,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "repo cannot be None, otherwise we would have a 404 since the URL wouldn't hit here :)",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240573",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3469,
        "line": 16,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Let's make this ``str(watch)`` to be sure :)",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240600",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3470,
        "line": 19,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "No need for the ``if user``, just specify it, if ``user`` is None, it'll know what to do, check the code ;-)",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240664",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3471,
        "line": 25,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "``rollback()`` shouldn't be needed for a ``PagureException`` but it would for a sqlalchemy error",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240714",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3472,
        "line": 38,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Split this string over two lines? (same below?)",
        "commit": "3c839ba86dcd909f4bc23d2ab7d9bc87d4442315",
        "date_created": "1458240771",
        "edited_on": None,
        "editor": None,
        "filename": "tests/test_pagure_flask_ui_repo.py",
        "id": 3473,
        "line": 42,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458275019",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3477,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458275207",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3478,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458281234",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3479,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Whenever you get time just review this. I have taken so much time for this issue, so now thinking that if this will merge then I will move to the next issue.",
        "commit": None,
        "date_created": "1458298555",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3486,
        "line": None,
        "notification": False,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "This should be taken care of in ``notify.py`` no?",
        "commit": "e9cd199e6d8e4e684b6d9b7440b7d8d3296699e4",
        "date_created": "1458298756",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/lib/model.py",
        "id": 3487,
        "line": 35,
        "notification": False,
        "parent": None,
        "tree": "00a6f09a5e31549784c6f61c48723942e7c108cf",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "No that is for the user is watching or not for watch/Unwatch button.",
        "commit": "e9cd199e6d8e4e684b6d9b7440b7d8d3296699e4",
        "date_created": "1458298870",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/lib/model.py",
        "id": 3488,
        "line": 35,
        "notification": False,
        "parent": None,
        "tree": "00a6f09a5e31549784c6f61c48723942e7c108cf",
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Let's be consistent about our URL schemas:\r\n\r\nI propose:\r\n\r\n    @APP.route('/<repo>/settings/watch', methods=['POST'])\r\n    @APP.route('/fork/<username>/<repo>/settings/watch', methods=['POST'])",
        "commit": "2158eb3ee1cafc26cd2632244efa655dc42c224b",
        "date_created": "1458298899",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3489,
        "line": "13",
        "notification": False,
        "parent": None,
        "tree": "00a6f09a5e31549784c6f61c48723942e7c108cf",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    }
    ],
    "commit_start": "498572b754599022f358b370bf66fe5c8c10db58",
    "commit_stop": "d3b1f21fed867629d541ec1c1537c65d06851d7d",
    "date_created": "1458226010",
    "id": 843,
    "project": {
        "date_created": "1431549490",
        "description": "A git centered forge",
        "id": 10,
        "name": "pagure",
        "parent": None,
        "settings": {
            "Enforce_signed-off_commits_in_pull-request": False,
            "Minimum_score_to_merge_pull-request": -1,
            "Only_assignee_can_merge_pull-request": False,
            "Web-hooks": None,
            "always_merge": False,
            "issue_tracker": True,
            "project_documentation": True,
            "pull_requests": True
        },
        "tags": [
            "pagure",
            "fedmsg",
            "fedora-infra"
        ],
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    "remote_git": None,
    "repo_from": {
        "date_created": "1449051695",
        "description": "A git centered forge",
        "id": 278,
        "name": "pagure",
        "parent": {
            "date_created": "1431549490",
            "description": "A git centered forge",
            "id": 10,
            "name": "pagure",
            "parent": None,
            "settings": {
                "Enforce_signed-off_commits_in_pull-request": False,
                "Minimum_score_to_merge_pull-request": -1,
                "Only_assignee_can_merge_pull-request": False,
                "Web-hooks": None,
                "always_merge": False,
                "issue_tracker": True,
                "project_documentation": True,
                "pull_requests": True
            },
            "tags": [
                "pagure",
                "fedmsg",
                "fedora-infra"
            ],
            "user": {
                "fullname": "Pierre-YvesChibon",
                "name": "pingou"
            }
        },
        "settings": {
            "Enforce_signed-off_commits_in_pull-request": False,
            "Minimum_score_to_merge_pull-request": -1,
            "Only_assignee_can_merge_pull-request": False,
            "Web-hooks": None,
            "always_merge": False,
            "issue_tracker": True,
            "project_documentation": True,
            "pull_requests": True
        },
        "tags": [],
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    "status": "Open",
    "title": "Added watch feature.",
    "uid": "53e47f3c13874c9eb39675973e21e711",
    "updated_on": "1458298091",
    "user": {
        "fullname": "Gaurav Kumar",
        "name": "aavrug"
    }
    }
    },
    "msg_id": "2016-fd909fc4-180a-4f4d-a68e-27411ebcad75",
    "timestamp": 1458298899.0,
    "topic": "io.pagure.prod.pagure.pull-request.comment.added"
    },
    {
        "i": 1,
        "msg": {
            "agent": "aavrug",
            "pullrequest": {
                "assignee": None,
                "branch": "master",
                "branch_from": "master",
                "closed_at": None,
                "closed_by": None,
                "comments": [
                    {
                        "comment": "Missing indentation for the content of the form :)",
                        "commit": "08d5e7567a6b1495be7d1da47ae8f5f5e0d079af",
                        "date_created": "1458228021",
                        "edited_on": None,
                        "editor": None,
                        "filename": "pagure/templates/repo_master.html",
                        "id": 3452,
                        "line": 13,
                        "notification": False,
                        "parent": None,
                        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
                        "user": {
                            "fullname": "Pierre-YvesChibon",
                            "name": "pingou"
                        }
                    },
                    {
                        "comment": "Pull-Request has been updated",
                        "commit": None,
                        "date_created": "1458228047",
                        "edited_on": None,
                        "editor": None,
                        "filename": None,
                        "id": 3453,
                        "line": None,
                        "notification": True,
                        "parent": None,
                        "tree": None,
                        "user": {
                            "fullname": "Gaurav Kumar",
                            "name": "aavrug"
                        }
                    },
                    {
                        "comment": "Instead of having these in the form w/ hidden fields, maybe we could place them in the URL as we do in other places",
                        "commit": "7ed981c2ce9e66f1637cba224455d45c611b660a",
                        "date_created": "1458228080",
                        "edited_on": None,
                        "editor": None,
                        "filename": "pagure/ui/repo.py",
                        "id": 3454,
                        "line": 16,
                        "notification": False,
                        "parent": None,
                        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
                        "user": {
                            "fullname": "Pierre-YvesChibon",
                            "name": "pingou"
                        }
                    },
    {
        "comment": "repo_user can be None, that's no problem, we just need to make sure it isn't ``''`` (ie: empty string)",
        "commit": "7ed981c2ce9e66f1637cba224455d45c611b660a",
        "date_created": "1458228121",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3455,
        "line": 21,
        "notification": False,
        "parent": None,
        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Could/Should we check the value of ``watch``?",
        "commit": "7ed981c2ce9e66f1637cba224455d45c611b660a",
        "date_created": "1458228145",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3456,
        "line": 14,
        "notification": False,
        "parent": None,
        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Well this doesn't tell us much since the URL doesn't exists whether a ``foo`` project exists or not :)",
        "commit": "9038eddfefdff0cf827a27ee38e05b8f638b2fe3",
        "date_created": "1458228184",
        "edited_on": None,
        "editor": None,
        "filename": "tests/test_pagure_flask_ui_repo.py",
        "id": 3457,
        "line": 8,
        "notification": False,
        "parent": None,
        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "It redirects you, but you're not checking the output, you should ``follow_redirects=True`` and see what's in the HTML. Did the ``Watch`` flag changed? Was there a message flashed? Did it redirect you to the right page?",
        "commit": "9038eddfefdff0cf827a27ee38e05b8f638b2fe3",
        "date_created": "1458228321",
        "edited_on": None,
        "editor": None,
        "filename": "tests/test_pagure_flask_ui_repo.py",
        "id": 3458,
        "line": 46,
        "notification": False,
        "parent": None,
        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458237791",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3464,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Pull-Request has been rebased",
        "commit": None,
        "date_created": "1458239574",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3465,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458240388",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3466,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Check the ConfirmationForm ;-)",
        "commit": "95df7c1b30c8288333a2d5247ddbcc3df7abf2a0",
        "date_created": "1458240462",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/forms.py",
        "id": 3467,
        "line": 5,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Check the login method, there is a way to check that the previous_url is sane",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240532",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3468,
        "line": 11,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "repo cannot be None, otherwise we would have a 404 since the URL wouldn't hit here :)",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240573",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3469,
        "line": 16,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Let's make this ``str(watch)`` to be sure :)",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240600",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3470,
        "line": 19,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "No need for the ``if user``, just specify it, if ``user`` is None, it'll know what to do, check the code ;-)",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240664",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3471,
        "line": 25,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "``rollback()`` shouldn't be needed for a ``PagureException`` but it would for a sqlalchemy error",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240714",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3472,
        "line": 38,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Split this string over two lines? (same below?)",
        "commit": "3c839ba86dcd909f4bc23d2ab7d9bc87d4442315",
        "date_created": "1458240771",
        "edited_on": None,
        "editor": None,
        "filename": "tests/test_pagure_flask_ui_repo.py",
        "id": 3473,
        "line": 42,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458275019",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3477,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458275207",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3478,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458281234",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3479,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Whenever you get time just review this. I have taken so much time for this issue, so now thinking that if this will merge then I will move to the next issue.",
        "commit": None,
        "date_created": "1458298555",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3486,
        "line": None,
        "notification": False,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "This should be taken care of in ``notify.py`` no?",
        "commit": "e9cd199e6d8e4e684b6d9b7440b7d8d3296699e4",
        "date_created": "1458298756",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/lib/model.py",
        "id": 3487,
        "line": 35,
        "notification": False,
        "parent": None,
        "tree": "00a6f09a5e31549784c6f61c48723942e7c108cf",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "No that is for the user is watching or not for watch/Unwatch button.",
        "commit": "e9cd199e6d8e4e684b6d9b7440b7d8d3296699e4",
        "date_created": "1458298870",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/lib/model.py",
        "id": 3488,
        "line": "35",
        "notification": False,
        "parent": None,
        "tree": "00a6f09a5e31549784c6f61c48723942e7c108cf",
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    }
    ],
    "commit_start": "498572b754599022f358b370bf66fe5c8c10db58",
    "commit_stop": "d3b1f21fed867629d541ec1c1537c65d06851d7d",
    "date_created": "1458226010",
    "id": 843,
    "project": {
        "date_created": "1431549490",
        "description": "A git centered forge",
        "id": 10,
        "name": "pagure",
        "parent": None,
        "settings": {
            "Enforce_signed-off_commits_in_pull-request": False,
            "Minimum_score_to_merge_pull-request": -1,
            "Only_assignee_can_merge_pull-request": False,
            "Web-hooks": None,
            "always_merge": False,
            "issue_tracker": True,
            "project_documentation": True,
            "pull_requests": True
        },
        "tags": [
            "pagure",
            "fedmsg",
            "fedora-infra"
        ],
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    "remote_git": None,
    "repo_from": {
        "date_created": "1449051695",
        "description": "A git centered forge",
        "id": 278,
        "name": "pagure",
        "parent": {
            "date_created": "1431549490",
            "description": "A git centered forge",
            "id": 10,
            "name": "pagure",
            "parent": None,
            "settings": {
                "Enforce_signed-off_commits_in_pull-request": False,
                "Minimum_score_to_merge_pull-request": -1,
                "Only_assignee_can_merge_pull-request": False,
                "Web-hooks": None,
                "always_merge": False,
                "issue_tracker": True,
                "project_documentation": True,
                "pull_requests": True
            },
            "tags": [
                "pagure",
                "fedmsg",
                "fedora-infra"
            ],
            "user": {
                "fullname": "Pierre-YvesChibon",
                "name": "pingou"
            }
        },
        "settings": {
            "Enforce_signed-off_commits_in_pull-request": False,
            "Minimum_score_to_merge_pull-request": -1,
            "Only_assignee_can_merge_pull-request": False,
            "Web-hooks": None,
            "always_merge": False,
            "issue_tracker": True,
            "project_documentation": True,
            "pull_requests": True
        },
        "tags": [],
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    "status": "Open",
    "title": "Added watch feature.",
    "uid": "53e47f3c13874c9eb39675973e21e711",
    "updated_on": "1458298091",
    "user": {
        "fullname": "Gaurav Kumar",
        "name": "aavrug"
    }
    }
    },
    "msg_id": "2016-9e63a009-4e66-480c-8eca-ab032cff462b",
    "timestamp": 1458298872.0,
    "topic": "io.pagure.prod.pagure.pull-request.comment.added"
    },
    {
        "i": 3,
        "msg": {
            "agent": "pingou",
            "pullrequest": {
                "assignee": None,
                "branch": "master",
                "branch_from": "master",
                "closed_at": None,
                "closed_by": None,
                "comments": [
                    {
                        "comment": "Missing indentation for the content of the form :)",
                        "commit": "08d5e7567a6b1495be7d1da47ae8f5f5e0d079af",
                        "date_created": "1458228021",
                        "edited_on": None,
                        "editor": None,
                        "filename": "pagure/templates/repo_master.html",
                        "id": 3452,
                        "line": 13,
                        "notification": False,
                        "parent": None,
                        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
                        "user": {
                            "fullname": "Pierre-YvesChibon",
                            "name": "pingou"
                        }
                    },
                    {
                        "comment": "Pull-Request has been updated",
                        "commit": None,
                        "date_created": "1458228047",
                        "edited_on": None,
                        "editor": None,
                        "filename": None,
                        "id": 3453,
                        "line": None,
                        "notification": True,
                        "parent": None,
                        "tree": None,
                        "user": {
                            "fullname": "Gaurav Kumar",
                            "name": "aavrug"
                        }
                    },
                    {
                        "comment": "Instead of having these in the form w/ hidden fields, maybe we could place them in the URL as we do in other places",
                        "commit": "7ed981c2ce9e66f1637cba224455d45c611b660a",
                        "date_created": "1458228080",
                        "edited_on": None,
                        "editor": None,
                        "filename": "pagure/ui/repo.py",
                        "id": 3454,
                        "line": 16,
                        "notification": False,
                        "parent": None,
                        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
                        "user": {
                            "fullname": "Pierre-YvesChibon",
                            "name": "pingou"
                        }
                    },
    {
        "comment": "repo_user can be None, that's no problem, we just need to make sure it isn't ``''`` (ie: empty string)",
        "commit": "7ed981c2ce9e66f1637cba224455d45c611b660a",
        "date_created": "1458228121",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3455,
        "line": 21,
        "notification": False,
        "parent": None,
        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Could/Should we check the value of ``watch``?",
        "commit": "7ed981c2ce9e66f1637cba224455d45c611b660a",
        "date_created": "1458228145",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3456,
        "line": 14,
        "notification": False,
        "parent": None,
        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Well this doesn't tell us much since the URL doesn't exists whether a ``foo`` project exists or not :)",
        "commit": "9038eddfefdff0cf827a27ee38e05b8f638b2fe3",
        "date_created": "1458228184",
        "edited_on": None,
        "editor": None,
        "filename": "tests/test_pagure_flask_ui_repo.py",
        "id": 3457,
        "line": 8,
        "notification": False,
        "parent": None,
        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "It redirects you, but you're not checking the output, you should ``follow_redirects=True`` and see what's in the HTML. Did the ``Watch`` flag changed? Was there a message flashed? Did it redirect you to the right page?",
        "commit": "9038eddfefdff0cf827a27ee38e05b8f638b2fe3",
        "date_created": "1458228321",
        "edited_on": None,
        "editor": None,
        "filename": "tests/test_pagure_flask_ui_repo.py",
        "id": 3458,
        "line": 46,
        "notification": False,
        "parent": None,
        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458237791",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3464,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Pull-Request has been rebased",
        "commit": None,
        "date_created": "1458239574",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3465,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458240388",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3466,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Check the ConfirmationForm ;-)",
        "commit": "95df7c1b30c8288333a2d5247ddbcc3df7abf2a0",
        "date_created": "1458240462",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/forms.py",
        "id": 3467,
        "line": 5,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Check the login method, there is a way to check that the previous_url is sane",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240532",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3468,
        "line": 11,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "repo cannot be None, otherwise we would have a 404 since the URL wouldn't hit here :)",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240573",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3469,
        "line": 16,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Let's make this ``str(watch)`` to be sure :)",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240600",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3470,
        "line": 19,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "No need for the ``if user``, just specify it, if ``user`` is None, it'll know what to do, check the code ;-)",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240664",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3471,
        "line": 25,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "``rollback()`` shouldn't be needed for a ``PagureException`` but it would for a sqlalchemy error",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240714",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3472,
        "line": 38,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Split this string over two lines? (same below?)",
        "commit": "3c839ba86dcd909f4bc23d2ab7d9bc87d4442315",
        "date_created": "1458240771",
        "edited_on": None,
        "editor": None,
        "filename": "tests/test_pagure_flask_ui_repo.py",
        "id": 3473,
        "line": 42,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458275019",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3477,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458275207",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3478,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458281234",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3479,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Whenever you get time just review this. I have taken so much time for this issue, so now thinking that if this will merge then I will move to the next issue.",
        "commit": None,
        "date_created": "1458298555",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3486,
        "line": None,
        "notification": False,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "This should be taken care of in ``notify.py`` no?",
        "commit": "e9cd199e6d8e4e684b6d9b7440b7d8d3296699e4",
        "date_created": "1458298756",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/lib/model.py",
        "id": 3487,
        "line": "35",
        "notification": False,
        "parent": None,
        "tree": "00a6f09a5e31549784c6f61c48723942e7c108cf",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    }
    ],
    "commit_start": "498572b754599022f358b370bf66fe5c8c10db58",
    "commit_stop": "d3b1f21fed867629d541ec1c1537c65d06851d7d",
    "date_created": "1458226010",
    "id": 843,
    "project": {
        "date_created": "1431549490",
        "description": "A git centered forge",
        "id": 10,
        "name": "pagure",
        "parent": None,
        "settings": {
            "Enforce_signed-off_commits_in_pull-request": False,
            "Minimum_score_to_merge_pull-request": -1,
            "Only_assignee_can_merge_pull-request": False,
            "Web-hooks": None,
            "always_merge": False,
            "issue_tracker": True,
            "project_documentation": True,
            "pull_requests": True
        },
        "tags": [
            "pagure",
            "fedmsg",
            "fedora-infra"
        ],
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    "remote_git": None,
    "repo_from": {
        "date_created": "1449051695",
        "description": "A git centered forge",
        "id": 278,
        "name": "pagure",
        "parent": {
            "date_created": "1431549490",
            "description": "A git centered forge",
            "id": 10,
            "name": "pagure",
            "parent": None,
            "settings": {
                "Enforce_signed-off_commits_in_pull-request": False,
                "Minimum_score_to_merge_pull-request": -1,
                "Only_assignee_can_merge_pull-request": False,
                "Web-hooks": None,
                "always_merge": False,
                "issue_tracker": True,
                "project_documentation": True,
                "pull_requests": True
            },
            "tags": [
                "pagure",
                "fedmsg",
                "fedora-infra"
            ],
            "user": {
                "fullname": "Pierre-YvesChibon",
                "name": "pingou"
            }
        },
        "settings": {
            "Enforce_signed-off_commits_in_pull-request": False,
            "Minimum_score_to_merge_pull-request": -1,
            "Only_assignee_can_merge_pull-request": False,
            "Web-hooks": None,
            "always_merge": False,
            "issue_tracker": True,
            "project_documentation": True,
            "pull_requests": True
        },
        "tags": [],
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    "status": "Open",
    "title": "Added watch feature.",
    "uid": "53e47f3c13874c9eb39675973e21e711",
    "updated_on": "1458298091",
    "user": {
        "fullname": "Gaurav Kumar",
        "name": "aavrug"
    }
    }
    },
    "msg_id": "2016-b60b2056-4228-404e-bae0-92b194a81fe9",
    "timestamp": 1458298757.0,
    "topic": "io.pagure.prod.pagure.pull-request.comment.added"
    },
    {
        "i": 4,
        "msg": {
            "agent": "aavrug",
            "pullrequest": {
                "assignee": None,
                "branch": "master",
                "branch_from": "master",
                "closed_at": None,
                "closed_by": None,
                "comments": [
                    {
                        "comment": "Missing indentation for the content of the form :)",
                        "commit": "08d5e7567a6b1495be7d1da47ae8f5f5e0d079af",
                        "date_created": "1458228021",
                        "edited_on": None,
                        "editor": None,
                        "filename": "pagure/templates/repo_master.html",
                        "id": 3452,
                        "line": 13,
                        "notification": False,
                        "parent": None,
                        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
                        "user": {
                            "fullname": "Pierre-YvesChibon",
                            "name": "pingou"
                        }
                    },
                    {
                        "comment": "Pull-Request has been updated",
                        "commit": None,
                        "date_created": "1458228047",
                        "edited_on": None,
                        "editor": None,
                        "filename": None,
                        "id": 3453,
                        "line": None,
                        "notification": True,
                        "parent": None,
                        "tree": None,
                        "user": {
                            "fullname": "Gaurav Kumar",
                            "name": "aavrug"
                        }
                    },
                    {
                        "comment": "Instead of having these in the form w/ hidden fields, maybe we could place them in the URL as we do in other places",
                        "commit": "7ed981c2ce9e66f1637cba224455d45c611b660a",
                        "date_created": "1458228080",
                        "edited_on": None,
                        "editor": None,
                        "filename": "pagure/ui/repo.py",
                        "id": 3454,
                        "line": 16,
                        "notification": False,
                        "parent": None,
                        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
                        "user": {
                            "fullname": "Pierre-YvesChibon",
                            "name": "pingou"
                        }
                    },
    {
        "comment": "repo_user can be None, that's no problem, we just need to make sure it isn't ``''`` (ie: empty string)",
        "commit": "7ed981c2ce9e66f1637cba224455d45c611b660a",
        "date_created": "1458228121",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3455,
        "line": 21,
        "notification": False,
        "parent": None,
        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Could/Should we check the value of ``watch``?",
        "commit": "7ed981c2ce9e66f1637cba224455d45c611b660a",
        "date_created": "1458228145",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3456,
        "line": 14,
        "notification": False,
        "parent": None,
        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Well this doesn't tell us much since the URL doesn't exists whether a ``foo`` project exists or not :)",
        "commit": "9038eddfefdff0cf827a27ee38e05b8f638b2fe3",
        "date_created": "1458228184",
        "edited_on": None,
        "editor": None,
        "filename": "tests/test_pagure_flask_ui_repo.py",
        "id": 3457,
        "line": 8,
        "notification": False,
        "parent": None,
        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "It redirects you, but you're not checking the output, you should ``follow_redirects=True`` and see what's in the HTML. Did the ``Watch`` flag changed? Was there a message flashed? Did it redirect you to the right page?",
        "commit": "9038eddfefdff0cf827a27ee38e05b8f638b2fe3",
        "date_created": "1458228321",
        "edited_on": None,
        "editor": None,
        "filename": "tests/test_pagure_flask_ui_repo.py",
        "id": 3458,
        "line": 46,
        "notification": False,
        "parent": None,
        "tree": "a02e041005632948452b5e55b7257543cb496dbb",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458237791",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3464,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Pull-Request has been rebased",
        "commit": None,
        "date_created": "1458239574",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3465,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458240388",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3466,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Check the ConfirmationForm ;-)",
        "commit": "95df7c1b30c8288333a2d5247ddbcc3df7abf2a0",
        "date_created": "1458240462",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/forms.py",
        "id": 3467,
        "line": 5,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Check the login method, there is a way to check that the previous_url is sane",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240532",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3468,
        "line": 11,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "repo cannot be None, otherwise we would have a 404 since the URL wouldn't hit here :)",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240573",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3469,
        "line": 16,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Let's make this ``str(watch)`` to be sure :)",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240600",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3470,
        "line": 19,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "No need for the ``if user``, just specify it, if ``user`` is None, it'll know what to do, check the code ;-)",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240664",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3471,
        "line": 25,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "``rollback()`` shouldn't be needed for a ``PagureException`` but it would for a sqlalchemy error",
        "commit": "057e1ff0685bfdfd71f7525663c6b7da2ce11373",
        "date_created": "1458240714",
        "edited_on": None,
        "editor": None,
        "filename": "pagure/ui/repo.py",
        "id": 3472,
        "line": 38,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Split this string over two lines? (same below?)",
        "commit": "3c839ba86dcd909f4bc23d2ab7d9bc87d4442315",
        "date_created": "1458240771",
        "edited_on": None,
        "editor": None,
        "filename": "tests/test_pagure_flask_ui_repo.py",
        "id": 3473,
        "line": 42,
        "notification": False,
        "parent": None,
        "tree": "389966f3da0423bc76d6198e7283266d47a28c1c",
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458275019",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3477,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458275207",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3478,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Pull-Request has been updated",
        "commit": None,
        "date_created": "1458281234",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3479,
        "line": None,
        "notification": True,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    {
        "comment": "Whenever you get time just review this. I have taken so much time for this issue, so now thinking that if this will merge then I will move to the next issue.",
        "commit": None,
        "date_created": "1458298555",
        "edited_on": None,
        "editor": None,
        "filename": None,
        "id": 3486,
        "line": None,
        "notification": False,
        "parent": None,
        "tree": None,
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    }
    ],
    "commit_start": "498572b754599022f358b370bf66fe5c8c10db58",
    "commit_stop": "d3b1f21fed867629d541ec1c1537c65d06851d7d",
    "date_created": "1458226010",
    "id": 843,
    "project": {
        "date_created": "1431549490",
        "description": "A git centered forge",
        "id": 10,
        "name": "pagure",
        "parent": None,
        "settings": {
            "Enforce_signed-off_commits_in_pull-request": False,
            "Minimum_score_to_merge_pull-request": -1,
            "Only_assignee_can_merge_pull-request": False,
            "Web-hooks": None,
            "always_merge": False,
            "issue_tracker": True,
            "project_documentation": True,
            "pull_requests": True
        },
        "tags": [
            "pagure",
            "fedmsg",
            "fedora-infra"
        ],
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    "remote_git": None,
    "repo_from": {
        "date_created": "1449051695",
        "description": "A git centered forge",
        "id": 278,
        "name": "pagure",
        "parent": {
            "date_created": "1431549490",
            "description": "A git centered forge",
            "id": 10,
            "name": "pagure",
            "parent": None,
            "settings": {
                "Enforce_signed-off_commits_in_pull-request": False,
                "Minimum_score_to_merge_pull-request": -1,
                "Only_assignee_can_merge_pull-request": False,
                "Web-hooks": None,
                "always_merge": False,
                "issue_tracker": True,
                "project_documentation": True,
                "pull_requests": True
            },
            "tags": [
                "pagure",
                "fedmsg",
                "fedora-infra"
            ],
            "user": {
                "fullname": "Pierre-YvesChibon",
                "name": "pingou"
            }
        },
        "settings": {
            "Enforce_signed-off_commits_in_pull-request": False,
            "Minimum_score_to_merge_pull-request": -1,
            "Only_assignee_can_merge_pull-request": False,
            "Web-hooks": None,
            "always_merge": False,
            "issue_tracker": True,
            "project_documentation": True,
            "pull_requests": True
        },
        "tags": [],
        "user": {
            "fullname": "Gaurav Kumar",
            "name": "aavrug"
        }
    },
    "status": "Open",
    "title": "Added watch feature.",
    "uid": "53e47f3c13874c9eb39675973e21e711",
    "updated_on": "1458298091",
    "user": {
        "fullname": "Gaurav Kumar",
        "name": "aavrug"
    }
    }
    },
    "msg_id": "2016-78a49276-f52d-45f1-aacb-6f9783338a2d",
    "timestamp": 1458298555.0,
    "topic": "io.pagure.prod.pagure.pull-request.comment.added"
    },
    {
        "i": 3,
        "msg": {
            "agent": "pingou",
            "issue": {
                "assignee": None,
                "blocks": [],
                "comments": [
                    {
                        "comment": "Hmmm, i can reproduce this one on pagure.io, but not in my local instance. It may have been fixed . Or there is some config difference between the two :(\r\n\r\n",
                        "date_created": "1458032385",
                        "edited_on": None,
                        "editor": None,
                        "id": 1950,
                        "parent": None,
                        "user": {
                            "fullname": "ryan lerch",
                            "name": "ryanlerch"
                        }
                    },
                    {
                        "comment": "I can't replicate in my local instance either. I think the difference in configuration is that locally the form gets submitted with regular post and redirect, so the page reloads and form clears. On pagure.io, the comments are submitted without page reload.",
                        "date_created": "1458295390",
                        "edited_on": None,
                        "editor": None,
                        "id": 2034,
                        "parent": None,
                        "user": {
                            "fullname": "Lubomír Sedlář",
                            "name": "lsedlar"
                        }
                    },
                    {
                        "comment": "You can run the SSE server by using\r\n\r\n    PAGURE_CONFIG=../config PYTHONPATH=. python ev-server/pagure-stream-server.py\r\n",
                        "date_created": "1458297874",
                        "edited_on": None,
                        "editor": None,
                        "id": 2035,
                        "parent": None,
                        "user": {
                            "fullname": "Pierre-YvesChibon",
                            "name": "pingou"
                        }
                    },
                    {
                        "comment": "I found the bug and the fix :)",
                        "date_created": "1458298137",
                        "edited_on": None,
                        "editor": None,
                        "id": 2036,
                        "parent": None,
                        "user": {
                            "fullname": "Pierre-YvesChibon",
                            "name": "pingou"
                        }
                    }
                ],
    "content": "Steps to reproduce:\r\n\r\n1. On issue page, write some text in comment input.\r\n2. Display preview\r\n3. Hit *Update issue* button\r\n\r\nThe comment gets added, but the preview is still displayed the exact same way. I would expect the view to switch back to clear textarea.",
    "date_created": "1458031264",
    "depends": [],
    "id": 833,
    "private": False,
    "status": "Open",
    "tags": [],
    "title": "Submitting issue comment does not clear preview",
    "user": {
        "fullname": "Lubomír Sedlář",
        "name": "lsedlar"
    }
    },
    "project": {
        "date_created": "1431549490",
        "description": "A git centered forge",
        "id": 10,
        "name": "pagure",
        "parent": None,
        "settings": {
            "Enforce_signed-off_commits_in_pull-request": False,
            "Minimum_score_to_merge_pull-request": -1,
            "Only_assignee_can_merge_pull-request": False,
            "Web-hooks": None,
            "always_merge": False,
            "issue_tracker": True,
            "project_documentation": True,
            "pull_requests": True
        },
        "tags": [
            "pagure",
            "fedmsg",
            "fedora-infra"
        ],
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    }
    },
    "msg_id": "2016-59add39c-492c-4cbe-a5ff-94951c626733",
    "timestamp": 1458298137.0,
    "topic": "io.pagure.prod.pagure.issue.comment.added"
    },
    {
        "i": 4,
        "msg": {
            "agent": "pingou",
            "issue": {
                "assignee": None,
                "blocks": [],
                "comments": [
                    {
                        "comment": "Hmmm, i can reproduce this one on pagure.io, but not in my local instance. It may have been fixed . Or there is some config difference between the two :(\r\n\r\n",
                        "date_created": "1458032385",
                        "edited_on": None,
                        "editor": None,
                        "id": 1950,
                        "parent": None,
                        "user": {
                            "fullname": "ryan lerch",
                            "name": "ryanlerch"
                        }
                    },
                    {
                        "comment": "I can't replicate in my local instance either. I think the difference in configuration is that locally the form gets submitted with regular post and redirect, so the page reloads and form clears. On pagure.io, the comments are submitted without page reload.",
                        "date_created": "1458295390",
                        "edited_on": None,
                        "editor": None,
                        "id": 2034,
                        "parent": None,
                        "user": {
                            "fullname": "Lubomír Sedlář",
                            "name": "lsedlar"
                        }
                    },
                    {
                        "comment": "You can run the SSE server by using\r\n\r\n    PAGURE_CONFIG=../config PYTHONPATH=. python ev-server/pagure-stream-server.py\r\n",
                        "date_created": "1458297874",
                        "edited_on": None,
                        "editor": None,
                        "id": 2035,
                        "parent": None,
                        "user": {
                            "fullname": "Pierre-YvesChibon",
                            "name": "pingou"
                        }
                    }
                ],
                "content": "Steps to reproduce:\r\n\r\n1. On issue page, write some text in comment input.\r\n2. Display preview\r\n3. Hit *Update issue* button\r\n\r\nThe comment gets added, but the preview is still displayed the exact same way. I would expect the view to switch back to clear textarea.",
                "date_created": "1458031264",
                "depends": [],
                "id": 833,
                "private": False,
                "status": "Open",
                "tags": [],
                "title": "Submitting issue comment does not clear preview",
                "user": {
                    "fullname": "Lubomír Sedlář",
                    "name": "lsedlar"
                }
    },
    "project": {
        "date_created": "1431549490",
        "description": "A git centered forge",
        "id": 10,
        "name": "pagure",
        "parent": None,
        "settings": {
            "Enforce_signed-off_commits_in_pull-request": False,
            "Minimum_score_to_merge_pull-request": -1,
            "Only_assignee_can_merge_pull-request": False,
            "Web-hooks": None,
            "always_merge": False,
            "issue_tracker": True,
            "project_documentation": True,
            "pull_requests": True
        },
        "tags": [
            "pagure",
            "fedmsg",
            "fedora-infra"
        ],
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    }
    },
    "msg_id": "2016-c8ff3789-462f-4346-abd5-cac4761933d1",
    "timestamp": 1458297874.0,
    "topic": "io.pagure.prod.pagure.issue.comment.added"
    },
    {
        "i": 2,
        "msg": {
            "agent": "pingou",
            "pullrequest": {
                "assignee": None,
                "branch": "master",
                "branch_from": "scroll-to-highlighted",
                "closed_at": "1458297187",
                "closed_by": None,
                "comments": [
                    {
                        "comment": "Visit [a page with line range highlighted](https://pagure.io/pagure/blob/master/f/pagure/__init__.py#_93-98), and the browser will not scroll to it automatically. This patch should fix that.\r\n\r\nIf you don't like the animation, replace that line with `window.scroll(0, offset);`.",
                        "commit": None,
                        "date_created": "1458294982",
                        "edited_on": None,
                        "editor": None,
                        "filename": None,
                        "id": 3482,
                        "line": None,
                        "notification": False,
                        "parent": None,
                        "tree": None,
                        "user": {
                            "fullname": "Lubomír Sedlář",
                            "name": "lsedlar"
                        }
                    },
                    {
                        "comment": "I like the idea but it seems it doesn't work for me if the lines selected are not part of the first file (in my local test I selected lines in the 5th files).",
                        "commit": None,
                        "date_created": "1458297107",
                        "edited_on": None,
                        "editor": None,
                        "filename": None,
                        "id": 3483,
                        "line": None,
                        "notification": False,
                        "parent": None,
                        "tree": None,
                        "user": {
                            "fullname": "Pierre-YvesChibon",
                            "name": "pingou"
                        }
                    },
                    {
                        "comment": "Nevermind I tested in on a PR where I think we should also add it, but this is for viewing a file and works like a charm :)\r\n\r\nThanks!",
                        "commit": None,
                        "date_created": "1458297179",
                        "edited_on": None,
                        "editor": None,
                        "filename": None,
                        "id": 3484,
                        "line": None,
                        "notification": False,
                        "parent": None,
                        "tree": None,
                        "user": {
                            "fullname": "Pierre-YvesChibon",
                            "name": "pingou"
                        }
                    }
    ],
    "commit_start": "0b01c0facd70179e17762d0f2a053280cae94427",
    "commit_stop": "0b01c0facd70179e17762d0f2a053280cae94427",
    "date_created": "1458294982",
    "id": 848,
    "project": {
        "date_created": "1431549490",
        "description": "A git centered forge",
        "id": 10,
        "name": "pagure",
        "parent": None,
        "settings": {
            "Enforce_signed-off_commits_in_pull-request": False,
            "Minimum_score_to_merge_pull-request": -1,
            "Only_assignee_can_merge_pull-request": False,
            "Web-hooks": None,
            "always_merge": False,
            "issue_tracker": True,
            "project_documentation": True,
            "pull_requests": True
        },
        "tags": [
            "pagure",
            "fedmsg",
            "fedora-infra"
        ],
        "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
        }
    },
    "remote_git": None,
    "repo_from": {
        "date_created": "1450686367",
        "description": "A git centered forge",
        "id": 293,
        "name": "pagure",
        "parent": {
            "date_created": "1431549490",
            "description": "A git centered forge",
            "id": 10,
            "name": "pagure",
            "parent": None,
            "settings": {
                "Enforce_signed-off_commits_in_pull-request": False,
                "Minimum_score_to_merge_pull-request": -1,
                "Only_assignee_can_merge_pull-request": False,
                "Web-hooks": None,
                "always_merge": False,
                "issue_tracker": True,
                "project_documentation": True,
                "pull_requests": True
            },
            "tags": [
                "pagure",
                "fedmsg",
                "fedora-infra"
            ],
            "user": {
                "fullname": "Pierre-YvesChibon",
                "name": "pingou"
            }
        },
        "settings": {
            "Enforce_signed-off_commits_in_pull-request": False,
            "Minimum_score_to_merge_pull-request": -1,
            "Only_assignee_can_merge_pull-request": False,
            "Web-hooks": None,
            "always_merge": False,
            "issue_tracker": False,
            "project_documentation": True,
            "pull_requests": False
        },
        "tags": [],
        "user": {
            "fullname": "Lubomír Sedlář",
            "name": "lsedlar"
        }
    },
    "status": "Merged",
    "title": "Automatically scroll to highlighted range",
    "uid": "59e41f825a9b42dfa6268c20d53c9f44",
    "updated_on": "1458297185",
    "user": {
        "fullname": "Lubomír Sedlář",
        "name": "lsedlar"
    }
    }
    },
    "msg_id": "2016-3f10a96f-0d00-47fd-95c1-7b78b8825f9d",
    "timestamp": 1458297187.0,
    "topic": "io.pagure.prod.pagure.pull-request.comment.added"
    }
    ]


class TestPagureConglomeratorByOldStyleCommit(
    fedmsg.tests.test_meta.ConglomerateBase):
    expected = [
        {
            'categories': set(['pagure']),
            'end_time': 1458324396.0,
            'human_time': arrow.get(1458324396).humanize(),
            'icon': 'https://apps.fedoraproject.org/packages/images/icons/package_128x128.png',
            'link': 'https://pagure.io/fedora-hubs/3704095da807fc94f6ceff2f9d3c8d1de4888c22',
            'packages': set([]),
            'secondary_icon': None,
            'start_time': 1458324396.0,
            'subjective': u'rbean@redhat.com pushed to fedora-hubs (develop). "We need this to match our locally-stored datanommer topics so that the feed works."',
            'subtitle': u'rbean@redhat.com pushed to fedora-hubs (develop). "We need this to match our locally-stored datanommer topics so that the feed works."',
            'timestamp': 1458324396.0,
            'topics': set(['io.pagure.prod.pagure.git.receive']),
            'usernames': set(['rbean@redhat.com'])
        }, {
            'categories': set(['pagure']),
            'end_time': 1458298728.0,
            'human_time': arrow.get(1458292032).humanize(),
            'icon': 'https://apps.fedoraproject.org/packages/images/icons/package_128x128.png',
            'link': 'https://pagure.io/fedora-websites/commits',
            'packages': set([]),
            'secondary_icon': 'https://seccdn.libravatar.org/avatar/f507d9bd18d7298a62d4efd485ce9136dea6145d728077d74f349d8b8bb02605?s=64&d=retro',
            'start_time': 1458288685.0,
            'subjective': 'robyduck pushed 3 commits to the fedora-websites project',
            'subtitle': 'robyduck pushed 3 commits to the fedora-websites project',
            'timestamp': 1458292032.6666667,
            'topics': set(['io.pagure.prod.pagure.git.receive']),
            'usernames': set(['robyduck'])
        }, {
            'categories': set(['pagure']),
            'end_time': 1458294681.0,
            'human_time': arrow.get(1458294681).humanize(),
            'icon': 'https://apps.fedoraproject.org/packages/images/icons/package_128x128.png',
            'link': 'https://pagure.io/fedoramagazine-images/d71918d84ae82565837e9eaa8c42954c754fef4c',
            'packages': set([]),
            'secondary_icon': None,
            'start_time': 1458294681.0,
            'subjective': u'rlerch@redhat.com pushed to fedoramagazine-images (openvpn). "added openVPN image"',
            'subtitle': u'rlerch@redhat.com pushed to fedoramagazine-images (openvpn). "added openVPN image"',
            'timestamp': 1458294681.0,
            'topics': set(['io.pagure.prod.pagure.git.receive']),
            'usernames': set(['rlerch@redhat.com'])
        }
    ]

    originals = [
        {
            "i": 1,
            "msg": {
                "commit": {
                    "agent": "git",
                    "branch": "refs/heads/develop",
                    "email": "rbean@redhat.com",
                    "message": "We need this to match our locally-stored datanommer topics so that the feed works.",
                    "name": "Ralph Bean",
                    "path": "/srv/git/repositories/fedora-hubs.git",
                    "repo": {
                        "date_created": "1433438868",
                        "description": "Fedora Hubs",
                        "id": 50,
                        "name": "fedora-hubs",
                        "parent": None,
                        "settings": {
                            "Enforce_signed-off_commits_in_pull-request": False,
                            "Minimum_score_to_merge_pull-request": -1,
                            "Only_assignee_can_merge_pull-request": False,
                            "Web-hooks": None,
                            "always_merge": False,
                            "issue_tracker": True,
                            "project_documentation": False,
                            "pull_requests": True
                        },
                        "tags": [
                            "fedora-infra"
                        ],
                        "user": {
                            "fullname": "Remy DeCausemaker",
                            "name": "decause"
                        }
                    },
                    "rev": "3704095da807fc94f6ceff2f9d3c8d1de4888c22",
                    "seen": False,
                    "stats": {
                        "files": {
                            "fedmsg.d/base.py": {
                                "additions": 1,
                                "deletions": 1,
                                "lines": 2
                            }
                        },
                        "total": {
                            "additions": 1,
                            "deletions": 1,
                            "files": 1,
                            "lines": 2
                        }
                    },
                    "summary": "We need this to match our locally-stored datanommer topics so that the feed works.",
                    "username": None
                }
    },
    "msg_id": "2016-9e3e2b6e-3155-4785-b6eb-7f493d1f46af",
    "timestamp": 1458324396.0,
    "topic": "io.pagure.prod.pagure.git.receive"
    },
    {
        "i": 1,
        "msg": {
            "commit": {
                "agent": "git",
                "branch": "refs/heads/master",
                "email": "robyduck@fedoraproject.org",
                "message": "budget numbers title needs a hyperlink",
                "name": "Robert Mayr",
                "path": "/srv/git/repositories/fedora-websites.git",
                "repo": {
                    "date_created": "1456583771",
                    "description": "Fedora Websites",
                    "id": 375,
                    "name": "fedora-websites",
                    "parent": None,
                    "settings": {
                        "Enforce_signed-off_commits_in_pull-request": False,
                        "Minimum_score_to_merge_pull-request": -1,
                        "Only_assignee_can_merge_pull-request": False,
                        "Web-hooks": None,
                        "always_merge": False,
                        "issue_tracker": True,
                        "project_documentation": True,
                        "pull_requests": True
                    },
                    "tags": [
                        "fedmsg",
                        "fedora-app"
                    ],
                    "user": {
                        "fullname": "Robert Mayr",
                        "name": "robyduck"
                    }
                },
                "rev": "c1cdc52d08cb51b6f4d9f6fd5e34759590f8a9a4",
                "seen": False,
                "stats": {
                    "files": {
                        "budget.fedoraproject.org/data/content/index.html": {
                            "additions": 1,
                            "deletions": 1,
                            "lines": 2
                        }
                    },
                    "total": {
                        "additions": 1,
                        "deletions": 1,
                        "files": 1,
                        "lines": 2
                    }
                },
                "summary": "budget numbers title needs a hyperlink",
                "username": None
    }
    },
    "msg_id": "2016-78f3efd4-7842-4488-9899-7f23f1037aa6",
    "timestamp": 1458298728.0,
    "topic": "io.pagure.prod.pagure.git.receive"
    },
    {
        "i": 1,
        "msg": {
            "commit": {
                "agent": "git",
                "branch": "refs/heads/openvpn",
                "email": "rlerch@redhat.com",
                "message": "added openVPN image",
                "name": "Ryan Lerch",
                "path": "/srv/git/repositories/fedoramagazine-images.git",
                "repo": {
                    "date_created": "1440421477",
                    "description": "Cover Images for the Fedora Magazine",
                    "id": 147,
                    "name": "fedoramagazine-images",
                    "parent": None,
                    "settings": {
                        "Enforce_signed-off_commits_in_pull-request": False,
                        "Minimum_score_to_merge_pull-request": -1,
                        "Only_assignee_can_merge_pull-request": False,
                        "Web-hooks": None,
                        "always_merge": False,
                        "issue_tracker": True,
                        "project_documentation": True,
                        "pull_requests": True
                    },
                    "tags": [
                        "SVG",
                        "magazine",
                        "assets"
                    ],
                    "user": {
                        "fullname": "ryan lerch",
                        "name": "ryanlerch"
                    }
                },
                "rev": "d71918d84ae82565837e9eaa8c42954c754fef4c",
                "seen": False,
                "stats": {
                    "files": {
                        "images/openvpn.svg": {
                            "additions": 1007,
                            "deletions": 0,
                            "lines": 1007
                        }
                    },
                    "total": {
                        "additions": 1007,
                        "deletions": 0,
                        "files": 1,
                        "lines": 1007
                    }
                },
                "summary": "added openVPN image",
    "username": None
    }
    },
    "msg_id": "2016-44a40335-b644-409e-ac1b-3bf4b421109e",
    "timestamp": 1458294681.0,
    "topic": "io.pagure.prod.pagure.git.receive"
    },
    {
        "i": 1,
        "msg": {
            "commit": {
                "agent": "git",
                "branch": "refs/heads/master",
                "email": "robyduck@fedoraproject.org",
                "message": "fix anchor id for budget numbers",
                "name": "Robert Mayr",
                "path": "/srv/git/repositories/fedora-websites.git",
                "repo": {
                    "date_created": "1456583771",
                    "description": "Fedora Websites",
                    "id": 375,
                    "name": "fedora-websites",
                    "parent": None,
                    "settings": {
                        "Enforce_signed-off_commits_in_pull-request": False,
                        "Minimum_score_to_merge_pull-request": -1,
                        "Only_assignee_can_merge_pull-request": False,
                        "Web-hooks": None,
                        "always_merge": False,
                        "issue_tracker": True,
                        "project_documentation": True,
                        "pull_requests": True
                    },
                    "tags": [
                        "fedmsg",
                        "fedora-app"
                    ],
                    "user": {
                        "fullname": "Robert Mayr",
                        "name": "robyduck"
                    }
                },
                "rev": "ec1d633b89a4dfdc05a09bd01b3a84cbe6aecbf7",
                "seen": False,
                "stats": {
                    "files": {
                        "budget.fedoraproject.org/data/content/index.html": {
                            "additions": 1,
                            "deletions": 1,
                            "lines": 2
                        }
                    },
                    "total": {
                        "additions": 1,
                        "deletions": 1,
                        "files": 1,
                        "lines": 2
                    }
                },
                "summary": "fix anchor id for budget numbers",
                "username": None
    }
    },
    "msg_id": "2016-9ad5642e-b9d9-49fc-9d0a-0f9e22b34158",
    "timestamp": 1458288685.0,
    "topic": "io.pagure.prod.pagure.git.receive"
    },
    {
        "i": 2,
        "msg": {
            "commit": {
                "agent": "git",
                "branch": "refs/heads/master",
                "email": "robyduck@fedoraproject.org",
                "message": "fix genshi markups for regional delegate titles",
                "name": "Robert Mayr",
                "path": "/srv/git/repositories/fedora-websites.git",
                "repo": {
                    "date_created": "1456583771",
                    "description": "Fedora Websites",
                    "id": 375,
                    "name": "fedora-websites",
                    "parent": None,
                    "settings": {
                        "Enforce_signed-off_commits_in_pull-request": False,
                        "Minimum_score_to_merge_pull-request": -1,
                        "Only_assignee_can_merge_pull-request": False,
                        "Web-hooks": None,
                        "always_merge": False,
                        "issue_tracker": True,
                        "project_documentation": True,
                        "pull_requests": True
                    },
                    "tags": [
                        "fedmsg",
                        "fedora-app"
                    ],
                    "user": {
                        "fullname": "Robert Mayr",
                        "name": "robyduck"
                    }
                },
                "rev": "e8523c28ea57af1a58f2e5aa4180338a5d5a6bd8",
                "seen": False,
                "stats": {
                    "files": {
                        "budget.fedoraproject.org/data/content/index.html": {
                            "additions": 4,
                            "deletions": 4,
                            "lines": 8
                        }
                    },
                    "total": {
                        "additions": 4,
                        "deletions": 4,
                        "files": 1,
                        "lines": 8
                    }
                },
                "summary": "fix genshi markups for regional delegate titles",
                "username": None
    }
    },
    "msg_id": "2016-e6dd6d1f-b013-4fe3-aa2b-09f275ada088",
    "timestamp": 1458288685.0,
    "topic": "io.pagure.prod.pagure.git.receive"
    }
    ]


class TestPagureConglomeratorByNewStyleCommit(
    fedmsg.tests.test_meta.ConglomerateBase):
    expected = [{
        'categories': set(['pagure']),
        'end_time': 1457538778,
        'human_time': arrow.get(1457538778).humanize(),
        'icon': 'https://apps.fedoraproject.org/packages/images/icons/package_128x128.png',
        'link': 'https://pagure.io/pagure/commits',
        'packages': set([]),
        'secondary_icon': 'https://seccdn.libravatar.org/avatar/01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c?s=64&d=retro',
        'start_time': 1457538778,
        'subjective': 'pingou pushed 5 commits to pagure (feature and master)',
        'subtitle': 'pingou pushed 5 commits to pagure (feature and master)',
        'timestamp': 1457538778,
        'topics': set(['io.pagure.prod.pagure.git.receive']),
        'usernames': set(['pingou']),
    }]

    originals = [{
      "username": "pingou",
      "i": 1,
      "timestamp": 1457538778,
      "msg_id": "2016-c854f690-5691-42e8-b488-2d65aef80fdc",
      "topic": "io.pagure.prod.pagure.git.receive",
      "msg": {
        "forced": False,
        "agent": "pingou",
        "repo": {
          "description": "test project #1",
          "parent": None,
          "settings": {
            "Minimum_score_to_merge_pull-request": -1,
            "Web-hooks": None,
            "project_documentation": False,
            "always_merge": True,
            "pull_requests": True,
            "Enforce_signed-off_commits_in_pull-request": False,
            "Comment-editing": False,
            "Only_assignee_can_merge_pull-request": False,
            "issue_tracker": True
          },
          "tags": [
            "fedora-infra",
            "fedora"
          ],
          "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
          },
          "date_created": "1426500194",
          "id": 1,
          "name": "pagure"
        },
        "end_commit": "edc02fbb423d3957d174c571896418f29fa169b8",
        "branch": "refs/heads/master",
        "total_commits": 3,
        "start_commit": "b5e65479e4bd91554d8d3084bf378ffb6e4ef605"
      }
    }, {
      "username": "pingou",
      "i": 1,
      "timestamp": 1457538778,
      "msg_id": "2016-c854f690-5691-42e8-b488-2d65aef80fdc",
      "topic": "io.pagure.prod.pagure.git.receive",
      "msg": {
        "forced": False,
        "agent": "pingou",
        "repo": {
          "description": "test project #1",
          "parent": None,
          "settings": {
            "Minimum_score_to_merge_pull-request": -1,
            "Web-hooks": None,
            "project_documentation": False,
            "always_merge": True,
            "pull_requests": True,
            "Enforce_signed-off_commits_in_pull-request": False,
            "Comment-editing": False,
            "Only_assignee_can_merge_pull-request": False,
            "issue_tracker": True
          },
          "tags": [
            "fedora-infra",
            "fedora"
          ],
          "user": {
            "fullname": "Pierre-YvesChibon",
            "name": "pingou"
          },
          "date_created": "1426500194",
          "id": 1,
          "name": "pagure"
        },
        "end_commit": "edc02fbb423d3957d174c571896418f29fa169b8",
        "branch": "refs/heads/feature",
        "total_commits": 2,
        "start_commit": "b5e65479e4bd91554d8d3084bf378ffb6e4ef605"
      }
    }]
