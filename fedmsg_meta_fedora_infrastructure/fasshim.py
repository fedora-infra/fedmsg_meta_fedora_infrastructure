import threading
import urllib
import socket
from hashlib import sha256, md5

_fas_cache = {}
_fas_cache_lock = threading.Lock()

import logging
log = logging.getLogger("moksha.hub")


def avatar_url(username, size=64, default='retro'):
    openid = "http://%s.id.fedoraproject.org/" % username
    return avatar_url_from_openid(openid, size, default)


def avatar_url_from_openid(openid, size=64, default='retro', dns=False):
    """
    Our own implementation since fas doesn't support this nicely yet.
    """

    if dns:
        # This makes an extra DNS SRV query, which can slow down our webapps.
        # It is necessary for libravatar federation, though.
        import libravatar
        return libravatar.libravatar_url(
            openid=openid,
            size=size,
            default=default,
        )
    else:
        query = urllib.urlencode({'s': size, 'd': default})
        hash = sha256(openid).hexdigest()
        return "https://seccdn.libravatar.org/avatar/%s?%s" % (hash, query)


def avatar_url_from_email(email, size=64, default='retro', dns=False):
    """
    Our own implementation since fas doesn't support this nicely yet.
    """

    if dns:
        # This makes an extra DNS SRV query, which can slow down our webapps.
        # It is necessary for libravatar federation, though.
        import libravatar
        return libravatar.libravatar_url(
            email=email,
            size=size,
            default=default,
        )
    else:
        query = urllib.urlencode({'s': size, 'd': default})
        hash = md5(email).hexdigest()
        return "https://seccdn.libravatar.org/avatar/%s?%s" % (hash, query)


gravatar_url = avatar_url  # backwards compat
gravatar_url_from_openid = avatar_url_from_openid
gravatar_url_from_email = avatar_url_from_email


def make_fas_cache(**config):
    global _fas_cache
    if _fas_cache:
        return _fas_cache

    log.warn("No previous fas cache found.  Looking to rebuild.")

    try:
        import fedora.client
        import fedora.client.fas2
    except ImportError:
        log.warn("No python-fedora installed.  Not caching fas.")
        return {}

    if not 'fas_credentials' in config:
        log.warn("No fas_credentials found.  Not caching fas.")
        return {}

    creds = config['fas_credentials']

    default_url = 'https://admin.fedoraproject.org/accounts/'
    fasclient = fedora.client.fas2.AccountSystem(
        base_url=creds.get('base_url', default_url),
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
    except fedora.client.ServerError as e:
        log.warning("Failed to download fas cache %r" % e)
        return {}
    finally:
        socket.setdefaulttimeout(timeout)

    log.info("Caching necessary user data")
    for user in request['people']:
        nick = user['ircnick']
        if nick:
            _fas_cache[nick] = user['username']

        email = user['email']
        if email:
            _fas_cache[email] = user['username']

    del request
    del fasclient
    del fedora.client.fas2

    return _fas_cache


def nick2fas(nickname, **config):
    with _fas_cache_lock:
        fas_cache = make_fas_cache(**config)
        return fas_cache.get(nickname, nickname)


def email2fas(email, **config):
    with _fas_cache_lock:
        fas_cache = make_fas_cache(**config)
        return fas_cache.get(email, email)
