__author__ = 'Peter'
from django import template
register = template.Library()

@register.filter(name='to_char')
def to_char_(value):
    return chr(value + 64)