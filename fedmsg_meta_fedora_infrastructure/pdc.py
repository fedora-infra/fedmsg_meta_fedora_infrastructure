# This file is part of fedmsg.
# Copyright (C) 2016 Red Hat, Inc.
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


class PDCProcessor(BaseProcessor):
    __name__ = "pdc"
    __description__ = "Product Definition Center"
    __link__ = "https://github.com/product-definition-center/product-definition-center"
    __docs__ = "https://github.com/product-definition-center/product-definition-center"
    __obj__ = "PDC Composes"

    def subtitle(self, msg, **config):
        tmpl = self._('Unhandled PDC message...')
        if msg['topic'].endswith('.pdc.rpms') or msg['topic'].endswith('.pdc.images'):
            tmpl = self._(
                'PDC imported metadata for {count} {attribute} for '
                'the {compose_id} {compose_type} compose'
            )
        elif msg['topic'].endswith('.pdc.compose'):
            tmpl = self._(
                'An entry for the {compose_id} {compose_type} compose '
                'was created in the Product Definition Center'
            )

        return tmpl.format(**msg['msg'])

    def link(self, msg, **config):
        idx = msg['msg']['compose_id']
        tmpl = 'https://pdc.fedoraproject.org/rest_api/v1/composes/{idx}/'
        return tmpl.format(idx=idx)

    def objects(self, msg, **config):
        attr = msg['topic'].split('.')[-1]
        return set([
            "{compose_id}/{action}/{attr}".format(attr=attr, **msg['msg'])
        ])
