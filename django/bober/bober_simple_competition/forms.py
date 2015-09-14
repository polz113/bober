from django import forms
from collections import OrderedDict
from django.forms.models import inlineformset_factory, model_to_dict, fields_for_model
# from django.forms.models import model_to_dict, fields_for_model
from bober_simple_competition.models import *
from django.utils.translation import ugettext as _
from extra_views import InlineFormSet
import code_based_auth.models
from django.contrib.admin import widgets as admin_widgets
import django.forms.extras.widgets as django_widgets
import autocomplete_light
from django.forms import ModelForm, TextInput

class ProfileForm(forms.ModelForm):
    class Meta:
        exclude = tuple()
        model = Profile

class MinimalAccessCodeForm(forms.Form):
    access_code = forms.CharField(label=_('Access code'), max_length=256)

class BasicProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        """exclude = ('user', 'created_codes', 'received_codes',
            'vcard', 'question_sets', 'managed_profiles', 'used_codes',
            'update_used_codes_timestamp', 'update_managers_timestamp')"""
        fields = ('merged_with',);
        widgets = {
            # the autocomplete: off is supposed to preven firefox from filling in the form
            # with the current username
            'merged_with': autocomplete_light.ChoiceWidget('ManagedUsersAutocomplete', 
                attrs={'class':'modern-style', 'autocomplete': 'off'}),
        #    'merged_with': django_widgets.Select()
        }
    password = forms.CharField(required=False, 
        widget = forms.PasswordInput(attrs={'autocomplete': 'off'}))
    def __init__(self, *args, **kwargs):
        _fields = ('first_name', 'last_name', 'email')
        instance = kwargs.get('instance', None)
        _initial = kwargs.get('initial', {})
        _initial.update(
            model_to_dict(instance.user, _fields) if instance is not None else {})
        kwargs['initial'] = _initial
        super(BasicProfileForm, self).__init__(*args, **kwargs)
        # reorder fields
        unordered_fields = self.fields
        unordered_fields.update(fields_for_model(User, _fields))
        self.fields = OrderedDict()
        for k in ['first_name', 'last_name', 'email', 'password', 'merged_with']:
            try:
                self.fields[k] = unordered_fields.pop(k)
            except:
                pass
        # add the fields not listed above at the end
        self.fields.update(unordered_fields)
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
        if self.instance.merged_with is not None:
            for p in self.instance.former_profile_set.all():
                p.merged_with = self.instance.merged_with
        profile = super(BasicProfileForm, self).save(*args,**kwargs)
        profile.managed_profiles.add(profile)
        return profile 

class ProfileEditForm(BasicProfileForm):
    pass

class CodeRegistrationForm(BasicProfileForm):
    class Meta:
        model = Profile
        """exclude = ('user', 'created_codes', 'received_codes',
            'vcard', 'question_sets', 'managed_profiles', 'used_codes',
            'update_used_codes_timestamp', 'update_managers_timestamp')"""
        fields = []
        widgets = {
            # the autocomplete: off is supposed to preven firefox from filling in the form
            # with the current username
            'merged_with': autocomplete_light.ChoiceWidget('ManagedUsersAutocomplete', 
                attrs={'class':'modern-style', 'autocomplete': 'off'}),
        #    'merged_with': django_widgets.Select()
        }
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
            # comment out the following 2 lines to improve performance; 
            # the managers can be update later
            code = codegen.codes.get(value = self.cleaned_data["access_code"])
            self.update_managers(codes = [code])
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
            'questionsets')
        widgets = {
            'start': admin_widgets.AdminSplitDateTime(),
            'end': admin_widgets.AdminSplitDateTime(),
        }
    competitor_code_format = forms.ModelChoiceField(
        queryset = code_based_auth.models.CodeFormat.objects.filter(
            components__name = 'competition_questionset').distinct())
    admin_code_format = forms.ModelChoiceField(
        queryset = code_based_auth.models.CodeFormat.objects.filter(
            components__name = 'admin_privileges').distinct())
    admin_salt = forms.CharField()
    competitor_salt = forms.CharField()

class CompetitionUpdateForm(forms.ModelForm):
    class Meta:
        model = Competition
        exclude = ['questionsets']
        widgets = {
            'start': admin_widgets.AdminSplitDateTime(),
            'end': admin_widgets.AdminSplitDateTime(),
        }

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
        initial = 'a',
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
 
class CompetitionQuestionSetCreateForm(forms.ModelForm):
    class Meta:
        model = CompetitionQuestionSet
        exclude = ('guest_code',)
    create_guest_code = forms.BooleanField(required=False)

class CompetitionQuestionSetUpdateForm(forms.ModelForm):
    class Meta:
        model = CompetitionQuestionSet
        exclude = []
    create_guest_code = forms.BooleanField(required=False)
    def save(self, *args, **kwargs):
        retval = super(CompetitionQuestionSetUpdateForm,self).save(*args, **kwargs)
        if self.cleaned_data['create_guest_code'] and \
                self.instance.guest_code is None:
            print "Generating code!"
            generator = self.instance.competition.competitor_code_generator
            code_data = {
                'competitor_privileges':[
                    'attempt', 'results_before_end'
                ],
                'code_effects': ['new_attempt'],
                'competition_questionset': [
                    self.instance.slug_str()]
            }
            c = generator.create_code(code_data)
            self.instance.guest_code = c
            self.instance.save()
        return retval

class QuestionSetForm(forms.ModelForm):
    class Meta:
        model = QuestionSet
        exclude = ['resource_caches']
    def save(self, *args, **kwargs):
        retval = super(QuestionSetForm, self).save(*args, **kwargs)
        self.instance.rebuild_caches()
        return retval

class CompetitionQuestionSetCreateInline(InlineFormSet):
    model = CompetitionQuestionSet
    form_class = CompetitionQuestionSetCreateForm
    can_delete = False

class CompetitionQuestionSetUpdateInline(InlineFormSet):
    model = CompetitionQuestionSet
    form_class = CompetitionQuestionSetUpdateForm

CompetitionCreateFormSet = inlineformset_factory(Competition,
    CompetitionQuestionSet, form = CompetitionQuestionSetCreateForm, can_delete = False)

CompetitionUpdateFormSet = inlineformset_factory(Competition, 
    CompetitionQuestionSet, form = CompetitionQuestionSetUpdateForm, fields='__all__')
