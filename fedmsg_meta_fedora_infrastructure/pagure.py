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

from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url
from fedmsg_meta_fedora_infrastructure import BaseProcessor

class PagureProcessor(BaseProcessor):
    topic_prefix_re = 'io\\.pagure\\.(dev|stg|prod)'

    __name__ = "pagure"
    __description__ = "Pagure forge"
    __link__ = "https://pagure.io"
    __docs__ = "https://pagure.io/pagure"
    __obj__ = "Pagure forge"
    __icon__ = ("https://apps.fedoraproject.org/packages/"
                "images/icons/package_128x128.png")

    def __get_project(self, msg):
        ''' Return the project as `foo` or `user/foo` if the project is a
        fork.
        '''
        project = msg['project']['name']
        if msg['project']['parent']:
            user = msg['project']['user']['name']
            project = '/'.join([user, project])
        return project

    def link(self, msg, **config):
        try:
            project = self.__get_project(msg['msg'])
        except KeyError:
            try:
                project = self.__get_project(msg['msg']['pullrequest'])
            except KeyError:
                project = "(unknown)"

        base_url = "https://pagure.io"

        tmpl = '{base_url}/{project}'
        if '/' in project:
            tmpl = '{base_url}/fork/{project}'
        if 'pagure.issue' in msg['topic']:
            issueid = msg['msg']['issue']['id']
            tmpl += '/issue/{id}'
            return tmpl.format(
                base_url=base_url, project=project, id=issueid)
        elif 'pagure.project' in msg['topic']:
            return tmpl.format(base_url=base_url, project=project)
        elif 'pagure.pull-request' in msg['topic']:
            prid = msg['msg']['pullrequest']['id']
            tmpl += '/pull-request/{id}'
            return tmpl.format(
                base_url=base_url, project=project, id=prid)
        else:
            return base_url

        return None

    def subtitle(self, msg, **config):
        try:
            project = self.__get_project(msg['msg'])
        except KeyError:
            try:
                project = self.__get_project(msg['msg']['pullrequest'])
            except KeyError:
                project = "(unknown)"
        user = msg['msg']['agent']

        if 'pagure.project.new' in msg['topic']:
            tmpl = self._(
                '{user} created a new project "{project}"'
            )
            return tmpl.format(user=user, project=project)
        elif 'pagure.issue.new' in msg['topic']:
            issueid = msg['msg']['issue']['id']
            title = msg['msg']['issue']['title']
            tmpl = self._(
                '{user} opened a new ticket {project}#{id}: "{title}"'
            )
            return tmpl.format(
                user=user, project=project, title=title, id=issueid)
        elif 'pagure.issue.comment.added' in msg['topic']:
            issueid = msg['msg']['issue']['id']
            title = msg['msg']['issue']['title']
            tmpl = self._(
                '{user} commented on the ticket {project}#{id}: "{title}"'
            )
            return tmpl.format(
                user=user, project=project, title=title, id=issueid)
        elif 'pagure.issue.tag.added' in msg['topic']:
            issueid = msg['msg']['issue']['id']
            tags = ', '.join(msg['msg']['tags'])
            tmpl = self._(
                '{user} tagged the ticket {project}#{id}: {tags}'
            )
            return tmpl.format(
                user=user, project=project, id=issueid, tags=tags)
        elif 'pagure.issue.tag.removed' in msg['topic']:
            issueid = msg['msg']['issue']['id']
            tags = ', '.join(msg['msg']['tags'])
            tmpl = self._(
                '{user} removed tags: {tags}, from the ticket {project}#{id}'
            )
            return tmpl.format(
                user=user, project=project, id=issueid, tags=tags)
        elif 'pagure.issue.assigned.added' in msg['topic']:
            issueid = msg['msg']['issue']['id']
            assignee = msg['msg']['issue']['assignee']['name']
            tmpl = self._(
                '{user} assigned {assignee} to the ticket {project}#{id}'
            )
            return tmpl.format(
                user=user, project=project, id=issueid, assignee=assignee)
        elif 'pagure.issue.assigned.reset' in msg['topic']:
            issueid = msg['msg']['issue']['id']
            tmpl = self._(
                '{user} reset the assignee of the ticket {project}#{id}'
            )
            return tmpl.format(user=user, project=project, id=issueid)
        elif 'pagure.issue.dependency.added' in msg['topic']:
            issueid = msg['msg']['issue']['id']
            dep_id = msg['msg']['added_dependency']
            tmpl = self._(
                '{user} added on the ticket {project}#{id} a dependency on '
                'ticket {project}#{dep_id}'
            )
            return tmpl.format(
                user=user, project=project, id=issueid,
                dep_id=dep_id)
        elif 'pagure.issue.dependency.removed' in msg['topic']:
            issueid = msg['msg']['issue']['id']
            removed = msg['msg']['removed_dependency']
            tmpl = self._(
                '{user} removed on the ticket {project}#{id} the dependency '
                'on ticket {project}#{removed}'
            )
            return tmpl.format(
                user=user, project=project, id=issueid, removed=removed)
        elif 'pagure.issue.edit' in msg['topic']:
            issueid = msg['msg']['issue']['id']
            fields = '", "'.join(msg['msg']['fields'])
            tmpl = self._(
                '{user} edited the fields: "{fields}" of the ticket '
                '{project}#{id}'
            )
            return tmpl.format(
                user=user, project=project, id=issueid, fields=fields)
        elif 'pagure.project.edit' in msg['topic']:
            fields = '", "'.join(msg['msg']['fields'])
            tmpl = self._(
                '{user} edited the fields: "{fields}" of the project '
                '{project}'
            )
            return tmpl.format(user=user, project=project, fields=fields)
        elif 'pagure.project.user.added' in msg['topic']:
            new_user = msg['msg']['new_user']
            tmpl = self._(
                '{user} added "{new_user}" to the project {project}'
            )
            return tmpl.format(user=user, project=project, new_user=new_user)
        elif 'pagure.project.tag.removed' in msg['topic']:
            tags = '", "'.join(msg['msg']['tags'])
            tmpl = self._(
                '{user} removed tags "{tags}" of the project {project}'
            )
            return tmpl.format(user=user, project=project, tags=tags)
        elif 'pagure.project.tag.edited' in msg['topic']:
            old_tag = msg['msg']['old_tag']
            new_tag = msg['msg']['new_tag']
            tmpl = self._(
                '{user} edited tags "{old_tag}" of the project {project} '
                'to "{new_tag}"'
            )
            return tmpl.format(
                user=user, project=project,
                old_tag=old_tag, new_tag=new_tag)
        elif 'pagure.project.forked' in msg['topic']:
            old_project = msg['msg']['project']['parent']['name']
            tmpl = self._(
                '{user} forked project "{old_project}" to "{project}"'
            )
            return tmpl.format(
                user=user, old_project=old_project, project=project)
        elif 'pagure.pull-request.comment.added' in msg['topic']:
            prid = msg['msg']['pullrequest']['id']
            tmpl = self._(
                '{user} commented on the pull-request#{id} of project '
                '"{project}"'
            )
            return tmpl.format(user=user, id=prid, project=project)
        elif 'pagure.pull-request.closed' in msg['topic']:
            prid = msg['msg']['pullrequest']['id']
            merged = msg['msg']['merged']
            if merged:
                tmpl = self._(
                    '{user} merged the pull-request#{id} of project '
                    '"{project}"'
                )
            else:
                tmpl = self._(
                    '{user} closed (without merging) the pull-request#{id} '
                    'of project "{project}"'
                )
            return tmpl.format(user=user, id=prid, project=project)
        elif 'pagure.pull-request.new' in msg['topic']:
            prid = msg['msg']['pullrequest']['id']
            title = msg['msg']['pullrequest']['title']
            tmpl = self._(
                '{user} opened the pull-request#{id}: "{title}" for the '
                'project "{project}"'
            )
            return tmpl.format(
                user=user, id=prid, project=project, title=title)
        elif 'pagure.pull-request.flag.added' in msg['topic']:
            prid = msg['msg']['pullrequest']['id']
            username = msg['msg']['flag']['username']
            comment = msg['msg']['flag']['comment']
            tmpl = self._(
                '{username} flagged {project} #{id} with "{comment}"'
            )
            return tmpl.format(
                username=username, id=prid, comment=comment, project=project)

        elif 'pagure.pull-request.flag.updated' in msg['topic']:
            prid = msg['msg']['pullrequest']['id']
            username = msg['msg']['flag']['username']
            comment = msg['msg']['flag']['comment']
            tmpl = self._(
                '{username} updated the flag of {project} #{id} with: '
                '"{comment}"'
            )
            return tmpl.format(
                username=username, id=prid, comment=comment, project=project)

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
        if username:
            return set([username])
        else:
            return set([])

    def objects(self, msg, **config):
        try:
            project = self.__get_project(msg['msg'])
        except KeyError:
            try:
                project = self.__get_project(msg['msg']['pullrequest'])
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
            return set([
                'pull-request/%s' % msg['msg']['pullrequest']['id'],
                'project/%s' % project,
            ])

        return set([])
