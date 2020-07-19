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
        self.assertTrue(len(response.data.get("refresh")) > 0)
        self.assertTrue(len(response.data.get("access")) > 0)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class AuthTestCase(APITestCase):
    """ Test user authorization """

    def setUp(self):
        self.client = APIClient()
        self.tokens = self.client.post("/api/register/", data=user_data, format="json").data
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.tokens.get("access"))

    def test_login(self):
        """
        Tries to login and verify that the response contains the access and refresh tokens.
        """
        response = self.client.post("/api/login/", data=user_data, format="json")
        self.assertTrue(len(response.data.get("refresh")) > 0)
        self.assertTrue(len(response.data.get("access")) > 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_refresh_token(self):
        """
        Tries to generate a new access token.
        """
        response = self.client.post("/api/token/refresh/", data={"refresh": self.tokens.get("refresh")}, format="json")
        self.assertTrue(len(response.data.get("access")) > 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GuestUserTestCase(TestCase):
    """Test the guest user at model level"""

    def test_guest_user_creation(self):
        """Tries to create a guest user"""
        user = User.objects.create_guest_user()
        self.assertTrue(user.is_guest)

    def test_non_guest_user_creation(self):
        """Tries to create a non guest user"""
        user = User.objects.create_user(**user_data)
        self.assertFalse(user.is_guest)
