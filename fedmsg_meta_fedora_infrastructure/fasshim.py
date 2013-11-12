import urllib
import socket
from hashlib import md5

_valid_gravatar_sizes = (32, 64, 140)

_fas_cache = {}

import logging
log = logging.getLogger("moksha.hub")


def gravatar_url(username, size=64, default=None):
    try:
        import fedora.client
        system = fedora.client.AccountSystem()
        return system.gravatar_url(
            username, size, default, lookup_email=False)
    except Exception:
        email = username + "@fedoraproject.org"
        return gravatar_url_from_email(email, size, default)


def gravatar_url_from_email(email, size=64, default=None):
    """
    Our own implementation since fas doesn't support this nicely yet.
    """

    if size not in _valid_gravatar_sizes:
        raise ValueError(b_(
            'Size %(size)i disallowed.  Must be in %(valid_sizes)r') % {
                'size': size, 'valid_sizes': _valid_gravatar_sizes})

    if not default:
        default = ("http://fedoraproject.org/static/images/"
                   "fedora_infinity_%ix%i.png" % (size, size))

    return _kernel(email, size, default, service='gravatar')


def _kernel(email, size, default, service='gravatar'):
    """ Copy-and-paste of some code from python-fedora. """

    if service == 'libravatar':
        import libravatar
        return libravatar.libravatar_url(
            email=email,
            size=size,
            default=default,
        )
    else:
        query_string = urllib.urlencode({
            's': size,
            'd': default,
        })

        hash = md5(email).hexdigest()

        return "http://www.gravatar.com/avatar/%s?%s" % (hash, query_string)


def make_fas_cache(**config):
    global _fas_cache
    if _fas_cache:
        return _fas_cache

    log.warn("No previous fas cache found.  Looking to rebuild.")

    try:
        import fedora.client.fas2
    except ImportError:
        log.warn("No python-fedora installed.  Not caching fas.")
        return {}

    if not 'fas_credentials' in config:
        log.warn("No fas_credentials found.  Not caching fas.")
        return {}

    creds = config['fas_credentials']

    fasclient = fedora.client.fas2.AccountSystem(
        username=creds['username'],
        password=creds['password'],
    )

    timeout = socket.getdefaulttimeout()
    socket.setdefaulttimeout(600)
    try:
        log.info("Downloading FAS cache")
        request = fasclient.send_request('/user/list',
                                         req_params={'search': '*'},
                                         auth=True)
    finally:
        socket.setdefaulttimeout(timeout)

    log.info("Caching necessary user data")
    for user in request['people']:
        nick = user['ircnick']
        if nick:
            _fas_cache[nick] = user['username']

    del request
    del fasclient
    del fedora.client.fas2

    return _fas_cache


def nick2fas(nickname, **config):
    fas_cache = make_fas_cache(**config)
    return fas_cache.get(nickname, nickname)
