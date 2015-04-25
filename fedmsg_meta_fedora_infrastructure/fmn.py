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
# Authors:  Ralph Bean <rbean@redhat.com>

import six

from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url
from fedmsg_meta_fedora_infrastructure import BaseProcessor


class FMNProcessor(BaseProcessor):
    __name__ = "FMN"
    __description__ = "the Fedora Notifications System"
    __link__ = "https://apps.fedoraproject.org/notifications/"
    __icon__ = "https://apps.fedoraproject.org/img/icons/fedmsg.png"
    __docs__ = "https://github.com/fedora-infra/fmn"
    __obj__ = "Notification Preference Updates"

    def subtitle(self, msg, **config):
        kwargs = dict(
            user=self.username(msg),
            ctx=msg['msg']['context'],
            obj=msg['topic'].split('.')[-2],
            changed=msg['msg']['changed'],
        )

        if 'fmn.confirmation.update' in msg['topic']:
            tmpl = self._("the {changed} of one of {user}'s "
                          "pending confirmations changed")
        elif 'fmn.rule.update' in msg['topic']:
            tmpl = self._("{user} updated the {changed} on a fmn {ctx} rule")
        elif 'fmn.filter.update' in msg['topic']:
            tmpl = self._("{user} updated the {changed} on a fmn {ctx} filter")
        elif 'fmn.preference.update' in msg['topic']:
            if 'enabled' == kwargs['changed']:
                tmpl = self._("{user} toggled their flow of {ctx} messages")
            else:
                swaps = {
                    'batch_values': self._('digest options'),
                    'details': self._('delivery details'),
                }
                changed = kwargs['changed']
                kwargs['changed'] = swaps.get(changed, changed)
                tmpl = self._("{user} updated their {ctx} {changed}")
        else:
            tmpl = ''

        return tmpl.format(**kwargs)

    def link(self, msg, **config):
        return self.__link__

    def secondary_icon(self, msg, **config):
        return avatar_url(self.username(msg))

    def usernames(self, msg, **config):
        return set([self.username(msg)])

    def username(self, msg):
        return msg['msg']['openid'].split('.')[0]

    def objects(self, msg, **config):
        user = self.username(msg)
        ctx = msg['msg']['context']
        obj = msg['topic'].split('.')[-2]
        changed = msg['msg']['changed']
        tokens = [user, ctx, obj, changed]
        return set(['/'.join(map(six.text_type, tokens))])
