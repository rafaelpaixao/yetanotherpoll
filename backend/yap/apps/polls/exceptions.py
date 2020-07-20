from rest_framework import status
from rest_framework.exceptions import APIException


class PollRequiresAuthToVote(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "This poll requires authentication to vote, please login."
    default_code = "poll_requires_auth_to_vote"
