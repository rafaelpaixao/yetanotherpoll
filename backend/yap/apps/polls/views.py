from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from yap.apps.users.decorators import allow_guest_mode
from yap.apps.users.models import User

from .models import Option, Poll, Vote
from .serializers import PollCreateSerializer, PollResultSerializer, PollSerializer, VoteSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_polls(request):
    """List polls authored by user"""
    polls = Poll.objects.filter(author=request.user)
    serializer = PollSerializer(polls, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@allow_guest_mode()
def vote_on_poll(request, option_id):
    """Submit user vote on poll"""

    # Fetch option and raise error if it doesn't exists
    option_qs = Option.objects.filter(pk=option_id)
    if not option_qs.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)
    option = option_qs.first()

    # If user has voted on this poll, update the vote
    vote_qs = Vote.objects.filter(option__poll=option.poll, author=request.user)
    if vote_qs.exists():
        vote_qs.update(option=option)
        response_status = status.HTTP_200_OK
    else:
        Vote.objects.create(option=option, author=request.user)
        response_status = status.HTTP_201_CREATED

    return Response(status=response_status)


@api_view(["GET"])
def get_poll(request, poll_id):
    """ Fetch a single poll by given id"""
    response_data = {
        "poll": None,
        "vote": None,
    }

    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Returns user's vote, if any
    if request.user.pk is not None:
        vote = Vote.objects.filter(option__poll=poll, author=request.user).first()
        response_data["vote"] = VoteSerializer(vote).data

    load_results = request.query_params.get("results", False)
    if load_results:
        response_data["poll"] = PollResultSerializer(poll).data
    else:
        response_data["poll"] = PollSerializer(poll).data

    return Response(response_data)


@api_view(["POST"])
@allow_guest_mode()
def create_poll(request):
    """ Creates a new poll"""

    # Create poll read serializer to validate request data
    serializer = PollSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    # Create poll write serializer to persist the data
    serializer = PollCreateSerializer(data={**request.data, "author": request.user.pk})
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def edit_poll(request, poll_id):
    """ Edits a poll"""

    try:
        poll = Poll.objects.get(pk=poll_id, author=request.user)
    except Poll.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PollSerializer(poll, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data, status=status.HTTP_200_OK)
