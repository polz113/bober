import copy
import django.forms as forms
from django.contrib.admin.options import IS_POPUP_VAR, TO_FIELD_VAR
from django.db.models.deletion import CASCADE
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.urls import reverse


class RelatedFieldWidgetWrapper(forms.Widget):
    """
    This class is a wrapper to a given widget to add the add, edit and delete
    icons.
    """
    template = 'popup_modelviews/related_widget_wrapper.html'

    def __init__(self, widget, rel, current_app=None, current_site=None,
                 add_related_view=None,
                 change_related_view=None,
                 delete_related_view=None
                 ):
        self.needs_multipart_form = widget.needs_multipart_form
        self.attrs = widget.attrs
        self.choices = widget.choices
        self.widget = widget
        self.rel = rel
        self.current_app = current_app
        self.current_site = current_site
        # Backwards compatible check for whether a user can add related
        # objects.
        self.add_related_view = add_related_view
        self.change_related_view = change_related_view
        self.delete_related_view = delete_related_view
        # XXX: The UX does not support multiple selected values.
        multiple = getattr(widget, 'allow_multiple_selected', False)
        if multiple:
            self.change_related_view = None
        # XXX: The deletion UX can be confusing when dealing with cascading deletion.
        cascade = getattr(rel, 'on_delete', None) is CASCADE
        if multiple or cascade:
            self.delete_related_view = None
        # so we can check if the related object is registered with this AdminSite

    def __deepcopy__(self, memo):
        obj = copy.copy(self)
        obj.widget = copy.deepcopy(self.widget, memo)
        obj.attrs = self.widget.attrs
        memo[id(self)] = obj
        return obj

    @property
    def is_hidden(self):
        return self.widget.is_hidden

    @property
    def media(self):
        return self.widget.media

    def render(self, name, value, *args, **kwargs):
        rel_opts = self.rel.related_model._meta
        self.widget.choices = self.choices
        url_params = '&'.join("%s=%s" % param for param in [
            (TO_FIELD_VAR, self.rel.remote_field.name),
            (IS_POPUP_VAR, 1),
        ])
        context = {
            'widget': self.widget.render(name, value, *args, **kwargs),
            'name': name,
            'url_params': url_params,
            'model': rel_opts.verbose_name,
        }
        if self.change_related_view:
            change_related_template_url = reverse(self.change_related_view,
                                                  args=['__fk__'])
            context.update(
                can_change_related=True,
                change_related_template_url=change_related_template_url,
            )
        if self.add_related_view:
            add_related_url = reverse(self.add_related_view)
            context.update(
                can_add_related=True,
                add_related_url=add_related_url,
            )
        if self.delete_related_view:
            delete_related_template_url = reverse(self.delete_related_view,
                                                  args=['__fk__'])
            context.update(
                can_delete_related=True,
                delete_related_template_url=delete_related_template_url,
            )
        return mark_safe(render_to_string(self.template, context))

    def build_attrs(self, extra_attrs=None, **kwargs):
        "Helper function for building an attribute dictionary."
        self.attrs = self.widget.build_attrs(extra_attrs=None, **kwargs)
        return self.attrs

    def value_from_datadict(self, data, files, name):
        return self.widget.value_from_datadict(data, files, name)

    def id_for_label(self, id_):
        return self.widget.id_for_label(id_)


def add_related_field_wrapper(form, col_name,
                              add_related_view=None,
                              change_related_view=None,
                              delete_related_view=None):
    rel_model = form.Meta.model
    rel = rel_model._meta.get_field(col_name)
    form.fields[col_name].widget = RelatedFieldWidgetWrapper(
        form.fields[col_name].widget, rel,
        add_related_view=add_related_view,
        change_related_view=change_related_view,
        delete_related_view=delete_related_view)
