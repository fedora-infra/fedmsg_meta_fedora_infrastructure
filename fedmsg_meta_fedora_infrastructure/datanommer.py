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
from fedmsg_meta_fedora_infrastructure import BaseProcessor


class DatanommerProcessor(BaseProcessor):
    __name__ = "datanommer"
    __description__ = "Exceptional Datanommer Events"
    __link__ = "https://github.com/fedora-infra/datanommer"
    __docs__ = "https://github.com/fedora-infra/datanommer"
    __obj__ = "Datanommer Events"

    def subtitle(self, msg, **config):
        return "datanommer encountered a duplicate uuid"

    def icon(self, msg, **config):
        return "https://i.imgur.com/4g9NZu1.png"

    def secondary_icon(self, msg, **config):
        return "https://i.imgur.com/58oJkOr.gif"

    def link(self, msg, **config):
        return "https://www.destroyallsoftware.com/talks/wat"

    def usernames(self, msg, **config):
        return set()

    def packages(self, msg, **config):
        return set()

    def objects(self, msg, **config):
        return set(['wat'])
