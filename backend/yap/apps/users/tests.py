from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from yap.apps.users.models import User
from yap.apps.users.serializers import TokenSerializer

USER_DATA = {
    "username": "test_user",
    "password": "super_secret_password",
}


class UserSetUp:
    """ Creates an user and set authorization header for api client """

    def setUp(self):
        self.user = User.objects.create_user(**USER_DATA)
        tokens = TokenSerializer().get_token(self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + str(tokens.access_token))


class GuestUserSetUp:
    """ Creates an guest user and set authorization header for api client """

    def setUp(self):
        self.guest = User.objects.create_guest_user()
        tokens = TokenSerializer().get_token(self.guest)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + str(tokens.access_token))


class UserModelTestCase(TestCase):
    """Test user creation"""

    def test_guest_user_creation(self):
        """Tries to create a guest user"""
        user = User.objects.create_guest_user()
        self.assertTrue(user.is_guest)

    def test_non_guest_user_creation(self):
        """Tries to create a non guest user"""
        user = User.objects.create_user(**USER_DATA)
        self.assertFalse(user.is_guest)


class GuestRegistrationTestCase(GuestUserSetUp, APITestCase):
    """ Test guest user registration """

    def test_guest_registration(self):
        """
        Creates a user and verify that the response contains the access and refresh tokens.
        """
        response = self.client.post("/api/register_guest/", data=USER_DATA, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("refresh", response.data)
        self.assertIn("access", response.data)
        # Verify that the registered user has the same PK as the guest user
        self.assertEqual(User.objects.get(username=USER_DATA["username"]).pk, self.guest.pk)


class LoginTestCase(UserSetUp, APITestCase):
    """ Test user login """

    def setUp(self):
        self.client = APIClient()
        self.client.post("/api/register/", data=USER_DATA, format="json")

    def _test_login(self, data, status_code, expected_params):
        """
        Tries to login with the given data, then verify the status code and the params in the response
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
            data=USER_DATA, status_code=status.HTTP_200_OK, expected_params=["access", "refresh"],
        )

    def test_login_wrong_username(self):
        """
        Tries to login with invalid username.
        """
        self._test_login(
            data={"username": "someting invalid", "password": USER_DATA["password"],},
            status_code=status.HTTP_401_UNAUTHORIZED,
            expected_params=["detail"],
        )

    def test_login_wrong_password(self):
        """
        Tries to login with invalid password.
        """
        self._test_login(
            data={"password": "someting invalid", "username": USER_DATA["username"],},
            status_code=status.HTTP_401_UNAUTHORIZED,
            expected_params=["detail"],
        )
