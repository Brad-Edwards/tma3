from django.urls import path
from django.views.generic import TemplateView

from roots import views

app_name = "roots"
urlpatterns = [
    path("check_in/", views.check_in, name="check_in"),
    path("check_in_success/", views.check_in_success, name="check_in_success"),
    path("check_out/", views.check_out, name="check_out"),
    path("check_out_success/", views.check_out_success, name="check_out_success"),
    path("landing/", TemplateView.as_view(template_name="roots/index.html"), name="index"),
    path("meal/", views.meal, name="meal"),
    path("meal_success/", views.meal_success, name="meal_success"),
    path("naps/", views.nap, name="nap"),
    path("nap_success/", views.nap_success, name="nap_success"),
    path("registration/register/", views.register, name="register"),
    path("registration/register/success/", views.register_success, name="register_success"),
    path("registration_landing/", TemplateView.as_view(template_name="roots/registration_landing.html"), name="registration_landing"),
    path("toileting/", views.toileting, name="toileting"),
    path("toileting_success/", views.toileting_success, name="toileting_success"),
]

