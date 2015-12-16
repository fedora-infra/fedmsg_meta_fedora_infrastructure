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
# Authors:  Ralph Bean <rbean@redhat.com>

from fedmsg_meta_fedora_infrastructure import BaseProcessor
from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url


class NagiosProcessor(BaseProcessor):
    __name__ = "Nagios"
    __description__ = "Fedora Infra Service Monitoring"
    __link__ = "https://admin.fedoraproject.org/nagios"
    __docs__ = "https://infrastructure.fedoraproject.org/infra/docs/nagios.rst"
    __obj__ = "Service Outage Alerts"
    __icon__ = "https://apps.fedoraproject.org/img/icons/nagios-logo.png"

    def subtitle(self, msg, **config):
        states = {
            'CRITICAL': self._('down'),
            'WARNING': self._('having problems'),
            'OK': self._('back up'),
        }
        state = msg['msg']['state']
        state = states.get(state, self._('in an unknown state'))
        host = msg['msg']['host']

        result = None
        if msg['topic'].endswith('host.state.change'):
            tmpl = self._('{host} is {state}')
            result = tmpl.format(host=host, state=state)
        elif msg['topic'].endswith('service.state.change'):
            service = msg['msg'].get('service', 'some service')
            tmpl = self._('{service} is {state} on {host}')
            result = tmpl.format(service=service, host=host, state=state)

        if msg['msg']['type'] == 'ACKNOWLEDGEMENT':
            users = self.usernames(msg, **config)
            agent = 'somebody'
            if users:
                agent = list(users)[0]
            prefix = self._('{agent} acknowledged that ').format(agent=agent)
            result = prefix + result

        if result and 'output' in msg['msg']:
            result += ': "{output}"'.format(output=msg['msg']['output'])

        return result

    def link(self, msg, **config):
        base = 'https://admin.fedoraproject.org/nagios/cgi-bin/status.cgi'
        query = '?navbarsearch=1&host='
        host = msg['msg']['host']
        return base + query + host

    def secondary_icon(self, msg, **config):
        users = self.usernames(msg, **config)
        if users:
            return avatar_url(list(users)[0])
        return self.__icon__

    def usernames(self, msg, **config):
        users = set()
        service_ack = msg['msg']['service_ack_author']
        if service_ack:
            users.add(service_ack.split('://')[-1].split('.')[0])

        host_ack = msg['msg']['host_ack_author']
        if host_ack:
            users.add(host_ack.split('://')[-1].split('.')[0])

        return users

    def objects(self, msg, **config):
        host = msg['msg']['host']
        service = msg['msg'].get('service', 'unknown')
        if msg['topic'].endswith('host.state.change'):
            service = 'state'
        return set([
            '/'.join([host, service]),
        ])
