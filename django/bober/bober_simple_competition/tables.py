import django_tables2 as dt2

from django.utils.translation import ugettext_lazy as _
from bober_simple_competition.models import Profile, Question

class ProfileTable(dt2.Table):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'username', 'vcard')
        attrs = {'class': 'taskTable table table-hover'}
    first_name = dt2.Column(accessor='user.first_name', verbose_name=_("First Name"))
    last_name = dt2.Column(accessor='user.last_name', verbose_name = _("Last Name"))
    email = dt2.Column(accessor='user.email', verbose_name=_("E-Mail"))
    username = dt2.Column(accessor='user.username', verbose_name=_("Username"))
    select = dt2.CheckBoxColumn(accessor='id', verbose_name=_("vcard"))

class QuestionTable(dt2.Table):
    class Meta:
        model = Question
        fields = ('identifier', 'title', 'country', 'license', 'language')
