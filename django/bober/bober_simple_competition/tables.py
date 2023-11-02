import django_tables2 as dt2
from django_tables2.utils import A
from django.utils.translation import gettext_lazy as _
from bober_simple_competition.models import Profile, Question


class ProfileTable(dt2.Table):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'username', 'vcard')
        attrs = {'class': 'taskTable table table-hover'}
    first_name = dt2.Column(accessor='user.first_name',
                            verbose_name=_("First Name"))
    last_name = dt2.Column(accessor='user.last_name',
                           verbose_name=_("Last Name"))
    username = dt2.LinkColumn("profile_detail",
                              args=[A('pk')],
                              verbose_name=_("username"), )
    email = dt2.Column(accessor='user.email', verbose_name=_("E-Mail"))
    select = dt2.CheckBoxColumn(accessor='id', verbose_name=_("vcard"))


class QuestionTable(dt2.Table):
    class Meta:
        model = Question
        fields = ('identifier', 'title', 'country', 'license', 'language')
