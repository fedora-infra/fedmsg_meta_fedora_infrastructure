# This file is part of fedmsg.
# Copyright (C) 2016 Red Hat, Inc.
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
# Authors:  Adam Williamson <awilliam@redhat.com>

from fedmsg_meta_fedora_infrastructure import BaseProcessor

class OpenQAProcessor(BaseProcessor):
    __name__ = "openqa"
    __description__ = "Distribution-level automated testing"
    __link__ = "https://openqa.fedoraproject.org"
    __docs__ = "https://os-autoinst.github.io/openQA/documentation/"
    __obj__ = "openQA test results"
    __icon__ = "https://apps.fedoraproject.org/img/icons/openqa.png"

    def _msg_type(self, msg):
        """We often have to handle different types of messages in
        entirely different ways; this is the identification logic, so
        we don't keep repeating it.
        """
        if '.job.' in msg['topic']:
            return 'job'
        if '.comment.' in msg['topic']:
            return 'comment'

    def subtitle(self, msg, **config):
        if self._msg_type(msg) == 'job':
            return self._subtitle_job(msg, **config)
        elif self._msg_type(msg) == 'comment':
            return self._subtitle_comment(msg, **config)

    def _subtitle_job(self, msg, **config):
        job = msg['msg'].get('id', '')
        # old messages had 'build' not 'BUILD'
        build = msg['msg'].get('BUILD', msg['msg'].get('build', ''))
        remain = msg['msg'].get('remaining', '')
        result = msg['msg'].get('result')
        # all the following do not exist in old messages so we always
        # check before using them
        test = msg['msg'].get('TEST')
        arch = msg['msg'].get('ARCH')
        machine = msg['msg'].get('MACHINE')
        flavor = msg['msg'].get('FLAVOR')
        iso = msg['msg'].get('ISO')
        hdd1 = msg['msg'].get('HDD_1')

        msgtmpl = ''
        if ".stg" in msg['topic']:
            msgtmpl = "staging "

        msgtmpl += "job {0} ".format(job)
        if test:
            # if we have 'test' we can assume 'machine'
            msgtmpl += "(test {0} on {1}".format(test, machine)
            if iso:
                msgtmpl += " for iso {0}) ".format(iso)
            elif hdd1:
                msgtmpl += " for disk {0}) ".format(hdd1)
            else:
                # just for general safety...
                msgtmpl += ") "

        if msg['topic'].endswith('job.duplicate'):
            auto = msg['msg'].get('auto', '')
            if auto == "0":
                auto = "manually "
            if auto == "1":
                auto = "automatically "
            msgtmpl += "{0}duplicated as {1} for {2}"
            return msgtmpl.format(auto, result, build)

        if msg['topic'].endswith('job.restart'):
            msgtmpl += "restarted as {0} for {1}"
            return msgtmpl.format(result, build)

        if msg['topic'].endswith('job.done'):
            msgtmpl += "completed for {0}, {1} remaining jobs"
            return msgtmpl.format(build, remain)

    def _subtitle_comment(self, msg, **config):
        # get the info
        extract = msg['msg'].get('text', '')
        if len(extract) > 30:
            extract = extract[:30] + "..."
        user = msg['msg'].get('user', 'someone')
        comment = msg['msg'].get('id')
        job = msg['msg'].get('job_id')
        group = msg['msg'].get('group_id')
        action = 'did something to'
        if msg['topic'].endswith('comment.create'):
            action = 'created'
        elif msg['topic'].endswith('comment.update'):
            action = 'updated'
        elif msg['topic'].endswith('comment.delete'):
            action = 'deleted'

        # construct the message
        subtitle = "{0} {1} comment #{2} on openQA".format(user, action, comment)
        if job:
            subtitle += " job {0}".format(job)
        elif group:
            subtitle += " group {0}".format(group)
        if extract:
            subtitle += ", text: {0}".format(extract)

        # return it
        return subtitle

    def link(self, msg, **config):
        if '.stg' in msg['topic']:
            baseurl = 'https://openqa.stg.fedoraproject.org'
        else:
            baseurl = 'https://openqa.fedoraproject.org'

        if self._msg_type(msg) == 'job':
            # job messages
            urltmpl = '{0}/tests/{1}'
            return urltmpl.format(baseurl, msg['msg'].get('id'))

        elif self._msg_type(msg) == 'comment':
            # comment messages
            job = msg['msg'].get('job_id')
            group = msg['msg'].get('group_id')
            if job:
                urltmpl = '{0}/tests/{1}#comments'
                return urltmpl.format(baseurl, job)
            elif group:
                # comments are just right on the page
                urltmpl = '{0}/group_overview/{1}'
                return urltmpl.format(baseurl, group)
            else:
                # we have no idea, just return openQA
                return baseurl

    def objects(self, msg, **config):
        objs = []
        if 'build' in msg['msg']:
            objs.append(msg['msg']['build'])
        elif 'BUILD' in msg['msg']:
            objs.append(msg['msg']['BUILD'])

        if 'ISO' in msg['msg']:
            objs.append(msg['msg']['ISO'])
        # HDD_1 is probably not an 'object' if there's an ISO, it's
        # more likely just a test component
        elif 'HDD_1' in msg['msg']:
            objs.append(msg['msg']['HDD_1'])

        if msg['msg'].get('job_id'):
            objs.append(msg['msg']['job_id'])
        if msg['msg'].get('group_id'):
            objs.append(msg['msg']['group_id'])

        return set(objs)

    def usernames(self, msg, **config):
        # comment messages have a 'user', job messages don't
        user = msg['msg'].get('user')
        if user:
            return set((user,))
        else:
            return set()
