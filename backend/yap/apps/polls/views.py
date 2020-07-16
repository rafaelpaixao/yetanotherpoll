from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from yap.apps.users.models import User
from yap.apps.users.views import response_with_user_token

from .models import Option, Poll, Vote
from .serializers import PollReadSerializer, PollResultSerializer, PollUpdateSerializer, PollWriteSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_polls(request):
    """List polls authored by user"""
    polls = Poll.objects.filter(author=request.user)
    serializer = PollReadSerializer(polls, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def vote_on_poll(request, option_id):
    """Submit user vote on poll"""

    # Check if the selected option exists
    option_qs = Option.objects.filter(pk=option_id)
    if not option_qs.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)

    # User is not logged in
    if request.user.pk is None:
        # Creates guest user
        user = User.objects.create_guest_user()
        # Register vote
        Vote.objects.create(option_id=option_id, author=user)
        # Return tokens
        return response_with_user_token(user)

    # User is logged in
    if request.user:
        # Verify if user has voted on this poll before
        option = option_qs.first()
        vote = Vote.objects.filter(option__poll=option.poll, author=request.user)
        if vote.exists():
            # If user has voted, update option
            vote.update(option=option)
        else:
            # Else, register vote
            Vote.objects.create(option=option, author=request.user)

        return Response(status=status.HTTP_200_OK)


@api_view(["GET"])
def get_poll(request, poll_id):
    """ Fetch a single poll by given id"""

    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PollReadSerializer(poll)
    return Response(serializer.data)


@api_view(["GET"])
def get_poll_results(request, poll_id):
    """ Fetch a single poll results by given id"""

    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PollResultSerializer(poll)
    return Response(serializer.data)


@api_view(["POST"])
def create_poll(request):
    """ Creates a new poll"""

    # Create poll read serializer to validate request data
    serializer = PollReadSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    # User is not logged in
    if request.user.pk is None:
        # Creates guest user
        author = User.objects.create_guest_user()
    else:
        author = request.user

    # Create poll write serializer to persist the data
    serializer = PollWriteSerializer(data={**request.data, "author": author.pk})
    serializer.is_valid(raise_exception=True)
    serializer.save()

    if author.is_guest:
        return response_with_user_token(author)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def edit_poll(request, poll_id):
    """ Edits a poll"""

    try:
        poll = Poll.objects.get(pk=poll_id, author=request.user)
    except Poll.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PollUpdateSerializer(poll, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data, status=status.HTTP_200_OK)
