from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from yap.apps.users.models import User

from .models import Option, Poll, Vote

user_data = {
    "username": "test_user",
    "password": "super_secret_password",
}

poll = {
    "title": "Test poll 1",
    "description": "Test poll description",
}
options = [
    {"title": "Option A"},
    {"title": "Option B"},
    {"title": "Option C"},
]


class PollTestCase(APITestCase):
    """ Test user registration """

    def setUp(self):
        self.user = User.objects.create_user(**user_data)
        self.poll = Poll.objects.create(**poll, author=self.user)
        self.options = [Option.objects.create(**option, poll=self.poll) for option in options]
        self.client = APIClient()
        self.tokens = self.client.post("/api/login/", data=user_data, format="json").data
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.tokens.get("access"))

    def test_get_user_polls(self):
        """
        List all polls authored by user
        """
        response = self.client.get("/api/poll/", format="json")
        data = response.data[0]
        self.assertEqual(data.get("title"), self.poll.title)
        self.assertEqual(data.get("description"), self.poll.description)
        self.assertEqual(data.get("options")[0].get("title"), self.options[0].title)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_vote_on_poll_as_guest(self):
        """
        Vote on poll without authentication
        """
        client = APIClient()
        response = client.post(f"/api/vote/{self.options[0].pk}/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.has_header("Token"))

    def test_vote_on_as_non_guest(self):
        """
        Vote on poll with authentication
        """
        # Vote on first option
        response = self.client.post(f"/api/vote/{self.options[0].pk}/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Then, changes vote to second option
        response = self.client.post(f"/api/vote/{self.options[1].pk}/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Find votes from user on poll
        vote_qs = Vote.objects.filter(author=self.user, option__poll=self.poll)
        # Should has only one vote on that poll
        self.assertEqual(vote_qs.count(), 1)
        self.assertEqual(vote_qs.first().option.pk, self.options[1].pk)

    def test_get_poll(self):
        """
        Fetch single poll
        """
        response = self.client.get(f"/api/poll/{self.poll.pk}/", format="json")
        poll_data = response.data
        self.assertEqual(poll_data.get("title"), self.poll.title)
        self.assertEqual(poll_data.get("description"), self.poll.description)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_poll_results(self):
        """
        Fetch single poll results
        """

        # Add a few votes
        self.client.post(f"/api/vote/{self.options[0].pk}/", format="json")
        self.client.post(f"/api/vote/{self.options[0].pk}/", format="json")
        self.client.post(f"/api/vote/{self.options[1].pk}/", format="json")

        response = self.client.get(f"/api/poll/{self.poll.pk}/results/", format="json")
        options_data = response.data.get("options")
        self.assertEqual(options_data[0].get("count_votes"), self.options[0].count_votes())
        self.assertEqual(options_data[1].get("count_votes"), self.options[1].count_votes())
        self.assertEqual(options_data[2].get("count_votes"), self.options[2].count_votes())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_poll_as_guest(self):
        """
        Creates a poll as guest user
        """
        client = APIClient()
        response = client.post("/api/poll/create/", data={**poll, "options": []}, format="json")
        self.assertTrue(response.has_header("Token"))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_poll_as_non_guest(self):
        """
        Creates a poll
        """
        response = self.client.post("/api/poll/create/", data={**poll, "options": []}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get("title"), poll.get("title"))
        self.assertEqual(response.data.get("description"), poll.get("description"))

    def test_edit_poll(self):
        """
        Edits a poll
        """
        new_title = "Poll new title"
        response = self.client.put(
            f"/api/poll/{self.poll.pk}/edit/",
            data={"title": new_title, "description": poll.get("description"), "options": []},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("title"), new_title)
        self.assertEqual(response.data.get("id"), self.poll.pk)
