import datetime

import django.forms
from django.conf import settings
from django.db import models
from django.contrib.admin import widgets as adminWidget
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateField, ForeignKey, ManyToManyField, \
    Model, TextChoices, TextField, TimeField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField

def get_time():
    return datetime.datetime.now().time()

class Child(Model):
    person = ForeignKey("roots.Person", null=True, on_delete=models.SET_NULL)
    parents = ManyToManyField("roots.Parent", blank=True)

    def __str__(self):
        return f'{self.pk}'

    def get_absolute_url(self):
        return reverse("children", kwargs={"id": self.pk})


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
    country = CharField(_("Country"), default="Canada", max_length=255)
    phone1 = PhoneNumberField(blank=True)
    phone2 = PhoneNumberField(blank=True)

    def __str__(self):
        return self.street_address

    def get_absolute_url(self):
        return reverse("contact_info", kwargs={"pk": self.pk})


class Classroom(Model):
    name = CharField(_("Class Name"), blank=False, max_length=255)
    children = ManyToManyField("roots.Child", blank=True)
    short_name = CharField(_("Abbreviation"), blank=True, max_length=10)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("classroom", kwargs={"name": self.name})


class Family(Model):
    name = CharField(_("Family Name"), blank=False, null=False, max_length=255)
    children = ManyToManyField("roots.Person", blank=True, related_name="children")
    parents = ManyToManyField("roots.Person", blank=True, related_name="parents")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("families", kwargs={"id": self.pk})


class Food(Model):
    name = CharField(_("Name"), max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("food", kwargs={'id', self.pk})


class Meal(Model):
    date = DateField(_("Date"), default=datetime.date.today)
    classrooms = ManyToManyField("roots.Classroom", blank=True)
    children = ManyToManyField("roots.Child", blank=True)
    start_time = TimeField(_("Start Time"), default=get_time, blank=False, null=False)
    end_time = TimeField(_("End Time"), default=get_time, blank=False, null=False)
    menu = ManyToManyField("roots.Menu", blank=True)
    food = ManyToManyField("roots.Food", blank=True)
    notes = TextField(_("Notes"), blank=True, null=True)


    def __str__(self):
        return f'{str(self.date)} {self.pk}'

    def get_absolute_url(self):
        return reverse("meal", kwargs={'id', self.pk})


class Menu(Model):
    name = CharField(_("Name"), blank=True, null=True, max_length=255)
    date = DateField(_("Date"), default=datetime.date.today)
    classrooms = ManyToManyField("roots.Classroom", blank=True)
    food = ManyToManyField("roots.Food", blank=True)
    notes = TextField(_("Notes"), blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("menu", kwargs={'id': self.pk})


class Nap(Model):
    date = DateField(_("Date"), blank=False, null=False, default=datetime.date.today)
    start_time = TimeField(_("Start Time"), default=get_time, blank=False, null=False)
    end_time = TimeField(_("End Time"), default=get_time, blank=False, null=False)
    children = ManyToManyField("roots.Child", blank=True)
    notes = TextField(_("Notes"), blank=True, null=True)


    def __str__(self):
        return self.pk

    def get_absolute_url(self):
        return reverse("naps", kwargs={"id": self.pk})


class Parent(Model):
    person = ForeignKey("roots.Parent", blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("parents/", kwargs={"id": self.pk})


class Person(Model):

    class Roles(TextChoices):
        CHILD = 'CHILD', _("Child")
        PARENT = 'PARENT', _("Parent")
        STAFF = 'STAFF', _("Staff")


    contact_info = ForeignKey(ContactInfo, null=True, on_delete=models.SET_NULL)
    first_name = CharField(_("First Name"), blank=False, max_length=255)
    last_name = CharField(_("Last Name"), blank=False, max_length=255)
    role = CharField(max_length=6,
                     choices=Roles.choices,
                     default=Roles.CHILD,
                     )
    user = ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse("people", kwargs={"id": self.pk})


class Registration(Model):
    child = ForeignKey("roots.Child", blank=False, null=False, on_delete=models.CASCADE)
    classroom = ForeignKey("roots.Classroom", blank=True, null=True, on_delete=models.CASCADE)
    start_date = DateField(_("Start Date"), blank=False, null=False, default=datetime.date.today)
    parents = ManyToManyField("roots.Parent", blank=True)


    def __str__(self):
        return self.pk

    def get_absolute_url(self):
        return reverse(_("registration", kwargs={"id": self.pk}))


class Toileting(Model):

    CHOICES = (("none", "None"),
               ("pee", "Pee"),
               ("poo", "Poo"))
    child = ForeignKey("roots.Child", blank=False, null=False, on_delete=models.CASCADE)
    date = DateField(_("Date"), blank=False, null=False, default=datetime.date.today)
    start_time = TimeField(_("Start Time"), default=get_time, blank=False, null=False)
    end_time = TimeField(_("End Time"), default=get_time, blank=False, null=False)
    notes = TextField(_("Notes"), blank=True, null=True)
    activity = MultiSelectField(choices=CHOICES, default="none", max_choices=2)

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("toileting", kwargs={"id": self.pk})
