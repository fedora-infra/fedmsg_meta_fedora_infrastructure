# This file is part of fedmsg.
# Copyright (C) 2012-2015 Red Hat, Inc.
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
""" Tests for fedmsg.meta """

import unittest

from fedmsg_meta_fedora_infrastructure.tests.base import Base

from fedmsg_meta_fedora_infrastructure.tests.common import add_doc


class TestZanataMilestone(Base):
    """ Fedora uses `zanata <https://fedora.zanata.org>`_ for translations and
    they can ping us back when documents reach various milestones.  Here's
    an example of a document reaching 100% status:
    """
    expected_title = "zanata.document.milestone.event"
    expected_subti = "foo.txt from the webhooks-dummy project is now " + \
        "100% translated in the 'af' locale"
    expected_icon = 'https://pbs.twimg.com/profile_images/' + \
        '378800000417679469/47eb45c6205aa9f2cdb8705e6d46745c_normal.png'
    expected_secondary_icon = expected_icon
    expected_link = 'https://fedora.zanata.org/' + \
        'iteration/view/webhooks-dummy/0.1/languages/af'
    expected_usernames = set([])
    expected_packages = set([])
    expected_objects = set([
        'webhooks-dummy/0.1/languages/af',
    ])

    msg = {
        "i": 16,
        "msg": {
            "project": "webhooks-dummy",
            "version": "0.1",
            "docId": "foo.txt",
            "locale": "af",
            "milestone": "100% Translated",
            "eventType": "org.zanata.event.DocumentMilestoneEvent",
        },
        "topic": "org.fedoraproject.dev.zanata.document.milestone.event",
        "timestamp": 1345572862.556145
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
