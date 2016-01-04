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
# Authors:  Martin Krizek <mkrizek@redhat.com>
#           Ralph Bean <rbean@redhat.com>

import logging

import requests

from fedmsg_meta_fedora_infrastructure import BaseProcessor

log = logging.getLogger('fedmsg.meta')


class TaskotronProcessor(BaseProcessor):
    __name__ = "taskotron"
    __description__ = "Framework for automated task execution"
    __link__ = "https://taskotron.fedoraproject.org/"
    __docs__ = "https://docs.qadevel.cloud.fedoraproject.org/libtaskotron/latest/"
    __obj__ = "Automated task results"
    __icon__ = "https://apps.fedoraproject.org/img/icons/taskotron.png"

    def subtitle(self, msg, **config):
        if msg['topic'].endswith('taskotron.result.new'):
            taskname = msg['msg']['task'].get('name', '')
            outcome = msg['msg']['result'].get('outcome', '')
            taskitem = msg['msg']['task'].get('item', '')
            return '%s %s for %s' % (taskname, outcome, taskitem)

    def link(self, msg, **config):
        if msg['topic'].endswith('taskotron.result.new'):
            return msg['msg']['result'].get('log_url', '')

    def objects(self, msg, **config):
        packages = self.packages(msg, **config)
        return set([
            '/'.join([
                msg['msg']['task'].get('name', ''),
                package,
                msg['msg']['result'].get('outcome', '')
            ])
            for package in packages
        ])

    def packages(self, msg, **config):
        type = msg['msg']['task']['type']
        if type == 'koji_build':
            nvr = msg['msg']['task']['item']
            name, version, release = nvr.rsplit('-', 2)
            return set([name])
        elif type == 'bodhi_update':
            alias = msg['msg']['task']['item']
            default_url = 'https://bodhi.fedoraproject.org'
            bodhi_url = config.get('bodhi_url', default_url)
            resp = requests.get(bodhi_url + '/updates/' + alias)
            if not bool(resp):
                log.warn("Failed to talk to bodhi %r %r" % (resp, resp.url))
                return set()
            data = resp.json()
            builds = data['update']['builds']
            nvrs = [build['nvr'] for build in builds]
            packages = [nvr.rsplit('-', 2)[0] for nvr in nvrs]
            return set(packages)

        log.warn('Unhandled taskotron type %r' % type)
        return set()

    def secondary_icon(self, msg, **config):
        packages = self.packages(msg, **config)
        if len(packages) != 1:
            # If it is 0 or greater than 1, just use the taskotron icon.
            return self.__icon__
        else:
            url = 'https://apps.fedoraproject.org/packages/images/icons/%s.png'
            package = list(packages)[0]
            return url % package
