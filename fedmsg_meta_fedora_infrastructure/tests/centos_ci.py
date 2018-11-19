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


class TestPackageIgnore(Base):
    """ These messages are published when the Atomic CI pipeline announces that
    it ignores a commit made on dist-git.
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


class TestPackageComplete(Base):
    """ These messages are published when the Atomic CI pipeline announces that
    the build of a package completed.
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


class TestPackageQueued(Base):
    """ These messages are published when the Atomic CI pipeline announces that
    the build of a package is queued.
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


class TestPackageRunning(Base):
    """ These messages are published when the Atomic CI pipeline announces that
    the build of a package is running.
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


class TestComposeComplete(Base):
    """ These messages are published when the Atomic CI pipeline announces that
    a compose containing a specified package has completed.
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


class TestComposeRunning(Base):
    """ These messages are published when the Atomic CI pipeline announces that
    a compose containing a specified package is running.
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


class TestComposeTestIntegrationComplete(Base):
    """ These messages are published when the Atomic CI pipeline announces that
    the integration test of a compose containing a specified package has
    completed.
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


class TestComposeTestIntegrationRunning(Base):
    """ These messages are published when the Atomic CI pipeline announces that
    the integration test of a compose containing a specified package are
    running.
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


class TestComposeTestIntegrationQueued(Base):
    """ These messages are published when the Atomic CI pipeline announces that
    the integration test of a compose containing a specified package are
    queued.
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


class TestImageComplete(Base):
    """ These messages are published when the Atomic CI pipeline announces that
    the build of the image generated from the compose containing a specified
    package has completed.
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


class TestImageRunning(Base):
    """ These messages are published when the Atomic CI pipeline announces that
    the build of the image generated from the compose containing a specified
    package is running.
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


class TestImageTestSmokeComplete(Base):
    """ These messages are published when the Atomic CI pipeline announces that
    the image generated from the compose containing a specified
    package has completed its tests.
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


class TestImageTestSmokeRunning(Base):
    """ These messages are published when the Atomic CI pipeline announces that
    the image generated from the compose containing a specified
    package has completed its tests.
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

class TestPackageTestFunctionalQueued(Base):
    """ These messages are published when the Atomic CI pipeline announces queuing
    the function tests of a package.
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


class TestPackageTestFunctionalRunning(Base):
    """ These messages are published when the Atomic CI pipeline announces running
    the function tests of a package.
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


class TestPackageTestFunctionalComplete(Base):
    """ These messages are published when the Atomic CI pipeline announces having
    completed the function tests of a package.
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


class TestCompleteSuccess(Base):
    """ These messages are published when the Atomic CI pipeline announces having
    completed successfully running the entire pipeline on a package.
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


class TestCompleteAborted(Base):
    """ These messages are published when the Atomic CI pipeline announces having
    aborted a run of the pipeline on a package.
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


class TestCompleteFailed(Base):
    """ These messages are published when the Atomic CI pipeline announces having
    failed a run of the pipeline on a package.

    This means the pipeline failed to run the tests (as opposed to run the
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


class TestCompleteError(Base):
    """ These messages are published when the Atomic CI pipeline announces having
    errored a run of the pipeline on a package.

    This means the pipeline could run the tests but the tests themselves failed
    (as opposed to the pipeline failed to run the tests).
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


class LegacyTestAllPackagesPackageRunning(Base):
    """ These messages are published when the Allpackages CI pipeline
    announces that the build of a package is running.
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


class LegacyTestAllPackagesCompleteSuccess(Base):
    """ These messages are published when the All Packages CI pipeline
    announces having completed successfully running the entire pipeline
    on a package.
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


class TestAllPackagesPackageRunning(Base):
    """ These messages are published when the Allpackages CI pipeline
    announces that the build of a package is running.
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


class TestAllPackagesCompleteSuccess(Base):
    """ These messages are published when the All Packages CI pipeline
    announces having completed successfully running the entire pipeline
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
