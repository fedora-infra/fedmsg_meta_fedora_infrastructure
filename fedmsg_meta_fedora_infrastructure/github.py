# This file is part of fedmsg.
# Copyright (C) 2012-2014 Red Hat, Inc.
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

from fasshim import gravatar_url
from fedmsg_meta_fedora_infrastructure import BaseProcessor


class GithubProcessor(BaseProcessor):
    __name__ = "github"
    __description__ = "Fedora-related Github Repos"
    __link__ = "https://github.com"
    __icon__ = "https://apps.fedoraproject.org/img/icons/github.png"
    __docs__ = "http://developer.github.com/webhooks/#events"
    __obj__ = "Github Events"

    def _get_user(self, msg):
        if 'pusher' in msg['msg']:
            pusher = msg['msg']['pusher']['name']
            return msg['msg']['fas_usernames'].get(pusher, pusher)
        if 'sender' in msg['msg']:
            sender = msg['msg']['sender']['login']
            return msg['msg']['fas_usernames'].get(sender, sender)
        if 'forkee' in msg['msg']:
            forkee = msg['msg']['forkee']['owner']['login']
            return msg['msg']['fas_usernames'].get(forkee, forkee)
        return None

    def _get_repo(self, msg):
        try:
            repo = msg['msg']['repository']
            if 'login' in repo['owner']:
                return repo['owner']['login'] + '/' + repo['name']
            else:
                return repo['owner']['name'] + '/' + repo['name']

        except KeyError:
            return None

    def link(self, msg, **config):
        if 'compare' in msg['msg']:
            return msg['msg']['compare']
        if 'pull_request' in msg['msg']:
            return msg['msg']['pull_request']['html_url']
        if 'comment' in msg['msg']:
            return msg['msg']['comment']['html_url']
        if 'issue' in msg['msg']:
            return msg['msg']['issue']['html_url']
        if 'forkee' in msg['msg']:
            return msg['msg']['forkee']['html_url']
        if 'repository' in msg['msg']:
            return msg['msg']['repository']['html_url']

    def subtitle(self, msg, **config):
        user = self._get_user(msg)
        repo = self._get_repo(msg)
        if 'github.webhook' in msg['topic']:
            return self._('A new github repository has been added to fedmsg')
        elif 'github.push' in msg['topic']:
            n = len(msg['msg']['commits'])
            tmpl = self._('{user} pushed {n} commit(s) to {repo}')
            return tmpl.format(user=user, repo=repo, n=n)
        elif 'github.pull_request.' in msg['topic']:
            action = msg['msg']['action']
            n = msg['msg']['number']
            tmpl = self._('{user} {action} pull request #{n} on {repo}')
            return tmpl.format(user=user, action=action, n=n, repo=repo)
        elif 'github.issue.' in msg['topic']:
            if 'comment' in msg['msg']:
                action = 'commented on'
            else:
                action = msg['msg']['action']

            try:
                n = msg['msg']['number']
            except KeyError:
                n = msg['msg']['issue']['number']

            tmpl = self._('{user} {action} issue #{n} on {repo}')
            return tmpl.format(user=user, action=action, n=n, repo=repo)
        elif 'github.create' in msg['topic']:
            typ = msg['msg']['ref_type']
            ref = msg['msg']['ref']
            tmpl = self._('{user} created a new {typ} "{ref}" at {repo}')
            return tmpl.format(user=user, repo=repo, ref=ref, typ=typ)
        elif 'github.fork' in msg['topic']:
            tmpl = self._('{user} forked {repo}')
            return tmpl.format(user=user, repo=repo)
        else:
            pass

    def secondary_icon(self, msg, **config):
        if 'github.webhook' in msg['topic']:
            return self.icon(msg, **config)
        # Otherwise
        return gravatar_url(self._get_user(msg))

    def usernames(self, msg, **config):
        return set(msg['msg']['fas_usernames'].values())

    def objects(self, msg, **config):
        suffix = '.'.join(msg['topic'].split('.')[3:5])
        lookup = {
            'github.push': 'git',
            'github.pull_request': 'pull_request',
            'github.issue': 'issue',
            'github.fork': 'forks',
            'github.create': 'create',
        }

        if suffix not in lookup:
            return set()

        base = lookup[suffix] + '/' + self._get_repo(msg)

        items = []
        if 'commits' in msg['msg']:
            for c in msg['msg']['commits']:
                items = c['added'] + c['removed'] + c['modified']
        elif suffix == 'github.pull_request':
            items = ['%s' % msg['msg']['number']]
        elif suffix == 'github.issue':
            try:
                n = msg['msg']['number']
            except KeyError:
                n = msg['msg']['issue']['number']
            items = ['%s' % n]
        elif suffix == 'github.fork':
            items = [self._get_user(msg)]
        elif suffix == 'github.create':
            items = ['/'.join([msg['msg']['ref_type'], msg['msg']['ref']])]

        return set([base + '/' + item for item in items])
