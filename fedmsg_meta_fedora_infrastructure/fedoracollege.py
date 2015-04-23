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
# Authors:  Hammad Haleem <hammadhaleem@gmail.com>
'''Preprocessor for fedora college'''

from fedmsg_meta_fedora_infrastructure import BaseProcessor
from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url


class FedoraCollegeProcessor(BaseProcessor):
    __name__ = "FedoraCollege"
    __description__ = "The virtual Classroom for new fedora contributors"
    __obj__ = "Delivering video tutorials"

    '''
    currently not in production
    __link__ = "https://ask.fedoraproject.org"
    __docs__ = "https://askbot.com"
    __icon__ = "https://apps.fedoraproject.org/img/icons/ask_fedora.png"
    '''

    def subtitle(self, msg, **config):

        username = msg['msg']['username']
        title = msg['msg']['title']

        if "fedoracollege.media.upload" in msg['topic']:
            tmpl = self._(
                '{username} uploaded a new file of type "{title}"')
        elif "fedoracollege.content.added" in msg['topic']:
            tmpl = self._(
                '{username} Created new content titled "{title}"')
        elif "fedoracollege.content.edit" in msg['topic']:
            tmpl = self._(
                '{username} Edited content titled "{title}"')
        else:
            raise NotImplementedError("%r" % msg)

        return tmpl.format(username=username, title=title)

    def secondary_icon(self, msg, **config):
        user = None

        try:
            user = msg['msg']['username']
        except KeyError:
            pass

        if not user:
            return ""

        return avatar_url(username=user)

    def usernames(self, msg, **config):
        if 'username' in msg['msg']:
            return set([msg['msg']['username']])

        return set()

    def link(self, msg, **config):
        return msg['msg']['link']
