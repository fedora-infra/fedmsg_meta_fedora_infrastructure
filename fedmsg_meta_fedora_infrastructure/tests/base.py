from fedmsg.tests.test_meta import Base as _Base

import fedmsg_meta_fedora_infrastructure.fasshim


class Base(_Base):
    def setUp(self):
        # We don't want to actually query FAS during our test runs,
        # so mock out _fas_cache to contain a dummy cache.
        fedmsg_meta_fedora_infrastructure.fasshim._fas_cache = {
            'threebean': 'ralph',
            'rbean@redhat.com': 'ralph',
            'puiterwijk@gmail.com': 'puiterwijk',
            'nicolas.mailhot@laposte.net': 'nim',
        }
        super(Base, self).setUp()

    def tearDown(self):
        # At the end of each test, set things back to the way they were.
        fedmsg_meta_fedora_infrastructure.fasshim._fas_cache = {}
        super(Base, self).tearDown()
