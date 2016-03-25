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
    # there is no distro-neutral openQA icon, they use the SUSE geeko
    #__icon__ = "https://apps.fedoraproject.org/img/icons/taskotron.png"

    def subtitle(self, msg, **config):
        job = msg['msg'].get('id', '')
        build = msg['msg'].get('build', '')
        remain = msg['msg'].get('remaining', '')
        result = msg['msg'].get('result')
        msgtmpl = ''
        if ".stg" in msg['topic']:
            msgtmpl = "staging "

        if msg['topic'].endswith('job.duplicate'):
            auto = msg['msg'].get('auto', '')
            if auto == "0":
                auto = " manually"
            if auto == "1":
                auto = " automatically"
            msgtmpl += "job {0}{1} duplicated as {2} for {3}"
            return msgtmpl.format(job, auto, result, build)

        if msg['topic'].endswith('job.restart'):
            msgtmpl += "job {0} restarted as {1} for {2}"
            return msgtmpl.format(job, result, build)

        if msg['topic'].endswith('job.done'):
            msgtmpl += "job {0} completed for {1}, {2} remaining jobs"
            return msgtmpl.format(job, build, remain)

    def link(self, msg, **config):
        urltmpl = 'https://openqa.fedoraproject.org/tests/{0}'
        if '.stg' in msg['topic']:
            urltmpl = 'https://openqa.stg.fedoraproject.org/tests/{0}'
        return urltmpl.format(msg['msg'].get('id'))

    def objects(self, msg, **config):
        return set([msg['msg'].get('build')])
