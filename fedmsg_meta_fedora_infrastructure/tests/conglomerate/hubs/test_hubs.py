# -*- coding: utf-8 -*-

import fedmsg.tests.test_meta
import arrow


class TestHubsConglomerateHubUpdated(
        fedmsg.tests.test_meta.ConglomerateBase):
    originals = [
        {
            "i": 1,
            "msg": {
                "changed_keys": [
                    "description"
                ],
                "hub_id": 9,
                "hub_name": "abompard",
                "hub_type": "user",
                "hub_url": "https://hubs.fedoraproject.org/u/abompard/",
            },
            "msg_id": "2018-b61c3bd6-1851-4716-a5b3-799ddbe48b5f",
            "source_name": "datanommer",
            "source_version": "0.8.2",
            "timestamp": 1519204726.0,
            "topic": "org.fedoraproject.stg.hubs.hub.updated",
            "username": "hubs"
        },
        {
            "i": 1,
            "msg": {
                "changed_keys": [
                    "pagure_username",
                    "github_username",
                    "bugzilla_email"
                ],
                "hub_id": 9,
                "hub_name": "abompard",
                "hub_type": "user",
                "hub_url": "https://hubs.fedoraproject.org/u/abompard/",
            },
            "msg_id": "2018-70d903c5-3637-49da-b13d-d8f35f3a4e51",
            "source_name": "datanommer",
            "source_version": "0.8.2",
            "timestamp": 1519204746.0,
            "topic": "org.fedoraproject.stg.hubs.hub.updated",
            "username": "hubs"
        },
    ]
    expected = [{
        'subtitle': "Hub abompard's configuration was changed 2 times",
        'subjective': "Hub abompard's configuration was changed 2 times",
        'link': 'https://hubs.fedoraproject.org/u/abompard/',
        'icon': 'https://hubs.fedoraproject.org/static/img/favicon.png',
        'secondary_icon': 'https://hubs.fedoraproject.org/static/img/favicon.png',
        'start_time': 1519204726.0,
        'end_time': 1519204746.0,
        'timestamp': 1519204736.0,
        'human_time': arrow.get(1519204736.0).humanize(),
        'usernames': set(),
        'topics': set(['org.fedoraproject.stg.hubs.hub.updated']),
        'categories': set(['hubs']),
        'packages': set(),
        'msg_ids': [
            "2018-b61c3bd6-1851-4716-a5b3-799ddbe48b5f",
            "2018-70d903c5-3637-49da-b13d-d8f35f3a4e51",
        ],
    } ]


class TestHubsConglomerateWidgetUpdated(
        fedmsg.tests.test_meta.ConglomerateBase):
    originals = [
        {
            "i": 1,
            "msg": {
                "changed_keys": [
                    "per_page"
                ],
                "hub_id": 9,
                "hub_name": "abompard",
                "hub_type": "user",
                "hub_url": "https://hubs.fedoraproject.org/u/abompard/",
                "widget_id": 72,
                "widget_label": "Library",
            },
            "msg_id": "2018-616bbb50-a35f-4e3d-b563-9a44ee4aa0af",
            "source_name": "datanommer",
            "source_version": "0.8.2",
            "timestamp": 1519308843.0,
            "topic": "org.fedoraproject.stg.hubs.widget.updated",
            "username": "hubs"
        },
        {
            "i": 2,
            "msg": {
                "changed_keys": [
                    "per_page"
                ],
                "hub_id": 9,
                "hub_name": "abompard",
                "hub_type": "user",
                "hub_url": "https://hubs.fedoraproject.org/u/abompard/",
                "widget_id": 72,
                "widget_label": "Library",
            },
            "msg_id": "2018-616bbb50-a35f-4e3d-b563-9a44ee4aa0a0",
            "source_name": "datanommer",
            "source_version": "0.8.2",
            "timestamp": 1519308844.0,
            "topic": "org.fedoraproject.stg.hubs.widget.updated",
            "username": "hubs"
        },
    ]
    expected = [{
        'subtitle': "On hub abompard, the configuration for widget "
                    "\"Library\" was changed 2 times",
        'subjective': "On hub abompard, the configuration for widget "
                      "\"Library\" was changed 2 times",
        'link': 'https://hubs.fedoraproject.org/u/abompard/',
        'icon': 'https://hubs.fedoraproject.org/static/img/favicon.png',
        'secondary_icon': 'https://hubs.fedoraproject.org/static/img/favicon.png',
        'start_time': 1519308843.0,
        'end_time': 1519308844.0,
        'timestamp': 1519308843.5,
        'human_time': arrow.get(1519308843.5).humanize(),
        'usernames': set(),
        'topics': set(['org.fedoraproject.stg.hubs.widget.updated']),
        'categories': set(['hubs']),
        'packages': set(),
        'msg_ids': [
            "2018-616bbb50-a35f-4e3d-b563-9a44ee4aa0af",
            "2018-616bbb50-a35f-4e3d-b563-9a44ee4aa0a0",
        ],
    } ]
