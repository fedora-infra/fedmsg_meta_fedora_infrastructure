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

    def link(self, msg, **config):
        urltmpl = 'https://openqa.fedoraproject.org/tests/{0}'
        if '.stg' in msg['topic']:
            urltmpl = 'https://openqa.stg.fedoraproject.org/tests/{0}'
        return urltmpl.format(msg['msg'].get('id'))

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

        return set(objs)
