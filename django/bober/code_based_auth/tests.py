from django.test import SimpleTestCase, TestCase

from code_based_auth import code_v2
from code_based_auth.models import (
    CODE_VERSION_V2, CodeFormat, CodeGenerator, CODE_ERROR_MESSAGES,
    long_to_str,
)

KEY = b"0123456789abcdef0123456789abcdef"
GROUP = "12-bober-2026-mlajsi"
OTHER_GROUP = "13-bober-2026-starejsi"

COMPETITOR_PRIVILEGES = ['attempt', 'attempt_before_start',
                         'results_before_end', 'resume_attempt']


def replace_char(code, index, new_char):
    raw = code.replace("-", "")
    raw = raw[:index] + new_char + raw[index + 1:]
    return code_v2.group(raw)


def other_char(c):
    return code_v2.ALPHABET[(code_v2.DECODE[c] + 1) % 32]


class CodeV2Test(SimpleTestCase):
    """The v2 code itself (no database)."""

    def test_reference_vectors(self):
        # produced by the reference implementation from the design document
        self.assertEqual(
            code_v2.make_code(KEY, GROUP, 3, ['attempt']), "00000-312BJ-SZ5CG")
        self.assertEqual(
            code_v2.make_code(KEY, GROUP, 123456,
                              ['attempt', 'resume_attempt']),
            "003RJ-095XR-3CVSG")
        self.assertEqual(
            code_v2.make_code(KEY, "7", 2 ** 30 - 1, COMPETITOR_PRIVILEGES),
            "ZZZZZ-ZF8YW-N39J7")

    def test_round_trip(self):
        for code_id in (1, 2, 31, 32, 123456, code_v2.MAX_CODE_ID):
            for privileges in ([], ['attempt'], COMPETITOR_PRIVILEGES,
                               ['attempt', 'resume_attempt']):
                code = code_v2.make_code(KEY, GROUP, code_id, privileges)
                self.assertRegex(code,
                                 r'^[0-9A-Z]{5}-[0-9A-Z]{5}-[0-9A-Z]{5}$')
                self.assertEqual(
                    code_v2.parse_code(KEY, GROUP, code),
                    (code, code_id, set(privileges)))

    def test_code_id_out_of_range(self):
        with self.assertRaises(ValueError):
            code_v2.make_code(KEY, GROUP, code_v2.MAX_CODE_ID + 1, [])

    def test_lenient_input_gives_canonical_form(self):
        code = "00000-312BJ-SZ5CG"
        variants = [
            code.lower(),
            code.replace("-", ""),
            code.replace("-", " "),
            " " + code.lower().replace("-", "") + " ",
            code.replace("0", "O"),
            code.replace("0", "o").replace("1", "l"),
            code.replace("1", "I"),
            code.replace("1", "i"),
        ]
        for typed in variants:
            self.assertEqual(code_v2.parse_code(KEY, GROUP, typed)[0], code,
                             typed)
            self.assertEqual(code_v2.canonical(typed), code, typed)

    def test_wrong_format(self):
        code = code_v2.make_code(KEY, GROUP, 42, ['attempt'])
        for typed in ("", code[:-1], code + "0", "U" + code[1:],
                      code[:5] + "*" + code[6:], "12*" + code):
            with self.assertRaises(code_v2.InvalidCodeFormat, msg=typed):
                code_v2.parse_code(KEY, GROUP, typed)

    def test_single_typo_is_detected_by_check_character(self):
        code = code_v2.make_code(KEY, GROUP, 123456, ['attempt'])
        raw = code.replace("-", "")
        for i in range(len(raw)):
            for c in code_v2.ALPHABET:
                if c == raw[i]:
                    continue
                with self.assertRaises(code_v2.CodeChecksumError):
                    code_v2.parse_code(KEY, GROUP, replace_char(code, i, c))

    def test_adjacent_transposition_is_detected(self):
        code = code_v2.make_code(KEY, GROUP, 123456, ['attempt'])
        raw = code.replace("-", "")
        for i in range(len(raw) - 1):
            if raw[i] == raw[i + 1]:
                continue
            swapped = raw[:i] + raw[i + 1] + raw[i] + raw[i + 2:]
            with self.assertRaises(code_v2.CodeChecksumError):
                code_v2.parse_code(KEY, GROUP, swapped)

    def test_code_from_other_group_is_rejected(self):
        code = code_v2.make_code(KEY, GROUP, 42, ['attempt'])
        with self.assertRaises(code_v2.CodeSignatureError):
            code_v2.parse_code(KEY, OTHER_GROUP, code)

    def test_code_with_other_key_is_rejected(self):
        code = code_v2.make_code(KEY, GROUP, 42, ['attempt'])
        with self.assertRaises(code_v2.CodeSignatureError):
            code_v2.parse_code(b"another key", GROUP, code)

    def _with_fixed_check_char(self, code, index, new_char):
        body = code.replace("-", "")[:-1]
        body = body[:index] + new_char + body[index + 1:]
        return code_v2.group(body + code_v2.luhn32(body))

    def test_changed_privileges_with_fixed_check_char_are_rejected(self):
        code = code_v2.make_code(KEY, GROUP, 42, ['attempt'])
        for flags in range(32):
            if flags == code_v2.FLAGS['attempt']:
                continue
            forged = self._with_fixed_check_char(
                code, code_v2.ID_CHARS, code_v2.ALPHABET[flags])
            with self.assertRaises(code_v2.CodeSignatureError):
                code_v2.parse_code(KEY, GROUP, forged)

    def test_changed_code_id_with_fixed_check_char_is_rejected(self):
        code = code_v2.make_code(KEY, GROUP, 42, ['attempt'])
        raw = code.replace("-", "")
        i = code_v2.ID_CHARS - 1
        forged = self._with_fixed_check_char(code, i, other_char(raw[i]))
        with self.assertRaises(code_v2.CodeSignatureError):
            code_v2.parse_code(KEY, GROUP, forged)

    def test_derive_key(self):
        self.assertEqual(code_v2.derive_key("abc"), code_v2.derive_key(b"abc"))
        self.assertEqual(len(code_v2.derive_key("abc")), 32)
        self.assertNotEqual(code_v2.derive_key("abc"),
                            code_v2.derive_key("abd"))


class CodeFormatV2Test(TestCase):
    """v2 through the CodeFormat / CodeGenerator entry points."""

    def setUp(self):
        self.format = CodeFormat.create_v2()
        self.generator = CodeGenerator.objects.create(
            unique_code_component='code_id', format=self.format,
            salt='0123456789abcdef0123456789abcdef')

    def create_code(self, privileges=('attempt',), group=GROUP):
        return self.generator.create_code({
            'competitor_privileges': list(privileges),
            'competition_questionset': [group],
        })

    def short_code(self, code):
        return code.value.split(self.format.separator, 1)[1]

    def test_migration_created_v2_competitor_format(self):
        f = CodeFormat.objects.get(name="Competitor code v2")
        self.assertEqual(f.code_version, CODE_VERSION_V2)
        self.assertEqual(
            list(f.components.order_by('ordering').values_list(
                'name', flat=True)),
            ['competition_questionset', 'code_id', 'competitor_privileges'])

    def test_generated_value(self):
        code = self.create_code(['attempt', 'resume_attempt'])
        context, short = code.value.split('*')
        self.assertEqual(context, GROUP)
        key = code_v2.derive_key(self.generator.salt)
        self.assertEqual(
            code_v2.parse_code(key, GROUP, short),
            (short, code.id, {'attempt', 'resume_attempt'}))
        self.assertIn(code, self.generator.codes.all())

    def test_code_matches(self):
        code = self.create_code(['attempt', 'resume_attempt'])
        matches = self.generator.code_matches
        self.assertTrue(matches(code.value,
                                {'competitor_privileges': ['attempt']}))
        self.assertTrue(matches(
            code.value,
            {'competitor_privileges': ['attempt', 'resume_attempt']}))
        self.assertFalse(matches(
            code.value, {'competitor_privileges': ['results_before_end']}))
        self.assertFalse(matches(
            code.value, {'competitor_privileges': ['attempt_before_start']}))
        self.assertTrue(matches(code.value,
                                {'competition_questionset': [GROUP]}))
        self.assertFalse(matches(code.value,
                                 {'competition_questionset': [OTHER_GROUP]}))
        self.assertFalse(matches(code.value, {'admin_privileges': ['x']}))
        self.assertFalse(matches(code.value, {}))
        self.assertFalse(matches(code.value, {'competitor_privileges': []}))
        # the format-level entry point used with Code.salt
        self.assertTrue(self.format.code_matches(
            code.value, code.salt, {'competitor_privileges': ['attempt']}))

    def test_unknown_privileges_are_not_granted(self):
        code = self.create_code(['attempt', 'results_before_end',
                                 'new_attempt'])
        self.assertTrue(self.generator.code_matches(
            code.value, {'competitor_privileges': ['results_before_end']}))
        self.assertFalse(self.generator.code_matches(
            code.value, {'competitor_privileges': ['new_attempt']}))

    def test_typed_variants_match_and_canonicalize(self):
        code = self.create_code()
        short = self.short_code(code)
        for typed in (short.lower(), short.replace("-", ""),
                      short.lower().replace("-", " "),
                      short.replace("0", "O")):
            full = GROUP + '*' + typed
            self.assertTrue(self.generator.code_matches(
                full, {'competitor_privileges': ['attempt']}), typed)
            self.assertEqual(self.generator.canonical_code(full), code.value)
        # not a v2 code: returned unchanged
        self.assertEqual(self.generator.canonical_code(GROUP + '*abc'),
                         GROUP + '*abc')
        self.assertIsNone(self.generator.canonical_code(None))

    def test_code_from_other_group_is_rejected(self):
        code = self.create_code(group=GROUP)
        full = OTHER_GROUP + '*' + self.short_code(code)
        self.assertFalse(self.generator.code_matches(
            full, {'competitor_privileges': ['attempt']}))
        self.assertEqual(
            self.generator.code_error_message(full),
            CODE_ERROR_MESSAGES[code_v2.CodeSignatureError])

    def test_error_messages(self):
        code = self.create_code()
        short = self.short_code(code)
        self.assertIsNone(self.generator.code_error_message(code.value))
        self.assertEqual(
            self.generator.code_error_message(GROUP + '*' + short[:-2]),
            CODE_ERROR_MESSAGES[code_v2.InvalidCodeFormat])
        typo = replace_char(short, 3, other_char(short.replace('-', '')[3]))
        self.assertEqual(
            self.generator.code_error_message(GROUP + '*' + typo),
            CODE_ERROR_MESSAGES[code_v2.CodeChecksumError])
        self.assertEqual(
            self.generator.code_error_message(short),
            CODE_ERROR_MESSAGES[code_v2.InvalidCodeFormat])

    def test_other_salt_is_rejected(self):
        code = self.create_code()
        other = CodeGenerator.objects.create(
            unique_code_component='code_id', format=self.format,
            salt='another salt, another competition')
        self.assertFalse(other.code_matches(
            code.value, {'competitor_privileges': ['attempt']}))


class LegacyCodeFormatTest(TestCase):
    """The original hash-component format keeps working unchanged."""

    def setUp(self):
        # as created by CompetitorCodeFormatCreate
        self.format = CodeFormat.from_components([
            {'name': 'competition_questionset', 'hash_len': 64,
             'hash_format': 'r', 'hash_algorithm': 'noop', 'max_parts': 1},
            {'name': 'code_id', 'hash_len': 8, 'hash_format': 'h',
             'hash_algorithm': 'noop', 'max_parts': 1},
            {'name': 'competitor_privileges', 'hash_len': 3,
             'hash_format': 'h', 'hash_algorithm': 'sha512',
             'max_parts': 4},
        ])
        self.generator = CodeGenerator.objects.create(
            unique_code_component='code_id', format=self.format,
            salt='abcdefghij')

    def create_code(self, privileges):
        return self.generator.create_code({
            'competitor_privileges': privileges,
            'competition_questionset': [GROUP],
        })

    def test_legacy_code(self):
        self.assertFalse(self.format.is_v2)
        code = self.create_code(['attempt', 'resume_attempt'])
        parts = code.value.split('*')
        self.assertEqual(len(parts), 3)
        self.assertEqual(parts[0], GROUP)
        self.assertEqual(int(parts[1], 16), code.id)
        self.assertEqual(len(parts[2].split('+')), 2)
        matches = self.generator.code_matches
        self.assertTrue(matches(code.value,
                                {'competitor_privileges': ['attempt']}))
        self.assertTrue(matches(code.value,
                                {'competitor_privileges': ['resume_attempt']}))
        self.assertFalse(matches(
            code.value, {'competitor_privileges': ['results_before_end']}))
        self.assertTrue(matches(code.value,
                                {'competition_questionset': [GROUP]}))
        self.assertFalse(matches(code.value,
                                 {'competition_questionset': [OTHER_GROUP]}))
        # hex format is case-insensitive
        upper = parts[0] + '*' + parts[1].upper() + '*' + parts[2].upper()
        self.assertEqual(self.generator.canonical_code(upper), code.value)
        self.assertIsNone(self.generator.code_error_message(code.value))

    def test_known_legacy_value(self):
        # computed with code_based_auth from master before v2 was added
        value = '12-bober-2026-mlajsi*04d2*903+597'
        self.assertEqual(self.format.code_from_parts('abcdefghij', {
            'competition_questionset': [GROUP],
            'code_id': [long_to_str(1234)],
            'competitor_privileges': ['attempt', 'resume_attempt'],
        }), value)
        for privilege, ok in (('attempt', True), ('resume_attempt', True),
                              ('attempt_before_start', False)):
            self.assertEqual(self.format.code_matches(
                value, 'abcdefghij', {'competitor_privileges': [privilege]}),
                ok)

    def test_regenerated_value_is_unchanged(self):
        # values already stored in the database and handed out to teachers
        # must still be produced and accepted the same way
        code = self.create_code(['attempt'])
        stored = code.value
        code.parts = code.parts
        self.assertEqual(code.value, stored)
        self.assertTrue(self.format.code_matches(
            stored, 'abcdefghij', {'competitor_privileges': ['attempt']}))
