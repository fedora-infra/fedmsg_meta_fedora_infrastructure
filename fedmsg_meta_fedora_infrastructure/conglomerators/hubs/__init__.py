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
import fedmsg.meta.base


class HubUpdated(fedmsg.meta.base.BaseConglomerator):

    def can_handle(self, msg, **config):
        return '.hubs.hub.updated' in msg['topic']

    def matches(self, a, b, **config):
        return (
            a['msg'].get('agent') == b['msg'].get('agent') and
            a['msg']['hub_id'] == b['msg']['hub_id']
        )

    def merge(self, constituents, subject, **config):
        N = len(constituents)
        first_msg = constituents[0]['msg']
        hub = first_msg["hub_name"]
        agent = first_msg.get('agent')
        tmpl = self.produce_template(constituents, subject, **config)
        if agent:
            subtitle = "{agent} changed hub {hub}'s configuration {N} times"
            subjective = "You changed hub {hub}'s configuration {N} times"
        else:
            subtitle = "Hub {hub}'s configuration was changed {N} times"
            subjective = subtitle
        tmpl['subtitle'] = subtitle.format(hub=hub, agent=agent, N=N)
        tmpl['subjective'] = subjective.format(hub=hub, N=N)
        tmpl['secondary_icon'] = self.processor.__icon__
        tmpl['link'] = first_msg.get("hub_url")
        return tmpl


class WidgetUpdated(fedmsg.meta.base.BaseConglomerator):

    def can_handle(self, msg, **config):
        return '.hubs.widget.updated' in msg['topic']

    def matches(self, a, b, **config):
        return (
            a['msg'].get('agent') == b['msg'].get('agent') and
            a['msg']['hub_id'] == b['msg']['hub_id'] and
            a['msg']['widget_id'] == b['msg']['widget_id']
        )

    def merge(self, constituents, subject, **config):
        N = len(constituents)
        first_msg = constituents[0]['msg']
        hub = first_msg["hub_name"]
        widget = first_msg["widget_label"]
        agent = first_msg.get('agent')
        tmpl = self.produce_template(constituents, subject, **config)
        if agent:
            subtitle = (
                "{agent} changed the configuration for widget \"{widget}\" "
                "on hub {hub} {N} times"
            )
            subjective = (
                "You changed the configuration for widget \"{widget}\" "
                "on hub {hub} {N} times"
            )
        else:
            subtitle = (
                "On hub {hub}, the configuration for widget \"{widget}\" "
                "was changed {N} times"
            )
            subjective = subtitle
        tmpl['subtitle'] = subtitle.format(
            hub=hub, widget=widget, agent=agent, N=N)
        tmpl['subjective'] = subjective.format(hub=hub, widget=widget, N=N)
        tmpl['secondary_icon'] = self.processor.__icon__
        tmpl['link'] = first_msg.get("hub_url")
        return tmpl
