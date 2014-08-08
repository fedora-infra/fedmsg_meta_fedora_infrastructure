# This file is part of fedmsg.
# Copyright (C) 2014 Red Hat, Inc.
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
#
""" Tests for Fedimg messages """

import unittest

from fedmsg.tests.test_meta import Base

from common import add_doc


class TestImageUpload(Base):
    """ These messages are awarded when an image starts has started,
    completes, or fails. """

    expected_title = "fedimg.image.upload"
    image_name = "fedora-cloud-base-rawhide-20140604.x86_64"
    dest = "EC2-eu-west-1"
    expected_subti = "Image {0} started uploading to {1}".format(image_name,
                                                                 dest)
    expected_link = None
    expected_icon = None
    expected_secondary_icon = None
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set([])
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


class TestImageTest(Base):
    """ These messages are awarded when an image starts has started,
    completes, or fails. """

    expected_title = "fedimg.image.test"
    image_name = "fedora-cloud-base-rawhide-20140604.x86_64"
    dest = "EC2-eu-west-1"
    expected_subti = "Image {0} started testing on {1}".format(image_name,
                                                                 dest)
    expected_link = None
    expected_icon = None
    expected_secondary_icon = None
    expected_packages = set([])
    expected_usernames = set([])
    expected_objects = set([])
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
        u'topic': u'org.fedoraproject.stg.fedimg.image.test',
        u'username': u'fedimg',
        u'timestamp': 1371498303.125771,
    }

add_doc(locals())

if __name__ == '__main__':
    unittest.main()
