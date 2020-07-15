from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager


class User(AbstractUser):
    """
    Custom user model
    """

    objects = UserManager()

    is_guest = models.BooleanField(
        default=False, help_text="Guest users can author Polls and vote on public polls prior to registration.",
    )
