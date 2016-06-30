from django import forms
from django.utils.translation import ugettext as _
from extra_views import InlineFormSet
from models import School
import autocomplete_light
import autocomplete_light.widgets

class OverviewForm(forms.Form):
    access_code = forms.CharField(label=_('Access code'), max_length=256)

class SchoolCodesCreateForm(forms.Form):
    school = forms.ModelChoiceField(label=_('School'), queryset=School.objects.all(),
        widget=autocomplete_light.widgets.ChoiceWidget('SchoolAutocomplete',
            attrs={'class':'modern-style'}))

class TeacherCodeRegistrationPasswordResetForm(forms.Form):
    email = forms.EmailField(label=_('email'), max_length=30)
    password = forms.CharField(label=_('password'),  widget=forms.PasswordInput)
    hidden_code = forms.CharField(label=_('hidden_code'), widget=forms.HiddenInput)
