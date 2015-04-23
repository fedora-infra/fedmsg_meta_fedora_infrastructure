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
#
#
# Authors:  Hammad Haleem <hammadhaleem@gmail.com>

""" Tests for Fedora College Message """

import unittest
import datetime

from fedmsg.tests.test_meta import Base

from .common import add_doc


class TestMediaUploadBase():

    """ These messages are for people when
    they upload stuff to fedora College portal`_.
    """

    expected_title = "fedoracollege.media.upload"
    expected_subtitle = 'pingou uploaded a new file of type "image"'
    expected_link = "http://testlink"
    expected_icon = (None)
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c"
        "?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    msg = {
        "username": "pingou",
        "i": 1,
        "timestamp": 1379638157.759283,
        "msg_id": "2013-96f9ca0e-c7c6-43f0-9de7-7a268c7f1cef",
        "topic": "fedoracollege.media.upload",
        "link": "https://FedoraCollege.org/testlink",
        "msg":
        {
                    "title": "image",
                    "link": "https://testlink",
                    "content_url": "http://demo.engineerinme.com/static/uploads/\
                    hammadhaleem/1404190396.4603c7aec5\
                    a7f21a64a4489fc68d762168.png",
                    "file_type": "image",
                    "filename": "1404190396.4603c7aec5a7f\
                    21a64a4489fc68d762168.png",
                    "id": "1",
                    "name": "File upload",
                    "sys_path ": "/home/engineer/fedora-college/fedora_college/static/\
                    uploads/hammadhaleem/34343423.png",
                    "tags": "fedora-college  image-upload website ",
                    "thumb": "static/uploads/hammadhaleem/1404190396.4603c7aec5a7f21a64a4489f\
                    c68d762168.png_thumb.jpg",
                    "timestamp": "2014-07-01 04:53:16.599954",
                    "username": "pingou"
        }
    }


class TestContentEdit(Base):

    """ These messages are published when
    someone edit content in the fedora College.
    """
    expected_title = "fedoracollege.content.edit"
    expected_subtitle = 'pingou Edited content titled "test"'
    expected_link = "http://testlink"
    expected_icon = (None)
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c"
        "?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    msg = {
        "username": "pingou",
        "i": 1,
        "timestamp": 1379638157.759283,
        "msg_id": "2013-96f9ca0e-c7c6-43f0-9de7-7a268c7f1cef",
        "topic": "fedoracollege.content.edit",
        "link": "https://FedoraCollege.org/testlink",
        "msg":
        {
                    "title": "test",
                    "link": "https://testlink",
                    "active": True,
                    "date_added": "Tue, 01 Jul 2014 19:07:00 GMT",
                    "description": "The Content available on this\
                    website is contributed from people in fedora\
                    community. Mostly all\
                    the content has CC licence.</p>",
                    "id": 2,
                    "media_added_ids": "",
                    "slug": "about-the-content",
                    "tags": "fedora-college, blog",
                    "title": "About the content",
                    "type": "blog",
                    "username": "pingou"
        }
    }


class TestContentAdded(Base):

    """ These messages are published when
    someone edit content in the fedora College.
    """

    expected_title = "fedoracollege.content.edit"
    expected_subtitle = 'pingou Created new content titled "test"'
    expected_link = "http://testlink"
    expected_icon = (None)
    expected_secondary_icon = (
        "https://seccdn.libravatar.org/avatar/"
        "01fe73d687f4db328da1183f2a1b5b22962ca9d9c50f0728aafeac974856311c"
        "?s=64&d=retro")
    expected_packages = set([])
    expected_usernames = set(['pingou'])
    msg = {
        "username": "pingou",
        "i": 1,
        "timestamp": 1379638157.759283,
        "msg_id": "2013-96f9ca0e-c7c6-43f0-9de7-7a268c7f1cef",
        "topic": "fedoracollege.content.added",
        "link": "https://FedoraCollege.org/testlink",
        "msg": {
            "title": "test",
            "link": "https://testlink",
            "active": True,
                    "date_added": "Tue, 01 Jul 2014 19:07:00 GMT",
                    "description": "The Content available on this\
                    website is contributed from people in fedora\
                    community. Mostly all\
                    the content has CC licence.</p>",
                    "id": 2,
                    "media_added_ids": "",
                    "slug": "about-the-content",
                    "tags": "fedora-college, blog",
                    "title": "About the content",
                    "type": "blog",
                    "username": "pingou"
        }
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
