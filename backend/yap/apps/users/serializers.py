from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "is_guest",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "is_guest": {"required": False},
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        if "username" in validated_data:
            instance.username = validated_data["username"]
        if "password" in validated_data:
            instance.set_password(validated_data["password"])
        instance.save()
        return instance


class TokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Adding extra claims as showed in:
        # https://django-rest-framework-simplejwt.readthedocs.io/en/latest/customizing_token_claims.html
        token["username"] = "Guest" if user.is_guest else user.username
        token["is_guest"] = user.is_guest

        return token
