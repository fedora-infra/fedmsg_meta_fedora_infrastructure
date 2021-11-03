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

from fedmsg_meta_fedora_infrastructure.fasshim import \
        avatar_url, avatar_url_from_email, email2fas
from fedmsg_meta_fedora_infrastructure import BaseProcessor

MAX_LEN = 40

bz_components_that_are_not_packages = [
    'Package Review',
    # ... can you think of any others?
]


def comma_join(fields, oxford=True):
    """ Join together words. """

    def fmt(field):
        return "'%s'" % field

    if not fields:
        # this indicates a bugzilla bug: see
        # https://bugzilla.redhat.com/show_bug.cgi?id=1718045
        return "nothing? (likely bugzilla sent us a buggy message)"
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
        comment = msg['msg'].get('comment')
        event = msg['msg'].get('event')
        if comment:
            email = comment['author']
        elif event and event.get('who'):
            email = event.get('who')
        else:
            email = msg['msg']['bug'].get('creator')

        user, is_fas = self._email_to_fas(email, **config)
        return user, is_fas

    def link(self, msg, **config):
        url = msg['msg']['bug'].get('weburl')
        if not url:
            # bz5 / bugzilla2fedmsg 0.3.1+ messages do not always
            # provide this. we don't seem to have bugzilla2fedmsg in
            # staging at all so let's just assume prod.
            url = "https://bugzilla.redhat.com/show_bug.cgi?id={0}"
            url = url.format(msg['msg']['bug']['id'])
        return url

    def subtitle(self, msg, **config):
        user, is_fas = self._get_user(msg, **config)
        idx = msg['msg'].get('bug', {}).get('id')
        title = msg['msg'].get('bug', {}).get('summary')
        event = msg['msg'].get('event', {})

        if len(title) > MAX_LEN:
            title = title[:MAX_LEN] + "..."

        # bugzilla2fedmsg 0.3.1's 'new bug' detection was broken and
        # it sent bug.update messages for bug creation events, so we
        # catch those with the second condition here
        if 'bug.new' in msg['topic'] or (event.get('target') == 'bug' and
                                         event.get('action') == 'create'):
            tmpl = self._("{user} filed a new bug RHBZ#{idx} '{title}'")
            return tmpl.format(user=user, idx=idx, title=title)

        if msg['msg'].get('comment'):
            tmpl = self._("{user} commented on RHBZ#{idx} '{title}'")
            return tmpl.format(user=user, idx=idx, title=title)
        elif event:
            fields = [d['field_name'] for d in
                      event['changes']]
            fields = comma_join(fields)
            tmpl = self._("{user} updated {fields} "
                          "on RHBZ#{idx} '{title}'")
            return tmpl.format(user=user, fields=fields,
                               idx=idx, title=title)
        else:
            tmpl = self._("{user} updated RHBZ#{idx} '{title}'")
            return tmpl.format(user=user, idx=idx, title=title)

    def secondary_icon(self, msg, **config):
        user, is_fas = self._get_user(msg, **config)
        if is_fas:
            return avatar_url(user)
        else:
            return avatar_url_from_email(user)

    def _gather_emails(self, msg):
        users = set()
        msg = msg['msg']
        bug = msg['bug']

        if msg.get('comment'):
            author = msg['comment'].get('author')
            if author:
                users.add(author)

        if msg.get('event'):
            who = msg['event'].get('who')
            if who:
                users.add(who)

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

    def packages(self, msg, **config):
        component = msg['msg']['bug']['component']
        if component in bz_components_that_are_not_packages:
            return set()
        return set([component])

    def usernames(self, msg, **config):
        emails = self._gather_emails(msg)
        users = set()
        for email in emails:
            user, is_fas = self._email_to_fas(email, **config)
            if is_fas:
                users.add(user)
        return users

    def objects(self, msg, **config):
        product = msg['msg']['bug']['product']
        component = msg['msg']['bug']['component']
        # in bugzilla2fedmsg 0.3.1 messages and 0.4+ messages without
        # backwards compatibility, 'product' and 'component' are dicts
        # and we have to go one level deeper
        try:
            product = product['name']
            component = component['name']
        except TypeError:
            pass
        return set([
            '/'.join([
                product,
                component,
                str(msg['msg']['bug']['id']),
            ])
        ])
