class ProfileMiddleware(object):
    """
    Add profile to autenticated user requests.
    It is available as profile property on request object.
    """
    def process_request(self, request):
        if not hasattr(request, 'profile') and \
                request.user.is_authenticated():
            profile = request.user.profile
            if profile.merged_with is not None:
                profile = profile.merge_to_top(limit=5)
            request.profile = profile
        return None
