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

from fasshim import gravatar_url

fs_prefix = "/srv/web/infra/ansible/"


def relative_playbook(playbook):
    """ Returns a tuple (controlled, playbook).

    - controlled is a boolean indicating whether or not we think that the
      playbook being run was checked in to our ansible git repo.
    - playbook is the relative file path of the playbook.
    """
    if playbook.startswith(fs_prefix):
        return True, playbook[len(fs_prefix):]
    else:
        return False, playbook.split('/')[-1]


class AnsibleProcessor(BaseProcessor):
    __name__ = "ansible"
    __description__ = "Fedora Infrastructure Ansible Runs"
    __link__ = "http://infrastructure.fedoraproject.org/cgit/ansible.git"
    __docs__ = \
        "https://fedoraproject.org/wiki/Infrastructure_ansible_migration"
    __obj__ = "Ansible Runs"

    def subtitle(self, msg, **config):
        user = msg['msg']['userid']
        controlled, playbook = relative_playbook(msg['msg']['playbook'])

        if 'ansible.playbook.start' in msg['topic']:
            tmpl = self._("{user} started an ansible run of {playbook}")
            return tmpl.format(user=user, playbook=playbook)
        elif 'ansible.playbook.complete' in msg['topic']:
            tmpl = self._("{user}'s {playbook} playbook run completed")
            return tmpl.format(user=user, playbook=playbook)
        return ""

    def secondary_icon(self, msg, **config):
        user = msg['msg']['userid']
        return gravatar_url(user)

    def link(self, msg, **config):
        base = "http://infrastructure.fedoraproject.org/cgit/ansible.git/tree/"
        controlled, playbook = relative_playbook(msg['msg']['playbook'])
        if not controlled:
            return None
        else:
            return base + playbook

    def usernames(self, msg, **config):
        return set([msg['msg']['userid']])

    def objects(self, msg, **config):
        controlled, playbook = relative_playbook(msg['msg']['playbook'])

        if not controlled:
            playbook = "uncontrolled-playbooks/" + playbook

        if 'results' in msg['msg']:
            return set([playbook] + [
                "inventory/" + host for host in msg['msg']['results'].keys()
            ])
        else:
            return set([playbook])
