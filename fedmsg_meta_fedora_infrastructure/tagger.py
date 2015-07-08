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

from fedmsg_meta_fedora_infrastructure.conglomerators.tagger \
    import tags as tagger_tags

class TaggerProcessor(BaseProcessor):
    __name__ = "fedoratagger"
    __description__ = "the Fedora package labeller/tagger"
    __link__ = "https://apps.fedoraproject.org/tagger"
    __docs__ = "https://github.com/ralphbean/fedora-tagger"
    __icon__ = "https://apps.fedoraproject.org/img/icons/tagger.png"
    __obj__ = "Package Tag Votes"

    conglomerators = [
        tagger_tags.UpdateByUser,
        tagger_tags.CreateByUser,
    ]

    def link(self, msg, **config):
        vote = msg.get('msg', {}).get('vote', {})
        pack = vote.get('tag', {}).get('package', None)

        # Backwards compat with old tagger messages
        if hasattr(pack, 'keys'):
            pack = list(pack.keys())[0]

        if not pack and 'rating' in msg['msg']:
            pack = msg['msg']['rating']['package']['name']

        if 'package' in msg['msg']:
            pack = msg['msg']['package']['name']

        if pack:
            return "https://apps.fedoraproject.org/tagger/" + pack
        else:
            return ""

    def subtitle(self, msg, **config):
        if 'fedoratagger.tag.update' in msg['topic']:
            user = msg['msg']['vote']['user']['username']
            tag = msg['msg']['vote']['tag']['tag']
            package = msg['msg']['vote']['tag']['package']

            # Backwards compat with old tagger messages
            if hasattr(package, 'keys'):
                package = list(package.keys())[0]

            if msg['msg']['vote']['like']:
                verb = "up"
            else:
                verb = "down"

            tmpl = self._('{user} {verb}voted "{tag}" on {package}')
            return tmpl.format(user=user, tag=tag, verb=verb, package=package)
        elif 'fedoratagger.rating.update' in msg['topic']:
            user = msg['msg']['rating']['user']
            if user.get('anonymous', False):
                user = self._('An anonymous user')
            else:
                user = user['username']
            package = msg['msg']['rating']['package']['name']
            rating = msg['msg']['rating']['rating']
            tmpl = self._('{user} gave {package} a rating of {rating}')
            return tmpl.format(user=user, package=package, rating=rating)
        elif 'fedoratagger.tag.create' in msg['topic']:
            user = msg['msg']['vote']['user']['username']
            tag = msg['msg']['vote']['tag']['tag']
            package = msg['msg']['vote']['tag']['package']

            # Backwards compat with old tagger messages
            if hasattr(package, 'keys'):
                package = list(package.keys())[0]

            tmpl = self._('{user} added tag "{tag}" to {package}')
            return tmpl.format(user=user, tag=tag, package=package)
        elif 'fedoratagger.user.rank.update' in msg['topic']:
            user = msg['msg']['user']['username']
            rank = msg['msg']['user']['rank']
            tmpl = self._("{user}'s rank changed to {rank}")
            return tmpl.format(user=user, rank=rank)
        elif 'fedoratagger.usage.toggle' in msg['topic']:
            user = msg['msg']['user']
            if user.get('anonymous', False):
                user = self._('An anonymous user')
            else:
                user = user['username']
            package = msg['msg']['package']['name']
            if msg['msg']['usage']:
                tmpl = self._(
                    "{user} declared that they use {package}")
            else:
                tmpl = self._(
                    "{user} declared that they no longer use {package}")
            return tmpl.format(user=user, package=package)
        else:
            raise NotImplementedError("%r" % msg)

    def secondary_icon(self, msg, **config):
        usernames = self.usernames(msg, **config)
        if usernames:
            return avatar_url(list(usernames)[0])
        else:
            return self.__icon__

    def usernames(self, msg, **config):
        user = 'anonymous'
        if 'fedoratagger.tag.' in msg['topic']:
            user = msg['msg']['vote']['user']['username']
        elif 'fedoratagger.user.rank.update' in msg['topic']:
            user = msg['msg']['user']['username']
        elif 'fedoratagger.rating.update' in msg['topic']:
            user = msg['msg']['rating']['user']['username']
        elif 'fedoratagger.usage.toggle' in msg['topic']:
            user = msg['msg']['user']['username']

        if user is 'anonymous':
            return set()
        else:
            return set([user])

    def packages(self, msg, **config):
        if 'fedoratagger.tag.' in msg['topic']:
            package = msg['msg']['vote']['tag']['package']

            # Backwards compat with old tagger messages
            if hasattr(package, 'keys'):
                package = list(package.keys())[0]

            return set([package])
        elif 'fedoratagger.rating.update' in msg['topic']:
            package = msg['msg']['rating']['package']['name']
            return set([package])
        elif 'fedoratagger.usage.toggle' in msg['topic']:
            package = msg['msg']['package']['name']
            return set([package])

        return set()

    def objects(self, msg, **config):
        packages = self.packages(msg, **config)
        objs = set(['packages/' + p for p in packages])
        if 'vote' in msg['msg']:
            objs.add('labels/' + msg['msg']['vote']['tag']['tag'])
        return objs
