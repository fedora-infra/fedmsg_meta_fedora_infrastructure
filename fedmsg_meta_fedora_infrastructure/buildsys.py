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

import fedmsg.meta.base

import copy
import datetime
from pytz import UTC

try:
    import koji
except ImportError:
    koji = None


_build_template = """Package:    {name}-{version}-{release}
Status:     {status}
Built by:   {owner_name}
ID:         {id}
Started:    {started}
Finished:   {finished}

"""

_task_header_template = """Task {id} on {build_host}
Task Type: {method} ({arch})
Link: {url}
"""

import logging
log = logging.getLogger('fedmsg.meta.buildsys')


class KojiProcessor(BaseProcessor):
    __name__ = "buildsys"
    __description__ = "the Fedora build system"
    __link__ = "http://koji.fedoraproject.org/koji"
    __docs__ = "https://fedoraproject.org/wiki/Using_the_Koji_build_system"
    __obj__ = "Koji Builds"
    __icon__ = ("https://fedoraproject.org/w/uploads/2/20/"
                "Artwork_DesignService_koji-icon-48.png")

    @classmethod
    def _fill_task_template(cls, sess, taskid):
        file_base = 'https://kojipkgs.fedoraproject.org/work/'

        info = sess.getTaskInfo(taskid)
        if info['host_id'] is None:
            info['build_host'] = '(unscheduled)'
        else:
            host = sess.getHost(info['host_id'])
            info['build_host'] = host['name']

        weburl = sess.baseurl.rsplit('/', 1)[0] + '/koji/'
        info['url'] = weburl + 'taskinfo?taskID=%i' % info['id']

        retval = _task_header_template.format(**info)

        result = None
        try:
            result = sess.getTaskResult(taskid)
        except Exception as e:
            log.warning(unicode(e))
            retval += "\n" + unicode(e) + "\n"

        if result:
            for kind in ['logs', 'rpms', 'srpms']:
                if kind in result:
                    retval += kind + ":\n"
                    for item in result[kind]:
                        retval += "  " + file_base + item + "\n"

            for kind in ['srpm']:
                if kind in result:
                    retval += kind + ":\n  " + file_base + result[kind] + "\n"

        children = sess.getTaskChildren(taskid)
        for child in sorted(children, key=lambda d: d['completion_ts']):
            retval += "\n" + cls._fill_task_template(sess, child['id'])

        return retval

    @classmethod
    def _fill_build_template(cls, sess, build):
        full_build = sess.getBuild(build['build_id'])

        # We *often* hit a race condition with koji here.
        # It publishes the fedmsg message before it has committed the details
        # its database.  When we receive the message, we here try to query koji
        # for more details but... the fedmsg got to us before the db commit
        # finished and koji says "I know nothing."
        if not full_build:
            errmsg = "    Failed to retrieve further details about %r"
            return errmsg % build['build_id']

        lookup = dict(zip(*zip(*koji.BUILD_STATES.items())[::-1]))
        full_build['status'] = lookup[full_build['state']].lower()

        fmt = '%a, %d %b %Y %H:%M:%S %Z'

        try:
            dt = datetime.datetime.fromtimestamp(
                full_build['creation_ts'], UTC).strftime(fmt)
        except TypeError:
            dt = ''
        full_build['started'] = dt

        try:
            dt = datetime.datetime.fromtimestamp(
                full_build['completion_ts'], UTC).strftime(fmt)
        except TypeError:
            dt = ''
        full_build['finished'] = dt

        try:
            _build_str = _build_template.format(**full_build)
        except Exception as e:
            log.warning(unicode(e))
            _build_str = unicode(e) + "\n"

        task_id = full_build['task_id']
        if task_id is None:
            _task_str = "Build imported into koji\n"
        else:
            try:
                _task_str = "Closed tasks:\n-------------\n"
                _task_str += cls._fill_task_template(sess, task_id)
            except Exception as e:
                log.warning(unicode(e))
                _task_str = unicode(e) + "\n"

        return _build_str + _task_str

    def long_form(self, msg, **config):
        instance = msg['msg'].get('instance', 'primary')

        if instance == 'primary':
            url = "https://koji.fedoraproject.org/kojihub"
        elif instance == 'ppc':
            url = "https://ppc.koji.fedoraproject.org/kojihub"
        elif instance == 's390':
            url = "https://s390.koji.fedoraproject.org/kojihub"
        elif instance == 'arm':
            url = "https://arm.koji.fedoraproject.org/kojihub"

        if 'buildsys.build.state.change' in msg['topic'] and koji:
            session = koji.ClientSession(url)
            build = msg['msg']
            long_form = self._fill_build_template(session, build)
            return long_form
        if 'buildsys.task.state.change' in msg['topic'] and koji:
            session = koji.ClientSession(url)
            taskid = msg['msg']['id']
            try:
                long_form = self._fill_task_template(session, taskid)
            except Exception as e:
                log.warning(unicode(e))
                long_form = unicode(e)
            return long_form

    def subtitle(self, msg, **config):
        inst = msg['msg'].get('instance', 'primary')
        if inst == 'primary':
            inst = ''
        else:
            inst = ' (%s)' % inst

        if 'buildsys.tag' in msg['topic']:
            tmpl = self._(
                "{owner}'s {name}-{version}-{release} tagged "
                "into {tag} by {user}{inst}"
            )
            return tmpl.format(inst=inst, **msg['msg'])
        elif 'buildsys.untag' in msg['topic']:
            tmpl = self._(
                "{owner}'s {name}-{version}-{release} untagged "
                "from {tag} by {user}{inst}"
            )
            return tmpl.format(inst=inst, **msg['msg'])
        elif 'buildsys.repo.init' in msg['topic']:
            tmpl = self._('Repo initialized:  {tag}{inst}')
            return tmpl.format(inst=inst, tag=msg['msg'].get('tag', 'unknown'))
        elif 'buildsys.repo.done' in msg['topic']:
            tmpl = self._('Repo done:  {tag}{inst}')
            return tmpl.format(inst=inst, tag=msg['msg'].get('tag', 'unknown'))
        elif 'buildsys.package.list.change' in msg['topic']:
            tmpl = self._(
                "Package list change for {package}:  '{tag}'{inst}")
            return tmpl.format(inst=inst, **msg['msg'])
        elif 'buildsys.rpm.sign' in msg['topic']:
            tmpl = self._('Koji build '
                          '{name}-{version}-{release}.{arch}.rpm '
                          'signed with sigkey \'{sigkey}\'')
            if 'info' in msg['msg']:
                kwargs = copy.copy(msg['msg']['info'])
            else:
                kwargs = copy.copy(msg['msg']['rpm'])
                kwargs['sigkey'] = msg['msg']['sigkey']
            return tmpl.format(**kwargs)
        elif 'buildsys.build.state.change' in msg['topic']:
            templates = [
                self._("{owner}'s {name}-{version}-{release} "
                       "started building{inst}"),
                self._("{owner}'s {name}-{version}-{release} "
                       "completed{inst}"),
                self._("{owner}'s {name}-{version}-{release} "
                       "was deleted{inst}"),
                self._("{owner}'s {name}-{version}-{release} "
                       "failed to build{inst}"),
                self._("{owner}'s {name}-{version}-{release} "
                       "was cancelled{inst}"),
            ]
            tmpl = templates[msg['msg']['new']]

            # If there was no owner of the build, chop off the prefix.
            if not msg['msg']['owner']:
                tmpl = tmpl[len("{owner}'s "):]

            return tmpl.format(inst=inst, **msg['msg'])
        elif 'buildsys.task.state.change' in msg['topic']:
            templates = {
                'OPEN': self._(
                    "{owner}'s scratch build of {srpm}{target} started{inst}"),
                'FAILED': self._(
                    "{owner}'s scratch build of {srpm}{target} failed{inst}"),
                'CLOSED': self._(
                    "{owner}'s scratch build of {srpm}{target} completed{inst}"),
                'CANCELED': self._(
                    "{owner}'s scratch build of {srpm}{target} "
                    "was cancelled{inst}"),
            }
            target = ''
            if msg['msg'].get('info', {}).get('request'):
                targets = set()
                for item in msg['msg']['info']['request']:
                    if not isinstance(item, (dict, list)) and \
                            not item.endswith('.rpm'):
                        targets.add(item)
                if targets:
                    target = ' for %s'  % (
                        fedmsg.meta.base.BaseConglomerator.list_to_series(
                            targets))
            default = self._(
                "{owner}'s scratch build of {srpm}{target} changed{inst}")
            tmpl = templates.get(msg['msg']['new'], default)

            # If there was no owner of the build, chop off the prefix.
            if not msg['msg']['owner']:
                tmpl = tmpl[len("{owner}'s "):]

            return tmpl.format(inst=inst, target=target, **msg['msg'])

    def secondary_icon(self, msg, **config):
        owner = msg['msg'].get('owner')

        if owner:
            return avatar_url(owner)

        return self.__icon__

    def usernames(self, msg, **config):
        if 'buildsys.tag' in msg['topic']:
            return set([
                msg['msg']['owner'],
                msg['msg']['user'],
            ])
        elif 'buildsys.untag' in msg['topic']:
            return set([
                msg['msg']['owner'],
                msg['msg']['user'],
            ])
        elif 'buildsys.repo.init' in msg['topic']:
            return set()
        elif 'buildsys.repo.done' in msg['topic']:
            return set()
        elif 'buildsys.package.list.change' in msg['topic']:
            return set()
        elif 'buildsys.rpm.sign' in msg['topic']:
            return set()
        elif 'buildsys.build.state.change' in msg['topic']:
            if msg['msg']['owner']:
                return set([
                    msg['msg']['owner'],
                ])

            # Sometimes there is no owner
            return set()
        elif 'buildsys.task.state.change' in msg['topic']:
            if msg['msg']['owner']:
                return set([
                    msg['msg']['owner'],
                ])

            # Sometimes there is no owner
            return set()

    def packages(self, msg, **config):
        if 'buildsys.tag' in msg['topic']:
            return set([msg['msg']['name']])
        elif 'buildsys.untag' in msg['topic']:
            return set([msg['msg']['name']])
        elif 'buildsys.repo.init' in msg['topic']:
            return set([])
        elif 'buildsys.repo.done' in msg['topic']:
            return set([])
        elif 'buildsys.package.list.change' in msg['topic']:
            return set([msg['msg']['package']])
        elif 'buildsys.rpm.sign' in msg['topic']:
            if 'info' in msg['msg']:
                return set([msg['msg']['info']['name']])
            else:
                return set([msg['msg']['rpm']['name']])
        elif 'buildsys.build.state.change' in msg['topic']:
            return set([msg['msg']['name']])
        elif 'buildsys.task.state.change' in msg['topic']:
            # We can't *really* associate scratch builds with a package,
            # honestly.
            return set([])

        return set()

    def link(self, msg, **config):

        instance = msg['msg'].get('instance', 'primary')
        if instance == 'primary':
            base = "http://koji.fedoraproject.org/koji"
        elif instance == 'ppc':
            base = "http://ppc.koji.fedoraproject.org/koji"
        elif instance == 's390':
            base = "http://s390.koji.fedoraproject.org/koji"
        elif instance == 'arm':
            base = "http://arm.koji.fedoraproject.org/koji"
        else:
            raise NotImplementedError("Unhandled instance")

        # One last little switch-a-roo for stg
        if '.stg.' in msg['topic']:
            base = "http://koji.stg.fedoraproject.org/koji"

        if 'buildsys.tag' in msg['topic'] and 'tag_id' in msg['msg']:
            return base + "/taginfo?tagID=%i" % (
                msg['msg']['tag_id'])
        elif 'buildsys.untag' in msg['topic'] and 'tag_id' in msg['msg']:
            return base + "/taginfo?tagID=%i" % (
                msg['msg']['tag_id'])
        elif 'buildsys.repo.init' in msg['topic'] and 'tag_id' in msg['msg']:
            return base + "/taginfo?tagID=%i" % (
                msg['msg']['tag_id'])
        elif 'buildsys.repo.done' in msg['topic'] and 'tag_id' in msg['msg']:
            return base + "/taginfo?tagID=%i" % (
                msg['msg']['tag_id'])
        elif 'buildsys.build.state.change' in msg['topic']:
            return base + "/buildinfo?buildID=%i" \
                % (msg['msg']['build_id'])
        elif 'buildsys.task.state.change' in msg['topic']:
            return base + "/taskinfo?taskID=%i" \
                % (msg['msg']['id'])
        elif 'buildsys.package.list.change' in msg['topic']:
            return None
        elif 'buildsys.rpm.sign' in msg['topic']:
            if 'info' in msg['msg']:
                idx = msg['msg']['info']['build_id']
            else:
                idx = msg['msg']['rpm']['build_id']
            return base + "/buildinfo?buildID=%i" % idx
        else:
            return base

    def objects(self, msg, **config):
        instance = msg['msg'].get('instance', 'primary')

        if 'buildsys.tag' in msg['topic']:
            return set([
                '/'.join([
                    instance,
                    'builds',
                    msg['msg']['name'],
                    msg['msg']['version'],
                    msg['msg']['release'],
                ]),
                '/'.join([
                    instance,
                    'tags',
                    msg['msg']['tag'],
                ]),
            ])
        elif 'buildsys.untag' in msg['topic']:
            return set([
                '/'.join([
                    instance,
                    'builds',
                    msg['msg']['name'],
                    msg['msg']['version'],
                    msg['msg']['release'],
                ]),
                '/'.join([
                    instance,
                    'tags',
                    msg['msg'].get('tag', 'unknown'),
                ]),
            ])
        elif 'buildsys.build.state.change' in msg['topic']:
            return set(['/'.join([
                instance,
                'builds',
                msg['msg']['name'],
                msg['msg']['version'],
                msg['msg']['release'],
            ])])
        elif 'buildsys.task.state.change' in msg['topic']:
            return set(['/'.join([
                instance,
                'scratch_builds',
                msg['msg']['srpm'],
            ])])
        elif 'buildsys.repo.init' in msg['topic']:
            return set(['/'.join([
                instance,
                'repos',
                msg['msg'].get('tag', 'unknown'),
            ])])
        elif 'buildsys.repo.done' in msg['topic']:
            return set(['/'.join([
                instance,
                'repos',
                msg['msg'].get('tag', 'unknown'),
            ])])
        elif 'buildsys.package.list.change' in msg['topic']:
            return set(['/'.join([
                instance,
                'tags',
                msg['msg'].get('tag', 'unknown'),
            ])])
        elif 'buildsys.rpm.sign' in msg['topic']:
            if 'info' in msg['msg']:
                name = msg['msg']['info']['name']
            else:
                name = msg['msg']['rpm']['name']
            return set(['signatures/' + name])

        return set()
