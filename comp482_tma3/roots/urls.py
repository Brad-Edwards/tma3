from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "roots"
urlpatterns = [
    path("children/", views.children, name="children"),
    path("classrooms/", views.classroom, name="classroom"),
    path("contact_info/", views.contact_info, name="contact_info"),
    path("families/", views.families, name="families"),
    path("foods/", views.food, name="food"),
    path("landing/", TemplateView.as_view(template_name="roots/index.html"), name="index"),
    path("menus/", views.menu, name="menu"),
    path("naps/", views.nap, name="nap"),
    path("parents/", views.parents, name="parents"),
    path("people/", views.people, name="people"),
    path("registration/", views.registration, name="registration"),
    path("registration/register/", views.RegisterCreateView.as_view(template_name="roots/register_form.html"), name="register"),
    path("registration_landing/", TemplateView.as_view(template_name="roots/registration_landing.html"), name="registration_landing"),
    path("toileting/", views.toileting, name="toileting")
]

