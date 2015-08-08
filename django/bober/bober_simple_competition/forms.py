from django import forms
from django.forms.models import inlineformset_factory, model_to_dict, fields_for_model
# from django.forms.models import model_to_dict, fields_for_model
from bober_simple_competition.models import *
from django.utils.translation import ugettext as _
import code_based_auth.models
from django.contrib.admin import widgets

class ProfileForm(forms.ModelForm):
    class Meta:
        exclude = tuple()
        model = Profile

class MinimalAccessCodeForm(forms.Form):
    access_code = forms.CharField(label=_('Access code'), max_length=256)

class BasicProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'created_codes', 'received_codes',
            'vcard', 'merged_with', 'managed_users')
    password = forms.CharField(widget = forms.PasswordInput, required=False)
    def __init__(self, *args, **kwargs):
        _fields = ('first_name', 'last_name', 'email')
        instance = kwargs.get('instance', None)
        _initial = kwargs.get('initial', {})
        _initial.update(model_to_dict(instance.user, _fields) if instance is not None else {})
        kwargs['instance'] = instance
        kwargs['initial'] = _initial
        super(BasicProfileForm, self).__init__(*args, **kwargs)
        self.fields.update(fields_for_model(User, _fields))

    def save(self, *args, **kwargs):
        if self.instance.id is not None:
            u = self.instance.user
        else:
            u = User()
        cleaned_data = self.cleaned_data
        u.first_name = cleaned_data['first_name']
        u.last_name = cleaned_data['last_name']
        u.email = cleaned_data['email']
        u.username = cleaned_data['email']
        password = cleaned_data.get('password', '')
        if self.instance.id is None and len(password) < 1:
            password = cleaned_data[access_code]
            self.cleaned_data["password"] = password 
        if len(password) > 0:
            u.set_password(cleaned_data['password'])
        u.save()
        if self.instance.id is None:
            self.instance = u.profile
        profile = super(BasicProfileForm, self).save(*args,**kwargs)
        return profile 

class ProfileEditForm(BasicProfileForm):
    pass

class CodeRegistrationForm(BasicProfileForm):
    access_code = forms.CharField(label=_('Access code'), max_length=256)
    register_as = forms.ChoiceField(choices=USER_ROLES)
    competition = forms.ModelChoiceField(Competition.objects.all())
    def save(self, *args, **kwargs):
        profile = super(CodeRegistrationForm, self).save(*args,**kwargs)
        competition = self.cleaned_data['competition']
        if self.cleaned_data['register_as'] == 'admin':
            codegen = competition.administrator_code_generator
        elif self.cleaned_data['register_as'] == 'competitor':
            codegen = competition.competitor_code_generator
        try:
            # since the codes might not be synchronized between nodes, this
            # might as well fail. The managers for a user can be recreated later.
            code = codegen.codes.get(value = self.cleaned_data["access_code"])
            for o in code.owner_set.all():
                o.managed_users.add(profile.user)
                for s in superiors(o, 
                        competition.administrator_code_generator, set()):
                    s.managed_users.add(profile.user)
        except Exception, e:
            print e
            pass
        return profile
    
    def clean(self):
        cleaned_data = super(CodeRegistrationForm, self).clean()
        if cleaned_data['register_as'] == 'admin':
            codegen = cleaned_data['competition'].administrator_code_generator
        elif cleaned_data['register_as'] == 'competitor':
            codegen = cleaned_data['competition'].competitor_code_generator
        else:
            raise forms.ValidationError(_("Wrong user role"))
        if not codegen.code_matches(cleaned_data['access_code'], 
            {'competitor_privileges': ['attempt']}):
            raise forms.ValidationError(_("Invalid access code"))
        return cleaned_data

class CompetitionRegistrationForm(CodeRegistrationForm):
    register_as = forms.ChoiceField(choices=USER_ROLES)
    competition = forms.ModelChoiceField(Competition.objects.all(), widget=forms.HiddenInput)

class ImmediateCompetitionForm(CompetitionRegistrationForm):
    competition_questionset_field = forms.ModelChoiceField(
        queryset = CompetitionQuestionSet.objects.all())

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
            'questionsets', 'guest_code')
        widgets = {
            'start': widgets.AdminSplitDateTime(),
            'end': widgets.AdminSplitDateTime(),

        }
    competitor_code_format = forms.ModelChoiceField(
        queryset = code_based_auth.models.CodeFormat.objects.filter(
            components__name = 'competition_questionset').distinct())
    admin_code_format = forms.ModelChoiceField(
        queryset = code_based_auth.models.CodeFormat.objects.filter(
            components__name = 'admin_privileges').distinct())
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
    code_effects_bits = forms.IntegerField()
    code_effects_format = forms.ChoiceField(
        choices = code_based_auth.models.CODE_COMPONENT_FORMATS)
    code_effects_hash = forms.ChoiceField(
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
 
CompetitionFormSet = inlineformset_factory(Competition, 
    CompetitionQuestionSet, fields='__all__')

