from django.http import Http404
from django.shortcuts import get_object_or_404, render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import request, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet

import poll
from poll.models import Choice, Poll, Vote
from poll.serializers import (ChoiceSerializer, PollSerializer, UserSerializer,
                              VoteSerializer)


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class ChoiceViewSet(ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import Vote
from .serializers import VoteSerializer


class VoteViewSet(ViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    def create(self, request):
        serializer = VoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        vote = self.get_object()
        serializer = self.serializer_class(vote)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        vote = self.get_object()
        serializer = self.serializer_class(vote, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        vote = self.get_object()
        serializer = self.serializer_class(vote, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        vote = self.get_object()
        vote.delete()
        return Response({"success": True}, status=status.HTTP_204_NO_CONTENT)

    def get_object(self):
        return self.queryset.get(pk=self.kwargs["pk"])


class UserCreateView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
