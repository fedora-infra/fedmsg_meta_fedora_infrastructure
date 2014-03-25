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

from fasshim import gravatar_url, gravatar_url_from_email, email2fas
from fedmsg_meta_fedora_infrastructure import BaseProcessor

MAX_LEN = 40


def comma_join(fields, oxford=True):
    """ Join together words. """

    def fmt(field):
        return "'%s'" % field

    if not fields:
        return "nothing"
    elif len(fields) == 1:
        return fmt(fields[0])
    elif len(fields) == 2:
        return " and ".join([fmt(f) for f in fields])
    else:
        result = ", ".join([fmt(f) for f in fields[:-1]])
        if oxford:
            result += ","
        result += " and %s" % fmt(fields[-1])
        return result


class BugzillaProcessor(BaseProcessor):
    __name__ = "bugzilla"
    __description__ = "Red Hat Bugzilla"
    __link__ = "https://bugzilla.redhat.com"
    __icon__ = "https://apps.fedoraproject.org/img/icons/bugzilla.png"
    __docs__ = "https://bugzilla.redhat.com"
    __obj__ = "Bug Updates"

    def _email_to_fas(self, email, **config):
        user = email2fas(email, **config)

        if '@' in user:
            is_fas = False
        else:
            is_fas = True

        return user, is_fas

    def _get_user(self, msg, **config):
        email = msg['msg']['event'].get('who')
        if not email:
            email = msg['msg']['bug'].get('creator')

        user, is_fas = self._email_to_fas(email, **config)
        return user, is_fas

    def link(self, msg, **config):
        return msg['msg']['bug']['weburl']

    def subtitle(self, msg, **config):
        user, is_fas = self._get_user(msg, **config)
        idx = msg['msg'].get('bug', {}).get('id')
        title = msg['msg'].get('bug', {}).get('summary')

        if len(title) > MAX_LEN:
            title = title[:MAX_LEN] + "..."

        if 'bug.update' in msg['topic']:
            fields = [d['field_name'] for d in msg['msg']['event']['changes']]
            fields = comma_join(fields)
            tmpl = self._("{user} updated {fields} on RHBZ#{idx} '{title}'")
            return tmpl.format(user=user, fields=fields, idx=idx, title=title)
        elif 'bug.new' in msg['topic']:
            tmpl = self._("{user} filed a new bug RHBZ#{idx} '{title}'")
            return tmpl.format(user=user, idx=idx, title=title)

    def secondary_icon(self, msg, **config):
        user, is_fas = self._get_user(msg, **config)
        if is_fas:
            return gravatar_url(user)
        else:
            return gravatar_url_from_email(user)

    def _gather_emails(self, msg):
        users = set()
        msg = msg['msg']
        bug = msg['bug']

        users.add(msg['event'].get('who'))
        users.add(bug.get('creator'))
        users.add(bug.get('assigned_to'))

        for email in bug['cc']:
            users.add(email)

        # Strip anything that made it in erroneously
        for user in list(users):
            if not user:
                users.remove(user)
                continue
            if user.endswith('lists.fedoraproject.org'):
                users.remove(user)
                continue

        return users

    def usernames(self, msg, **config):
        emails = self._gather_emails(msg)
        users = set()
        for email in emails:
            user, is_fas = self._email_to_fas(email, **config)
            if is_fas:
                users.add(user)
        return users

    def objects(self, msg, **config):
        return set([
            '/'.join([
                msg['msg']['bug']['product'],
                msg['msg']['bug']['component'],
                str(msg['msg']['bug']['id']),
            ])
        ])
