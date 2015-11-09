from django.db import models
import hashlib
from collections import defaultdict

CODE_COMPONENT_FORMATS = (
    ('h', 'hex'),
    ('i', 'decimal'),
    ('l', 'letters and digits'),
    ('L', 'case-insensitive letters and digits'),
    ('w', 'words'),
    ('W', 'case-insensitive words'),
    ('r', 'raw no hash'),
)

CASE_INSENSITIVE_FORMATS = ['h', 'l', 'L', 'W']

HASH_ALGORITHMS = tuple(
    [(i, i) for i in list(hashlib.algorithms)] + [('noop', 'No hash')]
)

DEFAULT_COMPONENT_FORMAT = 'h'
DEFAULT_HASH_BITS = 32
DEFAULT_HASH_ALGORITHM = 'sha512'
DEFAULT_SEPARATOR = "*"
DEFAULT_PART_SEPARATOR = "+"

# TODO load words from a file or database
DEFAULT_WORDS = ['Beaver', 'Tree', 'Brook', 'Stream']
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = LOWERCASE_LETTERS.upper()
DIGITS = "0123456789"
LOWERCASE_LETTERS_AND_DIGITS = LOWERCASE_LETTERS + DIGITS
LETTERS_AND_DIGITS = LOWERCASE_LETTERS + UPPERCASE_LETTERS + DIGITS
REDUCED_LETTERS = 'ghijklmnoprstuvz'
ALNUM32 = '0123456789abcdef' + REDUCED_LETTERS
ALNUM32_SEPARATORS = 'qwx'

def str_hash(salt, s, algorithm = DEFAULT_HASH_ALGORITHM):
    if algorithm == 'noop':
        return s
    h = hashlib.new(algorithm)
    h.update(salt)
    h.update(s)
    return h.digest()

def str_last_bits(s, bits):
    s_out = ""
    if bits % 8 != 0 and len(s) > bits/8:
        i = ord(s[-bits/8-1])
        i = i & (2**(bits%8) -1)
        s_out = chr(i)
    return s_out + s[-bits/8]

def split_by_bits(s, bits):
    b = ceil(1.0 * bits / 8)
    return [s[i:i+b] for i in xrange(0, len(s), b)]
    
def str_to_long(s):
    l = 0
    for c in s:
        l = l * 256
        l += ord(c)
    return l

def long_to_str(l):
    s = ""
    while l > 0:
        c = chr(l % 256)
        l = l / 256
        s = c + s
    return s

def str_to_hex(s):
    return s.encode('hex')

def hex_to_str(s):
    return s.decode('hex')

def str_to_dec(s):
    return str(str_to_long(s))

def dec_to_str(s):
    return long_to_str(long(s))

def words_codecs(words=DEFAULT_WORDS, separator=" "):
    val_words_dict = dict(((i, w) for i, w in enumerate(words)))
    n_words = len(words)
    def __str_to_words(s):
        l = str_to_long(s)
        res = ""
        if l <= 0:
            return words[0]
        while l > 0:
            w = words[l % n_words]
            l = l / n_words
            if res == "":
                res = w
            else:
                res = w + separator + res
        return res
    def __words_to_str(s):
        l = 0
        while(s):
            if separator:
                word_end = find(s, separator)
                if word_end == -1:
                    word_end = len(s)
            else:
                word_end = 1
                while s[:word_end] not in val_words_dict:
                    word_end += 1    
            word = s[:word_end]
            l = l * n_words
            l += val_words_dict.get(word, 0)
        return long_to_str(l)
    return (__str_to_words, __words_to_str)
 
FORMAT_FUNCTIONS = {
    'h': (str_to_hex, hex_to_str),
    'i': (str_to_dec, dec_to_str),
    'w': words_codecs(DEFAULT_WORDS, " "),
    'W': words_codecs([w.lower() for w in DEFAULT_WORDS], " "),
    'l': words_codecs(LETTERS_AND_DIGITS, ''),
    'L': words_codecs(LOWERCASE_LETTERS_AND_DIGITS, ''),
    'r': (lambda x: x, lambda x: x),
} 

class CodeField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 256 # up to 2048 bits total
        super(CodeField, self).__init__(*args, **kwargs)
    def deconstruct(self):
        name, path, args, kwargs = super(CodeField, self).deconstruct()
        del kwargs["max_length"]
        return name, path, args, kwargs

class CodeComponent(models.Model):
    def __unicode__(self):
        if self.max_parts > 1:
            part_desc = self.part_separator + str(self.max_parts)
        else:
            part_desc = ''
        return u"{}:({},{}({}){})".format(
            self.name, self.hash_format, self.hash_algorithm,
            self.hash_len, part_desc)
    code_format = models.ForeignKey('CodeFormat', related_name='components')
    ordering = models.PositiveIntegerField()
    name = models.CharField(max_length = 64)
    hash_format = models.CharField(max_length=2, 
        choices = CODE_COMPONENT_FORMATS)
    # hash_bits = models.PositiveIntegerField()
    hash_len = models.PositiveIntegerField()
    hash_algorithm = models.CharField(max_length = 16,
        choices = HASH_ALGORITHMS, null=True, blank=True)
    max_parts = models.IntegerField(default=1)
    part_separator = models.CharField(max_length=1, default=DEFAULT_PART_SEPARATOR)

class CodeFormat(models.Model):
    def __unicode__(self):
        return self.separator.join([
            unicode(i) for i in self.components.order_by('ordering')])
    separator = models.CharField(max_length=1, default=DEFAULT_SEPARATOR)
    @classmethod
    def from_components(cls, components, separator=DEFAULT_SEPARATOR):
        cf = cls(separator = separator)
        cf.save()
        for i, p in enumerate(components):
            cc = CodeComponent(code_format = cf, ordering = i, **p)
            cc.save()
        return cf
    def code_matches(self, code, salt, parts):
        if len(parts) < 1:
            return False
        salt = salt.encode('utf-8')
        format_components = self.components.order_by('ordering')
        split_parts = code.split(self.separator)
        hash_params = dict()
        challenge = bytes()
        try:
            # collect the hashes, calculate challenge
            hashes = defaultdict(set)
            for i, component in enumerate(format_components):
                h = split_parts[i]
                if component.hash_format in CASE_INSENSITIVE_FORMATS:
                    h = h.lower()
                if component.max_parts == 1 and component.hash_algorithm == 'noop':
                    challenge += h 
                if not component.part_separator:
                    h_len = component.hash_len
                    split_hash = [h[i:i+h_len] for i in xrange(0, len(h), h_len)]
                else:
                    split_hash = h.split(component.part_separator)
                if len(split_hash) > component.max_parts:
                    return False
                for h in split_hash:
                    hashes[component.name].add(h)
                hash_params[component.name] = (FORMAT_FUNCTIONS[component.hash_format][0], 
                    component.hash_algorithm, component.hash_len, hashes)
            # calculate the hashes for components
            # print "hashes:", hashes, hash_params
            for k, values in parts.iteritems():
                format_fn, algorithm, hash_len, hashes = hash_params[k]
                if len(values) < 1:
                    return False
                for value in values:
                    # print value, format_fn, algorithm, format_fn(value)
                    h = format_fn(str_hash(salt + challenge,
                            value, algorithm))[-hash_len:]
                    #print "h:", h
                    if h not in hashes[k]:
                    #    print "  not in ", hashes[k]
                        return False
        except Exception, e:
            print e
            return False
        return True
                
    def code_from_parts(self, salt, parts):
        salt = salt.encode('utf-8')
        format_components = self.components.order_by('ordering')
        challenge = bytes()
        unhashed_format_components = format_components.filter(
            hash_algorithm='noop', max_parts=1)
        for i in unhashed_format_components:
            for value in parts.get(i.name, []):
                s = FORMAT_FUNCTIONS[i.hash_format][0](value)
                challenge += s[-i.hash_len:]
        hashed_components = list()
        for i, component in enumerate(format_components):
            hash_list = list()
            hash_format = component.hash_format
            values = parts.get(component.name, [])
            for value in values:
                h = str_hash(salt + challenge,
                    value, component.hash_algorithm)
                s = FORMAT_FUNCTIONS[component.hash_format][0](h)
                if hash_format in CASE_INSENSITIVE_FORMATS:
                    s = s.lower()
                hash_list.append(s[-component.hash_len:])
            hashed_components.append(component.part_separator.join(hash_list))
        return self.separator.join(hashed_components)

class CodePart(models.Model):
    def __unicode__(self):
        return str(self.ordering) + self.value
    code = models.ForeignKey('Code', related_name = 'code_parts')
    ordering = models.IntegerField(default=0)
    name = models.CharField(max_length = 64)
    value = models.CharField(max_length = 256)

class Code(models.Model):
    def __unicode__(self):
        return self.value
    value = CodeField()
    salt = models.CharField(max_length=256)
    format = models.ForeignKey('CodeFormat')
    @property
    def parts(self):
        parts = defaultdict(list)
        for i in self.code_parts.order_by('name', 'ordering'):
            parts[i.name].append(i.value)
        return dict(parts)
    @parts.setter
    def parts(self, parts_dict):
        self.code_parts.all().delete()
        for k, values in parts_dict.iteritems():
            for i, value in enumerate(values):
                part = CodePart(code = self, ordering = i,
                    name = k, value = value)
                part.save()
        self.value = self.format.code_from_parts(self.salt, parts_dict)
    @parts.deleter
    def parts(self):
        self.code_parts.delete()
    @classmethod
    def create(cls, format, salt, parts):
        c = cls(format=format, salt=salt, value = "foo")
        c.save()
        c.parts = parts
        return c

class CodeGenerator(models.Model):
    def __unicode__(self):
        return self.salt + " " + unicode(self.format)
    unique_code_component = models.CharField(null = True, blank = True, 
        max_length = 256)
    format = models.ForeignKey('CodeFormat')
    salt = models.CharField(max_length=256)
    codes = models.ManyToManyField('Code', null=True, blank=True)
    def create_code(self, parts):
        created_code = Code.create(salt=self.salt, format=self.format, 
            parts={})
        if self.unique_code_component:
            parts[self.unique_code_component] = [long_to_str(created_code.id).encode('string_escape')]
        created_code.parts = parts
        created_code.save()
        self.codes.add(created_code)
        return created_code
    def variable_components(self):
        return self.format.components.order_by('ordering').exclude(
            name = self.unique_code_component)
    def code_matches(self, code, parts):
        return self.format.code_matches(salt = self.salt, 
            code = code, parts = parts)
