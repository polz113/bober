from django import forms
from collections import OrderedDict
from django.forms.models import inlineformset_factory, model_to_dict,\
    fields_for_model
from django.contrib.admin import widgets
from bober_simple_competition.models import\
    ADMIN_PRIVILEGES, COMPETITOR_PRIVILEGES,\
    Profile, Competitor, Competition,\
    CompetitionQuestionSet, QuestionSet
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from extra_views import InlineFormSet
import code_based_auth.models
from django.core.exceptions import ValidationError
# import django.forms.extras.widgets as django_widgets
# from django.forms import ModelForm, TextInput
# from django.core.validators import validate_email
# from django.contrib.flatpages.models import FlatPage
from dal import autocomplete
# from django.contrib import admin
from django.contrib.auth.models import User
# from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
# from django.template.loader import render_to_string
from popup_modelviews.widgets import add_related_field_wrapper
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Fieldset, Div


class ProfileForm(forms.ModelForm):
    class Meta:
        exclude = tuple()
        model = Profile


class ProfileAdminForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = tuple()
        widgets = {
            'managed_profiles': autocomplete.ModelSelect2Multiple(url='profile_autocomplete'),
            'merged_with': autocomplete.ModelSelect2(url='profile_autocomplete'),
            'created_codes': autocomplete.ModelSelect2Multiple(url='code_autocomplete'),
            'received_codes': autocomplete.ModelSelect2Multiple(url='code_autocomplete'),
            'used_codes': autocomplete.ModelSelect2Multiple(url='code_autocomplete'),
        }


class CompetitionQuestionSetInlineAdminForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = tuple()
        widgets = {
            'guest_code': autocomplete.ModelSelect2Multiple(url='code_autocomplete'),
        }



class AccessCodeForm(forms.Form):
    access_code = forms.CharField(label=_('Access code'), max_length=256)
    defer_update_used_codes = forms.BooleanField(
            label=_('Update used codes later'), required=False,
            initial=False)
    defer_effects = forms.BooleanField(
            label=_('Execute effects later'), required=False,
            initial=False)


class MinimalAccessCodeForm(forms.Form):
    access_code = forms.CharField(label=_('Access code'), max_length=256)


class BasicProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        """exclude = ('user', 'created_codes', 'received_codes',
            'vcard', 'question_sets', 'managed_profiles', 'used_codes',
            'update_used_codes_timestamp', 'update_managers_timestamp')"""
        # fields = ('merged_with',);
        fields = ('date_of_birth',)
        widgets = {
            # the autocomplete: off is supposed to prevent firefox from filling in the form
            # with the current username
        #    'merged_with': autocomplete.ModelSelect2(url='profile_autocomplete'),
        #    'merged_with': autocomplete_light.ChoiceWidget('ManagedUsersAutocomplete',
        #        attrs={'class':'modern-style', 'autocomplete': 'off'}),
        #    'merged_with': django_widgets.Select()
        }
    # password = forms.CharField(required=False, widget = forms.PasswordInput(attrs={'autocomplete': 'off'}),label=_("Password"),)

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
        for k in ['first_name', 'last_name', 'email', 'merged_with']:
            try:
                self.fields[k] = unordered_fields.pop(k)
            except:
                pass
        # add the fields not listed above at the end
        self.fields.update(unordered_fields)

    def save(self, *args, **kwargs):
        cleaned_data = self.cleaned_data
        user_data = dict()
        for k in ['first_name', 'last_name', 'email', 'username', 'password']:
            if len(cleaned_data.get(k, '')):
                user_data[k] = cleaned_data[k]
        if self.instance.id is not None:
            u = User.objects.filter(profile__id=self.instance.id)
            u.update(**user_data)
            u = u[0]
        else:
            u = User.objects.create(**user_data)
            self.instance = u.profile
        password = user_data.get('password', '')
        if len(password) > 0:
            u.set_password(password)
            u.save()
        if self.instance.merged_with == self.instance:
            self.instance.merged_with = None
        if self.instance.merged_with is not None:
            for p in self.instance.former_profile_set.all():
                p.merged_with = self.instance.merged_with
                p.save()
        profile = super(BasicProfileForm, self).save(*args, **kwargs)
        profile = profile.merge_to_top(limit=10)
        # by default, each user should be able to manage their own profile.
        profile.managed_profiles.add(profile)
        return profile


class ProfileEditForm(BasicProfileForm):
    pass


class ProfileMergeForm(forms.ModelForm):
    class Meta:
        model = Profile
        """exclude = ('user', 'created_codes', 'received_codes',
            'vcard', 'question_sets', 'managed_profiles', 'used_codes',
            'update_used_codes_timestamp', 'update_managers_timestamp')"""
        fields = ('merged_with',)
        # fields = ()
        widgets = {
            'merged_with': autocomplete.ModelSelect2(url='profile_autocomplete')
        }
        labels = {
            'merged_with': _('Merged with')
        }

        def clean(self):
            # assert both profiles are managed
            managed_profiles = self.request.profile.managed_profiles
            assert managed_profiles.filter(id=self.instance.id).exists()
            assert managed_profiles.filter(id=self.instance.mereged_with).exists()


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
            self.cleaned_data['email'] = self.cleaned_data['username'] \
                + '@bober.acm.si'
        cleaned_data = super(QuestionSetRegistrationForm, self).clean()
        if cleaned_data is None:
            cleaned_data = self.cleaned_data
        if not self.cleaned_data.get('password', None):
            self.cleaned_data['password'] = self.cleaned_data.get('access_code', '')
        return cleaned_data

    def clean_access_code(self):
        full_code = self.questionset_slug + self.codegen.format.separator\
            + self.cleaned_data['access_code']
        if not self.codegen.code_matches(
                full_code,
                {'competitor_privileges': ['attempt']}):
            raise ValidationError(_('Wrong access code'), code='access_code')
        self.cleaned_data['full_code'] = full_code
        return self.cleaned_data['access_code']

    #def clean_username(self):
    #    validate_email(self.cleaned_data['username'])
    #    return self.cleaned_data['username']

    def save(self, *args, **kwargs):
        instance = super(QuestionSetRegistrationForm, self).save(*args, **kwargs)
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
        self.fields['competition_questionset'] = forms.ModelChoiceField(
            label=_("Group"),
            queryset=self.competition.competitionquestionset_set.all(),
            required=True)
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
            full_code = questionset_slug + self.codegen.format.separator\
                + self.cleaned_data['access_code']
            if not self.codegen.code_matches(
                    full_code,
                    {'competitor_privileges': ['attempt']}):
                self.errors['access_code'] = [_('Wrong access code')]
            self.cleaned_data['full_code'] = full_code
        else:
            self.errors['competition_questionset'] = [_('This field is required')]
        return super(CompetitionRegistrationForm, self).clean()


class QuestionSetCompetitorForm(forms.ModelForm):
    class Meta:
        model = Competitor
        fields = ['first_name', 'last_name']
    # profile = forms.ModelChoiceField(required=False, queryset=Profile.objects.all(), widget=forms.HiddenInput())
    short_access_code = forms.CharField(label=_('Access code'), required=False)

    def __init__(self, *args, **kwargs):
        cqs = kwargs.pop('competitionquestionset')
        self.guest_code = cqs.guest_code
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
        cleaned_data['profile'] = self.profile or None
        self.cleaned_data = cleaned_data
        return cleaned_data

    def clean_short_access_code(self):
        short_code = self.cleaned_data.get('short_access_code', '')
        if len(short_code):
            full_code = self.questionset_slug \
                + self.codegen.format.separator \
                + short_code
        else:
            full_code = None
            if self.guest_code is not None:
                full_code = self.guest_code.value
            if full_code is None:
                self.errors['short_access_code'] = [_('Wrong access code')]
        if not self.codegen.code_matches(
                full_code,
                {'competitor_privileges': ['attempt']}):
            raise ValidationError(_('Wrong access code'), code='short_access_code')
        if self.codegen.code_matches(
                full_code,
                {'competitor_privileges': ['resume_attempt']}):
            # print("code:", full_code)
            full_code = self.codegen.canonical_code(full_code)
            # print("  canonical:", full_code)
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
            self.instance = Competitor.objects.filter(
                profile=cleaned['profile'],
                first_name=cleaned['first_name'],
                last_name=cleaned['last_name'])[0]
        except:
            pass
        # print self.instance.id, self.instance
        instance = super(QuestionSetCompetitorForm, self).save(*args, **kwargs)
        # print instance.id, self.instance
        return instance


class CompetitionSetChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return u"{}".format(obj.name)


class CompetitionCompetitorForm(QuestionSetCompetitorForm):

    def __init__(self, *args, **kwargs):
        self.competition = kwargs.pop('competition')
        self.profile = kwargs.pop('profile', False)
        self.codegen = self.competition.competitor_code_generator
        retval = super(QuestionSetCompetitorForm, self).__init__(*args, **kwargs)
        self.fields['competition_questionset'] = CompetitionSetChoiceField(
            label=_("Group"),
            queryset=self.competition.competitionquestionset_set.all(),
            required=True)
        self._meta.fields += ['profile']
        return retval

    def clean_short_access_code(self):
        return self.cleaned_data.get('short_access_code', '')

    def clean_competition_questionset(self):
        return self.cleaned_data['competition_questionset']

    def clean(self):
        cqs = self.cleaned_data.get('competition_questionset', None)
        if cqs is not None:
            questionset_slug = self.cleaned_data['competition_questionset'].slug_str()
            short_code = self.cleaned_data.get('short_access_code', '')
            if len(short_code):
                # print("short code: ", short_code)
                full_code = self.codegen.canonical_code(
                    questionset_slug + self.codegen.format.separator
                    + short_code)
                # print("canonical code: ", full_code)
            else:
                full_code = None
                if cqs.guest_code is not None:
                    full_code = cqs.guest_code.value
                if full_code is None:
                    self.errors['short_access_code'] = [_('Wrong access code')]
            if not self.codegen.code_matches(
                    full_code,
                    {'competitor_privileges': ['attempt']}):
                self.errors['short_access_code'] = [_('Wrong access code')]
            if self.codegen.code_matches(
                    full_code,
                    {'competitor_privileges': ['resume_attempt']}):
                if not self.profile:
                    self.profile = None
            self.cleaned_data['full_code'] = full_code
        else:
            self.errors['competition_questionset'] = [_('This field is required')]
        return super(CompetitionCompetitorForm, self).clean()


class CompetitorUpdateForm(forms.ModelForm):
    class Meta:
        model = Competitor
        fields = ['first_name', 'last_name']
    cqs_id = forms.IntegerField(min_value=0, widget=forms.HiddenInput)
    attempt_id = forms.IntegerField(min_value=0, widget=forms.HiddenInput)


class CompetitorCodeForm(forms.Form):
    competitor_privileges = forms.MultipleChoiceField(
        choices=COMPETITOR_PRIVILEGES,
        widget=forms.CheckboxSelectMultiple())


class AdminCodeForm(CompetitorCodeForm):
    admin_privileges = forms.MultipleChoiceField(
        choices=ADMIN_PRIVILEGES,
        widget=forms.CheckboxSelectMultiple())


class CompetitionFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(CompetitionFormHelper, self).__init__(*args, **kwargs)
        self.form_method = 'POST'
        self.form_tag = False
        self.disable_csrf = True
        self.form_class = "form-horizontal"
        self.label_class = 'col-lg-2'
        self.field_class = 'col-lg-10'


class CompetitionCreateFormHelper(CompetitionFormHelper):
    def __init__(self, *args, **kwargs):
        super(CompetitionCreateFormHelper, self).__init__(*args, **kwargs)
        self.layout = Layout(
            Fieldset(
                _('Basic competition data'),
                'title',
                'slug',
                'start',
                'end',
                'duration',
                'motd',
            ),
            Fieldset(
                "<a data-toggle='collapse' href='#competition_advanced'>"
                + str(_('Advanced competition data')) + "</a>",
                Div(
                    'promoted',
                    'competitor_code_format',
                    'competitor_salt',
                    'admin_code_format',
                    'admin_salt',
                    css_class="competition_advanced collapse",
                    id="competition_advanced",
                )
            ),
        )


class CompetitionCreateForm(forms.ModelForm):
    class Meta:
        model = Competition
        exclude = (
            'administrator_code_generator',
            'competitor_code_generator',
            'questionsets')
        widgets = {
            'start': widgets.AdminDateWidget(),
            'end': widgets.AdminDateWidget(),
        }
    competitor_code_format = forms.ModelChoiceField(
        queryset=code_based_auth.models.CodeFormat.objects.filter(
            components__name='competition_questionset').distinct(),
        label=_('Competitor code format'))
    admin_code_format = forms.ModelChoiceField(
        queryset=code_based_auth.models.CodeFormat.objects.filter(
            components__name='admin_privileges').distinct(),
        label=_('Admin code format'))
    admin_salt = forms.CharField(label=_('Admin salt'))
    competitor_salt = forms.CharField(label=_('Competitor salt'))

    def __init__(self, *args, **kwargs):
        super(CompetitionCreateForm, self).__init__(*args, **kwargs)
        self.helper = CompetitionCreateFormHelper()


class CompetitionUpdateFormHelper(CompetitionFormHelper):
    def __init__(self, *args, **kwargs):
        super(CompetitionUpdateFormHelper, self).__init__(*args, **kwargs)


class CompetitionUpdateForm(forms.ModelForm):
    class Meta:
        model = Competition
        exclude = ['questionsets']
        widgets = {
            'start': widgets.AdminDateWidget(),
            'end': widgets.AdminDateWidget(),
        }
        # widgets = {
        #     'start': forms.DateInput(attrs={'class': 'datepicker'}),
        #     'end': forms.DateInput(attrs={'class': 'datepicker'}),
        # }

    def __init__(self, *args, **kwargs):
        super(CompetitionUpdateForm, self).__init__(*args, **kwargs)
        self.helper = CompetitionUpdateFormHelper()


class CodeFormatForm(forms.Form):
    code_id_length = forms.IntegerField(initial=8, label=_("Code id length"))
    code_id_format = forms.ChoiceField(
        choices=code_based_auth.models.CODE_COMPONENT_FORMATS,
        label=_("Code id format"))
    competitor_privilege_length = forms.IntegerField(
        min_value=1,
        label=_("Competitor privilege length"))
    competitor_privilege_format = forms.ChoiceField(
        choices=code_based_auth.models.CODE_COMPONENT_FORMATS,
        label=_("Competitor privilege format"))
    competitor_privilege_hash = forms.ChoiceField(
        initial=code_based_auth.models.DEFAULT_HASH_ALGORITHM,
        choices=code_based_auth.models.HASH_ALGORITHMS,
        label=_("Competitor privilege hash"))


class CompetitorCodeFormatForm(CodeFormatForm):
    questionset_format = forms.ChoiceField(
        choices=code_based_auth.models.CODE_COMPONENT_FORMATS,
        label=_("Questionset format"))
    questionset_hash = forms.ChoiceField(
        initial='noop',
        choices=code_based_auth.models.HASH_ALGORITHMS,
        label=_("Questionset hash"))


class AdminCodeFormatForm(CodeFormatForm):
    admin_privilege_length = forms.IntegerField(
        min_value=1, label=_("Admin privilege length"))
    admin_privilege_format = forms.ChoiceField(
        choices=code_based_auth.models.CODE_COMPONENT_FORMATS,
        label=_("Admin privilege format"))
    admin_privilege_hash = forms.ChoiceField(
        initial=code_based_auth.models.DEFAULT_HASH_ALGORITHM,
        choices=code_based_auth.models.HASH_ALGORITHMS,
        label=_("Admin privilege hash"))
    allowed_effects_length = forms.IntegerField(
        min_value=1, label=_("Allowed effects length"))
    allowed_effects_format = forms.ChoiceField(
        choices=code_based_auth.models.CODE_COMPONENT_FORMATS,
        label=_("Allowed effects format"))
    allowed_effects_hash = forms.ChoiceField(
        initial=code_based_auth.models.DEFAULT_HASH_ALGORITHM,
        choices=code_based_auth.models.HASH_ALGORITHMS,
        label=_("Allowed effects hash"))


class CompetitionQuestionSetFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(CompetitionQuestionSetFormHelper, self).__init__(*args, **kwargs)
        self.form_method = 'POST'
        self.form_tag = False
        self.disable_csrf = True
        self.form_class = "form-horizontal"
        self.label_class = 'col-lg-2'
        self.field_class = 'col-lg-10'
        self.layout = Layout(
            Fieldset(
                '&nbsp;',
                'name',
                'id',
                'questionset',
                'guest_privileges'
            )
        )


class CompetitionQuestionSetCreateForm(forms.ModelForm):
    class Meta:
        model = CompetitionQuestionSet
        exclude = ('guest_code',)

    create_guest_code = forms.BooleanField(
        required=False, label=_("Create guest code"))

    def __init__(self, *args, **kwargs):
        super(CompetitionQuestionSetCreateForm, self).__init__(*args, **kwargs)
        add_related_field_wrapper(self, 'questionset',
                                  add_related_view='questionset_add',
                                  change_related_view='questionset_change')
        self.helper = CompetitionQuestionSetFormHelper()


class CompetitionQuestionSetUpdateForm(forms.ModelForm):
    class Meta:
        model = CompetitionQuestionSet
        exclude = ('guest_code',)
    guest_privileges = forms.MultipleChoiceField(
        choices=COMPETITOR_PRIVILEGES, required=False,
        widget=forms.CheckboxSelectMultiple())

    def __init__(self, *args, **kwargs):
        super(CompetitionQuestionSetUpdateForm, self).__init__(*args, **kwargs)
        add_related_field_wrapper(self, 'questionset',
                                  add_related_view='questionset_add',
                                  change_related_view='questionset_change')
        guest_privileges = []
        try:
            generator = self.instance.competition.competitor_code_generator
            if self.instance.guest_code is not None:
                print(self.instance.guest_code.value)
                for privilege, description in COMPETITOR_PRIVILEGES:
                    if generator.code_matches(
                            self.instance.guest_code.value,
                            {'competitor_privileges': [privilege]}):
                        guest_privileges.append(privilege)
        except:
            pass
        self.fields['guest_privileges'].initial = guest_privileges
        self.helper = CompetitionQuestionSetFormHelper()

    def save(self, *args, **kwargs):
        retval = super(CompetitionQuestionSetUpdateForm, self).save(*args, **kwargs)
        self.new_code_created = False
        old_guest_privileges = set()
        generator = self.instance.competition.competitor_code_generator
        if self.instance.guest_code is not None:
            for privilege, description in COMPETITOR_PRIVILEGES:
                if generator.code_matches(
                        self.instance.guest_code.value,
                        {'competitor_privileges': [privilege]}):
                    old_guest_privileges.add(privilege)
        new_guest_privileges = set(self.cleaned_data['guest_privileges'])
        if old_guest_privileges != new_guest_privileges:
            if len(new_guest_privileges) == 0:
                self.instance.guest_code = None
            else:
                code_data = {
                    'competitor_privileges': list(new_guest_privileges),
                    'code_effects': ['new_attempt'],
                    'competition_questionset': [
                        self.instance.slug_str()]
                }
                self.new_code_created = True
                c = generator.create_code(code_data)
                print("created new code: {} -> {}".format(new_guest_privileges, c))
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


CompetitionCreateFormSet = inlineformset_factory(
    Competition,
    CompetitionQuestionSet,
    form=CompetitionQuestionSetCreateForm,
    can_delete=False)

CompetitionUpdateFormSet = inlineformset_factory(
    Competition,
    CompetitionQuestionSet,
    form=CompetitionQuestionSetUpdateForm,
    fields='__all__')


class MailForm(forms.Form):
    mail_to = forms.CharField(
        widget=forms.TextInput(attrs={'size': 71, 'style': 'margin-bottom:10px;'}),
        label=_("To"),
        required=True)
    mail_subject = forms.CharField(
        widget=forms.TextInput(attrs={'size': 71, 'style': 'margin-bottom:10px;'}),
        label=_("Subject"),
        required=True)
    mail_content = forms.CharField(label=_("Content"), required=True)
