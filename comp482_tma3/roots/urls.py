from django.urls import path

from . import views

app_name = "roots"
urlpatterns = [
    path("children/", views.children, name="children"),
    path("classrooms/", views.classroom, name="classroom"),
    path("contact_info/", views.contact_info, name="contact_info"),
    path("foods/", views.food, name="food"),
    path("menus/", views.menu, name="menu"),
    path("naps/", views.nap, name="nap"),
    path("parents/", views.parents, name="parents"),
    path("people/", views.people, name="people"),
    path("registration/", views.registration, name="registration"),
    path("toileting/", views.toileting, name="toileting")
]
