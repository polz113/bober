class ProfileMiddleware(object):
    def process_request(self, request): 
        if not hasattr(request, 'profile') and \
                request.user.is_authenticated():
            profile = request.user.profile
            while profile.merged_with is not None:
                profile = profile.merged_with
            print "profile set to:", profile
            request.session['profile'] = profile.pk
            request.profile = profile
        # Code to be executed for each request/response after
        # the view is called.

        return None
