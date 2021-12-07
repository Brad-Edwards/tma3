from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, ForeignKey, TextChoices
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    """Default user for COMP482 TMA3."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Username"), blank=True, max_length=255)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"name": self.name})
