from django import forms
from django.forms.models import inlineformset_factory, model_to_dict, fields_for_model
import code_based_auth.models
from django.utils.translation import ugettext as _

# TODO: none of this works.
class CodeFromGeneratorForm(forms.Form):
    def __init__(self, *args, **kwargs):
        generator = kwargs.pop('generator', None)
        if generator is None raise Exception("missing generator")
        super(CodeFromGeneratorForm, self).__init__(*args, **kwargs)
        for i in generator.variable_components(): 
            self.fields[str(i.name)] = forms.CharField()
