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
# Authors:  Marek Brysa <mbrysa@redhat.com>
#
""" Tests for FAF (ABRT server) messages """

import unittest

from fedmsg.tests.test_meta import Base

from .common import add_doc


class TestFAFReport1(Base):
    """ `ABRT server <https://retrace.fedoraproject.org/>`_ notifies about a crash report
    """
    expected_title = "faf.report.threshold1"
    expected_subti = "ABRT report for package evolution has reached 7 occurrences"
    expected_packages = set(["evolution"])
    expected_usernames = set()
    expected_objects = set()
    expected_link = "http://example.org/faf/reports/1234/"
    expected_secondary_icon = "https://apps.fedoraproject.org/packages/images/icons/evolution.png"
    expected_long_form = """Packages: evolution
Function: main
First occurrence: 2015-04-10
Type:     core
Count:    7
URL:      http://example.org/faf/reports/1234/
"""
    msg = {
        u"username": u"faf",
        u"i": 1,
        u"timestamp": 1429777247,
        u"msg_id": u"2015-0284a675-995a-4942-bc59-2a5384e892b7",
        u"topic": u"org.fedoraproject.prod.faf.report.threshold1",
        u"msg": {
            u"count": 7,
            u"function": u"main",
            u"level": 1,
            u"url": u"http://example.org/faf/reports/1234/",
            u"components": [u"evolution"],
            u"type": u"core",
            u"first_occurrence": u"2015-04-10",
            u"report_id": 1234,
            u"problem_id": 4321
            }
        }


class TestFAFProblem10(Base):
    """ `ABRT server <https://retrace.fedoraproject.org/>`_ notifies about a problem
    """
    expected_title = "faf.problem.threshold10"
    expected_subti = "ABRT problem for package evolution, thunderbird has reached 77 occurrences"
    expected_packages = set(["evolution", "thunderbird"])
    expected_usernames = set()
    expected_objects = set()
    expected_link = "http://example.org/faf/problems/4321/"
    expected_secondary_icon = "https://apps.fedoraproject.org/packages/images/icons/evolution.png"
    expected_long_form = """Packages: evolution, thunderbird
Function: main
First occurrence: 2015-04-10
Type:     core
Count:    77
URL:      http://example.org/faf/problems/4321/
"""
    msg = {
        u"username": u"faf",
        u"i": 1,
        u"timestamp": 1429777247,
        u"msg_id": u"2015-0284a675-995a-4942-bc59-2a5384e892b7",
        u"topic": u"org.fedoraproject.prod.faf.problem.threshold10",
        u"msg": {
            u"count": 77,
            u"function": u"main",
            u"level": 1,
            u"url": u"http://example.org/faf/problems/4321/",
            u"components": [u"evolution", u"thunderbird"],
            u"type": u"core",
            u"first_occurrence": u"2015-04-10",
            u"problem_id": 4321
            }
        }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
