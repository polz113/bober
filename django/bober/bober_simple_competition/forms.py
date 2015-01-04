from django import forms
from django.forms.models import inlineformset_factory, model_to_dict, fields_for_model
from bober_simple_competition.models import *
from django.utils.translation import ugettext as _
import code_based_auth.models

class ProfileForm(forms.ModelForm):
    class Meta:
        exclude = tuple()
        model = Profile

class ImmediateCompetitionForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'created_codes', 'received_codes',
            'vcard', 'merged_with')
    competition_questionset_field = forms.ModelChoiceField(
        queryset = CompetitionQuestionSet.objects.all())

class UserForm(forms.ModelForm):
    class Meta:
        exclude = tuple()
        model = User

class MinimalCompetitionRegistrationForm(forms.Form):
    access_code = forms.CharField(label=_('Access code'), max_length=256)

class BasicRegistrationForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user','registration_codes','received_codes',
            'vcard', 'merged_with')
    
    def __init__(self, instance=None, *args, **kwargs):
        _fields = ('first_name', 'last_name', 'email',)
        _initial = model_to_dict(instance.user, _fields) if instance is not None else {}
        super(BasicRegistrationForm, self).__init__(initial=_initial, instance=instance, *args, **kwargs)
        self.fields.update(fields_for_model(User, _fields))

    def save(self, *args, **kwargs):
        u = self.instance.user
        u.first_name = self.cleaned_data['first_name']
        u.last_name = self.cleaned_data['last_name']
        u.email = self.cleaned_data['email']
        u.save()
        profile = super(BasicRegistrationForm, self).save(*args,**kwargs)
        return profile

class VCardRegistrationForm(BasicRegistrationForm):
    class Meta:
        model = Profile
        exclude = ('user', 'created_codes', 'received_codes',
            'vcard', 'merged_with')
    def __init__(self, instance=None, *args, **kwargs):
        _fields = ('first_name', 'last_name', 'email',)
        _initial = model_to_dict(instance.user, _fields) if instance is not None else {}
        super(BasicRegistrationForm, self).__init__(initial=_initial, instance=instance, *args, **kwargs)
        self.fields.update(fields_for_model(User, _fields))
    def save(self, *args, **kwargs):
        u = self.instance.user
        u.first_name = self.cleaned_data['first_name']
        u.last_name = self.cleaned_data['last_name']
        u.email = self.cleaned_data['email']
        u.save()
        profile = super(BasicRegistrationForm, self).save(*args,**kwargs)
        return profile

class TeacherRegistrationForm(VCardRegistrationForm):
    class Meta:
        model = Profile
        exclude = ('user', 'received_codes', 'created_codes',
            'vcard','merged_with')
    def __init__(self, instance=None, *args, **kwargs):
        _fields = ('first_name', 'last_name', 'email',)
        _initial = model_to_dict(instance.user, _fields) if instance is not None else {}
        super(BasicRegistrationForm, self).__init__(initial=_initial, instance=instance, *args, **kwargs)
        self.fields.update(fields_for_model(User, _fields))
    def save(self, *args, **kwargs):
        u = self.instance.user
        u.first_name = self.cleaned_data['first_name']
        u.last_name = self.cleaned_data['last_name']
        u.email = self.cleaned_data['email']
        u.save()
        profile = super(BasicRegistrationForm, self).save(*args,**kwargs)
        return profile

class CompetitorCodeForm(forms.Form):
    competitor_privileges = forms.MultipleChoiceField(
        choices=COMPETITOR_PRIVILEGES)

class AdminCodeForm(CompetitorCodeForm):
    admin_privileges = forms.MultipleChoiceField(choices=ADMIN_PRIVILEGES)

class CompetitionCreateForm(forms.ModelForm):
    class Meta:
        model = Competition
        exclude = ('administrator_code_generator', 
            'competitor_code_generator',
            'questionsets')
    competitor_code_format = forms.ModelChoiceField(
        queryset = code_based_auth.models.CodeFormat.objects.all())
    admin_code_format = forms.ModelChoiceField(
        queryset = code_based_auth.models.CodeFormat.objects.all())
    admin_salt = forms.CharField()
    competitor_salt = forms.CharField()

class CodeFormatForm(forms.Form):
    code_id_bits = forms.IntegerField(initial=32)
    competitor_privilege_bits = forms.IntegerField()
    competitor_privilege_format = forms.ChoiceField(
        choices = code_based_auth.models.CODE_COMPONENT_FORMATS)
    competitor_privilege_hash = forms.ChoiceField(
        initial = code_based_auth.models.DEFAULT_HASH_ALGORITHM,
        choices = code_based_auth.models.HASH_ALGORITHMS)
   
class CompetitorCodeFormatForm(CodeFormatForm):
    questionset_bits = forms.IntegerField()
    questionset_format = forms.ChoiceField(
        initial = 'r',
        choices = code_based_auth.models.CODE_COMPONENT_FORMATS)
    questionset_hash = forms.ChoiceField(
        initial = 'noop',
        choices = code_based_auth.models.HASH_ALGORITHMS)
 
class AdminCodeFormatForm(CodeFormatForm):
    admin_privilege_bits = forms.IntegerField()
    admin_privilege_format = forms.ChoiceField(
        choices = code_based_auth.models.CODE_COMPONENT_FORMATS)
    admin_privilege_hash = forms.ChoiceField(
        initial = code_based_auth.models.DEFAULT_HASH_ALGORITHM,
        choices = code_based_auth.models.HASH_ALGORITHMS)
 
CompetitionFormSet = forms.inlineformset_factory(Competition, CompetitionQuestionSet)

