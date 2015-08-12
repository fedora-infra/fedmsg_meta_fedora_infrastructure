import fedmsg.tests.test_meta
import arrow

class TestPkgdbConglomerateCommentSubject(
        fedmsg.tests.test_meta.ConglomerateBase):
    originals = [{
        "source_name": "datanommer",
        "i": 25,
        "timestamp": 1416428310.0,
        "msg_id": "2014-9e46f5ce-4881-4497-aec4-89cf83332b2d",
        "topic": "org.fedoraproject.prod.pkgdb.acl.update",
        "source_version": "0.6.4",
        "msg": {
            "status": "Approved",
            "username": "mcepl",
            "package_listing": {
                "status": "Approved",
                "point_of_contact": "mcepl",
                "package": {
                    "status": "Approved",
                    "upstream_url": "https://cryptography.io/",
                    "description": "",
                    "creation_date": 1416428295.0,
                    "acls": [],
                    "summary": "PyCA's cryptography library",
                    "review_url": "https://bugzilla.redhat.com/1114267",
                    "name": "python-cryptography"
                },
                "collection": {
                    "status": "Under Development",
                    "dist_tag": ".fc22",
                    "koji_name": "rawhide",
                    "name": "Fedora",
                    "version": "devel",
                    "branchname": "master"
                },
                "critpath": False,
                "status_change": 1416428298.0
            },
            "package_name": "python-cryptography",
            "agent": "limb",
            "previous_status": "",
            "acl": "approveacls"
        }
    },
    {
        "source_name": "datanommer",
        "i": 20,
        "timestamp": 1416428307.0,
        "msg_id": "2014-06ef29dd-adb5-47d8-92aa-f1ead0c4d8f1",
        "topic": "org.fedoraproject.prod.pkgdb.acl.update",
        "source_version": "0.6.4",
        "msg": {
            "status": "Approved",
            "username": "mcepl",
            "package_listing": {
                "status": "Approved",
                "point_of_contact": "mcepl",
                "package": {
                    "status": "Approved",
                    "upstream_url": "https://cryptography.io/",
                    "description": "",
                    "creation_date": 1416428295.0,
                    "acls": [],
                    "summary": "PyCA's cryptography library",
                    "review_url": "https://bugzilla.redhat.com/1114267",
                    "name": "python-cryptography"
                },
                "collection": {
                    "status": "Under Development",
                    "dist_tag": ".el7",
                    "koji_name": "epel7",
                    "name": "Fedora EPEL",
                    "version": "7",
                    "branchname": "epel7"
                },
                "acls": [ {
                    "fas_name": "mcepl",
                    "status": "Approved",
                    "acl": "commit"
                }, {
                    "fas_name": "mcepl",
                    "status": "Approved",
                    "acl": "watchbugzilla"
                }, {
                    "fas_name": "mcepl",
                    "status": "Approved",
                    "acl": "watchcommits"
                } ],
                "critpath": False,
                "status_change": 1416428298.0
            },
            "package_name": "python-cryptography",
            "agent": "limb",
            "previous_status": "",
            "acl": "watchcommits"
        }
    },
    ]
    expected = [{
        'subtitle': 'limb changed mcepl\'s approveacls and watchcommits '
        'permissions on python-cryptography (epel7 and master) '
        'to Approved.',
        'subjective': 'limb changed mcepl\'s approveacls and watchcommits '
        'permissions on python-cryptography (epel7 and master) '
        'to Approved.',
        'link': 'https://admin.fedoraproject.org/pkgdb/packager/mcepl/',

        'icon': 'https://apps.fedoraproject.org/packages/images/'
        'icons/package_128x128.png',
        'secondary_icon': 'https://seccdn.libravatar.org/avatar/'
        'f0496e0b40a4e1e780cb09ee8a89870aa0f90643fa36b095a9057be4c61ec3b6'
        '?s=64&d=retro',

        'start_time': 1416428307.0,
        'end_time': 1416428310.0,
        'timestamp': 1416428308.5,

        'human_time': arrow.get(1416428308.5).humanize(),

        'usernames': set(['mcepl', 'limb']),
        'packages': set(['python-cryptography']),
        'topics': set(['org.fedoraproject.prod.pkgdb.acl.update']),
        'categories': set(['pkgdb']),
        'msg_ids': [
            '2014-9e46f5ce-4881-4497-aec4-89cf83332b2d',
            '2014-06ef29dd-adb5-47d8-92aa-f1ead0c4d8f1',
        ],
    }]
