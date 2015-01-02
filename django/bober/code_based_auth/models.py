from django.db import models
import hashlib
from collections import defaultdict

CODE_COMPONENT_FORMATS = (
    ('h', 'hex'),
    ('i', 'decimal'),
    ('w', 'words'),
    ('r', 'raw no hash'),
    ('a', 'match any'),
)

HASH_ALGORITHMS = tuple(
    [(i, i) for i in list(hashlib.algorithms_available)]
)

DEFAULT_HASH_BITS = 32
DEFAULT_ALGORITHM = 'sha512'
DEFAULT_SEPARATOR = "-"

# TODO load words from a file or database
DEFAULT_WORDS = ['Beaver', 'Tree', 'Brook', 'Stream']

def long_hash(salt, data, bits, algorithm = DEFAULT_ALGORITHM):
    h = hashlib.new(algorithm)
    h.update(salt)
    h.update(data)
    digest = h.hexdigest()
    s = ""
    if bits % 4 != 0:
        i = int(digest[-bits/4-1], 16)
        i = i & [0, 1, 3, 7][bits%4]
        s = hex(i)[2:]
    s += digest[-bits/4:]
    return long(s, 16)
 
def hex_hash(salt, data, bits, algorithm = DEFAULT_ALGORITHM):
    return hex(long_hash(salt, data, bits, algorithm))[2:-1]

def decimal_hash(salt, data, bits, algorithm = DEFAULT_ALGORITHM):
    return str(long_hash(salt, data, bits, algorithm))[:-1]

def words_hash(salt, data, bits, algorithm = DEFAULT_ALGORITHM, 
    words=DEFAULT_WORDS):
    i = long_hash(salt, data, bits, algorithm)
    base = len(words)
    digest = ""
    while i > 0:
        digest += words[i % base]
        i = i / base
    return digest

# Warning! This hash function rounds the bits down to 8!
def raw_hash(salt, data, bits, algorithm):
    return data[:int(bits/8)]

def empty_hash(salt, data, bits, algorithm):
    return ''

def noop_hash(salt, data, bits, algorithm):
    return data

_HASH_FUNCTIONS = {
    'h': hex_hash,
    'i': decimal_hash,
    'w': words_hash,
    'r': raw_hash,
    'a': noop_hash,
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
        return u"{}:({},{}({}bit){})".format(
            self.name, self.hash_format, self.hash_algorithm,
            self.hash_bits, part_desc)
    code_format = models.ForeignKey('CodeFormat', related_name='components')
    ordering = models.PositiveIntegerField()
    name = models.CharField(max_length = 64)
    hash_format = models.CharField(max_length=2, 
        choices = CODE_COMPONENT_FORMATS)
    hash_bits = models.PositiveIntegerField()
    hash_algorithm = models.CharField(max_length = 16,
        choices=HASH_ALGORITHMS, null=True, blank=True)
    max_parts = models.IntegerField(default=1)
    part_separator = models.CharField(max_length=1, default='+')

class CodeFormat(models.Model):
    def __unicode__(self):
        return self.separator.join([
            unicode(i) for i in self.components.order_by('ordering')])
    separator = models.CharField(max_length=1, default=DEFAULT_SEPARATOR)
    @classmethod
    def from_parts(cls, parts, separator=DEFAULT_SEPARATOR):
        cf = cls(separator = separator)
        cf.save()
        for i, p in enumerate(parts):
            cc = CodeComponent(code_format = cf, ordering = i, **p)
            cc.save()
    def code_matches(self, code, salt, components):
        if len(components) < 1:
            return False
        format_components = self.components.order_by('ordering')
        split_components = code.split(self.separator)
        hash_params = dict()
        challenge = bytes()
        # collect the hashes, calculate challenge
        for i, component in enumerate(format_components):
            hashes = set()
            if component.hash_format == 'a' or not component.part_separator:
                h = split_components[i]
                if component.hash_format == 'a':
                    challenge += h
                hashes.add(h)
            else:
                s = split_components[i].split(component.part_separator)
                if len(s) > component.max_parts:
                    return False
                for h in s:
                    hashes.add(h)
            hash_params[component.name] = (_HASH_FUNCTIONS[component.hash_format], 
                component.hash_bits, component.hash_algorithm, hashes)
        # calculate the hashes for components
        for k, values in components.iteritems():
            fn, bits, algorithm, hashes = hash_params[k]
            if len(values) < 1:
                return False
            for value in values:
                h = fn(salt + challenge,
                    value, bits, algorithm)
                if h not in hashes:
                    return False
        return True
                
    def code_from_components(self, salt, components):
        format_components = self.components.order_by('ordering')
        # 'a' means match any
        unhashed_format_components = format_components.filter(hash_format='a')
        challenge = bytes()
        for i in unhashed_format_components:
            for value in components.get(i.name, []):
                challenge += value
        hashed_components = list()
        for i, component in enumerate(format_components):
            hash_list = list()
            hash_format = component.hash_format
            values = components.get(component.name, [])
            if hash_format == 'a':
                hash_list += values
            else:
                for value in values:
                    # print "V:", value, i, component
                    hash_list.append(_HASH_FUNCTIONS[component.hash_format](
                        salt + challenge, 
                        value, component.hash_bits, component.hash_algorithm))
            hashed_components.append(component.part_separator.join(hash_list))
        return self.separator.join(hashed_components)

class CodePart(models.Model):
    def __unicode__(self):
        return str(self.ordering) + self.value
    code = models.ForeignKey('Code', related_name = 'parts')
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
    def components(self):
        components = defaultdict(list)
        for i in self.parts.order_by('name', 'ordering'):
            components[i.name].append(i.value)
        return dict(components)
    @components.setter
    def components(self, component_dict):
        self.parts.all().delete()
        print component_dict
        for k, values in component_dict.iteritems():
            for i, value in enumerate(values):
                part = CodePart(code = self, ordering = i,
                    name = k, value = value)
                part.save()
        self.value = self.format.code_from_components(self.salt, component_dict)
    @components.deleter
    def components(self):
        self.parts.delete()
    @classmethod
    def create(cls, format, salt, components):
        c = cls(format=format, salt=salt, value = "foo")
        c.save()
        c.components = components
        return c

class CodeGenerator(models.Model):
    def __unicode__(self):
        return self.salt + " " + unicode(self.format)
    unique_code_component = models.CharField(null = True, blank = True, 
        max_length = 256)
    format = models.ForeignKey('CodeFormat')
    salt = models.CharField(max_length=256)
    codes = models.ManyToManyField('Code', null=True, blank=True)
    def create_code(self, components):
        created_code = Code.create(salt=self.salt, format=self.format, 
            components={})
        if self.unique_code_component:
            components[self.unique_code_component] = [str(created_code.id)]
        created_code.components = components
        created_code.save()
        self.codes.add(created_code)
        return created_code
    def variable_components(self):
        return self.format.components.order_by('ordering').exclude(
            name = self.unique_code_component)
    def code_matches(self, code, components):
        return self.format.code_matches(salt = self.salt, 
            code = code, components = components)
