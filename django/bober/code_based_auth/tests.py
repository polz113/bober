from django.test import SimpleTestCase

from code_based_auth import random_code


class RandomCodeTest(SimpleTestCase):
    def test_generate_form(self):
        for _ in range(100):
            code = random_code.generate()
            self.assertEqual(len(code), 11)
            self.assertEqual(code[5], '-')
            self.assertTrue(all(c in random_code.ALPHABET
                                for c in code.replace('-', '')))
            self.assertEqual(random_code.canonical(code), code)

    def test_generate_is_random(self):
        codes = set(random_code.generate() for _ in range(1000))
        self.assertEqual(len(codes), 1000)

    def test_canonical_normalizes_typed_input(self):
        for typed in ('ab1cd-ef0gh', 'AB1CDEF0GH', 'ab1cd ef0gh',
                      ' aBlcd-ef-Ogh ', 'AbICD EFoGH'):
            self.assertEqual(random_code.canonical(typed), 'AB1CD-EF0GH',
                             typed)

    def test_canonical_rejects_other_input(self):
        for typed in ('', 'AB1CD', 'AB1CD-EF0GH-JKMNP-QRSTVW', 'AB1CD-EF0GU',
                      'AB1CD*EF0GH', None):
            self.assertIsNone(random_code.canonical(typed), typed)

    def test_lookup_values(self):
        self.assertEqual(random_code.lookup_values('ab1cd ef0gh'),
                         ['AB1CD-EF0GH', 'ab1cd ef0gh'])
        self.assertEqual(random_code.lookup_values('AB1CD-EF0GH'),
                         ['AB1CD-EF0GH'])
        # older codes are only found exactly as issued
        self.assertEqual(random_code.lookup_values(' 0000002a*f3c '),
                         ['0000002a*f3c'])
        self.assertEqual(random_code.lookup_values('  '), [])

    def test_lengths(self):
        for length, form in ((6, 'XXX-XXX'), (7, 'XXXX-XXX'), (8, 'XXXX-XXXX'),
                             (9, 'XXXXX-XXXX'), (10, 'XXXXX-XXXXX'),
                             (12, 'XXXX-XXXX-XXXX'),
                             (20, 'XXXXX-XXXXX-XXXXX-XXXXX')):
            code = random_code.generate(length)
            self.assertEqual(len(code.replace('-', '')), length)
            self.assertEqual(
                ''.join('X' if c != '-' else '-' for c in code), form)
            self.assertEqual(random_code.canonical(code), code)
            self.assertEqual(random_code.canonical(
                code.replace('-', '').lower()), code)
        for length in (5, 21):
            with self.assertRaises(ValueError):
                random_code.generate(length)
