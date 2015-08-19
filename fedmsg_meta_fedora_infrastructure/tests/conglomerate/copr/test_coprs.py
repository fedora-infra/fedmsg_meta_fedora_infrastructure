import fedmsg.tests.test_meta

import arrow


class TestCoprConglomerateByUser(
        fedmsg.tests.test_meta.ConglomerateBase):
    expected = [{
        'categories': set(['copr']),
        'end_time': 1436455206.0,
        'human_time': arrow.get(1436455009.7142856).humanize(),
        'icon': 'https://apps.fedoraproject.org/img/icons/copr.png',
        'link': 'https://copr.fedoraproject.org/coprs/logocomune/seafile-client/',
        'packages': set([]),
        'secondary_icon': 'https://seccdn.libravatar.org/avatar/'
        '4638766eef9c176dac0b11adb9d1fd974d20d818a9b1ab9d3f78c7252f67fcf3'
        '?s=64&d=retro',
        'start_time': 1436454907.0,
        'subtitle': 'logocomune kicked off 5 rebuilds of the seafile-client copr',
        'subjective': 'logocomune kicked off 5 rebuilds of the seafile-client copr',
        'timestamp': 1436455009.7142856,
        'topics': set(['org.fedoraproject.prod.copr.build.end',
                        'org.fedoraproject.prod.copr.build.start',
                        'org.fedoraproject.prod.copr.chroot.start']),
        'usernames': set(['logocomune'])},
        {'categories': set(['copr']),
        'end_time': 1436455187.0,
        'human_time': arrow.get(1436455055.66).humanize(),
        'icon': 'https://apps.fedoraproject.org/img/icons/copr.png',
        'link': 'https://copr.fedoraproject.org/coprs/andykimpe/freshplayerplugin/',
        'packages': set([]),
        'secondary_icon': 'https://seccdn.libravatar.org/avatar/'
        '046b0af91b968fa7cc33360e0a5c2ba0fdde525780d45aecd54c902a10a5823b'
        '?s=64&d=retro',
        'start_time': 1436454810.0,
        'subtitle': 'andykimpe kicked off 3 rebuilds of the freshplayerplugin copr',
        'subjective': 'andykimpe kicked off 3 rebuilds of the freshplayerplugin copr',
        'timestamp': 1436455055.6666667,
        'topics': set(['org.fedoraproject.prod.copr.build.end',
                        'org.fedoraproject.prod.copr.build.start',
                        'org.fedoraproject.prod.copr.chroot.start']),
        'usernames': set(['andykimpe'])},
        {'categories': set(['copr']),
        'end_time': 1436455177.0,
        'human_time': arrow.get(1436455031.6).humanize(),
        'icon': 'https://apps.fedoraproject.org/img/icons/copr.png',
        'link': 'https://copr.fedoraproject.org/coprs/avsej/nim-devel/',
        'packages': set([]),
        'secondary_icon': 'https://seccdn.libravatar.org/avatar/'
        '8ae6c08d3b2c200def86e6a408e3f774fc885b6c42da85b550c8fdb32461fbb9'
        '?s=64&d=retro',
        'start_time': 1436454814.0,
        'subtitle': 'avsej kicked off 2 rebuilds of the nim-devel copr',
        'subjective': 'avsej kicked off 2 rebuilds of the nim-devel copr',
        'timestamp': 1436455031.6,
        'topics': set(['org.fedoraproject.prod.copr.build.end',
                        'org.fedoraproject.prod.copr.build.start',
                        'org.fedoraproject.prod.copr.chroot.start']),
        'usernames': set(['avsej'])},
    ]

    originals = [ {
        "i": 7,
        "msg": {
            "build": 103162,
            "copr": "seafile-client",
            "ip": "172.25.86.29",
            "owner": "logocomune",
            "pid": 10140,
            "pkg": "seafile-client-qt5-4.2.7-1.fc20",
            "user": "logocomune",
            "what": "build start: user:logocomune copr:seafile-clientpkg: seafile-client-qt5-4.2.7-1.fc20 build:103162 ip:172.25.86.29  pid:10140",
            "who": "worker-27"
        },
        "msg_id": "2015-2a2b5942-c638-416d-85f4-254c800ead28",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436455206.0,
        "topic": "org.fedoraproject.prod.copr.build.start"
    },
    {
        "i": 8,
        "msg": {
            "build": 103162,
            "chroot": "fedora-22-x86_64",
            "copr": "seafile-client",
            "ip": "172.25.86.29",
            "owner": "logocomune",
            "pid": 10140,
            "pkg": "seafile-client-qt5-4.2.7-1.fc20",
            "user": "logocomune",
            "what": "chroot start: chroot:fedora-22-x86_64 user:logocomunecopr:seafile-client pkg: seafile-client-qt5-4.2.7-1.fc20 build:103162 ip:172.25.86.29  pid:10140",
            "who": "worker-27"
        },
        "msg_id": "2015-0b702c9c-7951-4e40-80ab-946e40842e30",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436455206.0,
        "topic": "org.fedoraproject.prod.copr.chroot.start"
    },
    {
        "i": 8,
        "msg": {
            "build": 103137,
            "copr": "freshplayerplugin",
            "ip": "172.25.86.32",
            "owner": "andykimpe",
            "pid": 10122,
            "pkg": "chromium-42.0.2311.152-1.el6",
            "user": "andykimpe",
            "what": "build start: user:andykimpe copr:freshplayerpluginpkg: chromium-42.0.2311.152-1.el6 build:103137 ip:172.25.86.32  pid:10122",
            "who": "worker-21"
        },
        "msg_id": "2015-d786cf7e-f7ad-4612-9b28-a987774aab05",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436455187.0,
        "topic": "org.fedoraproject.prod.copr.build.start"
    },
    {
        "i": 9,
        "msg": {
            "build": 103137,
            "chroot": "fedora-rawhide-i386",
            "copr": "freshplayerplugin",
            "ip": "172.25.86.32",
            "owner": "andykimpe",
            "pid": 10122,
            "pkg": "chromium-42.0.2311.152-1.el6",
            "user": "andykimpe",
            "what": "chroot start: chroot:fedora-rawhide-i386 user:andykimpecopr:freshplayerplugin pkg: chromium-42.0.2311.152-1.el6 build:103137 ip:172.25.86.32  pid:10122",
            "who": "worker-21"
        },
        "msg_id": "2015-faf0c84a-b40f-43d0-890e-a33e568469ce",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436455187.0,
        "topic": "org.fedoraproject.prod.copr.chroot.start"
    },
    {
        "i": 9,
        "msg": {
            "build": 103154,
            "chroot": "fedora-rawhide-i386",
            "copr": "seafile-client",
            "ip": "172.25.86.29",
            "owner": "logocomune",
            "pid": 10076,
            "pkg": "seafile-4.2.7-1.fc20",
            "status": 1,
            "user": "logocomune",
            "version": "4.2.7-1.fc20",
            "what": "build end: user:logocomune copr:seafile-client build:103154  pkg: seafile-4.2.7-1.fc20  version: 4.2.7-1.fc20 ip:172.25.86.29  pid:10076 status:1",
            "who": "worker-6"
        },
        "msg_id": "2015-16295a6a-e05a-4129-97a2-df51916af19e",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436455184.0,
        "topic": "org.fedoraproject.prod.copr.build.end"
    },
    {
        "i": 10,
        "msg": {
            "build": 103168,
            "copr": "nim-devel",
            "ip": "172.25.86.30",
            "owner": "avsej",
            "pid": 10091,
            "pkg": "nim-0.11.3-836.g218c61a.el7.centos",
            "user": "avsej",
            "what": "build start: user:avsej copr:nim-develpkg: nim-0.11.3-836.g218c61a.el7.centos build:103168 ip:172.25.86.30  pid:10091",
            "who": "worker-11"
        },
        "msg_id": "2015-c1fb8f9e-53a6-4adb-8222-624a43c0bdf6",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436455177.0,
        "topic": "org.fedoraproject.prod.copr.build.start"
    },
    {
        "i": 11,
        "msg": {
            "build": 103168,
            "chroot": "fedora-22-x86_64",
            "copr": "nim-devel",
            "ip": "172.25.86.30",
            "owner": "avsej",
            "pid": 10091,
            "pkg": "nim-0.11.3-836.g218c61a.el7.centos",
            "user": "avsej",
            "what": "chroot start: chroot:fedora-22-x86_64 user:avsejcopr:nim-devel pkg: nim-0.11.3-836.g218c61a.el7.centos build:103168 ip:172.25.86.30  pid:10091",
            "who": "worker-11"
        },
        "msg_id": "2015-8e1126fa-6ac3-44a9-a73b-8d5c176889b6",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436455177.0,
        "topic": "org.fedoraproject.prod.copr.chroot.start"
    },
    {
        "i": 6,
        "msg": {
            "build": 103168,
            "chroot": "fedora-22-i386",
            "copr": "nim-devel",
            "ip": "172.25.86.30",
            "owner": "avsej",
            "pid": 10140,
            "pkg": "nim-0.11.3-836.g218c61a.el7.centos",
            "status": 1,
            "user": "avsej",
            "version": "0.11.3-836.g218c61a.el7.centos",
            "what": "build end: user:avsej copr:nim-devel build:103168  pkg: nim-0.11.3-836.g218c61a.el7.centos  version: 0.11.3-836.g218c61a.el7.centos ip:172.25.86.30  pid:10140 status:1",
            "who": "worker-27"
        },
        "msg_id": "2015-93bb0c96-e0e6-4cf3-a51b-ab545a656d0c",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436455176.0,
        "topic": "org.fedoraproject.prod.copr.build.end"
    },
    {
        "i": 17,
        "msg": {
            "build": 103164,
            "chroot": "epel-6-i386",
            "copr": "freshplayerplugin",
            "ip": "172.25.86.32",
            "owner": "andykimpe",
            "pid": 10085,
            "pkg": "chromiumlibs-glib2-2.36.3-4.el6",
            "status": 0,
            "user": "andykimpe",
            "version": "2.36.3-4.el6",
            "what": "build end: user:andykimpe copr:freshplayerplugin build:103164  pkg: chromiumlibs-glib2-2.36.3-4.el6  version: 2.36.3-4.el6 ip:172.25.86.32  pid:10085 status:0",
            "who": "worker-9"
        },
        "msg_id": "2015-8bb726fb-d01f-4c6a-95cb-8af51a9e74a1",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436455158.0,
        "topic": "org.fedoraproject.prod.copr.build.end"
    },
    {
        "i": 7,
        "msg": {
            "build": 103162,
            "copr": "seafile-client",
            "ip": "172.25.86.33",
            "owner": "logocomune",
            "pid": 10107,
            "pkg": "seafile-client-qt5-4.2.7-1.fc20",
            "user": "logocomune",
            "what": "build start: user:logocomune copr:seafile-clientpkg: seafile-client-qt5-4.2.7-1.fc20 build:103162 ip:172.25.86.33  pid:10107",
            "who": "worker-16"
        },
        "msg_id": "2015-63d7d786-5637-41be-af2b-7df91345f686",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436455068.0,
        "topic": "org.fedoraproject.prod.copr.build.start"
    },
    {
        "i": 8,
        "msg": {
            "build": 103162,
            "chroot": "epel-7-x86_64",
            "copr": "seafile-client",
            "ip": "172.25.86.33",
            "owner": "logocomune",
            "pid": 10107,
            "pkg": "seafile-client-qt5-4.2.7-1.fc20",
            "user": "logocomune",
            "what": "chroot start: chroot:epel-7-x86_64 user:logocomunecopr:seafile-client pkg: seafile-client-qt5-4.2.7-1.fc20 build:103162 ip:172.25.86.33  pid:10107",
            "who": "worker-16"
        },
        "msg_id": "2015-6516ad8f-e54e-4e54-ab50-519a1c20ee05",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436455068.0,
        "topic": "org.fedoraproject.prod.copr.chroot.start"
    },
    {
        "i": 15,
        "msg": {
            "build": 103164,
            "copr": "freshplayerplugin",
            "ip": "172.25.86.32",
            "owner": "andykimpe",
            "pid": 10085,
            "pkg": "chromiumlibs-glib2-2.36.3-4.el6",
            "user": "andykimpe",
            "what": "build start: user:andykimpe copr:freshplayerpluginpkg: chromiumlibs-glib2-2.36.3-4.el6 build:103164 ip:172.25.86.32  pid:10085",
            "who": "worker-9"
        },
        "msg_id": "2015-3398ecef-627c-467a-9acb-b72049394850",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436454996.0,
        "topic": "org.fedoraproject.prod.copr.build.start"
    },
    {
        "i": 16,
        "msg": {
            "build": 103164,
            "chroot": "epel-6-i386",
            "copr": "freshplayerplugin",
            "ip": "172.25.86.32",
            "owner": "andykimpe",
            "pid": 10085,
            "pkg": "chromiumlibs-glib2-2.36.3-4.el6",
            "user": "andykimpe",
            "what": "chroot start: chroot:epel-6-i386 user:andykimpecopr:freshplayerplugin pkg: chromiumlibs-glib2-2.36.3-4.el6 build:103164 ip:172.25.86.32  pid:10085",
            "who": "worker-9"
        },
        "msg_id": "2015-f0460a03-6358-494a-8dd1-0def62fef6d0",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436454996.0,
        "topic": "org.fedoraproject.prod.copr.chroot.start"
    },
    {
        "i": 13,
        "msg": {
            "build": 103162,
            "copr": "seafile-client",
            "ip": "172.25.86.18",
            "owner": "logocomune",
            "pid": 10143,
            "pkg": "seafile-client-qt5-4.2.7-1.fc20",
            "user": "logocomune",
            "what": "build start: user:logocomune copr:seafile-clientpkg: seafile-client-qt5-4.2.7-1.fc20 build:103162 ip:172.25.86.18  pid:10143",
            "who": "worker-28"
        },
        "msg_id": "2015-273d056f-d806-4893-8969-f9aabf88f2c3",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436454961.0,
        "topic": "org.fedoraproject.prod.copr.build.start"
    },
    {
        "i": 14,
        "msg": {
            "build": 103162,
            "chroot": "fedora-21-x86_64",
            "copr": "seafile-client",
            "ip": "172.25.86.18",
            "owner": "logocomune",
            "pid": 10143,
            "pkg": "seafile-client-qt5-4.2.7-1.fc20",
            "user": "logocomune",
            "what": "chroot start: chroot:fedora-21-x86_64 user:logocomunecopr:seafile-client pkg: seafile-client-qt5-4.2.7-1.fc20 build:103162 ip:172.25.86.18  pid:10143",
            "who": "worker-28"
        },
        "msg_id": "2015-d1e64ce4-f7c7-4639-ad99-ee391115db85",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436454961.0,
        "topic": "org.fedoraproject.prod.copr.chroot.start"
    },
    {
        "i": 9,
        "msg": {
            "build": 103161,
            "chroot": "fedora-22-x86_64",
            "copr": "seafile-client",
            "ip": "172.25.86.18",
            "owner": "logocomune",
            "pid": 10088,
            "pkg": "seafile-client-qt-4.2.7-1.fc20",
            "status": 1,
            "user": "logocomune",
            "version": "4.2.7-1.fc20",
            "what": "build end: user:logocomune copr:seafile-client build:103161  pkg: seafile-client-qt-4.2.7-1.fc20  version: 4.2.7-1.fc20 ip:172.25.86.18  pid:10088 status:1",
            "who": "worker-10"
        },
        "msg_id": "2015-363454be-447b-469a-840d-17074cb22385",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436454951.0,
        "topic": "org.fedoraproject.prod.copr.build.end"
    },
    {
        "i": 7,
        "msg": {
            "build": 103154,
            "copr": "seafile-client",
            "ip": "172.25.86.29",
            "owner": "logocomune",
            "pid": 10076,
            "pkg": "seafile-4.2.7-1.fc20",
            "user": "logocomune",
            "what": "build start: user:logocomune copr:seafile-clientpkg: seafile-4.2.7-1.fc20 build:103154 ip:172.25.86.29  pid:10076",
            "who": "worker-6"
        },
        "msg_id": "2015-a48dc863-6888-4dff-b4c8-e6f750896fc2",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436454932.0,
        "topic": "org.fedoraproject.prod.copr.build.start"
    },
    {
        "i": 8,
        "msg": {
            "build": 103154,
            "chroot": "fedora-rawhide-i386",
            "copr": "seafile-client",
            "ip": "172.25.86.29",
            "owner": "logocomune",
            "pid": 10076,
            "pkg": "seafile-4.2.7-1.fc20",
            "user": "logocomune",
            "what": "chroot start: chroot:fedora-rawhide-i386 user:logocomunecopr:seafile-client pkg: seafile-4.2.7-1.fc20 build:103154 ip:172.25.86.29  pid:10076",
            "who": "worker-6"
        },
        "msg_id": "2015-bb7d7971-875e-4aeb-9bcd-9d4368bef505",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436454932.0,
        "topic": "org.fedoraproject.prod.copr.chroot.start"
    },
    {
        "i": 12,
        "msg": {
            "build": 103161,
            "chroot": "fedora-20-x86_64",
            "copr": "seafile-client",
            "ip": "172.25.86.29",
            "owner": "logocomune",
            "pid": 10143,
            "pkg": "seafile-client-qt-4.2.7-1.fc20",
            "status": 1,
            "user": "logocomune",
            "version": "4.2.7-1.fc20",
            "what": "build end: user:logocomune copr:seafile-client build:103161  pkg: seafile-client-qt-4.2.7-1.fc20  version: 4.2.7-1.fc20 ip:172.25.86.29  pid:10143 status:1",
            "who": "worker-28"
        },
        "msg_id": "2015-b97ee951-f950-4a0b-bb16-8320b7a9d80e",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436454930.0,
        "topic": "org.fedoraproject.prod.copr.build.end"
    },
    {
        "i": 13,
        "msg": {
            "build": 103162,
            "copr": "seafile-client",
            "ip": "172.25.86.27",
            "owner": "logocomune",
            "pid": 10079,
            "pkg": "seafile-client-qt5-4.2.7-1.fc20",
            "user": "logocomune",
            "what": "build start: user:logocomune copr:seafile-clientpkg: seafile-client-qt5-4.2.7-1.fc20 build:103162 ip:172.25.86.27  pid:10079",
            "who": "worker-7"
        },
        "msg_id": "2015-c513fb14-a1e2-4ba8-8427-70412b6276b8",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436454915.0,
        "topic": "org.fedoraproject.prod.copr.build.start"
    },
    {
        "i": 14,
        "msg": {
            "build": 103162,
            "chroot": "fedora-22-i386",
            "copr": "seafile-client",
            "ip": "172.25.86.27",
            "owner": "logocomune",
            "pid": 10079,
            "pkg": "seafile-client-qt5-4.2.7-1.fc20",
            "user": "logocomune",
            "what": "chroot start: chroot:fedora-22-i386 user:logocomunecopr:seafile-client pkg: seafile-client-qt5-4.2.7-1.fc20 build:103162 ip:172.25.86.27  pid:10079",
            "who": "worker-7"
        },
        "msg_id": "2015-9eae696a-215a-4c52-9056-42e44261a8c8",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436454915.0,
        "topic": "org.fedoraproject.prod.copr.chroot.start"
    },
    {
        "i": 14,
        "msg": {
            "build": 103161,
            "chroot": "fedora-rawhide-x86_64",
            "copr": "seafile-client",
            "ip": "172.25.86.27",
            "owner": "logocomune",
            "pid": 10064,
            "pkg": "seafile-client-qt-4.2.7-1.fc20",
            "status": 1,
            "user": "logocomune",
            "version": "4.2.7-1.fc20",
            "what": "build end: user:logocomune copr:seafile-client build:103161  pkg: seafile-client-qt-4.2.7-1.fc20  version: 4.2.7-1.fc20 ip:172.25.86.27  pid:10064 status:1",
            "who": "worker-2"
        },
        "msg_id": "2015-9a9506fd-dfae-4493-b7f8-70faaec320dc",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436454907.0,
        "topic": "org.fedoraproject.prod.copr.build.end"
    },
    {
        "i": 4,
        "msg": {
            "build": 103168,
            "copr": "nim-devel",
            "ip": "172.25.86.30",
            "owner": "avsej",
            "pid": 10140,
            "pkg": "nim-0.11.3-836.g218c61a.el7.centos",
            "user": "avsej",
            "what": "build start: user:avsej copr:nim-develpkg: nim-0.11.3-836.g218c61a.el7.centos build:103168 ip:172.25.86.30  pid:10140",
            "who": "worker-27"
        },
        "msg_id": "2015-6e90808a-7108-4ce6-9078-f7909b3f10c8",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436454814.0,
        "topic": "org.fedoraproject.prod.copr.build.start"
    },
    {
        "i": 5,
        "msg": {
            "build": 103168,
            "chroot": "fedora-22-i386",
            "copr": "nim-devel",
            "ip": "172.25.86.30",
            "owner": "avsej",
            "pid": 10140,
            "pkg": "nim-0.11.3-836.g218c61a.el7.centos",
            "user": "avsej",
            "what": "chroot start: chroot:fedora-22-i386 user:avsejcopr:nim-devel pkg: nim-0.11.3-836.g218c61a.el7.centos build:103168 ip:172.25.86.30  pid:10140",
            "who": "worker-27"
        },
        "msg_id": "2015-d0b37df2-092a-4128-b377-27e87b6c5e51",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436454814.0,
        "topic": "org.fedoraproject.prod.copr.chroot.start"
    },
    {
        "i": 10,
        "msg": {
            "build": 103137,
            "copr": "freshplayerplugin",
            "ip": "172.25.86.87",
            "owner": "andykimpe",
            "pid": 10137,
            "pkg": "chromium-42.0.2311.152-1.el6",
            "user": "andykimpe",
            "what": "build start: user:andykimpe copr:freshplayerpluginpkg: chromium-42.0.2311.152-1.el6 build:103137 ip:172.25.86.87  pid:10137",
            "who": "worker-26"
        },
        "msg_id": "2015-4d522fa3-8290-4035-954c-84897f9fdb00",
        "source_name": "datanommer",
        "source_version": "0.6.5",
        "timestamp": 1436454810.0,
        "topic": "org.fedoraproject.prod.copr.build.start"
    }]
