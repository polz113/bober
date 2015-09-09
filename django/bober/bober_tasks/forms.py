from bober_tasks.models import *
from django import forms
from django.utils.translation import ugettext_lazy
from django.contrib.auth.models import User

class profileForm(forms.Form):
    first_name = forms.CharField(required=False, label=ugettext_lazy("First name"))
    last_name = forms.CharField(required=False, label=ugettext_lazy("Last name"))
    email = forms.CharField(label=ugettext_lazy("Email"))
    password = forms.CharField(widget=forms.PasswordInput, required=False, label=ugettext_lazy("Password"))
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=False, label=ugettext_lazy("Confirm password"))

class AgeGroupForm(forms.ModelForm):
  value = forms.CharField(required=True)
  class Meta:
      model = AgeGroup
      exclude = ('tasks',)

class CategoryForm(forms.ModelForm):
  acronym = forms.CharField(required=True)
  title = forms.CharField(required=True)
  description = forms.CharField(required=True)
  class Meta:
      model = Category
      exclude = []

class DifficultyForm(forms.ModelForm):
  value = forms.CharField(required=True)
  class Meta:
      model = DifficultyLevel
      exclude = []

