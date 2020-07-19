from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class TokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Adding extra claims as showed in:
        # https://django-rest-framework-simplejwt.readthedocs.io/en/latest/customizing_token_claims.html
        token["username"] = "Guest" if user.is_guest else user.username

        return token
