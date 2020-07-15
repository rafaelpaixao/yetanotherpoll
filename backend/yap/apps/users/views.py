from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import AuthSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def current_user(request):
    """Returns the current user"""
    return Response({"username": request.user.username})


@api_view(["POST"])
def register(request):
    """User registration.

    Request body:
        username
        password

    Returns:
        token: User's token for API access.
    """
    # Validation
    serializer = AuthSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    # Create a new user
    user = User.objects.create_user(username=serializer.data.get("username"), password=serializer.data.get("password"),)

    # Generates token
    refresh_token = RefreshToken.for_user(user)

    return Response(
        {"refresh": str(refresh_token), "access": str(refresh_token.access_token),}, status=status.HTTP_201_CREATED
    )
