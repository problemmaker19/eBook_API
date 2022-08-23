from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    is_teacher = models.BooleanField(
        _("teacher status"),
        default=False,
        help_text=_("Designates which fields the user can add/change/delete"),
    )

    def __str__(self):
        return f"{self.username}"
