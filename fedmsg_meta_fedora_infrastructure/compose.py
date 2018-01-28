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


class ComposeProcessor(BaseProcessor):
    __name__ = "compose"
    __description__ = "Fedora Release Engineering"
    __link__ = "https://pagure.io/releng"
    __docs__ = "https://pagure.io/docs/releng"
    __obj__ = "Composes"

    # dicts mapping topic substrings to subtitle event texts
    # These are the old 'make-updates' topics
    makeupevents = {
        '.make-updates.':       "",
        '.cloudimg-build.':     " building images for",
        '.mash-atomic':         " Atomic updates mash for",
        '.atomic-lorax':        " Atomic lorax run for",
        '.cloudimg-checksum.':  " image checksum generation for",
        '.cloudimg-staging.':   " master mirror publication for",
    }
    # as these events only existed prior to pungi 4 and the creation
    # of different 'dists', we can always treat the shortname / dist
    # as 'Fedora' for these
    oldevents = {
        '.mash.':               " mashing",
        '.pungify.':            " building boot.iso for",
        '.image.':              " building other images for",
    }
    oldevents.update(makeupevents)
    # These ones existed after pungi 4, so we cannot make inferences
    # about the dist / shortname; bare 'start' and 'complete' are
    # implicitly in this set too
    events = {
        '.rsync.':              " master mirror publication for",
    }
    allevents = dict()
    allevents.update(oldevents)
    allevents.update(events)

    def subtitle(self, msg, **config):

        # decide what event we're dealing with
        gotevent = False
        for event in self.allevents:
            if event in msg['topic']:
                gotevent = True
                evtext = self.allevents[event]
                # allow definition of event to leak
                break
        if not gotevent:
            # assume this is an overall compose start/done event
            event = 'compose'
            evtext = ''

        # discover the release number, if we can
        release = "(unknown release)"
        try:
            # 'branch' key is usually the release identifier (number or
            # 'rawhide' or 'bikeshed'), but for a while for modular
            # composes it was 'Modular-(release)', so handle that
            release = msg['msg']['branch'].split('Modular-')[-1].capitalize()
        except KeyError:
            # Some old messages in datanommer don't have that branch field,
            # so we have to extract it from the topic.
            comps = msg['topic'].split('.')
            if 'rawhide' in comps:
                release = "Rawhide"
            elif 'epelbeta' in comps:
                release = "EPEL Beta"
            else:
                # I'm not sure this is ever actually the case - a message with
                # a release number in the topic, but no 'branch' key - but
                # just in case, let's handle it
                for comp in comps:
                    if len(comp) == 2 and comp.isdigit():
                        release = comp
                        break

        # for old secondary arches, discover the arch and pad it
        arch = msg['msg'].get('arch', '')
        arch = arch and ' (%s)' % arch

        # set up compose ID text, if we have one
        if event in self.makeupevents:
            comptext = "post-release Cloud/Atomic/Docker respin compose"
        else:
            comptext = "compose"
        cid = msg['msg'].get('compose_id', '')
        if cid:
            comptext += " %s" % cid

        # Try to figure out the 'shortname', if we can, which differentiates
        # various types of compose
        try:
            short = msg['msg']['short']
        except KeyError:
            # default value
            short = 'Fedora'
            # this identifies modular composes before we added 'short' key
            if 'modular' in msg['msg'].get('branch', '').lower():
                short = 'Fedora-Modular'
            # these are known ambiguous: these messages could be for a
            # branched compose (Fedora), or a post-release Fedora-Atomic,
            # Fedora-Cloud or Fedora-Docker respin. If the message has a
            # compose_id but not a short, it must be for Fedora (we fixed
            # inclusion of compose_id for the other shortnames at the
            # same time we added the short key). If the message has an
            # arch it must be for Fedora (separate secondary arch composes
            # went away with the Pungi 4 migration which added shortnames).
            # 'branched' messages must be for Fedora as we switched to
            # numeric topics with the Pungi 4 migration.
            if release.isdigit() and event not in self.oldevents:
                if 'compose_id' not in msg['msg'] and not arch and 'branched' not in msg['topic']:
                    short = 'Fedora, Fedora-Atomic, Fedora-Cloud or Fedora-Docker'

        # Set the 'action' text; note we do not use the 'log' value
        # here because it's sometimes a lie, e.g. mash-atomic.stop
        # messages have their 'log' value as 'start'
        action = 'Did something to do with'
        actsplit = msg['topic'].split('.')[-1]
        if actsplit == 'start':
            action = 'Started'
        elif actsplit in ('complete', 'done', 'stop'):
            action = 'Completed'

        # Finally, construct the message
        tmpl = "{action}{evtext} {short} {release}{arch} {comptext}"
        return tmpl.format(action=action, evtext=evtext, short=short, release=release,
                           arch=arch, comptext=comptext)

    def link(self, msg, **config):
        return msg['msg'].get('location', 'https://kojipkgs.fedoraproject.org/compose/')

    def objects(self, msg, **config):
        branch = msg['topic'].split('.')[4]
        arch = msg['msg'].get('arch', '')
        arch = arch or 'primary'
        return set(["%s/%s" % (branch, arch)])
