from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import User


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
