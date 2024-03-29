"""JWT authentication mixins.
"""
from django.utils.decorators import method_decorator
from django.views import View

from .decorators import authenticated_user

class AuthenticatedUserMixin(View):
    @classmethod
    def as_view(cls, **initkwargs):
        """We modify the creation of the view function from the View class and
        apply our function decorator to a method decorator with the
        `method_decorator` function. Then we apply it to the dispatch function
        so the decorator is executed before any request handling.
        """
        # creating the view
        view = super().as_view(**initkwargs)
        # applying the decorator to the view
        return method_decorator(decorator=authenticated_user, name='dispatch')(view)
