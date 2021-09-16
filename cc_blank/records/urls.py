# records/urls.py
from django.urls import path

from .views import (
    record_list, record_create, 
    record_edit, record_filter_ajax,
    record_create_form, record_delete
)

app_name = "records"

urlpatterns = [
    path("", record_list, name="record_list"),
    path("filter/", record_filter_ajax, name="record_filter_ajax"),
    path("create/", record_create, name="record_create"),
    path("create_form/", record_create_form, name="record_create_form_ajax"),
    path("edit/<int:pk>/", record_edit, name="record_edit"),
    path("delete/<int:pk>/", record_delete, name="record_delete"),
]