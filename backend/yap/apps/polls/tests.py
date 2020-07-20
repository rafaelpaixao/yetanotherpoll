from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from yap.apps.users.models import User
from yap.apps.users.tests import UserSetUp

from .models import Option, Poll, Vote
from .serializers import PollSerializer

POLL_DATA = {
    "title": "Test poll 1",
    "description": "Test poll description",
}

OPTIONS_DATA = [
    {"title": "Option A"},
    {"title": "Option B"},
    {"title": "Option C"},
]

POLL_WITH_OPTIONS = {**POLL_DATA, **{"options": OPTIONS_DATA}}


class PollSetUp(UserSetUp):
    def setUp(self):
        super().setUp()
        self.poll = Poll.objects.create(**POLL_DATA, author=self.user)
        self.options = [Option.objects.create(**option, poll=self.poll) for option in OPTIONS_DATA]


class CreatePollWithoutUserTestCase(APITestCase):
    """ Test operations that doesn't require an user to be performed """

    def setUp(self):
        self.client = APIClient()

    def test_create_poll_without_user(self):
        """
        Creates a poll without an user and check if response header has a token
        """
        response = self.client.post("/api/poll/create/", data=POLL_WITH_OPTIONS, format="json")
        self.assertTrue(response.has_header("Token"))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", response.data)


class VoteOnPollWithoutUserTestCase(PollSetUp, APITestCase):
    def test_vote_on_poll_as_guest(self):
        """
        Vote on poll without an user and check if response header has a token
        """
        client = APIClient()
        response = client.post(f"/api/vote/{self.options[0].pk}/", format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.has_header("Token"))


class EditPollTestCase(PollSetUp, APITestCase):
    """ Test poll update """

    def setUp(self):
        super().setUp()
        self.poll_data = PollSerializer(Poll.objects.get(pk=self.poll.pk)).data

    def _edit_poll(self):
        response = self.client.put(f"/api/poll/{self.poll.pk}/edit/", data=self.poll_data, format="json",)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.poll_data)

    def test_edit_poll_title(self):
        """
        Changes the title of a poll
        """
        self.poll_data["title"] = "Poll new title"
        self._edit_poll()

    def test_edit_poll_description(self):
        """
        Changes the description of a poll
        """
        self.poll_data["description"] = "Poll new description"
        self._edit_poll()

    def test_edit_option_title(self):
        """
        Changes title of first option
        """
        self.poll_data["options"][0]["title"] = "Option new title"
        self._edit_poll()

    def test_add_option(self):
        """
        Add new option to the poll
        """
        self.poll_data["options"].append({"title": "New Option!!!!"})
        response = self.client.put(f"/api/poll/{self.poll.pk}/edit/", data=self.poll_data, format="json",)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["options"]), len(self.poll_data["options"]))

    def test_remove_option(self):
        """
        Remove option from poll
        """
        self.poll_data["options"].pop()
        self._edit_poll()


class CreatePollWithUserTestCase(UserSetUp, APITestCase):
    """ Test operations that doesn't require an user to be performed """

    def test_create_poll_with_user(self):
        """
        Creates a poll with an user
        """
        response = self.client.post("/api/poll/create/", data=POLL_WITH_OPTIONS, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get("title"), POLL_WITH_OPTIONS.get("title"))
        self.assertEqual(response.data.get("description"), POLL_WITH_OPTIONS.get("description"))


class VoteOnPollWithUserTestCase(PollSetUp, APITestCase):
    def test_vote_on_poll_with_user(self):
        """
        Vote on poll with an user
        """
        # Vote on first option
        response = self.client.post(f"/api/vote/{self.options[0].pk}/", format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Then, changes vote to second option
        response = self.client.post(f"/api/vote/{self.options[1].pk}/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Find votes from user on poll
        vote_qs = Vote.objects.filter(author=self.user, option__poll=self.poll)
        # Should has only one vote on that poll
        self.assertEqual(vote_qs.count(), 1)
        self.assertEqual(vote_qs.first().option.pk, self.options[1].pk)


class GetPollsTestCase(PollSetUp, APITestCase):
    def setUp(self):
        super().setUp()
        self.vote = Vote.objects.create(option=self.options[0], author=self.user)

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

    def test_get_poll(self):
        """
        Fetch single poll
        """
        response = self.client.get(f"/api/poll/{self.poll.pk}/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("poll", response.data)
        self.assertIn("vote", response.data)

    def test_get_poll_results(self):
        """
        Fetch single poll results
        """
        response = self.client.get(f"/api/poll/{self.poll.pk}/?results=true", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("poll", response.data)
        self.assertIn("vote", response.data)
        options_data = response.data["poll"]["options"]
        self.assertEqual(options_data[0].get("count_votes"), self.options[0].count_votes())
        self.assertEqual(options_data[1].get("count_votes"), self.options[1].count_votes())
        self.assertEqual(options_data[2].get("count_votes"), self.options[2].count_votes())


class DeletePollTestCase(PollSetUp, APITestCase):
    def test_delete_poll(self):
        """
        Tries to delete the poll
        """
        response = self.client.delete(f"/api/poll/{self.poll.pk}/delete/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
