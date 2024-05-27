"""Base Mixins for the project.
"""
from typing import (
    Dict,
    List,
    Union,
    Any,
)
from django.db.models.query import QuerySet
from django.utils.translation import gettext as _
from django.http import HttpRequest, JsonResponse
from django.forms import ModelForm, Form
from django.db.models import Q
from django.core.exceptions import (
    ValidationError,
    ObjectDoesNotExist,
    MultipleObjectsReturned,
)

from .logger import base_logger
from .models import BaseModel
from .http_status_codes import HTTP_STATUS as status


class BaseMixin:
    model: BaseModel
    form: Union[ModelForm, Form, None] = None
    serializer_depth: int = 0

    def serialize(
        self,
        objects: Union[QuerySet, BaseModel],
    ) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        """
        Serializer of the different objects that we are working with. If its a
        `Queryset` what is passed, a list of each element serialized will be
        returned. If is a `BaseModel` type object, just the serialized item
        will be returned.
        """
        if isinstance(objects, QuerySet):
            serialized_objects = [element.serializer(depth=self.serializer_depth) for element in objects]
        elif isinstance(objects, BaseModel):
            serialized_objects = objects.serializer(depth=self.serializer_depth)
        else:
            raise NotImplementedError("The `Type` that you are passing won't be processed.")
        return serialized_objects

    def validate_form(
        self,
        request: HttpRequest,
    ) -> Dict[str, Any]:
        """
        Validating the information passed in the request. If the form is valid
        we will return the return the cleaned values from the form. Else we
        will return a JsonResponse with the errors on the information given.
        """
        if not self.form:
            msg = (
                f"{request.path_info}, "
                "There is no form to evaluate."
            )
            base_logger.critical(msg)
            raise NotImplementedError(msg)

        request_values = {}

        if request.method == "GET":
            request_values = request.GET
        elif request.method == "POST":
            request_values = request.POST

        form: Union[ModelForm, Form] = self.form(request_values)

        if not form.is_valid():
            msg = {
                "response": _("Error in the information given"),
                "errors": form.errors.as_json(),
            }
            raise ValidationError(msg)

        cleaned_data = {}
        for key in request_values.keys():
            # checking for each value of the request Dict, the values that
            # come out of the form.
            form_data = form.cleaned_data.get(key)
            if form_data:
                # if the form data exists we create the entry in the dict
                cleaned_data[key] = form_data
        return cleaned_data

    def filter_query(
        self,
        data: Dict[str, Any],
    ) -> QuerySet:
        """Dinamically created filtering query given the data.
        """
        query = Q()

        # TODO: check how are we going to list the elements that are deleted.
        # if "is_deleted" not in data:
        #     data["is_deleted"] = False

        for key, value in data.items():
            query &= Q(**{key:value})

        queryset: QuerySet = self.model.objects.filter(query)

        # TODO: Add prefetch and select related to optimice the database calls
        # for when the depth of the serializer is greater than 0.

        return queryset

    def get_query(
        self,
        data: Dict[str, Any]
    ) -> BaseModel:
        """Dinamically created get query, given the data.
        """
        query = Q()

        for key, value in data.items():
            query &= Q(**{key:value})

        try:
            db_object: BaseModel = self.model.objects.get(query)
            return db_object
        except self.model.MultipleObjectsReturned as e:
            msg = {
                "response": _(f"Multiple entries of type {self.model._meta.verbose_name} found.")
            }
            raise MultipleObjectsReturned(msg)
        except self.model.DoesNotExist as e:
            msg = {
                "response": _(f"{self.model._meta.verbose_name} not found.")
            }
            raise ObjectDoesNotExist(msg)
        except Exception as e:
            msg = {
                "response": _("Internal server error.")
            }
            base_logger.critical(e)
            raise Exception(msg)

    def create_object(self, data: Dict) -> BaseModel:
        """Creates a model object with the given cleaned data.
        """
        try:
            model_object: BaseModel = self.model()

            for key, value in data.items():
                setattr(model_object, key, value)

            model_object.full_clean()
            model_object.save()
            return model_object
        except Exception as e:
            # Handle validation or database constraint errors
            msg = {
                "response": _(f"Error creating object {self.model._meta.verbose_name}")
            }
            base_logger.critical(e)
            raise Exception(msg)

    def update_object(self, data: Dict, db_object: BaseModel) -> BaseModel:
        """Updates a model object with the given cleaned data.
        """
        try:
            changed = False

            for key, value in data.items():
                if value is not None and hasattr(db_object, key):
                    model_object_value = getattr(db_object, key)
                    if model_object_value != value:
                        setattr(db_object, key, value)
                        changed = True

            if changed is True:
                db_object.full_clean()
                db_object.save()
            return db_object
        except Exception as e:
            # Handle validation or database constraint errors
            msg = {
                "response": _(f"Error updating object {self.model._meta.verbose_name}")
            }
            base_logger.critical(e)
            raise Exception(msg)

    def delete_object(self, db_object: BaseModel):
        """Updates a model object with the given cleaned data.
        """
        try:
            db_object.is_deleted = True
            db_object.save()
        except Exception as e:
            # Handle validation or database constraint errors
            msg = {
                "response": _(f"Error deleting object {self.model._meta.verbose_name}")
            }
            base_logger.critical(e)
            raise Exception(msg)
