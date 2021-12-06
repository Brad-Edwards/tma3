import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateField, ForeignKey, ManyToManyField, Model
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from comp482_tma3.users.models import User

class Classroom(Model):
    name = CharField(_("Class Name"), blank=False, max_length=255)
    children = ManyToManyField(User, blank=True, limit_choices_to={'role': "Child"})
    short_name = CharField(_("Abbreviation"), blank=True, max_length=10)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("classroom", kwargs={"name": self.name})


class Attendance(Model):
    date = DateField(_("Date"), default=datetime.date.today)
    children = ManyToManyField(User)
    classroom = ForeignKey(Classroom, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.date) + classroom.name

    def get_absolute_url(self):
        return reverse("attendance", kwargs={"pk": self.pk})




