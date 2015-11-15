import fedmsg.tests.test_meta
import arrow


class TestBodhiConglomerateTag(fedmsg.tests.test_meta.ConglomerateBase):
    originals = [
        {
            "i": 5,
            "msg": {
                "override": {
                    "build": {
                        "nvr": "golang-github-bugsnag-panicwrap-0-0.1.gite5f9854.el6"
                    },
                    "build_id": 55600,
                    "expiration_date": "2015-11-07 00:00:00",
                    "expired_date": None,
                    "notes": "Override",
                    "nvr": "golang-github-bugsnag-panicwrap-0-0.1.gite5f9854.el6",
                    "submission_date": "2015-10-19 14:22:57",
                    "submitter": {
                        "avatar": None,
                        "email": "fpokorny@redhat.com",
                        "groups": [
                            {
                                "name": "packager"
                            }
                        ],
                        "id": 104,
                        "name": "fpokorny",
                        "openid": None
                    },
                    "submitter_id": 104
                }
            },
            "msg_id": "2015-5af08502-68ca-4b1b-bfbd-cec012122206",
            "timestamp": 1445264577.0,
            "topic": "org.fedoraproject.prod.bodhi.buildroot_override.tag"
        },
        {
            "i": 6,
            "msg": {
                "override": {
                    "build": {
                        "nvr": "golang-github-jfrazelle-go-0-0.1.git6e461eb.fc23"
                    },
                    "build_id": 55582,
                    "expiration_date": "2015-11-07 00:00:00",
                    "expired_date": None,
                    "notes": "Override",
                    "nvr": "golang-github-jfrazelle-go-0-0.1.git6e461eb.fc23",
                    "submission_date": "2015-10-19 14:21:28",
                    "submitter": {
                        "avatar": None,
                        "email": "fpokorny@redhat.com",
                        "groups": [
                            {
                                "name": "packager"
                            }
                        ],
                        "id": 104,
                        "name": "fpokorny",
                        "openid": None
                    },
                    "submitter_id": 104
                }
            },
            "msg_id": "2015-f5f95d7d-2658-4b19-b5b0-9be3b12c7626",
            "timestamp": 1445264488.0,
            "topic": "org.fedoraproject.prod.bodhi.buildroot_override.tag"
        },
        {
            "i": 12,
            "msg": {
                "override": {
                    "build": {
                        "nvr": "golang-github-jfrazelle-go-0-0.1.git6e461eb.fc21"
                    },
                    "build_id": 55578,
                    "expiration_date": "2015-11-07 00:00:00",
                    "expired_date": None,
                    "notes": "Override",
                    "nvr": "golang-github-jfrazelle-go-0-0.1.git6e461eb.fc21",
                    "submission_date": "2015-10-19 14:21:25",
                    "submitter": {
                        "avatar": None,
                        "email": "fpokorny@redhat.com",
                        "groups": [
                            {
                                "name": "packager"
                            }
                        ],
                        "id": 104,
                        "name": "fpokorny",
                        "openid": None
                    },
                    "submitter_id": 104
                }
            },
            "msg_id": "2015-264b6974-27c2-48c1-b2e0-2856c199c793",
            "timestamp": 1445264485.0,
            "topic": "org.fedoraproject.prod.bodhi.buildroot_override.tag"
        }
    ]
    expected = [{
        'subtitle': 'fpokorny submitted 3 overrides for '
        'golang-github-bugsnag-panicwrap and golang-github-jfrazelle-go '
        'on el6, fc21, and fc23',
        'subjective': 'fpokorny submitted 3 overrides for '
        'golang-github-bugsnag-panicwrap and golang-github-jfrazelle-go '
        'on el6, fc21, and fc23',
        'link': 'https://bodhi.fedoraproject.org/overrides/?user=fpokorny',
        'icon': 'https://apps.fedoraproject.org/img/icons/bodhi.png',
        'secondary_icon': 'https://seccdn.libravatar.org/avatar/'
        'b1b6c806cd1bbd4433ed428fe7625af0fbcca93ff469251b43f1860358fab9b1'
        '?s=64&d=retro',

        'start_time': 1445264485.0,
        'end_time': 1445264577.0,
        'timestamp': 1445264516.6666667,
        'human_time': arrow.get(1445264516.6666667).humanize(),

        'usernames': set(['fpokorny']),
        'packages': set([
            'golang-github-bugsnag-panicwrap',
            'golang-github-jfrazelle-go',
        ]),
        'topics': set(['org.fedoraproject.prod.bodhi.buildroot_override.tag']),
        'categories': set(['bodhi']),
        'msg_ids': [
            '2014-3db55159-6a93-4659-8eb7-19a24255df9c',
            '2014-8572040e-4456-48cc-b5c2-b457879e82ae',
        ],
    } ]


class TestBodhiConglomerateUnTag(fedmsg.tests.test_meta.ConglomerateBase):
    originals = [
        {
            "i": 5,
            "msg": {
                "override": {
                    "build": {
                        "nvr": "golang-github-bugsnag-panicwrap-0-0.1.gite5f9854.el6"
                    },
                    "build_id": 55600,
                    "expiration_date": "2015-11-07 00:00:00",
                    "expired_date": None,
                    "notes": "Override",
                    "nvr": "golang-github-bugsnag-panicwrap-0-0.1.gite5f9854.el6",
                    "submission_date": "2015-10-19 14:22:57",
                    "submitter": {
                        "avatar": None,
                        "email": "fpokorny@redhat.com",
                        "groups": [
                            {
                                "name": "packager"
                            }
                        ],
                        "id": 104,
                        "name": "fpokorny",
                        "openid": None
                    },
                    "submitter_id": 104
                }
            },
            "msg_id": "2015-5af08502-68ca-4b1b-bfbd-cec012122206",
            "timestamp": 1445264577.0,
            "topic": "org.fedoraproject.prod.bodhi.buildroot_override.untag"
        },
        {
            "i": 6,
            "msg": {
                "override": {
                    "build": {
                        "nvr": "golang-github-jfrazelle-go-0-0.1.git6e461eb.fc23"
                    },
                    "build_id": 55582,
                    "expiration_date": "2015-11-07 00:00:00",
                    "expired_date": None,
                    "notes": "Override",
                    "nvr": "golang-github-jfrazelle-go-0-0.1.git6e461eb.fc23",
                    "submission_date": "2015-10-19 14:21:28",
                    "submitter": {
                        "avatar": None,
                        "email": "fpokorny@redhat.com",
                        "groups": [
                            {
                                "name": "packager"
                            }
                        ],
                        "id": 104,
                        "name": "fpokorny",
                        "openid": None
                    },
                    "submitter_id": 104
                }
            },
            "msg_id": "2015-f5f95d7d-2658-4b19-b5b0-9be3b12c7626",
            "timestamp": 1445264488.0,
            "topic": "org.fedoraproject.prod.bodhi.buildroot_override.untag"
        },
        {
            "i": 12,
            "msg": {
                "override": {
                    "build": {
                        "nvr": "golang-github-jfrazelle-go-0-0.1.git6e461eb.fc21"
                    },
                    "build_id": 55578,
                    "expiration_date": "2015-11-07 00:00:00",
                    "expired_date": None,
                    "notes": "Override",
                    "nvr": "golang-github-jfrazelle-go-0-0.1.git6e461eb.fc21",
                    "submission_date": "2015-10-19 14:21:25",
                    "submitter": {
                        "avatar": None,
                        "email": "fpokorny@redhat.com",
                        "groups": [
                            {
                                "name": "packager"
                            }
                        ],
                        "id": 104,
                        "name": "fpokorny",
                        "openid": None
                    },
                    "submitter_id": 104
                }
            },
            "msg_id": "2015-264b6974-27c2-48c1-b2e0-2856c199c793",
            "timestamp": 1445264485.0,
            "topic": "org.fedoraproject.prod.bodhi.buildroot_override.untag"
        }
    ]
    expected = [{
        'subtitle': 'fpokorny expired 3 overrides for '
        'golang-github-bugsnag-panicwrap and golang-github-jfrazelle-go '
        'on el6, fc21, and fc23',
        'subjective': 'fpokorny expired 3 overrides for '
        'golang-github-bugsnag-panicwrap and golang-github-jfrazelle-go '
        'on el6, fc21, and fc23',
        'link': 'https://bodhi.fedoraproject.org/overrides/?user=fpokorny',
        'icon': 'https://apps.fedoraproject.org/img/icons/bodhi.png',
        'secondary_icon': 'https://seccdn.libravatar.org/avatar/'
        'b1b6c806cd1bbd4433ed428fe7625af0fbcca93ff469251b43f1860358fab9b1'
        '?s=64&d=retro',

        'start_time': 1445264485.0,
        'end_time': 1445264577.0,
        'timestamp': 1445264516.6666667,
        'human_time': arrow.get(1445264516.6666667).humanize(),

        'usernames': set(['fpokorny']),
        'packages': set([
            'golang-github-bugsnag-panicwrap',
            'golang-github-jfrazelle-go',
        ]),
        'topics': set(['org.fedoraproject.prod.bodhi.buildroot_override.untag']),
        'categories': set(['bodhi']),
        'msg_ids': [
            '2014-3db55159-6a93-4659-8eb7-19a24255df9c',
            '2014-8572040e-4456-48cc-b5c2-b457879e82ae',
        ],
    } ]
