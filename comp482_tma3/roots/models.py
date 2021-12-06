import datetime
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

import comp482_tma3

class Attendance(models.Model):
    date = models.DateField(_("Date"), default=datetime.date.today)
    children = models.ManyToManyField(User)
    classroom = models.ForeignKey(Class, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.date) + classroom.name

    def get_absolute_url(self):
        return reverse("attendance", kwargs={"pk": self.pk})


class Class(models.Model):
    name = CharField(_("Class Name"), blank=False, max_length=255)
    children = models.ManyToManyField(User)
    short_name = CharField(_("Abbreviation"), blank=True, max_length=10)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("classroom", kwargs={"name": self.name})

