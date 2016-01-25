import autocomplete_light
from models import Profile, Question

class ManagedUsersAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = [
        'user__first_name', 
        'user__last_name',
        'user__email',
        'user__username',
        # TODO add the functionality below
        #'^former_profile_set__user__first_name',
        #'^former_profile_set__user__last_name',
        #'^former_profile_set__user__email_name',
        #'^former_profile_set__user__username',
    ]
    model = Profile
    attrs={
        'placeholder': '',
        'data-autocomplete-minimum-characters': 1,
    }

    def choices_for_request(self):
        try:
            self.choices = self.request.profile.managed_profiles.all()
        except Exception, e:
            # print e
            self.choices = Profile.objects.none()
        return super(ManagedUsersAutocomplete, self).choices_for_request()

autocomplete_light.register(ManagedUsersAutocomplete)
