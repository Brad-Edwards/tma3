from django.urls import path

app_name = "roots"
urlpatterns = [
    path("attendance/", views.attendance, name="attendance"),
    path("classrooms/", views.classroom, name="classroom"),
]
