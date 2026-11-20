"""Random access code values.

A code is random characters from the Crockford base32 alphabet (5 bits
each), by default 10 (50 bits), shown in dash separated groups of at most
5 characters (``XXXXX-XXXXX``; ``XXXX-XXXX`` for 8 characters). The value
carries no meaning: what a code allows is stored next to it in the
database, and a code is checked by looking it up.

Typed input is normalized before the lookup: case does not matter, dashes
and spaces are ignored and the easily confused letters ``O``, ``I`` and
``L`` are read as ``0``, ``1`` and ``1``.
"""
import secrets

ALPHABET = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"
CODE_CHARS = 10  # default length
MIN_CODE_CHARS = 6
MAX_CODE_CHARS = 20
GROUP_SIZE = 5

_DECODE = {c: c for c in ALPHABET}
_DECODE.update({"O": "0", "I": "1", "L": "1"})


def generate(length=CODE_CHARS):
    """Return a new random code of length characters, canonical form."""
    if not MIN_CODE_CHARS <= length <= MAX_CODE_CHARS:
        raise ValueError("code length must be between %d and %d"
                         % (MIN_CODE_CHARS, MAX_CODE_CHARS))
    return group("".join(secrets.choice(ALPHABET) for _ in range(length)))


def group(raw):
    """Split raw into dash separated groups of at most GROUP_SIZE
    characters, as even as possible (longer groups first)."""
    n_groups = -(-len(raw) // GROUP_SIZE)
    size, longer = divmod(len(raw), n_groups)
    groups, start = [], 0
    for i in range(n_groups):
        end = start + size + (1 if i < longer else 0)
        groups.append(raw[start:end])
        start = end
    return "-".join(groups)


def canonical(typed):
    """Return the canonical form (e.g. ``XXXXX-XXXXX``) of a typed code.

    Any length between MIN_CODE_CHARS and MAX_CODE_CHARS is accepted, so
    codes keep working when the code length of a group is changed. Returns
    None when the input can not be such a code (length or characters
    outside the alphabet).
    """
    if typed is None:
        return None
    s = typed.upper().replace("-", "").replace(" ", "")
    if not MIN_CODE_CHARS <= len(s) <= MAX_CODE_CHARS:
        return None
    try:
        s = "".join(_DECODE[c] for c in s)
    except KeyError:
        return None
    return group(s)


def lookup_values(typed):
    """Values to look up for a typed code.

    The canonical form for codes of the current form, plus the code exactly
    as typed (without surrounding whitespace), so codes issued before random
    codes were introduced keep working when typed exactly as issued.
    """
    if typed is None:
        return []
    values = []
    c = canonical(typed)
    if c is not None:
        values.append(c)
    exact = typed.strip()
    if exact and exact not in values:
        values.append(exact)
    return values
