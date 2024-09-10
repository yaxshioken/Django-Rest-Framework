from django.db.models import CharField
from django.template.context_processors import request
from rest_framework import serializers, status
from rest_framework.generics import get_object_or_404
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.response import Response

from account.models import User
from poll.models import Choice, Poll, Vote


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ("id", "author", "question", "pub_date")
        read_only_fields = ("id", "pub_date")

    def create(self, validated_data):
        return super().create(validated_data)

    def list(self, request, *args, **kwargs):
        serializer = PollSerializer(data=self.queryset.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, instance, validated_data):
        instance.question = validated_data.get("question", instance.question)
        instance.pub_date = validated_data.get("pub_date", instance.pub_date)
        instance.author = validated_data.get("author", instance.author)
        instance.save()
        return instance

    def destroy(self, instance):
        instance.delete()
        return {"success": True}


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ("id", "poll", "question")
        read_only_fields = ("id",)

    def create(self, validated_data):
        return super().create(validated_data)

    def list(self, request, *args, **kwargs):
        serializer = ChoiceSerializer(data=self.query_set.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, instance, validated_data):
        instance.question = validated_data.get("question", instance.question)
        instance.poll = validated_data.get("poll", instance.poll)

        instance.save()
        return instance

    def destroy(self, instance):
        instance.delete()
        return {"success": True}


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = "__all__"
        read_only_fields = ("id",)
