from rest_framework import serializers

from .models import Option, Poll, Vote


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = (
            "id",
            "title",
        )
        read_only_fields = ("id",)


class PollReadSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = Poll
        fields = (
            "id",
            "title",
            "description",
            "options",
        )
        read_only_fields = (
            "id",
            "author",
        )

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

        for option in validated_data.get("options"):
            if option.get("id", None) is None:
                Option.objects.create(poll=instance, **option)
            else:
                option_instance = Option.objects.get(pk=option.get("id"))
                option_instance.title = option.get("title")
                option_instance.save()

        return instance


class OptionResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = (
            "title",
            "count_votes",
        )
        read_only_fields = (
            "title",
            "count_votes",
        )


class PollResultSerializer(serializers.ModelSerializer):
    options = OptionResultSerializer(many=True)

    class Meta:
        model = Poll
        fields = ("id", "title", "description", "options")
        read_only_fields = ("id", "title", "description", "options")


class PollWriteSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = Poll
        fields = ("id", "title", "description", "options", "author")
        read_only_fields = ("id",)

    def create(self, validated_data):
        options_data = validated_data.pop("options")
        poll = Poll.objects.create(**validated_data)
        for option_data in options_data:
            Option.objects.create(poll=poll, **option_data)
        return poll


class PollUpdateSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = Poll
        fields = (
            "id",
            "title",
            "description",
            "options",
        )
        read_only_fields = (
            "id",
            "author",
        )

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title")
        instance.description = validated_data.get("description")
        instance.save()

        for option in validated_data.get("options"):
            if option.get("id", None) is None:
                Option.objects.create(poll=instance, **option)
            else:
                option_instance = Option.objects.get(pk=option.get("id"))
                option_instance.title = option.get("title")
                option_instance.save()

        return instance