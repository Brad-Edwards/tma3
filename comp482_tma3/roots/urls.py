from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "roots"
urlpatterns = [
    path("check_in/", views.check_in, name="check_in"),
    path("check_in_success/", views.check_in_success, name="check_in_success"),
    path("check_out/", views.check_out, name="check_out"),
    path("check_out_success/", views.check_out_success, name="check_out_success"),
    path("children/", views.children, name="children"),
    path("classrooms/", views.classroom, name="classroom"),
    path("contact_info/", views.contact_info, name="contact_info"),
    path("families/", views.families, name="families"),
    path("foods/", views.food, name="food"),
    path("landing/", TemplateView.as_view(template_name="roots/index.html"), name="index"),
    path("menus/", views.menu, name="menu"),
    path("naps/", views.nap, name="nap"),
    path("nap_success/", views.nap_success, name="nap_success"),
    path("parents/", views.parents, name="parents"),
    path("people/", views.people, name="people"),
    path("registration/", views.registration, name="registration"),
    path("registration/register/", views.register, name="register"),
    path("registration/register/success/", views.register_success, name="register_success"),
    path("registration_landing/", TemplateView.as_view(template_name="roots/registration_landing.html"), name="registration_landing"),
    path("toileting/", views.toileting, name="toileting"),
    path("toileting_success/", views.toileting_success, name="toileting_success"),
]

