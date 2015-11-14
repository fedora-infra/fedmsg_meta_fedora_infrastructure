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

from fedmsg_meta_fedora_infrastructure import BaseProcessor


import fedmsg.meta.base

def get_packages(message):
    ''' Returns the list of all the packages mentionned in the message. '''
    pkgs = set()
    for category in message['msg']['differences']:
        for action in message['msg']['differences'][category]:
            for details in message['msg']['differences'][category][action]:
                if '/' in details[0]:
                    pkgs.add(details[-1])
                else:
                    pkgs.add(details[0])
    return pkgs

def get_summary(message):
    ''' Returns a summary of the addition/deletion for each category in
    the specified message.
    '''
    summary = list()
    for category in message['msg']['differences']:
        cnt_a = len(message['msg']['differences'][category]['added'])
        cnt_d = len(message['msg']['differences'][category]['removed'])
        summary.append('{}: +{}/-{}'.format(category, cnt_a, cnt_d))
    return summary


class MdapiProcessor(BaseProcessor):
    __name__ = "mdapi"
    __description__ = "the Fedora repository meta-data API"
    __link__ = "https://apps.fedoraproject.org/mdapi"
    __docs__ = "https://apps.fedoraproject.org/mdapi"
    __obj__ = "Medata API update"
    __icon__ = ("https://apps.fedoraproject.org/packages/"
                "images/icons/package_128x128.png")

    def subtitle(self, msg, **config):
        if 'mdapi.repo.update' in msg['topic']:
            tmpl = self._(
                u"mdapi meta-data update: {summary}"
            )
            summary = ', '.join(get_summary(msg))
            return tmpl.format(summary=summary)
        else:
            raise NotImplementedError("%r" % msg)

    def secondary_icon(self, msg, **config):
        return ""

    def link(self, msg, **config):
        return "https://apps.fedoraproject.org/mdapi"

    def objects(self, msg, **config):
        objs = set()

        if 'mdapi.repo.update' in msg['topic']:
            objs.add('mdapi/repo/update')

        return objs

    def packages(self, msg, **config):
        packages = set()

        if 'mdapi.repo.update' in msg['topic']:
            packages.update(get_packages(msg))

        return packages
