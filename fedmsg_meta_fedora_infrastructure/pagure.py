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
# Authors:  Pierre-Yves Chibon <pingou@pingoured.fr>
#

from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url, email2fas
from fedmsg_meta_fedora_infrastructure import BaseProcessor

from fedmsg_meta_fedora_infrastructure.conglomerators.pagure import \
        pagure as pagure_conglomerator

import fedmsg.meta.base


def _get_project(msg, key='project'):
    ''' Return the project as `foo` or `user/foo` if the project is a
    fork.
    '''
    project = msg[key]['name']
    ns = msg[key].get('namespace')
    if ns:
        project = '/'.join([ns, project])
    if msg[key]['parent']:
        user = msg[key]['user']['name']
        project = '/'.join(['fork', user, project])
    return project


def _git_receive_v1(msg, tmpl, **config):
    ''' Return the subtitle for the first version of pagure git.receive
    messages.
    '''
    repo = _get_project(msg['msg']['commit'], key='repo')
    email = msg['msg']['commit']['email']
    user = email2fas(email, **config)
    summ = msg['msg']['commit']['summary']
    whole = msg['msg']['commit']['message']
    if summ.strip() != whole.strip():
        summ += " (..more)"

    branch = msg['msg']['commit']['branch']
    if 'refs/heads/' in branch:
        branch = branch.replace('refs/heads/', '')
    return tmpl.format(user=user or email, repo=repo,
                       branch=branch, summary=summ)


def _git_receive_v2(msg, tmpl):
    ''' Return the subtitle for the second version of pagure git.receive
    messages.
    '''
    repo = _get_project(msg['msg'], key='repo')
    user = msg['msg']['agent']
    n_commits = msg['msg']['total_commits']
    commit_lbl = 'commit' if str(n_commits) == '1' else 'commits'
    branch = msg['msg']['branch']
    if 'refs/heads/' in branch:
        branch = branch.replace('refs/heads/', '')
    return tmpl.format(user=user, repo=repo,
                       branch=branch, n_commits=n_commits,
                       commit_lbl=commit_lbl)


class PagureProcessor(BaseProcessor):
    topic_prefix_re = 'io\\.pagure\\.(dev|stg|prod)'

    __name__ = "pagure"
    __description__ = "Pagure forge"
    __link__ = "https://pagure.io"
    __stg_link__ = "https://stg.pagure.io"
    __docs__ = "https://pagure.io/pagure"
    __obj__ = "Pagure forge"
    __icon__ = ("https://apps.fedoraproject.org/packages/"
                "images/icons/package_128x128.png")

    conglomerators = [
        pagure_conglomerator.ByPR,
        pagure_conglomerator.ByIssue,
        pagure_conglomerator.ByNewStyleCommit,
        pagure_conglomerator.ByOldStyleCommit,
    ]


    def link(self, msg, **config):
        try:
            project = _get_project(msg['msg'])
        except KeyError:
            try:
                project = _get_project(msg['msg']['pullrequest'])
            except KeyError:
                project = "(unknown)"

        base_url = self.__link__
        if '.stg.' in msg['topic']:
            base_url = self.__stg_link__

        tmpl = '{base_url}/{project}'
        if 'pagure.issue' in msg['topic']:
            issueid = msg['msg']['issue']['id']
            if 'comment.edited' in msg['topic']:
                # This is for an edited issue..
                comment = msg['msg'].get('comment')
                comment_id = None
                if comment:
                    comment_id = comment.get('id')
                if comment_id and project != "(unknown)":
                    tmpl += '/issue/{id}#comment-{comment}'
                    return tmpl.format(
                        base_url=base_url, project=project, id=issueid,
                        comment=comment_id)
                elif project != "(unknown)":
                    tmpl += '/issue/{id}'
                    return tmpl.format(
                        base_url=base_url, project=project, id=issueid)
                else:
                    return base_url
            elif 'comment.added' in msg['topic']:
                comments = msg['msg']['issue']['comments']
                if comments:
                    tmpl += '/issue/{id}#comment-{comment}'
                    return tmpl.format(
                        base_url=base_url, project=project, id=issueid,
                        comment=comments[-1]['id'])
                else:
                    tmpl += '/issue/{id}'
                    return tmpl.format(
                        base_url=base_url, project=project, id=issueid)
            else:
                tmpl += '/issue/{id}'
                return tmpl.format(
                    base_url=base_url, project=project, id=issueid)
        elif 'pagure.pull-request' in msg['topic']:
            key = 'pullrequest'
            for k in ['pullrequest', 'pull_request', 'pull-request']:
                if k in msg['msg']:
                    key = k
                    break
            prid = msg['msg'][key]['id']
            if 'comment' in msg['topic']:
                comments = msg['msg']['pullrequest']['comments']
                if comments:
                    tmpl += '/pull-request/{id}#comment-{comment}'
                    return tmpl.format(
                        base_url=base_url, project=project, id=prid,
                        comment=comments[-1]['id'])
                elif msg['msg'].get('comment'):
                    comment_id = msg['msg']['comment']['id']
                    tmpl += '/pull-request/{id}#comment-{comment}'
                    return tmpl.format(
                        base_url=base_url, project=project, id=prid,
                        comment=comment_id)
                else:
                    tmpl += '/pull-request/{id}'
                    return tmpl.format(
                        base_url=base_url, project=project, id=prid)
            else:
                tmpl += '/pull-request/{id}'
                return tmpl.format(
                    base_url=base_url, project=project, id=prid)
        elif 'pagure.request' in msg['topic']:
            prid = msg['msg']['request']['id']
            tmpl += '/pull-request/{id}'
            return tmpl.format(
                    base_url=base_url, project=project, id=prid)
        elif 'pagure.project.deleted' in msg['topic']:
            return base_url
        elif 'pagure.project' in msg['topic']:
            return tmpl.format(base_url=base_url, project=project)
        elif 'pagure.commit.flag' in msg['topic']:
            tmpl += '/c/{commit_hash}'
            project = _get_project(msg['msg'], 'repo')
            commit_hash = msg['msg']['flag']['commit_hash']
            return tmpl.format(
                base_url=base_url, project=project, commit_hash=commit_hash)
        elif 'pagure.git.receive' in msg['topic']:
            if 'commit' in msg['msg']:
                project = _get_project(msg['msg']['commit'], key='repo')
                item = msg['msg']['commit']['rev']
                tmpl += '/{item}'
            else:
                project = _get_project(msg['msg'], key='repo')
                item = msg['msg']['branch']
                if 'refs/heads/' in item:
                    item = item.replace('refs/heads/', '')
                tmpl += '/branch/{item}'
            return tmpl.format(
                base_url=base_url, project=project, item=item)

        else:
            return base_url

        return None

    def subtitle(self, msg, **config):
        try:
            project = _get_project(msg['msg'])
        except KeyError:
            try:
                project = _get_project(msg['msg']['pullrequest'])
            except KeyError:
                project = "(unknown)"
        user = msg['msg'].get('agent')

        if 'pagure.project.new' in msg['topic']:
            tmpl = self._(
                '{user} created a new project "{project}"'
            )
            return tmpl.format(user=user, project=project)
        elif 'pagure.issue.new' in msg['topic']:
            issueid = msg['msg']['issue']['id']
            title = msg['msg']['issue']['title']
            tmpl = self._(
                '{user} opened a new ticket {project}#{id}: "{title}"')
            return tmpl.format(
                user=user, project=project, title=title, id=issueid)
        elif 'pagure.issue.drop' in msg['topic']:
            issueid = msg['msg']['issue']['id']
            title = msg['msg']['issue']['title']
            tmpl = self._(
                '{user} deleted ticket {project}#{id}: "{title}"')
            return tmpl.format(
                user=user,project=project,title=title,id=issueid)
        elif 'pagure.issue.comment.edited' in msg['topic']:
            issueid = msg['msg']['issue']['id']
            title = msg['msg']['issue']['title']
            tmpl = self._(
                '{user} edited a comment on ticket {project}#{id}: "{title}"')
            return tmpl.format(
                user=user, project=project, title=title, id=issueid)
        elif 'pagure.issue.comment.added' in msg['topic']:
            issueid = msg['msg']['issue']['id']
            title = msg['msg']['issue']['title']
            tmpl = self._(
                '{user} commented on ticket {project}#{id}: "{title}"')
            return tmpl.format(
                user=user, project=project, title=title, id=issueid)
        elif 'pagure.issue.tag.added' in msg['topic']:
            issueid = msg['msg']['issue']['id']
            tags = msg['msg']['tags']
            tags = fedmsg.meta.base.BaseConglomerator.list_to_series(tags)
            tmpl = self._(
                '{user} tagged ticket {project}#{id}: {tags}')
            return tmpl.format(
                user=user, project=project, id=issueid, tags=tags)
        elif 'pagure.issue.tag.removed' in msg['topic']:
            issueid = msg['msg']['issue']['id']
            tags = msg['msg']['tags']
            tags = fedmsg.meta.base.BaseConglomerator.list_to_series(tags)
            tmpl = self._(
                '{user} removed the {tags} tags from ticket {project}#{id}')
            return tmpl.format(
                user=user, project=project, id=issueid, tags=tags)
        elif 'pagure.pull-request.tag.added' in msg['topic']:
            issueid = msg['msg']['pull_request']['id']
            tags = msg['msg']['tags']
            tags = fedmsg.meta.base.BaseConglomerator.list_to_series(tags)
            tmpl = self._(
                '{user} tagged pull-request {project}#{id}: {tags}')
            return tmpl.format(
                user=user, project=project, id=issueid, tags=tags)
        elif 'pagure.pull-request.tag.removed' in msg['topic']:
            issueid = msg['msg']['pull_request']['id']
            tags = msg['msg']['tags']
            tags = fedmsg.meta.base.BaseConglomerator.list_to_series(tags)
            tmpl = self._(
                '{user} removed the {tags} tags from pull-request {project}#{id}')
            return tmpl.format(
                user=user, project=project, id=issueid, tags=tags)
        elif 'pagure.issue.assigned.added' in msg['topic']:
            issueid = msg['msg']['issue']['id']
            assignee = ''
            if msg['msg']['issue']['assignee']:
                assignee = ' to {0}'.format(
                    msg['msg']['issue']['assignee']['name']
                )
            tmpl = self._(
                '{user} assigned ticket {project}#{id}{assignee}')
            return tmpl.format(
                user=user, project=project, id=issueid, assignee=assignee)
        elif 'pagure.issue.assigned.reset' in msg['topic']:
            issueid = msg['msg']['issue']['id']
            tmpl = self._(
                '{user} reset the assignee of ticket {project}#{id}')
            return tmpl.format(user=user, project=project, id=issueid)
        elif 'pagure.issue.dependency.added' in msg['topic']:
            issueid = msg['msg']['issue']['id']
            dep_id = msg['msg']['added_dependency']
            tmpl = self._(
                '{user} added ticket {project}#{id} as a dependency of '
                'ticket {project}#{dep_id}'
            )
            return tmpl.format(
                user=user, project=project, id=issueid,
                dep_id=dep_id)
        elif 'pagure.issue.dependency.removed' in msg['topic']:
            issueid = msg['msg']['issue']['id']
            removed = msg['msg']['removed_dependency']
            tmpl = self._(
                '{user} removed ticket {project}#{id} as a dependency '
                'of ticket {project}#{removed}'
            )
            return tmpl.format(
                user=user, project=project, id=issueid, removed=removed)
        elif 'pagure.issue.edit' in msg['topic']:
            issueid = msg['msg']['issue']['id']
            fields = msg['msg']['fields']
            if fields == ['status']:
                status = msg['msg']['issue']['status']
                tmpl = self._(
                    '{user} set the status of ticket {project}#{id} to: '
                    '{status}')
                return tmpl.format(
                    user=user, project=project, id=issueid, status=status)
            fields = fedmsg.meta.base.BaseConglomerator.list_to_series(fields)
            tmpl = self._(
                '{user} edited the {fields} fields of ticket '
                '{project}#{id}'
            )
            return tmpl.format(
                user=user, project=project, id=issueid, fields=fields)
        elif 'pagure.project.edit' in msg['topic']:
            fields = msg['msg']['fields']
            fields = fedmsg.meta.base.BaseConglomerator.list_to_series(fields)
            tmpl = self._(
                '{user} edited the {fields} fields of project {project}')
            return tmpl.format(user=user, project=project, fields=fields)
        elif 'pagure.project.group.added' in msg['topic']:
            new_group = msg['msg']['new_group']
            access = msg['msg'].get('access')
            if access:
                tmpl = self._(
                    '{user} added group "{new_group}" to project {project} ' + \
                    'with {access} access'
                )
            else:
                tmpl = self._(
                    '{user} added group "{new_group}" to project {project}'
                )
            return tmpl.format(
                user=user, project=project, new_group=new_group, access=access)
        elif 'pagure.project.group.access.updated' in msg['topic']:
            new_group = msg['msg']['new_group']
            new_access = msg['msg']['new_access']
            tmpl = self._(
                '{user} updated access of group "{new_group}" ' + \
                'to {new_access} on project {project}'
            )
            return tmpl.format(
                user=user, project=project, new_group=new_group, new_access=new_access)
        elif 'pagure.project.user.added' in msg['topic']:
            new_user = msg['msg']['new_user']
            access = msg['msg'].get('access')
            if access:
                tmpl = self._(
                    '{user} added "{new_user}" to project {project} '
                    'with {access} access'
                )
            else:
                tmpl = self._(
                    '{user} added "{new_user}" to project {project}'
                )
            return tmpl.format(
                user=user, project=project, new_user=new_user, access=access)
        elif 'pagure.project.user.access.updated' in msg['topic']:
            new_user = msg['msg']['new_user']
            new_access = msg['msg']['new_access']
            tmpl = self._(
                '{user} updated access of "{new_user}" to {new_access} '
                'in project {project}'
            )
            return tmpl.format(
                user=user, project=project, new_user=new_user, new_access=new_access)
        elif 'pagure.project.tag.removed' in msg['topic']:
            tags = msg['msg']['tags']
            tags = fedmsg.meta.base.BaseConglomerator.list_to_series(tags)
            tmpl = self._(
                '{user} removed tags "{tags}" from project {project}'
            )
            return tmpl.format(user=user, project=project, tags=tags)
        elif 'pagure.project.tag.edited' in msg['topic']:
            old_tag = msg['msg']['old_tag']
            new_tag = msg['msg']['new_tag']
            tmpl = self._(
                '{user} altered tags on project {project} from '
                '"{old_tag}" to "{new_tag}"'
            )
            return tmpl.format(
                user=user, project=project,
                old_tag=old_tag, new_tag=new_tag)
        elif 'pagure.project.forked' in msg['topic']:
            old_project = msg['msg']['project']['parent']['name']
            tmpl = self._(
                '{user} forked {old_project} to {project}'
            )
            return tmpl.format(
                user=user, old_project=old_project, project=project)
        elif 'pagure.pull-request.comment.added' in msg['topic']:
            prid = msg['msg']['pullrequest']['id']
            tmpl = self._(
                '{user} commented on PR #{id} on {project}'
            )
            return tmpl.format(user=user, id=prid, project=project)
        elif 'pagure.pull-request.comment.edited' in msg['topic']:
            prid = msg['msg']['pullrequest']['id']
            tmpl = self._(
                '{user} edited a comment on PR #{id} on {project}'
            )
            return tmpl.format(user=user, id=prid, project=project)
        elif 'pagure.pull-request.closed' in msg['topic']:
            prid = msg['msg']['pullrequest']['id']
            merged = msg['msg']['merged']
            if merged:
                tmpl = self._(
                    '{user} merged pull request #{id} on {project}'
                )
            else:
                tmpl = self._(
                    '{user} closed (without merging) pull request #{id} '
                    'on {project}'
                )
            return tmpl.format(user=user, id=prid, project=project)
        elif 'pagure.pull-request.new' in msg['topic']:
            prid = msg['msg']['pullrequest']['id']
            title = msg['msg']['pullrequest']['title']
            tmpl = self._(
                '{user} opened pull request #{id} on {project}: {title}'
            )
            return tmpl.format(
                user=user, id=prid, project=project, title=title)
        elif 'pagure.pull-request.updated' in msg['topic']:
            prid = msg['msg']['pullrequest']['id']
            tmpl = self._(
                'Pull-request #{id} has been updated'
            )
            return tmpl.format(id=prid)
        elif 'pagure.pull-request.rebased' in msg['topic']:
            prid = msg['msg']['pullrequest']['id']
            tmpl = self._(
                'Pull-request #{id} has been rebased'
            )
            return tmpl.format(id=prid)
        elif 'pagure.pull-request.flag.added' in msg['topic']:
            prid = msg['msg']['pullrequest']['id']
            username = msg['msg']['flag']['username']
            comment = msg['msg']['flag']['comment']
            tmpl = self._(
                '{username} flagged {project}#{id} with "{comment}"'
            )
            return tmpl.format(
                username=username, id=prid, comment=comment, project=project)
        elif 'pagure.pull-request.flag.updated' in msg['topic']:
            prid = msg['msg']['pullrequest']['id']
            username = msg['msg']['flag']['username']
            comment = msg['msg']['flag']['comment']
            tmpl = self._(
                '{username} updated the flags on {project}#{id} with: '
                '"{comment}"'
            )
            return tmpl.format(
                username=username, id=prid, comment=comment, project=project)
        elif 'pagure.request.assigned.added' in msg['topic']:
            prid = msg['msg']['request']['id']
            assignee = ''
            if msg['msg']['request']['assignee']:
                assignee = ' to {0}'.format(
                    msg['msg']['request']['assignee']['name']
                )
            tmpl = self._(
                '{user} assigned PR {project}#{id}{assignee}')
            return tmpl.format(
                user=user, project=project, id=prid, assignee=assignee)
        elif 'pagure.request.assigned.reset' in msg['topic']:
            prid = msg['msg']['request']['id']
            tmpl = self._(
                '{user} reset the assignee of PR {project}#{id}')
            return tmpl.format(user=user, project=project, id=prid)
        elif 'pagure.git.receive' in msg['topic']:
            if 'commit' in msg['msg']:
                tmpl = self._('{user} pushed to {repo} ({branch}). "{summary}"')
                return _git_receive_v1(msg, tmpl, **config)
            else:
                tmpl = self._(
                    '{user} pushed {n_commits} {commit_lbl} '
                    'to {repo} ({branch})')
                return _git_receive_v2(msg, tmpl)
        elif 'pagure.project.deleted' in msg['topic']:
            tmpl = self._(
                '{user} deleted the project "{project}"'
            )
            return tmpl.format(user=user, project=project)
        elif 'pagure.commit.flag.added' in msg['topic']:
            tmpl = self._(
                '{user} added a flag on the commit {commit} of the '
                'project {project}'
            )
            user = msg['msg']['flag']['username']
            project = _get_project(msg['msg'], key='repo')
            commit = msg['msg']['flag']['commit_hash'][:8]
            return tmpl.format(user=user, project=project, commit=commit)
        elif 'pagure.commit.flag.updated' in msg['topic']:
            tmpl = self._(
                '{user} updated its flag on the commit {commit} of the '
                'project {project}'
            )
            user = msg['msg']['flag']['username']
            project = _get_project(msg['msg'], key='repo')
            commit = msg['msg']['flag']['commit_hash'][:8]
            return tmpl.format(user=user, project=project, commit=commit)
        elif 'pagure.project.user.removed' in msg['topic']:
            removed_user = msg['msg']['removed_user']
            tmpl = self._(
                '{user} removed "{removed_user}" from the project {project}'
            )
            return tmpl.format(
                user=user, project=project, removed_user=removed_user)

        else:
            pass

    def secondary_icon(self, msg, **config):
        username = msg['msg'].get('agent')
        if username:
            return avatar_url(username)
        else:
            return None

    def usernames(self, msg, **config):
        username = msg['msg'].get('agent')
        if not username and 'pagure.git.receive' in msg['topic']:
            email = msg['msg']['commit']['email']
            username = email2fas(email, **config)

        if username:
            return set([username])
        else:
            return set([])

    def objects(self, msg, **config):
        try:
            project = _get_project(msg['msg'])
        except KeyError:
            try:
                project = _get_project(msg['msg']['pullrequest'])
            except KeyError:
                project = "(unknown)"

        if 'pagure.project' in msg['topic']:
            return set([
                'project/%s' % project,
            ])
        elif 'pagure.issue' in msg['topic']:
            return set([
                'issue/%s' % msg['msg']['issue']['id'],
                'project/%s' % project,
            ])
        elif 'pagure.pull-request' in msg['topic']:
            key = 'pullrequest'
            for k in ['pullrequest', 'pull_request', 'pull-request']:
                if k in msg['msg']:
                    key = k
                    break
            return set([
                'pull-request/%s' % msg['msg'][key]['id'],
                'project/%s' % project,
            ])
        elif 'pagure.request' in msg['topic']:
            return set([
                'pull-request/%s' % msg['msg']['request']['id'],
                'project/%s' % project,
            ])
        elif 'pagure.git.receive' in msg['topic']:
            if 'commit' in msg['msg']:
                project = _get_project(msg['msg']['commit'], key='repo')
            else:
                project = _get_project(msg['msg'], key='repo')
            return set([
                'project/%s' % project,
            ])
        elif 'pagure.commit.flag' in msg['topic']:
            project = _get_project(msg['msg'], key='repo')
            return set([
                'project/%s' % project,
            ])

        return set([])


class DistGitPagureProcessor(PagureProcessor):
    topic_prefix_re = 'org\\.fedoraproject\\.(dev|stg|prod)'

    __name__ = "pagure"
    __description__ = "Pagure over Dist-git"
    __link__ = "https://src.fedoraproject.org"
    __stg_link__ = "https://src.stg.fedoraproject.org"
    __docs__ = "https://src.fedoraproject.org"
    __obj__ = "Pagure over Dist-git"
    __icon__ = ("https://apps.fedoraproject.org/packages/"
                "images/icons/package_128x128.png")

    conglomerators = [
        pagure_conglomerator.ByPR,
        pagure_conglomerator.ByIssue,
        pagure_conglomerator.ByNewStyleCommit,
        pagure_conglomerator.ByOldStyleCommit,
    ]
