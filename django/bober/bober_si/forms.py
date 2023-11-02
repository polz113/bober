from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from bober_si.models import School
from dal import autocomplete
import django.core.validators as validators


class OverviewForm(forms.Form):
    access_code = forms.CharField(label=_('Access code'), max_length=256)


class SchoolCodesCreateForm(forms.Form):
    school = forms.ModelChoiceField(label=_('School'), queryset=School.objects.all(),
                                    widget=autocomplete.ModelSelect2(url='school_autocomplete'))


def validate_username_unique(value):
    try:
        assert not User.objects.filter(username=value).exists()
    except Exception:
        raise ValidationError(_('A user with this username exists'))


def validate_email_unique(value):
    try:
        assert not User.objects.filter(email=value).exists()
    except Exception:
        raise ValidationError(_('A user with this email exists'))


class TeacherCodeRegistrationPasswordResetForm(forms.Form):
    username = forms.SlugField(label=_('username'), max_length=30,
                               validators=[validators.validate_slug,
                                           validate_username_unique])
    email = forms.EmailField(label=_('email'),
                             validators=[validators.validate_email,
                                         validate_email_unique])
    password = forms.CharField(label=_('password'),  widget=forms.PasswordInput)
    hidden_code = forms.CharField(label=_('hidden_code'), widget=forms.HiddenInput)
