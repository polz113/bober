from django.forms import ModelForm, HiddenInput, Textarea
import bober_paper_submissions.models

class JuniorResult(ModelForm):
    class Meta:
        model = bober_paper_submissions.models.JuniorResult
        widgets = {
            'school_mentor': HiddenInput(),
            'id': HiddenInput(),
        }
