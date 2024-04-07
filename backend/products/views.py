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


# @require_GET
# @authenticated_user
# @role_validation(allowed_roles=[
#     RoleChoices.MANAGEMENT,
#     RoleChoices.PRODUCTION_MANAGER,
# ])
# def get_products_view(request: HttpRequest) -> JsonResponse:
#
#     form = ProductForm(request.GET)
#     ...


class ProductListView(BaseListView):
    """
    Class based view to handle the filtering and listing the objects.
    """
    model = Product
    form = ProductForm
    serializer_depth = 0


class ProductCreationView(BaseCreateView):
    """
    Class to chandle the creation of the Product model objects.
    """
    model = Product
    form = ProductCreationForm
    serializer_depth = 0


class ProductDetailUpdateDeleteView(
    BaseDetailView,
    BaseUpdateView,
    BaseDeleteView
):
    """
    Class to handle the deatiled view, the update and the delete of the Product
    model object.
    """
    model = Product
    form = ProductUpdateForm
    serializer_depth = 0
    url_kwarg: str = "id"
