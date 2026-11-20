"""Stored access codes.

Codes are random strings (see random_code) stored in Code.value; what a
code allows is stored next to it (bober_simple_competition.CompetitorCode
and AdminCode). Codes used to be "talking" codes, built from hashes of
their privileges according to a CodeFormat; CodeFormat, CodeComponent and
the format and salt fields are kept only so that the data of older codes
stays in the database. They are no longer used to create or check codes.
"""
import hashlib

from django.db import models
from django.utils.translation import gettext_lazy as _


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
    [(i, i) for i in sorted(list(hashlib.algorithms_available))] + [('noop', _('No hash'))]
)

DEFAULT_SEPARATOR = "*"
DEFAULT_PART_SEPARATOR = "+"


class CodeField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 256  # up to 2048 bits total
        super(CodeField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(CodeField, self).deconstruct()
        del kwargs["max_length"]
        return name, path, args, kwargs


class CodeComponent(models.Model):
    """Part of a code format of older codes (no longer used)."""
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
    hash_len = models.PositiveIntegerField()
    hash_algorithm = models.CharField(
        max_length=16, choices=HASH_ALGORITHMS,
        null=True, blank=True)
    max_parts = models.IntegerField(default=1)
    part_separator = models.CharField(
        max_length=1, default=DEFAULT_PART_SEPARATOR)


class CodeFormat(models.Model):
    """Format of older codes (no longer used); its separator is still the
    separator between the questionset and the code in competitor codes."""
    def __str__(self):
        if self.name:
            return self.name
        return self.separator.join([
            str(i) for i in self.components.order_by('ordering')])
    separator = models.CharField(max_length=1, default=DEFAULT_SEPARATOR)
    name = models.CharField(max_length=256, blank=True, null=True)


class CodePart(models.Model):
    """Data stored with a code: the privileges of older codes, and the
    code effects ('code_effects') of all codes."""
    def __str__(self):
        return str(self.ordering) + self.value
    code = models.ForeignKey('Code', related_name='code_parts',
                             on_delete=models.CASCADE)
    ordering = models.IntegerField(default=0)
    name = models.CharField(max_length=64)
    value = models.CharField(max_length=256)


class Code(models.Model):
    def __str__(self):
        return self.value
    value = CodeField(db_index=True)
    # salt and format only describe older codes
    salt = models.CharField(max_length=256, blank=True, default='')
    format = models.ForeignKey('CodeFormat', null=True, blank=True,
                               on_delete=models.CASCADE)

    @property
    def parts(self):
        parts = {}
        for i in self.code_parts.order_by('name', 'ordering'):
            parts.setdefault(i.name, []).append(i.value)
        return parts

    def has_part(self, name, value):
        return self.code_parts.filter(name=name, value=value).exists()


class CodeGenerator(models.Model):
    """The codes of one kind (competitor or administrator) of a
    competition."""
    def __str__(self):
        return self.salt + " " + str(self.format)

    unique_code_component = models.CharField(null=True, blank=True,
                                             max_length=256)
    # format and salt only describe older codes
    format = models.ForeignKey('CodeFormat', null=True, blank=True,
                               on_delete=models.CASCADE)
    salt = models.CharField(max_length=256, blank=True, default='')
    codes = models.ManyToManyField('Code', blank=True)

    @property
    def separator(self):
        """Separator between the questionset and the code in the full
        value of competitor codes."""
        if self.format_id is not None:
            return self.format.separator
        return DEFAULT_SEPARATOR
