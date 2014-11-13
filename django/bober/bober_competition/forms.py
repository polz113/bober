from django.forms import ModelForm
import bober_paper_submissions.models

class JuniorResult(ModelForm):
    class Meta:
        model = bober_paper_submissions.models.JuniorResult