"""Production related models.
"""
from django.utils.translation import gettext as _
from django.db import models

from base.models import BaseModel
from products.models import Product
from clients.models import Client


class ProductionOrder(BaseModel):
    """Production order on which a certain ammount of product should be
    produced and delivered before a certain date for a client.

    Parameters
    ----------
    client: Client
        Client to which the product will be delivered.
    product: Product
        Product that is going to be produced in this particular order.
    product_ammount: int
        Ammount of Product needed to be made for this order to be fullfilled.
    notes: str
        Notes from the commercial that are needed to be taken into account for
        this production order.
    delivery_date: DateTime
        Date on which the product must be delivered to the client.
    """
    client = models.ForeignKey(
        to=Client,
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
    )
    product_ammount = models.IntegerField(
        default=0,
    )
    notes = models.TextField(
        null=True,
        blank=True,
    )
    delivery_date = models.DateField()


class QualityEvaluationProductionOrder(BaseModel):
    """Evaluation of the execution of the production order.

    After the Production Order is completed and sended to the buyer, there are
    observations that are needed to be done in case we have non conforming
    product, send an erronious ammount or some other eventuality happens that
    may compromise the initial time calculated for the production order.

    If no observations are detected, the delivery time should be the same that
    the one present in the Production Order so that the indicator is not
    affected.

    Parameters
    ----------
    production_order: ProductionOrder
        Production Order that is going to be evaluated.
    non_conforming_product_ammount: int
        Ammount of product deemed not up to standard to the client.
    notes: str
        Observations or notes made from the Quality personel, regarding the
        production.
    delivery_date: DateTime
        Date on which the Production Order was succesfully delivered.
    """
    production_order = models.ForeignKey(
        to=ProductionOrder,
        on_delete=models.CASCADE,
    )
    non_conforming_product_ammount = models.IntegerField(
        default=0,
    )
    notes = models.TextField(
        null=True,
        blank=True,
    )
    delivery_date = models.DateField()
