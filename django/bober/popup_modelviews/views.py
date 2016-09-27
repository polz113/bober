from django.shortcuts import render
from django.views.generic import FormView

IS_POPUP_VAR = '_popup' 
TO_FIELD_VAR = '_to_field'

# Create your views here.

class PopupFormView(FormView):
    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        if IS_POPUP_VAR in request.POST:
            to_field = request.POST.get(TO_FIELD_VAR)
            if to_field:
                attr = str(to_field)
            else:
                attr = obj._meta.pk.attname
            value = obj.serializable_value(attr)
            popup_response_data = json.dumps({
                'value': six.text_type(value),
                'obj': six.text_type(obj),
            })
            return SimpleTemplateResponse('popup_modelviews/popup_response.html', {
                'popup_response_data': popup_response_data,
            })
        return HttpResponseRedirect(self.get_success_url())
