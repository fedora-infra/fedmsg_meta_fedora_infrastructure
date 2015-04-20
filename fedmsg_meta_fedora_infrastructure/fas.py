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
import six

from fedmsg_meta_fedora_infrastructure import BaseProcessor
from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url


def string_or_dict(msg, key):
    if isinstance(msg[key], six.text_type):
        return msg[key]
    else:
        if 'username' in msg[key]:
            return msg[key]['username']
        else:
            return msg[key]['name']


class FASProcessor(BaseProcessor):
    __name__ = "FAS"
    __description__ = "the Fedora Account System"
    __link__ = "https://admin.fedoraproject.org/accounts"
    __docs__ = "https://fedoraproject.org/wiki/Account_System"
    __obj__ = "Account Changes"
    __icon__ = ("https://admin.fedoraproject.org/accounts/static/"
                "theme/fas/images/account.png")

    def subtitle(self, msg, **config):
        if 'fas.user.create' in msg['topic']:
            agent = string_or_dict(msg['msg'], 'agent')
            user = string_or_dict(msg['msg'], 'user')
            tmpl = self._(
                "New FAS account:  '{user}'  (created by '{agent}')"
            )
            return tmpl.format(agent=agent, user=user)
        elif 'fas.user.update' in msg['topic']:
            agent = string_or_dict(msg['msg'], 'agent')
            user = string_or_dict(msg['msg'], 'user')
            fields = ", ".join(msg['msg']['fields'])
            tmpl = self._(
                "{agent} edited the following fields of " +
                "{user}'s FAS profile:  {fields}"
            )
            return tmpl.format(agent=agent, user=user, fields=fields)
        elif 'fas.group.member.' in msg['topic']:
            action = msg['topic'].split('.')[-1]
            agent = string_or_dict(msg['msg'], 'agent')
            user = string_or_dict(msg['msg'], 'user')
            group = string_or_dict(msg['msg'], 'group')
            tmpls = {
                'apply': self._(
                    "{agent} applied for {user}'s membership " +
                    "in the {group} group"
                ),
                'sponsor': self._(
                    "{agent} sponsored {user}'s membership " +
                    "in the {group} group"
                ),
                'remove': self._(
                    "{agent} removed {user} from " +
                    "the {group} group"
                ),
            }
            tmpl = tmpls.get(action, self._(
                '<unhandled action in fedmsg.meta.fas>'
            ))
            return tmpl.format(agent=agent, user=user, group=group)
        elif 'fas.group.create' in msg['topic']:
            agent = string_or_dict(msg['msg'], 'agent')
            group = string_or_dict(msg['msg'], 'group')
            tmpl = self._("{agent} created new FAS group {group}")
            return tmpl.format(agent=agent, group=group)
        elif 'fas.group.update' in msg['topic']:
            agent = string_or_dict(msg['msg'], 'agent')
            group = string_or_dict(msg['msg'], 'group')
            fields = ", ".join(msg['msg']['fields'])
            tmpl = self._(
                "{agent} edited the following fields of the {group} " +
                "FAS group:  {fields}"
            )
            return tmpl.format(agent=agent, group=group, fields=fields)
        elif 'fas.role.update' in msg['topic']:
            tmpl = self._(
                "{agent} changed {user}'s role in the {group} group"
            )
            agent = string_or_dict(msg['msg'], 'agent')
            user = string_or_dict(msg['msg'], 'user')
            group = string_or_dict(msg['msg'], 'group')
            if 'status' in msg['msg']:
                status = string_or_dict(msg['msg'], 'status')
                tmpl += self._(' to {status}')
            else:
                status = None
            return tmpl.format(agent=agent,
                               group=group,
                               user=user,
                               status=status)
        else:
            raise NotImplementedError("%r" % msg)

    def secondary_icon(self, msg, **config):
        # Every fas fedmsg message has an "agent" field.. "whodunnit"
        return avatar_url(username=string_or_dict(msg['msg'], 'agent'))

    def usernames(self, msg, **config):
        users = []

        try:
            users.append(string_or_dict(msg['msg'], 'agent'))
        except KeyError:
            pass

        try:
            users.append(string_or_dict(msg['msg'], 'user'))
        except KeyError:
            pass

        return set(users)

    def objects(self, msg, **config):
        objs = set()

        if 'user' in msg['msg']:
            objs.add('users/' + string_or_dict(msg['msg'], 'user'))

        if 'group' in msg['msg']:
            objs.add('groups/' + string_or_dict(msg['msg'], 'group'))

        return objs
