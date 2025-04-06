from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("flights/", views.flights, name="flights"),
    path("flights/forms/", views.create_forms, name="create-forms"),
]
