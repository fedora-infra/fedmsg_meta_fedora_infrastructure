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
#           Ralph Bean <rbean@redhat.com>
#

from fedmsg_meta_fedora_infrastructure import BaseProcessor

import fedmsg.meta.base


def get_packages(message):
    ''' Returns the list of all the packages mentionned in the message. '''
    if 'differences' in message['msg']:
        return _get_packages_oldschool(message)
    else:
        return _get_packages_newschool(message)

def _get_packages_oldschool(message):
    pkgs = set()
    for category in message['msg']['differences']:
        for action in message['msg']['differences'][category]:
            for details in message['msg']['differences'][category][action]:
                if '/' in details[0]:
                    name = details[-1]
                else:
                    name = details[0]
                name = name.split('(')[0]
                pkgs.add(name)
    return pkgs


def _get_packages_newschool(message):
    return message['msg']['packages']


def get_objects(message):
    if 'differences' in message['msg']:
        return _get_objects_oldschool(message)
    else:
        return _get_objects_newschool(message)

def _get_objects_oldschool(message):
    repo = message['msg']['name']
    for category in message['msg']['differences']:
        for action in message['msg']['differences'][category]:
            for details in message['msg']['differences'][category][action]:
                if '/' in details[0]:
                    name = details[-1]
                else:
                    name = details[0]
                yield '%s/%s/%s/%s' % (repo, category, action, name)


def _get_objects_newschool(message):
    repo = message['msg']['name']
    for name in message['msg']['packages']:
        yield '%s/%s' % (repo, name)


def get_summary(message):
    ''' Returns a summary of the addition/deletion for each category in
    the specified message.
    '''
    if 'differences' in message['msg']:
        return ', '.join(_get_summary_oldschool(message))
    else:
        return _get_summary_newschool(message)

def _get_summary_oldschool(message):
    summary = list()
    for category in sorted(message['msg']['differences']):
        count_a = len(message['msg']['differences'][category]['added'])
        count_b = len(message['msg']['differences'][category]['removed'])
        if not count_a and not count_b:
            continue
        summary.append('{0}: +{1}/-{2}'.format(category, count_a, count_b))
    return summary

def _get_summary_newschool(message):
    packages = message['msg']['packages']
    return fedmsg.meta.base.BaseConglomerator.list_to_series(packages)

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
                u"mdapi noticed a {repo} repomd change: {summary}"
            )
            repo = msg['msg']['name']
            summary = get_summary(msg)
            return tmpl.format(repo=repo, summary=summary)
        else:
            raise NotImplementedError("%r" % msg)

    def secondary_icon(self, msg, **config):
        return self.__icon__

    def link(self, msg, **config):
        url = msg['msg']['url']
        if url.startswith('http'):
            return url
        else:
            return 'https://download.fedoraproject.org/pub/' + url

    def objects(self, msg, **config):
        return set(get_objects(msg))

    def packages(self, msg, **config):
        return set(get_packages(msg))
