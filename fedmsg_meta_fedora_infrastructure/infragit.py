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
#
from fedmsg_meta_fedora_infrastructure import BaseProcessor
from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url


class InfraGitProcessor(BaseProcessor):
    __name__ = "infragit"
    __description__ = "Fedora Infrastructure repos"
    __link__ = "https://infrastructure.fedoraproject.org/cgit/"
    __docs__ = "https://fedoraproject.org/wiki/Using_Fedora_GIT"
    __docs__ = "https://infrastructure.fedoraproject.org/infra/" + \
        "docs/infra-git-repo.rst"
    __obj__ = "Infrastructure Commits"
    __icon__ = "https://apps.fedoraproject.org/img/icons/git-logo.png"

    def _get_repo(self, msg):
        return msg['msg']['commit']['path'].split('/')[-1]

    def subtitle(self, msg, **config):
        repo = self._get_repo(msg)
        user = self.agent(msg, **config)

        summ = msg['msg']['commit']['summary']
        whole = msg['msg']['commit']['message']
        if summ.strip() != whole.strip():
            summ += " (..more)"

        branch = msg['msg']['commit']['branch']

        tmpl = self._('{user} pushed a commit to the fedora-infra {repo} repo '
                      '({branch}):  "{summary}"')
        return tmpl.format(user=user, repo=repo, branch=branch, summary=summ)

    def link(self, msg, **config):
        prefix = "https://infrastructure.fedoraproject.org/cgit"
        repo = self._get_repo(msg)

        # We don't have public links to some old repos..
        if repo in ['puppet']:
            return ''

        rev = msg['msg']['commit']['rev']
        branch = msg['msg']['commit']['branch']
        tmpl = "{prefix}/{repo}.git/commit/?h={branch}&id={rev}"
        return tmpl.format(prefix=prefix, repo=repo, branch=branch, rev=rev)

    def secondary_icon(self, msg, **config):
        return avatar_url(self.agent(msg, **config))

    def usernames(self, msg, **config):
        return set([self.agent(msg, **config)])

    def agent(self, msg, **config):
        return msg['msg']['commit']['username']

    def objects(self, msg, **config):
        repo = self._get_repo(msg)
        return set([
            repo + '/' + filename
            for filename in msg['msg']['commit']['stats']['files']
        ])
