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

from fedmsg_meta_fedora_infrastructure import BaseProcessor

_long_template = """Packages: {components}
Function: {function}
First occurrence: {first_occurrence}
Type:     {type}
Count:    {count}
URL:      {url}
"""


class FAFProcessor(BaseProcessor):
    __name__ = "faf"
    __description__ = "ABRT crash analysis server"
    __link__ = "https://retrace.fedoraproject.org"
    __obj__ = "New and significant crashes"
    __docs__ = "https://github.com/abrt/faf/wiki"
    __icon__ = "https://apps.fedoraproject.org/packages/images/icons/abrt.png"

    def long_form(self, msg, **config):
        return _long_template.format(**{
            "components": ", ".join(msg["msg"].get("components", [])),
            "first_occurrence": msg["msg"].get("first_occurrence"),
            "function": msg["msg"].get("function"),
            "type": msg["msg"].get("type"),
            "count": msg["msg"].get("count"),
            "url": msg["msg"].get("url"),
            })

    def subtitle(self, msg, **config):
        obj_name = "report"
        if "problem.threshold" in msg["topic"]:
            obj_name = "problem"
        return ("ABRT {0} for package {1} has reached {2} occurrences"
                .format(obj_name, ", ".join(msg["msg"].get("components", [])),
                        msg["msg"].get("count")))

    def link(self, msg, **config):
        return msg["msg"].get("url")

    def usernames(self, msg, **config):
        return set(msg["msg"].get("maintainers", []))

    def packages(self, msg, **config):
        return set(msg["msg"].get("components", []))

    def secondary_icon(self, msg, **config):
        pkgs = msg["msg"].get("components", [])
        if not pkgs:
            return None
        return ("https://apps.fedoraproject.org/packages/images/icons/{0}.png"
                .format(pkgs[0]))
