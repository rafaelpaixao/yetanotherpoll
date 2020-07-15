from rest_framework import status
from rest_framework.test import APIClient, APITestCase

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
        response = self.client.post("/api/token/", data=user_data, format="json")
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

    def test_current_user(self):
        """
        Get the current user.
        """
        response = self.client.get("/api/user/me/", format="json")
        self.assertEqual(response.data.get("username"), user_data.get("username"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_current_user_without_token(self):
        """
        Tries to get the current user without providing a token.
        Expects the status code to be Unauthorized.
        """
        client = APIClient()
        response = client.get("/api/user/me/", format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_current_user_with_invalid_token(self):
        """
        Tries to get the current user providing an invalid token.
        Expects the status code to be Unauthorized.
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION="Bearer InvalidToken")
        response = client.get("/api/user/me/", format="json")
        self.assertEqual(response.data.get("code"), "token_not_valid")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
