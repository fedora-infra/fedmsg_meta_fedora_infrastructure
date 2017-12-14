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
# Authors:  Ralph Bean <rbean@redhat.com>
#
""" Tests for Greenwave messages """

import unittest

from fedmsg_meta_fedora_infrastructure.tests.base import Base

from .common import add_doc


class TestGreenwaveDecisionChange(Base):
    """ These messages are published by the `greenwave
    <http://fedoraproject.org/wiki/Infrastructure/Factory2/Focus/Greenwave>`_
    when some event causes it to change its decision about an artifacts.

    Here we have an example of a positive decision change on whether or not
    Bodhi should allow libmtp-1.1.14-1.fc27 to go to the stable repos.
    """
    expected_title = "greenwave.decision.update"
    expected_subti = "greenwave is a GO on libmtp-1.1.14-1.fc27 for " + \
        "\"bodhi_update_push_stable\" (fedora-27)"
    expected_link = "https://taskotron.fedoraproject.org/resultsdb/" + \
        "results?item=libmtp-1.1.14-1.fc27&type=koji_build"
    expected_icon = "https://apps.fedoraproject.org/img/icons/greenwave.png"
    expected_secondary_icon = ("https://apps.fedoraproject.org/packages/"
                               "images/icons/libmtp.png")
    expected_packages = set(['libmtp'])

    msg = {
        "i": 3,
        "username": "openshift",
        "timestamp": 1508872576.0,
        "msg_id": "2017-5ee197f3-dcc7-4cd6-af54-c5c448e0fe94",
        "crypto": "x509",
        "topic": "org.fedoraproject.prod.greenwave.decision.update",
        "msg": {
            "policies_satisified": True,
            "decision_context": "bodhi_update_push_stable",
            "product_version": "fedora-27",
            "applicable_policies": [
                "taskotron_release_critical_tasks_for_stable"
            ],
            "unsatisfied_requirements": [],
            "subject": [
                {
                    "item": "libmtp-1.1.14-1.fc27",
                    "type": "koji_build"
                }
            ],
            "summary": "all required tests passed",
            "previous": {
                "policies_satisified": False,
                "summary": "1 of 2 required tests not found",
                "unsatisfied_requirements": [
                    {
                        "testcase": "dist.upgradepath",
                        "item": {
                            "item": "libmtp-1.1.14-1.fc27",
                            "type": "koji_build"
                        },
                        "type": "test-result-missing"
                    }
                ],
                "applicable_policies": [
                    "taskotron_release_critical_tasks_for_stable"
                ]
            }
        }
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
