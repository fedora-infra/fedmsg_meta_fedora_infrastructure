# This file is part of fedmsg.
# Copyright (C) 2017 Red Hat, Inc.
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
""" Tests for ci.centos.org messages """

import unittest

from fedmsg.tests.test_meta import Base

from .common import add_doc


class LegacyTestPackageIgnore(Base):
    """ These messages were published when an older version of the CI
    pipeline announced that it ignored a commit made on dist-git.
    """

    expected_title = "ci.pipeline.package.ignore"
    expected_subti = 'Commit "ada94828" of package rpms/protobuf is being '\
        'ignored by the Atomic CI pipeline on branch f26'
    expected_link = "https://ci.centos.org/job/ci-pipeline-2-0/47/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '0a3d99117b8b56a071b50877c98db3dccbae292f188ef1a1c5b77f66d60c57fa'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['fedora-atomic'])
    expected_objects = set(
        ['rpms/protobuf/ada94828daa8fcd0bb68ce13e3ad123545d1c7cc/'
         'f26/package/ignore'])
    msg = {
      "i": 1,
      "timestamp": 1498625602.0,
      "msg_id": "2017-e3ce244c-a1ea-496f-9a6f-2245dd5ea110",
      "topic": "org.centos.prod.ci.pipeline.package.ignore",
      "source_version": "0.7.0",
      "msg": {
        "CI_TYPE": "custom",
        "build_id": "47",
        "username": "fedora-atomic",
        "rev": "ada94828daa8fcd0bb68ce13e3ad123545d1c7cc",
        "message-content": "",
        "build_url": "https://ci.centos.org/job/ci-pipeline-2-0/47/",
        "namespace": "rpms",
        "CI_NAME": "ci-pipeline-2-0",
        "repo": "protobuf",
        "topic": "org.centos.prod.ci.pipeline.package.ignore",
        "status": "success",
        "branch": "f26",
        "test_guidance": "''",
        "ref": "fedora/f26/x86_64/atomic-host"
      }
    }


class LegacyTestPackageComplete(Base):
    """ These messages were published when an older version of the CI
    pipeline announced that the build of a package completed.
    """

    expected_title = "ci.pipeline.package.complete"
    expected_subti = 'Commit 0cc505ca of package rpms/NetworkManager '\
        'passed building in the Atomic CI pipeline on branch f26'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/job/ci-pipeline-f26/8/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '0a3d99117b8b56a071b50877c98db3dccbae292f188ef1a1c5b77f66d60c57fa'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['fedora-atomic'])
    expected_objects = set(
        ['rpms/NetworkManager/0cc505ca294de0daa6260bd80e65e18a318b8057/'
         'f26/package/complete'])
    msg = {
      "i": 1,
      "timestamp": 1500665940.0,
      "msg_id": "2017-3a8e6539-d16d-49da-8a33-ac4c3f75dd27",
      "topic": "org.centos.prod.ci.pipeline.package.complete",
      "source_version": "0.7.0",
      "msg": {
        "CI_TYPE": "custom",
        "build_id": "8",
        "username": "fedora-atomic",
        "rev": "0cc505ca294de0daa6260bd80e65e18a318b8057",
        "message-content": "",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/job/ci-pipeline-f26/8/",
        "namespace": "rpms",
        "CI_NAME": "ci-pipeline-f26",
        "repo": "NetworkManager",
        "topic": "org.centos.stage.ci.pipeline.package.complete",
        "status": "SUCCESS",
        "test_guidance": "''",
        "branch": "f26",
        "package_url": "http://artifacts.ci.centos.org/fedora-atomic/f26/repo/NetworkManager_repo/NetworkManager-1.8.2-2.fc26.673.0cc505c.x86_64.rpm",
        "ref": "fedora/f26/x86_64/atomic-host"
      }
    }


class LegacyTestPackageQueued(Base):
    """ These messages were published when an older version of the CI
    pipeline announced that the build of a package was queued.
    """

    expected_title = "ci.pipeline.package.queued"
    expected_subti = 'Commit 0cc505ca of package rpms/NetworkManager is '\
        'queued to be built in the Atomic CI pipeline on branch f26'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/job/ci-pipeline-trigger/39/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '0a3d99117b8b56a071b50877c98db3dccbae292f188ef1a1c5b77f66d60c57fa'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['fedora-atomic'])
    expected_objects = set(
        ['rpms/NetworkManager/0cc505ca294de0daa6260bd80e65e18a318b8057/'
         'f26/package/queued'])
    msg = {
      "i": 1,
      "timestamp": 1500651841.0,
      "msg_id": "2017-4864d380-a500-4f71-a40e-fe59cc150824",
      "topic": "org.centos.prod.ci.pipeline.package.queued",
      "source_version": "0.7.0",
      "msg": {
        "CI_TYPE": "custom",
        "build_id": "39",
        "username": "fedora-atomic",
        "rev": "0cc505ca294de0daa6260bd80e65e18a318b8057",
        "message-content": "",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/job/ci-pipeline-trigger/39/",
        "namespace": "rpms",
        "CI_NAME": "ci-pipeline-trigger",
        "repo": "NetworkManager",
        "topic": "org.centos.stage.ci.pipeline.package.queued",
        "status": "success",
        "branch": "f26",
        "test_guidance": "''",
        "ref": "fedora/f26/x86_64/atomic-host"
      }
    }


class LegacyTestPackageRunning(Base):
    """ These messages were published when an older version of the CI
    pipeline announced that the build of a package was running.
    """

    expected_title = "ci.pipeline.package.running"
    expected_subti = 'Commit 0cc505ca of package rpms/NetworkManager is '\
        'being built in the Atomic CI pipeline on branch f26'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/job/ci-pipeline-f26/5/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '0a3d99117b8b56a071b50877c98db3dccbae292f188ef1a1c5b77f66d60c57fa'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['fedora-atomic'])
    expected_objects = set(
        ['rpms/NetworkManager/0cc505ca294de0daa6260bd80e65e18a318b8057/'
         'f26/package/running'])
    msg = {
      "i": 1,
      "timestamp": 1500651862.0,
      "msg_id": "2017-66ce76b7-0519-4807-a9b0-831c61b1da6c",
      "topic": "org.centos.stage.ci.pipeline.package.running",
      "source_version": "0.7.0",
      "msg": {
        "CI_TYPE": "custom",
        "build_id": "5",
        "username": "fedora-atomic",
        "rev": "0cc505ca294de0daa6260bd80e65e18a318b8057",
        "message-content": "",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/job/ci-pipeline-f26/5/",
        "namespace": "rpms",
        "CI_NAME": "ci-pipeline-f26",
        "repo": "NetworkManager",
        "topic": "org.centos.stage.ci.pipeline.package.running",
        "status": "SUCCESS",
        "branch": "f26",
        "test_guidance": "''",
        "ref": "fedora/f26/x86_64/atomic-host"
      }
    }


class LegacyTestComposeComplete(Base):
    """ These messages were published when an older version of the CI
    pipeline announced that a compose containing a specified package
    had completed.
    """

    expected_title = "ci.pipeline.compose.complete"
    expected_subti = 'Commit 7327f260 of package rpms/device-mapper-multipath ' \
        'passed a compose in the Atomic CI pipeline on branch master'
    expected_link = "https://ci.centos.org/job/ci-pipeline-ostree-compose/772/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '0a3d99117b8b56a071b50877c98db3dccbae292f188ef1a1c5b77f66d60c57fa'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['fedora-atomic'])
    expected_objects = set(
        ['rpms/device-mapper-multipath/'
         '7327f260a8a90058efd576b8ce12d78e403d269d/'
         'master/compose/complete'])
    msg = {
      "i": 1,
      "timestamp": 1498242025.0,
      "msg_id": "2017-f3a0d6ca-d0d1-4d2c-a578-040cbfc9e2b0",
      "topic": "org.centos.prod.ci.pipeline.compose.complete",
      "source_version": "0.7.0",
      "msg": {
        "CI_TYPE": "custom",
        "build_id": "772",
        "status": "SUCCESS",
        "username": "fedora-atomic",
        "compose_url": "http://artifacts.ci.centos.org/artifacts/fedora-atomic/master/ostree",
        "rev": "7327f260a8a90058efd576b8ce12d78e403d269d",
        "message-content": "",
        "build_url": "https://ci.centos.org/job/ci-pipeline-ostree-compose/772/",
        "namespace": "rpms",
        "CI_NAME": "ci-pipeline-ostree-compose",
        "repo": "device-mapper-multipath",
        "compose_rev": "7a8b6262efe6a4a5194bf48eb4577527fd05c23ff4f2192c276dc98deaa8e718",
        "topic": "org.centos.prod.ci.pipeline.compose.complete",
        "CI_STATUS": "passed",
        "branch": "master",
        "test_guidance": "",
        "ref": "fedora/master/x86_64/atomic-host"
      }
    }


class LegacyTestComposeRunning(Base):
    """ These messages were published when an older version of the CI
    pipeline announced that a compose containing a specified package
    was running.
    """

    expected_title = "ci.pipeline.compose.running"
    expected_subti = 'Commit 7327f260 of package rpms/device-mapper-multipath '\
        'is being part of a compose in the Atomic CI pipeline on branch master'
    expected_link = "https://ci.centos.org/job/ci-pipeline-ostree-compose/772/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '0a3d99117b8b56a071b50877c98db3dccbae292f188ef1a1c5b77f66d60c57fa'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['fedora-atomic'])
    expected_objects = set(
        ['rpms/device-mapper-multipath/'
         '7327f260a8a90058efd576b8ce12d78e403d269d/'
         'master/compose/running'])
    msg = {
      "i": 1,
      "timestamp": 1498241532.0,
      "msg_id": "2017-0b1258d6-dfe6-434c-8754-4af0b83ede64",
      "topic": "org.centos.prod.ci.pipeline.compose.running",
      "source_version": "0.7.0",
      "msg": {
        "CI_TYPE": "custom",
        "build_id": "772",
        "username": "fedora-atomic",
        "compose_url": "http://artifacts.ci.centos.org/artifacts/fedora-atomic/rawhide/ostree",
        "rev": "7327f260a8a90058efd576b8ce12d78e403d269d",
        "message-content": "",
        "build_url": "https://ci.centos.org/job/ci-pipeline-ostree-compose/772/",
        "namespace": "rpms",
        "CI_NAME": "ci-pipeline-ostree-compose",
        "repo": "device-mapper-multipath",
        "compose_rev": "",
        "topic": "org.centos.prod.ci.pipeline.compose.running",
        "status": "success",
        "branch": "master",
        "test_guidance": "",
        "ref": "fedora/rawhide/x86_64/atomic-host"
      }
    }


class LegacyTestComposeTestIntegrationComplete(Base):
    """ These messages were published when an older version of the CI
    pipeline announced that the integration test of a compose
    containing a specified package had completed.
    """

    expected_title = "ci.pipeline.compose.test.integration.complete"
    expected_subti = 'Commit 7b272f5f of package rpms/kernel failed its ' \
        'tests as part of a compose in the Atomic CI pipeline on branch f26'
    expected_link = "https://ci.centos.org/job/ci-pipeline-atomic-host-tests/377/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/' \
        '0a3d99117b8b56a071b50877c98db3dccbae292f188ef1a1c5b77f66d60c57fa' \
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['fedora-atomic'])
    expected_objects = set(
        ['rpms/kernel/'
         '7b272f5f610d89eb9077640c3fc13b6472e4c31d/'
         'f26/compose/test/integration/complete'])
    msg = {
      "i": 1,
      "timestamp": 1498577008.0,
      "msg_id": "2017-2f33b69b-6336-4e67-98fa-fc17d0a004bc",
      "topic": "org.centos.prod.ci.pipeline.compose.test.integration.complete",
      "source_version": "0.7.0",
      "msg": {
        "CI_TYPE": "custom",
        "build_id": "377",
        "username": "fedora-atomic",
        "compose_url": "http://artifacts.ci.centos.org/artifacts/fedora-atomic/f26/ostree",
        "rev": "7b272f5f610d89eb9077640c3fc13b6472e4c31d",
        "message-content": "",
        "build_url": "https://ci.centos.org/job/ci-pipeline-atomic-host-tests/377/",
        "namespace": "rpms",
        "CI_NAME": "ci-pipeline-atomic-host-tests",
        "repo": "kernel",
        "status": "FAILED",
        "topic": "org.centos.prod.ci.pipeline.compose.test.integration.complete",
        "CI_STATUS": "failed",
        "branch": "f26",
        "test_guidance": "",
        "ref": "fedora/f26/x86_64/atomic-host"
      }
    }


class LegacyTestComposeTestIntegrationRunning(Base):
    """ These messages are published when an older version of the CI
    pipeline announced that the integration test of a compose
    containing a specified package was running.
    """

    expected_title = "ci.pipeline.compose.test.integration.running"
    expected_subti = 'Commit 7b272f5f of package rpms/kernel is being '\
        'tested as part of a compose in the Atomic CI pipeline on branch f26'
    expected_link = "https://ci.centos.org/job/ci-pipeline-atomic-host-tests/377/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '0a3d99117b8b56a071b50877c98db3dccbae292f188ef1a1c5b77f66d60c57fa'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['fedora-atomic'])
    expected_objects = set(
        ['rpms/kernel/'
         '7b272f5f610d89eb9077640c3fc13b6472e4c31d/'
         'f26/compose/test/integration/running'])
    msg = {
      "i": 1,
      "timestamp": 1498575078.0,
      "msg_id": "2017-cb05d8b5-24d5-4ac0-9424-a21af20ae15c",
      "topic": "org.centos.prod.ci.pipeline.compose.test.integration.running",
      "source_version": "0.7.0",
      "msg": {
        "CI_TYPE": "custom",
        "build_id": "377",
        "username": "fedora-atomic",
        "compose_url": "http://artifacts.ci.centos.org/artifacts/fedora-atomic/f26/ostree",
        "rev": "7b272f5f610d89eb9077640c3fc13b6472e4c31d",
        "message-content": "",
        "build_url": "https://ci.centos.org/job/ci-pipeline-atomic-host-tests/377/",
        "namespace": "rpms",
        "CI_NAME": "ci-pipeline-atomic-host-tests",
        "repo": "kernel",
        "topic": "org.centos.prod.ci.pipeline.compose.test.integration.running",
        "status": "success",
        "branch": "f26",
        "test_guidance": "",
        "ref": "fedora/f26/x86_64/atomic-host"
      }
    }


class LegacyTestComposeTestIntegrationQueued(Base):
    """ These messages are published when an older version of the CI
    pipeline announced that  the integration test of a compose
    containing a specified package was queued.
    """

    expected_title = "ci.pipeline.compose.test.integration.queued"
    expected_subti = 'Commit 77d0810c of package rpms/grub2 is queued for ' \
        'tests as part of a compose in the Atomic CI pipeline on branch f26'
    expected_link = "https://ci.centos.org/job/ci-pipeline-ostree-boot-sanity/537/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '0a3d99117b8b56a071b50877c98db3dccbae292f188ef1a1c5b77f66d60c57fa'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['fedora-atomic'])
    expected_objects = set(
        ['rpms/grub2/'
         '77d0810cf0c2dae524736a0c39decffb95c20f4c/'
         'f26/compose/test/integration/queued'])
    msg = {
      "i": 1,
      "timestamp": 1498512283.0,
      "msg_id": "2017-b8b527ce-c03a-48fa-9ff2-d2ee2be9de6d",
      "topic": "org.centos.prod.ci.pipeline.compose.test.integration.queued",
      "source_version": "0.7.0",
      "msg": {
        "CI_TYPE": "custom",
        "build_id": "537",
        "username": "fedora-atomic",
        "compose_url": "http://artifacts.ci.centos.org/artifacts/fedora-atomic/f26/ostree",
        "rev": "77d0810cf0c2dae524736a0c39decffb95c20f4c",
        "message-content": "",
        "build_url": "https://ci.centos.org/job/ci-pipeline-ostree-boot-sanity/537/",
        "namespace": "rpms",
        "CI_NAME": "ci-pipeline-ostree-boot-sanity",
        "repo": "grub2",
        "topic": "org.centos.prod.ci.pipeline.compose.test.integration.queued",
        "status": "success",
        "branch": "f26",
        "test_guidance": "",
        "ref": "fedora/f26/x86_64/atomic-host"
      }
    }


class LegacyTestImageComplete(Base):
    """ These messages were published when an older version of the CI
    pipeline announced that the build of the image generated from the
    compose containing a specified package had completed.
    """

    expected_title = "ci.pipeline.image.complete"
    expected_subti = 'Commit 77d0810c of package rpms/grub2 failed ' \
        'being built in an image in the Atomic CI pipeline on branch f25'
    expected_link = "https://ci.centos.org/job/ci-pipeline-ostree-image-compose/123/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/' \
        '0a3d99117b8b56a071b50877c98db3dccbae292f188ef1a1c5b77f66d60c57fa' \
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['fedora-atomic'])
    expected_objects = set(
        ['rpms/grub2/'
         '77d0810cf0c2dae524736a0c39decffb95c20f4c/'
         'f25/image/complete'])
    msg = {
      "i": 1,
      "timestamp": 1498220998.0,
      "msg_id": "2017-49a59f79-24fb-487a-ba13-bb0901acdab5",
      "topic": "org.centos.prod.ci.pipeline.image.complete",
      "source_version": "0.7.0",
      "msg": {
        "CI_TYPE": "custom",
        "build_id": "123",
        "status": "FAILED",
        "username": "fedora-atomic",
        "compose_url": "http://artifacts.ci.centos.org/artifacts/fedora-atomic/f25/ostree",
        "rev": "77d0810cf0c2dae524736a0c39decffb95c20f4c",
        "message-content": "",
        "build_url": "https://ci.centos.org/job/ci-pipeline-ostree-image-compose/123/",
        "namespace": "rpms",
        "CI_NAME": "ci-pipeline-ostree-image-compose",
        "image_name": "fedora-atomic-25.71-ce1d81054a2b79a.qcow2",
        "repo": "grub2",
        "compose_rev": "ce1d81054a2b79a99d66ea413fac25ce94734daa4fec387c39ee03d8e0506158",
        "topic": "org.centos.prod.ci.pipeline.image.complete",
        "CI_STATUS": "passed",
        "test_guidance": "",
        "branch": "f25",
        "type": "qcow2",
        "image_url": "http://artifacts.ci.centos.org/artifacts/fedora-atomic/f25/images/fedora-atomic-25.71-ce1d81054a2b79a.qcow2",
        "ref": "fedora/f25/x86_64/atomic-host"
      }
    }


class LegacyTestImageRunning(Base):
    """ These messages were published when an older version of the CI
    pipeline announced that the build of the image generated from the
    compose containing a specified package was running.
    """

    expected_title = "ci.pipeline.image.running"
    expected_subti = 'Commit 0cc505ca of package rpms/NetworkManager is ' \
        'being built in an image in the Atomic CI pipeline on branch f26'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/job/ci-pipeline-f26/11/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '0a3d99117b8b56a071b50877c98db3dccbae292f188ef1a1c5b77f66d60c57fa'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['fedora-atomic'])
    expected_objects = set(
        ['rpms/NetworkManager/'
         '0cc505ca294de0daa6260bd80e65e18a318b8057/'
         'f26/image/running'])
    msg = {
      "i": 1,
      "timestamp": 1500918319.0,
      "msg_id": "2017-b61a647a-8f98-4f2b-afe9-aa5a7f2ea257",
      "topic": "org.centos.stage.ci.pipeline.image.running",
      "source_version": "0.7.0",
      "msg": {
        "CI_TYPE": "custom",
        "build_id": "11",
        "status": "SUCCESS",
        "username": "fedora-atomic",
        "compose_url": "http://artifacts.ci.centos.org/artifacts/fedora-atomic/f26/ostree",
        "rev": "0cc505ca294de0daa6260bd80e65e18a318b8057",
        "message-content": "",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/job/ci-pipeline-f26/11/",
        "namespace": "rpms",
        "CI_NAME": "ci-pipeline-f26",
        "image_name": "''",
        "repo": "NetworkManager",
        "compose_rev": "c6ab48d6bb155131de5f16350903c80494e6eecac52a00d369b8b920ccd6dafd",
        "topic": "org.centos.stage.ci.pipeline.image.running",
        "image_url": "''",
        "branch": "f26",
        "type": "qcow2",
        "test_guidance": "''",
        "ref": "fedora/f26/x86_64/atomic-host"
      }
    }


class LegacyTestImageTestSmokeComplete(Base):
    """ These messages were published when an older version of the CI
    pipeline announced that the image generated from the compose
    containing a specified package had completed its tests.
    """

    expected_title = "ci.pipeline.image.test.smoke.complete"
    expected_subti = 'Commit fff28640 of package rpms/nspr passed its '\
        'tests in an image in the Atomic CI pipeline on branch f26'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/job/ci-pipeline-f26/132/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '0a3d99117b8b56a071b50877c98db3dccbae292f188ef1a1c5b77f66d60c57fa'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['fedora-atomic'])
    expected_objects = set(
        ['rpms/nspr/'
         'fff28640d156c8b5e7302b7736e16442087b6007/'
         'f26/image/test/smoke/complete'])
    msg = {
      "i": 1,
      "timestamp": 1500918319.0,
      "msg_id": "2017-b61a647a-8f98-4f2b-afe9-aa5a7f2ea257",
      "topic": "org.centos.prod.ci.pipeline.image.test.smoke.complete",
      "source_version": "0.7.0",
      "msg": {
        "CI_NAME": "ci-pipeline-f26",
        "CI_TYPE": "custom",
        "branch": "f26",
        "build_id": "132",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/job/ci-pipeline-f26/132/",
        "compose_rev ": "b1777ffee14021a94d0b027fbcd841a15bd7cdeebd97527b742eab4e666dc9ec",
        "compose_url ": "http: //artifacts.ci.centos.org/artifacts/fedora-atomic/f26/ostree",
        "image_name": "fedora-atomic-26.223-b1777ffee14021a.qcow2",
        "image_url ": "http: //artifacts.ci.centos.org/artifacts/fedora-atomic/f26/images/fedora-atomic-26.223-b1777ffee14021a.qcow2 ",
        "message-content ": "",
        "namespace": "rpms",
        "ref ": "fedora/f26/x86_64/atomic-host",
        "repo": "nspr",
        "rev": "fff28640d156c8b5e7302b7736e16442087b6007",
        "status": "SUCCESS",
        "test_guidance": "''",
        "topic": "org.centos.prod.ci.pipeline.image.test.smoke.complete",
        "type ": "qcow2",
        "username": "fedora-atomic"
      }
    }


class LegacyTestImageTestSmokeRunning(Base):
    """ These messages were published when an older version of the CI
    pipeline announced that the image generated from the compose
    containing a specified package had completed its tests.
    """

    expected_title = "ci.pipeline.image.test.smoke.running"
    expected_subti = 'Commit fff28640 of package rpms/nspr is ' \
        'being tested in an image in the Atomic CI pipeline on branch f26'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/job/ci-pipeline-f26/132/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '0a3d99117b8b56a071b50877c98db3dccbae292f188ef1a1c5b77f66d60c57fa'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['fedora-atomic'])
    expected_objects = set(
        ['rpms/nspr/'
         'fff28640d156c8b5e7302b7736e16442087b6007/'
         'f26/image/test/smoke/running'])
    msg = {
      "i": 1,
      "timestamp": 1500918319.0,
      "msg_id": "2017-b61a647a-8f98-4f2b-afe9-aa5a7f2ea257",
      "topic": "org.centos.prod.ci.pipeline.image.test.smoke.running",
      "source_version": "0.7.0",
      "msg": {
        "CI_NAME": "ci-pipeline-f26",
        "CI_TYPE": "custom",
        "branch": "f26",
        "build_id": "132",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/job/ci-pipeline-f26/132/",
        "compose_rev": "b1777ffee14021a94d0b027fbcd841a15bd7cdeebd97527b742eab4e666dc9ec",
        "compose_url": "http://artifacts.ci.centos.org/artifacts/fedora-atomic/f26/ostree",
        "image_name": "fedora-atomic-26.223-b1777ffee14021a.qcow2",
        "image_url": "http://artifacts.ci.centos.org/artifacts/fedora-atomic/f26/images/fedora-atomic-26.223-b1777ffee14021a.qcow2",
        "message-content": "",
        "namespace": "rpms",
        "ref": "fedora/f26/x86_64/atomic-host",
        "repo": "nspr",
        "rev": "fff28640d156c8b5e7302b7736e16442087b6007",
        "status": "SUCCESS",
        "test_guidance": "''",
        "topic": "org.centos.prod.ci.pipeline.image.test.smoke.running",
        "type": "qcow2",
        "username": "fedora-atomic"
      }
    }


# The coming three tests are based on the documented expected format not
# on real messages, fingers crossed
# https://github.com/CentOS-PaaS-SIG/ci-pipeline/#orgcentosprodcipipelinepackagetestfunctionalqueued

class LegacyTestPackageTestFunctionalQueued(Base):
    """ These messages were published when an older version of the CI
    pipeline announced queueing the functional tests of a package.
    """

    expected_title = "ci.pipeline.package.test.functional.queued"
    expected_subti = 'Commit 591b0d2f of package rpms/vim is queued for '\
        'functional testing in the Atomic CI pipeline on branch f26'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/job/ci-pipeline-f26/91/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '0a3d99117b8b56a071b50877c98db3dccbae292f188ef1a1c5b77f66d60c57fa'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['fedora-atomic'])
    expected_objects = set(
        ['rpms/vim/'
         '591b0d2fc67a45e4ad13bdc3e312d5554852426a/'
         'f26/package/test/functional/queued'])
    msg = {
      "i": 1,
      "timestamp": 1501741048,
      "msg_id": "2017-b420134c-0e39-4f70-8e5f-0975d7019e4b",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.package.test.functional.queued",
      "msg": {
        "CI_TYPE": "custom",
        "build_id": "91",
        "username": "fedora-atomic",
        "rev": "591b0d2fc67a45e4ad13bdc3e312d5554852426a",
        "message-content": "",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/job/ci-pipeline-f26/91/",
        "namespace": "rpms",
        "CI_NAME": "ci-pipeline-f26",
        "repo": "vim",
        "topic": "org.centos.prod.ci.pipeline.package.test.functional.queued",
        "status": "SUCCESS",
        "test_guidance": "''",
        "branch": "f26",
        "package_url": "http://artifacts.ci.centos.org/fedora-atomic/f26/repo/vim_repo/",
        "ref": "fedora/f26/x86_64/atomic-host"
      }
    }


class LegacyTestPackageTestFunctionalRunning(Base):
    """ These messages were published when an older version of the CI
    pipeline announced running the functional tests of a package.
    """

    expected_title = "ci.pipeline.package.test.functional.running"
    expected_subti = 'Commit 591b0d2f of package rpms/vim is running its '\
        'functional tests in the Atomic CI pipeline on branch f26'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/job/ci-pipeline-f26/91/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '0a3d99117b8b56a071b50877c98db3dccbae292f188ef1a1c5b77f66d60c57fa'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['fedora-atomic'])
    expected_objects = set(
        ['rpms/vim/'
         '591b0d2fc67a45e4ad13bdc3e312d5554852426a/'
         'f26/package/test/functional/running'])
    msg = {
      "i": 1,
      "timestamp": 1501741048,
      "msg_id": "2017-b420134c-0e39-4f70-8e5f-0975d7019e4b",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.package.test.functional.running",
      "msg": {
        "CI_TYPE": "custom",
        "build_id": "91",
        "username": "fedora-atomic",
        "rev": "591b0d2fc67a45e4ad13bdc3e312d5554852426a",
        "message-content": "",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/job/ci-pipeline-f26/91/",
        "namespace": "rpms",
        "CI_NAME": "ci-pipeline-f26",
        "repo": "vim",
        "topic": "org.centos.prod.ci.pipeline.package.test.functional.queued",
        "status": "SUCCESS",
        "test_guidance": "''",
        "branch": "f26",
        "package_url": "http://artifacts.ci.centos.org/fedora-atomic/f26/repo/vim_repo/",
        "ref": "fedora/f26/x86_64/atomic-host"
      }
    }


class LegacyTestPackageTestFunctionalComplete(Base):
    """ These messages were published when an older version of the CI
    pipeline announced having completed the functional tests of a
    package.
    """

    expected_title = "ci.pipeline.package.test.functional.complete"
    expected_subti = 'Commit 591b0d2f of package rpms/vim passed its '\
        'functional tests in the Atomic CI pipeline on branch f26'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/job/ci-pipeline-f26/91/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '0a3d99117b8b56a071b50877c98db3dccbae292f188ef1a1c5b77f66d60c57fa'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['fedora-atomic'])
    expected_objects = set(
        ['rpms/vim/'
         '591b0d2fc67a45e4ad13bdc3e312d5554852426a/'
         'f26/package/test/functional/complete'])
    msg = {
      "i": 1,
      "timestamp": 1501741048,
      "msg_id": "2017-b420134c-0e39-4f70-8e5f-0975d7019e4b",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.package.test.functional.complete",
      "msg": {
        "CI_TYPE": "custom",
        "build_id": "91",
        "username": "fedora-atomic",
        "rev": "591b0d2fc67a45e4ad13bdc3e312d5554852426a",
        "message-content": "",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/job/ci-pipeline-f26/91/",
        "namespace": "rpms",
        "CI_NAME": "ci-pipeline-f26",
        "repo": "vim",
        "topic": "org.centos.prod.ci.pipeline.package.test.functional.queued",
        "status": "SUCCESS",
        "test_guidance": "''",
        "branch": "f26",
        "package_url": "http://artifacts.ci.centos.org/fedora-atomic/f26/repo/vim_repo/",
        "ref": "fedora/f26/x86_64/atomic-host"
      }
    }


class LegacyTestCompleteSuccess(Base):
    """ These messages were published when an older version of the CI
    pipeline announced having completed running the entire pipeline
    on a package.
    """

    expected_title = "ci.pipeline.complete"
    expected_subti = 'Commit "591b0d2f" of package rpms/vim passed the Atomic CI pipeline on branch f26'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/job/ci-pipeline-f26/91/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '0a3d99117b8b56a071b50877c98db3dccbae292f188ef1a1c5b77f66d60c57fa'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['fedora-atomic'])
    expected_objects = set(
        ['rpms/vim/'
         '591b0d2fc67a45e4ad13bdc3e312d5554852426a/'
         'f26/complete'])
    msg = {
      "i": 1,
      "timestamp": 1501741048,
      "msg_id": "2017-b420134c-0e39-4f70-8e5f-0975d7019e4b",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.complete",
      "msg": {
        "CI_TYPE": "custom",
        "build_id": "91",
        "username": "fedora-atomic",
        "rev": "591b0d2fc67a45e4ad13bdc3e312d5554852426a",
        "message-content": "",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/job/ci-pipeline-f26/91/",
        "namespace": "rpms",
        "CI_NAME": "ci-pipeline-f26",
        "repo": "vim",
        "topic": "org.centos.prod.ci.pipeline.complete",
        "status": "SUCCESS",
        "test_guidance": "''",
        "branch": "f26",
        "package_url": "http://artifacts.ci.centos.org/fedora-atomic/f26/repo/vim_repo/",
        "ref": "fedora/f26/x86_64/atomic-host"
      }
    }


class LegacyTestCompleteAborted(Base):
    """ These messages were published when an older version of the CI
    pipeline announced having aborted a run of the pipeline on a
    package.
    """

    expected_title = "ci.pipeline.complete"
    expected_subti = 'Commit "591b0d2f" of package rpms/vim was aborted on the Atomic CI pipeline on branch f26'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/job/ci-pipeline-f26/91/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '0a3d99117b8b56a071b50877c98db3dccbae292f188ef1a1c5b77f66d60c57fa'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['fedora-atomic'])
    expected_objects = set(
        ['rpms/vim/'
         '591b0d2fc67a45e4ad13bdc3e312d5554852426a/'
         'f26/complete'])
    msg = {
      "i": 1,
      "timestamp": 1501741048,
      "msg_id": "2017-b420134c-0e39-4f70-8e5f-0975d7019e4b",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.complete",
      "msg": {
        "CI_TYPE": "custom",
        "build_id": "91",
        "username": "fedora-atomic",
        "rev": "591b0d2fc67a45e4ad13bdc3e312d5554852426a",
        "message-content": "",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/job/ci-pipeline-f26/91/",
        "namespace": "rpms",
        "CI_NAME": "ci-pipeline-f26",
        "repo": "vim",
        "topic": "org.centos.prod.ci.pipeline.complete",
        "status": "ABORTED",
        "test_guidance": "''",
        "branch": "f26",
        "package_url": "http://artifacts.ci.centos.org/fedora-atomic/f26/repo/vim_repo/",
        "ref": "fedora/f26/x86_64/atomic-host"
      }
    }


class LegacyTestCompleteFailed(Base):
    """ These messages were published when an older version of the CI
    pipeline announced having failed a run of the pipeline on a package.

    This meant the pipeline failed to run the tests (as opposed to run the
    tests but these failed).
    """

    expected_title = "ci.pipeline.complete"
    expected_subti = 'Commit "591b0d2f" of package rpms/vim failed the Atomic CI pipeline on branch f26'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/job/ci-pipeline-f26/91/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '0a3d99117b8b56a071b50877c98db3dccbae292f188ef1a1c5b77f66d60c57fa'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['fedora-atomic'])
    expected_objects = set(
        ['rpms/vim/'
         '591b0d2fc67a45e4ad13bdc3e312d5554852426a/'
         'f26/complete'])
    msg = {
      "i": 1,
      "timestamp": 1501741048,
      "msg_id": "2017-b420134c-0e39-4f70-8e5f-0975d7019e4b",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.complete",
      "msg": {
        "CI_TYPE": "custom",
        "build_id": "91",
        "username": "fedora-atomic",
        "rev": "591b0d2fc67a45e4ad13bdc3e312d5554852426a",
        "message-content": "",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/job/ci-pipeline-f26/91/",
        "namespace": "rpms",
        "CI_NAME": "ci-pipeline-f26",
        "repo": "vim",
        "topic": "org.centos.prod.ci.pipeline.complete",
        "status": "FAILEd",
        "test_guidance": "''",
        "branch": "f26",
        "package_url": "http://artifacts.ci.centos.org/fedora-atomic/f26/repo/vim_repo/",
        "ref": "fedora/f26/x86_64/atomic-host"
      }
    }


class LegacyTestCompleteError(Base):
    """ These messages were published when an older version of the CI
    pipeline announced having errored a run of the pipeline on a
    package.

    This meant the pipeline could run the tests but the tests
    themselves failed (as opposed to the pipeline failed to run the
    tests).
    """

    expected_title = "ci.pipeline.complete"
    expected_subti = 'Commit "591b0d2f" of package rpms/vim errored the Atomic CI pipeline on branch f26'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/job/ci-pipeline-f26/91/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '0a3d99117b8b56a071b50877c98db3dccbae292f188ef1a1c5b77f66d60c57fa'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['fedora-atomic'])
    expected_objects = set(
        ['rpms/vim/'
         '591b0d2fc67a45e4ad13bdc3e312d5554852426a/'
         'f26/complete'])
    msg = {
      "i": 1,
      "timestamp": 1501741048,
      "msg_id": "2017-b420134c-0e39-4f70-8e5f-0975d7019e4b",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.complete",
      "msg": {
        "CI_TYPE": "custom",
        "build_id": "91",
        "username": "fedora-atomic",
        "rev": "591b0d2fc67a45e4ad13bdc3e312d5554852426a",
        "message-content": "",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/job/ci-pipeline-f26/91/",
        "namespace": "rpms",
        "CI_NAME": "ci-pipeline-f26",
        "repo": "vim",
        "topic": "org.centos.prod.ci.pipeline.complete",
        "status": "UNSTABLE",
        "test_guidance": "''",
        "branch": "f26",
        "package_url": "http://artifacts.ci.centos.org/fedora-atomic/f26/repo/vim_repo/",
        "ref": "fedora/f26/x86_64/atomic-host"
      }
    }


class Legacy1TestAllPackagesPackageRunning(Base):
    """ These messages were published on the old topic when the All
    Packages CI pipeline (from before the split between 'build' and
    'pr' pipelines) announced that the build of a package was running.
    """

    expected_title = "allpackages.pipeline.package.running"
    expected_subti = 'Commit 35cdcb6a of package rpms/gdb is '\
        'being built in the All Packages CI pipeline on branch f28'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/" \
        "blue/organizations/jenkins/upstream-fedora-f28-pipeline/detail/" \
        "upstream-fedora-f28-pipeline/335/pipeline/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '4a5e1bf0da6d9dfba3e0dc300fe58f6fc7d064df703eafbf2502dd900f69c1b4'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['jankratochvil'])
    expected_objects = set(
        ['rpms/gdb/35cdcb6a32562b632c075f2fd42793f7492dcdb3/'
         'f28/package/running'])
    msg = {
      "username": None,
      "source_name": "datanommer",
      "i": 1,
      "timestamp": 1522054091.0,
      "msg_id": "2018-cfb9a40e-3220-4dcf-a5aa-270a6cee975c",
      "crypto": "x509",
      "topic": "org.centos.prod.allpackages.pipeline.package.running",
      "headers": {},
      "source_version": "0.8.2",
      "msg": {
        "CI_TYPE": "custom",
        "build_id": "335",
        "original_spec_nvr": "",
        "username": "jankratochvil",
        "nvr": "",
        "rev": "35cdcb6a32562b632c075f2fd42793f7492dcdb3",
        "message-content": "",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/blue/organizations/jenkins/upstream-fedora-f28-pipeline/detail/upstream-fedora-f28-pipeline/335/pipeline/",
        "namespace": "rpms",
        "CI_NAME": "upstream-fedora-f28-pipeline",
        "repo": "gdb",
        "topic": "org.centos.prod.allpackages.pipeline.package.running",
        "status": "SUCCESS",
        "branch": "f28",
        "test_guidance": "''",
        "ref": "x86_64"
      }
    }


class Legacy1TestAllPackagesCompleteSuccess(Base):
    """ These messages were published on the old topic when the All
    Packages CI pipeline (from before the split between 'build' and
    'pr' pipelines) announced having completed successfully running
    the entire pipeline on a package.
    """

    expected_title = "allpackages.pipeline.complete"
    expected_subti = 'Commit "35cdcb6a" of package rpms/gdb passed the ' \
        'All Packages CI pipeline on branch f28'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/" \
        "blue/organizations/jenkins/upstream-fedora-f28-pipeline/detail/" \
        "upstream-fedora-f28-pipeline/335/pipeline/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '4a5e1bf0da6d9dfba3e0dc300fe58f6fc7d064df703eafbf2502dd900f69c1b4'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['jankratochvil'])
    expected_objects = set(
        ['rpms/gdb/'
         '35cdcb6a32562b632c075f2fd42793f7492dcdb3/'
         'f28/complete'])
    msg = {
      "username": None,
      "source_name": "datanommer",
      "i": 1,
      "timestamp": 1522055492.0,
      "msg_id": "2018-1436f172-aa90-49f2-9ff0-9b34608f38e8",
      "crypto": "x509",
      "topic": "org.centos.prod.allpackages.pipeline.complete",
      "headers": {},
      "source_version": "0.8.2",
      "msg": {
        "CI_TYPE": "custom",
        "build_id": "335",
        "original_spec_nvr": "",
        "username": "jankratochvil",
        "nvr": "",
        "rev": "35cdcb6a32562b632c075f2fd42793f7492dcdb3",
        "message-content": "",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/blue/organizations/jenkins/upstream-fedora-f28-pipeline/detail/upstream-fedora-f28-pipeline/335/pipeline/",
        "namespace": "rpms",
        "CI_NAME": "upstream-fedora-f28-pipeline",
        "repo": "gdb",
        "topic": "org.centos.prod.allpackages.pipeline.complete",
        "status": "SUCCESS",
        "branch": "f28",
        "test_guidance": "''",
        "ref": "x86_64"
      }
    }


class Legacy2TestAllPackagesPackageRunning(Base):
    """ These messages were published when the All Packages CI pipeline
    (from before the split between 'build' and 'pr' pipelines)
    announced that the build of a package was running.
    """

    expected_title = "ci.pipeline.allpackages.package.running"
    expected_subti = 'Commit 35cdcb6a of package rpms/gdb is '\
        'being built in the All Packages CI pipeline on branch f28'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/" \
        "blue/organizations/jenkins/upstream-fedora-f28-pipeline/detail/" \
        "upstream-fedora-f28-pipeline/335/pipeline/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '4a5e1bf0da6d9dfba3e0dc300fe58f6fc7d064df703eafbf2502dd900f69c1b4'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['jankratochvil'])
    expected_objects = set(
        ['rpms/gdb/35cdcb6a32562b632c075f2fd42793f7492dcdb3/'
         'f28/allpackages/package/running'])
    msg = {
      "username": None,
      "source_name": "datanommer",
      "i": 1,
      "timestamp": 1522054091.0,
      "msg_id": "2018-cfb9a40e-3220-4dcf-a5aa-270a6cee975c",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.allpackages.package.running",
      "headers": {},
      "source_version": "0.8.2",
      "msg": {
        "CI_TYPE": "custom",
        "build_id": "335",
        "original_spec_nvr": "",
        "username": "jankratochvil",
        "nvr": "",
        "rev": "35cdcb6a32562b632c075f2fd42793f7492dcdb3",
        "message-content": "",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/blue/organizations/jenkins/upstream-fedora-f28-pipeline/detail/upstream-fedora-f28-pipeline/335/pipeline/",
        "namespace": "rpms",
        "CI_NAME": "upstream-fedora-f28-pipeline",
        "repo": "gdb",
        "topic": "org.centos.prod.ci.pipeline.allpackages.package.running",
        "status": "SUCCESS",
        "branch": "f28",
        "test_guidance": "''",
        "ref": "x86_64"
      }
    }


class Legacy2TestAllPackagesCompleteSuccess(Base):
    """ These messages were published when the All Packages CI pipeline
    (from before the split between 'build' and 'pr' pipelines)
    announced having completed successfully running the entire pipeline
    on a package.
    """

    expected_title = "ci.pipeline.allpackages.complete"
    expected_subti = 'Commit "35cdcb6a" of package rpms/gdb passed the ' \
        'All Packages CI pipeline on branch f28'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/" \
        "blue/organizations/jenkins/upstream-fedora-f28-pipeline/detail/" \
        "upstream-fedora-f28-pipeline/335/pipeline/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '4a5e1bf0da6d9dfba3e0dc300fe58f6fc7d064df703eafbf2502dd900f69c1b4'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['jankratochvil'])
    expected_objects = set(
        ['rpms/gdb/'
         '35cdcb6a32562b632c075f2fd42793f7492dcdb3/'
         'f28/allpackages/complete'])
    msg = {
      "username": None,
      "source_name": "datanommer",
      "i": 1,
      "timestamp": 1522055492.0,
      "msg_id": "2018-1436f172-aa90-49f2-9ff0-9b34608f38e8",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.allpackages.complete",
      "headers": {},
      "source_version": "0.8.2",
      "msg": {
        "CI_TYPE": "custom",
        "build_id": "335",
        "original_spec_nvr": "",
        "username": "jankratochvil",
        "nvr": "",
        "rev": "35cdcb6a32562b632c075f2fd42793f7492dcdb3",
        "message-content": "",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/blue/organizations/jenkins/upstream-fedora-f28-pipeline/detail/upstream-fedora-f28-pipeline/335/pipeline/",
        "namespace": "rpms",
        "CI_NAME": "upstream-fedora-f28-pipeline",
        "repo": "gdb",
        "topic": "org.centos.prod.ci.pipeline.allpackages.complete",
        "status": "SUCCESS",
        "branch": "f28",
        "test_guidance": "''",
        "ref": "x86_64"
      }
    }


class TestAllPackagesBuildPackageIgnored(Base):
    """ These messages are published when the Allpackages (build) CI
    pipeline announces that the build of a package has been ignored.
    """

    expected_title = "ci.pipeline.allpackages-build.package.ignored"
    expected_subti = 'Koji task "34128170" of package unknown_namespace/pytest is '\
        'being ignored by the All Packages (Build) CI pipeline on branch master'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/" \
        "blue/organizations/jenkins/fedora-task-pipeline-trigger/detail/" \
        "fedora-task-pipeline-trigger/5742/pipeline/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '4a5e1bf0da6d9dfba3e0dc300fe58f6fc7d064df703eafbf2502dd900f69c1b4'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['jankratochvil'])
    expected_objects = set(
        ['unknown_namespace/pytest/kojitask-34128170/master/allpackages-build/package/ignored'])
    msg = {
      "username": None,
      "source_name": "datanommer",
      "i": 0,
      "timestamp": 1555083483.0,
      "msg_id": "2019-607fbb14-eb51-4423-a0a1-d7df3f0fdc04",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.allpackages-build.package.ignored",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "build_id": "5742",
        "status": "SUCCESS",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/blue/organizations/jenkins/fedora-task-pipeline-trigger/detail/fedora-task-pipeline-trigger/5742/pipeline/",
        "nvr": "",
        "rev": "kojitask-34128170",
        "ci_topic": "org.centos.prod.ci.pipeline.allpackages-build.package.ignored",
        "username": "jankratochvil",
        "comment_id": None,
        "namespace": None,
        "repo": "pytest",
        "original_spec_nvr": "",
        "test_guidance": "''",
        "branch": "master",
        "scratch": True,
        "ref": "x86_64"
      }
    }


class TestAllPackagesPRPackageIgnored(Base):
    """ These messages are published when the Allpackages (PR) CI
    pipeline announces that a pull request for a package has been
    ignored.
    """

    expected_title = "ci.pipeline.allpackages-pr.package.ignored"
    expected_subti = 'Pull request "1" of package rpms/toolbox is '\
        'being ignored by the All Packages (PR) CI pipeline on branch master'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/" \
        "blue/organizations/jenkins/fedora-pr-comment-trigger/detail/" \
        "fedora-pr-comment-trigger/2854/pipeline/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = None
    expected_packages = set([])
    expected_usernames = set()
    expected_objects = set(
        ['rpms/toolbox/PR-1/master/allpackages-pr/package/ignored'])
    msg = {
      "username": None,
      "source_name": "datanommer",
      "i": 0,
      "timestamp": 1555083162.0,
      "msg_id": "2019-c944485a-c647-4dec-82aa-b8b83c0e8553",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.allpackages-pr.package.ignored",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "build_id": "2854",
        "status": "SUCCESS",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/blue/organizations/jenkins/fedora-pr-comment-trigger/detail/fedora-pr-comment-trigger/2854/pipeline/",
        "nvr": "",
        "rev": "PR-1",
        "ci_topic": "org.centos.prod.ci.pipeline.allpackages-pr.package.ignored",
        "username": None,
        "comment_id": "23810",
        "namespace": "rpms",
        "repo": "toolbox",
        "original_spec_nvr": "",
        "test_guidance": "''",
        "branch": "master",
        "scratch": "",
        "ref": "x86_64"
      }
    }


class TestAllPackagesBuildPackageQueued(Base):
    """ These messages are published when the Allpackages (build) CI
    pipeline announces that the build of a package is queued.
    """

    expected_title = "ci.pipeline.allpackages-build.package.queued"
    expected_subti = 'Koji task 34126640 of package unknown_namespace/nmstate is '\
        'queued to be built in the All Packages (Build) CI pipeline on branch f28'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/" \
        "blue/organizations/jenkins/fedora-build-pipeline-trigger/detail/" \
        "fedora-build-pipeline-trigger/264227/pipeline/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '4a5e1bf0da6d9dfba3e0dc300fe58f6fc7d064df703eafbf2502dd900f69c1b4'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['jankratochvil'])
    expected_objects = set(
        ['unknown_namespace/nmstate/kojitask-34126640/f28/allpackages-build/package/queued'])
    msg = {
      "username": None,
      "source_name": "datanommer",
      "i": 0,
      "timestamp": 1555074142.0,
      "msg_id": "2019-8a7b8304-75c3-42b8-b57c-d3fc7b88bc83",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.allpackages-build.package.queued",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "build_id": "264227",
        "status": "SUCCESS",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/blue/organizations/jenkins/fedora-build-pipeline-trigger/detail/fedora-build-pipeline-trigger/264227/pipeline/",
        "nvr": "",
        "rev": "kojitask-34126640",
        "ci_topic": "org.centos.prod.ci.pipeline.allpackages-build.package.queued",
        "username": "jankratochvil",
        "comment_id": None,
        "namespace": None,
        "repo": "nmstate",
        "original_spec_nvr": "",
        "test_guidance": "''",
        "branch": "f28",
        "scratch": False,
        "ref": "x86_64"
      }
    }


class TestAllPackagesBuildPackageFunctionalQueued(Base):
    """ These messages are published when the Allpackages (build) CI
    pipeline announces that the functional testing build of a package
    is queued.
    """

    expected_title = "ci.pipeline.allpackages-build.package.test.functional.queued"
    expected_subti = 'Koji task 34126640 of package rpms/nmstate is queued '\
        'for functional testing in the All Packages (Build) CI pipeline on branch f28'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/" \
        "blue/organizations/jenkins/fedora-f28-build-pipeline/detail/" \
        "fedora-f28-build-pipeline/384/pipeline/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '4a5e1bf0da6d9dfba3e0dc300fe58f6fc7d064df703eafbf2502dd900f69c1b4'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['jankratochvil'])
    expected_objects = set(
        ['rpms/nmstate/kojitask-34126640/f28/allpackages-build/package/test/functional/queued'])
    msg = {
      "username": None,
      "source_name": "datanommer",
      "i": 0,
      "timestamp": 1555074463.0,
      "msg_id": "2019-27d3db55-9f06-4546-9971-cdc44e0c785e",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.allpackages-build.package.test.functional.queued",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "build_id": "384",
        "status": "SUCCESS",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/blue/organizations/jenkins/fedora-f28-build-pipeline/detail/fedora-f28-build-pipeline/384/pipeline/",
        "nvr": "nmstate-0.0.5-2.fc28",
        "rev": "kojitask-34126640",
        "ci_topic": "org.centos.prod.ci.pipeline.allpackages-build.package.test.functional.queued",
        "username": "jankratochvil",
        "comment_id": None,
        "namespace": "rpms",
        "repo": "nmstate",
        "original_spec_nvr": "nmstate-0.0.5-2.fc28",
        "test_guidance": "''",
        "branch": "f28",
        "scratch": False,
        "ref": "x86_64"
      }
    }


class TestAllPackagesBuildImageQueued(Base):
    """ These messages are published when the Allpackages (build) CI
    pipeline announces that the build of an image containing a package
    build is queued.
    """

    expected_title = "ci.pipeline.allpackages-build.image.queued"
    expected_subti = 'Koji task 34126640 of package rpms/nmstate is '\
        'queued to be built in an image in the All Packages (Build) CI pipeline '\
        'on branch f28'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/" \
        "blue/organizations/jenkins/fedora-f28-build-pipeline/detail/" \
        "fedora-f28-build-pipeline/384/pipeline/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '4a5e1bf0da6d9dfba3e0dc300fe58f6fc7d064df703eafbf2502dd900f69c1b4'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['jankratochvil'])
    expected_objects = set(
        ['rpms/nmstate/kojitask-34126640/f28/allpackages-build/image/queued'])
    msg = {
      "username": None,
      "source_name": "datanommer",
      "i": 0,
      "timestamp": 1555074216.0,
      "msg_id": "2019-ea702b9d-bdaf-4684-9306-34ee62c13126",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.allpackages-build.image.queued",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "build_id": "384",
        "status": "SUCCESS",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/blue/organizations/jenkins/fedora-f28-build-pipeline/detail/fedora-f28-build-pipeline/384/pipeline/",
        "type": "qcow2",
        "nvr": "nmstate-0.0.5-2.fc28",
        "rev": "kojitask-34126640",
        "ci_topic": "org.centos.prod.ci.pipeline.allpackages-build.image.queued",
        "username": "jankratochvil",
        "comment_id": None,
        "namespace": "rpms",
        "repo": "nmstate",
        "original_spec_nvr": "nmstate-0.0.5-2.fc28",
        "test_guidance": "''",
        "branch": "f28",
        "scratch": False,
        "ref": "x86_64"
      }
    }


class TestAllPackagesPRPackageQueued(Base):
    """ These messages are published when the Allpackages (PR) CI
    pipeline announces that a pull request for a package is queued.
    """

    expected_title = "ci.pipeline.allpackages-pr.package.queued"
    expected_subti = 'Pull request 19 of package rpms/selinux-policy is '\
        'queued to be built in the All Packages (PR) CI pipeline on branch master'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/" \
        "blue/organizations/jenkins/fedora-pr-new-trigger/detail/" \
        "fedora-pr-new-trigger/13631/pipeline/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = None
    expected_packages = set([])
    expected_usernames = set()
    expected_objects = set(
        ['rpms/selinux-policy/PR-19/master/allpackages-pr/package/queued'])
    msg = {
      "username": None,
      "source_name": "datanommer",
      "i": 0,
      "timestamp": 1555083159.0,
      "msg_id": "2019-e65e8421-390d-4f19-b114-78e6584bcbe3",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.allpackages-pr.package.queued",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "build_id": "13631",
        "status": "SUCCESS",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/blue/organizations/jenkins/fedora-pr-new-trigger/detail/fedora-pr-new-trigger/13631/pipeline/",
        "nvr": "",
        "rev": "PR-19",
        "ci_topic": "org.centos.prod.ci.pipeline.allpackages-pr.package.queued",
        "username": None,
        "comment_id": None,
        "namespace": "rpms",
        "repo": "selinux-policy",
        "original_spec_nvr": "",
        "test_guidance": "''",
        "branch": "master",
        "scratch": "",
        "ref": "x86_64"
      }
    }


class TestAllPackagesPRPackageFunctionalQueued(Base):
    """ These messages are published when the Allpackages (PR) CI
    pipeline announces that the functional testing build of a pull
    request for a package is queued.
    """

    expected_title = "ci.pipeline.allpackages-pr.package.test.functional.queued"
    expected_subti = 'Pull request 105 of package rpms/python3 is queued '\
        'for functional testing in the All Packages (PR) CI pipeline on branch master'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/" \
        "blue/organizations/jenkins/fedora-rawhide-pr-pipeline/detail/" \
        "fedora-rawhide-pr-pipeline/1167/pipeline/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = None
    expected_packages = set([])
    expected_usernames = set()
    expected_objects = set(
        ['rpms/python3/PR-105/master/allpackages-pr/package/test/functional/queued'])
    msg = {
      "username": None,
      "source_name": "datanommer",
      "i": 0,
      "timestamp": 1555060917.0,
      "msg_id": "2019-dba7d16a-510e-41f5-9c70-42aa42d92429",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.allpackages-pr.package.test.functional.queued",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "build_id": "1167",
        "status": "SUCCESS",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/blue/organizations/jenkins/fedora-rawhide-pr-pipeline/detail/fedora-rawhide-pr-pipeline/1167/pipeline/",
        "nvr": "python3-3.7.3-2.fc31.pr.4229607131614fc0a723aa38ea21b892",
        "rev": "PR-105",
        "ci_topic": "org.centos.prod.ci.pipeline.allpackages-pr.package.test.functional.queued",
        "username": None,
        "comment_id": None,
        "namespace": "rpms",
        "repo": "python3",
        "original_spec_nvr": "python3-3.7.3-2.fc31",
        "test_guidance": "''",
        "branch": "master",
        "scratch": True,
        "ref": "x86_64"
      }
    }


class TestAllPackagesPRImageQueued(Base):
    """ These messages are published when the Allpackages (PR) CI
    pipeline announces that the build of an image containing a pull
    request for a package is queued.
    """

    expected_title = "ci.pipeline.allpackages-pr.image.queued"
    expected_subti = 'Pull request 105 of package rpms/python3 is '\
        'queued to be built in an image in the All Packages (PR) CI pipeline '\
        'on branch master'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/" \
        "blue/organizations/jenkins/fedora-rawhide-pr-pipeline/detail/" \
        "fedora-rawhide-pr-pipeline/1167/pipeline/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = None
    expected_packages = set([])
    expected_usernames = set()
    expected_objects = set(
        ['rpms/python3/PR-105/master/allpackages-pr/image/queued'])
    msg = {
      "username": None,
      "source_name": "datanommer",
      "i": 0,
      "timestamp": 1555060689.0,
      "msg_id": "2019-420f348a-f62d-4e7c-b57c-1ddeb320c03c",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.allpackages-pr.image.queued",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "build_id": "1167",
        "status": "SUCCESS",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/blue/organizations/jenkins/fedora-rawhide-pr-pipeline/detail/fedora-rawhide-pr-pipeline/1167/pipeline/",
        "type": "qcow2",
        "nvr": "python3-3.7.3-2.fc31.pr.4229607131614fc0a723aa38ea21b892",
        "rev": "PR-105",
        "ci_topic": "org.centos.prod.ci.pipeline.allpackages-pr.image.queued",
        "username": None,
        "comment_id": None,
        "namespace": "rpms",
        "repo": "python3",
        "original_spec_nvr": "python3-3.7.3-2.fc31",
        "test_guidance": "''",
        "branch": "master",
        "scratch": True,
        "ref": "x86_64"
      }
    }


class TestAllPackagesBuildPackageRunning(Base):
    """ These messages are published when the Allpackages (build) CI
    pipeline announces that the build of a package is running.
    """

    expected_title = "ci.pipeline.allpackages-build.package.running"
    expected_subti = 'Koji task 34126640 of package rpms/nmstate is '\
        'being built in the All Packages (Build) CI pipeline on branch f28'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/" \
        "blue/organizations/jenkins/fedora-f28-build-pipeline/detail/" \
        "fedora-f28-build-pipeline/384/pipeline/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '4a5e1bf0da6d9dfba3e0dc300fe58f6fc7d064df703eafbf2502dd900f69c1b4'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['jankratochvil'])
    expected_objects = set(
        ['rpms/nmstate/kojitask-34126640/f28/allpackages-build/package/running'])
    msg = {
      "username": None,
      "source_name": "datanommer",
      "i": 0,
      "timestamp": 1555074192.0,
      "msg_id": "2019-d5d09d7f-29a1-49f8-bb79-5107df7838fd",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.allpackages-build.package.running",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "build_id": "384",
        "status": "SUCCESS",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/blue/organizations/jenkins/fedora-f28-build-pipeline/detail/fedora-f28-build-pipeline/384/pipeline/",
        "nvr": "",
        "rev": "kojitask-34126640",
        "ci_topic": "org.centos.prod.ci.pipeline.allpackages-build.package.running",
        "username": "jankratochvil",
        "comment_id": None,
        "namespace": "rpms",
        "repo": "nmstate",
        "original_spec_nvr": "",
        "test_guidance": "''",
        "branch": "f28",
        "scratch": False,
        "ref": "x86_64"
      }
    }


class TestAllPackagesBuildPackageFunctionalRunning(Base):
    """ These messages are published when the Allpackages (build) CI
    pipeline announces that the functional testing build of a package
    is running.
    """

    expected_title = "ci.pipeline.allpackages-build.package.test.functional.running"
    expected_subti = 'Koji task 34126640 of package rpms/nmstate is running its '\
        'functional tests in the All Packages (Build) CI pipeline on branch f28'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/" \
        "blue/organizations/jenkins/fedora-f28-build-pipeline/detail/" \
        "fedora-f28-build-pipeline/384/pipeline/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '4a5e1bf0da6d9dfba3e0dc300fe58f6fc7d064df703eafbf2502dd900f69c1b4'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['jankratochvil'])
    expected_objects = set(
        ['rpms/nmstate/kojitask-34126640/f28/allpackages-build/package/test/functional/running'])
    msg = {
      "username": None,
      "source_name": "datanommer",
      "i": 0,
      "timestamp": 1555074470.0,
      "msg_id": "2019-72d436cb-c5e3-439a-87ce-4b1f6a162957",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.allpackages-build.package.test.functional.running",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "build_id": "384",
        "status": "SUCCESS",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/blue/organizations/jenkins/fedora-f28-build-pipeline/detail/fedora-f28-build-pipeline/384/pipeline/",
        "nvr": "nmstate-0.0.5-2.fc28",
        "rev": "kojitask-34126640",
        "ci_topic": "org.centos.prod.ci.pipeline.allpackages-build.package.test.functional.running",
        "username": "jankratochvil",
        "comment_id": None,
        "namespace": "rpms",
        "repo": "nmstate",
        "original_spec_nvr": "nmstate-0.0.5-2.fc28",
        "test_guidance": "''",
        "branch": "f28",
        "scratch": False,
        "ref": "x86_64"
      }
    }


class TestAllPackagesBuildImageRunning(Base):
    """ These messages are published when the Allpackages (build) CI
    pipeline announces that the build of an image containing a package
    build is running.
    """

    expected_title = "ci.pipeline.allpackages-build.image.running"
    expected_subti = 'Koji task 34126640 of package rpms/nmstate is '\
        'being built in an image in the All Packages (Build) CI pipeline '\
        'on branch f28'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/" \
        "blue/organizations/jenkins/fedora-f28-build-pipeline/detail/" \
        "fedora-f28-build-pipeline/384/pipeline/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '4a5e1bf0da6d9dfba3e0dc300fe58f6fc7d064df703eafbf2502dd900f69c1b4'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['jankratochvil'])
    expected_objects = set(
        ['rpms/nmstate/kojitask-34126640/f28/allpackages-build/image/running'])
    msg = {
      "username": None,
      "source_name": "datanommer",
      "i": 0,
      "timestamp": 1555074222.0,
      "msg_id": "2019-a3efac22-0512-4251-92f5-9b3bd6365dc6",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.allpackages-build.image.running",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "build_id": "384",
        "status": "SUCCESS",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/blue/organizations/jenkins/fedora-f28-build-pipeline/detail/fedora-f28-build-pipeline/384/pipeline/",
        "type": "''",
        "nvr": "nmstate-0.0.5-2.fc28",
        "rev": "kojitask-34126640",
        "ci_topic": "org.centos.prod.ci.pipeline.allpackages-build.image.running",
        "username": "jankratochvil",
        "comment_id": None,
        "namespace": "rpms",
        "repo": "nmstate",
        "original_spec_nvr": "nmstate-0.0.5-2.fc28",
        "test_guidance": "''",
        "branch": "f28",
        "scratch": False,
        "ref": "x86_64"
      }
    }


class TestAllPackagesPRPackageRunning(Base):
    """ These messages are published when the Allpackages (PR) CI
    pipeline announces that a pull request for a package is running.
    """

    expected_title = "ci.pipeline.allpackages-pr.package.running"
    expected_subti = 'Pull request 19 of package rpms/selinux-policy is '\
        'being built in the All Packages (PR) CI pipeline on branch master'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/" \
        "blue/organizations/jenkins/fedora-rawhide-pr-pipeline/detail/" \
        "fedora-rawhide-pr-pipeline/1168/pipeline/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = None
    expected_packages = set([])
    expected_usernames = set()
    expected_objects = set(
        ['rpms/selinux-policy/PR-19/master/allpackages-pr/package/running'])
    msg = {
      "username": None,
      "source_name": "datanommer",
      "i": 0,
      "timestamp": 1555083213.0,
      "msg_id": "2019-5d7755f0-14f4-4de7-a927-824d7a068825",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.allpackages-pr.package.running",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "build_id": "1168",
        "status": "SUCCESS",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/blue/organizations/jenkins/fedora-rawhide-pr-pipeline/detail/fedora-rawhide-pr-pipeline/1168/pipeline/",
        "nvr": "",
        "rev": "PR-19",
        "ci_topic": "org.centos.prod.ci.pipeline.allpackages-pr.package.running",
        "username": None,
        "comment_id": None,
        "namespace": "rpms",
        "repo": "selinux-policy",
        "original_spec_nvr": "",
        "test_guidance": "''",
        "branch": "master",
        "scratch": True,
        "ref": "x86_64"
      }
    }


class TestAllPackagesPRPackageFunctionalRunning(Base):
    """ These messages are published when the Allpackages (PR) CI
    pipeline announces that the functional testing build of a pull
    request for a package is running.
    """

    expected_title = "ci.pipeline.allpackages-pr.package.test.functional.running"
    expected_subti = 'Pull request 105 of package rpms/python3 is running its '\
        'functional tests in the All Packages (PR) CI pipeline on branch master'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/" \
        "blue/organizations/jenkins/fedora-rawhide-pr-pipeline/detail/" \
        "fedora-rawhide-pr-pipeline/1167/pipeline/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = None
    expected_packages = set([])
    expected_usernames = set()
    expected_objects = set(
        ['rpms/python3/PR-105/master/allpackages-pr/package/test/functional/running'])
    msg = {
      "username": None,
      "source_name": "datanommer",
      "i": 0,
      "timestamp": 1555060923.0,
      "msg_id": "2019-a5cfb619-fa0b-4f34-a286-7e216d846c66",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.allpackages-pr.package.test.functional.running",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "build_id": "1167",
        "status": "SUCCESS",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/blue/organizations/jenkins/fedora-rawhide-pr-pipeline/detail/fedora-rawhide-pr-pipeline/1167/pipeline/",
        "nvr": "python3-3.7.3-2.fc31.pr.4229607131614fc0a723aa38ea21b892",
        "rev": "PR-105",
        "ci_topic": "org.centos.prod.ci.pipeline.allpackages-pr.package.test.functional.running",
        "username": None,
        "comment_id": None,
        "namespace": "rpms",
        "repo": "python3",
        "original_spec_nvr": "python3-3.7.3-2.fc31",
        "test_guidance": "''",
        "branch": "master",
        "scratch": True,
        "ref": "x86_64"
      }
    }


class TestAllPackagesPRImageRunning(Base):
    """ These messages are published when the Allpackages (PR) CI
    pipeline announces that the build of an image containing a pull
    request for a package is running.
    """

    expected_title = "ci.pipeline.allpackages-pr.image.running"
    expected_subti = 'Pull request 105 of package rpms/python3 is '\
        'being built in an image in the All Packages (PR) CI pipeline '\
        'on branch master'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/" \
        "blue/organizations/jenkins/fedora-rawhide-pr-pipeline/detail/" \
        "fedora-rawhide-pr-pipeline/1167/pipeline/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = None
    expected_packages = set([])
    expected_usernames = set()
    expected_objects = set(
        ['rpms/python3/PR-105/master/allpackages-pr/image/running'])
    msg = {
      "username": None,
      "source_name": "datanommer",
      "i": 0,
      "timestamp": 1555060695.0,
      "msg_id": "2019-37db7e9b-7dde-41c7-bdaa-eee2863ca30a",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.allpackages-pr.image.running",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "build_id": "1167",
        "status": "SUCCESS",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/blue/organizations/jenkins/fedora-rawhide-pr-pipeline/detail/fedora-rawhide-pr-pipeline/1167/pipeline/",
        "type": "''",
        "nvr": "python3-3.7.3-2.fc31.pr.4229607131614fc0a723aa38ea21b892",
        "rev": "PR-105",
        "ci_topic": "org.centos.prod.ci.pipeline.allpackages-pr.image.running",
        "username": None,
        "comment_id": None,
        "namespace": "rpms",
        "repo": "python3",
        "original_spec_nvr": "python3-3.7.3-2.fc31",
        "test_guidance": "''",
        "branch": "master",
        "scratch": True,
        "ref": "x86_64"
      }
    }


class TestAllPackagesBuildPackageCompleteSuccess(Base):
    """ These messages are published when the All Packages (build) CI
    pipeline announces that the build of a package completed.
    """

    expected_title = "ci.pipeline.allpackages-build.package.complete"
    expected_subti = 'Koji task 34126640 of package rpms/nmstate passed ' \
        'building in the All Packages (Build) CI pipeline on branch f28'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/" \
        "blue/organizations/jenkins/fedora-f28-build-pipeline/detail/" \
        "fedora-f28-build-pipeline/384/pipeline/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '4a5e1bf0da6d9dfba3e0dc300fe58f6fc7d064df703eafbf2502dd900f69c1b4'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['jankratochvil'])
    expected_objects = set(['rpms/nmstate/kojitask-34126640/f28/allpackages-build/package/complete'])
    msg = {
      "username": None,
      "source_name": "datanommer",
      "i": 0,
      "timestamp": 1555074209.0,
      "msg_id": "2019-5e1ebd5f-7ee2-4cfb-b37f-92daa80260dd",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.allpackages-build.package.complete",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "build_id": "384",
        "status": "SUCCESS",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/blue/organizations/jenkins/fedora-f28-build-pipeline/detail/fedora-f28-build-pipeline/384/pipeline/",
        "nvr": "nmstate-0.0.5-2.fc28",
        "rev": "kojitask-34126640",
        "ci_topic": "org.centos.prod.ci.pipeline.allpackages-build.package.complete",
        "username": "jankratochvil",
        "comment_id": None,
        "namespace": "rpms",
        "repo": "nmstate",
        "original_spec_nvr": "nmstate-0.0.5-2.fc28",
        "test_guidance": "''",
        "branch": "f28",
        "scratch": False,
        "ref": "x86_64"
      }
    }


class TestAllPackagesBuildPackageFunctionalCompleteSuccess(Base):
    """ These messages are published when the Allpackages (build) CI
    pipeline announces that the functional testing build of a package
    has completed.
    """

    expected_title = "ci.pipeline.allpackages-build.package.test.functional.complete"
    expected_subti = 'Koji task 34126640 of package rpms/nmstate passed its '\
        'functional tests in the All Packages (Build) CI pipeline on branch f28'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/" \
        "blue/organizations/jenkins/fedora-f28-build-pipeline/detail/" \
        "fedora-f28-build-pipeline/384/pipeline/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '4a5e1bf0da6d9dfba3e0dc300fe58f6fc7d064df703eafbf2502dd900f69c1b4'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['jankratochvil'])
    expected_objects = set(
        ['rpms/nmstate/kojitask-34126640/f28/allpackages-build/package/test/functional/complete'])
    msg = {
      "username": None,
      "source_name": "datanommer",
      "i": 0,
      "timestamp": 1555074628.0,
      "msg_id": "2019-9762bda3-5c5b-4890-9f44-94c134b5b67e",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.allpackages-build.package.test.functional.complete",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "build_id": "384",
        "status": "SUCCESS",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/blue/organizations/jenkins/fedora-f28-build-pipeline/detail/fedora-f28-build-pipeline/384/pipeline/",
        "nvr": "nmstate-0.0.5-2.fc28",
        "rev": "kojitask-34126640",
        "ci_topic": "org.centos.prod.ci.pipeline.allpackages-build.package.test.functional.complete",
        "username": "jankratochvil",
        "comment_id": None,
        "namespace": "rpms",
        "repo": "nmstate",
        "original_spec_nvr": "nmstate-0.0.5-2.fc28",
        "test_guidance": "''",
        "branch": "f28",
        "scratch": False,
        "ref": "x86_64"
      }
    }


class TestAllPackagesBuildImageCompleteSuccess(Base):
    """ These messages are published when the Allpackages (build) CI
    pipeline announces that the build of an image containing a package
    has completed.
    """

    expected_title = "ci.pipeline.allpackages-build.image.complete"
    expected_subti = 'Koji task 34126640 of package rpms/nmstate passed '\
        'being built in an image in the All Packages (Build) CI pipeline '\
        'on branch f28'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/" \
        "blue/organizations/jenkins/fedora-f28-build-pipeline/detail/" \
        "fedora-f28-build-pipeline/384/pipeline/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '4a5e1bf0da6d9dfba3e0dc300fe58f6fc7d064df703eafbf2502dd900f69c1b4'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['jankratochvil'])
    expected_objects = set(
        ['rpms/nmstate/kojitask-34126640/f28/allpackages-build/image/complete'])
    msg = {
      "username": None,
      "source_name": "datanommer",
      "i": 0,
      "timestamp": 1555074363.0,
      "msg_id": "2019-00a1eb4e-5159-49cd-a230-3436af472461",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.allpackages-build.image.complete",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "build_id": "384",
        "status": "SUCCESS",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/blue/organizations/jenkins/fedora-f28-build-pipeline/detail/fedora-f28-build-pipeline/384/pipeline/",
        "type": "qcow2",
        "nvr": "nmstate-0.0.5-2.fc28",
        "rev": "kojitask-34126640",
        "ci_topic": "org.centos.prod.ci.pipeline.allpackages-build.image.complete",
        "username": "jankratochvil",
        "comment_id": None,
        "namespace": "rpms",
        "repo": "nmstate",
        "original_spec_nvr": "nmstate-0.0.5-2.fc28",
        "test_guidance": "''",
        "branch": "f28",
        "scratch": False,
        "ref": "x86_64"
      }
    }


class TestAllPackagesPRPackageCompleteFailure(Base):
    """ These messages are published when the All Packages (PR) CI
    pipeline announces that the build of a pull request for a package
    completed.
    """

    expected_title = "ci.pipeline.allpackages-pr.package.complete"
    expected_subti = 'Pull request 19 of package rpms/selinux-policy failed ' \
        'building in the All Packages (PR) CI pipeline on branch master'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/" \
        "blue/organizations/jenkins/fedora-rawhide-pr-pipeline/detail/" \
        "fedora-rawhide-pr-pipeline/1168/pipeline/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = None
    expected_packages = set([])
    expected_usernames = set()
    expected_objects = set(
        ['rpms/selinux-policy/PR-19/master/allpackages-pr/package/complete'])
    msg = {
      "username": None,
      "source_name": "datanommer",
      "i": 0,
      "timestamp": 1555083574.0,
      "msg_id": "2019-4e3896db-a922-4663-862b-e80ee213bac6",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.allpackages-pr.package.complete",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "build_id": "1168",
        "status": "FAILURE",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/blue/organizations/jenkins/fedora-rawhide-pr-pipeline/detail/fedora-rawhide-pr-pipeline/1168/pipeline/",
        "nvr": "",
        "rev": "PR-19",
        "ci_topic": "org.centos.prod.ci.pipeline.allpackages-pr.package.complete",
        "username": None,
        "comment_id": None,
        "namespace": "rpms",
        "repo": "selinux-policy",
        "original_spec_nvr": "",
        "test_guidance": "''",
        "branch": "master",
        "scratch": True,
        "ref": "x86_64"
      }
    }


class TestAllPackagesPRPackageFunctionalCompleteSuccess(Base):
    """ These messages are published when the Allpackages (PR) CI
    pipeline announces that the functional testing build of a pull
    request for a package has completed.
    """

    expected_title = "ci.pipeline.allpackages-pr.package.test.functional.complete"
    expected_subti = 'Pull request 105 of package rpms/python3 passed its '\
        'functional tests in the All Packages (PR) CI pipeline on branch master'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/" \
        "blue/organizations/jenkins/fedora-rawhide-pr-pipeline/detail/" \
        "fedora-rawhide-pr-pipeline/1167/pipeline/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = None
    expected_packages = set([])
    expected_usernames = set()
    expected_objects = set(
        ['rpms/python3/PR-105/master/allpackages-pr/package/test/functional/complete'])
    msg = {
      "username": None,
      "source_name": "datanommer",
      "i": 0,
      "timestamp": 1555062557.0,
      "msg_id": "2019-0fa8c562-edec-495e-b558-1cfb82e76fb0",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.allpackages-pr.package.test.functional.complete",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "build_id": "1167",
        "status": "SUCCESS",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/blue/organizations/jenkins/fedora-rawhide-pr-pipeline/detail/fedora-rawhide-pr-pipeline/1167/pipeline/",
        "nvr": "python3-3.7.3-2.fc31.pr.4229607131614fc0a723aa38ea21b892",
        "rev": "PR-105",
        "ci_topic": "org.centos.prod.ci.pipeline.allpackages-pr.package.test.functional.complete",
        "username": None,
        "comment_id": None,
        "namespace": "rpms",
        "repo": "python3",
        "original_spec_nvr": "python3-3.7.3-2.fc31",
        "test_guidance": "''",
        "branch": "master",
        "scratch": True,
        "ref": "x86_64"
      }
    }


class TestAllPackagesPRImageCompleteSuccess(Base):
    """ These messages are published when the Allpackages (PR) CI
    pipeline announces that the build of an image containing a pull
    request for a package has completed.
    """

    expected_title = "ci.pipeline.allpackages-pr.image.complete"
    expected_subti = 'Pull request 105 of package rpms/python3 passed '\
        'being built in an image in the All Packages (PR) CI pipeline '\
        'on branch master'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/" \
        "blue/organizations/jenkins/fedora-rawhide-pr-pipeline/detail/" \
        "fedora-rawhide-pr-pipeline/1167/pipeline/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = None
    expected_packages = set([])
    expected_usernames = set()
    expected_objects = set(
        ['rpms/python3/PR-105/master/allpackages-pr/image/complete'])
    msg = {
      "username": None,
      "source_name": "datanommer",
      "i": 0,
      "timestamp": 1555060816.0,
      "msg_id": "2019-16f053b2-794d-4695-8ae5-62d874f91ab5",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.allpackages-pr.image.complete",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "build_id": "1167",
        "status": "SUCCESS",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/blue/organizations/jenkins/fedora-rawhide-pr-pipeline/detail/fedora-rawhide-pr-pipeline/1167/pipeline/",
        "type": "qcow2",
        "nvr": "python3-3.7.3-2.fc31.pr.4229607131614fc0a723aa38ea21b892",
        "rev": "PR-105",
        "ci_topic": "org.centos.prod.ci.pipeline.allpackages-pr.image.complete",
        "username": None,
        "comment_id": None,
        "namespace": "rpms",
        "repo": "python3",
        "original_spec_nvr": "python3-3.7.3-2.fc31",
        "test_guidance": "''",
        "branch": "master",
        "scratch": True,
        "ref": "x86_64"
      }
    }


class TestAllPackagesBuildCompleteSuccess(Base):
    """ These messages are published when the Allpackages (build) CI
    pipeline announces having completed running the entire pipeline
    on a build of a package.
    """

    expected_title = "ci.pipeline.allpackages-build.complete"
    expected_subti = 'Koji task "34126640" of package rpms/nmstate passed '\
        'the All Packages (Build) CI pipeline '\
        'on branch f28'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/" \
        "blue/organizations/jenkins/fedora-f28-build-pipeline/detail/" \
        "fedora-f28-build-pipeline/384/pipeline/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        '4a5e1bf0da6d9dfba3e0dc300fe58f6fc7d064df703eafbf2502dd900f69c1b4'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['jankratochvil'])
    expected_objects = set(
        ['rpms/nmstate/kojitask-34126640/f28/allpackages-build/complete'])
    msg = {
      "username": None,
      "source_name": "datanommer",
      "i": 0,
      "timestamp": 1555074635.0,
      "msg_id": "2019-72768646-f42c-47fe-a033-8c3b9581ad7e",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.allpackages-build.complete",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "build_id": "384",
        "status": "SUCCESS",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/blue/organizations/jenkins/fedora-f28-build-pipeline/detail/fedora-f28-build-pipeline/384/pipeline/",
        "nvr": "nmstate-0.0.5-2.fc28",
        "rev": "kojitask-34126640",
        "ci_topic": "org.centos.prod.ci.pipeline.allpackages-build.complete",
        "username": "jankratochvil",
        "comment_id": None,
        "namespace": "rpms",
        "repo": "nmstate",
        "original_spec_nvr": "nmstate-0.0.5-2.fc28",
        "test_guidance": "''",
        "branch": "f28",
        "scratch": False,
        "ref": "x86_64"
      }
    }


class TestAllPackagesPRCompleteSuccess(Base):
    """ These messages are published when the All Packages (PR) CI
    pipeline announces having completed running the entire pipeline
    on a pull request for a package.
    """

    expected_title = "ci.pipeline.allpackages-pr.complete"
    expected_subti = 'Pull request "11" of package rpms/python38 passed ' \
        'the All Packages (PR) CI pipeline on branch master'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/" \
        "blue/organizations/jenkins/fedora-rawhide-pr-pipeline/detail/" \
        "fedora-rawhide-pr-pipeline/1165/pipeline/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = None
    expected_packages = set([])
    expected_usernames = set()
    expected_objects = set(
        ['rpms/python38/PR-11/master/allpackages-pr/complete'])
    msg = {
      "username": None,
      "source_name": "datanommer",
      "i": 0,
      "timestamp": 1554997291.0,
      "msg_id": "2019-b9387d85-612c-48d2-98e3-cb824b772e4e",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.allpackages-pr.complete",
      "headers": {},
      "source_version": "0.9.0",
      "msg": {
        "build_id": "1165",
        "status": "SUCCESS",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/blue/organizations/jenkins/fedora-rawhide-pr-pipeline/detail/fedora-rawhide-pr-pipeline/1165/pipeline/",
        "nvr": "python38-3.8.0~a3-1.fc31.pr.69dff692474b47c5b91beec249cb4cad",
        "rev": "PR-11",
        "ci_topic": "org.centos.prod.ci.pipeline.allpackages-pr.complete",
        "username": None,
        "comment_id": None,
        "namespace": "rpms",
        "repo": "python38",
        "original_spec_nvr": "python38-3.8.0~a3-1.fc31",
        "test_guidance": "''",
        "branch": "master",
        "scratch": True,
        "ref": "x86_64"
      }
    }


class TestContainerTestRunning(Base):
    """ These messages are published when the Container CI pipeline
    announces that the test of a container is running.
    """

    expected_title = "ci.pipeline.container-pr.container.test.functional.running"
    expected_subti = 'Commit 35cdcb6a of container container/tools is '\
        'running its functional tests in the Container CI pipeline '\
        'on branch master'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/" \
        "blue/organizations/jenkins/fedcontainer-rawhide-pr-pipeline/detail/" \
        "fedcontainer-rawhide-pr-pipeline/50/pipeline/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        'b13ed9018e915cdb42f59c1435e3d55bcac2f4d9843cda1a1d978dc6cad09968'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['cverna'])
    expected_objects = set(
        ['container/tools/35cdcb6a32562b632c075f2fd42793f7492dcdb3/'
         'master/container-pr/container/test/functional/running'])
    msg = {
      "username": None,
      "source_name": "datanommer",
      "i": 1,
      "timestamp": 1522054091.0,
      "msg_id": "2018-cfb9a40e-3220-4dcf-a5aa-270a6cee975c",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.container-pr.container.test.functional.running",
      "headers": {},
      "source_version": "0.8.2",
      "msg": {
        "CI_TYPE": "custom",
        "build_id": "50",
        "username": "cverna",
        "rev": "35cdcb6a32562b632c075f2fd42793f7492dcdb3",
        "message-content": "",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/blue/organizations/jenkins/fedcontainer-rawhide-pr-pipeline/detail/fedcontainer-rawhide-pr-pipeline/50/pipeline/",
        "namespace": "container",
        "CI_NAME": "fedcontainer-rawhide-pr-pipeline",
        "repo": "tools",
        "topic": "org.centos.prod.ci.pipeline.container-pr.container.test.functional.running",
        "status": "SUCCESS",
        "branch": "master",
        "test_guidance": "''",
        "ref": "x86_64"
      }
    }


class TestContainerCompleteSuccess(Base):
    """ These messages are published when the Container CI pipeline
    announces having completed successfully running the entire pipeline
    on a container.
    """

    expected_title = "ci.pipeline.container-pr.complete"
    expected_subti = 'Commit "35cdcb6a" of container container/tools passed the ' \
        'Container CI pipeline on branch master'
    expected_link = "https://jenkins-continuous-infra.apps.ci.centos.org/" \
        "blue/organizations/jenkins/fedcontainer-rawhide-pr-pipeline/detail/" \
        "fedcontainer-rawhide-pr-pipeline/50/pipeline/"
    expected_icon = "https://ci.centos.org/static/ec6de755/images/" \
        "headshot.png"
    expected_secondary_icon = 'https://seccdn.libravatar.org/avatar/'\
        'b13ed9018e915cdb42f59c1435e3d55bcac2f4d9843cda1a1d978dc6cad09968'\
        '?s=64&d=retro'
    expected_packages = set([])
    expected_usernames = set(['cverna'])
    expected_objects = set(
        ['container/tools/'
         '35cdcb6a32562b632c075f2fd42793f7492dcdb3/'
         'master/container-pr/complete'])
    msg = {
      "username": None,
      "source_name": "datanommer",
      "i": 1,
      "timestamp": 1522055492.0,
      "msg_id": "2018-1436f172-aa90-49f2-9ff0-9b34608f38e8",
      "crypto": "x509",
      "topic": "org.centos.prod.ci.pipeline.container-pr.complete",
      "headers": {},
      "source_version": "0.8.2",
      "msg": {
        "CI_TYPE": "custom",
        "build_id": "50",
        "username": "cverna",
        "rev": "35cdcb6a32562b632c075f2fd42793f7492dcdb3",
        "message-content": "",
        "build_url": "https://jenkins-continuous-infra.apps.ci.centos.org/blue/organizations/jenkins/fedcontainer-rawhide-pr-pipeline/detail/fedcontainer-rawhide-pr-pipeline/50/pipeline/",
        "namespace": "container",
        "CI_NAME": "upstream-fedora-f28-pipeline",
        "repo": "tools",
        "topic": "org.centos.prod.ci.pipeline.container-pr.complete",
        "status": "SUCCESS",
        "branch": "master",
        "test_guidance": "''",
        "ref": "x86_64"
      }
    }


add_doc(locals())


if __name__ == '__main__':
    unittest.main()
