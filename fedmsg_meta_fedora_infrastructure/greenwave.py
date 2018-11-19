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

from six.moves.urllib.parse import urlencode
from fedmsg_meta_fedora_infrastructure import BaseProcessor


class GreenwaveProcessor(BaseProcessor):
    __name__ = "greenwave"
    __description__ = "Greenwave Gating Service"
    __link__ = "greenwave-web-greenwave.app.os.fedoraproject.org/api/v1.0/policies"
    __docs__ = "https://fedoraproject.org/wiki/Infrastructure/Factory2/Focus/Greenwave"
    __obj__ = "Gating Decisions"
    __icon__ = "https://apps.fedoraproject.org/img/icons/greenwave.png"

    @staticmethod
    def satisfied(msg):
        try:
            # https://pagure.io/greenwave/pull-request/100
            return msg['msg']['policies_satisfied']
        except KeyError:
            return msg['msg']['policies_satisified']

    def link(self, msg, **config):
        subject = msg['msg']['subject']
        if subject:
            base = "https://taskotron.fedoraproject.org/resultsdb/results"
            query = urlencode(sorted(subject[0].items()))
            return base + "?" + query

    def subtitle(self, msg, **config):
        if self.satisfied(msg):
            decision = self._("is a GO")
        else:
            decision = self._("says NO-GO")

        tmpl = self._(
            "greenwave {decision} on {item} for "
            "\"{decision_context}\" ({product_version})"
        )
        msg_body = msg['msg']
        item = msg_body.get('subject_identifier')
        if not item:
            subject = msg_body['subject']
            items = [entry.get('item') for entry in subject if entry.get('item')]
            item = items[0] if items else "\"something\""
        return tmpl.format(decision=decision, item=item, **msg['msg'])

    def secondary_icon(self, msg, **config):
        packages = self.packages(msg, **config)
        if packages:
            primary = sorted(packages)[0]
            base = 'https://apps.fedoraproject.org/packages/images/icons/'
            return base + primary + '.png'

    def packages(self, msg, **config):
        subject = msg['msg']['subject']
        items = [
            entry.get('item') for entry in subject
            if entry.get('item') and entry.get('type') == 'koji_build'
        ]
        return set([item.rsplit('-', 2)[0] for item in items])
