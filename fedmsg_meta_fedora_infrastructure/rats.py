# This file is part of fedmsg.
# Copyright (C) 2018 Red Hat, Inc.
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
# Authors:  Pierre-Yves Chibon <pingou@pingoured.fr>
#

from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url, email2fas
from fedmsg_meta_fedora_infrastructure import BaseProcessor
from fedmsg_meta_fedora_infrastructure.pagure import (
    _get_project, DistGitPagureProcessor)


import fedmsg.meta.base


class RatsProcessor(BaseProcessor):
    topic_prefix_re = 'org\\.fedoraproject\\.(dev|stg|prod)'

    __name__ = "rats"
    __description__ = "Run Another Test System"
    __link__ = "https://pagure.io/rats"
    __docs__ = "https://pagure.io/rats"
    __obj__ = "RATS"
    __icon__ = ("https://apps.fedoraproject.org/packages/"
                "images/icons/package_128x128.png")

    def link(self, msg, **config):
        if 'test.simple-koji-ci' in msg['topic']:
            msg2 = msg.copy()
            msg2['topic'] = msg2['topic'].replace(
                'rats.test.simple-koji-ci', 'pagure.pull-request.new')
            msg2['msg']['pullrequest'] = msg2['msg']['pull_request']
            return DistGitPagureProcessor(self._, **config).link(msg2, **config)

    def subtitle(self, msg, **config):
        user = msg['msg'].get('agent')

        if 'test.simple-koji-ci' in msg['topic']:
            project = _get_project(msg['msg']['pull_request'])
            prid = prid = msg['msg']['pull_request']['id']
            tmpl = self._(
                '{user} requested a run of simple-koji-ci on '
                '"{project}/pull-request/{prid}"'
            )
            return tmpl.format(user=user, project=project, prid=prid)

        elif 'test.taskotron' in msg['topic']:
            test = msg['msg']['test']
            target = msg['msg']['identifier']
            rdbid = msg['msg']['result_id']
            if target:
                tmpl = self._(
                    '{user} requested a run of taskotron\'s {test} on '
                    '"{target}"'
                )
            else:
                tmpl = self._(
                    '{user} requested a run of taskotron on '
                    'resultsdb\'s result id: "{rdbid}"'
                )
            return tmpl.format(
                user=user, test=test, target=target, rdbid=rdbid)

        elif 'test.atomic-ci' in msg['topic']:
            test = msg['msg']['test']
            target = msg['msg']['identifier']
            rdbid = msg['msg']['result_id']
            if target:
                tmpl = self._(
                    '{user} requested a run of atomic-ci on '
                    '"{target}"'
                )
            else:
                tmpl = self._(
                    '{user} requested a run of atomic-ci on '
                    'resultsdb\'s result id: "{rdbid}"'
                )
            return tmpl.format(
                user=user, test=test, target=target, rdbid=rdbid)

    def secondary_icon(self, msg, **config):
        username = msg['msg'].get('agent')
        if username:
            return avatar_url(username)

    def usernames(self, msg, **config):
        username = msg['msg'].get('agent')
        if username:
            return set([username])
        else:
            return set([])

    def objects(self, msg, **config):
        if 'test.simple-koji-ci' in msg['topic']:
            project = _get_project(msg['msg']['pull_request']).strip()
            prid = msg['msg']['pull_request']['id']
            return set([
                'simple-koji-ci/%s/pull-request/%s' % (project, prid)
            ])
        elif 'test.taskotron' in msg['topic']:
            test = msg['msg']['test']
            target = msg['msg']['identifier']
            rdbid = msg['msg']['result_id']
            if target:
                return set([
                    'taskotron/%s/%s' % (test, target)
                ])
            else:
                return set([
                    'taskotron/resultsdb/%s' % (rdbid)
                ])

        elif 'test.atomic-ci' in msg['topic']:
            test = msg['msg']['test']
            target = msg['msg']['identifier']
            rdbid = msg['msg']['result_id']
            if target:
                return set([
                    'AtomicCI/%s' % (target)
                ])
            else:
                return set([
                    'AtomicCI/resultsdb/%s' % (rdbid)
                ])

        return set([])
