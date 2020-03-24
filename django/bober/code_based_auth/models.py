import random
import codecs
import hashlib
from math import ceil
from sys import version_info
from collections import defaultdict

from django.db import models
from django.utils.translation import ugettext_lazy as _
# from django.utils.six import python_2_unicode_compatible


CODE_COMPONENT_FORMATS = (
    ('h', _('hex')),
    ('i', _('decimal')),
    ('l', _('letters and digits')),
    ('L', _('case-insensitive letters and digits')),
    ('s', _('unambiguous letters and digits')),
    ('S', _('case-insensitive unambiguous letters and digits')),
    ('w', _('words')),
    ('W', _('case-insensitive words')),
    ('r', _('raw no hash')),
)


HASH_ALGORITHMS = tuple(
    [(i, i) for i in list(hashlib.algorithms_available)] + [('noop', _('No hash'))]
)

DEFAULT_COMPONENT_FORMAT = 'h'
DEFAULT_HASH_BITS = 32
DEFAULT_HASH_ALGORITHM = 'sha512'
DEFAULT_SEPARATOR = "*"
DEFAULT_PART_SEPARATOR = "+"

# TODO load words from a file or database
DEFAULT_WORDS = ['Beaver', 'Tree', 'Brook', 'Stream']
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UNAMBIGUOUS_LETTERS_AND_DIGITS = 'abcdefghjkmnpqrstuvwxyz23456789'
UPPERCASE_LETTERS = LOWERCASE_LETTERS.upper()
DIGITS = "0123456789"
LOWERCASE_LETTERS_AND_DIGITS = LOWERCASE_LETTERS + DIGITS
LETTERS_AND_DIGITS = LOWERCASE_LETTERS + UPPERCASE_LETTERS + DIGITS
REDUCED_LETTERS = 'ghijklmnoprstuvz'
ALNUM32 = '0123456789abcdef'
ALNUM32_SEPARATORS = 'qwx'


def __compat_ord(c):
    if version_info >= (3, 0, 0):
        return c
    else:
        return ord(c)


def value_hash(salt, value, algorithm=DEFAULT_HASH_ALGORITHM):
    value = value.encode('iso8859-1')
    if algorithm == 'noop':
        return value
    h = hashlib.new(algorithm)
    h.update(salt)
    h.update(value)
    return h.digest()


def str_last_bits(s, bits):
    s_out = ""
    if bits % 8 != 0 and len(s) > bits//8:
        i = __compat_ord(s[-bits//8-1])
        i = i & (2**(bits % 8) - 1)
        s_out = chr(i).encode('iso8859-1')
    return s_out + s[-bits//8]


def split_by_bits(s, bits):
    b = ceil(1.0 * bits // 8)
    return [s[i:i+b] for i in range(0, len(s), b)]


def b_to_long(s):
    """maybe replace this with int.from_bytes in python3"""
    my_long = 0
    for c in s:
        my_long *= 256
        my_long += __compat_ord(c)
    return my_long


def long_to_str(my_long):
    """maybe replace most of this with int.to_bytes in python3"""
    s = ""
    while my_long > 0:
        c = "" + chr(my_long % 256)
        my_long = my_long // 256
        s = c + s
    try:
        return s
    except Exception:
        # TODO: handle exception
        pass
    return s


def hexstr_to_b(s):
    if version_info >= (3, 0, 0) or type(s) == str:
        s = s.encode('iso8859-1')
    return codecs.decode(s, 'hex')


def b_to_hexstr(s):
    return codecs.encode(s, 'hex').decode('iso8859-1')


def decstr_to_b(s):
    return str(b_to_long(s))


def b_to_decstr(s):
    return long_to_str(int(s))


def words_codecs(words=DEFAULT_WORDS, separator=" ", canonical_fn=None):
    val_words_dict = dict(((i, w) for i, w in enumerate(words)))
    n_words = len(words)
    if canonical_fn is None:
        def canonical_fn(x):
            return x

    def __b_to_words(s):
        my_long = b_to_long(s)
        res = ""
        if my_long <= 0:
            return words[0]
        while my_long > 0:
            w = words[my_long % n_words]
            my_long = my_long // n_words
            if res == "":
                res = w
            else:
                res = w + separator + res
        return res

    def __words_to_b(s):
        my_long = 0
        while(s):
            if separator:
                word_end = s.find(separator)
                if word_end == -1:
                    word_end = len(s)
            else:
                word_end = 1
                while s[:word_end] not in val_words_dict:
                    word_end += 1
            word = s[:word_end]
            my_long = my_long * n_words
            my_long += val_words_dict.get(word, 0)
        return long_to_str(my_long)
    return (__b_to_words, __words_to_b, canonical_fn)


FORMAT_FUNCTIONS = {
    'h': (b_to_hexstr, hexstr_to_b, lambda x: x.lower()),
    'i': (b_to_decstr, decstr_to_b, lambda x: x),
    'w': words_codecs(DEFAULT_WORDS, " "),
    'W': words_codecs([w.lower() for w in DEFAULT_WORDS], " ", lambda x: x.lower()),

    's': words_codecs(UNAMBIGUOUS_LETTERS_AND_DIGITS, "", lambda x: x),
    'S': words_codecs(UNAMBIGUOUS_LETTERS_AND_DIGITS, "", lambda x: x.lower()),
    'l': words_codecs(LETTERS_AND_DIGITS, ''),
    'L': words_codecs(LOWERCASE_LETTERS_AND_DIGITS, '', lambda x: x.lower()),
    'r': (lambda x: x.decode('iso8859-1'), lambda x: x.encode('iso8859-1'), lambda x: x),
}


class CodeField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 256  # up to 2048 bits total
        super(CodeField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(CodeField, self).deconstruct()
        del kwargs["max_length"]
        return name, path, args, kwargs


class CodeComponent(models.Model):
    def __str__(self):
        if self.max_parts > 1:
            part_desc = self.part_separator + str(self.max_parts)
        else:
            part_desc = ''
        return u"{}:({},{}({}){})".format(
            self.name, self.hash_format, self.hash_algorithm,
            self.hash_len, part_desc)

    code_format = models.ForeignKey('CodeFormat', related_name='components',
                                    on_delete=models.CASCADE)
    ordering = models.PositiveIntegerField()
    name = models.CharField(max_length=64)
    hash_format = models.CharField(
        max_length=2,
        choices=CODE_COMPONENT_FORMATS)
    # hash_bits = models.PositiveIntegerField()
    hash_len = models.PositiveIntegerField()
    hash_algorithm = models.CharField(
        max_length=16, choices=HASH_ALGORITHMS,
        null=True, blank=True)
    max_parts = models.IntegerField(default=1)
    part_separator = models.CharField(
        max_length=1, default=DEFAULT_PART_SEPARATOR)


class CodeFormat(models.Model):
    def __str__(self):
        return self.separator.join([
            str(i) for i in self.components.order_by('ordering')])
    separator = models.CharField(max_length=1, default=DEFAULT_SEPARATOR)

    @classmethod
    def from_components(cls, components, separator=DEFAULT_SEPARATOR):
        cf = cls(separator=separator)
        cf.save()
        for i, p in enumerate(components):
            cc = CodeComponent(code_format=cf, ordering=i, **p)
            cc.save()
        return cf

    def code_matches(self, code, salt, parts):
        if len(parts) < 1:
            return False
        format_components = self.components.order_by('ordering')
        # hash_params is a dict of
        # (  format conversion function,
        #    hash algorithm,
        #    max. nr. of parts,
        #    set of component parts)
        # indexed by code component name
        hash_params = dict()
        challenge = bytes()  # the fixed part of the code
        try:
            split_parts = code.split(self.separator)
            salt_b = salt.encode('utf-8')
            # collect the hashes, calculate challenge
            hashes = defaultdict(set)
            for i, component in enumerate(format_components):
                format_functions = FORMAT_FUNCTIONS[component.hash_format]
                h = format_functions[2](split_parts[i])
                if component.max_parts == 1 and component.hash_algorithm == 'noop':
                    challenge += h.encode('iso8859-1')
                if not component.part_separator:
                    h_len = component.hash_len
                    split_hash = [h[i:i+h_len] for i in range(0, len(h), h_len)]
                else:
                    split_hash = h.split(component.part_separator)
                if len(split_hash) > component.max_parts:
                    return False
                for h in split_hash:
                    hashes[component.name].add(h)
                hash_params[component.name] = (
                    format_functions[0],
                    component.hash_algorithm, component.hash_len, hashes)
            # calculate the hashes for components
            # print ("hashes:", hashes)
            # print ("parts:", parts)
            for k, values in parts.items():
                to_b_fn, algorithm, hash_len, hashes = hash_params[k]
                if len(values) < 1:
                    # print "  len too small for ", k
                    return False
                for value in values:
                    # print(value, to_b_fn, algorithm)
                    # print("static pre:", salt_b, challenge)
                    h = to_b_fn(value_hash(
                            salt_b + challenge,
                            value, algorithm))[-hash_len:]
                    # if component.hash_format in CASE_INSENSITIVE_FORMATS:
                    #    h = h.lower()
                    # print("  k", k, "h:", h, "hashes:", hashes[k])
                    if h not in hashes[k]:
                        # print ("  ", h, "not in", hashes[k])
                        return False
        except Exception as e:
            # print(e)
            return False
        return True

    def unhashed_formatted_part(self, part, value):
        component = self.components.get(
            name=part,
            hash_algorithm='noop', max_parts=1)
        fn = FORMAT_FUNCTIONS[component.hash_format][0]
        return fn(value)[-component.hash_len:]

    def code_from_parts(self, salt, parts):
        # print ("parts:", parts)
        salt = salt.encode('utf-8')
        format_components = self.components.order_by('ordering')
        challenge = bytes()
        unhashed_format_components = format_components.filter(
            hash_algorithm='noop', max_parts=1)
        for i in unhashed_format_components:
            for value in parts.get(i.name, []):
                s = FORMAT_FUNCTIONS[i.hash_format][0](value.encode('iso8859-1'))
                challenge += s[-i.hash_len:].encode('iso8859-1')
        hashed_components = list()
        for i, component in enumerate(format_components):
            hash_list = list()
            hash_format = component.hash_format
            values = parts.get(component.name, [])
            for value in values:
                h = value_hash(salt + challenge,
                               value, component.hash_algorithm)
                s = FORMAT_FUNCTIONS[component.hash_format][0](h)
                hash_list.append(s[-component.hash_len:])
            hashed_components.append(component.part_separator.join(hash_list))
        return self.separator.join(hashed_components)

    def canonical_code(self, code):
        # print("canonizing:", code)
        try:
            format_components = self.components.order_by('ordering')
            split_parts = code.split(self.separator)
            canonical_parts = []
            for i, component in enumerate(format_components):
                canonical_parts.append(
                    FORMAT_FUNCTIONS[component.hash_format][2](
                        split_parts[i]))
            # print("  parts:", canonical_parts)
            return self.separator.join(canonical_parts)
        except Exception as e:
            # print(e)
            pass
        return code


# @python_2_unicode_compatible
class CodePart(models.Model):
    def __str__(self):
        return str(self.ordering) + self.value
    code = models.ForeignKey('Code', related_name='code_parts',
                             on_delete=models.CASCADE)
    ordering = models.IntegerField(default=0)
    name = models.CharField(max_length=64)
    value = models.CharField(max_length=256)


# @python_2_unicode_compatible
class Code(models.Model):
    def __str__(self):
        return self.value
    value = CodeField(db_index=True)
    salt = models.CharField(max_length=256)
    format = models.ForeignKey('CodeFormat', on_delete=models.CASCADE)

    @property
    def parts(self):
        parts = defaultdict(list)
        for i in self.code_parts.order_by('name', 'ordering'):
            parts[i.name].append(i.value)
        return dict(parts)

    @parts.setter
    def parts(self, parts_dict):
        self.code_parts.all().delete()
        for k, values in parts_dict.items():
            for i, value in enumerate(values):
                part = CodePart(code=self, ordering=i,
                                name=k, value=value)
                part.save()
        self.value = self.format.code_from_parts(self.salt, parts_dict)

    @parts.deleter
    def parts(self):
        self.code_parts.delete()

    @classmethod
    def create(cls, format, salt, parts):
        c = cls(format=format, salt=salt, value="foo")
        c.save()
        c.parts = parts
        return c


class CodeGenerator(models.Model):
    def __str__(self):
        return self.salt + " " + str(self.format)

    unique_code_component = models.CharField(null=True, blank=True,
                                             max_length=256)
    format = models.ForeignKey('CodeFormat', on_delete=models.CASCADE)
    salt = models.CharField(max_length=256)
    codes = models.ManyToManyField('Code', blank=True)

    def create_code(self, parts, random_unique=False):
        if not random_unique:
            created_code = Code.create(salt=self.salt, format=self.format,
                                       parts={})
            code_id = created_code.id
        if self.unique_code_component:
            if random_unique:
                parts[self.unique_code_component] = [long_to_str(random.getrandbits(64))]
            else:
                parts[self.unique_code_component] = [long_to_str(code_id)]
        if random_unique:
            created_code = Code.create(salt=self.salt, format=self.format,
                                       parts=parts)
        else:
            created_code.parts = parts
        created_code.save()
        self.codes.add(created_code)
        return created_code

    def variable_components(self):
        return self.format.components.order_by('ordering').exclude(
            name=self.unique_code_component)

    def code_matches(self, code, parts):
        return self.format.code_matches(salt=self.salt, code=code, parts=parts)

    def canonical_code(self, code):
        return self.format.canonical_code(code)
