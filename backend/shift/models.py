"""
Shift related models
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
from employees.models import Employee
from products.models import ProductionOrder


class ShiftTypes(models.TextChoices):
    """TextChoices class to store the different types of shifts that can occur
    at the factory, where are defined both the value on the database and the
    human redable label.

    Example
    -------
    >>> maintenance = MachineType.objects.get(id=id)
    >>> print(machine.machine_type)
    """
    MAINTENANCE = "maintenance", _("maintenance")
    REPAIR = "repair", _("repair")
    PRODUCTION = "production", _("production")


ShiftTypes_dict = {value: label for value, label in ShiftTypes.choices}


class Shift(BaseModel):
    """
    """
    employee = models.ForeignKey(
        to=Employee,
        on_delete=models.SET_NULL,
    )
    production_order = models.ForeignKey(
        to=ProductionOrder,
        on_delete=models.SET_NULL,
    )
    produced_ammount = models.IntegerField(
    )
    shift_type = models.CharField(
        max_length=20,
        choices=ShiftTypes.choices,
        blank=False,
        null=False,
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
