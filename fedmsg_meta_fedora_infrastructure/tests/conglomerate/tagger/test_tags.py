import fedmsg.tests.test_meta

import arrow


class TestTaggerConglomerateByUser(
        fedmsg.tests.test_meta.ConglomerateBase):
    expected =[
        {'categories': set(['fedoratagger']),
         'end_time': 1436284694.0,
         'human_time': arrow.get(1436284677.6666667).humanize(),
         'icon': 'https://apps.fedoraproject.org/img/icons/tagger.png',
         'link': 'http://infrastructure.fedoraproject.org/infra/ansible.git/',
         'packages': set(['php-pear-console-color2']),
         'secondary_icon': 'https://seccdn.libravatar.org/avatar/'
         '1240f5f278e39089bdcee4c09aa4f6f8dc6e02b5446f61cb8c8c0bf9d53950a8'
         '?s=64&d=retro',
         'start_time': 1436284655.0,
         'subtitle': 'nalin voted on the tags: library '
         'and module to the packages: php-pear-console-color2',
         'subjective': 'nalin voted on the tags: library '
         'and module to the packages: php-pear-console-color2',
         'timestamp': 1436284677.6666667,
         'topics': set(['org.fedoraproject.prod.fedoratagger.tag.update']),
         'usernames': set(['nalin'])},
        {'categories': set(['fedoratagger']),
         'end_time': 1436270087.0,
         'human_time': arrow.get(1436269900.93).humanize(),
         'icon': 'https://apps.fedoraproject.org/img/icons/tagger.png',
         'link': 'http://infrastructure.fedoraproject.org/infra/ansible.git/',
         'packages': set(['GtkAda3',
                          'fedmsg',
                          'github2fedmsg',
                          'libgcrypt',
                          'modem-manager-gui',
                          'pam_krb5',
                          'ppp']),
         'secondary_icon': 'https://seccdn.libravatar.org/avatar/'
         '861506b8dba9fe9ee12a83ce2cd7c6fff15091298f9f1a4e6149876490c53e9b'
         '?s=64&d=retro',
         'start_time': 1436269755.0,
         'subtitle': 'pbrobinson voted on the tags: ada, crypto, '
         'and 13 others to the packages: GtkAda3, fedmsg, and 5 others',
         'subjective': 'pbrobinson voted on the tags: ada, crypto, '
         'and 13 others to the packages: GtkAda3, fedmsg, and 5 others',
         'timestamp': 1436269900.9333334,
         'topics': set(['org.fedoraproject.prod.fedoratagger.tag.update']),
         'usernames': set(['pbrobinson'])},
        {'categories': set(['fedoratagger']),
         'end_time': 1436269913.0,
         'human_time': arrow.get(1436269860.75).humanize(),
         'icon': 'https://apps.fedoraproject.org/img/icons/tagger.png',
         'link': 'http://infrastructure.fedoraproject.org/infra/ansible.git/',
         'packages': set(['fedmsg', 'pam_krb5', 'rstp']),
         'secondary_icon': 'https://seccdn.libravatar.org/avatar/'
         '861506b8dba9fe9ee12a83ce2cd7c6fff15091298f9f1a4e6149876490c53e9b'
         '?s=64&d=retro',
         'start_time': 1436269765.0,
         'subtitle': 'pbrobinson created new tags: authentication, msgbus, '
         'and 2 others on the packages: fedmsg, pam_krb5, and rstp',
         'subjective': 'pbrobinson created new tags: authentication, msgbus, '
         'and 2 others on the packages: fedmsg, pam_krb5, and rstp',
         'timestamp': 1436269860.75,
         'topics': set(['org.fedoraproject.prod.fedoratagger.tag.create']),
         'usernames': set(['pbrobinson'])}
    ]
    originals = [{
        "i": 15,
        "msg": {
            "tag": {
                "dislike": 0,
                "like": 2,
                "package": "php-pear-console-color2",
                "tag": "module",
                "total": 2,
                "votes": 2
            },
            "user": {
                "anonymous": False,
                "rank": 231,
                "score": 2,
                "username": "nalin",
                "votes": 2
            },
            "vote": {
                "like": True,
                "tag": {
                    "dislike": 0,
                    "like": 2,
                    "package": "php-pear-console-color2",
                    "tag": "module",
                    "total": 2,
                    "votes": 2
                },
                "user": {
                    "anonymous": False,
                    "rank": 231,
                    "score": 2,
                    "username": "nalin",
                    "votes": 2
                }
            }
        },
        "msg_id": "2015-ad796f57-d993-4b01-be34-97d24a144f83",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436284694.0,
        "topic": "org.fedoraproject.prod.fedoratagger.tag.update"
    },
    {
        "i": 15,
        "msg": {
            "tag": {
                "dislike": 0,
                "like": 2,
                "package": "php-pear-console-color2",
                "tag": "library",
                "total": 2,
                "votes": 2
            },
            "user": {
                "anonymous": False,
                "rank": 231,
                "score": 2,
                "username": "nalin",
                "votes": 2
            },
            "vote": {
                "like": True,
                "tag": {
                    "dislike": 0,
                    "like": 2,
                    "package": "php-pear-console-color2",
                    "tag": "library",
                    "total": 2,
                    "votes": 2
                },
                "user": {
                    "anonymous": False,
                    "rank": 231,
                    "score": 2,
                    "username": "nalin",
                    "votes": 2
                }
            }
        },
        "msg_id": "2015-1d1206f8-60ed-4e4c-b5b4-09c55231bafc",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436284692.0,
        "topic": "org.fedoraproject.prod.fedoratagger.tag.update"
    },
    {
        "i": 14,
        "msg": {
            "tag": {
                "dislike": 1,
                "like": 1,
                "package": "php-pear-console-color2",
                "tag": "library",
                "total": 0,
                "votes": 2
            },
            "user": {
                "anonymous": False,
                "rank": 231,
                "score": 2,
                "username": "nalin",
                "votes": 2
            },
            "vote": {
                "like": False,
                "tag": {
                    "dislike": 1,
                    "like": 1,
                    "package": "php-pear-console-color2",
                    "tag": "library",
                    "total": 0,
                    "votes": 2
                },
                "user": {
                    "anonymous": False,
                    "rank": 231,
                    "score": 2,
                    "username": "nalin",
                    "votes": 2
                }
            }
        },
        "msg_id": "2015-a46f0f83-2f7f-4aeb-a662-1f5982a1db85",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436284687.0,
        "topic": "org.fedoraproject.prod.fedoratagger.tag.update"
    },
    {
        "i": 13,
        "msg": {
            "tag": {
                "dislike": 1,
                "like": 1,
                "package": "php-pear-console-color2",
                "tag": "module",
                "total": 0,
                "votes": 2
            },
            "user": {
                "anonymous": False,
                "rank": 231,
                "score": 2,
                "username": "nalin",
                "votes": 2
            },
            "vote": {
                "like": False,
                "tag": {
                    "dislike": 1,
                    "like": 1,
                    "package": "php-pear-console-color2",
                    "tag": "module",
                    "total": 0,
                    "votes": 2
                },
                "user": {
                    "anonymous": False,
                    "rank": 231,
                    "score": 2,
                    "username": "nalin",
                    "votes": 2
                }
            }
        },
        "msg_id": "2015-9d2de038-01c7-440a-9f2a-4f7518919366",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436284683.0,
        "topic": "org.fedoraproject.prod.fedoratagger.tag.update"
    },
    {
        "i": 15,
        "msg": {
            "tag": {
                "dislike": 0,
                "like": 2,
                "package": "php-pear-console-color2",
                "tag": "module",
                "total": 2,
                "votes": 2
            },
            "user": {
                "anonymous": False,
                "rank": 231,
                "score": 0.5,
                "username": "nalin",
                "votes": 1
            },
            "vote": {
                "like": True,
                "tag": {
                    "dislike": 0,
                    "like": 2,
                    "package": "php-pear-console-color2",
                    "tag": "module",
                    "total": 2,
                    "votes": 2
                },
                "user": {
                    "anonymous": False,
                    "rank": 231,
                    "score": 0.5,
                    "username": "nalin",
                    "votes": 1
                }
            }
        },
        "msg_id": "2015-60108dbb-ab48-42ef-8c80-e4443cce56f8",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436284655.0,
        "topic": "org.fedoraproject.prod.fedoratagger.tag.update"
    },
    {
        "i": 12,
        "msg": {
            "tag": {
                "dislike": 0,
                "like": 2,
                "package": "php-pear-console-color2",
                "tag": "library",
                "total": 2,
                "votes": 2
            },
            "user": {
                "anonymous": False,
                "rank": 231,
                "score": 1.5,
                "username": "nalin",
                "votes": 2
            },
            "vote": {
                "like": True,
                "tag": {
                    "dislike": 0,
                    "like": 2,
                    "package": "php-pear-console-color2",
                    "tag": "library",
                    "total": 2,
                    "votes": 2
                },
                "user": {
                    "anonymous": False,
                    "rank": 231,
                    "score": 1.5,
                    "username": "nalin",
                    "votes": 2
                }
            }
        },
        "msg_id": "2015-6c58888b-ab74-4c53-bb14-53d2ff42bfaa",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436284655.0,
        "topic": "org.fedoraproject.prod.fedoratagger.tag.update"
    },
    {
        "i": 10,
        "msg": {
            "tag": {
                "dislike": 0,
                "like": 3,
                "package": "modem-manager-gui",
                "tag": "modem",
                "total": 3,
                "votes": 3
            },
            "user": {
                "anonymous": False,
                "rank": 139,
                "score": 190.5,
                "username": "pbrobinson",
                "votes": 126
            },
            "vote": {
                "like": True,
                "tag": {
                    "dislike": 0,
                    "like": 3,
                    "package": "modem-manager-gui",
                    "tag": "modem",
                    "total": 3,
                    "votes": 3
                },
                "user": {
                    "anonymous": False,
                    "rank": 139,
                    "score": 190.5,
                    "username": "pbrobinson",
                    "votes": 126
                }
            }
        },
        "msg_id": "2015-1ee9888a-4f00-4eb5-8ebd-d31e89b3f7f2",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436270087.0,
        "topic": "org.fedoraproject.prod.fedoratagger.tag.update"
    },
    {
        "i": 11,
        "msg": {
            "tag": {
                "dislike": 0,
                "like": 5,
                "package": "github2fedmsg",
                "tag": "fedmsg",
                "total": 5,
                "votes": 5
            },
            "user": {
                "anonymous": False,
                "rank": 139,
                "score": 189.5,
                "username": "pbrobinson",
                "votes": 125
            },
            "vote": {
                "like": True,
                "tag": {
                    "dislike": 0,
                    "like": 5,
                    "package": "github2fedmsg",
                    "tag": "fedmsg",
                    "total": 5,
                    "votes": 5
                },
                "user": {
                    "anonymous": False,
                    "rank": 139,
                    "score": 189.5,
                    "username": "pbrobinson",
                    "votes": 125
                }
            }
        },
        "msg_id": "2015-f3923e94-d145-4254-8582-a8e69799d4b7",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436270056.0,
        "topic": "org.fedoraproject.prod.fedoratagger.tag.update"
    },
    {
        "i": 14,
        "msg": {
            "tag": {
                "dislike": 0,
                "like": 5,
                "package": "github2fedmsg",
                "tag": "github",
                "total": 5,
                "votes": 5
            },
            "user": {
                "anonymous": False,
                "rank": 139,
                "score": 188.5,
                "username": "pbrobinson",
                "votes": 124
            },
            "vote": {
                "like": True,
                "tag": {
                    "dislike": 0,
                    "like": 5,
                    "package": "github2fedmsg",
                    "tag": "github",
                    "total": 5,
                    "votes": 5
                },
                "user": {
                    "anonymous": False,
                    "rank": 139,
                    "score": 188.5,
                    "username": "pbrobinson",
                    "votes": 124
                }
            }
        },
        "msg_id": "2015-f30906f2-e0fd-45d9-bb6e-0d3fa2a7e3ed",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436270054.0,
        "topic": "org.fedoraproject.prod.fedoratagger.tag.update"
    },
    {
        "i": 13,
        "msg": {
            "tag": {
                "dislike": 0,
                "like": 3,
                "package": "ppp",
                "tag": "network",
                "total": 3,
                "votes": 3
            },
            "user": {
                "anonymous": False,
                "rank": 139,
                "score": 187.5,
                "username": "pbrobinson",
                "votes": 123
            },
            "vote": {
                "like": True,
                "tag": {
                    "dislike": 0,
                    "like": 3,
                    "package": "ppp",
                    "tag": "network",
                    "total": 3,
                    "votes": 3
                },
                "user": {
                    "anonymous": False,
                    "rank": 139,
                    "score": 187.5,
                    "username": "pbrobinson",
                    "votes": 123
                }
            }
        },
        "msg_id": "2015-7d8eb8ed-c13d-4b7f-b009-4595c98b3115",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436269987.0,
        "topic": "org.fedoraproject.prod.fedoratagger.tag.update"
    },
    {
        "i": 10,
        "msg": {
            "tag": {
                "dislike": 1,
                "like": 3,
                "package": "ppp",
                "tag": "ppp",
                "total": 2,
                "votes": 4
            },
            "user": {
                "anonymous": False,
                "rank": 139,
                "score": 186.5,
                "username": "pbrobinson",
                "votes": 122
            },
            "vote": {
                "like": True,
                "tag": {
                    "dislike": 1,
                    "like": 3,
                    "package": "ppp",
                    "tag": "ppp",
                    "total": 2,
                    "votes": 4
                },
                "user": {
                    "anonymous": False,
                    "rank": 139,
                    "score": 186.5,
                    "username": "pbrobinson",
                    "votes": 122
                }
            }
        },
        "msg_id": "2015-d56c5828-e013-4d2f-a26f-57c7cdfd688b",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436269986.0,
        "topic": "org.fedoraproject.prod.fedoratagger.tag.update"
    },
    {
        "i": 9,
        "msg": {
            "tag": {
                "dislike": 0,
                "like": 4,
                "package": "libgcrypt",
                "tag": "cryptography",
                "total": 4,
                "votes": 4
            },
            "user": {
                "anonymous": False,
                "rank": 139,
                "score": 185.5,
                "username": "pbrobinson",
                "votes": 121
            },
            "vote": {
                "like": True,
                "tag": {
                    "dislike": 0,
                    "like": 4,
                    "package": "libgcrypt",
                    "tag": "cryptography",
                    "total": 4,
                    "votes": 4
                },
                "user": {
                    "anonymous": False,
                    "rank": 139,
                    "score": 185.5,
                    "username": "pbrobinson",
                    "votes": 121
                }
            }
        },
        "msg_id": "2015-8cd2b9d5-5237-4895-b259-bdd51a69cd21",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436269931.0,
        "topic": "org.fedoraproject.prod.fedoratagger.tag.update"
    },
    {
        "i": 9,
        "msg": {
            "tag": {
                "dislike": 0,
                "like": 5,
                "package": "libgcrypt",
                "tag": "crypto",
                "total": 5,
                "votes": 5
            },
            "user": {
                "anonymous": False,
                "rank": 139,
                "score": 184.5,
                "username": "pbrobinson",
                "votes": 120
            },
            "vote": {
                "like": True,
                "tag": {
                    "dislike": 0,
                    "like": 5,
                    "package": "libgcrypt",
                    "tag": "crypto",
                    "total": 5,
                    "votes": 5
                },
                "user": {
                    "anonymous": False,
                    "rank": 139,
                    "score": 184.5,
                    "username": "pbrobinson",
                    "votes": 120
                }
            }
        },
        "msg_id": "2015-9db798bc-4ae4-429e-9745-04cc7dd61b50",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436269928.0,
        "topic": "org.fedoraproject.prod.fedoratagger.tag.update"
    },
    {
        "i": 8,
        "msg": {
            "tag": {
                "dislike": 0,
                "like": 1,
                "package": "rstp",
                "tag": "routing protocol",
                "total": 1,
                "votes": 1
            },
            "user": {
                "anonymous": False,
                "rank": 139,
                "score": 184,
                "username": "pbrobinson",
                "votes": 119
            },
            "vote": {
                "like": True,
                "tag": {
                    "dislike": 0,
                    "like": 1,
                    "package": "rstp",
                    "tag": "routing protocol",
                    "total": 1,
                    "votes": 1
                },
                "user": {
                    "anonymous": False,
                    "rank": 139,
                    "score": 184,
                    "username": "pbrobinson",
                    "votes": 119
                }
            }
        },
        "msg_id": "2015-2c67e7e4-6460-4da5-9316-ca5f259f244b",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436269913.0,
        "topic": "org.fedoraproject.prod.fedoratagger.tag.create"
    },
    {
        "i": 4,
        "msg": {
            "tag": {
                "dislike": 0,
                "like": 1,
                "package": "rstp",
                "tag": "network",
                "total": 1,
                "votes": 1
            },
            "user": {
                "anonymous": False,
                "rank": 139,
                "score": 182,
                "username": "pbrobinson",
                "votes": 118
            },
            "vote": {
                "like": True,
                "tag": {
                    "dislike": 0,
                    "like": 1,
                    "package": "rstp",
                    "tag": "network",
                    "total": 1,
                    "votes": 1
                },
                "user": {
                    "anonymous": False,
                    "rank": 139,
                    "score": 182,
                    "username": "pbrobinson",
                    "votes": 118
                }
            }
        },
        "msg_id": "2015-5aeca8f3-9b52-4cbc-91c4-d565c2238bfd",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436269904.0,
        "topic": "org.fedoraproject.prod.fedoratagger.tag.create"
    },
    {
        "i": 9,
        "msg": {
            "tag": {
                "dislike": 0,
                "like": 1,
                "package": "fedmsg",
                "tag": "msgbus",
                "total": 1,
                "votes": 1
            },
            "user": {
                "anonymous": False,
                "rank": 139,
                "score": 180,
                "username": "pbrobinson",
                "votes": 117
            },
            "vote": {
                "like": True,
                "tag": {
                    "dislike": 0,
                    "like": 1,
                    "package": "fedmsg",
                    "tag": "msgbus",
                    "total": 1,
                    "votes": 1
                },
                "user": {
                    "anonymous": False,
                    "rank": 139,
                    "score": 180,
                    "username": "pbrobinson",
                    "votes": 117
                }
            }
        },
        "msg_id": "2015-0c2bd9e4-15f2-4980-9ce5-6fb749859770",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436269861.0,
        "topic": "org.fedoraproject.prod.fedoratagger.tag.create"
    },
    {
        "i": 9,
        "msg": {
            "tag": {
                "dislike": 1,
                "like": 6,
                "package": "fedmsg",
                "tag": "open infrastructure",
                "total": 5,
                "votes": 7
            },
            "user": {
                "anonymous": False,
                "rank": 139,
                "score": 177.5,
                "username": "pbrobinson",
                "votes": 116
            },
            "vote": {
                "like": True,
                "tag": {
                    "dislike": 1,
                    "like": 6,
                    "package": "fedmsg",
                    "tag": "open infrastructure",
                    "total": 5,
                    "votes": 7
                },
                "user": {
                    "anonymous": False,
                    "rank": 139,
                    "score": 177.5,
                    "username": "pbrobinson",
                    "votes": 116
                }
            }
        },
        "msg_id": "2015-ddd21ea6-2906-4308-8dea-a8fd10df3ed3",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436269847.0,
        "topic": "org.fedoraproject.prod.fedoratagger.tag.update"
    },
    {
        "i": 8,
        "msg": {
            "tag": {
                "dislike": 0,
                "like": 6,
                "package": "fedmsg",
                "tag": "zeromq",
                "total": 6,
                "votes": 6
            },
            "user": {
                "anonymous": False,
                "rank": 139,
                "score": 175.5,
                "username": "pbrobinson",
                "votes": 114
            },
            "vote": {
                "like": True,
                "tag": {
                    "dislike": 0,
                    "like": 6,
                    "package": "fedmsg",
                    "tag": "zeromq",
                    "total": 6,
                    "votes": 6
                },
                "user": {
                    "anonymous": False,
                    "rank": 139,
                    "score": 175.5,
                    "username": "pbrobinson",
                    "votes": 114
                }
            }
        },
        "msg_id": "2015-6d3fd8d8-e21f-4dd9-8b05-295231dbbe25",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436269845.0,
        "topic": "org.fedoraproject.prod.fedoratagger.tag.update"
    },
    {
        "i": 8,
        "msg": {
            "tag": {
                "dislike": 0,
                "like": 5,
                "package": "fedmsg",
                "tag": "fedora",
                "total": 5,
                "votes": 5
            },
            "user": {
                "anonymous": False,
                "rank": 139,
                "score": 176.5,
                "username": "pbrobinson",
                "votes": 115
            },
            "vote": {
                "like": True,
                "tag": {
                    "dislike": 0,
                    "like": 5,
                    "package": "fedmsg",
                    "tag": "fedora",
                    "total": 5,
                    "votes": 5
                },
                "user": {
                    "anonymous": False,
                    "rank": 139,
                    "score": 176.5,
                    "username": "pbrobinson",
                    "votes": 115
                }
            }
        },
        "msg_id": "2015-9fc045bf-c593-484d-bb32-d0a2538721de",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436269845.0,
        "topic": "org.fedoraproject.prod.fedoratagger.tag.update"
    },
    {
        "i": 7,
        "msg": {
            "tag": {
                "dislike": 0,
                "like": 7,
                "package": "GtkAda3",
                "tag": "gtk",
                "total": 7,
                "votes": 7
            },
            "user": {
                "anonymous": False,
                "rank": 139,
                "score": 174.5,
                "username": "pbrobinson",
                "votes": 113
            },
            "vote": {
                "like": True,
                "tag": {
                    "dislike": 0,
                    "like": 7,
                    "package": "GtkAda3",
                    "tag": "gtk",
                    "total": 7,
                    "votes": 7
                },
                "user": {
                    "anonymous": False,
                    "rank": 139,
                    "score": 174.5,
                    "username": "pbrobinson",
                    "votes": 113
                }
            }
        },
        "msg_id": "2015-34f75959-3994-4bc9-bd73-8036d02f6efe",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436269840.0,
        "topic": "org.fedoraproject.prod.fedoratagger.tag.update"
    },
    {
        "i": 10,
        "msg": {
            "tag": {
                "dislike": 0,
                "like": 6,
                "package": "GtkAda3",
                "tag": "ada",
                "total": 6,
                "votes": 6
            },
            "user": {
                "anonymous": False,
                "rank": 139,
                "score": 173.5,
                "username": "pbrobinson",
                "votes": 112
            },
            "vote": {
                "like": True,
                "tag": {
                    "dislike": 0,
                    "like": 6,
                    "package": "GtkAda3",
                    "tag": "ada",
                    "total": 6,
                    "votes": 6
                },
                "user": {
                    "anonymous": False,
                    "rank": 139,
                    "score": 173.5,
                    "username": "pbrobinson",
                    "votes": 112
                }
            }
        },
        "msg_id": "2015-3b902a67-01cf-45ae-b6d6-9080217c5b28",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436269837.0,
        "topic": "org.fedoraproject.prod.fedoratagger.tag.update"
    },
    {
        "i": 7,
        "msg": {
            "tag": {
                "dislike": 0,
                "like": 4,
                "package": "pam_krb5",
                "tag": "authentication",
                "total": 4,
                "votes": 4
            },
            "user": {
                "anonymous": False,
                "rank": 139,
                "score": 173,
                "username": "pbrobinson",
                "votes": 111
            },
            "vote": {
                "like": True,
                "tag": {
                    "dislike": 0,
                    "like": 4,
                    "package": "pam_krb5",
                    "tag": "authentication",
                    "total": 4,
                    "votes": 4
                },
                "user": {
                    "anonymous": False,
                    "rank": 139,
                    "score": 173,
                    "username": "pbrobinson",
                    "votes": 111
                }
            }
        },
        "msg_id": "2015-3d543935-bd79-4c06-b84e-b58ff0e0e351",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436269765.0,
        "topic": "org.fedoraproject.prod.fedoratagger.tag.create"
    },
    {
        "i": 6,
        "msg": {
            "tag": {
                "dislike": 0,
                "like": 4,
                "package": "pam_krb5",
                "tag": "krb5",
                "total": 4,
                "votes": 4
            },
            "user": {
                "anonymous": False,
                "rank": 139,
                "score": 171.5,
                "username": "pbrobinson",
                "votes": 110
            },
            "vote": {
                "like": True,
                "tag": {
                    "dislike": 0,
                    "like": 4,
                    "package": "pam_krb5",
                    "tag": "krb5",
                    "total": 4,
                    "votes": 4
                },
                "user": {
                    "anonymous": False,
                    "rank": 139,
                    "score": 171.5,
                    "username": "pbrobinson",
                    "votes": 110
                }
            }
        },
        "msg_id": "2015-69169809-4307-44aa-a76b-9a32e11de4a6",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436269759.0,
        "topic": "org.fedoraproject.prod.fedoratagger.tag.update"
    },
    {
        "i": 12,
        "msg": {
            "tag": {
                "dislike": 0,
                "like": 7,
                "package": "pam_krb5",
                "tag": "kerberos",
                "total": 7,
                "votes": 7
            },
            "user": {
                "anonymous": False,
                "rank": 139,
                "score": 170.5,
                "username": "pbrobinson",
                "votes": 109
            },
            "vote": {
                "like": True,
                "tag": {
                    "dislike": 0,
                    "like": 7,
                    "package": "pam_krb5",
                    "tag": "kerberos",
                    "total": 7,
                    "votes": 7
                },
                "user": {
                    "anonymous": False,
                    "rank": 139,
                    "score": 170.5,
                    "username": "pbrobinson",
                    "votes": 109
                }
            }
        },
        "msg_id": "2015-a4ccaf4f-8ed6-4ba4-be74-02d868de1e8a",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436269757.0,
        "topic": "org.fedoraproject.prod.fedoratagger.tag.update"
    },
    {
        "i": 5,
        "msg": {
            "tag": {
                "dislike": 0,
                "like": 7,
                "package": "pam_krb5",
                "tag": "pam",
                "total": 7,
                "votes": 7
            },
            "user": {
                "anonymous": False,
                "rank": 139,
                "score": 169.5,
                "username": "pbrobinson",
                "votes": 108
            },
            "vote": {
                "like": True,
                "tag": {
                    "dislike": 0,
                    "like": 7,
                    "package": "pam_krb5",
                    "tag": "pam",
                    "total": 7,
                    "votes": 7
                },
                "user": {
                    "anonymous": False,
                    "rank": 139,
                    "score": 169.5,
                    "username": "pbrobinson",
                    "votes": 108
                }
            }
        },
        "msg_id": "2015-96e05d2c-a4f4-4b07-92f7-bb6be7f3bb02",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436269755.0,
        "topic": "org.fedoraproject.prod.fedoratagger.tag.update"
    }]
