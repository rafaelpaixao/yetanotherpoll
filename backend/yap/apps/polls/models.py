from django.db import models
from django_extensions.db.models import TimeStampedModel


class Poll(TimeStampedModel):
    """
    Stores a poll
    """

    title = models.CharField(max_length=120)
    description = models.TextField(max_length=240)

    def __str__(self):
        return self.title


class Option(TimeStampedModel):
    """
    Stores a poll's option
    """

    title = models.CharField(max_length=120)
    poll = models.ForeignKey(Poll, models.PROTECT,)

    def __str__(self):
        return self.title


class Answer(TimeStampedModel):
    """
    Stores an answer by referency the selected option.
    """

    option = models.ForeignKey(Option, models.PROTECT)

    def __str__(self):
        return f"{self.option.poll} - {self.option}"
