"""
Product related models
"""
from typing import (
    Any,
    Optional,
    Dict,
    List,
)
from django.utils.translation import gettext as _
from django.db import models
from django.db.models import Q

from base.models import BaseModel


class Product(BaseModel):
    """
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
    production_time = models.TimeField(
        blank=False,
        null=True,
    )


class ProductionOrder(BaseModel):
    """
    """
    client_id = ...
    product = ...
    product_ammount = ...
    delivery_date = ...
