import collections
import threading
import socket
import string
from hashlib import sha256, md5

_fas_cache = {}
_fas_cache_lock = threading.Lock()

import logging
log = logging.getLogger("moksha.hub")

try:
    from six.moves.urllib import parse
except ImportError:
    # Really really old 'six' doesn't have this move.. so we fall back to
    # python-2 only usage.  If we're on an old 'six', then we can assume that
    # we must also be on an old Python.
    import urllib as parse


def _ordered_query_params(params):
    # if OrderedDict is available, preserver order of params
    #  to make this easily testable on PY3
    if hasattr(collections, 'OrderedDict'):
        retval = collections.OrderedDict(params)
    else:
        retval = dict(params)
    return retval


# https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/issues/320
hardcoded_avatars = {
    'bodhi': 'https://apps.fedoraproject.org/img/icons/bodhi-{size}.png',
    'koschei': 'https://apps.fedoraproject.org/img/icons/koschei-{size}.png',
    # Taskotron may have a new logo at some point.  Check this out:
    # https://mashaleonova.wordpress.com/2015/08/18/a-logo-for-taskotron/
    # Ask tflink before actually putting this in place though.  we need
    # a nice small square version.  It'll look great!
    # In the meantime, we can use this temporary logo.
    'taskotron': 'https://apps.fedoraproject.org/img/icons/taskotron-{size}.png'
}


def avatar_url(username, size=64, default='retro'):
    if username in hardcoded_avatars:
        return hardcoded_avatars[username].format(size=size)
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
        params = _ordered_query_params([('s', size), ('d', default)])
        query = parse.urlencode(params)
        hash = sha256(openid.encode('utf-8')).hexdigest()
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
        params = _ordered_query_params([('s', size), ('d', default)])
        query = parse.urlencode(params)
        hash = md5(email.encode('utf-8')).hexdigest()
        return "https://seccdn.libravatar.org/avatar/%s?%s" % (hash, query)


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
    for key in string.ascii_lowercase:
        socket.setdefaulttimeout(600)
        try:
            log.info("Downloading FAS cache for %s*" % key)
            response = fasclient.send_request(
                '/user/list',
                req_params={'search': '%s*' % key},
                auth=True)
        except fedora.client.ServerError as e:
            log.warning("Failed to download fas cache for %s %r" % (key, e))
            continue
        finally:
            socket.setdefaulttimeout(timeout)

        log.info("Caching necessary user data for %s*" % key)
        for user in response['people']:
            nick = user['ircnick']
            if nick:
                _fas_cache[nick] = user['username']

            email = user['email']
            if email:
                _fas_cache[email] = user['username']

        del response

    del fasclient
    del fedora.client.fas2

    return _fas_cache


def nick2fas(nickname, **config):
    log.debug("Acquiring _fas_cache_lock for nicknames.")
    with _fas_cache_lock:
        log.debug("Got _fas_cache_lock for nicknames.")
        fas_cache = make_fas_cache(**config)
        result = fas_cache.get(nickname, nickname)
    log.debug("Released _fas_cache_lock for nicknames.")
    return result


def email2fas(email, **config):
    if email.endswith('@fedoraproject.org'):
        return email.rsplit('@', 1)[0]

    log.debug("Acquiring _fas_cache_lock for emails.")
    with _fas_cache_lock:
        log.debug("Got _fas_cache_lock for emails.")
        fas_cache = make_fas_cache(**config)
        result = fas_cache.get(email, email)
    log.debug("Released _fas_cache_lock for emails.")
    return result
