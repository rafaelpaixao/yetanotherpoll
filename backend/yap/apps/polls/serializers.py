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
        read_only_fields = ("id",)


class OptionResultSerializer(OptionSerializer):
    """Option Serializer with count_votes attribute"""

    def __init__(self, *args, **kwargs):
        super(OptionResultSerializer, self).__init__(*args, **kwargs)
        self.fields["count_votes"] = serializers.IntegerField()


class PollSerializer(serializers.ModelSerializer):
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
        read_only_fields = ("id",)

    def create(self, validated_data):
        options_data = validated_data.pop("options")
        poll = Poll.objects.create(**validated_data)
        for option_data in options_data:
            Option.objects.create(poll=poll, **option_data)
        return poll

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title")
        instance.description = validated_data.get("description")
        instance.save()

        options_ids = []
        for option in validated_data.get("options"):
            # If option has id, update it's instance
            if "id" in option:
                option_id = option.get("id")
                Option.objects.filter(pk=option_id, poll=instance).update(title=option["title"])
                # Save ids to delete the ones that are missing
                options_ids.append(option_id)
            else:
                Option.objects.create(poll=instance, **option)

        # Delete options associated with the poll, but that doesn't exists in the new data
        Option.objects.filter(poll=instance).exclude(pk__in=options_ids).delete()

        return instance


class PollResultSerializer(PollSerializer):
    """Poll Serializer with options vote count"""

    options = OptionResultSerializer(many=True)
