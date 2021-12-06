import datetime
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateField, ForeignKey, ManyToManyField, Model, TextChoices
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

from comp482_tma3.users.models import User

class Classroom(Model):
    name = CharField(_("Class Name"), blank=False, max_length=255)
    children = ManyToManyField(User, blank=True, limit_choices_to={'role': User.UserRoles.CHILD})
    short_name = CharField(_("Abbreviation"), blank=True, max_length=10)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("classroom", kwargs={"name": self.name})


class Attendance(Model):
    date = DateField(_("Date"), default=datetime.date.today)
    children = ManyToManyField(User, blank=True)
    classroom = ForeignKey(Classroom, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.date) + self.classroom.name

    def get_absolute_url(self):
        return reverse("attendance", kwargs={"pk": self.pk})


class ContactInfo(Model):

    class Provinces(TextChoices):
        AB = 'AB', _("AB")
        BC = 'BC', _("BC")
        MB = 'MB', _("MB")
        NB = "NB", _("NB")
        NL = "NL", _("NL")
        NS = "NS", _("NS")
        NT = "NT", _("NT")
        NU = "NU", _("NU")
        ON = "ON", _("ON")
        PE = "PE", _("PE")
        QC = "QC", _("QC")
        SK = "SK", _("SK")
        YT = "YT", _("YT")


    street_address = CharField(_("Address"), max_length=255)
    city = CharField(_("City"), max_length=255)
    postal_code = CharField(_("Postal Code"), max_length=255)
    province = CharField(max_length=2,
                         choices=Provinces.choices,
                         default=Provinces.BC)
    country = CharField(_("Country"), max_length=255)
    phone1 = PhoneNumberField(blank=True)
    phone2 = PhoneNumberField(blank=True)

    def __str__(self):
        return self.street_address

    def get_absolute_url(self):
        return reverse("contact_info", kwargs={"pk": self.pk})


class Menu(Model):
    date = DateField(_("Date"), default=datetime.date.today)
    classrooms = ManyToManyField(Classroom, blank=True)

    def __str__(self):
        return self.pk

    def get_absolute_url(self):
        return reverse("menu", kwargs={'pk': self.pk})


class Food(Model):
    name = CharField(_("Name"), max_length=255)
    menus = ManyToManyField(Menu, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("food", kwargs={'pk', self.pk})
