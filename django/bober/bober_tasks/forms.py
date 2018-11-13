from bober_tasks.models import Task, AgeGroup, Category, DifficultyLevel, \
    TaskTranslation, Answer, Remark
from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from extra_views import InlineFormSet
from django.contrib.flatpages.models import FlatPage


class FlatPageForm(forms.ModelForm):
    content = forms.CharField(widget=forms.TextInput(
        attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = FlatPage
        fields = '__all__'


class profileForm(forms.Form):
    first_name = forms.CharField(required=False, label=_("First name"))
    last_name = forms.CharField(required=False, label=_("Last name"))
    email = forms.CharField(label=_("Email"))
    password = forms.CharField(widget=forms.PasswordInput,
                               required=False, label=_("Password"))
    confirm_password = forms.CharField(widget=forms.PasswordInput,
                                       required=False,
                                       label=_("Confirm password"))


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['international_id', 'country', 'author']
        labels = {
            'international_id': _('international_id'),
            'country': _('country'),
            'author': _('author')}

    language_locale = forms.ChoiceField(
        choices=settings.LANGUAGES,
        required=True,
        label=_('The language for the first version of the task'))


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


class TaskTranslationForm(forms.ModelForm):
    class Meta:
        model = TaskTranslation
        fields = ['title', 'template', 'body', 'solution',
                  'it_is_informatics', 'comment']
        labels = {
            'title': _('Title'),
            'template': _('Template'),
            'body': _('Body'),
            'solution': _('Solution'),
            'it_is_informatics': _('it_is_informatics'),
            'comment': _('Comment'),
        }
        widgets = {
            'comment': forms.TextInput(
                attrs={'class': 'tinymce', 'cols': 45, 'rows': 25}),
            'body': forms.TextInput(
                attrs={'class': 'tinymce', 'cols': 45, 'rows': 25}),
            'it_is_informatics': forms.TextInput(
                attrs={'class': 'tinymce', 'cols': 45, 'rows': 25}),
            'solution': forms.TextInput(
                attrs={'class': 'tinymce', 'cols': 45, 'rows': 25}),
        }


class InlineAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['label', 'correct', 'value']
        labels = {
            'label': _('label'),
            'correct': _('correct'),
            'value': _('value'),
        }
        widgets = {'value': forms.TextInput(
            attrs={'class': 'tinymce', 'cols': 100, 'rows': 25})}

    correct = forms.BooleanField(label=_('correct'),
                                 initial=True, required=False)


class AnswerInline(InlineFormSet):
    model = Answer
    form_class = InlineAnswerForm
    factory_kwargs = {
        'can_delete': False,
        'extra': 0
    }


class InlineRemarkForm(forms.ModelForm):
    class Meta:
        model = Remark
        fields = ["comment"]
        labels = {'comment': _('comment')}
        widgets = {'comment': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        retval = super(InlineRemarkForm, self).__init__(*args, **kwargs)
        # TODO: init should always return None??
        return retval

    def save(self, *args, **kwargs):
        self._fields.append('user')
        self.cleaned_data['user'] = self.user
        self.cleaned_data['user_id'] = self.user.id
        return super(InlineRemarkForm, self).save(*args, **kwargs)


class RemarkInline(InlineFormSet):
    model = Remark
    form_class = InlineRemarkForm
    factory_kwargs = {
        "can_delete": False,
        "extra": 1
    }
