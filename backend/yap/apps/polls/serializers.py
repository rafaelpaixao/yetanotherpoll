from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers

from .models import Option, Poll, Vote


class VoteSerializer(serializers.ModelSerializer):
    """Vote Serializer with related ids"""

    class Meta:
        model = Vote
        fields = (
            "id",
            "option",
        )


class OptionSerializer(serializers.ModelSerializer):
    """Option Serializer with only model fields"""

    class Meta:
        model = Option
        fields = (
            "id",
            "title",
        )


class OptionResultSerializer(OptionSerializer):
    """Option Serializer with count_votes attribute"""

    def __init__(self, *args, **kwargs):
        super(OptionResultSerializer, self).__init__(*args, **kwargs)
        self.fields["count_votes"] = serializers.IntegerField()


class PollSerializer(WritableNestedModelSerializer):
    """Poll serializer with custom create and update to handle options data."""

    options = OptionSerializer(many=True)

    class Meta:
        model = Poll
        fields = (
            "id",
            "title",
            "description",
            "options",
            "author",
        )


class PollResultSerializer(PollSerializer):
    """Poll Serializer with options vote count"""

    options = OptionResultSerializer(many=True)
