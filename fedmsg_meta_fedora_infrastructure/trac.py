# This file is part of fedmsg.
# Copyright (C) 2012 Red Hat, Inc.
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

short_repos = [
    '389',
    'aeolus',
    'bluecurve',
    'bluecurve-classic-metacity-theme',
    'bluecurve-gdm-theme',
    'bluecurve-gnome-theme',
    'bluecurve-gtk-themes',
    'bluecurve-icon-theme',
    'bluecurve-kde-theme',
    'bluecurve-kdm-theme',
    'bluecurve-kwin-theme',
    'bluecurve-metacity-theme',
    'bluecurve-qt-engine',
    'bluecurve-xmms-skin',
    'cobbler',
    'deltacloud',
    'docs',
    'echo-icon-theme',
    'fedorabubbles-gdm-theme',
    'fedoradna-gdm-theme',
    'fedoradna-kdm-theme',
    'fedoraflyinghigh-gdm-theme',
    'fedoraflyinghigh-kdm-theme',
    'fedora-gnome-theme',
    'fedora-icon-theme',
    'fedorainfinity-gdm-theme',
    'fedorainfinity-screensaver-theme',
    'fedora-screensaver-theme',
    'freeotp',
    'grid',
    'koji',
    'l10n',
    'livecd',
    'mash',
    'mirrormanager',
    'mkinitrd',
    'nodoka',
    'opyum',
    'ovirt',
    'presto',
    'readahead',
    'redhat-rpm-config',
    'releng',
    'revisor',
    'rhq',
    'snake',
    'thetango',
    'thincrust',
    'umltester',
    'updatinator',
    'webauthinfra',
    'wevisor',
]


def repo_name(msg):
    """ Compat util to get the repo name from a message. """
    try:
        # git messages look like this now
        path = msg['msg']['commit']['path']
        project = path.split('.git')[0][9:]
    except KeyError:
        # they used to look like this, though
        project = msg['msg']['commit']['repo']

    return project


class TracProcessor(BaseProcessor):
    __name__ = "Trac"
    __description__ = "events from select Fedora Hosted projects"
    __link__ = "https://fedorahosted.org"
    __docs__ = "https://fedorahosted.org/readme"
    __obj__ = "Fedora Hosted Events"
    __icon__ = "https://www.edgewall.org/gfx/trac_bullet.png"

    def long_form(self, msg, **config):
        if 'ticket' in msg['msg']:
            comment = msg['msg'].get('comment')
            description = msg['msg']['ticket'].get('description')
            summary = msg['msg']['ticket'].get('summary')

            retval = ""
            if summary:
                retval += "Summary: " + summary + "\n"
            if comment:
                retval += "Comment: " + comment + "\n"
            elif description:
                retval += "Description: " + description + "\n"
            return retval

    def subtitle(self, msg, **config):
        if 'page' in msg['msg']:
            old_name = None
            user = msg['msg']['agent']
            name = msg['msg']['page']['name']
            project = msg['msg']['instance']['project_name']
            if 'page.version.delete' in msg['topic']:
                tmpl = self._(
                    "{user} deleted a version of the '{name}' wiki "
                    "page on the {project} trac instance")
            elif 'page.delete' in msg['topic']:
                tmpl = self._(
                    "{user} straight-up deleted the '{name}' wiki "
                    "page on the {project} trac instance")
            elif 'page.rename' in msg['topic']:
                old_name = msg['msg']['old_name']
                tmpl = self._(
                    "{user} renamed the wiki page '{old_name}' to '{name}' "
                    "on the {project} trac instance")
            elif 'page.update' in msg['topic']:
                tmpl = self._(
                    "{user} updated the '{name}' wiki page "
                    "on the {project} trac instance")
            elif 'page.new' in msg['topic']:
                tmpl = self._(
                    "{user} created a new '{name}' wiki page "
                    "on the {project} trac instance")

            return tmpl.format(
                user=user,
                name=name,
                old_name=old_name,
                project=project)
        elif 'ticket' in msg['msg']:
            status = None
            resolution = None
            user = msg['msg']['agent']
            project = msg['msg']['instance']['project_name']
            if 'ticket.delete' in msg['topic']:
                tmpl = self._(
                    "{user} straight-up deleted a ticket "
                    "on the {project} trac instance")
            elif 'ticket.new' in msg['topic']:
                tmpl = self._(
                    "{user} opened a new ticket "
                    "on the {project} trac instance")
            elif 'ticket.update' in msg['topic']:
                tmpl = self._(
                    "{user} updated a ticket "
                    "on the {project} trac instance")
                status = msg['msg']['ticket']['status']
                old_values = msg['msg']['old_values']
                if status == 'reopened' and 'status' in old_values:
                    tmpl = self._(
                        "{user} reopened a ticket "
                        "on the {project} trac instance")
                elif status == 'closed' and 'status' in old_values:
                    resolution = msg['msg']['ticket']['resolution']
                    tmpl = self._(
                        "{user} closed a ticket "
                        "on the {project} trac instance "
                        "as '{resolution}'")

            return tmpl.format(
                user=user,
                project=project,
                status=status,
                resolution=resolution,
            )
        elif 'git.receive' in msg['topic']:
            user = msg['msg']['commit']['username']
            project = repo_name(msg)

            tmpl = self._(
                "{user} pushed some commits to the '{project}' "
                "fedorahosted git repository")

            return tmpl.format(user=user, project=project)

    def secondary_icon(self, msg, **config):
        user = None

        try:
            user = msg['msg']['agent']
        except KeyError:
            pass

        try:
            user = msg['msg']['commit']['username']
        except KeyError:
            pass

        if not user:
            return ""

        return avatar_url(username=user)

    def usernames(self, msg, **config):
        users = set()

        try:
            users.add(msg['msg']['agent'])
        except KeyError:
            pass

        try:
            user = msg['msg']['page']['author'].strip()
            if user:
                users.add(user)
        except KeyError:
            pass

        try:
            user = msg['msg']['ticket']['owner'].strip()
            if user:
                users.add(user)
        except KeyError:
            pass

        try:
            user = msg['msg']['ticket']['reporter'].strip()
            if user:
                users.add(user)
        except KeyError:
            pass

        try:
            for user in msg['msg']['ticket']['cc'].split(','):
                user = user.strip()
                if user:
                    users.add(user)
        except KeyError:
            pass

        try:
            user = msg['msg']['commit']['username'].strip()
            if user:
                users.add(user)
        except KeyError:
            pass

        return users

    def objects(self, msg, **config):
        if 'trac.wiki.page.rename' in msg['topic']:
            project = msg['msg']['instance']['project_name']
            name = msg['msg']['page']['name']
            old_name = msg['msg']['old_name']
            return set([
                '/'.join([project, 'wiki', name]),
                '/'.join([project, 'wiki', old_name]),
            ])
        elif 'trac.wiki.' in msg['topic']:
            project = msg['msg']['instance']['project_name']
            name = msg['msg']['page']['name']
            return set(['/'.join([project, 'wiki', name])])
        elif 'trac.ticket.' in msg['topic']:
            project = msg['msg']['instance']['project_name']
            id = msg['msg']['ticket']['id']
            return set(['/'.join([project, 'ticket', str(id)])])
        elif '.git.receive' in msg['topic']:
            files = msg['msg']['commit']['stats']['files'].keys()
            project = repo_name(msg)
            return set([
                project + '/git/' + filename
                for filename in files
            ])

    def link(self, msg, **config):
        if 'trac.wiki.' in msg['topic']:
            base_url = msg['msg']['instance']['base_url'].strip('/')
            name = msg['msg']['page']['name']
            url = '/'.join([base_url, 'wiki', name])

            version = msg['msg']['page']['version']
            versioned = version and all([
                '.rename' not in msg['topic'],
                '.new' not in msg['topic'],
            ])
            if versioned:
                url += "?action=diff&version=%i" % version

            return url
        elif 'trac.ticket.' in msg['topic']:
            base_url = msg['msg']['instance']['base_url'].strip('/')
            id = msg['msg']['ticket']['id']
            url = '/'.join([base_url, 'ticket', str(id)])
            return url
        elif '.git.receive' in msg['topic']:
            name = repo_name(msg)
            suffix = '' if name in short_repos else '.git'
            rev = msg['msg']['commit']['rev']
            tmpl = "https://git.fedorahosted.org/cgit/" + \
                "{name}{suffix}/commit/?id={rev}"
            return tmpl.format(name=name, rev=rev, suffix=suffix)
