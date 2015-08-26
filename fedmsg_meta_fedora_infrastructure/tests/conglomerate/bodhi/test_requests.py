import fedmsg.tests.test_meta
import arrow

class TestBodhiConglomerateTestingSamePackageSameUser(
        fedmsg.tests.test_meta.ConglomerateBase):
    originals = [
        {
            "i": 3,
            "msg": {
                "agent": "pghmcfc",
                "update": {
                    "approved": None,
                    "bugs": [
                        {
                            "bz_id": 1130581,
                            "parent": False,
                            "security": False,
                            "title": "Review Request: perl-Devel-CheckBin",
                        }
                    ],
                    "builds": [
                        {
                            "nvr": "perl-Devel-CheckBin-0.02-2.fc19",
                            "package": {
                                "committers": [
                                    "pghmcfc"
                                ],
                                "name": "perl-Devel-CheckBin",
                                "suggest_reboot": False
                            }
                        }
                    ],
                    "close_bugs": False,
                    "comments": [
                        {
                            "anonymous": False,
                            "author": "bodhi",
                            "group": None,
                            "karma": 0,
                            "text": "This update has been submitted for "
                            "testing by pghmcfc. ",
                            "timestamp": 1408636112.0,
                            "update_request": "testing",
                            "update_status": "pending",
                            "update_submitter": "pghmcfc",
                            "update_title": "perl-Devel-CheckBin-0.02-2.fc19"
                        }
                    ],
                    "critpath": False,
                    "critpath_approved": False,
                    "date_modified": None,
                    "date_pushed": None,
                    "date_submitted": 1408636106.0,
                    "karma": 0,
                    "nagged": None,
                    "notes": "This is the first Fedora release "
                    "of perl-Devel-CheckBin.",
                    "release": {
                        "dist_tag": "f19",
                        "id_prefix": "FEDORA",
                        "locked": False,
                        "long_name": "Fedora 19",
                        "name": "F19"
                    },
                    "request": "testing",
                    "stable_karma": 2,
                    "status": "pending",
                    "submitter": "pghmcfc",
                    "title": "perl-Devel-CheckBin-0.02-2.fc19",
                    "type": "newpackage",
                    "unstable_karma": -2,
                    "updateid": None
                }
            },
            "msg_id": "2014-3db55159-6a93-4659-8eb7-19a24255df9c",
            "source_name": "datanommer",
            "source_version": "0.6.4",
            "timestamp": 1408636112.0,
            "topic": "org.fedoraproject.prod.bodhi.update.request.testing"
        },
        {
            "i": 2,
            "msg": {
                "agent": "pghmcfc",
                "update": {
                    "approved": None,
                    "bugs": [
                        {
                            "bz_id": 1130581,
                            "parent": False,
                            "security": False,
                            "title": "Review Request: perl-Devel-CheckBin",
                        }
                    ],
                    "builds": [
                        {
                            "nvr": "perl-Devel-CheckBin-0.02-2.fc20",
                            "package": {
                                "committers": [
                                    "pghmcfc"
                                ],
                                "name": "perl-Devel-CheckBin",
                                "suggest_reboot": False
                            }
                        }
                    ],
                    "close_bugs": False,
                    "comments": [
                        {
                            "anonymous": False,
                            "author": "bodhi",
                            "group": None,
                            "karma": 0,
                            "text": "This update has been submitted for "
                            "testing by pghmcfc. ",
                            "timestamp": 1408636105.0,
                            "update_request": "testing",
                            "update_status": "pending",
                            "update_submitter": "pghmcfc",
                            "update_title": "perl-Devel-CheckBin-0.02-2.fc20"
                        }
                    ],
                    "critpath": False,
                    "critpath_approved": False,
                    "date_modified": None,
                    "date_pushed": None,
                    "date_submitted": 1408636098.0,
                    "karma": 0,
                    "nagged": None,
                    "notes": "This is the first Fedora release of "
                    "perl-Devel-CheckBin.",
                    "release": {
                        "dist_tag": "f20",
                        "id_prefix": "FEDORA",
                        "locked": False,
                        "long_name": "Fedora 20",
                        "name": "F20"
                    },
                    "request": "testing",
                    "stable_karma": 2,
                    "status": "pending",
                    "submitter": "pghmcfc",
                    "title": "perl-Devel-CheckBin-0.02-2.fc20",
                    "type": "newpackage",
                    "unstable_karma": -2,
                    "updateid": None
                }
            },
            "msg_id": "2014-8572040e-4456-48cc-b5c2-b457879e82ae",
            "source_name": "datanommer",
            "source_version": "0.6.4",
            "timestamp": 1408636105.0,
            "topic": "org.fedoraproject.prod.bodhi.update.request.testing"
        },
    ]
    expected = [{
        'subtitle': 'pghmcfc submitted 2 perl-Devel-CheckBin '
        'testing updates for F19 and F20',
        'subjective': 'pghmcfc submitted 2 perl-Devel-CheckBin '
        'testing updates for F19 and F20',
        'link': 'https://bodhi.fedoraproject.org/updates/perl-Devel-CheckBin',
        'icon': 'https://apps.fedoraproject.org/img/icons/bodhi.png',
        'secondary_icon': 'https://seccdn.libravatar.org/avatar/'
        'f9800f2daf8aabc0b33bca9b4033019c74db77b3baca2d9f98cc629147430e20'
        '?s=64&d=retro',

        'start_time': 1408636105.0,
        'end_time': 1408636112.0,
        'timestamp': 1408636108.5,
        'human_time': arrow.get(1408636108.5).humanize(),

        'usernames': set(['pghmcfc']),
        'packages': set(['perl-Devel-CheckBin']),
        'topics': set(['org.fedoraproject.prod.bodhi.update.request.testing']),
        'categories': set(['bodhi']),
        'msg_ids': [
            '2014-3db55159-6a93-4659-8eb7-19a24255df9c',
            '2014-8572040e-4456-48cc-b5c2-b457879e82ae',
        ],
    } ]


class TestBodhiConglomerateTestingSamePackageDifferentUser(
        fedmsg.tests.test_meta.ConglomerateBase):
    originals = [
        {
            "i": 3,
            "msg": {
                "agent": "ralph",
                "update": {
                    "approved": None,
                    "bugs": [
                        {
                            "bz_id": 1130581,
                            "parent": False,
                            "security": False,
                            "title": "Review Request: perl-Devel-CheckBin",
                        }
                    ],
                    "builds": [
                        {
                            "nvr": "perl-Devel-CheckBin-0.02-2.fc19",
                            "package": {
                                "committers": [
                                    "pghmcfc"
                                ],
                                "name": "perl-Devel-CheckBin",
                                "suggest_reboot": False
                            }
                        }
                    ],
                    "close_bugs": False,
                    "comments": [
                        {
                            "anonymous": False,
                            "author": "bodhi",
                            "group": None,
                            "karma": 0,
                            "text": "This update has been submitted for "
                            "testing by ralph. ",
                            "timestamp": 1408636112.0,
                            "update_request": "testing",
                            "update_status": "pending",
                            "update_submitter": "ralph",
                            "update_title": "perl-Devel-CheckBin-0.02-2.fc19"
                        }
                    ],
                    "critpath": False,
                    "critpath_approved": False,
                    "date_modified": None,
                    "date_pushed": None,
                    "date_submitted": 1408636106.0,
                    "karma": 0,
                    "nagged": None,
                    "notes": "This is the first Fedora release "
                    "of perl-Devel-CheckBin.",
                    "release": {
                        "dist_tag": "f19",
                        "id_prefix": "FEDORA",
                        "locked": False,
                        "long_name": "Fedora 19",
                        "name": "F19"
                    },
                    "request": "testing",
                    "stable_karma": 2,
                    "status": "pending",
                    "submitter": "ralph",
                    "title": "perl-Devel-CheckBin-0.02-2.fc19",
                    "type": "newpackage",
                    "unstable_karma": -2,
                    "updateid": None
                }
            },
            "msg_id": "2014-3db55159-6a93-4659-8eb7-19a24255df9c",
            "source_name": "datanommer",
            "source_version": "0.6.4",
            "timestamp": 1408636112.0,
            "topic": "org.fedoraproject.prod.bodhi.update.request.testing"
        },
        {
            "i": 2,
            "msg": {
                "agent": "pghmcfc",
                "update": {
                    "approved": None,
                    "bugs": [
                        {
                            "bz_id": 1130581,
                            "parent": False,
                            "security": False,
                            "title": "Review Request: perl-Devel-CheckBin",
                        }
                    ],
                    "builds": [
                        {
                            "nvr": "perl-Devel-CheckBin-0.02-2.fc20",
                            "package": {
                                "committers": [
                                    "pghmcfc"
                                ],
                                "name": "perl-Devel-CheckBin",
                                "suggest_reboot": False
                            }
                        }
                    ],
                    "close_bugs": False,
                    "comments": [
                        {
                            "anonymous": False,
                            "author": "bodhi",
                            "group": None,
                            "karma": 0,
                            "text": "This update has been submitted for "
                            "testing by pghmcfc. ",
                            "timestamp": 1408636105.0,
                            "update_request": "testing",
                            "update_status": "pending",
                            "update_submitter": "pghmcfc",
                            "update_title": "perl-Devel-CheckBin-0.02-2.fc20"
                        }
                    ],
                    "critpath": False,
                    "critpath_approved": False,
                    "date_modified": None,
                    "date_pushed": None,
                    "date_submitted": 1408636098.0,
                    "karma": 0,
                    "nagged": None,
                    "notes": "This is the first Fedora release of "
                    "perl-Devel-CheckBin.",
                    "release": {
                        "dist_tag": "f20",
                        "id_prefix": "FEDORA",
                        "locked": False,
                        "long_name": "Fedora 20",
                        "name": "F20"
                    },
                    "request": "testing",
                    "stable_karma": 2,
                    "status": "pending",
                    "submitter": "pghmcfc",
                    "title": "perl-Devel-CheckBin-0.02-2.fc20",
                    "type": "newpackage",
                    "unstable_karma": -2,
                    "updateid": None
                }
            },
            "msg_id": "2014-8572040e-4456-48cc-b5c2-b457879e82ae",
            "source_name": "datanommer",
            "source_version": "0.6.4",
            "timestamp": 1408636105.0,
            "topic": "org.fedoraproject.prod.bodhi.update.request.testing"
        },
    ]
    expected = [{
        'subtitle': 'pghmcfc and ralph submitted 2 perl-Devel-CheckBin '
        'updates for F19 and F20',
        'subjective': 'pghmcfc and ralph submitted 2 perl-Devel-CheckBin '
        'updates for F19 and F20',
        'link': 'https://bodhi.fedoraproject.org/updates/perl-Devel-CheckBin',
        'icon': 'https://apps.fedoraproject.org/img/icons/bodhi.png',
        'secondary_icon': 'https://apps.fedoraproject.org/img/icons/bodhi.png',

        'start_time': 1408636105.0,
        'end_time': 1408636112.0,
        'timestamp': 1408636108.5,
        'human_time': arrow.get(1408636108.5).humanize(),

        'usernames': set(['pghmcfc', 'ralph']),
        'packages': set(['perl-Devel-CheckBin']),
        'topics': set(['org.fedoraproject.prod.bodhi.update.request.testing']),
        'categories': set(['bodhi']),
        'msg_ids': [
            '2014-3db55159-6a93-4659-8eb7-19a24255df9c',
            '2014-8572040e-4456-48cc-b5c2-b457879e82ae',
        ],
    } ]


class TestBodhiConglomerateTestingSameUserDifferentPackage(
        fedmsg.tests.test_meta.ConglomerateBase):
    originals = [
        {
            "i": 3,
            "msg": {
                "agent": "pghmcfc",
                "update": {
                    "approved": None,
                    "bugs": [
                        {
                            "bz_id": 1130581,
                            "parent": False,
                            "security": False,
                            "title": "Review Request: perl-Devel-CheckBin",
                        }
                    ],
                    "builds": [
                        {
                            "nvr": "perl-Devel-CheckBin-0.02-2.fc19",
                            "package": {
                                "committers": [
                                    "pghmcfc"
                                ],
                                "name": "perl-Devel-CheckBin",
                                "suggest_reboot": False
                            }
                        }
                    ],
                    "close_bugs": False,
                    "comments": [
                        {
                            "anonymous": False,
                            "author": "bodhi",
                            "group": None,
                            "karma": 0,
                            "text": "This update has been submitted for "
                            "testing by pghmcfc. ",
                            "timestamp": 1408636112.0,
                            "update_request": "testing",
                            "update_status": "pending",
                            "update_submitter": "pghmcfc",
                            "update_title": "perl-Devel-CheckBin-0.02-2.fc19"
                        }
                    ],
                    "critpath": False,
                    "critpath_approved": False,
                    "date_modified": None,
                    "date_pushed": None,
                    "date_submitted": 1408636106.0,
                    "karma": 0,
                    "nagged": None,
                    "notes": "This is the first Fedora release "
                    "of perl-Devel-CheckBin.",
                    "release": {
                        "dist_tag": "f19",
                        "id_prefix": "FEDORA",
                        "locked": False,
                        "long_name": "Fedora 19",
                        "name": "F19"
                    },
                    "request": "testing",
                    "stable_karma": 2,
                    "status": "pending",
                    "submitter": "pghmcfc",
                    "title": "perl-Devel-CheckBin-0.02-2.fc19",
                    "type": "newpackage",
                    "unstable_karma": -2,
                    "updateid": None
                }
            },
            "msg_id": "2014-3db55159-6a93-4659-8eb7-19a24255df9c",
            "source_name": "datanommer",
            "source_version": "0.6.4",
            "timestamp": 1408636112.0,
            "topic": "org.fedoraproject.prod.bodhi.update.request.testing"
        },
        {
            "i": 2,
            "msg": {
                "agent": "pghmcfc",
                "update": {
                    "approved": None,
                    "bugs": [
                        {
                            "bz_id": 1130581,
                            "parent": False,
                            "security": False,
                            "title": "Review Request: nethack",
                        }
                    ],
                    "builds": [
                        {
                            "nvr": "nethack-0.02-2.fc20",
                            "package": {
                                "committers": [
                                    "pghmcfc"
                                ],
                                "name": "nethack",
                                "suggest_reboot": False
                            }
                        }
                    ],
                    "close_bugs": False,
                    "comments": [
                        {
                            "anonymous": False,
                            "author": "bodhi",
                            "group": None,
                            "karma": 0,
                            "text": "This update has been submitted for "
                            "testing by pghmcfc. ",
                            "timestamp": 1408636105.0,
                            "update_request": "testing",
                            "update_status": "pending",
                            "update_submitter": "pghmcfc",
                            "update_title": "nethack-0.02-2.fc20"
                        }
                    ],
                    "critpath": False,
                    "critpath_approved": False,
                    "date_modified": None,
                    "date_pushed": None,
                    "date_submitted": 1408636098.0,
                    "karma": 0,
                    "nagged": None,
                    "notes": "This is the first Fedora release of "
                    "nethack.",
                    "release": {
                        "dist_tag": "f20",
                        "id_prefix": "FEDORA",
                        "locked": False,
                        "long_name": "Fedora 20",
                        "name": "F20"
                    },
                    "request": "testing",
                    "stable_karma": 2,
                    "status": "pending",
                    "submitter": "pghmcfc",
                    "title": "nethack-0.02-2.fc20",
                    "type": "newpackage",
                    "unstable_karma": -2,
                    "updateid": None
                }
            },
            "msg_id": "2014-8572040e-4456-48cc-b5c2-b457879e82ae",
            "source_name": "datanommer",
            "source_version": "0.6.4",
            "timestamp": 1408636105.0,
            "topic": "org.fedoraproject.prod.bodhi.update.request.testing"
        },
    ]
    expected = [{
        'subtitle': 'pghmcfc submitted nethack and perl-Devel-CheckBin '
        'updates for F19 and F20',
        'subjective': 'pghmcfc submitted nethack and perl-Devel-CheckBin '
        'updates for F19 and F20',
        'link': 'https://bodhi.fedoraproject.org/users/pghmcfc',
        'icon': 'https://apps.fedoraproject.org/img/icons/bodhi.png',
        'secondary_icon': 'https://seccdn.libravatar.org/avatar/'
        'f9800f2daf8aabc0b33bca9b4033019c74db77b3baca2d9f98cc629147430e20'
        '?s=64&d=retro',

        'start_time': 1408636105.0,
        'end_time': 1408636112.0,
        'timestamp': 1408636108.5,
        'human_time': arrow.get(1408636108.5).humanize(),

        'usernames': set(['pghmcfc']),
        'packages': set(['perl-Devel-CheckBin', 'nethack']),
        'topics': set(['org.fedoraproject.prod.bodhi.update.request.testing']),
        'categories': set(['bodhi']),
        'msg_ids': [
            '2014-3db55159-6a93-4659-8eb7-19a24255df9c',
            '2014-8572040e-4456-48cc-b5c2-b457879e82ae',
        ],
    } ]
