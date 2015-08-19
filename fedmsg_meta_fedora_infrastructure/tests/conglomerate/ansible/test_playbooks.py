import fedmsg.tests.test_meta
import arrow

class TestPkgdbConglomerateCommentSubject(
        fedmsg.tests.test_meta.ConglomerateBase):
    subject = 'lmacken'
    expected = [{
        'categories': set(['ansible']),
        'end_time': 1436292424.0,
        'human_time': arrow.get(1436290771.0714285).humanize(),
        'icon': 'https://apps.fedoraproject.org/img/icons/ansible.png',
        'link': 'http://infrastructure.fedoraproject.org/infra/ansible.git/',
        'packages': set([]),
        'secondary_icon': 'https://seccdn.libravatar.org/avatar/203f6cb95b44b5d38aa21425b066dd522d3e19d8919cf4b339f29e0ea7f03e9b?s=64&d=retro',
        'start_time': 1436290155.0,
        'subtitle': 'lmacken ran the bodhi2.yml and proxies.yml playbooks 7 times',
        'subjective': 'You ran the bodhi2.yml and proxies.yml playbooks 7 times',
        'timestamp': 1436290771.0714285,
        'topics': set(['org.fedoraproject.prod.ansible.playbook.complete',
                       'org.fedoraproject.prod.ansible.playbook.start']),
        'usernames': set(['lmacken']),
    }, {
        'subtitle': 'kevin ran the jenkins-cloud.yml playbook 5 times',
        'subjective': 'kevin ran the jenkins-cloud.yml playbook 5 times',
        'link': 'http://infrastructure.fedoraproject.org/infra/ansible.git/',

        'icon': 'https://apps.fedoraproject.org/img/icons/ansible.png',
        'secondary_icon': 'https://seccdn.libravatar.org/avatar/'
        '1a7d8c43c8b89789a33a3266b0e20be7759a502ff38b74ff724a4db6aa33ede8'
        '?s=64&d=retro',

        'start_time': 1436287486.0,
        'end_time': 1436289694.0,
        'timestamp': 1436288676.6,

        'human_time': arrow.get(1436288676.6).humanize(),

        'usernames': set(['kevin']),
        'packages': set([]),
        'topics': set([
            'org.fedoraproject.prod.ansible.playbook.start',
            'org.fedoraproject.prod.ansible.playbook.complete',
        ]),
        'categories': set(['ansible']),
        'msg_ids': [
            '2014-9e46f5ce-4881-4497-aec4-89cf83332b2d',
            '2014-06ef29dd-adb5-47d8-92aa-f1ead0c4d8f1',
        ],
    }]

    originals = [ {
            "i": 2,
            "msg": {
                "playbook": "/home/fedora/lmacken/ansible/playbooks/groups/proxies.yml",
                "results": {
                    "proxy01.phx2.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 54,
                        "skipped": 0,
                        "unreachable": 0
                    },
                    "proxy01.stg.phx2.fedoraproject.org": {
                        "changed": 2,
                        "failures": 0,
                        "ok": 55,
                        "skipped": 0,
                        "unreachable": 0
                    },
                    "proxy02.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 54,
                        "skipped": 0,
                        "unreachable": 0
                    },
                    "proxy03.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 54,
                        "skipped": 0,
                        "unreachable": 0
                    },
                    "proxy04.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 54,
                        "skipped": 0,
                        "unreachable": 0
                    },
                    "proxy05.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 54,
                        "skipped": 0,
                        "unreachable": 0
                    },
                    "proxy06.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 54,
                        "skipped": 0,
                        "unreachable": 0
                    },
                    "proxy07.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 54,
                        "skipped": 0,
                        "unreachable": 0
                    },
                    "proxy08.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 54,
                        "skipped": 0,
                        "unreachable": 0
                    },
                    "proxy09.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 54,
                        "skipped": 0,
                        "unreachable": 0
                    },
                    "proxy10.phx2.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 54,
                        "skipped": 0,
                        "unreachable": 0
                    },
                    "proxy11.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 54,
                        "skipped": 0,
                        "unreachable": 0
                    }
                },
                "userid": "lmacken"
            },
            "msg_id": "2015-2b1e1269-0c96-41e8-9b89-e88f6073f364",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1436292424.0,
            "topic": "org.fedoraproject.prod.ansible.playbook.complete"
        },
        {
            "i": 1,
            "msg": {
                "check": False,
                "extra_vars": {},
                "inventory": "/srv/web/infra/ansible/inventory/",
                "playbook": "/home/fedora/lmacken/ansible/playbooks/groups/proxies.yml",
                "playbook_checksum": False,
                "userid": "lmacken"
            },
            "msg_id": "2015-46150020-4a1d-4b8d-a5cd-ab3d97dbeffe",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1436292289.0,
            "topic": "org.fedoraproject.prod.ansible.playbook.start"
        },
        {
            "i": 2,
            "msg": {
                "playbook": "/home/fedora/lmacken/ansible/playbooks/groups/proxies.yml",
                "results": {
                    "proxy01.phx2.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 54,
                        "skipped": 0,
                        "unreachable": 0
                    },
                    "proxy01.stg.phx2.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 54,
                        "skipped": 0,
                        "unreachable": 0
                    },
                    "proxy02.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 54,
                        "skipped": 0,
                        "unreachable": 0
                    },
                    "proxy03.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 54,
                        "skipped": 0,
                        "unreachable": 0
                    },
                    "proxy04.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 54,
                        "skipped": 0,
                        "unreachable": 0
                    },
                    "proxy05.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 54,
                        "skipped": 0,
                        "unreachable": 0
                    },
                    "proxy06.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 54,
                        "skipped": 0,
                        "unreachable": 0
                    },
                    "proxy07.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 54,
                        "skipped": 0,
                        "unreachable": 0
                    },
                    "proxy08.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 54,
                        "skipped": 0,
                        "unreachable": 0
                    },
                    "proxy09.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 54,
                        "skipped": 0,
                        "unreachable": 0
                    },
                    "proxy10.phx2.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 54,
                        "skipped": 0,
                        "unreachable": 0
                    },
                    "proxy11.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 54,
                        "skipped": 0,
                        "unreachable": 0
                    }
                },
                "userid": "lmacken"
            },
            "msg_id": "2015-de60d578-7092-4fc4-af6b-713873bc1e5b",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1436290963.0,
            "topic": "org.fedoraproject.prod.ansible.playbook.complete"
        },
        {
            "i": 1,
            "msg": {
                "check": False,
                "extra_vars": {},
                "inventory": "/srv/web/infra/ansible/inventory/",
                "playbook": "/home/fedora/lmacken/ansible/playbooks/groups/proxies.yml",
                "playbook_checksum": False,
                "userid": "lmacken"
            },
            "msg_id": "2015-15437abe-3948-45e1-b6f7-7e5d789ecd60",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1436290844.0,
            "topic": "org.fedoraproject.prod.ansible.playbook.start"
        },
        {
            "i": 2,
            "msg": {
                "playbook": "/home/fedora/lmacken/ansible/playbooks/groups/proxies.yml",
                "results": {
                    "proxy01.phx2.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 14,
                        "skipped": 1,
                        "unreachable": 0
                    },
                    "proxy01.stg.phx2.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 14,
                        "skipped": 1,
                        "unreachable": 0
                    },
                    "proxy02.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 14,
                        "skipped": 1,
                        "unreachable": 0
                    },
                    "proxy03.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 14,
                        "skipped": 1,
                        "unreachable": 0
                    },
                    "proxy04.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 14,
                        "skipped": 1,
                        "unreachable": 0
                    },
                    "proxy05.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 14,
                        "skipped": 1,
                        "unreachable": 0
                    },
                    "proxy06.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 14,
                        "skipped": 1,
                        "unreachable": 0
                    },
                    "proxy07.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 14,
                        "skipped": 1,
                        "unreachable": 0
                    },
                    "proxy08.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 14,
                        "skipped": 1,
                        "unreachable": 0
                    },
                    "proxy09.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 14,
                        "skipped": 1,
                        "unreachable": 0
                    },
                    "proxy10.phx2.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 14,
                        "skipped": 1,
                        "unreachable": 0
                    },
                    "proxy11.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 14,
                        "skipped": 1,
                        "unreachable": 0
                    }
                },
                "userid": "lmacken"
            },
            "msg_id": "2015-7754e09c-88aa-43c4-9a67-65cf09709db2",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1436290826.0,
            "topic": "org.fedoraproject.prod.ansible.playbook.complete"
        },
        {
            "i": 1,
            "msg": {
                "check": False,
                "extra_vars": {},
                "inventory": "/srv/web/infra/ansible/inventory/",
                "playbook": "/home/fedora/lmacken/ansible/playbooks/groups/proxies.yml",
                "playbook_checksum": False,
                "userid": "lmacken"
            },
            "msg_id": "2015-1108ff47-65fd-4769-90ec-2d3c7dcb0385",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1436290755.0,
            "topic": "org.fedoraproject.prod.ansible.playbook.start"
        },
        {
            "i": 2,
            "msg": {
                "playbook": "/home/fedora/lmacken/ansible/playbooks/groups/bodhi2.yml",
                "results": {
                    "bodhi02.stg.phx2.fedoraproject.org": {
                        "changed": 2,
                        "failures": 0,
                        "ok": 107,
                        "skipped": 41,
                        "unreachable": 0
                    }
                },
                "userid": "lmacken"
            },
            "msg_id": "2015-0d2909e5-ac3e-4515-a6b1-1eee223ee123",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1436290620.0,
            "topic": "org.fedoraproject.prod.ansible.playbook.complete"
        },
        {
            "i": 1,
            "msg": {
                "check": False,
                "extra_vars": {},
                "inventory": "/srv/web/infra/ansible/inventory/",
                "playbook": "/home/fedora/lmacken/ansible/playbooks/groups/bodhi2.yml",
                "playbook_checksum": False,
                "userid": "lmacken"
            },
            "msg_id": "2015-f5356b7b-4b8c-4a9a-a746-64a3e5ca7fbf",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1436290558.0,
            "topic": "org.fedoraproject.prod.ansible.playbook.start"
        },
        {
            "i": 2,
            "msg": {
                "playbook": "/home/fedora/lmacken/ansible/playbooks/groups/bodhi2.yml",
                "results": {
                    "bodhi02.stg.phx2.fedoraproject.org": {
                        "changed": 6,
                        "failures": 0,
                        "ok": 108,
                        "skipped": 41,
                        "unreachable": 0
                    }
                },
                "userid": "lmacken"
            },
            "msg_id": "2015-b9b6eb6b-2768-4a04-85fa-76c318dd3012",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1436290350.0,
            "topic": "org.fedoraproject.prod.ansible.playbook.complete"
        },
        {
            "i": 1,
            "msg": {
                "check": False,
                "extra_vars": {},
                "inventory": "/srv/web/infra/ansible/inventory/",
                "playbook": "/home/fedora/lmacken/ansible/playbooks/groups/bodhi2.yml",
                "playbook_checksum": False,
                "userid": "lmacken"
            },
            "msg_id": "2015-e5670762-fa5c-49e5-b788-3fa33a6ac2ca",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1436290291.0,
            "topic": "org.fedoraproject.prod.ansible.playbook.start"
        },
        {
            "i": 2,
            "msg": {
                "playbook": "/home/fedora/lmacken/ansible/playbooks/groups/proxies.yml",
                "results": {
                    "proxy01.stg.phx2.fedoraproject.org": {
                        "changed": 0,
                        "failures": 0,
                        "ok": 14,
                        "skipped": 1,
                        "unreachable": 0
                    }
                },
                "userid": "lmacken"
            },
            "msg_id": "2015-819bcbfe-b9c3-4a09-b546-41249c0068ce",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1436290275.0,
            "topic": "org.fedoraproject.prod.ansible.playbook.complete"
        },
        {
            "i": 1,
            "msg": {
                "check": False,
                "extra_vars": {},
                "inventory": "/srv/web/infra/ansible/inventory/",
                "playbook": "/home/fedora/lmacken/ansible/playbooks/groups/proxies.yml",
                "playbook_checksum": False,
                "userid": "lmacken"
            },
            "msg_id": "2015-4c68804b-ba66-43a7-a064-cb85cf03d1d0",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1436290267.0,
            "topic": "org.fedoraproject.prod.ansible.playbook.start"
        },
        {
            "i": 2,
            "msg": {
                "playbook": "/home/fedora/lmacken/ansible/playbooks/groups/proxies.yml",
                "results": {
                    "proxy01.stg.phx2.fedoraproject.org": {
                        "changed": 2,
                        "failures": 0,
                        "ok": 55,
                        "skipped": 0,
                        "unreachable": 0
                    }
                },
                "userid": "lmacken"
            },
            "msg_id": "2015-5c577688-1682-4a70-a2f1-05f1bef88499",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1436290178.0,
            "topic": "org.fedoraproject.prod.ansible.playbook.complete"
        },
        {
            "i": 1,
            "msg": {
                "check": False,
                "extra_vars": {},
                "inventory": "/srv/web/infra/ansible/inventory/",
                "playbook": "/home/fedora/lmacken/ansible/playbooks/groups/proxies.yml",
                "playbook_checksum": False,
                "userid": "lmacken"
            },
            "msg_id": "2015-5045127a-aef8-48ac-b4ea-f22871640ee2",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1436290155.0,
            "topic": "org.fedoraproject.prod.ansible.playbook.start"
        },
        {
            "i": 2,
            "msg": {
                "playbook": "/srv/web/infra/ansible/playbooks/groups/jenkins-cloud.yml",
                "results": {
                    "209.132.184.137": {
                        "changed": 4,
                        "failures": 0,
                        "ok": 28,
                        "skipped": 25,
                        "unreachable": 0
                    },
                    "209.132.184.153": {
                        "changed": 8,
                        "failures": 0,
                        "ok": 78,
                        "skipped": 20,
                        "unreachable": 0
                    },
                    "209.132.184.165": {
                        "changed": 4,
                        "failures": 0,
                        "ok": 28,
                        "skipped": 25,
                        "unreachable": 0
                    },
                    "209.132.184.209": {
                        "changed": 11,
                        "failures": 0,
                        "ok": 36,
                        "skipped": 17,
                        "unreachable": 0
                    },
                    "jenkins-f22.fedorainfracloud.org": {
                        "changed": 11,
                        "failures": 0,
                        "ok": 32,
                        "skipped": 7,
                        "unreachable": 0
                    }
                },
                "userid": "kevin"
            },
            "msg_id": "2015-0a7d8ad6-0867-4eb9-8a45-92c1ade0f2ed",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1436289694.0,
            "topic": "org.fedoraproject.prod.ansible.playbook.complete"
        },
        {
            "i": 1,
            "msg": {
                "check": False,
                "extra_vars": {},
                "inventory": "/srv/web/infra/ansible/inventory/",
                "playbook": "/srv/web/infra/ansible/playbooks/groups/jenkins-cloud.yml",
                "playbook_checksum": False,
                "userid": "kevin"
            },
            "msg_id": "2015-6f4cdf28-13af-43d6-9993-e4df7a4417cb",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1436289416.0,
            "topic": "org.fedoraproject.prod.ansible.playbook.start"
        },
        {
            "i": 2,
            "msg": {
                "playbook": "/srv/web/infra/ansible/playbooks/groups/jenkins-cloud.yml",
                "results": {
                    "jenkins-f22.fedorainfracloud.org": {
                        "changed": 11,
                        "failures": 0,
                        "ok": 32,
                        "skipped": 7,
                        "unreachable": 0
                    }
                },
                "userid": "kevin"
            },
            "msg_id": "2015-10fab449-03b0-4c87-b97c-d6efd9c8daed",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1436288964.0,
            "topic": "org.fedoraproject.prod.ansible.playbook.complete"
        },
        {
            "i": 1,
            "msg": {
                "check": False,
                "extra_vars": {},
                "inventory": "/srv/web/infra/ansible/inventory/",
                "playbook": "/srv/web/infra/ansible/playbooks/groups/jenkins-cloud.yml",
                "playbook_checksum": False,
                "userid": "kevin"
            },
            "msg_id": "2015-9e986ed7-2458-4531-b9e7-98886489bc4c",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1436288838.0,
            "topic": "org.fedoraproject.prod.ansible.playbook.start"
        },
        {
            "i": 2,
            "msg": {
                "playbook": "/srv/web/infra/ansible/playbooks/groups/jenkins-cloud.yml",
                "results": {
                    "jenkins-f22.fedorainfracloud.org": {
                        "changed": 11,
                        "failures": 0,
                        "ok": 32,
                        "skipped": 7,
                        "unreachable": 0
                    }
                },
                "userid": "kevin"
            },
            "msg_id": "2015-85796b67-65fc-49bb-b04f-571aa9b2061d",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1436288816.0,
            "topic": "org.fedoraproject.prod.ansible.playbook.complete"
        },
        {
            "i": 1,
            "msg": {
                "check": False,
                "extra_vars": {},
                "inventory": "/srv/web/infra/ansible/inventory/",
                "playbook": "/srv/web/infra/ansible/playbooks/groups/jenkins-cloud.yml",
                "playbook_checksum": False,
                "userid": "kevin"
            },
            "msg_id": "2015-0a51512d-2882-497b-a5d5-5247d91ba4d9",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1436288687.0,
            "topic": "org.fedoraproject.prod.ansible.playbook.start"
        },
        {
            "i": 2,
            "msg": {
                "playbook": "/srv/web/infra/ansible/playbooks/groups/jenkins-cloud.yml",
                "results": {
                    "jenkins-f22.fedorainfracloud.org": {
                        "changed": 18,
                        "failures": 0,
                        "ok": 33,
                        "skipped": 7,
                        "unreachable": 0
                    }
                },
                "userid": "kevin"
            },
            "msg_id": "2015-10188bc8-a4f2-44b8-b84e-bd077323100f",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1436288669.0,
            "topic": "org.fedoraproject.prod.ansible.playbook.complete"
        },
        {
            "i": 1,
            "msg": {
                "check": False,
                "extra_vars": {},
                "inventory": "/srv/web/infra/ansible/inventory/",
                "playbook": "/srv/web/infra/ansible/playbooks/groups/jenkins-cloud.yml",
                "playbook_checksum": False,
                "userid": "kevin"
            },
            "msg_id": "2015-30f9d339-a556-47a9-ae5a-c05a2ea4f271",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1436288540.0,
            "topic": "org.fedoraproject.prod.ansible.playbook.start"
        },
        {
            "i": 2,
            "msg": {
                "playbook": "/srv/web/infra/ansible/playbooks/groups/jenkins-cloud.yml",
                "results": {
                    "jenkins-f22.fedorainfracloud.org": {
                        "changed": 4,
                        "failures": 1,
                        "ok": 19,
                        "skipped": 7,
                        "unreachable": 0
                    }
                },
                "userid": "kevin"
            },
            "msg_id": "2015-284b3e88-797c-4dd0-95af-8f76240c7de3",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1436287656.0,
            "topic": "org.fedoraproject.prod.ansible.playbook.complete"
        },
        {
            "i": 1,
            "msg": {
                "check": False,
                "extra_vars": {},
                "inventory": "/srv/web/infra/ansible/inventory/",
                "playbook": "/srv/web/infra/ansible/playbooks/groups/jenkins-cloud.yml",
                "playbook_checksum": False,
                "userid": "kevin"
            },
            "msg_id": "2015-19625863-9b34-496e-a6be-a833f41ffaf0",
            "source_name": "datanommer",
            "source_version": "0.6.5",
            "timestamp": 1436287486.0,
            "topic": "org.fedoraproject.prod.ansible.playbook.start"
        }
    ]
