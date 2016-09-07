import autocomplete_light.shortcuts as autocomplete_light
from models import School

class SchoolAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = [
        'name',
        'address',
        'post',
        # TODO add the functionality below
        #'^former_profile_set__user__first_name',
        #'^former_profile_set__user__last_name',
        #'^former_profile_set__user__email_name',
        #'^former_profile_set__user__username',
        # something for filtering on competition mentorship
    ]
    model = School
    attrs={
        'placeholder': '',
        'data-autocomplete-minimum-characters': 1,
    }

autocomplete_light.register(SchoolAutocomplete)
