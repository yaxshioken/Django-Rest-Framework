from django.db.models import Count
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from account.models import User
from account.serializers import UserSerializer
from poll.models import Choice, Poll, Vote
from poll.serializers import ChoiceSerializer, PollSerializer, VoteSerializer


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    @action(detail=True, methods=["get"], url_path="choices_list")
    def choices(self, *args, **kwargs):
        poll = self.get_object()
        choices = Choice.objects.filter(poll=poll)
        serializer = ChoiceSerializer(choices, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"], url_path="top-votes")
    def top_votes(self, request):
        polls_vote = Poll.objects.annotate(vote_count=Count("vote")).order_by(
            "-vote_count"
        )
        top_votes = polls_vote[:3]

        serializer = self.get_serializer(top_votes, many=True)
        return Response(serializer.data)


class ChoiceViewSet(ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class VoteViewSet(ViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class UserCreateViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
