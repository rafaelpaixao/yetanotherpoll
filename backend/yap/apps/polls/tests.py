from rest_framework import status
from rest_framework.test import APIClient, APITestCase

options_data = [
    {"title": "Option 1"},
    {"title": "Option 2"},
    {"title": "Option 3"},
]

poll_data = {
    "title": "My awesome poll",
    "description": "This is my poll",
    "options": options_data,
}


class PollTestCase(APITestCase):
    """ Test module for Poll API """

    def setUp(self):
        self.client = APIClient()

    def test_create_poll_without_authentication(self):
        response = self.client.post("/api/poll/", data=poll_data, format="json")
        self.assertEqual(response.data["title"], poll_data["title"])
        self.assertEqual(response.data["description"], poll_data["description"])
        self.assertEqual(len(response.data["options"]), len(poll_data["options"]))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
