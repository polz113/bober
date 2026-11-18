"""Access code format v2.

A v2 code is 15 characters of Crockford base32
(``0123456789ABCDEFGHJKMNPQRSTVWXYZ``, no I, L, O, U), shown as
``XXXXX-XXXXX-XXXXX``, e.g. ``0030E-D95AF-BWJVD``.

=====  =========================================================  ====
chars  field                                                      bits
=====  =========================================================  ====
6      code id (``Code.pk``)                                      30
1      privileges as a bit mask (see ``FLAGS``)                   5
7      signature: top 35 bits of                                  35
       ``HMAC-SHA256(key, "bober-v2|<context>|<code_id>|<flags>")``
1      Luhn mod 32 check character over the first 14 characters
=====  =========================================================  ====

The context (for competitor codes: the competition questionset) is not
part of the code; it is chosen by the competitor and bound into the
signature, so a code is only valid for the group it was issued for.

Input is case-insensitive, dashes and spaces are ignored and the
look-alike characters ``O`` -> ``0`` and ``I``/``L`` -> ``1`` are accepted.
``parse_code`` always returns the canonical form.
"""
import hashlib
import hmac

ALPHABET = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"
DECODE = {c: i for i, c in enumerate(ALPHABET)}
DECODE.update({"O": 0, "I": 1, "L": 1})

FLAGS = {
    "attempt": 1,
    "attempt_before_start": 2,
    "results_before_end": 4,
    "resume_attempt": 8,
}
ID_CHARS, FLAG_CHARS, MAC_CHARS = 6, 1, 7
CODE_CHARS = ID_CHARS + FLAG_CHARS + MAC_CHARS + 1
MAX_CODE_ID = 2 ** (5 * ID_CHARS) - 1
GROUP_SIZE = 5


class CodeError(ValueError):
    """Base class for v2 code validation errors."""


class InvalidCodeFormat(CodeError):
    def __init__(self, msg="invalid code format"):
        super().__init__(msg)


class CodeChecksumError(CodeError):
    def __init__(self, msg="typo - check the code"):
        super().__init__(msg)


class CodeSignatureError(CodeError):
    def __init__(self, msg="code not valid for this group"):
        super().__init__(msg)


def derive_key(salt):
    """Derive the HMAC key from a code generator salt.

    The salt is the per-generator secret that every code entry point
    already passes around (``CodeGenerator.salt``, ``Code.salt``), so the
    key is derived from it instead of being stored separately.
    """
    if isinstance(salt, str):
        salt = salt.encode("utf-8")
    return hashlib.sha256(b"bober-v2-key|" + salt).digest()


def b32(n, width):
    return "".join(ALPHABET[(n >> (5 * i)) & 31] for i in reversed(range(width)))


def luhn32(s):
    total, factor = 0, 2
    for c in reversed(s):
        a = factor * DECODE[c]
        total += a // 32 + a % 32
        factor = 3 - factor
    return ALPHABET[(32 - total % 32) % 32]


def mac(key, context, code_id, flags):
    msg = "bober-v2|{}|{}|{}".format(context, code_id, flags).encode()
    digest = hmac.new(key, msg, hashlib.sha256).digest()
    return int.from_bytes(digest, "big") >> (256 - 5 * MAC_CHARS)


def flags_from_privileges(privileges):
    return sum(FLAGS[p] for p in set(privileges))


def privileges_from_flags(flags):
    return {p for p, bit in FLAGS.items() if flags & bit}


def group(raw):
    return "-".join(raw[i:i + GROUP_SIZE] for i in range(0, len(raw), GROUP_SIZE))


def make_code(key, context, code_id, privileges):
    if not 0 <= code_id <= MAX_CODE_ID:
        raise ValueError("code id out of range for v2 codes")
    flags = flags_from_privileges(privileges)
    body = (b32(code_id, ID_CHARS) + b32(flags, FLAG_CHARS)
            + b32(mac(key, context, code_id, flags), MAC_CHARS))
    return group(body + luhn32(body))


def normalize(typed):
    """Return the 15 canonical characters of a typed code (no dashes).

    Raises InvalidCodeFormat if the input cannot be a v2 code.
    """
    s = typed.upper().replace("-", "").replace(" ", "")
    if not all(c in DECODE for c in s):
        raise InvalidCodeFormat()
    s = "".join(ALPHABET[DECODE[c]] for c in s)
    if len(s) != CODE_CHARS:
        raise InvalidCodeFormat()
    return s


def canonical(typed):
    """Canonical display form of a typed code; does not verify it."""
    return group(normalize(typed))


def parse_code(key, context, typed):
    """Verify a typed code.

    Returns ``(canonical_code, code_id, privileges)`` or raises
    InvalidCodeFormat, CodeChecksumError or CodeSignatureError.
    """
    s = normalize(typed)
    body, check = s[:-1], s[-1]
    if luhn32(body) != check:
        raise CodeChecksumError()

    def n(a, b):
        return sum(DECODE[c] << (5 * i) for i, c in enumerate(reversed(body[a:b])))

    code_id = n(0, ID_CHARS)
    flags = n(ID_CHARS, ID_CHARS + FLAG_CHARS)
    m = n(ID_CHARS + FLAG_CHARS, ID_CHARS + FLAG_CHARS + MAC_CHARS)
    if not hmac.compare_digest(b32(m, MAC_CHARS),
                               b32(mac(key, context, code_id, flags), MAC_CHARS)):
        raise CodeSignatureError()
    privs = privileges_from_flags(flags)
    return make_code(key, context, code_id, privs), code_id, privs
