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
#           Luke Macken <lmacken@redhat.com>

import re

from fedmsg_meta_fedora_infrastructure import BaseProcessor
from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url

from fedmsg_meta_fedora_infrastructure.conglomerators.bodhi import \
        requests as bodhi_requests
from fedmsg_meta_fedora_infrastructure.conglomerators.bodhi import \
        comments as bodhi_comments
from fedmsg_meta_fedora_infrastructure.conglomerators.bodhi import \
        overrides as bodhi_overrides


def get_sync_product(msg):
    # Extract the product name from a ftpsync message.
    product = msg['topic'].split('.')[-2]
    if product == 'fedora':
        product = 'Fedora'
    elif product == 'epel':
        product = 'EPEL'
    else:
        pass
    return product


def get_sync_release(msg):
    """Return the release for an ftpsync message, determining if we're
    modular along the way. Returns the release and a boolean for "are
    we modular"
    """
    modular = False
    release = msg['msg']['release']
    if release.endswith('m'):
        modular = True
        release = release.rstrip('m')
    return (release, modular)


def is_ftp_sync(msg):
    """Identify update sync messages. These are not published by bodhi
    itself but by the new-updates-sync script, which lives in the
    ansible infra repo in the bodhi backend role.
    """
    return 'bodhi.updates.' in msg['topic'] and msg['topic'].endswith('.sync')


def truncate(title):
    if len(title) >= 40:
        title = title[:40] + "..."
    return title


def titlestring(msg):
    """ Return a title string for the update. If we can find an
    update dict and it has a title, return that. Otherwise if we
    can find a builds dict, synthesize one from that and return
    it. `title` is not part of the update message schema so we
    cannot technically rely on it being present, but we use this
    style of string in several places, so factor out finding it.
    """
    comment = msg['msg'].get('comment', {})
    update = msg['msg'].get('update', comment.get('update', {}))
    if not update:
        return comment.get('update_title', '')
    title = update.get('title')
    if not title:
        title = ' '.join([build['nvr'] for build in update.get('builds', [])])
    return title


class BodhiProcessor(BaseProcessor):
    __name__ = "Bodhi"
    __description__ = "the Fedora update system"
    __link__ = "https://bodhi.fedoraproject.org/"
    __docs__ = "https://fedoraproject.org/wiki/Bodhi"
    __obj__ = "Package Updates"
    __icon__ = "https://apps.fedoraproject.org/img/icons/bodhi.png"
    conglomerators = [
        bodhi_requests.ByUserAndPackageTesting,
        bodhi_requests.ByUserAndPackageStable,
        bodhi_requests.ByPackage,
        bodhi_requests.ByUser,
        bodhi_comments.ByUpdate,
        bodhi_comments.ByUser,
        bodhi_overrides.ByUserTag,
        bodhi_overrides.ByUserUnTag,
    ]

    def _comment_author(self, msg):
        """Find the author of the 'comment' dict in the message, if
        there is one. Otherwise, return None.
        """
        comment = msg['msg'].get('comment', {})
        author = comment.get('user', comment.get('author'))
        if isinstance(author, dict):
            author = author.get('name')
        return author

    def _update_author(self, msg):
        """Find the author of the 'update' dict in the message, if
        there is one. Otherwise, return None.
        """
        update = msg['msg'].get('update', {})
        author = update.get('user', update.get('submitter'))
        if isinstance(author, dict):
            author = author.get('name')
        return author

    def _override_author(self, msg):
        """Find the author (submitter) of the 'override' dict in the
        message, if there is one. Otherwise, return None.
        """
        author = None
        override = msg['msg'].get('override')
        if override:
            author = override['submitter']
        if isinstance(author, dict):
            author = author['name']
        return author

    def _override_nvr(self, msg):
        """Find the NVR of the 'override' dict in the message, if
        there is one. Otherwise, return None.
        """
        build = msg['msg'].get('override', {}).get('build')
        if isinstance(build, dict):
            return build.get('nvr')
        else:
            return build

    def _u2p(self, nvrstring):
        """ Take a string - expected to be one or more package NVRs,
        split by commas or spaces, e.g. an update title - and return
        a list of just the package names.
        """
        # TODO -- make this unnecessary by having bodhi emit the
        # package name (and not just the update name) to begin with.
        return [build.rsplit('-', 2)[0] for build in re.split('[ ,]', nvrstring)]

    @property
    def _updatetopics(self):
        """ A bunch of update-related message topics. We use this same
        set of topics in several places, so it's factored out here.
        """
        updatetopics = ['comment', 'complete', 'request', 'edit', 'eject', 'karma.threshold',
                         'requirements_met']
        updatetopics = ['bodhi.update.{0}'.format(ut) for ut in updatetopics]
        updatetopics.extend(['bodhi.errata.publish'])
        return tuple(updatetopics)

    def title_or_alias(self, msg):
        comment = msg['msg'].get('comment', {})
        update = msg['msg'].get('update', comment.get('update', {}))
        # we can't use .get('alias', .get('title')) or similar here
        # because sometimes the dict has an alias key whose value is
        # None...
        value = update.get('alias')
        if not value:
            value = update.get('title')
        if not value:
            value = comment.get('update_alias')
        if not value:
            value = comment.get('update_title', '')
        return value

    def secondary_icon(self, msg, **config):
        username = ''
        if 'bodhi.update.comment' in msg['topic']:
            username = self._comment_author(msg)
        elif 'bodhi.buildroot_override' in msg['topic']:
            username = self._override_author(msg)
        elif 'bodhi.stack' in msg['topic']:
            username = msg['msg']['agent']
        elif self._update_author(msg):
            username = self._update_author(msg)
        else:
            username = msg['msg'].get('agent')

        avatar = self.__icon__
        if username:
            avatar = avatar_url(username)
        else:
            # If we don't have a user, then try with a package
            if titlestring(msg):
                packages = self._u2p(titlestring(msg))
                tmpl = 'https://apps.fedoraproject.org/packages/' + \
                    'images/icons/%s.png'
                if packages:
                    avatar = tmpl % packages[0]

        return avatar

    def long_form(self, msg, **config):
        if 'bodhi.update.comment' in msg['topic']:
            return msg['msg']['comment']['text']
        elif 'bodhi.errata.publish' in msg['topic']:
            return msg['msg']['body']
        elif 'bodhi.masher.start' in msg['topic'] or 'bodhi.composer.start' in msg['topic']:
            if 'updates' in msg['msg']:
                return "\n- " + "\n- ".join(msg['msg']['updates']) + "\n"

    def subtitle(self, msg, **config):
        if is_ftp_sync(msg):
            product = get_sync_product(msg)
            (truerelease, modular) = get_sync_release(msg)
            if modular:
                modular = " modular"
            else:
                modular = ""
            msg = msg['msg']
            tmpl = self._(
                'New {product} {truerelease} {repo}{modular} content synced out '
                '({bytes} changed with {deleted} files deleted)')
            return tmpl.format(product=product, truerelease=truerelease, modular=modular, **msg)
        elif 'bodhi.masher.start' in msg['topic'] or 'bodhi.composer.start' in msg['topic']:
            agent = msg['msg']['agent']
            if 'updates' in msg['msg']:
                # pre-Bodhi 3.2.0
                updates = len(msg['msg']['updates'])
                tmpl = self._("{agent} requested a mash of {updates} updates")
                return tmpl.format(agent=agent, updates=updates)
            else:
                # post-Bodhi 3.2.0. These messages are fairly useless:
                # https://github.com/fedora-infra/bodhi/issues/3360
                tmpl = self._("{agent} requested a mash of some updates")
                return tmpl.format(agent=agent)
        elif 'bodhi.update.comment' in msg['topic']:
            comment = msg['msg']['comment']
            author = self._comment_author(msg)
            karma = comment['karma']
            title = comment.get('update_title', comment.get('update', {}).get('title', ''))
            tmpl = self._(
                "{author} commented on bodhi update {title} (karma: {karma})"
            )
            return tmpl.format(author=author, karma=karma,
                               title=truncate(title))

        elif 'bodhi.update.complete.' in msg['topic']:
            update = msg['msg']['update']
            author = self._update_author(msg)
            pkgs = truncate(titlestring(msg))
            status = update['status']
            tmpl = self._(
                "{author}'s {pkgs} bodhi update completed push to {status}"
            )
            return tmpl.format(author=author, pkgs=pkgs, status=status)
        elif 'bodhi.update.eject' in msg['topic']:
            update = msg['msg']['update']
            author = self._update_author(msg)
            pkgs = truncate(titlestring(msg))
            repo = msg['msg']['repo']
            reason = msg['msg']['reason']
            tmpl = self._(
                "{author}'s {pkgs} bodhi update was ejected from "
                "the {repo} mash.  Reason: \"{reason}\"")
            return tmpl.format(author=author, pkgs=pkgs,
                               repo=repo, reason=reason)
        elif 'bodhi.update.edit' in msg['topic']:
            author = msg['msg']['agent']
            pkgs = truncate(titlestring(msg))
            tmpl = self._("{author} edited {pkgs}")
            return tmpl.format(author=author, pkgs=pkgs)
        elif 'bodhi.update.request' in msg['topic']:
            status = msg['topic'].split('.')[-1]
            author = msg['msg'].get('agent')
            title = titlestring(msg)
            if status in ('unpush', 'obsolete', 'revoke'):
                # make our status past-tense
                status = status + (status[-1] == 'e' and 'd' or 'ed')
                tmpl = self._("{author} {status} {title}")
            else:
                tmpl = self._("{author} submitted {title} to {status}")

            return tmpl.format(author=author, title=truncate(title),
                               status=status)
        elif 'bodhi.mashtask.start' in msg['topic']:
            return self._("bodhi masher started a push")
        elif 'bodhi.mashtask.mashing' in msg['topic']:
            repo = msg['msg'].get('repo')
            tmpl = self._("bodhi masher started mashing {repo}")
            return tmpl.format(repo=repo)
        elif 'bodhi.mashtask.complete' in msg['topic']:
            success = msg['msg']['success']
            if success:
                tmpl = self._("bodhi masher successfully mashed {repo}")
            else:
                tmpl = self._("bodhi masher failed to mash {repo}")
            return tmpl.format(repo=msg['msg'].get('repo'))
        elif 'bodhi.mashtask.sync.wait' in msg['topic']:
            return self._("bodhi masher is waiting for {repo} to "
                          "hit the master mirror").format(
                              repo=msg['msg'].get('repo'))
        elif 'bodhi.mashtask.sync.done' in msg['topic']:
            return self._("bodhi masher finished waiting for {repo} to "
                          "hit the master mirror").format(
                              repo=msg['msg'].get('repo'))
        elif 'bodhi.compose.start' in msg['topic']:
            return self._("bodhi composer started a run")
        elif 'bodhi.compose.composing' in msg['topic']:
            ctype = msg['msg'].get('ctype', "unknown type")
            repo = msg['msg'].get('repo', "unknown repo")
            tmpl = self._("bodhi {ctype} compose of repo {repo} started")
            return tmpl.format(ctype=ctype, repo=repo)
        elif 'bodhi.repo.done' in msg['topic']:
            repo = msg['msg'].get('repo', "unknown repo")
            tmpl = self._("bodhi repo {repo} created")
            return tmpl.format(repo=repo)
        elif 'bodhi.compose.complete' in msg['topic']:
            tmpl = self._("bodhi {ctype} compose of repo {repo} {result}")
            ctype = msg['msg'].get('ctype', "unknown type")
            repo = msg['msg'].get('repo', "unknown repo")
            result = msg['msg'].get('success', "completed")
            if result is True:
                result = "succeeded"
            if result is False:
                result = "failed"
            return tmpl.format(ctype=ctype, repo=repo, result=result)
        elif 'bodhi.compose.sync.wait' in msg['topic']:
            return self._("bodhi composer is waiting for {repo} to "
                          "hit the master mirror").format(
                              repo=msg['msg'].get('repo'))
        elif 'bodhi.compose.sync.done' in msg['topic']:
            return self._("bodhi composer finished waiting for {repo} to "
                          "hit the master mirror").format(
                              repo=msg['msg'].get('repo'))

        elif 'bodhi.buildroot_override.tag' in msg['topic']:
            tmpl = self._("{submitter} submitted a buildroot override " +
                          "for {build}")

            submitter = self._override_author(msg)
            build = self._override_nvr(msg)

            return tmpl.format(submitter=submitter, build=build)
        elif 'bodhi.buildroot_override.untag' in msg['topic']:
            tmpl = self._("{submitter} expired a buildroot override " +
                          "for {build}")

            submitter = self._override_author(msg)
            build = self._override_nvr(msg)

            return tmpl.format(submitter=submitter, build=build)
        elif 'bodhi.stack.save' in msg['topic']:
            tmpl = self._("{agent} updated the \"{name}\" stack")
            agent = msg['msg']['agent']
            name = msg['msg']['stack']['name']
            return tmpl.format(agent=agent, name=name)
        elif 'bodhi.stack.delete' in msg['topic']:
            tmpl = self._("{agent} deleted the \"{name}\" stack")
            agent = msg['msg']['agent']
            name = msg['msg']['stack']['name']
            return tmpl.format(agent=agent, name=name)
        elif 'bodhi.update.karma.threshold' in msg['topic']:
            tmpl = self._("{title} reached the {status} karma threshold")
            title = truncate(titlestring(msg))
            status = msg['msg']['status']
            return tmpl.format(title=title, status=status)
        elif 'bodhi.update.requirements_met' in msg['topic']:
            status = msg['topic'].split('.')[-1]
            title = truncate(titlestring(msg))
            tmpl = self._("{title} reached the {status} testing threshold")
            return tmpl.format(title=title, status=status)
        elif 'bodhi.errata.publish' in msg['topic']:
            return msg['msg']['subject']

    def link(self, msg, **config):
        prefix = 'https://bodhi.fedoraproject.org'
        tmpl = prefix + "/updates/{title}"
        if any(utopic in msg['topic'] for utopic in self._updatetopics):
            return tmpl.format(title=self.title_or_alias(msg))
        elif 'bodhi.stack' in msg['topic']:
            return prefix + "/stacks/{title}".format(
                title=msg['msg']['stack']['name'])
        elif 'bodhi.buildroot_override' in msg['topic']:
            build = self._override_nvr(msg)
            return prefix + "/overrides/{nvr}".format(nvr=build)
        elif is_ftp_sync(msg):
            link = "https://download.fedoraproject.org/pub/"
            repo = msg['msg']['repo']
            (release, ismodular) = get_sync_release(msg)
            product = get_sync_product(msg).lower()
            link += product + "/"

            if product == 'fedora':
                if repo == 'atomic':
                    link += "linux/atomic/"
                else:
                    link += "linux/updates/"

            if repo.endswith('testing'):
                link += "testing/"

            link += release + "/"

            if ismodular:
                link += "Modular/"
            elif release.isdigit():
                if (product == 'fedora' and int(release) > 27) or (product == 'epel' and
                                                                   int(release) > 7):
                    link += "Everything/"

            return link
        else:
            return "https://bodhi.fedoraproject.org"

    def packages(self, msg, **config):
        if any(utopic in msg['topic'] for utopic in self._updatetopics):
            return set(self._u2p(titlestring(msg)))
        elif 'bodhi.buildroot_override.' in msg['topic']:
            nvr = self._override_nvr(msg)
            return set(self._u2p(nvr))
        elif 'bodhi.stack' in msg['topic']:
            return set([p['name'] for p in msg['msg']['stack']['packages']])
        elif 'bodhi.masher.start' in msg['topic']:
            # this is flattening a list-of-lists into a list then turning it
            # into a set
            return set(sum([
                self._u2p(update) for update in msg['msg'].get('updates', [])
            ], []))

        return set()

    def usernames(self, msg, **config):
        users = []

        users.append(self._comment_author(msg))
        users.append(self._update_author(msg))
        users.append(self._override_author(msg))

        if 'comment' in msg['msg']:
            text = msg['msg']['comment']['text']
            mentions = re.findall('@\w+', text)
            for mention in mentions:
                users.append(mention[1:])

        if 'agent' in msg['msg']:
            users.append(msg['msg']['agent'])

        # Strip out None values.  In some cases, we're getting None values
        # here.. I think from the 'agent' field of an anonymous bodhi comment.
        users = [u for u in users if u is not None]

        return set(users)

    def objects(self, msg, **config):
        # for all of these, 'objects' includes the repo
        repotopics = ('bodhi.mashtask', 'bodhi.compose', 'bodhi.repo.done')
        # for all of these, 'objects' includes discoverable package names
        packagetopics = list(self._updatetopics)
        packagetopics.append('bodhi.masher.start')

        if is_ftp_sync(msg):
            product = get_sync_product(msg).lower()
            (release, _) = get_sync_release(msg)
            msg = msg['msg']
            return set(['/'.join([product, msg['repo'], release])])
        elif 'repo' in msg['msg'] and any(rtopic in msg['topic'] for rtopic in repotopics):
            return set(['repos/' + msg['msg']['repo']])
        elif any(ptopic in msg['topic'] for ptopic in packagetopics):
            return set([
                'packages/' + p for p in
                self.packages(msg, **config)
            ])
        elif 'bodhi.buildroot_override.' in msg['topic']:
            nvr = self._override_nvr(msg)
            return set([
                'packages/' + p for p in
                self._u2p(nvr)
            ])
        elif 'bodhi.stack' in msg['topic']:
            return set(
                [
                    'packages/' + p['name']
                    for p in msg['msg']['stack']['packages']
                ] + ['stacks/' + msg['msg']['stack']['name']]
            )

        return set()
