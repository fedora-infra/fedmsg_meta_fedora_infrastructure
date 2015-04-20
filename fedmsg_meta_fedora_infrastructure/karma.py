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
from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url


class KarmaProcessor(BaseProcessor):
    __name__ = "irc"
    __description__ = "IRC Karma"
    __link__ = "https://fedoraproject.org/wiki/Zodbot"
    __docs__ = "https://fedoraproject.org/wiki/Zodbot"
    __obj__ = "IRC Karma"
    __icon__ = "https://apps.fedoraproject.org/img/icons/meetbot.png"

    def subtitle(self, msg, **config):
        if msg['msg']['vote'] == 1:
            tmpl = self._('{agent} gave {recipient}({total}) '
                          'a karma cookie in {channel}')
        else:
            tmpl = self._('{agent} gave {recipient}({total}) '
                          'negative karma in {channel}')

        # Backwards compat
        if 'line' in msg['msg']:
            tmpl = tmpl + self._('.  "{line}"')

        return tmpl.format(**msg['msg'])

    def link(self, msg, **config):
        user = msg['msg']['recipient']
        return 'https://badges.fedoraproject.org/user/' + user

    def icon(self, msg, **config):
        return avatar_url(msg['msg']['agent'])

    def secondary_icon(self, msg, **config):
        return avatar_url(msg['msg']['recipient'])

    def usernames(self, msg, **config):
        return set([msg['msg']['agent'], msg['msg']['recipient']])

    def objects(self, msg, **config):
        return set(['karma/' + msg['msg']['recipient']])
