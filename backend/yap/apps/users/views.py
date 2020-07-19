from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import TokenSerializer, UserSerializer


class LoginView(TokenObtainPairView):
    serializer_class = TokenSerializer


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
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    # Create a new user
    user = serializer.save()
    token = TokenSerializer().get_token(user)
    data = {
        "access": str(token.access_token),
        "refresh": str(token),
    }

    return Response(data, status=status.HTTP_201_CREATED)
