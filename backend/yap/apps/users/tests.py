from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .models import User

user_data = {
    "username": "test_user",
    "password": "super_secret_password",
}


class RegistrationTestCase(APITestCase):
    """ Test user registration """

    def setUp(self):
        self.client = APIClient()

    def test_user_registration(self):
        """
        Creates a user and verify that the response contains the access and refresh tokens.
        """
        response = self.client.post("/api/register/", data=user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("refresh", response.data)
        self.assertIn("access", response.data)


class LoginTestCase(APITestCase):
    """ Test user login """

    def setUp(self):
        self.client = APIClient()
        self.client.post("/api/register/", data=user_data, format="json")

    def _test_login(self, data, status_code, expected_params):
        """
        Tries to login with invalid password.
        """
        response = self.client.post("/api/login/", data=data, format="json")
        self.assertEqual(response.status_code, status_code)
        for param in expected_params:
            self.assertIn(param, response.data)

    def test_login_success(self):
        """
        Tries to login and verify that the response contains the access and refresh tokens.
        """
        self._test_login(
            data=user_data, status_code=status.HTTP_200_OK, expected_params=["access", "refresh"],
        )

    def test_login_wrong_username(self):
        """
        Tries to login with invalid username.
        """
        self._test_login(
            data={"username": "someting invalid", "password": user_data["password"],},
            status_code=status.HTTP_401_UNAUTHORIZED,
            expected_params=["detail"],
        )

    def test_login_wrong_password(self):
        """
        Tries to login with invalid password.
        """
        self._test_login(
            data={"password": "someting invalid", "username": user_data["username"],},
            status_code=status.HTTP_401_UNAUTHORIZED,
            expected_params=["detail"],
        )


class UserTestCase(TestCase):
    """Test user creation"""

    def test_guest_user_creation(self):
        """Tries to create a guest user"""
        user = User.objects.create_guest_user()
        self.assertTrue(user.is_guest)

    def test_non_guest_user_creation(self):
        """Tries to create a non guest user"""
        user = User.objects.create_user(**user_data)
        self.assertFalse(user.is_guest)
