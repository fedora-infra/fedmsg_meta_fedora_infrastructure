# This file is part of fedmsg.
# Copyright (C) 2018 Red Hat, Inc.
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
# Authors:  Aurelien Bompard <abompard@fedoraproject.org>
#
from fedmsg_meta_fedora_infrastructure import BaseProcessor
from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url

from fedmsg_meta_fedora_infrastructure.conglomerators import \
        hubs as hubs_conglomerator


class HubsProcessor(BaseProcessor):
    __name__ = "Hubs"
    __description__ = "Fedora Hubs"
    __link__ = "https://hubs.fedoraproject.org"
    __docs__ = "https://fedoraproject.org/wiki/Fedora_Hubs"
    __obj__ = "Hubs changes"
    __icon__ = "https://hubs.fedoraproject.org/static/img/favicon.png"

    conglomerators = [
        hubs_conglomerator.HubUpdated,
        hubs_conglomerator.WidgetUpdated,
    ]

    def handle_msg(self, msg, **config):
        result = super(HubsProcessor, self).handle_msg(msg, **config)
        if result is None:
            return None
        # Ignore stream hub actions, it's kind of private anyway.
        if msg["msg"].get("hub_type") == "stream":
            return None
        ## Ignore a user's action on their own hub
        #if (msg["msg"].get("hub_type") == "user" and
        #    msg["msg"].get("hub_name") == msg["msg"].get("username")):
        #    return None
        return result

    def subtitle(self, msg, **config):
        if 'hubs.user.created' in msg['topic']:
            user = msg['msg']["username"]
            tmpl = self._(
                "New Hubs user: {user}"
            )
            return tmpl.format(user=user)
        elif 'hubs.user.role.added' in msg['topic']:
            hub = msg['msg']["hub_name"]
            user = msg['msg']["username"]
            role = msg['msg']["role"]
            tmpl = self._(
                "{user} has joined hub {hub} as {role}"
            )
            return tmpl.format(user=user, hub=hub, role=role)
        elif 'hubs.user.role.changed' in msg['topic']:
            hub = msg['msg']["hub_name"]
            user = msg['msg']["username"]
            old_role = msg['msg']["old_role"]
            role = msg['msg']["role"]
            tmpl = self._(
                "{user}'s role on hub {hub} changed from {old_role} "
                "to {role}"
            )
            return tmpl.format(
                user=user, hub=hub, role=role, old_role=old_role)
        elif 'hubs.user.role.removed' in msg['topic']:
            hub = msg['msg']["hub_name"]
            user = msg['msg']["username"]
            role = msg['msg']["role"]
            tmpl = self._(
                "{user}'s role {role} on hub {hub} was removed"
            )
            return tmpl.format(user=user, hub=hub, role=role)
        elif 'hubs.hub.created' in msg['topic']:
            hub = msg['msg']["hub_name"]
            tmpl = self._(
                "New hub: {hub}"
            )
            return tmpl.format(hub=hub)
        elif 'hubs.hub.updated' in msg['topic']:
            hub = msg['msg']["hub_name"]
            tmpl = self._(
                "Hub {hub}'s configuration was changed"
            )
            return tmpl.format(hub=hub)
        elif 'hubs.widget.updated' in msg['topic']:
            hub = msg['msg']["hub_name"]
            widget = msg['msg']["widget_label"]
            tmpl = self._(
                "On hub {hub}, the configuration for widget \"{widget}\" "
                "was changed"
            )
            return tmpl.format(hub=hub, widget=widget)
        else:
            raise NotImplementedError("%r" % msg)

    def secondary_icon(self, msg, **config):
        user = msg['msg'].get("username")
        if user:
            return avatar_url(user)
        else:
            return self.__icon__

    def link(self, msg, **config):
        hub_url = msg['msg'].get("hub_url")
        if hub_url:
            return hub_url
        user = msg['msg'].get("username")
        if user:
            return "/".join([self.__link__, "u", user]) + "/"
        return None

    def usernames(self, msg, **config):
        usernames = set()
        user = msg['msg'].get("username")
        if user:
            usernames.add(user)
        hub = msg['msg'].get("hub_name")
        if hub and msg['msg'].get("hub_type") == "user":
            usernames.add(hub)
        return usernames

    def objects(self, msg, **config):
        result = set()
        hub = msg['msg'].get("hub_name")
        if hub:
            result.add("hubs/{}".format(hub))
        user = msg['msg'].get("username")
        if user:
            result.add("users/{}".format(user))
        return result
