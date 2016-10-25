from django.shortcuts import render
from django.template.response import SimpleTemplateResponse
from django.views.generic import CreateView, DeleteView, UpdateView, FormView
import django.forms
from django.forms.widgets import HiddenInput
import json
from django.utils import six

IS_POPUP_VAR = '_popup' 
TO_FIELD_VAR = '_to_field'

# Create your views here.

class PopupFormViewMixin():
    def _form_valid_redirect(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        if IS_POPUP_VAR in self.request.POST:
            to_field = self.request.POST.get(TO_FIELD_VAR)
            obj = form.instance
            if to_field:
                attr = str(to_field)
            else:
                attr = obj._meta.pk.attname
            value = obj.serializable_value(attr)
            popup_response_data = json.dumps({
                'value': six.text_type(value),
                # 'obj': six.text_type(obj),
            })
            return SimpleTemplateResponse('popup_modelviews/popup_response.html', {
                'popup_response_data': popup_response_data,
            })
        return None
    
    def get_form(self, form_class=None):
        """
        add the is_popup and to_field fields to form
        """
        if form_class is None:
            form_class = self.get_form_class()
        form = form_class(**self.get_form_kwargs())
        if self.request.method == 'GET':
            if TO_FIELD_VAR in self.request.GET:
                to_field = django.forms.fields.CharField(
                    widget = HiddenInput,
                    initial = self.request.GET[TO_FIELD_VAR])
                form.fields[TO_FIELD_VAR] = to_field
            if IS_POPUP_VAR in self.request.GET:
                is_popup_field = django.forms.fields.CharField(
                    widget = HiddenInput,
                    initial = self.request.GET[IS_POPUP_VAR])
                form.fields[IS_POPUP_VAR] = is_popup_field
        return form

class PopupFormView(PopupFormViewMixin, FormView):
    def form_valid(self, form):
        retval_redir = self._form_valid_redirect(form)
        retval = FormView.form_valid(self, form)
        if retval_redir is not None:
            return retval_redir
        return retval
    
class PopupCreateView(PopupFormViewMixin, CreateView):
    def form_valid(self, form):
        retval_redir = self._form_valid_redirect(form)
        retval = CreateView.form_valid(self, form)
        if retval_redir is not None:
            return retval_redir
        return retval

class PopupUpdateView(PopupFormViewMixin, UpdateView):
    def form_valid(self, form):
        retval_redir = self._form_valid_redirect(form)
        retval = UpdateView.form_valid(self, form)
        if retval_redir is not None:
            return retval_redir
        return retval

