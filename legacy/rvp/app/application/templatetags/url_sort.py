__author__ = 'Peter'
from django import template
register = template.Library()

@register.simple_tag
def url_sort(request, field, value):
    """
    Append '-' if double clicking order_by
    """
    dict_ = request.GET.copy()
    if field == 'order' and field in dict_.keys():
      if dict_[field].startswith('-') and dict_[field].lstrip('-') == value:
      # click twice on same column, revert ascending/descending
        dict_[field] = value
      else:
        dict_[field] = "-"+value
    else:
      dict_[field] = value

    return dict_.urlencode()