# This file is part of fedmsg.
# Copyright (C) 2014-2018 Red Hat, Inc.
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
# Authors:  David Gay <oddshocks@riseup.net>
#           Sayan Chowdhury <sayanchowdhury@fedoraproject.org>
""" Tests for Fedimg messages """

import unittest

from fedmsg.tests.test_meta import Base

from .common import add_doc


class TestImageUploadStart(Base):
    """ These messages are published when an image upload has started.
    Fedimg picks up this message when a compose finishes and will begin
    the process of registering the .raw.xz file as as an image
    with a cloud provider.
    """

    expected_title = "fedimg.image.upload"
    image_name = "Fedora-Cloud-Base-24-20160710.0.x86_64"
    dest = "eu-west-1"
    expected_subti = "{0} started uploading to {1}".format(image_name,
                                                           dest)
    expected_icon = 'https://apps.fedoraproject.org/img/icons/fedimg.png'
    expected_secondary_icon = None
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set(['image/upload/started'])

    msg = {
        u'i': 1,
        u'msg': {
            u'image_url': 'http://kojipkgs.fedoraproject.org/compose//twoweek/'
                          'Fedora-Atomic-24-20160710.0/compose/CloudImages/'
                          'x86_64/images/Fedora-Cloud-Base-24-'
                          '20160710.0.x86_64.raw.xz',
            u'image_name': 'Fedora-Cloud-Base-24-20160710.0.x86_64',
            u'destination': 'eu-west-1',
            u'status': 'started',
            u'compose': {
                u'compose_id': 'Fedora-Atomic-24-20160710.0',
            }
        },
        u'topic': u'org.fedoraproject.stg.fedimg.image.upload',
        u'username': u'fedimg',
        u'timestamp': 1371498303.125771,
    }


class TestImageUploadComplete(Base):
    """ These messages are published when an image upload finishes.
        At this point, Fedimg has completed registering a .raw.xz
        image with a cloud provider. """

    expected_title = "fedimg.image.upload"
    image_name = "Fedora-Cloud-Base-24-20160710.0.x86_64"
    dest = "eu-west-1"
    ami_id = 'ami-1234fda'
    virt_type = 'HVM'
    vol_type = 'gp2'
    expected_subti = "{0} finished uploading to {1} ({2}, {3}, {4})".format(
            image_name, dest, ami_id, virt_type, vol_type)
    expected_icon = 'https://apps.fedoraproject.org/img/icons/fedimg.png'
    expected_secondary_icon = None
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set(['image/upload/completed'])
    msg = {
        u'i': 1,
        u'msg': {
            u'image_url': 'http://kojipkgs.fedoraproject.org/compose//twoweek/'
                          'Fedora-Atomic-24-20160710.0/compose/CloudImages/'
                          'x86_64/images/Fedora-Cloud-Base-24-'
                          '20160710.0.x86_64.raw.xz',
            u'image_name': 'Fedora-Cloud-Base-24-20160710.0.x86_64',
            u'destination': 'eu-west-1',
            u'status': 'completed',
            u'extra': {
                u'id': 'ami-1234fda',
                u'virt_type': 'HVM',
                u'vol_type': 'gp2',
            },
            u'compose': {
                u'compose_id': 'Fedora-Atomic-24-20160710.0',
            }
        },
        u'topic': u'org.fedoraproject.stg.fedimg.image.upload',
        u'username': u'fedimg',
        u'timestamp': 1371498303.125771,
    }


class TestImagePublish(Base):
    """ These messages are published when an image and snapshot is made public.
    """

    expected_title = "fedimg.image.publish"
    image_name = "Fedora-Atomic-27-20180507.0.x86_64"
    dest = "eu-west-2"
    ami_id = 'ami-d813f1bf'
    virt_type = 'hvm'
    vol_type = 'gp2'
    expected_subti = "{0} published in region, {1} ({2}, {3}, {4})".format(
            image_name, dest, ami_id, virt_type, vol_type)
    expected_icon = 'https://apps.fedoraproject.org/img/icons/fedimg.png'
    expected_secondary_icon = None
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set([])
    msg = {
        u'i': 1,
        u'msg': {
            "compose": "Fedora-Atomic-27-20180507.0",
            "service": "EC2",
            "extra": {
              "virt_type": "hvm",
              "id": "ami-d813f1bf",
              "vol_type": "gp2"
            },
            "destination": "eu-west-2",
            "image_name": "Fedora-Atomic-27-20180507.0.x86_64",
            "image_url": None
        },
        u'topic': u'org.fedoraproject.stg.fedimg.image.publish',
        u'username': u'fedimg',
        u'timestamp': 1371498303.125771,
    }


class TestImageCopy(Base):
    """ These messages are published when an image has been copied to other
        region from the base region."""

    expected_title = "fedimg.image.copy"
    image_name = "Fedora-Atomic-27-20180507.0.x86_64"
    dest = "us-west-2"
    ami_id = 'ami-2e80f656'
    source_image_id = 'ami-991999e6'
    virt_type = 'hvm'
    vol_type = 'gp2'
    expected_subti = ("{0} copied to {1} using source image, {5} "
                      "({2}, {3}, {4})").format(image_name, dest, ami_id,
                                                virt_type, vol_type,
                                                source_image_id)
    expected_icon = 'https://apps.fedoraproject.org/img/icons/fedimg.png'
    expected_secondary_icon = None
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set([])
    msg = {
        u'i': 1,
        u'msg': {
            "service": "EC2",
            "destination": "us-west-2",
            "image_name": "Fedora-Atomic-27-20180507.0.x86_64",
            "compose_id": "Fedora-Atomic-27-20180507.0",
            "extra": {
                "virt_type": "hvm",
                "source_image_id": "ami-991999e6",
                "id": "ami-2e80f656",
                "vol_type": "gp2"
            }
        },
        u'topic': u'org.fedoraproject.stg.fedimg.image.copy',
        u'username': u'fedimg',
        u'timestamp': 1371498303.125771,
    }


class LegacyTestImageUploadStartCompose(Base):
    """ These messages are published when an image upload has started.
    Fedimg picks up this message when a compose finishes and will begin
    the process of registering the .raw.xz file as as an image
    with a cloud provider.
    """

    expected_title = "fedimg.image.upload"
    image_name = "Fedora-Cloud-Base-24-20160710.0.x86_64"
    dest = "EC2-eu-west-1"
    expected_subti = "{0} started uploading to {1}".format(image_name,
                                                           dest)
    expected_icon = 'https://apps.fedoraproject.org/img/icons/fedimg.png'
    expected_secondary_icon = None
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set(['image/upload/started'])

    msg = {
        u'i': 1,
        u'msg': {
            u'image_url': 'http://kojipkgs.fedoraproject.org/compose//twoweek/'
                          'Fedora-Atomic-24-20160710.0/compose/CloudImages/'
                          'x86_64/images/Fedora-Cloud-Base-24-'
                          '20160710.0.x86_64.raw.xz',
            u'image_name': 'Fedora-Cloud-Base-24-20160710.0.x86_64',
            u'destination': 'EC2-eu-west-1',
            u'status': 'started',
            u'compose': {
                u'compose_id': 'Fedora-Atomic-24-20160710.0',
            }
        },
        u'topic': u'org.fedoraproject.stg.fedimg.image.upload',
        u'username': u'fedimg',
        u'timestamp': 1371498303.125771,
    }


class LegacyTestImageUploadCompleteCompose(Base):
    """ These messages are published when an image upload finishes.
        At this point, Fedimg has completed registering a .raw.xz
        image with a cloud provider. """

    expected_title = "fedimg.image.upload"
    image_name = "Fedora-Cloud-Base-24-20160710.0.x86_64"
    dest = "EC2-eu-west-1"
    ami_id = 'ami-1234fda'
    virt_type = 'HVM'
    vol_type = 'gp2'
    expected_subti = "{0} finished uploading to {1} ({2}, {3}, {4})".format(
            image_name, dest, ami_id, virt_type, vol_type)
    expected_icon = 'https://apps.fedoraproject.org/img/icons/fedimg.png'
    expected_secondary_icon = None
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set(['image/upload/completed'])
    msg = {
        u'i': 1,
        u'msg': {
            u'image_url': 'http://kojipkgs.fedoraproject.org/compose//twoweek/'
                          'Fedora-Atomic-24-20160710.0/compose/CloudImages/'
                          'x86_64/images/Fedora-Cloud-Base-24-'
                          '20160710.0.x86_64.raw.xz',
            u'image_name': 'Fedora-Cloud-Base-24-20160710.0.x86_64',
            u'destination': 'EC2-eu-west-1',
            u'status': 'completed',
            u'extra': {
                u'id': 'ami-1234fda',
                u'virt_type': 'HVM',
                u'vol_type': 'gp2',
            },
            u'compose': {
                u'compose_id': 'Fedora-Atomic-24-20160710.0',
            }
        },
        u'topic': u'org.fedoraproject.stg.fedimg.image.upload',
        u'username': u'fedimg',
        u'timestamp': 1371498303.125771,
    }


class LegacyTestImageTestStartCompose(Base):
    """ These messages are published when an image test has started.
        At this point, Fedimg tries to start an instance of a
        image that it registered in the previous step, and check
        to see that it's running properly. """

    expected_title = "fedimg.image.test"
    image_name = "Fedora-Cloud-Base-24-20160710.0.x86_64"
    dest = "EC2-eu-west-1"
    ami_id = 'ami-1234fda'
    virt_type = 'HVM'
    vol_type = 'gp2'
    expected_subti = "{0} started testing on {1} ({2}, {3}, {4})".format(
            image_name, dest, ami_id, virt_type, vol_type)
    expected_icon = 'https://apps.fedoraproject.org/img/icons/fedimg.png'
    expected_secondary_icon = None
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set(['image/test/started'])
    msg = {
        u'i': 1,
        u'msg': {
            u'image_url': 'http://kojipkgs.fedoraproject.org/compose//twoweek/'
                          'Fedora-Atomic-24-20160710.0/compose/CloudImages/'
                          'x86_64/images/Fedora-Cloud-Base-24-'
                          '20160710.0.x86_64.raw.xz',
            u'image_name': 'Fedora-Cloud-Base-24-20160710.0.x86_64',
            u'destination': 'EC2-eu-west-1',
            u'status': 'started',
            u'extra': {
                u'id': 'ami-1234fda',
                u'virt_type': 'HVM',
                u'vol_type': 'gp2',
            },
            u'compose': {
                u'compose_id': 'Fedora-Atomic-24-20160710.0',
            }
        },
        u'topic': u'org.fedoraproject.stg.fedimg.image.test',
        u'username': u'fedimg',
        u'timestamp': 1371498303.125771,
    }


class LegacyTestImageUploadStart(Base):
    """ These messages are published when an image upload has started.
        At this point, Fedimg has picked up a completed Koji
        createImage task and will begin the process of registering
        the .raw.xz file as as an image with a cloud provider. """

    expected_title = "fedimg.image.upload"
    image_name = "fedora-cloud-base-rawhide-20140604.x86_64"
    dest = "EC2-eu-west-1"
    expected_subti = "{0} started uploading to {1}".format(image_name,
                                                                 dest)
    expected_icon = 'https://apps.fedoraproject.org/img/icons/fedimg.png'
    expected_secondary_icon = None
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set(['image/upload/started'])
    msg = {
        u'i': 1,
        u'msg': {
            u'image_url': 'https://kojipkgs.fedoraproject.org//work/'
                          'tasks/5144/6925144/fedora-cloud-base-'
                          'rawhide-20140604.x86_64.raw.xz',
            u'image_name': 'fedora-cloud-base-rawhide-20140604.x86_64',
            u'destination': 'EC2-eu-west-1',
            u'status': 'started',
        },
        u'topic': u'org.fedoraproject.stg.fedimg.image.upload',
        u'username': u'fedimg',
        u'timestamp': 1371498303.125771,
    }


class LegacyTestImageUploadComplete(Base):
    """ These messages are published when an image upload finishes.
        At this point, Fedimg has completed registering a .raw.xz
        image with a cloud provider. """

    expected_title = "fedimg.image.upload"
    image_name = "fedora-cloud-base-rawhide-20140604.x86_64"
    dest = "EC2-eu-west-1"
    ami_id = 'ami-1234fda'
    virt_type = 'HVM'
    vol_type = 'gp2'
    expected_subti = "{0} finished uploading to {1} ({2}, {3}, {4})".format(
            image_name, dest, ami_id, virt_type, vol_type)
    expected_icon = 'https://apps.fedoraproject.org/img/icons/fedimg.png'
    expected_secondary_icon = None
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set(['image/upload/completed'])
    msg = {
        u'i': 1,
        u'msg': {
            u'image_url': 'https://kojipkgs.fedoraproject.org//work/'
                          'tasks/5144/6925144/fedora-cloud-base-'
                          'rawhide-20140604.x86_64.raw.xz',
            u'image_name': 'fedora-cloud-base-rawhide-20140604.x86_64',
            u'destination': 'EC2-eu-west-1',
            u'status': 'completed',
            u'extra': {
                u'id': 'ami-1234fda',
                u'virt_type': 'HVM',
                u'vol_type': 'gp2',
            },
        },
        u'topic': u'org.fedoraproject.stg.fedimg.image.upload',
        u'username': u'fedimg',
        u'timestamp': 1371498303.125771,
    }


class LegacyTestImageTestStart(Base):
    """ These messages are published when an image test has started.
        At this point, Fedimg tries to start an instance of a
        image that it registered in the previous step, and check
        to see that it's running properly. """

    expected_title = "fedimg.image.test"
    image_name = "fedora-cloud-base-rawhide-20140604.x86_64"
    dest = "EC2-eu-west-1"
    ami_id = 'ami-1234fda'
    virt_type = 'HVM'
    vol_type = 'gp2'
    expected_subti = "{0} started testing on {1} ({2}, {3}, {4})".format(
            image_name, dest, ami_id, virt_type, vol_type)
    expected_icon = 'https://apps.fedoraproject.org/img/icons/fedimg.png'
    expected_secondary_icon = None
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set(['image/test/started'])
    msg = {
        u'i': 1,
        u'msg': {
            u'image_url': 'https://kojipkgs.fedoraproject.org//work/'
                          'tasks/5144/6925144/fedora-cloud-base-'
                          'rawhide-20140604.x86_64.raw.xz',
            u'image_name': 'fedora-cloud-base-rawhide-20140604.x86_64',
            u'destination': 'EC2-eu-west-1',
            u'status': 'started',
            u'extra': {
                u'id': 'ami-1234fda',
                u'virt_type': 'HVM',
                u'vol_type': 'gp2',
            },
        },
        u'topic': u'org.fedoraproject.stg.fedimg.image.test',
        u'username': u'fedimg',
        u'timestamp': 1371498303.125771,
    }

add_doc(locals())

if __name__ == '__main__':
    unittest.main()
