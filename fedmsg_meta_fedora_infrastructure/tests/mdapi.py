# This file is part of fedmsg.
# Copyright (C) 2015 Red Hat, Inc.
#
# fedmsg is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# fedmsg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with fedmsg; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Authors:  Pierre-Yves Chibon <pingou@pingoured.fr>
#
""" Tests for mdapi messages """

import unittest

from fedmsg_meta_fedora_infrastructure.tests.base import Base

from .common import add_doc


class TestNewProject(Base):
    """ These messages are published when a new project is created on
    `pagure <https://pagure.io>`_.
    """
    expected_title = "mdapi.repo.update"
    expected_subti = (
        'mdapi meta-data update: '
        'conflicts: +1/-2, '
        'enhances: +0/-0, '
        'files: +5/-4, '
        'obsoletes: +2/-2, '
        'packages: +2/-3, '
        'provides: +2/-2, '
        'recommends: +2/-1, '
        'requires: +2/-2, '
        'suggests: +2/-2, '
        'supplements: +0/-0')
    expected_link = "https://apps.fedoraproject.org/mdapi"
    expected_link = "https://download.fedoraproject.org/pub/fedora/linux/" + \
        "development/rawhide/x86_64/os/repodata/" + \
        "a0c75ee3abe48a4b602560d1c7c408d8d151caa1865678d2e0e1eb442d96ba90-" + \
        "filelists.sqlite.xz"
    expected_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_secondary_icon = "https://apps.fedoraproject.org/packages/" + \
        "images/icons/package_128x128.png"
    expected_packages = set([
        'java-1.8.0-openjdk-devel-debug',
        'vips',
        'python3-celery',
        'python3-dropbox',
        'libfdisk',
        'journal-brief',
        'meataxe',
        'rpm',
        'akonadi-mysql',
        'java-1.8.0-openjdk-headless',
        'python-wrapt-doc',
        'python3-yui',
        'python-faker-doc',
        'python3-PyQt4-devel',
        'boost',
        'PyOpenGL',
        'audit-libs-devel',
        'python-simplegeneric',
        'python-aniso8601',
        'python3',
        'django-markdown2',
        'python-pytools',
        'tyrus-container-servlet',
        'python3-devel',
        'waf-python3',
        'avahi-ui-sharp-devel',
        'python2-XStatic-roboto-fontface',
        'python-Traits',
    ])
    expected_usernames = set([])
    expected_objects = set([
        'rawhide/recommends/added/journal-brief',
        'rawhide/files/removed/python3-devel',
        'rawhide/provides/added/python2-XStatic-roboto-fontface',
        'rawhide/files/removed/python3-celery',
        'rawhide/provides/added/avahi-ui-sharp-devel(x86-64)',
        'rawhide/packages/removed/python-wrapt-doc',
        'rawhide/files/added/python3',
        'rawhide/files/added/java-1.8.0-openjdk-headless',
        'rawhide/obsoletes/removed/python-Traits(x86-64)',
        'rawhide/requires/removed/rpm',
        'rawhide/packages/removed/python3-dropbox',
        'rawhide/suggests/added/meataxe',
        'rawhide/recommends/removed/journal-brief',
        'rawhide/provides/removed/django-markdown2',
        'rawhide/conflicts/added/vips',
        'rawhide/files/removed/waf-python3',
        'rawhide/requires/added/libfdisk',
        'rawhide/recommends/added/akonadi-mysql',
        'rawhide/packages/added/python3-PyQt4-devel',
        'rawhide/obsoletes/added/python-pytools',
        'rawhide/obsoletes/added/python-aniso8601',
        'rawhide/conflicts/removed/vips',
        'rawhide/suggests/added/python-faker-doc',
        'rawhide/suggests/removed/python-faker-doc',
        'rawhide/requires/removed/boost(x86-32)',
        'rawhide/files/added/java-1.8.0-openjdk-devel-debug',
        'rawhide/packages/removed/audit-libs-devel',
        'rawhide/provides/removed/python3-yui(x86-64)',
        'rawhide/files/removed/java-1.8.0-openjdk-headless',
        'rawhide/requires/added/PyOpenGL',
        'rawhide/files/added/python3-celery',
        'rawhide/conflicts/removed/python3',
        'rawhide/packages/added/tyrus-container-servlet',
        'rawhide/obsoletes/removed/python-simplegeneric',
    ])
    msg = {
  "source_name": "datanommer",
  "certificate": "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUVWakNDQTcrZ0F3SUJBZ0lDQWpJd0RRWUpLb1pJaHZjTkFRRUZCUUF3Z2FBeEN6QUpCZ05WQkFZVEFsVlQKTVFzd0NRWURWUVFJRXdKT1F6RVFNQTRHQTFVRUJ4TUhVbUZzWldsbmFERVhNQlVHQTFVRUNoTU9SbVZrYjNKaApJRkJ5YjJwbFkzUXhEekFOQmdOVkJBc1RCbVpsWkcxelp6RVBNQTBHQTFVRUF4TUdabVZrYlhObk1ROHdEUVlEClZRUXBFd1ptWldSdGMyY3hKakFrQmdrcWhraUc5dzBCQ1FFV0YyRmtiV2x1UUdabFpHOXlZWEJ5YjJwbFkzUXUKYjNKbk1CNFhEVEUxTVRFd09URTFNRGN3TjFvWERUSTFNVEV3TmpFMU1EY3dOMW93Z2VReEN6QUpCZ05WQkFZVApBbFZUTVFzd0NRWURWUVFJRXdKT1F6RVFNQTRHQTFVRUJ4TUhVbUZzWldsbmFERVhNQlVHQTFVRUNoTU9SbVZrCmIzSmhJRkJ5YjJwbFkzUXhEekFOQmdOVkJBc1RCbVpsWkcxelp6RXhNQzhHQTFVRUF4TW9iV1JoY0drdGJXUmgKY0drd01TNXpkR2N1Y0doNE1pNW1aV1J2Y21Gd2NtOXFaV04wTG05eVp6RXhNQzhHQTFVRUtSTW9iV1JoY0drdApiV1JoY0drd01TNXpkR2N1Y0doNE1pNW1aV1J2Y21Gd2NtOXFaV04wTG05eVp6RW1NQ1FHQ1NxR1NJYjNEUUVKCkFSWVhZV1J0YVc1QVptVmtiM0poY0hKdmFtVmpkQzV2Y21jd2daOHdEUVlKS29aSWh2Y05BUUVCQlFBRGdZMEEKTUlHSkFvR0JBSzlPcmtWRUEyQXBPSUFwajZjTm95UEFzNjduaCswZTJHVzl4c0lCNEh3MkFkSUFERC9oVk1PeApZMitnSFA0SHRlb2F0dUpYcXpoZ0cybDJBNi8vTmVBQy9BZmhFSzJvUVcwNWs3K01nbklKbEdNb0ROU1hGL3FDCkdzNk1KL1VJdUQ1RXBCOTgwczNVSHRldjc0VnFVTE85Wi9UTkhIRTFOc1BKQVNOUlFtaVRBZ01CQUFHamdnRlgKTUlJQlV6QUpCZ05WSFJNRUFqQUFNQzBHQ1dDR1NBR0crRUlCRFFRZ0ZoNUZZWE41TFZKVFFTQkhaVzVsY21GMApaV1FnUTJWeWRHbG1hV05oZEdVd0hRWURWUjBPQkJZRUZMQXJsbEpZV3lTN2NLV1pSTkxRZzFITXptUTFNSUhWCkJnTlZIU01FZ2Mwd2djcUFGR3RBV3ZrU0NJbFo1MW5sQmZVQ0hRcE9meFFBb1lHbXBJR2pNSUdnTVFzd0NRWUQKVlFRR0V3SlZVekVMTUFrR0ExVUVDQk1DVGtNeEVEQU9CZ05WQkFjVEIxSmhiR1ZwWjJneEZ6QVZCZ05WQkFvVApEa1psWkc5eVlTQlFjbTlxWldOME1ROHdEUVlEVlFRTEV3Wm1aV1J0YzJjeER6QU5CZ05WQkFNVEJtWmxaRzF6Clp6RVBNQTBHQTFVRUtSTUdabVZrYlhObk1TWXdKQVlKS29aSWh2Y05BUWtCRmhkaFpHMXBia0JtWldSdmNtRncKY205cVpXTjBMbTl5WjRJSkFPTlFIa2RQRng1Rk1CTUdBMVVkSlFRTU1Bb0dDQ3NHQVFVRkJ3TUNNQXNHQTFVZApEd1FFQXdJSGdEQU5CZ2txaGtpRzl3MEJBUVVGQUFPQmdRQUN3dGhVTmxHVlJndjViKzBsUWNyMHlzVHVPM3ZKCmhKNHl3a2x4U2Z0TEZUWGlQTWVBeU5COWxUOHN0Tk00SkhLbmZjT2pScVAzRi9CVy8vUFdKczg0eEtza1dLeXQKWFI5NGp6RXl3bnBycENhOTdHbWFjZVRHM3h4ci9PQ1o4Q09OK3pqRjg1ODlDNWxMcFBFR1FTbG4rcU1PdWlXNAp2TzBseFNrQUtXeW1Odz09Ci0tLS0tRU5EIENFUlRJRklDQVRFLS0tLS0K",
  "i": 3,
  "timestamp": 1447413644.0,
  "msg_id": "2015-dbf52782-0a87-448f-a6fb-20c506cdd4eb",
  "topic": "org.fedoraproject.stg.mdapi.repo.update",
  "source_version": "0.6.5",
  "signature": "a4NsWrxIVQArE4FINUb/iE39KvD3dqYxrWhr7lmZf3FUz+4B7r72PWkv2TNZP324NCF0CNQgW/0kxM6xHqaCJPBStqOMzVDi+GTScBCZ1WHctuex7BNWeglSCyoehAy5vUAEVG4vrhAO+rajonVDcdt5WtOWSA0L67/WOQzV8jc=",
  "msg": {
    "url": "fedora/linux/development/rawhide/x86_64/os/repodata/a0c75ee3abe48a4b602560d1c7c408d8d151caa1865678d2e0e1eb442d96ba90-filelists.sqlite.xz",
    "differences": {
      "files": {
        "removed": [
          [
            "/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.60-17.b28.fc24.x86_64/jre/bin/tnameserv",
            "file",
            "java-1.8.0-openjdk-headless"
          ],
          [
            "/usr/bin/python3.4m-x86_64-config",
            "file",
            "python3-devel"
          ],
          [
            "/usr/bin/waf-3.4",
            "file",
            "waf-python3"
          ],
          [
            "/usr/lib/python3.4/site-packages/celery/tests/bin/__pycache__/test_beat.cpython-34.pyc",
            "file",
            "python3-celery"
          ]
        ],
        "added": [
          [
            "/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.65-1.b17.fc24.i386/jre/bin/orbd",
            "file",
            "java-1.8.0-openjdk-headless"
          ],
          [
            "/usr/lib/python3.5/site-packages/celery/bin/__pycache__/__init__.cpython-35.pyc",
            "file",
            "python3-celery"
          ],
          [
            "/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.65-1.b17.fc24.x86_64-debug/bin/rmiregistry",
            "file",
            "java-1.8.0-openjdk-devel-debug"
          ],
          [
            "/usr/lib/python3.5/site-packages/celery/tests/bin/test_celeryd_detach.py",
            "file",
            "python3-celery"
          ],
          [
            "/usr/bin/pydoc3.5",
            "file",
            "python3"
          ]
        ]
      },
      "enhances": {
        "removed": [],
        "added": []
      },
      "recommends": {
        "removed": [
          [
            "journal-brief",
            "EQ",
            "0",
            "1.1.3",
            "1.fc24",
            "python3-journal-brief"
          ]
        ],
        "added": [
          [
            "akonadi-mysql",
            "EQ",
            "0",
            "1.13.0",
            "22.fc24",
            "akonadi"
          ],
          [
            "journal-brief",
            "EQ",
            "0",
            "1.1.3",
            "2.fc24",
            "python3-journal-brief"
          ]
        ]
      },
      "suggests": {
        "removed": [
          [
            "python-faker-doc",
            "EQ",
            "0",
            "0.5.3",
            "4.fc24",
            "python3-faker"
          ],
          [
            "python-faker-doc",
            "EQ",
            "0",
            "0.5.3",
            "4.fc24",
            "python2-faker"
          ]
        ],
        "added": [
          [
            "python-faker-doc",
            "EQ",
            "0",
            "0.5.3",
            "5.fc24",
            "python3-faker"
          ],
          [
            "meataxe",
            None,
            None,
            None,
            None,
            "gap-pkg-atlasrep"
          ],
        ]
      },
      "supplements": {
        "removed": [],
        "added": []
      },
      "obsoletes": {
        "removed": [
          [
            "python-simplegeneric",
            "LT",
            "0",
            "0.8.1",
            "1.fc24",
            "python2-simplegeneric"
          ],
          [
            "python-Traits(x86-64)",
            "LT",
            "0",
            "4.5.0",
            "7.gitac5d029.fc24",
            "python2-Traits"
          ],
        ],
        "added": [
          [
            "python-pytools",
            "LT",
            "0",
            "2015.1.2",
            "2.fc24",
            "python3-pytools"
          ],
          [
            "python-aniso8601",
            "LT",
            "0",
            "1.1.0",
            "2.fc24",
            "python2-aniso8601"
          ]
        ]
      },
      "provides": {
        "removed": [
          [
            "django-markdown2",
            "EQ",
            "0",
            "0.2.1",
            "1.fc23",
            "python-django-markdown2"
          ],
          [
            "python3-yui(x86-64)",
            "EQ",
            "0",
            "1.1.0",
            "14.fc24",
            "python3-yui"
          ]
        ],
        "added": [
          [
            "avahi-ui-sharp-devel(x86-64)",
            "EQ",
            "0",
            "0.6.32",
            "0.3.rc.fc24",
            "avahi-ui-sharp-devel"
          ],
          [
            "python2-XStatic-roboto-fontface",
            "EQ",
            "0",
            "0.4.3.2",
            "5.fc24",
            "python2-XStatic-roboto-fontface"
          ]
        ]
      },
      "conflicts": {
        "removed": [
          [
            "vips",
            "GT",
            "0",
            "8.1.1",
            "1.fc24",
            "vips-doc"
          ],
          [
            "python3",
            "LT",
            "0",
            "3.4.3",
            "5.fc24",
            "python3-devel"
          ]
        ],
        "added": [
          [
            "vips",
            "GT",
            "0",
            "8.1.1",
            "2.fc24",
            "vips-doc"
          ]
        ]
      },
      "packages": {
        "removed": [
          [
            "audit-libs-devel",
            "2.4.4",
            "2.fc24",
            "0",
            "i686"
          ],
          [
            "python3-dropbox",
            "3.22",
            "1.fc24",
            "0",
            "noarch"
          ],
          [
            "python-wrapt-doc",
            "1.10.5",
            "1.fc23",
            "0",
            "x86_64"
          ]
        ],
        "added": [
          [
            "tyrus-container-servlet",
            "1.12",
            "3.fc24",
            "0",
            "noarch"
          ],
          [
            "python3-PyQt4-devel",
            "4.11.4",
            "5.fc24",
            "0",
            "i686"
          ]
        ]
      },
      "requires": {
        "removed": [
          [
            "boost(x86-32)",
            "EQ",
            "0",
            "1.59.0",
            "6.fc24",
            "boost-devel"
          ],
          [
            "rpm",
            "EQ",
            "0",
            "4.13.0",
            "0.rc1.11.fc24",
            "rpm-cron"
          ]
        ],
        "added": [
          [
            "PyOpenGL",
            "EQ",
            "0",
            "3.1.0",
            "4.fc24",
            "PyOpenGL-Tk"
          ],
          [
            "libfdisk",
            "EQ",
            "0",
            "2.27.1",
            "2.fc24",
            "libfdisk-devel"
          ]
        ]
      }
    },
    "name": "rawhide"
  }
}


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
