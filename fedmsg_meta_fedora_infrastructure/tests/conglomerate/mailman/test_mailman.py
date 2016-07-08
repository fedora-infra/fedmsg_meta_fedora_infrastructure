import fedmsg.tests.test_meta

import arrow


class TestMailmanConglomerateByMessageId(
        fedmsg.tests.test_meta.ConglomerateBase):
    expected = [
        {
            'categories': set(['mailman']),
            'end_time': 1450110137.0,
            'human_time': arrow.get(1450058909.6923077).humanize(),
            'icon': 'https://apps.fedoraproject.org/img/icons/hyperkitty.png',
            'link': 'http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/4OTZIFLXO7NQFH47S6BLPN45SBHOEA6P/',
            'packages': set([]),
            'secondary_icon': 'https://seccdn.libravatar.org/avatar/f73b95bc363f96a24ec56c1cca611dff?s=64&d=retro',
            'start_time': 1449998105.0,
            'subjective': u'ctubbsii-fedora@apache.org, fdeutsch@redhat.com, and 6 others wrote 13 replies to the "Easier %config management?" thread on the devel list',
            'subtitle': u'ctubbsii-fedora@apache.org, fdeutsch@redhat.com, and 6 others wrote 13 replies to the "Easier %config management?" thread on the devel list',
            'timestamp': 1450058909.6923077,
            'topics': set(['org.fedoraproject.prod.mailman.receive']),
            'usernames': set([])
        }, {
            'categories': set(['mailman']),
            'end_time': 1450107961.0,
            'human_time': arrow.get(1450107961.0).humanize(),
            'icon': 'https://apps.fedoraproject.org/img/icons/hyperkitty.png',
            'link': 'http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/N5VA2ZFGOQBKWUWWEIL4TBFWIT7Q74E2/',
            'packages': set([]),
            'secondary_icon': 'https://seccdn.libravatar.org/avatar/6382b3cc881412b77bfcaeed026001c00d9e3025e66c20f6e7e92f079851462a?s=64&d=retro',
            'start_time': 1450107961.0,
            'subjective': u"nobody wrote '[POC-change] Fedora packages point of contact updates' to the devel list",
            'subtitle': u"nobody wrote '[POC-change] Fedora packages point of contact updates' to the devel list",
            'timestamp': 1450107961.0,
            'topics': set(['org.fedoraproject.prod.mailman.receive']),
            'usernames': set(['nobody']),
        }, {
            'categories': set(['mailman']),
            'end_time': 1450106384.0,
            'human_time': arrow.get(1450106384.0).humanize(),
            'icon': 'https://apps.fedoraproject.org/img/icons/hyperkitty.png',
            'link': 'http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/MWGTN2OLUOKCFYDS4XNFMWHUJ3C5FHT5/',
            'packages': set([]),
            'secondary_icon': 'https://seccdn.libravatar.org/avatar/71630da8f590ff926d611abe228bd7f4a8935f09908ebe69ba3a2362c2d6fc5c?s=64&d=retro',
            'start_time': 1450106384.0,
            'subjective': u"rawhide wrote 'Fedora Rawhide 20151214 compose check report' to the devel list",
            'subtitle': u"rawhide wrote 'Fedora Rawhide 20151214 compose check report' to the devel list",
            'timestamp': 1450106384.0,
            'topics': set(['org.fedoraproject.prod.mailman.receive']),
            'usernames': set(['rawhide']),
        }, {
            'categories': set(['mailman']),
            'end_time': 1450104230.0,
            'human_time': arrow.get(1450104230.0).humanize(),
            'icon': 'https://apps.fedoraproject.org/img/icons/hyperkitty.png',
            'link': 'http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/GLDIH254AMANCVIQVOJ2JNOVAU6C32IT/',
            'packages': set([]),
            'secondary_icon': 'https://seccdn.libravatar.org/avatar/579f49f7c4d9f8763d6733e31568dd1a?s=64&d=retro',
            'start_time': 1450104230.0,
            'subjective': u"On the devel list, pwouters@redhat.com replied to 'Re: F24 System Wide Change: Default Local DNS Resolver'",
            'subtitle': u"On the devel list, pwouters@redhat.com replied to 'Re: F24 System Wide Change: Default Local DNS Resolver'",
            'timestamp': 1450104230.0,
            'topics': set(['org.fedoraproject.prod.mailman.receive']),
            'usernames': set([]),
        }, {
            'categories': set(['mailman']),
            'end_time': 1450093963.0,
            'human_time': arrow.get(1450093963.0).humanize(),
            'icon': 'https://apps.fedoraproject.org/img/icons/hyperkitty.png',
            'link': 'http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/BLDNP6AOSH2GH3V5OUWFOLMNLMC46OVT/',
            'packages': set([]),
            'secondary_icon': 'https://seccdn.libravatar.org/avatar/eb3db1dface818fe81cc1dce5e8ac680?s=64&d=retro',
            'start_time': 1450093963.0,
            'subjective': u"jkurik@redhat.com wrote '[Elections] Reminder : Voting Period Ends Today' to the devel list",
            'subtitle': u"jkurik@redhat.com wrote '[Elections] Reminder : Voting Period Ends Today' to the devel list",
            'timestamp': 1450093963.0,
            'topics': set(['org.fedoraproject.prod.mailman.receive']),
            'usernames': set([]),
        }, {
            'categories': set(['mailman']),
            'end_time': 1450089571.0,
            'human_time': arrow.get(1450089571.0).humanize(),
            'icon': 'https://apps.fedoraproject.org/img/icons/hyperkitty.png',
            'link': 'http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/YLFK7I4HTRJ6BBXOCMG5ZX5HCT3SNBSN/',
            'packages': set([]),
            'secondary_icon': 'https://seccdn.libravatar.org/avatar/71630da8f590ff926d611abe228bd7f4a8935f09908ebe69ba3a2362c2d6fc5c?s=64&d=retro',
            'start_time': 1450089571.0,
            'subjective': u"rawhide wrote 'rawhide report: 20151214 changes' to the devel list",
            'subtitle': u"rawhide wrote 'rawhide report: 20151214 changes' to the devel list",
            'timestamp': 1450089571.0,
            'topics': set(['org.fedoraproject.prod.mailman.receive']),
            'usernames': set(['rawhide']),
        }, {
            'categories': set(['mailman']),
            'end_time': 1450062083.0,
            'human_time': arrow.get(1450062083.0).humanize(),
            'icon': 'https://apps.fedoraproject.org/img/icons/hyperkitty.png',
            'link': 'http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/UQF6BKC5E22TDEL34TIXGTCEPSTVXSCM/',
            'packages': set([]),
            'secondary_icon': 'https://seccdn.libravatar.org/avatar/8213db2eb8fc1e9d78f70bcba52e4b379e44f662792e0e0407fb67ff168aeaee?s=64&d=retro',
            'start_time': 1450062083.0,
            'subjective': u"adamwill wrote '[Test-Announce] Proposal to CANCEL: 2015-12-14 Fedora QA Meeting' to the devel list",
            'subtitle': u"adamwill wrote '[Test-Announce] Proposal to CANCEL: 2015-12-14 Fedora QA Meeting' to the devel list",
            'timestamp': 1450062083.0,
            'topics': set(['org.fedoraproject.prod.mailman.receive']),
            'usernames': set(['adamwill']),
        }, {
            'categories': set(['mailman']),
            'end_time': 1450019998.0,
            'human_time': arrow.get(1450019998.0).humanize(),
            'icon': 'https://apps.fedoraproject.org/img/icons/hyperkitty.png',
            'link': 'http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/WXYKNWQN5HOMEP2XDQOSH56RK4JHBJUO/',
            'packages': set([]),
            'secondary_icon': 'https://seccdn.libravatar.org/avatar/71630da8f590ff926d611abe228bd7f4a8935f09908ebe69ba3a2362c2d6fc5c?s=64&d=retro',
            'start_time': 1450019998.0,
            'subjective': u"rawhide wrote 'Fedora Rawhide 20151213 compose check report' to the devel list",
            'subtitle': u"rawhide wrote 'Fedora Rawhide 20151213 compose check report' to the devel list",
            'timestamp': 1450019998.0,
            'topics': set(['org.fedoraproject.prod.mailman.receive']),
            'usernames': set(['rawhide']),
        }, {
            'categories': set(['mailman']),
            'end_time': 1450015355.0,
            'human_time': arrow.get(1450015355.0).humanize(),
            'icon': 'https://apps.fedoraproject.org/img/icons/hyperkitty.png',
            'link': 'http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/HPBHTMMCDAUU5ZMTUJCPFIERWZEHDNGG/',
            'packages': set([]),
            'secondary_icon': 'https://seccdn.libravatar.org/avatar/8de2bbf335b88faa16fefdb63281ed0c?s=64&d=retro',
            'start_time': 1450015355.0,
            'subjective': u"On the devel list, jpesco@gmx.com replied to 'Re: REMINDER: FESCo, Council, FAmSCo elections'",
            'subtitle': u"On the devel list, jpesco@gmx.com replied to 'Re: REMINDER: FESCo, Council, FAmSCo elections'",
            'timestamp': 1450015355.0,
            'topics': set(['org.fedoraproject.prod.mailman.receive']),
            'usernames': set([]),
        }, {
            'categories': set(['mailman']),
            'end_time': 1450012283.0,
            'human_time': arrow.get(1450012283.0).humanize(),
            'icon': 'https://apps.fedoraproject.org/img/icons/hyperkitty.png',
            'link': 'http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/3UGB7MTFX6KBXHUNYNRG3EJ5JB5T2HNP/',
            'packages': set([]),
            'secondary_icon': 'https://seccdn.libravatar.org/avatar/72d9d1481691ed08bf26954b3485d27d?s=64&d=retro',
            'start_time': 1450012283.0,
            'subjective': u"On the devel list, mschwendt@gmail.com replied to 'Re: dnf behavior expected?'",
            'subtitle': u"On the devel list, mschwendt@gmail.com replied to 'Re: dnf behavior expected?'",
            'timestamp': 1450012283.0,
            'topics': set(['org.fedoraproject.prod.mailman.receive']),
            'usernames': set([]),
        }, {
            'categories': set(['mailman']),
            'end_time': 1450002803.0,
            'human_time': arrow.get(1450002803.0).humanize(),
            'icon': 'https://apps.fedoraproject.org/img/icons/hyperkitty.png',
            'link': 'http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RDVKKW5QZZBFUXVQR32ZQ7N3DXMTBRRU/',
            'packages': set([]),
            'secondary_icon': 'https://seccdn.libravatar.org/avatar/71630da8f590ff926d611abe228bd7f4a8935f09908ebe69ba3a2362c2d6fc5c?s=64&d=retro',
            'start_time': 1450002803.0,
            'subjective': u"rawhide wrote 'rawhide report: 20151213 changes' to the devel list",
            'subtitle': u"rawhide wrote 'rawhide report: 20151213 changes' to the devel list",
            'timestamp': 1450002803.0,
            'topics': set(['org.fedoraproject.prod.mailman.receive']),
            'usernames': set(['rawhide']),
        }, {
            'categories': set(['mailman']),
            'end_time': 1449994343.0,
            'human_time': arrow.get(1449994281.0).humanize(),
            'icon': 'https://apps.fedoraproject.org/img/icons/hyperkitty.png',
            'link': 'http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/G6TQAZYKZF3KH6XW3SV6ZSW3MPARYG54/',
            'packages': set([]),
            'secondary_icon': 'https://seccdn.libravatar.org/avatar/5640a90bc0024f3300736f1a3527c9d1?s=64&d=retro',
            'start_time': 1449994219.0,
            'subjective': u'Bjorn@xn--rombobjrn-67a.se wrote 2 replies to the "Can Koji handle a soname change and a self-dependency?" thread on the devel list',
            'subtitle': u'Bjorn@xn--rombobjrn-67a.se wrote 2 replies to the "Can Koji handle a soname change and a self-dependency?" thread on the devel list',
            'timestamp': 1449994281.0,
            'topics': set(['org.fedoraproject.prod.mailman.receive']),
            'usernames': set([]),
        }
    ]


    originals = [
        {
            "i": 1285,
            "msg": {
                "mlist": {
                    "list_name": "devel"
                },
                "msg": {
                    "archived-at": "<http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/OFFAFTZZ6WU6SAAHDTYQRYIH76QFWPVN/>",
                    "cc": None,
                    "delivered-to": None,
                    "from": "Reindl Harald <h.reindl@thelounge.net>",
                    "in-reply-to": "<CAL5zq9bt8_aF-AhJHZsdAj-4gYs3cprq6XiCkG5bE1mqroFZdg@mail.gmail.com>",
                    "message-id": "<566EECA4.1060109@thelounge.net>",
                    "references": "<CAL5zq9ZYgmi+BejiUSA1HKa+wj_CSfQfFFoGA-VZHnMJ3bPz_g@mail.gmail.com>\n <CAObL_7HgBZgh1W0yJb0Pmfa2pBcwoz+J4e9z5y_qKrSbLLEkMA@mail.gmail.com>\n <566DD742.50607@thelounge.net>\n <CAL5zq9bt8_aF-AhJHZsdAj-4gYs3cprq6XiCkG5bE1mqroFZdg@mail.gmail.com>",
                    "subject": "Re: Easier %config management?",
                    "to": "devel@lists.fedoraproject.org",
                    "x-mailman-rule-hits": "member-moderation",
                    "x-mailman-rule-misses": "approved; emergency; loop",
                    "x-message-id-hash": "OFFAFTZZ6WU6SAAHDTYQRYIH76QFWPVN"
                }
            },
            "msg_id": "2015-d5fb3bff-a793-4cde-8ced-e63309bbba76",
            "timestamp": 1450110137.0,
            "topic": "org.fedoraproject.prod.mailman.receive"
        },
        {
            "i": 1269,
            "msg": {
                "mlist": {
                    "list_name": "devel"
                },
                "msg": {
                    "archived-at": "<http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/QIVQKUUJ5GJVFHOL7H7QSHLSV75MSBXF/>",
                    "cc": None,
                    "delivered-to": None,
                    "from": "Christopher <ctubbsii-fedora@apache.org>",
                    "in-reply-to": "<566DD742.50607@thelounge.net>",
                    "message-id": "<CAL5zq9bt8_aF-AhJHZsdAj-4gYs3cprq6XiCkG5bE1mqroFZdg@mail.gmail.com>",
                    "references": "<CAL5zq9ZYgmi+BejiUSA1HKa+wj_CSfQfFFoGA-VZHnMJ3bPz_g@mail.gmail.com>\n <CAObL_7HgBZgh1W0yJb0Pmfa2pBcwoz+J4e9z5y_qKrSbLLEkMA@mail.gmail.com> <566DD742.50607@thelounge.net>",
                    "subject": "Re: Easier %config management?",
                    "to": "Development discussions related to Fedora <devel@lists.fedoraproject.org>",
                    "x-mailman-rule-hits": "member-moderation",
                    "x-mailman-rule-misses": "approved; emergency; loop",
                    "x-message-id-hash": "QIVQKUUJ5GJVFHOL7H7QSHLSV75MSBXF"
                }
            },
            "msg_id": "2015-a4d4fabb-3ee4-4451-9f72-a668794c49a7",
            "timestamp": 1450108932.0,
            "topic": "org.fedoraproject.prod.mailman.receive"
        },
        {
            "i": 1264,
            "msg": {
                "mlist": {
                    "list_name": "devel"
                },
                "msg": {
                    "archived-at": "<http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/N5VA2ZFGOQBKWUWWEIL4TBFWIT7Q74E2/>",
                    "cc": None,
                    "delivered-to": None,
                    "from": "nobody@fedoraproject.org",
                    "in-reply-to": None,
                    "message-id": "<20151214100003.E03BD6099882@sundries01.phx2.fedoraproject.org>",
                    "references": None,
                    "subject": "[POC-change] Fedora packages point of contact updates",
                    "to": "devel@lists.fedoraproject.org",
                    "x-mailman-rule-hits": "nonmember-moderation",
                    "x-mailman-rule-misses": "approved; emergency; loop; member-moderation; header-match-40538; header-match-40539; header-match-40540; header-match-40541; header-match-40542; header-match-40543; header-match-40544",
                    "x-message-id-hash": "N5VA2ZFGOQBKWUWWEIL4TBFWIT7Q74E2"
                }
            },
            "msg_id": "2015-6e19ea40-2e0a-44f1-a2eb-0bce74de2070",
            "timestamp": 1450107961.0,
            "topic": "org.fedoraproject.prod.mailman.receive"
        },
        {
            "i": 1253,
            "msg": {
                "mlist": {
                    "list_name": "devel"
                },
                "msg": {
                    "archived-at": "<http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/FWGMQLVTDSXRT5RCI4YHIJ5TLC2EMPQH/>",
                    "cc": None,
                    "delivered-to": None,
                    "from": "Christopher <ctubbsii-fedora@apache.org>",
                    "in-reply-to": "<566DCBFD.3000704@thelounge.net>",
                    "message-id": "<CAL5zq9ZK4hdBqXuzrUcaowLfnSirHxg8+Oaf4yxTrMUbqJcRwQ@mail.gmail.com>",
                    "references": "<CAL5zq9ZYgmi+BejiUSA1HKa+wj_CSfQfFFoGA-VZHnMJ3bPz_g@mail.gmail.com>\n <566DCBFD.3000704@thelounge.net>",
                    "subject": "Re: Easier %config management?",
                    "to": "Development discussions related to Fedora <devel@lists.fedoraproject.org>",
                    "x-mailman-rule-hits": "member-moderation",
                    "x-mailman-rule-misses": "approved; emergency; loop",
                    "x-message-id-hash": "FWGMQLVTDSXRT5RCI4YHIJ5TLC2EMPQH"
                }
            },
            "msg_id": "2015-191c3c40-3e9f-47e9-b40d-c820b92d77d2",
            "timestamp": 1450106460.0,
            "topic": "org.fedoraproject.prod.mailman.receive"
        },
        {
            "i": 1251,
            "msg": {
                "mlist": {
                    "list_name": "devel"
                },
                "msg": {
                    "archived-at": "<http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/MWGTN2OLUOKCFYDS4XNFMWHUJ3C5FHT5/>",
                    "cc": None,
                    "delivered-to": None,
                    "from": "Fedora compose checker <rawhide@fedoraproject.org>",
                    "in-reply-to": None,
                    "message-id": "<20151214151926.4B8446062BF8@bastion01.phx2.fedoraproject.org>",
                    "references": None,
                    "subject": "Fedora Rawhide 20151214 compose check report",
                    "to": "test@lists.fedoraproject.org, devel@lists.fedoraproject.org",
                    "x-mailman-rule-hits": "member-moderation",
                    "x-mailman-rule-misses": "approved; emergency; loop",
                    "x-message-id-hash": "MWGTN2OLUOKCFYDS4XNFMWHUJ3C5FHT5"
                }
            },
            "msg_id": "2015-a9720f64-76e8-4274-8d9a-f87ee78ae25a",
            "timestamp": 1450106384.0,
            "topic": "org.fedoraproject.prod.mailman.receive"
        },
        {
            "i": 1213,
            "msg": {
                "mlist": {
                    "list_name": "devel"
                },
                "msg": {
                    "archived-at": "<http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/GLDIH254AMANCVIQVOJ2JNOVAU6C32IT/>",
                    "cc": "devel@lists.fedoraproject.org",
                    "delivered-to": None,
                    "from": "Paul Wouters <pwouters@redhat.com>",
                    "in-reply-to": "<6907000.gmhhBm2oPe@neon.home.il>",
                    "message-id": "<566ED390.8040603@redhat.com>",
                    "references": "<CA+Sa5FoQW2OYxWoTwWj3qrJ+rVEiievEqF3qP0G+5H3VA4JtMQ@mail.gmail.com>\n <22305478.k9qG4LVH1Z@neon.home.il> <566AD918.8070705@redhat.com>\n <6907000.gmhhBm2oPe@neon.home.il>",
                    "subject": "Re: F24 System Wide Change: Default Local DNS Resolver",
                    "to": "Oron Peled <oron@actcom.co.il>",
                    "x-mailman-rule-hits": "member-moderation",
                    "x-mailman-rule-misses": "approved; emergency; loop",
                    "x-message-id-hash": "GLDIH254AMANCVIQVOJ2JNOVAU6C32IT"
                }
            },
            "msg_id": "2015-287651b5-ed46-4943-9241-59ceb9aca191",
            "timestamp": 1450104230.0,
            "topic": "org.fedoraproject.prod.mailman.receive"
        },
        {
            "i": 1082,
            "msg": {
                "mlist": {
                    "list_name": "devel"
                },
                "msg": {
                    "archived-at": "<http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/BLDNP6AOSH2GH3V5OUWFOLMNLMC46OVT/>",
                    "cc": None,
                    "delivered-to": None,
                    "from": "Jan Kurik <jkurik@redhat.com>",
                    "in-reply-to": None,
                    "message-id": "<CA+Sa5FpvRehsPg_0jcKP79w5BDApxNSbM-yNFa3uWSM_ORE3AA@mail.gmail.com>",
                    "references": None,
                    "subject": "[Elections] Reminder : Voting Period Ends Today",
                    "to": "devel-announce@lists.fedoraproject.org, \n\tDevelopment discussions related to Fedora <devel@lists.fedoraproject.org>",
                    "x-mailman-rule-hits": "member-moderation",
                    "x-mailman-rule-misses": "approved; emergency; loop",
                    "x-message-id-hash": "BLDNP6AOSH2GH3V5OUWFOLMNLMC46OVT"
                }
            },
            "msg_id": "2015-26597411-4eca-4c4a-81e0-573a9308650d",
            "timestamp": 1450093963.0,
            "topic": "org.fedoraproject.prod.mailman.receive"
        },
        {
            "i": 1056,
            "msg": {
                "mlist": {
                    "list_name": "devel"
                },
                "msg": {
                    "archived-at": "<http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/YLFK7I4HTRJ6BBXOCMG5ZX5HCT3SNBSN/>",
                    "cc": None,
                    "delivered-to": None,
                    "from": "Fedora Rawhide Report <rawhide@fedoraproject.org>",
                    "in-reply-to": None,
                    "message-id": "<20151214103852.GA26839@rawhide-composer.phx2.fedoraproject.org>",
                    "references": None,
                    "subject": "rawhide report: 20151214 changes",
                    "to": "devel@lists.fedoraproject.org, test@lists.fedoraproject.org",
                    "x-mailman-rule-hits": "member-moderation",
                    "x-mailman-rule-misses": "approved; emergency; loop",
                    "x-message-id-hash": "YLFK7I4HTRJ6BBXOCMG5ZX5HCT3SNBSN"
                }
            },
            "msg_id": "2015-49e3b336-a560-46d4-8a2b-5e705073dd16",
            "timestamp": 1450089571.0,
            "topic": "org.fedoraproject.prod.mailman.receive"
        },
        {
            "i": 1038,
            "msg": {
                "mlist": {
                    "list_name": "devel"
                },
                "msg": {
                    "archived-at": "<http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/4OTZIFLXO7NQFH47S6BLPN45SBHOEA6P/>",
                    "cc": None,
                    "delivered-to": None,
                    "from": "Fabian Deutsch <fdeutsch@redhat.com>",
                    "in-reply-to": "<CAL5zq9ZYgmi+BejiUSA1HKa+wj_CSfQfFFoGA-VZHnMJ3bPz_g@mail.gmail.com>",
                    "message-id": "<CA+PVUaRf=1fM7djiP8Vtm97OjnyHBLAxpwDRvw6X5mwGOY+Kbg@mail.gmail.com>",
                    "references": "<CAL5zq9ZYgmi+BejiUSA1HKa+wj_CSfQfFFoGA-VZHnMJ3bPz_g@mail.gmail.com>",
                    "subject": "Re: Easier %config management?",
                    "to": "Development discussions related to Fedora <devel@lists.fedoraproject.org>",
                    "x-mailman-rule-hits": "member-moderation",
                    "x-mailman-rule-misses": "approved; emergency; loop",
                    "x-message-id-hash": "4OTZIFLXO7NQFH47S6BLPN45SBHOEA6P"
                }
            },
            "msg_id": "2015-c9d1afb8-0a80-4d6d-b389-76962b403f5f",
            "timestamp": 1450086838.0,
            "topic": "org.fedoraproject.prod.mailman.receive"
        },
        {
            "i": 984,
            "msg": {
                "mlist": {
                    "list_name": "devel"
                },
                "msg": {
                    "archived-at": "<http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/XL7UKU733VSUMO3CDQDME2IXSIHCIY2G/>",
                    "cc": None,
                    "delivered-to": None,
                    "from": "Panu Matilainen <pmatilai@laiskiainen.org>",
                    "in-reply-to": "<CAObL_7EYXGQP2Ow-jHj2gx=TBc1XOVSAw2=xoVk5q4nmB7o-Jg@mail.gmail.com>",
                    "message-id": "<566E7BAB.1010502@laiskiainen.org>",
                    "references": "<CAL5zq9ZYgmi+BejiUSA1HKa+wj_CSfQfFFoGA-VZHnMJ3bPz_g@mail.gmail.com>\n <CAObL_7HgBZgh1W0yJb0Pmfa2pBcwoz+J4e9z5y_qKrSbLLEkMA@mail.gmail.com>\n <566DD742.50607@thelounge.net>\n <CAObL_7EYXGQP2Ow-jHj2gx=TBc1XOVSAw2=xoVk5q4nmB7o-Jg@mail.gmail.com>",
                    "subject": "Re: Easier %config management?",
                    "to": "devel@lists.fedoraproject.org",
                    "x-mailman-rule-hits": "member-moderation",
                    "x-mailman-rule-misses": "approved; emergency; loop",
                    "x-message-id-hash": "XL7UKU733VSUMO3CDQDME2IXSIHCIY2G"
                }
            },
            "msg_id": "2015-fa768e7c-dc5f-4103-b59a-ec40dd634575",
            "timestamp": 1450081218.0,
            "topic": "org.fedoraproject.prod.mailman.receive"
        },
        {
            "i": 938,
            "msg": {
                "mlist": {
                    "list_name": "devel"
                },
                "msg": {
                    "archived-at": "<http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/UQF6BKC5E22TDEL34TIXGTCEPSTVXSCM/>",
                    "cc": None,
                    "delivered-to": None,
                    "from": "Adam Williamson <adamwill@fedoraproject.org>",
                    "in-reply-to": None,
                    "message-id": "<1450062061.7151.23.camel@fedoraproject.org>",
                    "references": None,
                    "subject": "[Test-Announce] Proposal to CANCEL: 2015-12-14 Fedora QA Meeting",
                    "to": "test-announce@lists.fedoraproject.org",
                    "x-mailman-rule-hits": "member-moderation",
                    "x-mailman-rule-misses": "approved; emergency; loop",
                    "x-message-id-hash": "UQF6BKC5E22TDEL34TIXGTCEPSTVXSCM"
                }
            },
            "msg_id": "2015-3b38a2b7-26c4-4f1b-979f-41807783bbbd",
            "timestamp": 1450062083.0,
            "topic": "org.fedoraproject.prod.mailman.receive"
        },
        {
            "i": 918,
            "msg": {
                "mlist": {
                    "list_name": "devel"
                },
                "msg": {
                    "archived-at": "<http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/BPOKLZCOCUFWMHTWKREVXKXD7D3C5A7L/>",
                    "cc": None,
                    "delivered-to": None,
                    "from": "Colin Walters <walters@verbum.org>",
                    "in-reply-to": "<20151213194131.GN26159@redhat.com>",
                    "message-id": "<1450044781.1619079.466286985.71F765CA@webmail.messagingengine.com>",
                    "references": "<CAL5zq9ZYgmi+BejiUSA1HKa+wj_CSfQfFFoGA-VZHnMJ3bPz_g@mail.gmail.com>\n <20151213194131.GN26159@redhat.com>",
                    "subject": "Re: Easier %config management?",
                    "to": "devel@lists.fedoraproject.org",
                    "x-mailman-rule-hits": "member-moderation",
                    "x-mailman-rule-misses": "approved; emergency; loop",
                    "x-message-id-hash": "BPOKLZCOCUFWMHTWKREVXKXD7D3C5A7L"
                }
            },
            "msg_id": "2015-75b64fc8-eb63-41ca-b9f3-87c8704a7e2e",
            "timestamp": 1450044801.0,
            "topic": "org.fedoraproject.prod.mailman.receive"
        },
        {
            "i": 914,
            "msg": {
                "mlist": {
                    "list_name": "devel"
                },
                "msg": {
                    "archived-at": "<http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/GZIKG6EFAPWEAKBPEMQ5KVYYLJG6WTEI/>",
                    "cc": None,
                    "delivered-to": None,
                    "from": "Reindl Harald <h.reindl@thelounge.net>",
                    "in-reply-to": "<CAObL_7EYXGQP2Ow-jHj2gx=TBc1XOVSAw2=xoVk5q4nmB7o-Jg@mail.gmail.com>",
                    "message-id": "<566DDB7E.1080505@thelounge.net>",
                    "references": "<CAL5zq9ZYgmi+BejiUSA1HKa+wj_CSfQfFFoGA-VZHnMJ3bPz_g@mail.gmail.com>\n <CAObL_7HgBZgh1W0yJb0Pmfa2pBcwoz+J4e9z5y_qKrSbLLEkMA@mail.gmail.com>\n <566DD742.50607@thelounge.net>\n <CAObL_7EYXGQP2Ow-jHj2gx=TBc1XOVSAw2=xoVk5q4nmB7o-Jg@mail.gmail.com>",
                    "subject": "Re: Easier %config management?",
                    "to": "devel@lists.fedoraproject.org",
                    "x-mailman-rule-hits": "member-moderation",
                    "x-mailman-rule-misses": "approved; emergency; loop",
                    "x-message-id-hash": "GZIKG6EFAPWEAKBPEMQ5KVYYLJG6WTEI"
                }
            },
            "msg_id": "2015-cbe5cf35-e092-40e4-ae24-f953a4579f7f",
            "timestamp": 1450040210.0,
            "topic": "org.fedoraproject.prod.mailman.receive"
        },
        {
            "i": 913,
            "msg": {
                "mlist": {
                    "list_name": "devel"
                },
                "msg": {
                    "archived-at": "<http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/M34UJ72IBEYB53BZVYNCDQJMEWOEYV6J/>",
                    "cc": None,
                    "delivered-to": None,
                    "from": "Andrew Lutomirski <luto@mit.edu>",
                    "in-reply-to": "<566DD742.50607@thelounge.net>",
                    "message-id": "<CAObL_7EYXGQP2Ow-jHj2gx=TBc1XOVSAw2=xoVk5q4nmB7o-Jg@mail.gmail.com>",
                    "references": "<CAL5zq9ZYgmi+BejiUSA1HKa+wj_CSfQfFFoGA-VZHnMJ3bPz_g@mail.gmail.com>\n\t<CAObL_7HgBZgh1W0yJb0Pmfa2pBcwoz+J4e9z5y_qKrSbLLEkMA@mail.gmail.com>\n\t<566DD742.50607@thelounge.net>",
                    "subject": "Re: Easier %config management?",
                    "to": "Development discussions related to Fedora <devel@lists.fedoraproject.org>",
                    "x-mailman-rule-hits": "member-moderation",
                    "x-mailman-rule-misses": "approved; emergency; loop",
                    "x-message-id-hash": "M34UJ72IBEYB53BZVYNCDQJMEWOEYV6J"
                }
            },
            "msg_id": "2015-2b4600fa-1813-407a-8283-f539ba25808c",
            "timestamp": 1450039852.0,
            "topic": "org.fedoraproject.prod.mailman.receive"
        },
        {
            "i": 912,
            "msg": {
                "mlist": {
                    "list_name": "devel"
                },
                "msg": {
                    "archived-at": "<http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/NNJBSF7M4AYB67FUUIO4LWV3MCJ7ANMX/>",
                    "cc": None,
                    "delivered-to": None,
                    "from": "Reindl Harald <h.reindl@thelounge.net>",
                    "in-reply-to": "<CAObL_7HgBZgh1W0yJb0Pmfa2pBcwoz+J4e9z5y_qKrSbLLEkMA@mail.gmail.com>",
                    "message-id": "<566DD742.50607@thelounge.net>",
                    "references": "<CAL5zq9ZYgmi+BejiUSA1HKa+wj_CSfQfFFoGA-VZHnMJ3bPz_g@mail.gmail.com>\n <CAObL_7HgBZgh1W0yJb0Pmfa2pBcwoz+J4e9z5y_qKrSbLLEkMA@mail.gmail.com>",
                    "subject": "Re: Easier %config management?",
                    "to": "devel@lists.fedoraproject.org",
                    "x-mailman-rule-hits": "member-moderation",
                    "x-mailman-rule-misses": "approved; emergency; loop",
                    "x-message-id-hash": "NNJBSF7M4AYB67FUUIO4LWV3MCJ7ANMX"
                }
            },
            "msg_id": "2015-a088bcf9-b796-47eb-9418-5ac7e5055a0f",
            "timestamp": 1450039132.0,
            "topic": "org.fedoraproject.prod.mailman.receive"
        },
        {
            "i": 910,
            "msg": {
                "mlist": {
                    "list_name": "devel"
                },
                "msg": {
                    "archived-at": "<http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/QBF6PDFCCH66ZCU4G4NR55QMQGWQIT24/>",
                    "cc": None,
                    "delivered-to": None,
                    "from": "Andrew Lutomirski <luto@mit.edu>",
                    "in-reply-to": "<CAL5zq9ZYgmi+BejiUSA1HKa+wj_CSfQfFFoGA-VZHnMJ3bPz_g@mail.gmail.com>",
                    "message-id": "<CAObL_7HgBZgh1W0yJb0Pmfa2pBcwoz+J4e9z5y_qKrSbLLEkMA@mail.gmail.com>",
                    "references": "<CAL5zq9ZYgmi+BejiUSA1HKa+wj_CSfQfFFoGA-VZHnMJ3bPz_g@mail.gmail.com>",
                    "subject": "Re: Easier %config management?",
                    "to": "Development discussions related to Fedora <devel@lists.fedoraproject.org>",
                    "x-mailman-rule-hits": "member-moderation",
                    "x-mailman-rule-misses": "approved; emergency; loop",
                    "x-message-id-hash": "QBF6PDFCCH66ZCU4G4NR55QMQGWQIT24"
                }
            },
            "msg_id": "2015-9cc72c62-90dd-4ee0-a876-5168e35b2065",
            "timestamp": 1450038189.0,
            "topic": "org.fedoraproject.prod.mailman.receive"
        },
        {
            "i": 906,
            "msg": {
                "mlist": {
                    "list_name": "devel"
                },
                "msg": {
                    "archived-at": "<http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/6Q7Y35X5GUKGNS3YECNVYQDYR7OCBEL6/>",
                    "cc": None,
                    "delivered-to": None,
                    "from": "Reindl Harald <h.reindl@thelounge.net>",
                    "in-reply-to": "<CAL5zq9ZYgmi+BejiUSA1HKa+wj_CSfQfFFoGA-VZHnMJ3bPz_g@mail.gmail.com>",
                    "message-id": "<566DCBFD.3000704@thelounge.net>",
                    "references": "<CAL5zq9ZYgmi+BejiUSA1HKa+wj_CSfQfFFoGA-VZHnMJ3bPz_g@mail.gmail.com>",
                    "subject": "Re: Easier %config management?",
                    "to": "devel@lists.fedoraproject.org",
                    "x-mailman-rule-hits": "member-moderation",
                    "x-mailman-rule-misses": "approved; emergency; loop",
                    "x-message-id-hash": "6Q7Y35X5GUKGNS3YECNVYQDYR7OCBEL6"
                }
            },
            "msg_id": "2015-64402233-3471-4de8-b909-db32c96de695",
            "timestamp": 1450036236.0,
            "topic": "org.fedoraproject.prod.mailman.receive"
        },
        {
            "i": 905,
            "msg": {
                "mlist": {
                    "list_name": "devel"
                },
                "msg": {
                    "archived-at": "<http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/TKJB5SDTGMXVRV2DJ7XWK7ZKGX3HXMFN/>",
                    "cc": None,
                    "delivered-to": None,
                    "from": "\"Richard W.M. Jones\" <rjones@redhat.com>",
                    "in-reply-to": "<CAL5zq9ZYgmi+BejiUSA1HKa+wj_CSfQfFFoGA-VZHnMJ3bPz_g@mail.gmail.com>",
                    "message-id": "<20151213194131.GN26159@redhat.com>",
                    "references": "<CAL5zq9ZYgmi+BejiUSA1HKa+wj_CSfQfFFoGA-VZHnMJ3bPz_g@mail.gmail.com>",
                    "subject": "Re: Easier %config management?",
                    "to": "Development discussions related to Fedora <devel@lists.fedoraproject.org>",
                    "x-mailman-rule-hits": "member-moderation",
                    "x-mailman-rule-misses": "approved; emergency; loop",
                    "x-message-id-hash": "TKJB5SDTGMXVRV2DJ7XWK7ZKGX3HXMFN"
                }
            },
            "msg_id": "2015-e73d5e41-46de-4f50-a4ce-7cc0b608ad53",
            "timestamp": 1450035716.0,
            "topic": "org.fedoraproject.prod.mailman.receive"
        },
        {
            "i": 873,
            "msg": {
                "mlist": {
                    "list_name": "devel"
                },
                "msg": {
                    "archived-at": "<http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/WXYKNWQN5HOMEP2XDQOSH56RK4JHBJUO/>",
                    "cc": None,
                    "delivered-to": None,
                    "from": "Fedora compose checker <rawhide@fedoraproject.org>",
                    "in-reply-to": None,
                    "message-id": "<20151213151942.93CC06076F73@bastion01.phx2.fedoraproject.org>",
                    "references": None,
                    "subject": "Fedora Rawhide 20151213 compose check report",
                    "to": "test@lists.fedoraproject.org, devel@lists.fedoraproject.org",
                    "x-mailman-rule-hits": "member-moderation",
                    "x-mailman-rule-misses": "approved; emergency; loop",
                    "x-message-id-hash": "WXYKNWQN5HOMEP2XDQOSH56RK4JHBJUO"
                }
            },
            "msg_id": "2015-ff061d3c-42c8-4a4e-9083-da16e7ffef8e",
            "timestamp": 1450019998.0,
            "topic": "org.fedoraproject.prod.mailman.receive"
        },
        {
            "i": 868,
            "msg": {
                "mlist": {
                    "list_name": "devel"
                },
                "msg": {
                    "archived-at": "<http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/HPBHTMMCDAUU5ZMTUJCPFIERWZEHDNGG/>",
                    "cc": None,
                    "delivered-to": None,
                    "from": "Joseph Pesco <jpesco@gmx.com>",
                    "in-reply-to": "<CAJCQCtRXk_-Sk0+825daQFWkjt39GBjb9moDFDdWTQyz7TRKOg@mail.gmail.com>",
                    "message-id": "<1450015318.3754.0.camel@gmx.com>",
                    "references": "\n\t<CA+Sa5FoBH8yewYNW=HKSG_NFmgwLs+uxDQ5_x=uX7E7aW4X9bQ@mail.gmail.com>\n\t <CAJCQCtT=rspdip--31GMFAQLeaKeZKiG6eZzWJuKybreur2+2w@mail.gmail.com>\n\t <1449858511.3952.51.camel@redhat.com>\n\t <CAJCQCtRXk_-Sk0+825daQFWkjt39GBjb9moDFDdWTQyz7TRKOg@mail.gmail.com>",
                    "subject": "Re: REMINDER: FESCo, Council, FAmSCo elections",
                    "to": "devel@lists.fedoraproject.org",
                    "x-mailman-rule-hits": "member-moderation",
                    "x-mailman-rule-misses": "approved; emergency; loop",
                    "x-message-id-hash": "HPBHTMMCDAUU5ZMTUJCPFIERWZEHDNGG"
                }
            },
            "msg_id": "2015-248bdd54-0f56-41bd-a226-8802479ae0c6",
            "timestamp": 1450015355.0,
            "topic": "org.fedoraproject.prod.mailman.receive"
        },
        {
            "i": 857,
            "msg": {
                "mlist": {
                    "list_name": "devel"
                },
                "msg": {
                    "archived-at": "<http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/3UGB7MTFX6KBXHUNYNRG3EJ5JB5T2HNP/>",
                    "cc": None,
                    "delivered-to": None,
                    "from": "Michael Schwendt <mschwendt@gmail.com>",
                    "in-reply-to": "<CAKHp9yqjoeijtK25Y8ROWQrMZqB2_nmLBv=psKCyJVR35bCmCA@mail.gmail.com>",
                    "message-id": "<20151213141102.40f3db30@noname>",
                    "references": "<CAKHp9ypJdqp_sc5S0KLcAE=QWbCeDdY5c24=ueyH0mHF+ouBRA@mail.gmail.com>\n\t<20151208165729.3d396e49@noname>\n\t<CAKHp9yqjoeijtK25Y8ROWQrMZqB2_nmLBv=psKCyJVR35bCmCA@mail.gmail.com>",
                    "subject": "Re: dnf behavior expected?",
                    "to": "devel@lists.fedoraproject.org",
                    "x-mailman-rule-hits": "member-moderation",
                    "x-mailman-rule-misses": "approved; emergency; loop",
                    "x-message-id-hash": "3UGB7MTFX6KBXHUNYNRG3EJ5JB5T2HNP"
                }
            },
            "msg_id": "2015-aa785443-2e4c-4beb-b837-4c26df63f24c",
            "timestamp": 1450012283.0,
            "topic": "org.fedoraproject.prod.mailman.receive"
        },
        {
            "i": 832,
            "msg": {
                "mlist": {
                    "list_name": "devel"
                },
                "msg": {
                    "archived-at": "<http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RDVKKW5QZZBFUXVQR32ZQ7N3DXMTBRRU/>",
                    "cc": None,
                    "delivered-to": None,
                    "from": "Fedora Rawhide Report <rawhide@fedoraproject.org>",
                    "in-reply-to": None,
                    "message-id": "<20151213103242.GA4337@rawhide-composer.phx2.fedoraproject.org>",
                    "references": None,
                    "subject": "rawhide report: 20151213 changes",
                    "to": "devel@lists.fedoraproject.org, test@lists.fedoraproject.org",
                    "x-mailman-rule-hits": "member-moderation",
                    "x-mailman-rule-misses": "approved; emergency; loop",
                    "x-message-id-hash": "RDVKKW5QZZBFUXVQR32ZQ7N3DXMTBRRU"
                }
            },
            "msg_id": "2015-3796f3ae-7678-4963-a42d-101f861f5983",
            "timestamp": 1450002803.0,
            "topic": "org.fedoraproject.prod.mailman.receive"
        },
        {
            "i": 820,
            "msg": {
                "mlist": {
                    "list_name": "devel"
                },
                "msg": {
                    "archived-at": "<http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/BHDNIRPDYET3WYNTMITN2BA2NLISYHJA/>",
                    "cc": None,
                    "delivered-to": None,
                    "from": "\"J. Randall Owens\" <jrowens.fedora@ghiapet.net>",
                    "in-reply-to": "<20151213080704.GA31870@host1.jankratochvil.net>",
                    "message-id": "<566D36FF.1020607@ghiapet.net>",
                    "references": "<CAL5zq9ZYgmi+BejiUSA1HKa+wj_CSfQfFFoGA-VZHnMJ3bPz_g@mail.gmail.com>\n <20151213080704.GA31870@host1.jankratochvil.net>",
                    "subject": "Re: Easier %config management?",
                    "to": "Development discussions related to Fedora <devel@lists.fedoraproject.org>",
                    "x-mailman-rule-hits": "member-moderation",
                    "x-mailman-rule-misses": "approved; emergency; loop",
                    "x-message-id-hash": "BHDNIRPDYET3WYNTMITN2BA2NLISYHJA"
                }
            },
            "msg_id": "2015-fe5fddb5-85df-4dd9-955d-5de1a68aea54",
            "timestamp": 1449998105.0,
            "topic": "org.fedoraproject.prod.mailman.receive"
        },
        {
            "i": 811,
            "msg": {
                "mlist": {
                    "list_name": "devel"
                },
                "msg": {
                    "archived-at": "<http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/S7KLJGO6QO233SNPOOBV6MOBUCD7GRGZ/>",
                    "cc": None,
                    "delivered-to": None,
                    "from": "=?UTF-8?B?QmrDtnJu?= Persson <Bjorn@xn--rombobjrn-67a.se>",
                    "in-reply-to": "<20151207113244.7934fed7@speedy.xn--rombobjrn-67a.se>",
                    "message-id": "<20151213091203.6d8cc34c@hactar.xn--rombobjrn-67a.se>",
                    "references": "<20151129003537.10219c62@hactar.xn--rombobjrn-67a.se>\n\t<20151129144048.7943824c@sheelba.scrye.com>\n\t<20151201154626.10e417cf@speedy.xn--rombobjrn-67a.se>\n\t<20151204100457.4ecbb61f@sheelba.scrye.com>\n\t<20151207113244.7934fed7@speedy.xn--rombobjrn-67a.se>",
                    "subject": "Re: Can Koji handle a soname change and a self-dependency?",
                    "to": "devel@lists.fedoraproject.org",
                    "x-mailman-rule-hits": "member-moderation",
                    "x-mailman-rule-misses": "approved; emergency; loop",
                    "x-message-id-hash": "S7KLJGO6QO233SNPOOBV6MOBUCD7GRGZ"
                }
            },
            "msg_id": "2015-1da1b4e6-e784-4f1f-937c-8846399ea534",
            "timestamp": 1449994343.0,
            "topic": "org.fedoraproject.prod.mailman.receive"
        },
        {
            "i": 810,
            "msg": {
                "mlist": {
                    "list_name": "devel"
                },
                "msg": {
                    "archived-at": "<http://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/G6TQAZYKZF3KH6XW3SV6ZSW3MPARYG54/>",
                    "cc": None,
                    "delivered-to": None,
                    "from": "=?UTF-8?B?QmrDtnJu?= Persson <Bjorn@xn--rombobjrn-67a.se>",
                    "in-reply-to": "<20151210232042.e00d69b0c02cd9986938caa6@danny.cz>",
                    "message-id": "<20151213090940.2d92c807@hactar.xn--rombobjrn-67a.se>",
                    "references": "<20151129003537.10219c62@hactar.xn--rombobjrn-67a.se>\n\t<20151129144048.7943824c@sheelba.scrye.com>\n\t<20151201154626.10e417cf@speedy.xn--rombobjrn-67a.se>\n\t<20151204100457.4ecbb61f@sheelba.scrye.com>\n\t<20151207113244.7934fed7@speedy.xn--rombobjrn-67a.se>\n\t<20151210232042.e00d69b0c02cd9986938caa6@danny.cz>",
                    "subject": "Re: Can Koji handle a soname change and a self-dependency?",
                    "to": "devel@lists.fedoraproject.org",
                    "x-mailman-rule-hits": "member-moderation",
                    "x-mailman-rule-misses": "approved; emergency; loop",
                    "x-message-id-hash": "G6TQAZYKZF3KH6XW3SV6ZSW3MPARYG54"
                }
            },
            "msg_id": "2015-273e2273-cdbe-4448-83fb-e133ead87f61",
            "timestamp": 1449994219.0,
            "topic": "org.fedoraproject.prod.mailman.receive"
        }
    ]
