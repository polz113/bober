class ProfileMiddleware:
    """
    Add profile to autenticated user requests.
    It is available as profile property on request object.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not hasattr(request, 'profile') and \
                request.user.is_authenticated:
            profile = request.user.profile
            if profile.merged_with is not None:
                profile = profile.merge_to_top(limit=5)
            request.profile = profile

        response = self.get_response(request)
        return response
