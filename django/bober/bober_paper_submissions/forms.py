from django.forms import ModelForm, HiddenInput, Textarea
import bober_paper_submissions.models

class JuniorResultForm(ModelForm):
    class Meta:
        model = bober_paper_submissions.models.JuniorResult
        exclude = tuple()
        widgets = {
            'school_mentor': HiddenInput(),
            'drugi_razred': Textarea(attrs={'rows': 30, 'cols': 30}),
            'tretji_razred': Textarea(attrs={'rows': 30, 'cols': 30}),
            'cetrti_razred': Textarea(attrs={'rows': 30, 'cols': 30}),
            'peti_razred': Textarea(attrs={'rows': 30, 'cols': 30}),
        }
