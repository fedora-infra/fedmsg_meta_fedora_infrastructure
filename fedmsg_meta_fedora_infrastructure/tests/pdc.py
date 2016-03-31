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
# Authors:  Ralph Bean <rbean@redhat.com>
#
""" Tests for PDC messages. """

import unittest

from fedmsg_meta_fedora_infrastructure.tests.base import Base

from fedmsg_meta_fedora_infrastructure.tests.common import add_doc


class TestPDCComposeImport(Base):
    """ The `Product Definition Center <https://pdc.fedoraproject.org>`_
    publishes messages on this topic whenever a new compose entry is created.
    This message comes early, when *we first begin to import the compose*.
    There are other messages that come after, when the images and rpms for the
    compose finish being imported.
    """
    expected_title = "pdc.compose"
    expected_subti = ("An entry for the Fedora-Rawhide-20160331.n.0 nightly "
                      "compose was created in the Product Definition Center")
    expected_link = ("https://pdc.fedoraproject.org/rest_api/v1/"
                     "composes/Fedora-Rawhide-20160331.n.0/")
    expected_objects = set(['Fedora-Rawhide-20160331.n.0/create/compose'])
    msg = {
        "timestamp": 1459420734.0,
        "msg_id": "2016-e9ec264b-ce44-4260-8641-e385e71da171",
        "topic": "org.fedoraproject.prod.pdc.compose",
        "source_version": "0.6.5",
        "msg": {
            "action": "create",
            "compose_respin": 0,
            "compose_date": "2016-03-31",
            "compose_id": "Fedora-Rawhide-20160331.n.0",
            "compose_type": "nightly"
        }
    }


class TestPDCImagesImport(Base):
    """ The `Product Definition Center <https://pdc.fedoraproject.org>`_
    publishes messages on this topic whenever a set of images are uploaded for
    a new compose entry. This message doesn't necessarily signify that the
    compose is fully imported.  The `pdc-updater
    <https://github.com/fedora-infra/pdc-updater>`_ project typically import
    the images first and the rpms second, but it could be that an admin
    manually imports a compose in which case the order is not guaranteed.
    """
    expected_title = "pdc.images"
    expected_subti = ("PDC imported metadata for 3 images for "
                      "the Fedora-Rawhide-20160331.n.0 nightly compose")
    expected_link = ("https://pdc.fedoraproject.org/rest_api/v1/"
                     "composes/Fedora-Rawhide-20160331.n.0/")
    expected_objects = set(['Fedora-Rawhide-20160331.n.0/import/images'])
    msg = {
        "timestamp": 1459420734.0,
        "topic": "org.fedoraproject.prod.pdc.images",
        "source_version": "0.6.5",
        "msg": {
            "action": "import",
            "attribute": "images",
            "count": 3,
            "compose_respin": 0,
            "compose_date": "2016-03-31",
            "compose_id": "Fedora-Rawhide-20160331.n.0",
            "compose_type": "nightly"
        }
    }


class TestPDCRPMsImport(Base):
    """ The `Product Definition Center <https://pdc.fedoraproject.org>`_
    publishes messages on this topic whenever a set of rpms are uploaded for
    a new compose entry. This message doesn't necessarily signify that the
    compose is fully imported.  The `pdc-updater
    <https://github.com/fedora-infra/pdc-updater>`_ project typically import
    the images first and the rpms second, but it could be that an admin
    manually imports a compose in which case the order is not guaranteed.
    """
    expected_title = "pdc.rpms"
    expected_subti = ("PDC imported metadata for 207 rpms for "
                      "the Fedora-Rawhide-20160331.n.0 nightly compose")
    expected_link = ("https://pdc.fedoraproject.org/rest_api/v1/"
                     "composes/Fedora-Rawhide-20160331.n.0/")
    expected_objects = set(['Fedora-Rawhide-20160331.n.0/import/rpms'])
    msg = {
        "timestamp": 1459420734.0,
        "topic": "org.fedoraproject.prod.pdc.rpms",
        "source_version": "0.6.5",
        "msg": {
            "action": "import",
            "attribute": "rpms",
            "count": 207,
            "compose_respin": 0,
            "compose_date": "2016-03-31",
            "compose_id": "Fedora-Rawhide-20160331.n.0",
            "compose_type": "nightly"
        }
    }


add_doc(locals())

if __name__ == '__main__':
    unittest.main()
