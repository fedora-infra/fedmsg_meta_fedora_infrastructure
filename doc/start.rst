Getting started with fedmsg_meta_fedora_infrastructure
======================================================

This project provides a mapping allowing to convert a specific `fedmsg
<http://fedmsg.com>`_ message into a single string of information describing the
action of that lead to this message.


Quick introduction to fedmsg_meta
---------------------------------

Sometime an example is worth more than just words:

::

    import requests

    import fedmsg
    import fedmsg.meta
    config = fedmsg.config.load_config()
    fedmsg.meta.make_processors(**config)

    req = requests.get('https://apps.fedoraproject.org/datagrepper/raw/')
    data = req.json()

    for message in data['raw_messages']:
        print fedmsg.meta.msg2subtitle(message)
        print fedmsg.meta.msg2usernames(message)
        print fedmsg.meta.msg2packages(message)


This simple script will retrieve recent messages from datagrepper and for
each message returned will print a one-line description of the action as
well as the persons and packages involved.
