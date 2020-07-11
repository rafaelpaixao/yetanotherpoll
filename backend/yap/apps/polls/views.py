from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from .models import Option, Poll
from .serializers import OptionSerializer, PollSerializer


class PollViewset(viewsets.ModelViewSet):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()


class OptionViewset(viewsets.ModelViewSet):
    serializer_class = OptionSerializer
    queryset = Option.objects.all()
