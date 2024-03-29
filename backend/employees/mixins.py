"""JWT role validation mixins.
"""
from django.utils.decorators import method_decorator
from django.views import View

from jwt_authentication.decorators import authenticated_user
from .decorators import role_validation

class RoleValidatorMixin(View):
    @classmethod
    def as_view(cls, allowed_roles, **initkwargs):
        """We modify the creation of the view function from the View class and
        apply our function decorator to a method decorator with the
        `method_decorator` function. Then we apply it to the dispatch function
        so the decorator is executed before any request handling.
        """
        view = super().as_view(**initkwargs)
        # Apply authentication first
        view = method_decorator(authenticated_user, name='dispatch')(view)
        # Apply role validation after
        view = method_decorator(role_validation(allowed_roles), name='dispatch')(view)
        return view
