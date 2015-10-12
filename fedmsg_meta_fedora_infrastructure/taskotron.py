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
# Authors:  Martin Krizek <mkrizek@redhat.com>
#
from fedmsg_meta_fedora_infrastructure import BaseProcessor


class TaskotronProcessor(BaseProcessor):
    __name__ = "taskotron"
    __description__ = "Framework for automated task execution"
    __link__ = "https://taskotron.fedoraproject.org/"
    __docs__ = "https://docs.qadevel.cloud.fedoraproject.org/libtaskotron/latest/"
    __obj__ = "Automated task results"
    __icon__ = "https://apps.fedoraproject.org/img/icons/taskotron.png"

    def subtitle(self, msg, **config):
        if msg['topic'].endswith('taskotron.result.new'):
            taskname = msg['msg']['task'].get('name', '')
            outcome = msg['msg']['result'].get('outcome', '')
            taskitem = msg['msg']['task'].get('item', '')
            return '%s %s for %s' % (taskname, outcome, taskitem)

    def link(self, msg, **config):
        if msg['topic'].endswith('taskotron.result.new'):
            return msg['msg']['result'].get('log_url', '')

    def secondary_icon(self, msg, **config):
        return self.__icon__
