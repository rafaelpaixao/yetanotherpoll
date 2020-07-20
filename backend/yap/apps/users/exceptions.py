from rest_framework import status
from rest_framework.exceptions import APIException


class UserIsNotAGuest(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "User is not a guest."
    default_code = "user_not_a_guest"
