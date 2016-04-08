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
#
from fedmsg_meta_fedora_infrastructure import BaseProcessor
from fedmsg_meta_fedora_infrastructure.fasshim import \
        avatar_url, avatar_url_from_email

import requests


already_seen_msg = "This commit already existed in another branch."


class SCMProcessor(BaseProcessor):
    __name__ = "git"
    __description__ = "the Fedora version control system"
    __link__ = "http://pkgs.fedoraproject.org/cgit"
    __docs__ = "https://fedoraproject.org/wiki/Using_Fedora_GIT"
    __obj__ = "Package Commits"
    __icon__ = "https://apps.fedoraproject.org/img/icons/git-logo.png"

    def secondary_icon(self, msg, **config):
        if '.git.receive' in msg['topic']:
            if 'username' in msg['msg']['commit']:
                username = msg['msg']['commit']['username']
                return avatar_url(username)
            email = msg['msg']['commit']['email']
            return avatar_url_from_email(email)
        elif '.git.lookaside' in msg['topic']:
            username = msg['msg']['agent']
            return avatar_url(username)
        elif 'agent' in msg['msg']:
            username = msg['msg']['agent']
            return avatar_url(username)

    def long_form(self, msg, **config):
        if '.git.receive' in msg['topic']:
            try:
                repo = msg['msg']['commit']['repo']
            except KeyError:
                repo = '.'.join(msg['topic'].split('.')[5:-1])

            rev = msg['msg']['commit']['rev']

            seen = msg['msg']['commit'].get('seen', False)
            if seen:
                return already_seen_msg

            url = 'http://pkgs.fedoraproject.org/cgit/' + \
                '{repo}.git/patch/?id={rev}'
            response = requests.get(url.format(repo=repo, rev=rev))
            if response.status_code == 200:
                return response.text
        elif '.git.lookaside' in msg['topic']:
            filename = msg['msg']['filename']
            xsum = msg['msg']['md5sum']
            tmpl = self._("{xsum}  {filename}")
            return tmpl.format(xsum=xsum, filename=filename)

    def lexer(self, msg, **config):
        if '.git.receive' in msg['topic']:
            import pygments.lexers.diff
            return pygments.lexers.diff.DiffLexer()

    def subtitle(self, msg, **config):
        if '.git.receive' in msg['topic']:
            try:
                repo = msg['msg']['commit']['repo']
            except KeyError:
                repo = '.'.join(msg['topic'].split('.')[5:-1])

            try:
                user = msg['msg']['commit']['username']
            except KeyError:
                user = msg['msg']['commit']['email']

            summ = msg['msg']['commit']['summary']
            whole = msg['msg']['commit']['message']
            if summ.strip() != whole.strip():
                summ += " (..more)"

            branch = msg['msg']['commit']['branch']
            tmpl = self._('{user} pushed to {repo} ({branch}).  "{summary}"')
            return tmpl.format(user=user, repo=repo,
                               branch=branch, summary=summ)
        elif '.git.branch' in msg['topic']:
            try:
                repo = msg['msg']['name']
                branch = msg['msg']['branch']
            except KeyError:
                repo = '.'.join(msg['topic'].split('.')[5:-1])
                branch = msg['topic'].split('.')[-1]

            try:
                repo = msg['msg']['namespace'] + '/' + repo
            except KeyError:
                pass

            agent = msg['msg']['agent']
            tmpl = self._(
                "{agent} created branch '{branch}' for the '{repo}' package"
            )
            return tmpl.format(agent=agent, branch=branch, repo=repo)
        elif '.git.lookaside' in msg['topic']:
            name = msg['msg']['name']
            agent = msg['msg']['agent']
            filename = msg['msg']['filename']
            tmpl = self._(
                "{agent} uploaded {filename} for {name}"
            )
            return tmpl.format(agent=agent, name=name, filename=filename)
        elif '.git.mass_branch.start' in msg['topic']:
            tmpl = self._('{agent} started a mass branch')
        elif '.git.mass_branch.complete' in msg['topic']:
            tmpl = self._('mass branch started by {agent} completed')
        elif '.git.pkgdb2branch.start' in msg['topic']:
            tmpl = self._('{agent} started a run of pkgdb2branch')
        elif '.git.pkgdb2branch.complete' in msg['topic']:
            errors = len(msg['msg'].get('unbranchedPackages') or [])
            if errors == 0:
                tmpl = self._(
                    'run of pkgdb2branch started by {agent} completed')
            elif errors == 1:
                tmpl = self._(
                    'run of pkgdb2branch started by {agent} completed' +
                    ' with 1 error'
                )
            else:
                tmpl = self._(
                    'run of pkgdb2branch started by {agent} completed' +
                    ' with %i errors'
                ) % errors

        agent = msg['msg'].get('agent', '(somebody)')
        return tmpl.format(agent=agent)

    def link(self, msg, **config):
        prefix = "http://pkgs.fedoraproject.org/cgit"
        if '.git.receive' in msg['topic']:
            try:
                repo = msg['msg']['commit']['repo']
            except KeyError:
                repo = '.'.join(msg['topic'].split('.')[5:-1])
            rev = msg['msg']['commit']['rev']
            branch = msg['msg']['commit']['branch']
            tmpl = "{prefix}/{repo}.git/commit/?h={branch}&id={rev}"
            return tmpl.format(prefix=prefix, repo=repo,
                               branch=branch, rev=rev)
        elif '.git.branch' in msg['topic']:
            try:
                repo = msg['msg']['name']
                branch = msg['msg']['branch']
            except KeyError:
                repo = '.'.join(msg['topic'].split('.')[5:-1])
                branch = msg['topic'].split('.')[-1]
            try:
                ns = msg['msg']['namespace'] + '/'
            except KeyError:
                ns = ''
            tmpl = "{prefix}/{ns}{repo}.git/log/?h={branch}"
            return tmpl.format(prefix=prefix, repo=repo, branch=branch, ns=ns)
        elif '.git.lookaside' in msg['topic']:
            prefix = "http://pkgs.fedoraproject.org/lookaside/pkgs"

            if 'path' in msg['msg']:
                path = msg['msg']['path']

            else:
                # Fallback to the old message format from the dark ages of MD5
                name = msg['msg']['name']
                md5sum = msg['msg']['md5sum']
                filename = msg['msg']['filename']
                tmpl = "{name}/{filename}/{md5sum}/{filename}"

                path = tmpl.format(name=name, md5sum=md5sum,
                                   filename=filename)

            return "{prefix}/{path}".format(prefix=prefix, path=path)

    def usernames(self, msg, **config):
        if 'agent' in msg['msg']:
            return set([msg['msg']['agent']])
        elif 'username' in msg['msg']['commit']:
            return set([msg['msg']['commit']['username']])
        else:
            return set()

    def packages(self, msg, **config):

        # If its not an rpms/ thing, then its not a package.
        if 'namespace' in msg['msg']:
            if not msg['msg']['namespace'] in ['rpms', 'rpms-checks']:
                return set()

        if 'git.receive' in msg['topic']:
            try:
                # Newer fedmsg
                return set([msg['msg']['commit']['repo']])
            except KeyError:
                # Legacy support
                return set(['.'.join(msg['topic'].split('.')[5:-1])])
        if 'git.branch' in msg['topic']:
            try:
                return set([msg['msg']['name']])
            except KeyError:
                return set(['.'.join(msg['topic'].split('.')[5:-1])])
        elif '.git.pkgdb2branch.complete' in msg['topic']:
            unbranched = msg['msg'].get('unbranchedPackages') or []
            branched = msg['msg'].get('branchedPackages') or []
            return set(unbranched + branched)
        elif '.git.lookaside' in msg['topic']:
            return set([msg['msg']['name']])

        return set()

    def objects(self, msg, **config):
        if 'git.receive' in msg['topic']:
            try:
                repo = msg['msg']['commit']['repo']
            except KeyError:
                repo = '.'.join(msg['topic'].split('.')[5:-1])
            return set([
                repo + '/' + filename for filename in
                msg['msg']['commit']['stats']['files']
            ])
        elif '.git.branch' in msg['topic']:
            try:
                repo = msg['msg']['name']
            except KeyError:
                repo = '.'.join(msg['topic'].split('.')[5:-1])
            return set([repo + '/__git__'])
        elif '.git.pkgdb2branch.complete' in msg['topic']:
            return set([
                p + '/__git__' for p in self.packages(msg, **config)
            ])
        elif '.git.lookaside' in msg['topic']:
            return set([msg['msg']['name'] + '/' + msg['msg']['filename']])

        return set()
