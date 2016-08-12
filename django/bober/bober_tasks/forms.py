from bober_tasks.models import *
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from extra_views import InlineFormSet
#from django import forms
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE

class FlatPageForm(forms.ModelForm):

    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    

    class Meta:
        model = FlatPage

class profileForm(forms.Form):
    first_name = forms.CharField(required=False, label=_("First name"))
    last_name = forms.CharField(required=False, label=_("Last name"))
    email = forms.CharField(label=_("Email"))
    password = forms.CharField(widget=forms.PasswordInput, required=False, label=_("Password"))
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=False, label=_("Confirm password"))

class TaskForm(forms.ModelForm):
    class Meta:
        #model= Post
        model = Task
        #fields= ['ulke kod','ulke', 'yazar']
        fields = ['international_id', 'country', 'author']
        labels={
            #'international_id': ('aa'),
            'international_id': _('international_id'),
            'country': _('country'),
            'author': _('author')}

    language_locale = forms.ChoiceField(choices=settings.LANGUAGES,
        required = True,
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
            'it_is_informatics', 'comment'
            ]
        labels={
            'title': _('Title'),
            'template': _('Template'),
            'body': _('Body'),
            'solution': _('Solution'),
            'it_is_informatics': _('it_is_informatics'),
            'comment': _('Comment'),
            }

        widgets = {
            'comment': forms.Textarea(),
            'body': forms.Textarea(),
            'it_is_informatics': forms.Textarea(),
            'solution': forms.Textarea(),
        }

class InlineAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['label', 'correct', 'value']
        labels={
        'label': _('label'),
        'correct': _('correct'),
        'value': _('value'),
        }
        widgets = {'value': forms.Textarea()}

    correct = forms.BooleanField(label=_('correct'), initial=True, required=False)

class AnswerInline(InlineFormSet):
    model = Answer
    form_class = InlineAnswerForm
    can_delete = False
    extra = 0

class InlineRemarkForm(forms.ModelForm):
    class Meta:
        model = Remark
        fields = ["comment"]
        labels={'comment': _('comment')}
        widgets = {'comment': forms.TextInput()}
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        retval = super(InlineRemarkForm, self).__init__(*args, **kwargs)
        return retval
    def save(self, *args, **kwargs):
        self._fields.append('user')
        self.cleaned_data['user'] = self.user
        self.cleaned_data['user_id'] = self.user.id
        return super(InlineRemarkForm, self).save(*args, **kwargs)

class RemarkInline(InlineFormSet):
    model = Remark
    form_class = InlineRemarkForm
    can_delete = False
    extra = 1
