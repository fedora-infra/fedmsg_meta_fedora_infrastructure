from fedmsg.tests.test_meta import Base


def add_doc(objects):
    """ Given a dict of names and classes, reattach the docstring as 'doc'.

    The core fedmsg lib uses that 'doc' attribute to build its own docs for
    http://fedmsg.com/

    This is needed as a workaround for this code:
    https://github.com/fedora-infra/fedmsg/blob/develop/fedmsg/doc_utilities.py
    """

    for k, v in objects.items():
        if 'Test' in k and issubclass(v, Base):
            v.doc = v.__doc__
