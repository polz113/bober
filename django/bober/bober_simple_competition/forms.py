from django import forms
from django.forms.models import inlineformset_factory, model_to_dict, fields_for_model
from bober_simple_competition.models import *
from django.utils.translation import ugettext as _

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
