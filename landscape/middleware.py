"""Landscape middleware catalog."""

# Django
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:
    """Profile completion middleware.

    Ensure every user that is interacting with the platform
    have their profile picture and biography.
    """

    def __init__(self, get_response):
        """Middleware initialization."""
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request before the view is called."""
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('users:update_profile'), reverse('users:logout')]:
                        return redirect('users:update_profile')

        response = self.get_response(request)
        return response


"""

The Middlewares have the following order:

SecurityMiddleware: It is in charge of checking all the security measures, the settings variables related to Https, Auth, among others.
SessionMiddleware: It is responsible for validating a session.
CommonMiddleware: It is responsible for verifying common components such as debugging.
CsrfViewMiddleware: It takes care of all the validation corresponding to CSRF. This allows us to use the tag {% csrf_token%} and it is the one that inserts the security token in each form.
AuthenticationMiddleware: It allows us to add request.user from the views.
MessageMiddleware: It belongs to the Django Message Framework, and allows you to pass a message without the need to maintain a state in the database or in memory.
XFrameOptionsMiddleware: Security Middleware.

"""