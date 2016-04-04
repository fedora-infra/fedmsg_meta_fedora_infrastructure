import fedmsg.tests.test_meta
import arrow

import os


class TestMeetbotConglomerateByURL(
        fedmsg.tests.test_meta.ConglomerateBase):
    expected = [{
        'subtitle': u'alexove, echevemaster, and 4 others participated in Fedora Latam Ambassadors Meeting in #fedora-meeting-2',
        'subjective': u'alexove, echevemaster, and 4 others participated in Fedora Latam Ambassadors Meeting in #fedora-meeting-2',
        'secondary_icon': 'https://seccdn.libravatar.org/avatar/928a57107752819b7dd75177b094733dd4ea881dc0c68f4430fcf3ddc7610aa6?s=64&d=retro',
        'icon': 'https://apps.fedoraproject.org/img/icons/meetbot.png',
        'link': 'https://meetbot.fedoraproject.org/fedora-meeting-2/2016-03-05/fedora_latam_ambassadors_meeting.2016-03-05-23.13',

        'packages': set([]),
        'categories': set(['meetbot']),

        'timestamp': 1457220101.0,
        'start_time': 1457219627.0,
        'end_time': 1457221175.0,
        'human_time': arrow.get(1457220101.0).humanize(),

        'topics': set([
            'org.fedoraproject.prod.meetbot.meeting.complete',
            'org.fedoraproject.prod.meetbot.meeting.item.link',
            'org.fedoraproject.prod.meetbot.meeting.start',
            'org.fedoraproject.prod.meetbot.meeting.topic.update',
        ]),
        'usernames': set([
            'alexove',
            'echevemaster',
            'lorddemon',
            'srkraken',
            'yn1v',
        ])
    }, {
        'subjective': u'decause, jflory7, and 2 others participated in BrickHack 2016 - FOSS Contributions and Licensing in #fedora-meeting-4',
        'subtitle': u'decause, jflory7, and 2 others participated in BrickHack 2016 - FOSS Contributions and Licensing in #fedora-meeting-4',

        'categories': set(['meetbot']),
        'icon': 'https://apps.fedoraproject.org/img/icons/meetbot.png',
        'link': 'https://meetbot.fedoraproject.org/fedora-meeting-4/2016-03-05/famna.2016-03-05-22.00',
        'packages': set([]),
        'secondary_icon': 'https://seccdn.libravatar.org/avatar/70d3fd3ea028073bfab8d315504133b203992d4d8eb8daf1ca4397c222377ee6?s=64&d=retro',
        'timestamp': 1457218880.3333333,
        'start_time': 1457218567.0,
        'end_time': 1457219582.0,
        'human_time': arrow.get(1457218880.3333333).humanize(),
        'topics': set([
            'org.fedoraproject.prod.meetbot.meeting.complete',
            'org.fedoraproject.prod.meetbot.meeting.item.info',
            'org.fedoraproject.prod.meetbot.meeting.item.link',
        ]),
        'usernames': set(['decause', 'jflory7', 'mikedep333'])
    }]


    originals = [
        {
            "i": 651,
            "msg": {
                "attendees": {
                    "alexove": 11,
                    "echevemaster": 57,
                    "lorddemon": 8,
                    "srkraken": 3,
                    "yn1v": 24,
                    "zodbot": 9
                },
                "chairs": {
                    "echevemaster": True
                },
                "channel": "#fedora-meeting-2",
                "details": {
                    "line": "",
                    "linenum": 112,
                    "nick": "echevemaster",
                    "time_": 1457221175.0
                },
                "meeting_topic": "Fedora Latam Ambassadors Meeting",
                "owner": "echevemaster",
                "topic": "roll call",
                "url": "https://meetbot.fedoraproject.org/fedora-meeting-2/2016-03-05/fedora_latam_ambassadors_meeting.2016-03-05-23.13"
            },
            "msg_id": "2016-c054b4c5-9aa5-4392-a688-77de1ed7c22b",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1457221175.0,
            "topic": "org.fedoraproject.prod.meetbot.meeting.complete"
        },
        {
            "i": 650,
            "msg": {
                "attendees": {
                    "alexove": 2,
                    "echevemaster": 10,
                    "lorddemon": 3,
                    "srkraken": 2,
                    "yn1v": 9,
                    "zodbot": 8
                },
                "chairs": {
                    "echevemaster": True
                },
                "channel": "#fedora-meeting-2",
                "details": {
                    "line": "https://fedoraproject.org/wiki/Foro_UCR_2016",
                    "linenum": 34,
                    "nick": "yn1v",
                    "time_": 1457219965.0
                },
                "meeting_topic": "Fedora Latam Ambassadors Meeting",
                "owner": "echevemaster",
                "topic": "roll call",
                "url": "https://meetbot.fedoraproject.org/fedora-meeting-2/2016-03-05/fedora_latam_ambassadors_meeting.2016-03-05-23.13"
            },
            "msg_id": "2016-657de7d5-c221-465d-9a7a-21cc6caf1f47",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1457219965.0,
            "topic": "org.fedoraproject.prod.meetbot.meeting.item.link"
        },
        {
            "i": 649,
            "msg": {
                "attendees": {
                    "echevemaster": 2,
                    "zodbot": 3
                },
                "chairs": {
                    "echevemaster": True
                },
                "channel": "#fedora-meeting-2",
                "details": {
                    "line": "roll call",
                    "linenum": 5,
                    "nick": "echevemaster",
                    "time_": 1457219637.0
                },
                "meeting_topic": "Fedora Latam Ambassadors Meeting",
                "owner": "echevemaster",
                "topic": "roll call",
                "url": "https://meetbot.fedoraproject.org/fedora-meeting-2/2016-03-05/fedora_latam_ambassadors_meeting.2016-03-05-23.13"
            },
            "msg_id": "2016-cf7710f9-1c19-4816-9d6f-1f75438325ad",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1457219637.0,
            "topic": "org.fedoraproject.prod.meetbot.meeting.topic.update"
        },
        {
            "i": 647,
            "msg": {
                "attendees": {
                    "echevemaster": 1
                },
                "chairs": {
                    "echevemaster": True
                },
                "channel": "#fedora-meeting-2",
                "details": {
                    "line": "Fedora Latam Ambassadors Meeting",
                    "linenum": 1,
                    "nick": "echevemaster",
                    "time_": 1457219627.0
                },
                "meeting_topic": "Fedora Latam Ambassadors Meeting",
                "owner": "echevemaster",
                "topic": "",
                "url": "https://meetbot.fedoraproject.org/fedora-meeting-2/2016-03-05/fedora_latam_ambassadors_meeting.2016-03-05-23.13"
            },
            "msg_id": "2016-90fa8f7e-af6e-4876-b5ea-a65dd9b440a6",
            "source_version": "0.6.5",
            "timestamp": 1457219627.0,
            "topic": "org.fedoraproject.prod.meetbot.meeting.start"
        },
        {
            "i": 646,
            "msg": {
                "attendees": {
                    "decause": 3,
                    "jflory7": 69,
                    "mikedep333": 35,
                    "zodbot": 8
                },
                "chairs": {
                    "decause": True,
                    "jflory7": True,
                    "mikedep333": True
                },
                "channel": "#fedora-meeting-4",
                "details": {
                    "line": "",
                    "linenum": 115,
                    "nick": "jflory7",
                    "time_": 1457219582.0
                },
                "meeting_topic": "BrickHack 2016 - FOSS Contributions and Licensing",
                "owner": "jflory7",
                "topic": "Questions & Answers",
                "url": "https://meetbot.fedoraproject.org/fedora-meeting-4/2016-03-05/famna.2016-03-05-22.00"
            },
            "msg_id": "2016-06dbd60e-259e-4125-a1fd-63add8a5c205",
            "source_name": "datanommer",
            "timestamp": 1457219582.0,
            "topic": "org.fedoraproject.prod.meetbot.meeting.complete"
        },
        {
            "i": 644,
            "msg": {
                "attendees": {
                    "decause": 3,
                    "jflory7": 68,
                    "mikedep333": 35,
                    "zodbot": 8
                },
                "chairs": {
                    "decause": True,
                    "jflory7": True,
                    "mikedep333": True
                },
                "channel": "#fedora-meeting-4",
                "details": {
                    "line": "https://lists.fedoraproject.org/archives/list/commops@lists.fedoraproject.org/",
                    "linenum": 114,
                    "nick": "jflory7",
                    "time_": 1457219168.0
                },
                "meeting_topic": "BrickHack 2016 - FOSS Contributions and Licensing",
                "owner": "jflory7",
                "topic": "Questions & Answers",
                "url": "https://meetbot.fedoraproject.org/fedora-meeting-4/2016-03-05/famna.2016-03-05-22.00"
            },
            "msg_id": "2016-f4f3af68-986f-48b1-a31e-d1463de2bfe6",
            "source_version": "0.6.5",
            "timestamp": 1457219168.0,
            "topic": "org.fedoraproject.prod.meetbot.meeting.item.link"
        },
        {
            "i": 643,
            "msg": {
                "attendees": {
                    "decause": 3,
                    "jflory7": 67,
                    "mikedep333": 35,
                    "zodbot": 8
                },
                "chairs": {
                    "decause": True,
                    "jflory7": True,
                    "mikedep333": True
                },
                "channel": "#fedora-meeting-4",
                "details": {
                    "line": "Check out the #fedora-commops IRC channel on Freenode!",
                    "linenum": 113,
                    "nick": "jflory7",
                    "time_": 1457219127.0
                },
                "meeting_topic": "BrickHack 2016 - FOSS Contributions and Licensing",
                "owner": "jflory7",
                "topic": "Questions & Answers",
                "url": "https://meetbot.fedoraproject.org/fedora-meeting-4/2016-03-05/famna.2016-03-05-22.00"
            },
            "msg_id": "2016-7c134589-30e8-4c70-8ebf-d98dc5403576",
            "source_name": "datanommer",
            "timestamp": 1457219127.0,
            "topic": "org.fedoraproject.prod.meetbot.meeting.item.info"
        },
        {
            "i": 642,
            "msg": {
                "attendees": {
                    "decause": 3,
                    "jflory7": 66,
                    "mikedep333": 35,
                    "zodbot": 8
                },
                "chairs": {
                    "decause": True,
                    "jflory7": True,
                    "mikedep333": True
                },
                "channel": "#fedora-meeting-4",
                "details": {
                    "line": "Remy works on the Community Operations (CommOps) team and is *super* glad to help anyone get started",
                    "linenum": 112,
                    "nick": "jflory7",
                    "time_": 1457219105.0
                },
                "meeting_topic": "BrickHack 2016 - FOSS Contributions and Licensing",
                "owner": "jflory7",
                "topic": "Questions & Answers",
                "url": "https://meetbot.fedoraproject.org/fedora-meeting-4/2016-03-05/famna.2016-03-05-22.00"
            },
            "msg_id": "2016-ccce4b2a-937b-4c30-bfd2-818777a39201",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1457219105.0,
            "topic": "org.fedoraproject.prod.meetbot.meeting.item.info"
        },
        {
            "i": 641,
            "msg": {
                "attendees": {
                    "decause": 3,
                    "jflory7": 65,
                    "mikedep333": 35,
                    "zodbot": 8
                },
                "chairs": {
                    "decause": True,
                    "jflory7": True,
                    "mikedep333": True
                },
                "channel": "#fedora-meeting-4",
                "details": {
                    "line": "Choose your own adventure! The above site is a sorting hat that can help you choose a place to contribute",
                    "linenum": 111,
                    "nick": "jflory7",
                    "time_": 1457219084.0
                },
                "meeting_topic": "BrickHack 2016 - FOSS Contributions and Licensing",
                "owner": "jflory7",
                "topic": "Questions & Answers",
                "url": "https://meetbot.fedoraproject.org/fedora-meeting-4/2016-03-05/famna.2016-03-05-22.00"
            },
            "msg_id": "2016-c7976d40-e70c-46cf-98e1-6c0f1a8b8aff",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1457219084.0,
            "topic": "org.fedoraproject.prod.meetbot.meeting.item.info"
        },
        {
            "i": 640,
            "msg": {
                "attendees": {
                    "decause": 3,
                    "jflory7": 64,
                    "mikedep333": 35,
                    "zodbot": 8
                },
                "chairs": {
                    "decause": True,
                    "jflory7": True,
                    "mikedep333": True
                },
                "channel": "#fedora-meeting-4",
                "details": {
                    "line": "http://whatcanidoforfedora.org/",
                    "linenum": 110,
                    "nick": "jflory7",
                    "time_": 1457219045.0
                },
                "meeting_topic": "BrickHack 2016 - FOSS Contributions and Licensing",
                "owner": "jflory7",
                "topic": "Questions & Answers",
                "url": "https://meetbot.fedoraproject.org/fedora-meeting-4/2016-03-05/famna.2016-03-05-22.00"
            },
            "msg_id": "2016-2a374faf-0ec9-4d3d-95bc-64fc2ec4828a",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1457219045.0,
            "topic": "org.fedoraproject.prod.meetbot.meeting.item.link"
        },
        {
            "i": 639,
            "msg": {
                "attendees": {
                    "decause": 3,
                    "jflory7": 63,
                    "mikedep333": 35,
                    "zodbot": 8
                },
                "chairs": {
                    "decause": True,
                    "jflory7": True,
                    "mikedep333": True
                },
                "channel": "#fedora-meeting-4",
                "details": {
                    "line": "Q: \"Fedora looks cool but how can I contribute?\"",
                    "linenum": 109,
                    "nick": "jflory7",
                    "time_": 1457219041.0
                },
                "meeting_topic": "BrickHack 2016 - FOSS Contributions and Licensing",
                "owner": "jflory7",
                "topic": "Questions & Answers",
                "url": "https://meetbot.fedoraproject.org/fedora-meeting-4/2016-03-05/famna.2016-03-05-22.00"
            },
            "msg_id": "2016-781a5269-d215-448f-ac52-cd0714bcfb4d",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1457219041.0,
            "topic": "org.fedoraproject.prod.meetbot.meeting.item.info"
        },
        {
            "i": 638,
            "msg": {
                "attendees": {
                    "decause": 3,
                    "jflory7": 62,
                    "mikedep333": 35,
                    "zodbot": 8
                },
                "chairs": {
                    "decause": True,
                    "jflory7": True,
                    "mikedep333": True
                },
                "channel": "#fedora-meeting-4",
                "details": {
                    "line": "Email licensing@fsf.org for 1x1 advice or help",
                    "linenum": 108,
                    "nick": "jflory7",
                    "time_": 1457218955.0
                },
                "meeting_topic": "BrickHack 2016 - FOSS Contributions and Licensing",
                "owner": "jflory7",
                "topic": "Questions & Answers",
                "url": "https://meetbot.fedoraproject.org/fedora-meeting-4/2016-03-05/famna.2016-03-05-22.00"
            },
            "msg_id": "2016-f09d3931-5e72-47ee-aa1e-186aaece1061",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1457218955.0,
            "topic": "org.fedoraproject.prod.meetbot.meeting.item.info"
        },
        {
            "i": 637,
            "msg": {
                "attendees": {
                    "decause": 3,
                    "jflory7": 61,
                    "mikedep333": 35,
                    "zodbot": 8
                },
                "chairs": {
                    "decause": True,
                    "jflory7": True,
                    "mikedep333": True
                },
                "channel": "#fedora-meeting-4",
                "details": {
                    "line": "https://sfconservancy.org/",
                    "linenum": 107,
                    "nick": "jflory7",
                    "time_": 1457218925.0
                },
                "meeting_topic": "BrickHack 2016 - FOSS Contributions and Licensing",
                "owner": "jflory7",
                "topic": "Questions & Answers",
                "url": "https://meetbot.fedoraproject.org/fedora-meeting-4/2016-03-05/famna.2016-03-05-22.00"
            },
            "msg_id": "2016-cbe4fd33-b075-4e85-9fef-54015cb237d8",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1457218925.0,
            "topic": "org.fedoraproject.prod.meetbot.meeting.item.link"
        },
        {
            "i": 636,
            "msg": {
                "attendees": {
                    "decause": 3,
                    "jflory7": 60,
                    "mikedep333": 35,
                    "zodbot": 8
                },
                "chairs": {
                    "decause": True,
                    "jflory7": True,
                    "mikedep333": True
                },
                "channel": "#fedora-meeting-4",
                "details": {
                    "line": "Questions about FOSS legal?? Not sure who to ask??",
                    "linenum": 106,
                    "nick": "jflory7",
                    "time_": 1457218905.0
                },
                "meeting_topic": "BrickHack 2016 - FOSS Contributions and Licensing",
                "owner": "jflory7",
                "topic": "Questions & Answers",
                "url": "https://meetbot.fedoraproject.org/fedora-meeting-4/2016-03-05/famna.2016-03-05-22.00"
            },
            "msg_id": "2016-f3a8d1fa-1421-42b4-85b2-66ff7d48d167",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1457218905.0,
            "topic": "org.fedoraproject.prod.meetbot.meeting.item.info"
        },
        {
            "i": 635,
            "msg": {
                "attendees": {
                    "decause": 3,
                    "jflory7": 59,
                    "mikedep333": 35,
                    "zodbot": 8
                },
                "chairs": {
                    "decause": True,
                    "jflory7": True,
                    "mikedep333": True
                },
                "channel": "#fedora-meeting-4",
                "details": {
                    "line": "There are many layers to this in a legal aspect and technological literacy to the nth degree is important",
                    "linenum": 105,
                    "nick": "jflory7",
                    "time_": 1457218854.0
                },
                "meeting_topic": "BrickHack 2016 - FOSS Contributions and Licensing",
                "owner": "jflory7",
                "topic": "Questions & Answers",
                "url": "https://meetbot.fedoraproject.org/fedora-meeting-4/2016-03-05/famna.2016-03-05-22.00"
            },
            "msg_id": "2016-0280bf12-c02e-4496-a0b0-a4ee82903670",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1457218854.0,
            "topic": "org.fedoraproject.prod.meetbot.meeting.item.info"
        },
        {
            "i": 634,
            "msg": {
                "attendees": {
                    "decause": 3,
                    "jflory7": 58,
                    "mikedep333": 35,
                    "zodbot": 8
                },
                "chairs": {
                    "decause": True,
                    "jflory7": True,
                    "mikedep333": True
                },
                "channel": "#fedora-meeting-4",
                "details": {
                    "line": "NOTE REMY IS NOT A LAWYER AND THIS DOES NOT CONSTITUTE LEGAL ADVICE",
                    "linenum": 104,
                    "nick": "jflory7",
                    "time_": 1457218779.0
                },
                "meeting_topic": "BrickHack 2016 - FOSS Contributions and Licensing",
                "owner": "jflory7",
                "topic": "Questions & Answers",
                "url": "https://meetbot.fedoraproject.org/fedora-meeting-4/2016-03-05/famna.2016-03-05-22.00"
            },
            "msg_id": "2016-f336da43-7c1e-4b8d-a03d-04163e2e8c49",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1457218779.0,
            "topic": "org.fedoraproject.prod.meetbot.meeting.item.info"
        },
        {
            "i": 633,
            "msg": {
                "attendees": {
                    "decause": 3,
                    "jflory7": 57,
                    "mikedep333": 35,
                    "zodbot": 8
                },
                "chairs": {
                    "decause": True,
                    "jflory7": True,
                    "mikedep333": True
                },
                "channel": "#fedora-meeting-4",
                "details": {
                    "line": "Changing a license is a very permanent thing -- you need 100% agreement by all contributors ever to change the license",
                    "linenum": 103,
                    "nick": "jflory7",
                    "time_": 1457218762.0
                },
                "meeting_topic": "BrickHack 2016 - FOSS Contributions and Licensing",
                "owner": "jflory7",
                "topic": "Questions & Answers",
                "url": "https://meetbot.fedoraproject.org/fedora-meeting-4/2016-03-05/famna.2016-03-05-22.00"
            },
            "msg_id": "2016-237af8bc-c7bd-4f87-9b35-93ad425e18fd",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1457218762.0,
            "topic": "org.fedoraproject.prod.meetbot.meeting.item.info"
        },
        {
            "i": 632,
            "msg": {
                "attendees": {
                    "decause": 3,
                    "jflory7": 56,
                    "mikedep333": 35,
                    "zodbot": 8
                },
                "chairs": {
                    "decause": True,
                    "jflory7": True,
                    "mikedep333": True
                },
                "channel": "#fedora-meeting-4",
                "details": {
                    "line": "In Fedora, you can use any list of approved licenses, if you don't specify, it defaults to MIT (permissive) license",
                    "linenum": 102,
                    "nick": "jflory7",
                    "time_": 1457218738.0
                },
                "meeting_topic": "BrickHack 2016 - FOSS Contributions and Licensing",
                "owner": "jflory7",
                "topic": "Questions & Answers",
                "url": "https://meetbot.fedoraproject.org/fedora-meeting-4/2016-03-05/famna.2016-03-05-22.00"
            },
            "msg_id": "2016-66cf6ebc-5604-4a7b-892a-1af856bc86d4",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1457218738.0,
            "topic": "org.fedoraproject.prod.meetbot.meeting.item.info"
        },
        {
            "i": 631,
            "msg": {
                "attendees": {
                    "decause": 3,
                    "jflory7": 55,
                    "mikedep333": 35,
                    "zodbot": 8
                },
                "chairs": {
                    "decause": True,
                    "jflory7": True,
                    "mikedep333": True
                },
                "channel": "#fedora-meeting-4",
                "details": {
                    "line": "Often you sign a Contributor Licensing Agreement that defines the terms",
                    "linenum": 101,
                    "nick": "jflory7",
                    "time_": 1457218714.0
                },
                "meeting_topic": "BrickHack 2016 - FOSS Contributions and Licensing",
                "owner": "jflory7",
                "topic": "Questions & Answers",
                "url": "https://meetbot.fedoraproject.org/fedora-meeting-4/2016-03-05/famna.2016-03-05-22.00"
            },
            "msg_id": "2016-6e8a812b-fdbe-4674-b25f-9d734509e485",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1457218714.0,
            "topic": "org.fedoraproject.prod.meetbot.meeting.item.info"
        },
        {
            "i": 630,
            "msg": {
                "attendees": {
                    "decause": 3,
                    "jflory7": 54,
                    "mikedep333": 35,
                    "zodbot": 8
                },
                "chairs": {
                    "decause": True,
                    "jflory7": True,
                    "mikedep333": True
                },
                "channel": "#fedora-meeting-4",
                "details": {
                    "line": "Imagine a timeline -- there's different milestones that can factor into when or how the code licensing can be changed",
                    "linenum": 100,
                    "nick": "jflory7",
                    "time_": 1457218699.0
                },
                "meeting_topic": "BrickHack 2016 - FOSS Contributions and Licensing",
                "owner": "jflory7",
                "topic": "Questions & Answers",
                "url": "https://meetbot.fedoraproject.org/fedora-meeting-4/2016-03-05/famna.2016-03-05-22.00"
            },
            "msg_id": "2016-e26c466e-b654-4703-98ec-29fad51d416a",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1457218699.0,
            "topic": "org.fedoraproject.prod.meetbot.meeting.item.info"
        },
        {
            "i": 629,
            "msg": {
                "attendees": {
                    "decause": 3,
                    "jflory7": 53,
                    "mikedep333": 35,
                    "zodbot": 8
                },
                "chairs": {
                    "decause": True,
                    "jflory7": True,
                    "mikedep333": True
                },
                "channel": "#fedora-meeting-4",
                "details": {
                    "line": "Licensing: Difficult to go from copyleft to permissive, easier the other way around",
                    "linenum": 99,
                    "nick": "jflory7",
                    "time_": 1457218664.0
                },
                "meeting_topic": "BrickHack 2016 - FOSS Contributions and Licensing",
                "owner": "jflory7",
                "topic": "Questions & Answers",
                "url": "https://meetbot.fedoraproject.org/fedora-meeting-4/2016-03-05/famna.2016-03-05-22.00"
            },
            "msg_id": "2016-27a0e6fc-4d99-4fdc-8194-06b451f9d9e9",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1457218664.0,
            "topic": "org.fedoraproject.prod.meetbot.meeting.item.info"
        },
        {
            "i": 628,
            "msg": {
                "attendees": {
                    "decause": 3,
                    "jflory7": 52,
                    "mikedep333": 35,
                    "zodbot": 8
                },
                "chairs": {
                    "decause": True,
                    "jflory7": True,
                    "mikedep333": True
                },
                "channel": "#fedora-meeting-4",
                "details": {
                    "line": "To get contributors: Have clear on-boarding paths, have good docs, have good communication (not \"RTFM or get out\")",
                    "linenum": 98,
                    "nick": "jflory7",
                    "time_": 1457218620.0
                },
                "meeting_topic": "BrickHack 2016 - FOSS Contributions and Licensing",
                "owner": "jflory7",
                "topic": "Questions & Answers",
                "url": "https://meetbot.fedoraproject.org/fedora-meeting-4/2016-03-05/famna.2016-03-05-22.00"
            },
            "msg_id": "2016-5a62f199-475f-4aaf-a60b-0273507c32f4",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1457218620.0,
            "topic": "org.fedoraproject.prod.meetbot.meeting.item.info"
        },
        {
            "i": 627,
            "msg": {
                "attendees": {
                    "decause": 3,
                    "jflory7": 51,
                    "mikedep333": 35,
                    "zodbot": 8
                },
                "chairs": {
                    "decause": True,
                    "jflory7": True,
                    "mikedep333": True
                },
                "channel": "#fedora-meeting-4",
                "details": {
                    "line": "Many different reasons people contribute to open source",
                    "linenum": 97,
                    "nick": "jflory7",
                    "time_": 1457218581.0
                },
                "meeting_topic": "BrickHack 2016 - FOSS Contributions and Licensing",
                "owner": "jflory7",
                "topic": "Questions & Answers",
                "url": "https://meetbot.fedoraproject.org/fedora-meeting-4/2016-03-05/famna.2016-03-05-22.00"
            },
            "msg_id": "2016-0546d52d-cf1b-4292-883e-5c4b4dc09dcf",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1457218581.0,
            "topic": "org.fedoraproject.prod.meetbot.meeting.item.info"
        },
        {
            "i": 626,
            "msg": {
                "attendees": {
                    "decause": 3,
                    "jflory7": 50,
                    "mikedep333": 35,
                    "zodbot": 8
                },
                "chairs": {
                    "decause": True,
                    "jflory7": True,
                    "mikedep333": True
                },
                "channel": "#fedora-meeting-4",
                "details": {
                    "line": "After that, it comes down to culture",
                    "linenum": 96,
                    "nick": "jflory7",
                    "time_": 1457218572.0
                },
                "meeting_topic": "BrickHack 2016 - FOSS Contributions and Licensing",
                "owner": "jflory7",
                "topic": "Questions & Answers",
                "url": "https://meetbot.fedoraproject.org/fedora-meeting-4/2016-03-05/famna.2016-03-05-22.00"
            },
            "msg_id": "2016-45d354ce-a272-4a56-a9cf-160dc690e474",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1457218572.0,
            "topic": "org.fedoraproject.prod.meetbot.meeting.item.info"
        },
        {
            "i": 625,
            "msg": {
                "attendees": {
                    "decause": 3,
                    "jflory7": 49,
                    "mikedep333": 35,
                    "zodbot": 8
                },
                "chairs": {
                    "decause": True,
                    "jflory7": True,
                    "mikedep333": True
                },
                "channel": "#fedora-meeting-4",
                "details": {
                    "line": "In FOSS, if you scratch an \"itch\" for something that someone has, there's a good chance someone will find you",
                    "linenum": 95,
                    "nick": "jflory7",
                    "time_": 1457218567.0
                },
                "meeting_topic": "BrickHack 2016 - FOSS Contributions and Licensing",
                "owner": "jflory7",
                "topic": "Questions & Answers",
                "url": "https://meetbot.fedoraproject.org/fedora-meeting-4/2016-03-05/famna.2016-03-05-22.00"
            },
            "msg_id": "2016-5e6623a2-c62b-420c-905c-04ccbb5cef48",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1457218567.0,
            "topic": "org.fedoraproject.prod.meetbot.meeting.item.info"
        }
    ]


if 'FEDMSG_META_NO_NETWORK' in os.environ:
    TestMeetbotConglomerateByURL = None
