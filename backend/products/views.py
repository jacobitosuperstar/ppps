from django.utils.translation import gettext as _
from base.generic_views import (
    BaseListView,
    BaseCreateView,
    BaseDetailView,
    BaseUpdateView,
    BaseDeleteView,
)

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
    View Class based view to handle the filtering and listing the objects.
    """
    model = Product
    form = ProductForm
    serializer_depth = 0


class ProductCreationView(RoleValidatorMixin, BaseCreateView):
    """
    View Class to chandle the creation of the Product model objects.
    """
    allowed_roles = [
        RoleChoices.PRODUCTION_MANAGER,
        RoleChoices.MANAGEMENT,
    ]
    model = Product
    form = ProductCreationForm
    serializer_depth = 0


class ProductDetailView(AuthenticatedUserMixin, BaseDetailView):
    """
    View Class to handle the Detailed Product View.
    """
    model = Product
    serializer_depth = 0
    url_kwarg: str = "id"


class ProductUpdateDeleteView(
    RoleValidatorMixin,
    BaseUpdateView,
    BaseDeleteView,
):
    """
    View Class to handle the deatiled view, the update and the delete of the
    Product model object.
    """
    allowed_roles = [
        RoleChoices.PRODUCTION_MANAGER,
        RoleChoices.MANAGEMENT,
    ]
    model = Product
    form = ProductUpdateForm
    serializer_depth = 0
    url_kwarg: str = "id"
