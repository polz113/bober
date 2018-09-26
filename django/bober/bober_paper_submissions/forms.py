from django.forms import ModelForm, HiddenInput, Textarea
from bober_paper_submissions.models import JuniorYear, JuniorMentorship, parse_competitor_data
from extra_views import InlineFormSet


class JuniorYearForm(ModelForm):
    class Meta:
        model = JuniorYear
        widgets = {
            'questionset': HiddenInput(),
            'access_code': HiddenInput(),
            'raw_data': Textarea(attrs={'rows': 20, 'cols': 20})
        }
        labels = {
            'raw_data': ''
        }
        fields = ['raw_data', 'questionset', 'access_code']

    def clean(self):
        retval = super(JuniorYearForm, self).clean()
        self.competitor_data = parse_competitor_data(
            self.cleaned_data['raw_data'])
        return retval

    def save(self, *args, **kwargs):
        instance = super(JuniorYearForm, self).save(*args, **kwargs)
        return instance


class JuniorMentorshipForm(ModelForm):
    class Meta:
        model = JuniorMentorship
        fields = ()


class JuniorYearInline(InlineFormSet):
    model = JuniorYear
    form_class = JuniorYearForm
    factory_kwargs = {'extra': 0, 'can_delete': False}
    fields = ['raw_data', 'questionset', 'access_code']
