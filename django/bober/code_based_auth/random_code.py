"""Random access code values.

A code is 10 random characters from the Crockford base32 alphabet
(50 bits), shown as ``XXXXX-XXXXX``. The value carries no meaning: what a
code allows is stored next to it in the database, and a code is checked by
looking it up.

Typed input is normalized before the lookup: case does not matter, dashes
and spaces are ignored and the easily confused letters ``O``, ``I`` and
``L`` are read as ``0``, ``1`` and ``1``.
"""
import secrets

ALPHABET = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"
CODE_CHARS = 10
GROUP_SIZE = 5

_DECODE = {c: c for c in ALPHABET}
_DECODE.update({"O": "0", "I": "1", "L": "1"})


def generate():
    """Return a new random code in its canonical form."""
    return group("".join(secrets.choice(ALPHABET) for _ in range(CODE_CHARS)))


def group(raw):
    return "-".join(raw[i:i + GROUP_SIZE]
                    for i in range(0, len(raw), GROUP_SIZE))


def canonical(typed):
    """Return the canonical form ``XXXXX-XXXXX`` of a typed code.

    Returns None when the input can not be a code of this form (wrong
    length or characters outside the alphabet).
    """
    if typed is None:
        return None
    s = typed.upper().replace("-", "").replace(" ", "")
    if len(s) != CODE_CHARS:
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
