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

import requests

from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url
from fedmsg_meta_fedora_infrastructure import BaseProcessor


class GithubProcessor(BaseProcessor):
    __name__ = "github"
    __description__ = "Fedora-related Github Repos"
    __link__ = "https://github.com"
    __icon__ = "https://apps.fedoraproject.org/img/icons/github.png"
    __docs__ = "https://developer.github.com/webhooks/#events"
    __obj__ = "Github Events"

    def _get_user(self, msg):
        if msg['msg'].get('commit', None):
            user = msg['msg']['commit'].get('author')
            if user:
                user = user.get('login')
            if user:
                return msg['msg']['fas_usernames'].get(user, user)
        if msg['msg'].get('pusher', None):
            pusher = msg['msg']['pusher']['name']
            return msg['msg']['fas_usernames'].get(pusher, pusher)
        if msg['msg'].get('sender', None):
            sender = msg['msg']['sender']['login']
            return msg['msg']['fas_usernames'].get(sender, sender)
        if msg['msg'].get('forkee', None):
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
        if 'github.deployment_status' in msg['topic']:
            return msg['msg']['deployment_status']['target_url']
        if 'github.watch' in msg['topic']:
            return msg['msg']['repository']['html_url'] + "/watchers"
        if 'github.star' in msg['topic']:
            return msg['msg']['repository']['html_url'] + "/stargazers"
        if 'github.page_build' in msg['topic']:
            temp = msg['msg']['repository']['html_url'].split("/")
            return 'http://{0}.github.io/{1}/'.format(temp[-2],temp[-1])
        if 'release' in msg['msg']:
            return msg['msg']['release']['html_url']
        if 'target_url' in msg['msg']:
            return msg['msg']['target_url']
        if 'compare' in msg['msg']:
            return msg['msg']['compare']
        if 'comment' in msg['msg']:
            return msg['msg']['comment']['html_url']
        if 'review' in msg['msg']:
            return msg['msg']['review']['html_url']
        if 'pull_request' in msg['msg']:
            return msg['msg']['pull_request']['html_url']
        if 'issue' in msg['msg']:
            return msg['msg']['issue']['html_url']
        if 'forkee' in msg['msg']:
            return msg['msg']['forkee']['html_url']
        if 'repository' in msg['msg']:
            return msg['msg']['repository']['html_url']

    def long_form(self, msg, **config):
        if '.pull_request_review_comment' in msg['topic']:
            body = msg['msg']['comment']['body']
            return body
        if '.issue.comment' in msg['topic']:
            body = msg['msg']['comment']['body']
            return body
        if '.issue.reopened' in msg['topic']:
            body = msg['msg']['issue']['body']
            return body
        if 'commit_comment' in msg['topic']:
            body = msg['msg']['comment']['body']
            return body
        elif 'github.push' in msg['topic']:
            url = msg['msg']['compare'] + ".patch"
            response = requests.get(url)
            if response.status_code == 200:
                return response.text

    def lexer(self, msg, **config):
        if 'github.push' in msg['topic']:
            import pygments.lexers.diff
            return pygments.lexers.diff.DiffLexer()
        else:
            import pygments_markdown_lexer
            return pygments_markdown_lexer.MarkdownLexer()

    def subtitle(self, msg, **config):
        user = self._get_user(msg)
        repo = self._get_repo(msg)
        if 'github.webhook' in msg['topic']:
            return self._('A new github repository has been added to fedmsg')
        elif 'github.deployment_status' in msg['topic']:
            tmpl = self._('{user}\'s deployment status for {repo} '
                          'updated to "{status}"')
            status = msg['msg']['deployment_status']['state']
            return tmpl.format(user=user, repo=repo, status=status)
        elif 'github.push' in msg['topic']:
            n = len(msg['msg']['commits'])
            tmpl = self._('{user} pushed {n} commit(s) to {repo}')
            return tmpl.format(user=user, repo=repo, n=n)
        elif 'github.pull_request.' in msg['topic']:
            action = msg['msg']['action']
            if action == 'synchronize':
                action = 'synchronized'
            n = msg['msg']['number']
            if action == 'opened':
                title = msg['msg']['pull_request']['title']
                tmpl = self._(
                    '{user} {action} pull request #{n} on {repo}: {title}')
                return tmpl.format(
                    user=user,
                    action=action,
                    n=n,
                    repo=repo,
                    title=title)
            else:
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

            if action == 'opened':
                title = msg['msg']['issue']['title']
                tmpl = self._('{user} {action} issue #{n} on {repo}: {title}')
                return tmpl.format(
                    user=user,
                    action=action,
                    n=n,
                    repo=repo,
                    title=title)
            elif action == 'labeled':
                label = msg['msg']['label']['name']
                tmpl = self._('{user} added label {label} to issue #{n} on {repo}')
                return tmpl.format(
                    user=user,
                    label=label,
                    n=n,
                    repo=repo)
            else:
                tmpl = self._('{user} {action} issue #{n} on {repo}')
                return tmpl.format(user=user, action=action, n=n, repo=repo)
        elif ('github.pull_request_review' in msg['topic'] and
                'github.pull_request_review_comment' not in msg['topic']):
            n = msg['msg']['pull_request']['number']
            state = msg['msg']['review']['state']
            if state == 'pending':
                tmpl = self._('{user} commented on PR #{n} on {repo} which is '
                              'in {state} state')
            if state == 'approved':
                tmpl = self._('{user} {state} the changes on PR #{n} on '
                              '{repo}')
            if state == 'changes_requested':
                state = 'requested changes'
                tmpl = self._('{user} {state} on PR #{n} on {repo}')
            if state == 'commented':
                tmpl = self._('{user} {state} on PR #{n} on {repo}')
            return tmpl.format(user=user, n=n, repo=repo, state=state)
        elif 'github.pull_request_review_comment' in msg['topic']:
            n = msg['msg']['pull_request']['number']
            tmpl = self._('{user} commented on PR #{n} on {repo}')
            return tmpl.format(user=user, n=n, repo=repo)
        elif 'github.commit_comment' in msg['topic']:
            tmpl = self._('{user} commented on a commit on {repo}')
            return tmpl.format(user=user, repo=repo)
        elif 'github.create' in msg['topic']:
            typ = msg['msg']['ref_type']
            ref = msg['msg']['ref']
            tmpl = self._('{user} created a new {typ} "{ref}" at {repo}')
            return tmpl.format(user=user, repo=repo, ref=ref, typ=typ)
        elif 'github.delete' in msg['topic']:
            typ = msg['msg']['ref_type']
            ref = msg['msg']['ref']
            tmpl = self._('{user} deleted the "{ref}" {typ} at {repo}')
            return tmpl.format(user=user, repo=repo, ref=ref, typ=typ)
        elif 'github.fork' in msg['topic']:
            tmpl = self._('{user} forked {repo}')
            return tmpl.format(user=user, repo=repo)
        elif 'github.status' in msg['topic']:
            description = msg['msg']['description']
            sha = msg['msg']['sha'][:8]
            tmpl = self._("{description} for {repo} {sha}")
            return tmpl.format(description=description, repo=repo, sha=sha)
        elif 'github.watch' in msg['topic']:
            tmpl = self._('{user} {action} watching {repo}')
            action = msg['msg']['action']
            return tmpl.format(user=user, repo=repo, action=action)
        elif 'github.star' in msg['topic']:
            tmpl = self._('{user} {action} {repo}')
            action = msg['msg']['action']
            if action == 'started':
                action = 'starred'
            else:
                action = 'unstarred'
            return tmpl.format(user=user, repo=repo, action=action)
        elif 'github.release' in msg['topic']:
            tmpl = self._('{user} cut a release of {repo}, version {version}')
            version = msg['msg']['release']['tag_name']
            repo = repo.split('/', 1)[1]
            return tmpl.format(user=user, repo=repo, version=version)
        elif 'github.page_build' in msg['topic']:
            tmpl = self._('{user} rebuilt the github.io page for {repo}')
            return tmpl.format(user=user, repo=repo)
        elif 'github.team_add' in msg['topic']:
            tmpl = self._("The '{team_name}' team was added to the {repo} repository")
            teamName = msg['msg']['team']['slug']
            return tmpl.format(team_name=teamName,repo=repo)
        elif 'github.member' in msg['topic']:
            if msg['msg']['action'] == 'added':
                tmpl = self._("{user} added {member} as a member of {repo}")
            else:
                tmpl = self._("{user} removed member {member} from {repo}")
            member = msg['msg']['member']['login']
            return tmpl.format(user=user,member=member,repo=repo)
        else:
            pass

    def secondary_icon(self, msg, **config):
        if 'github.webhook' in msg['topic']:
            return self.icon(msg, **config)
        # Otherwise
        return avatar_url(self._get_user(msg))

    def usernames(self, msg, **config):
        return set([name for name in msg['msg']['fas_usernames'].values()
                    if not name.startswith('github_org_')])

    def objects(self, msg, **config):
        suffix = '.'.join(msg['topic'].split('.')[3:5])
        lookup = {
            'github.push': 'tree',
            'github.issue': 'issues',
            'github.fork': 'forks',
            'github.status': 'status',
            'github.pull_request': 'pull',
            'github.pull_request_review': 'pull',
            'github.pull_request_review_comment': 'pull',
            'github.commit_comment': 'tree',
            'github.release': 'releases',
            'github.create': None,
            'github.delete': None,
            'github.watch': None,
            'github.star': None,
            'github.page_build': 'page_build',
            'github.team_add': 'team_add',
            'github.member': 'member',
            'github.deployment_status': 'deployment_status',
        }

        if suffix not in lookup:
            return set()

        base = self._get_repo(msg)
        if lookup[suffix]:
            base = base + "/" + lookup[suffix]

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
        elif 'github.pull_request_review' in suffix:
            n = msg['msg']['pull_request']['number']
            items = ['%s' % n]
        elif suffix == 'github.fork':
            items = [self._get_user(msg)]
        elif suffix == 'github.create' or suffix == 'github.delete':
            items = ['/'.join([msg['msg']['ref_type'], msg['msg']['ref']])]
        elif suffix == 'github.status':
            items = [msg['msg']['commit']['sha']]
        elif suffix == 'github.commit_comment':
            items = [msg['msg']['comment']['path']]
        elif suffix == 'github.release':
            items = [msg['msg']['release']['tag_name']]
        elif suffix == 'github.watch':
            items = ['watchers']
        elif suffix == 'github.star':
            items = ['stargazers']
        if not items:
            return set([base])
        return set([base + '/' + item for item in items])
