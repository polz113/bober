from django import forms
from collections import OrderedDict
from django.forms.models import inlineformset_factory, model_to_dict, fields_for_model
# from django.forms.models import model_to_dict, fields_for_model
from bober_simple_competition.models import *
from django.utils.translation import ugettext_lazy as _
from extra_views import InlineFormSet
import code_based_auth.models
import django.forms.extras.widgets as django_widgets
import autocomplete_light
from django.forms import ModelForm, TextInput
from django.core.validators import validate_email

class ProfileForm(forms.ModelForm):
    class Meta:
        exclude = tuple()
        model = Profile

class AccessCodeForm(forms.Form):
    access_code = forms.CharField(label=_('Access code'), max_length=256)
    defer_update_used_codes = forms.BooleanField(
            label=_('Update used codes later'), required = False,
            initial = False)
    defer_effects = forms.BooleanField(
            label=_('Execute effects later'), required = False,
            initial = False)

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

class QuestionSetRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
    username = forms.CharField(required=False, widget=forms.HiddenInput())
    access_code = forms.CharField(label=_('Access code'))
    def __init__(self, *args, **kwargs):
        cqs = kwargs.pop('competitionquestionset')
        self.questionset_slug = cqs.slug_str()
        self.codegen = cqs.competition.competitor_code_generator
        retval = super(QuestionSetRegistrationForm, self).__init__(*args, **kwargs)
        self._meta.fields += ['username', 'email']
        return retval
    def clean(self):
        if len(self.cleaned_data.get('username', '')) < 1:
            self.cleaned_data['username'] = '.'.join([
                slugify(self.cleaned_data.get('first_name', u'')),
                slugify(self.cleaned_data.get('last_name', u'')),
                slugify(self.cleaned_data.get('access_code', u''))])[:30]
        if len(self.cleaned_data.get('email', '')) < 1:
            self.cleaned_data['email'] = self.cleaned_data['username'] + '@bober.acm.si'
        cleaned_data = super(QuestionSetRegistrationForm, self).clean()
        if cleaned_data is None:
            cleaned_data = self.cleaned_data
        if not self.cleaned_data.get('password', None):
            self.cleaned_data['password'] = self.cleaned_data.get('access_code', '')
        return cleaned_data
    def clean_access_code(self):
        full_code = self.questionset_slug + self.codegen.format.separator + self.cleaned_data['access_code']
        if not self.codegen.code_matches(full_code, 
            {'competitor_privileges':['attempt']}):
            raise ValidationError(_('Wrong access code'), code='access_code')
        self.cleaned_data['full_code'] = full_code
        return self.cleaned_data['access_code']
    #def clean_username(self):
    #    validate_email(self.cleaned_data['username'])
    #    return self.cleaned_data['username']
    def save(self, *args, **kwargs):
        instance = super(QuestionSetRegistrationForm, self).save(*args,**kwargs)
        password = self.cleaned_data.get('password', '')
        if len(password) > 0:
            instance.set_password(password)
            instance.save()
        instance.profile.managed_profiles.add(instance.profile)
        return instance

class CompetitionRegistrationForm(QuestionSetRegistrationForm):
    def __init__(self, *args, **kwargs):
        self.competition = kwargs.pop('competition')
        self.codegen = self.competition.competitor_code_generator
        retval = super(QuestionSetRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['competition_questionset'] = forms.ModelChoiceField(label=_("Group"), queryset = self.competition.competitionquestionset_set.all(), required=True)
        self._meta.fields += ['username', 'email']
        return retval
    def clean_access_code(self):
        return self.cleaned_data['access_code']
    def clean_competition_questionset(self):
        return self.cleaned_data['competition_questionset']
    def clean(self):
        cqs = self.cleaned_data.get('competition_questionset', None)
        if cqs is not None:
            questionset_slug = self.cleaned_data['competition_questionset'].slug_str()
            full_code = questionset_slug + self.codegen.format.separator + self.cleaned_data['access_code']
            if not self.codegen.code_matches(full_code, 
                    {'competitor_privileges':['attempt']}):
                self.errors['access_code']=[_('Wrong access code')]
            self.cleaned_data['full_code'] = full_code
        else:
            self.errors['competition_questionset']=[_('This field is required')]
        return super(CompetitionRegistrationForm, self).clean()

class QuestionSetCompetitorForm(forms.ModelForm):
    class Meta:
        model = Competitor
        fields = ['first_name', 'last_name']
    # profile = forms.ModelChoiceField(required=False, queryset=Profile.objects.all(), widget=forms.HiddenInput())
    short_access_code = forms.CharField(label=_('Access code'))
    def __init__(self, *args, **kwargs):
        cqs = kwargs.pop('competitionquestionset')
        self.profile = kwargs.pop('profile', False)
        self.questionset_slug = cqs.slug_str()
        self.codegen = cqs.competition.competitor_code_generator
        retval = super(QuestionSetCompetitorForm, self).__init__(*args, **kwargs)
        self._meta.fields += ['profile']
        return retval
    def clean(self):
        cleaned_data = super(QuestionSetCompetitorForm, self).clean()
        if cleaned_data is None:
            cleaned_data = self.cleaned_data
        cleaned_data['profile'] = self.profile
        self.cleaned_data = cleaned_data
        return cleaned_data
    def clean_short_access_code(self):
        full_code = self.questionset_slug + self.codegen.format.separator + self.cleaned_data['short_access_code']
        if not self.codegen.code_matches(full_code, 
            {'competitor_privileges':['attempt']}):
            raise ValidationError(_('Wrong access code'), code='short_access_code')
        if self.codegen.code_matches(full_code,
            {'competitor_privileges':['resume_attempt']}):
            if not self.profile:
                self.profile = None
        self.cleaned_data['full_code'] = full_code
        return self.cleaned_data['short_access_code']
    #def clean_username(self):
    #    validate_email(self.cleaned_data['username'])
    #    return self.cleaned_data['username']
    def save(self, *args, **kwargs):
        try:
            assert self.profile is not False
            cleaned = self.cleaned_data
            self.instance = Competitor.objects.filter(profile = cleaned['profile'],
                first_name = cleaned['first_name'],
                last_name = cleaned['last_name'])[0]
        except:
            pass
        print self.instance.id, self.instance
        instance = super(QuestionSetCompetitorForm, self).save(*args,**kwargs)
        print instance.id, self.instance
        return instance

class CompetitionCompetitorForm(QuestionSetCompetitorForm):
    def __init__(self, *args, **kwargs):
        self.competition = kwargs.pop('competition')
        self.profile = kwargs.pop('profile', False)
        self.codegen = self.competition.competitor_code_generator
        retval = super(QuestionSetCompetitorForm, self).__init__(*args, **kwargs)
        self.fields['competition_questionset'] = forms.ModelChoiceField(label=_("Group"), queryset = self.competition.competitionquestionset_set.all(), required=True)
        self._meta.fields += ['profile']
        return retval
    def clean_short_access_code(self):
        return self.cleaned_data['short_access_code']
    def clean_competition_questionset(self):
        return self.cleaned_data['competition_questionset']
    def clean(self):
        cqs = self.cleaned_data.get('competition_questionset', None)
        if cqs is not None:
            questionset_slug = self.cleaned_data['competition_questionset'].slug_str()
            full_code = questionset_slug + self.codegen.format.separator + self.cleaned_data['short_access_code']
            if not self.codegen.code_matches(full_code, 
                    {'competitor_privileges':['attempt']}):
                self.errors['short_access_code']=[_('Wrong access code')]
            if self.codegen.code_matches(full_code,
                {'competitor_privileges':['resume_attempt']}):
                if not self.profile:
                    self.profile = None
            self.cleaned_data['full_code'] = full_code
        else:
            self.errors['competition_questionset']=[_('This field is required')]
        return super(CompetitionCompetitorForm, self).clean()


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
            'start': forms.DateInput(attrs={'class': 'datepicker'}),
            'end': forms.DateInput(attrs={'class': 'datepicker'}),
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
            'start': forms.DateInput(attrs={'class': 'datepicker'}),
            'end': forms.DateInput(attrs={'class': 'datepicker'}),
        }

class CodeFormatForm(forms.Form):
    code_id_length = forms.IntegerField(initial=8)
    code_id_format = forms.ChoiceField(
        choices = code_based_auth.models.CODE_COMPONENT_FORMATS)
    competitor_privilege_length = forms.IntegerField(min_value=1)
    competitor_privilege_format = forms.ChoiceField(
        choices = code_based_auth.models.CODE_COMPONENT_FORMATS)
    competitor_privilege_hash = forms.ChoiceField(
        initial = code_based_auth.models.DEFAULT_HASH_ALGORITHM,
        choices = code_based_auth.models.HASH_ALGORITHMS)

class CompetitorCodeFormatForm(CodeFormatForm):
    questionset_format = forms.ChoiceField(
        choices = code_based_auth.models.CODE_COMPONENT_FORMATS)
    questionset_hash = forms.ChoiceField(
        initial = 'noop',
        choices = code_based_auth.models.HASH_ALGORITHMS)
 
class AdminCodeFormatForm(CodeFormatForm):
    admin_privilege_length = forms.IntegerField(min_value=1)
    admin_privilege_format = forms.ChoiceField(
        choices = code_based_auth.models.CODE_COMPONENT_FORMATS)
    admin_privilege_hash = forms.ChoiceField(
        initial = code_based_auth.models.DEFAULT_HASH_ALGORITHM,
        choices = code_based_auth.models.HASH_ALGORITHMS)
    allowed_effects_length = forms.IntegerField(min_value=1)
    allowed_effects_format = forms.ChoiceField(
        choices = code_based_auth.models.CODE_COMPONENT_FORMATS)
    allowed_effects_hash = forms.ChoiceField(
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
