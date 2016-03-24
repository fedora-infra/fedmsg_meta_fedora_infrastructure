# This file is part of fedmsg.
# Copyright (C) 2012 Red Hat, Inc.
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
# Authors:  Ralph Bean <rbean@redhat.com>
#
""" Tests for planet messages """

import unittest

from fedmsg.tests.test_meta import Base

from .common import add_doc


class TestPlanetNewPost(Base):
    """ The `Fedora Planet <https://planet.fedoraproject.org/>`_ publishes
    messages of this topic whenever a new blog post is found.  Cool!
    """

    expected_title = "planet.post.new"
    expected_subti = 'ralph posted "Test Post 6"'
    expected_long_form = 'Test Post 6'
    expected_link = "http://threebean.org/blog/test-post-6"
    expected_icon = 'https://apps.fedoraproject.org/img/icons/planet_logo.png'
    expected_secondary_icon = ("https://secure.gravatar.com/avatar/"
                               "ba940b433c2695635d32d2c4aec00540?s=140")
    expected_packages = set([])
    expected_usernames = set(['ralph'])
    expected_objects = set(['threebean.org/blog/test-post-6'])
    msg = {
        "username": "planet-user",
        "i": 1,
        "timestamp": 1359579067.6178019,
        "topic": "org.fedoraproject.prod.planet.post.new",
        "msg": {
            "username": "ralph",
            "post": {
                "summary_detail": {
                    "base": "http://threebean.org/blog/category/"
                    "fedora/feed/index.xml",
                    "type": "text/html",
                    "value": "Test Post 6",
                    "language": None
                },
                "updated_parsed": 1359576000.0,
                "links": [
                    {
                        "href": "http://threebean.org/blog/test-post-6",
                        "type": "text/html",
                        "rel": "alternate"
                    }
                ],
                "tags": [
                    {
                        "term": "fedora",
                        "scheme": None,
                        "label": None
                    }
                ],
                "title": "Test Post 6",
                "updated": "Wed, 30 Jan 2013 15:00:00 EST",
                "summary": "Test Post 6",
                "content": [
                    {
                        "base": "http://threebean.org/blog/category/"
                        "fedora/feed/index.xml",
                        "type": "text/html",
                        "value": "<div class=\"document\">\n<p>Another "
                        "test post for fedmsg+fedoraplanet.</p>\n</div>",
                        "language": None
                    }
                ],
                "guidislink": False,
                "title_detail": {
                    "base": "http://threebean.org/blog/category/"
                    "fedora/feed/index.xml",
                    "type": "text/html",
                    "value": "Test Post 6",
                    "language": None
                },
                "link": "http://threebean.org/blog/test-post-6",
                "id": "http://threebean.org/blog/test-post-6"
            },
            "name": "Ralph Bean",
            "face": "https://secure.gravatar.com/avatar/"
            "ba940b433c2695635d32d2c4aec00540?s=140"
        }
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
