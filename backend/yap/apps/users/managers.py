from uuid import uuid4

from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """
    Custom manager for User model.
    """

    use_in_migrations = True

    def _create_user(self, username, password, is_guest):
        """
        Creates and saves a user
        """
        user = self.model(username=username, is_guest=is_guest)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, password):
        """
        Creates and saves a non Guest User
        """
        return self._create_user(username, password, is_guest=False)

    def create_guest_user(self):
        """
        Creates and saves a Guest User.
        """
        username = str(uuid4())
        password = str(uuid4())
        return self._create_user(username, password, is_guest=True)
