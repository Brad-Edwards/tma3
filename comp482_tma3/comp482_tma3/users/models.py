from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    class UserRoles(models.TextChoices):
        CHILD = 'CHILD', _("Child")
        PARENT = 'PARENT', _("Parent")
        STAFF = 'STAFF', _("Staff")

    """Default user for COMP482 TMA3."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    role = CharField(max_length=6,
                     choices=UserRoles.choices,
                     default=UserRoles.child,
                     )


    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
