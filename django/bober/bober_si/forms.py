from django import forms
from django.utils.translation import ugettext as _
from extra_views import InlineFormSet
from models import School
import autocomplete_light

class OverviewForm(forms.Form):
    access_code = forms.CharField(label=_('Access code'), max_length=256)

class SchoolCodesCreateForm(forms.Form):
    school = forms.ModelChoiceField(label=_('School'), queryset=School.objects.all(),
        widget=autocomplete_light.ChoiceWidget('SchoolAutocomplete',
            attrs={'class':'modern-style'}))
    
