import django_filters as df
from bober_simple_competition.models import Profile

class ProfileFilter(df.FilterSet):
    class Meta:
        model = Profile
        fields = {
            'user__first_name':[ "icontains" ],
            'user__last_name':[ "icontains" ],
            'user__username':[ "icontains" ],
            'user__email':[ "icontains" ],
        }
