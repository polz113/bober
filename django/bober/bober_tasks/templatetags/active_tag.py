from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag
def add_active( request, name, by_path=False ):
    """ Return the string 'active' current request.path is same as name
        Keyword aruguments:
        request -- Django request object
        name -- name of the url or the actual path
        by_path -- True if name contains a url instead of url name"""

    if by_path:
        path = name
    else:
        path = reverse(name)

    if request.path == path:
        return ' active '

    return ''