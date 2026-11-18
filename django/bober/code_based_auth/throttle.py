"""Limit the number of wrong access codes a client can enter.

The security of short signed codes (35 bit signature for v2 codes, even
less for short legacy hashes) relies on an attacker not being able to try
a large number of codes. Failures are counted per client IP address in the
Django cache, in a fixed window that starts with the first failure.

Settings:

- ``CODE_AUTH_MAX_FAILURES`` (default 100): failures allowed per window.
  A whole class usually shares one public IP address, so keep this well
  above the number of typos a class makes in a few minutes.
- ``CODE_AUTH_FAILURE_WINDOW`` (default 600): window length in seconds.

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


def _cache_key(request):
    return 'code_auth_failures:' + request.META.get('REMOTE_ADDR', '')


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


def reset(request):
    cache.delete(_cache_key(request))
