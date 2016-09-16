from django import forms
from django.utils.translation import ugettext as _

from mce_filebrowser.models import FileBrowserFile


class FileUploadForm(forms.ModelForm):
    """ File/Image Upload form """
    class Meta:
        model = FileBrowserFile
        fields = ('uploaded_file',)
