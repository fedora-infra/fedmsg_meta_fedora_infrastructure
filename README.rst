fedmsg_meta_fedora_infrastructure
=================================

.. split here

fedmsg metadata providers for Fedora Infrastructure's deployment
----------------------------------------------------------------

`fedmsg <http://fedmsg.com>`_ is a set of tools for knitting together services
and webapps into a realtime messaging net.  This package contains metadata
provider plugins for the primary deployment of that system:  `Fedora
Infrastructure <http://fedoraproject.org/wiki/Infrastructure>`_.

If you were to deploy fedmsg at another site, you would like want to write your
own module like this one that could provide textual representations of *your*
messages.

Pop into ``#fedora-apps`` on freenode if you have questions or comments.

Build Status
------------

.. |master| image:: https://secure.travis-ci.org/ralphbean/fedmsg_meta_fedora_infrastructure.png?branch=master
   :alt: Build Status - master branch
   :target: http://travis-ci.org/#!/ralphbean/fedmsg_meta_fedora_infrastructure

.. |develop| image:: https://secure.travis-ci.org/ralphbean/fedmsg_meta_fedora_infrastructure.png?branch=develop
   :alt: Build Status - develop branch
   :target: http://travis-ci.org/#!/ralphbean/fedmsg_meta_fedora_infrastructure

+----------+-----------+
| Branch   | Status    |
+==========+===========+
| master   | |master|  |
+----------+-----------+
| develop  | |develop| |
+----------+-----------+

Running the Tests
-----------------

::

    # Create a virtualenv
    $ sudo yum install python-virtualenv
    $ virtualenv my-env
    $ source my-env/bin/activate

    # Install the dependencies
    $ python setup.py develop

    # Run the tests
    $ pip install nose
    $ $(which nosetests)

Building the Docs
-----------------

::

    # Install additional dependencies
    $ pip install -r doc/requirements.txt
    $ sphinx-build doc/ htmldocs/
