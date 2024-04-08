from typing import (
    Union,
    Iterable,
    Optional,
    List,
    Dict,
)
from django.http import (
    HttpRequest,
    JsonResponse,
)
from django.utils.translation import gettext as _
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import (
    require_GET,
    require_POST,
)
from django.db.models import Q
from django.http import JsonResponse

from base.http_status_codes import HTTP_STATUS as status
from base.logger import base_logger
from base.generic_views import (
    BaseListView,
    BaseCreateView,
    BaseDetailView,
    BaseUpdateView,
    BaseDeleteView,
)
from jwt_authentication.decorators import authenticated_user
from employees.decorators import role_validation

from employees.models import RoleChoices
from employees.mixins import (
    AuthenticatedUserMixin,
    RoleValidatorMixin,
)
from .models import (
    Product,
)
from .forms import (
    ProductCreationForm,
    ProductUpdateForm,
    ProductForm,
)


class ProductListView(AuthenticatedUserMixin, BaseListView):
    """
    Class based view to handle the filtering and listing the objects.
    """
    model = Product
    form = ProductForm
    serializer_depth = 0


class ProductCreationView(RoleValidatorMixin, BaseCreateView):
    """
    Class to chandle the creation of the Product model objects.
    """
    allowed_roles = [
        RoleChoices.PRODUCTION_MANAGER,
        RoleChoices.MANAGEMENT,
    ]
    model = Product
    form = ProductCreationForm
    serializer_depth = 0

class ProductDetailView(AuthenticatedUserMixin, BaseDetailView):
    model = Product
    serializer_depth = 0
    url_kwarg: str = "id"

class ProductUpdateDeleteView(
    RoleValidatorMixin,
    BaseUpdateView,
    BaseDeleteView,
):
    """
    Class to handle the deatiled view, the update and the delete of the Product
    model object.
    """
    allowed_roles = [
        RoleChoices.PRODUCTION_MANAGER,
        RoleChoices.MANAGEMENT,
    ]
    model = Product
    form = ProductUpdateForm
    serializer_depth = 0
    url_kwarg: str = "id"
