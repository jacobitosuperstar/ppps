"""Clients related models.

Client:
    Clients to which the company generates production orders.
"""
from django.utils.translation import gettext as _
from django.db import models

from base.models import BaseModel


class Client(BaseModel):
    """Clients to which the company generates production orders.

    Parameters
    ----------
    client_id: str
        Idenfitication number of the client.
    client_name: str
        Name of the client.
    client_email: str
        Email of the client.
    """
    client_id = models.CharField()
    client_name = models.CharField()
    client_email = models.EmailField()
