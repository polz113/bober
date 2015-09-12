import autocomplete_light
from models import Profile, Question

class ManagedUsersAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['^user__first_name', 
        'user__last_name',
        'user__email',
        'user__username']
    model = Profile
    attrs={
        'placeholder': '',
        'data-autocomplete-minimum-characters': 1,
    }

    def choices_for_request(self):
        try:
            self.choices = self.request.user.profile.managed_profiles.all()
        except Exception, e:
            # print e
            self.choices = Profile.objects.none()
        return super(ManagedUsersAutocomplete, self).choices_for_request()

autocomplete_light.register(ManagedUsersAutocomplete)
