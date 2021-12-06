from django.urls import path

from . import views

app_name = "roots"
urlpatterns = [
    path("attendance/", views.attendance, name="attendance"),
    path("classrooms/", views.classroom, name="classroom"),
]
