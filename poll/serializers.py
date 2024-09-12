from rest_framework import serializers

from poll.models import Choice, Poll, Vote


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ("id", "author", "question", "pub_date")
        read_only_fields = ("id", "pub_date")


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ("id", "poll", "question")
        read_only_fields = ("id",)


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = "__all__"
        read_only_fields = ("id",)
