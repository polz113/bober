"""Limit the number of wrong access codes a client can enter.

Random competitor codes have 50 bits and short legacy hashes even less, so
guessing must be slow. Failures are counted per client IP address in the
Django cache, in a fixed window that starts with the first failure.

Settings:

- ``CODE_AUTH_MAX_FAILURES`` (default 100): failures allowed per window.
  A whole class usually shares one public IP address, so keep this well
  above the number of typos a class makes in a few minutes.
- ``CODE_AUTH_FAILURE_WINDOW`` (default 600): window length in seconds.
- ``CODE_AUTH_CLIENT_IP_HEADER`` (default None): behind a reverse proxy,
  REMOTE_ADDR is the address of the proxy, so all clients would share one
  counter. Set this to the request.META key in which the proxy passes the
  client address, e.g. ``'HTTP_X_REAL_IP'`` or ``'HTTP_X_FORWARDED_FOR'``
  (of a comma separated list, the last address is used: the one added by
  the proxy). Only set it if the proxy always sets the header, otherwise
  clients can choose their own address.

While a client is throttled, also correct codes are refused; otherwise
the answer would still tell an attacker which guess is right.

Use a cache shared between worker processes (memcached, redis, database);
with the default per-process local memory cache every worker counts
separately.
"""
from django.conf import settings
from django.core.cache import cache

DEFAULT_MAX_FAILURES = 100
DEFAULT_FAILURE_WINDOW = 600


def _max_failures():
    return getattr(settings, 'CODE_AUTH_MAX_FAILURES', DEFAULT_MAX_FAILURES)


def _window():
    return getattr(settings, 'CODE_AUTH_FAILURE_WINDOW',
                   DEFAULT_FAILURE_WINDOW)


def client_ip(request):
    header = getattr(settings, 'CODE_AUTH_CLIENT_IP_HEADER', None)
    if header:
        ip = request.META.get(header, '').split(',')[-1].strip()
        if ip:
            return ip
    return request.META.get('REMOTE_ADDR', '')


def _cache_key(request):
    return 'code_auth_failures:' + client_ip(request)


def is_throttled(request):
    return cache.get(_cache_key(request), 0) >= _max_failures()


def register_failure(request):
    key = _cache_key(request)
    cache.add(key, 0, _window())
    try:
        cache.incr(key)
    except ValueError:
        # expired between add() and incr()
        cache.set(key, 1, _window())

