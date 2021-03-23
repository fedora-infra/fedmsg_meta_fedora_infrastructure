import collections
import logging
import os
import socket
import string
import threading
from hashlib import sha256, md5

_fas_cache = {}
_fas_cache_lock = threading.Lock()

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
    'taskotron': (
        'https://apps.fedoraproject.org/img/icons/taskotron-{size}.png'
    )
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


def make_fasjson_cache(**config):
    global _fas_cache
    if _fas_cache:
        return _fas_cache

    log.warn("No previous fasjson cache found. Looking to rebuild.")

    creds = config['fasjson_credentials']

    krb5_principal = creds.get("krb5_principal")
    krb5_client_ktname = creds.get("krb5_client_ktname")
    gss_use_proxy = creds.get("gss_use_proxy")

    if krb5_client_ktname:
        os.environ["KRB5_CLIENT_KTNAME"] = krb5_client_ktname

    if gss_use_proxy:
        os.environ["GSS_USE_PROXY"] = "yes"

    # the base URL shouldn't contain the API version, the fasjson client takes
    # care of it
    default_url = 'https://fasjson.fedoraproject.org/'
    base_url = creds.get('base_url', default_url)

    try:
        import fasjson_client
    except ImportError:
        fasjson_client = None
        log.warn(
            "No fasjson-client installed.  Falling back to querying directly."
        )

    if fasjson_client:
        try:
            client = fasjson_client.Client(
                url=base_url, principal=krb5_principal
            )
        except fasjson_client.errors.ClientSetupError as e:
            log.error(
                "Error while setting up fasjson client: %s" % e
            )
            return {}
        APIError = fasjson_client.errors.APIError
    else:
        import requests
        import requests.exceptions
        from requests.compat import urlencode, urljoin
        from requests_gssapi import HTTPSPNEGOAuth

        # shim inside a shim
        class Client(object):
            def __init__(self, url, principal=None):
                self.url = url.rstrip("/") + "/v1/"
                self.principal = principal

                gssapi_auth = HTTPSPNEGOAuth(
                    opportunistic_auth=True, mutual_authentication="OPTIONAL"
                )
                self.session = requests.Session()
                self.session.auth = gssapi_auth

            def list_all_entities(self, ent_name):
                if not ent_name.endswith("/"):
                    # avoid redirection round trip
                    ent_name += "/"
                endpoint = urljoin(self.url, ent_name)

                # yay, pagination
                next_page_url = endpoint + "?" + urlencode({"page_number": 1})
                while next_page_url:
                    res = self.session.get(next_page_url)
                    for item in res["result"]:
                        yield item
                    next_page_url = res.get("page", {}).get("next_page")

        client = Client(url=base_url, principal=krb5_principal)

        APIError = requests.exceptions.RequestException

    try:
        _add_to_cache(list(client.list_all_entities("users")))
    except APIError as e:
        log.error("Something went wrong building cache with error: %s" % e)
        return {}

    return _fas_cache


def _add_to_cache(users):
    global _fas_cache

    for user in users:
        nicks = user.get('ircnicks', [])
        for nick in nicks:
            _fas_cache[nick] = user['username']

        emails = user.get('emails', [])
        for email in emails:
            _fas_cache[email] = user['username']


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

    if 'fas_credentials' not in config:
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
        fasjson = config.get('fasjson')
        if fasjson:
            fas_cache = make_fasjson_cache(**config)
        else:
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
        fasjson = config.get('fasjson')
        if fasjson:
            fas_cache = make_fasjson_cache(**config)
        else:
            fas_cache = make_fas_cache(**config)
        result = fas_cache.get(email, email)
    log.debug("Released _fas_cache_lock for emails.")
    return result
