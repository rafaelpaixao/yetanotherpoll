from django.db import models
from django_extensions.db.models import TimeStampedModel

from yap.apps.users.models import User


class Poll(TimeStampedModel):
    """
    Stores a poll
    """

    title = models.CharField(max_length=120)
    description = models.TextField(max_length=240)
    requires_non_guest_to_vote = models.BooleanField(
        default=False, help_text="To vote on this poll, user must be logged in and not be a Guest.",
    )

    author = models.ForeignKey(User, models.CASCADE, related_name="polls")

    def __str__(self):
        return self.title


class Option(TimeStampedModel):
    """
    Stores a poll's option
    """

    title = models.CharField(max_length=120)
    poll = models.ForeignKey(Poll, models.CASCADE, related_name="options")

    def count_votes(self):
        """Count total votes on option.

        Returns:
            int: Total votes on option.
        """
        return self.votes.count()

    def __str__(self):
        return self.title


class Vote(TimeStampedModel):
    """
    Stores a vote by referency the selected option and the user.
    """

    option = models.ForeignKey(Option, models.CASCADE, related_name="votes")
    author = models.ForeignKey(User, models.CASCADE, related_name="votes")

    def __str__(self):
        return f"{self.option.poll} - {self.option}"
