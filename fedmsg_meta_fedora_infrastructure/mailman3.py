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
from fasshim import gravatar_url_from_email

import email.utils
import warnings


def _full_email_to_email(full_from):
    return email.utils.parseaddr(full_from)[1]


def _email_to_username(email):
    # TODO -- use FAS to lookup a user from their email address.
    return email.split('@')[0]


class MailmanProcessor(BaseProcessor):
    __name__ = "Mailman"
    __description__ = "mailing list messages"
    __link__ = "https://lists.fedoraproject.org"
    __docs__ = "http://fedoraproject.org/wiki/" + \
        "Communicating_and_getting_help#Mailing_Lists"
    __obj__ = "Mailing List Messages"
    __icon__ = "http://cloud.ohloh.net/attachments/37686/mailman_med.png"

    def subtitle(self, msg, **config):
        if 'receive' in msg['topic']:
            lst = msg['msg']['mlist']['list_name']
            subject = msg['msg']['msg']['subject']

            full_from = msg['msg']['msg']['from']
            user = _email_to_username(_full_email_to_email(full_from))
            if not user:
                user = "someone"

            d = msg['msg']['msg']
            if d['references'] or d['in-reply-to']:
                tmpl = self._(
                    "On the {lst} list, {user} replied to '{subject}'")
            else:
                tmpl = self._("{user} wrote '{subject}' to the {lst} list")

            return tmpl.format(lst=lst, user=user, subject=subject)
        else:
            warnings.warn("mailman3 message *must* have 'receive' in topic")

    def secondary_icon(self, msg, **config):
        full_from = msg['msg']['msg']['from']
        email = _full_email_to_email(full_from)
        return gravatar_url_from_email(email)

    def link(self, msg, **config):
        base_url = 'https://lists.fedoraproject.org/hyperkitty'
        return base_url + msg['msg']['msg']['archived-at']

    def usernames(self, msg, **config):
        full_from = msg['msg']['msg']['from']
        user = _email_to_username(_full_email_to_email(full_from))
        if user:
            return set([user])
        else:
            return set()

    def objects(self, msg, **config):

        # Build a repr of all the messages in this thread
        references = msg['msg']['msg']['references']

        # Fall back to this header if there's nothing in the first.
        if not references:
            references = msg['msg']['msg']['in-reply-to']

        references = references and references.split() or []
        references = [r[1:-1] for r in references]
        message_id = msg['msg']['msg']['message-id'][1:-1]

        if references:
            tokens = ['/'.join(references), message_id, 'message']
        else:
            tokens = [message_id, 'message']

        return set(['/'.join(tokens)])
