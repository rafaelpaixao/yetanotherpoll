from uuid import uuid4

from django.contrib.auth.models import UserManager as DjangoUserManager


class UserManager(DjangoUserManager):
    """
    Custom manager for User model.
    """

    def create_guest_user(self):
        """
        Creates and saves a Guest User.
        """
        username = str(uuid4())
        password = str(uuid4())
        return self._create_user(username=username, email=None, password=password, is_guest=True)
