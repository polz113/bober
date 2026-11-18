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

Administrator codes use the same construction with a wider flag field
(``ADMIN_LAYOUT``): 17 characters, ``XXXXX-XXXXX-XXXXX-XX``, with 3 flag
characters (15 bits) for the admin privileges, the allowed code effects
and the competitor privileges the holder may hand out. They have no
context and sign ``"bober-v2a||<code_id>|<flags>"``; the different prefix
keeps admin and competitor signatures apart.
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


class Layout(object):
    """Field widths, signature prefix and flag bits of one kind of code.

    ``flags`` maps ``(component name, value)`` to a bit.
    """

    def __init__(self, prefix, flags, flag_chars, id_chars=ID_CHARS,
                 mac_chars=MAC_CHARS):
        self.prefix = prefix
        self.flags = dict(flags)
        self.flag_chars = flag_chars
        self.id_chars = id_chars
        self.mac_chars = mac_chars
        self.code_chars = id_chars + flag_chars + mac_chars + 1
        self.max_code_id = 2 ** (5 * id_chars) - 1
        if max(self.flags.values()) >= 2 ** (5 * flag_chars):
            raise ValueError("flags do not fit into the flag field")

    @property
    def components(self):
        """Names of the components encoded in the flag field, in order."""
        names = []
        for name, _value in self.flags:
            if name not in names:
                names.append(name)
        return names

    def flags_from_parts(self, parts):
        """Bit mask for {component: [values]}; unknown values are ignored."""
        flags = 0
        for name, values in parts.items():
            for value in values:
                flags |= self.flags.get((name, value), 0)
        return flags

    def parts_from_flags(self, flags):
        parts = {name: set() for name in self.components}
        for (name, value), bit in self.flags.items():
            if flags & bit:
                parts[name].add(value)
        return parts


COMPETITOR_LAYOUT = Layout(
    "bober-v2",
    {("competitor_privileges", p): bit for p, bit in FLAGS.items()},
    flag_chars=FLAG_CHARS)

ADMIN_PRIVILEGE_NAMES = (
    "create_admin_codes", "create_competitor_codes", "view_all_attempts",
    "view_all_admin_codes", "view_all_competitor_codes",
    "use_question_sets", "modify_competition", "use_questions",
)
ADMIN_EFFECT_NAMES = ("let_manage", "let_manage_recursive")


def _admin_flags():
    names = ([("admin_privileges", p) for p in ADMIN_PRIVILEGE_NAMES]
             + [("allowed_effects", e) for e in ADMIN_EFFECT_NAMES]
             + [("competitor_privileges", p) for p in FLAGS])
    return {name: 1 << i for i, name in enumerate(names)}


ADMIN_LAYOUT = Layout("bober-v2a", _admin_flags(), flag_chars=3)


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


def mac(key, context, code_id, flags, layout=COMPETITOR_LAYOUT):
    msg = "{}|{}|{}|{}".format(layout.prefix, context, code_id,
                               flags).encode()
    digest = hmac.new(key, msg, hashlib.sha256).digest()
    return int.from_bytes(digest, "big") >> (256 - 5 * layout.mac_chars)


def flags_from_privileges(privileges):
    return sum(FLAGS[p] for p in set(privileges))


def privileges_from_flags(flags):
    return {p for p, bit in FLAGS.items() if flags & bit}


def group(raw):
    return "-".join(raw[i:i + GROUP_SIZE] for i in range(0, len(raw), GROUP_SIZE))


def encode(key, context, code_id, flags, layout=COMPETITOR_LAYOUT):
    """Canonical code for a code id and a flag bit mask."""
    if not 0 <= code_id <= layout.max_code_id:
        raise ValueError("code id out of range for v2 codes")
    body = (b32(code_id, layout.id_chars) + b32(flags, layout.flag_chars)
            + b32(mac(key, context, code_id, flags, layout),
                  layout.mac_chars))
    return group(body + luhn32(body))


def normalize(typed, layout=COMPETITOR_LAYOUT):
    """Return the canonical characters of a typed code (no dashes).

    Raises InvalidCodeFormat if the input cannot be a code of this layout.
    """
    s = typed.upper().replace("-", "").replace(" ", "")
    if not all(c in DECODE for c in s):
        raise InvalidCodeFormat()
    s = "".join(ALPHABET[DECODE[c]] for c in s)
    if len(s) != layout.code_chars:
        raise InvalidCodeFormat()
    return s


def canonical(typed, layout=COMPETITOR_LAYOUT):
    """Canonical display form of a typed code; does not verify it."""
    return group(normalize(typed, layout))


def decode(key, context, typed, layout=COMPETITOR_LAYOUT):
    """Verify a typed code.

    Returns ``(canonical_code, code_id, flags)`` or raises
    InvalidCodeFormat, CodeChecksumError or CodeSignatureError.
    """
    s = normalize(typed, layout)
    body, check = s[:-1], s[-1]
    if luhn32(body) != check:
        raise CodeChecksumError()

    def n(a, b):
        return sum(DECODE[c] << (5 * i)
                   for i, c in enumerate(reversed(body[a:b])))

    id_end = layout.id_chars
    flags_end = id_end + layout.flag_chars
    code_id = n(0, id_end)
    flags = n(id_end, flags_end)
    m = n(flags_end, flags_end + layout.mac_chars)
    expected = mac(key, context, code_id, flags, layout)
    if not hmac.compare_digest(b32(m, layout.mac_chars),
                               b32(expected, layout.mac_chars)):
        raise CodeSignatureError()
    flags &= sum(layout.flags.values())
    return encode(key, context, code_id, flags, layout), code_id, flags


def make_code(key, context, code_id, privileges):
    """Competitor code (the 15 character layout) for a set of privileges."""
    return encode(key, context, code_id, flags_from_privileges(privileges))


def parse_code(key, context, typed):
    """Verify a typed competitor code.

    Returns ``(canonical_code, code_id, privileges)`` or raises
    InvalidCodeFormat, CodeChecksumError or CodeSignatureError.
    """
    canonical_code, code_id, flags = decode(key, context, typed)
    return canonical_code, code_id, privileges_from_flags(flags)
