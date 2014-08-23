from application.models import *
from django import forms
from django.utils.translation import ugettext_lazy
from django.contrib.auth.models import User

class newqForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    body = forms.CharField(widget=forms.Textarea, required=True)
    answer = forms.CharField(required=True)
    category = forms.CharField(required=True)
    language = forms.ChoiceField(choices=[('1','Slovensko'), ('2', 'English')])
    age = forms.ChoiceField(choices=[('1','10-15'), ('2', '15-20')])
    comment = forms.CharField(required=False)

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

class DifficultyForm(forms.ModelForm):
  value = forms.CharField(required=True)
  class Meta:
      model = DifficultyLevel

class LanguageForm(forms.ModelForm):
  value = forms.CharField(required=True)
  value_short = forms.CharField(required=True)
  class Meta:
      model = Language

class EditUserForm(forms.ModelForm):
    #first_name = forms.CharField(required=False, label=ugettext_lazy("First name"))
    #last_name = forms.CharField(required=False, label=ugettext_lazy("Last name"))
    #email = forms.CharField(label=ugettext_lazy("Email"))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'groups', 'is_staff', 'is_active', 'is_superuser']

class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['interface_lang_code']
