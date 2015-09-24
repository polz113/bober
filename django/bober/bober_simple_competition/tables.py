import django_tables2 as dt2

from bober_simple_competition.models import Profile

class ProfileTable(dt2.Table):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'username', 'vcard')
        attrs = {"class": "paleblue"}
    first_name = dt2.Column(accessor='user.first_name')
    last_name = dt2.Column(accessor='user.last_name')
    email = dt2.Column(accessor='user.email')
    username = dt2.Column(accessor='user.username')
    select = dt2.CheckBoxColumn(accessor='id')
