from rest_framework import status
from rest_framework.exceptions import APIException


class UserNotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'User not found.'
    default_code = 'user_notfound'


class UserInvalidCredentials(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = 'User invalid credentials.'
    default_code = 'user_invalidcredentials'
