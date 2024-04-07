"""Products endpoints.
"""
from django.urls import path
from employees.models import RoleChoices
from .views import (
    ProductListView,
    ProductCreationView,
    ProductDetailUpdateDeleteView,
)


urlpatterns = [
    path(
        "",
        ProductListView.as_view(),
        name="list_products"
    ),
    path(
        "create_product/",
        ProductCreationView.as_view(),
        name="create_product"
    ),
    path(
        "<int:id>/",
        ProductDetailUpdateDeleteView.as_view(),
        name="detailed_product"
    ),
    path(
        "<int:id>/update_product/",
        ProductDetailUpdateDeleteView.as_view(),
        name="update_product"
    ),
    path(
        "<int:id>/delete_product/",
        ProductDetailUpdateDeleteView.as_view(),
        name="delete_product"
    ),
]
