"""Products related models

Product:
    Items created from the company that are being sold to different clients.
"""
from django.utils.translation import gettext as _
from django.db import models

from base.models import BaseModel


class Product(BaseModel):
    """Items created from the company that are being sold to different clients.

    Parameters
    ----------
    name: str
        Name of the product.
    materials: Dict
        Dictonary of materials and ammounts needed for the creation of the
        product.
    production_time: int
        Time delta on which one product is created.
    setup_time: int
        Time delta needed to prepare the machines to start the creation of the
        product.
    """
    name = models.CharField(
        blank=False,
        null=False,
        max_length=255,
    )
    materials = models.JSONField(
        blank=False,
        null=True,
    )
    production_time = models.DurationField(
        blank=False,
        null=True,
    )
    setup_time = models.DurationField(
        blank=False,
        null=True,
    )
