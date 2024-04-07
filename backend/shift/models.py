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
from machines.models import Machine
from products.models import Product
from production.models import ProductionOrder


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
    """Time dedicated to fullfill a Production Order or to check machinery
    down times for maintenance and for repairs.

    Parameters
    ----------
    employee: Employee
        Employee assigned to work on this shift.
    machine: Machine
        Machine on which the work is going to be done.
    production_order: ProductionOrder
        Production order on which the employee is going to be working on.
    produced_ammount: int
        Ammount of product produced at the end of the shift.
    shift_type: str
        Type of shift.
    start_time: DateTime
        Starting time of the shift (HH:MM:SS DD/MM/YYYY).
    end_time: DateTime
        Ending time of the shift (HH:MM:SS DD/MM/YYYY).
    """
    employee = models.ForeignKey(
        to=Employee,
        on_delete=models.SET_NULL,
        null=True,
    )
    machine = models.ForeignKey(
        to=Machine,
        on_delete=models.SET_NULL,
        null=True,
    )
    production_order = models.ForeignKey(
        to=ProductionOrder,
        on_delete=models.SET_NULL,
        null=True,
    )
    produced_ammount = models.IntegerField(
        default=0,
    )
    shift_type = models.CharField(
        max_length=20,
        choices=ShiftTypes.choices,
        blank=False,
        null=False,
    )
    start_time = models.DateTimeField(
        blank=False,
        null=True,
    )
    end_time = models.DateTimeField(
        blank=False,
        null=True,
    )

    class Meta:
        db_table = "shift"
        verbose_name = "shift"
        verbose_name_plural = "shifts"
