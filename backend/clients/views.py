from typing import Union, Iterable, Optional
import secrets
import json
from django.http import (
    HttpRequest,
    JsonResponse,
    StreamingHttpResponse,
)
from django.utils.translation import gettext as _
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import (
    require_GET,
    require_POST,
)
from django.db.models import Q
from django.contrib.auth import authenticate
from django.http import JsonResponse
from base.http_status_codes import HTTP_STATUS as status
from base.logger import base_logger

from jwt_authentication.decorators import authenticated_user

from .models import (
    Client,
)
from .forms import (
    ClientCreationForm,
    ClientForm,
)
from .decorators import (
    role_validation,
)



