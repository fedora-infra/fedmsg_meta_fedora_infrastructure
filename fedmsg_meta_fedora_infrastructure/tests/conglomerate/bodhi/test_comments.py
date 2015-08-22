import fedmsg.tests.test_meta
import arrow

class TestBodhiConglomerateCommentSameUpdate(
        fedmsg.tests.test_meta.ConglomerateBase):
    originals = [
        {
            "i": 1,
            "msg": {
                "agent": "hreindl",
                "comment": {
                    "anonymous": False,
                    "author": "hreindl",
                    "group": None,
                    "karma": 1,
                    "text": "works for me",
                    "timestamp": 1408799774.0,
                    "update_request": None,
                    "update_status": "testing",
                    "update_submitter": "jstanek",
                    "update_title": "sqlite-3.8.6-2.fc20"
                }
            },
            "msg_id": "2014-10047900-1379-4ede-ba94-8319823541a8",
            "timestamp": 1408799776.0,
            "topic": "org.fedoraproject.prod.bodhi.update.comment"
        },
        {
            "i": 1,
            "msg": {
                "agent": "hreindl",
                "comment": {
                    "anonymous": False,
                    "author": "hreindl",
                    "group": None,
                    "karma": 1,
                    "text": "works for me",
                    "timestamp": 1408799744.0,
                    "update_request": None,
                    "update_status": "testing",
                    "update_submitter": "jkaluza",
                    "update_title": "file-5.19-4.fc20"
                }
            },
            "msg_id": "2014-c1ccc3bb-e9bc-4424-8b99-6fbfa24a128f",
            "timestamp": 1408799746.0,
            "topic": "org.fedoraproject.prod.bodhi.update.comment"
        },
        {
            "i": 1,
            "msg": {
                "agent": "volter",
                "comment": {
                    "anonymous": False,
                    "author": "volter",
                    "group": None,
                    "karma": 0,
                    "text": "Please add spatialite-tools-4.1.1-6.fc20",
                    "timestamp": 1408787443.0,
                    "update_request": None,
                    "update_status": "testing",
                    "update_submitter": "jstanek",
                    "update_title": "sqlite-3.8.6-2.fc20"
                }
            },
            "msg_id": "2014-f0205c2a-205e-4c79-aad3-542429b3fca8",
            "timestamp": 1408787444.0,
            "topic": "org.fedoraproject.prod.bodhi.update.comment"
        },

    ]
    expected = [{
        'subtitle': 'hreindl and volter commented on sqlite-3.8.6-2.fc20',
        'subjective': 'hreindl and volter commented on sqlite-3.8.6-2.fc20',
        'link': 'https://bodhi.fedoraproject.org/updates/sqlite-3.8.6-2.fc20',
        'icon': 'https://apps.fedoraproject.org/img/icons/bodhi.png',
        'secondary_icon': 'https://apps.fedoraproject.org/img/icons/bodhi.png',

        'start_time': 1408787444.0,
        'end_time': 1408799776.0,
        'timestamp': 1408793610.0,
        'human_time': arrow.get(1408793610.0).humanize(),

        'usernames': set(['volter', 'hreindl']),
        'packages': set(['sqlite']),
        'topics': set(['org.fedoraproject.prod.bodhi.update.comment']),
        'categories': set(['bodhi']),
        'msg_ids': [
            '2014-10047900-1379-4ede-ba94-8319823541a8',
            '2014-f0205c2a-205e-4c79-aad3-542429b3fca8',
        ],
    }, {
        'subtitle': u'hreindl commented on bodhi update '
        'file-5.19-4.fc20 (karma: 1)',
        'subjective': u'hreindl commented on bodhi update '
        'file-5.19-4.fc20 (karma: 1)',
        'link': 'https://bodhi.fedoraproject.org/updates/file-5.19-4.fc20',
        'icon': 'https://apps.fedoraproject.org/img/icons/bodhi.png',
        'secondary_icon': 'https://seccdn.libravatar.org/avatar/'
        'c82951c2d404ca0cfea20f51b040175ba4d1624f51e8ec366e75565b672e943d'
        '?s=64&d=retro',

        'start_time': 1408799746.0,
        'end_time': 1408799746.0,
        'timestamp': 1408799746.0,
        'human_time': arrow.get(1408799746.0).humanize(),

        'usernames': set(['hreindl']),
        'packages': set(['file']),
        'topics': set(['org.fedoraproject.prod.bodhi.update.comment']),
        'categories': set(['bodhi']),
        'msg_ids': ['2014-c1ccc3bb-e9bc-4424-8b99-6fbfa24a128f'],
    } ]


class TestBodhiConglomerateCommentSameUser(
        fedmsg.tests.test_meta.ConglomerateBase):
    originals = [
        {
            "i": 1,
            "msg": {
                "agent": "hreindl",
                "comment": {
                    "anonymous": False,
                    "author": "hreindl",
                    "group": None,
                    "karma": 1,
                    "text": "works for me",
                    "timestamp": 1408799774.0,
                    "update_request": None,
                    "update_status": "testing",
                    "update_submitter": "jstanek",
                    "update_title": "sqlite-3.8.6-2.fc20"
                }
            },
            "msg_id": "2014-10047900-1379-4ede-ba94-8319823541a8",
            "timestamp": 1408799776.0,
            "topic": "org.fedoraproject.prod.bodhi.update.comment"
        },
        {
            "i": 1,
            "msg": {
                "agent": "hreindl",
                "comment": {
                    "anonymous": False,
                    "author": "hreindl",
                    "group": None,
                    "karma": 1,
                    "text": "works for me",
                    "timestamp": 1408799744.0,
                    "update_request": None,
                    "update_status": "testing",
                    "update_submitter": "jkaluza",
                    "update_title": "file-5.19-4.fc20"
                }
            },
            "msg_id": "2014-c1ccc3bb-e9bc-4424-8b99-6fbfa24a128f",
            "timestamp": 1408799746.0,
            "topic": "org.fedoraproject.prod.bodhi.update.comment"
        },
    ]
    expected = [{
        'subtitle': 'hreindl commented on file-5.19-4.fc20 '
        'and sqlite-3.8.6-2.fc20',
        'subjective': 'hreindl commented on file-5.19-4.fc20 '
        'and sqlite-3.8.6-2.fc20',
        'link': 'https://bodhi.fedoraproject.org/users/hreindl',
        'icon': 'https://apps.fedoraproject.org/img/icons/bodhi.png',
        'secondary_icon': 'https://seccdn.libravatar.org/avatar/'
        'c82951c2d404ca0cfea20f51b040175ba4d1624f51e8ec366e75565b672e943d'
        '?s=64&d=retro',

        'start_time': 1408799746.0,
        'end_time': 1408799776.0,
        'timestamp': 1408799761.0,
        'human_time': arrow.get(1408799761.0).humanize(),

        'usernames': set(['hreindl']),
        'packages': set(['sqlite', 'file']),
        'topics': set(['org.fedoraproject.prod.bodhi.update.comment']),
        'categories': set(['bodhi']),
        'msg_ids': [
            '2014-10047900-1379-4ede-ba94-8319823541a8',
            '2014-c1ccc3bb-e9bc-4424-8b99-6fbfa24a128f',
        ],
    } ]
