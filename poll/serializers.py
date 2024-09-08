from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.response import Response

from poll.models import Poll, Choice, Vote


class PollSerializer(serializers.Serializer):
    id =serializers.IntegerField()
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    question = serializers.CharField()
    pub_date = serializers.DateTimeField()
    def create(self, validated_data):
        return Poll.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.question = validated_data.get('question', instance.question)
        Poll.objects.update(**instance.dict())
        return instance


class PollPatchSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author_id = serializers.IntegerField(allow_null=True, required=False)
    question = serializers.CharField(allow_blank=True, required=False)
    pub_date = serializers.DateTimeField(allow_null=True, required=False)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class PollDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    autor_id = serializers.IntegerField(read_only=True)
    question = serializers.CharField(read_only=True)
    pub_date = serializers.DateTimeField(read_only=True)


class ChoiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    poll_id = serializers.CharField()
    choice = serializers.CharField()

    def create(self, validated_data):
        instance = Choice.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.choice = validated_data.get('choice', instance.choice)
        instance.poll_id = validated_data.get('poll_id', instance.poll_id)
        instance.save()
        return instance


class ChoicePatchSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, required=False)
    poll_id = serializers.CharField(allow_null=True, required=False, allow_blank=True)
    choice = serializers.CharField(allow_null=True, required=False, allow_blank=True)

    def update(self, instance, validated_data):
        instance.choice = validated_data.get('choice', instance.choice)
        instance.poll_id = validated_data.get('poll_id', instance.poll_id)
        instance.save()
        return instance


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = "__all__"

class VoterSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    choice_id = serializers.PrimaryKeyRelatedField(queryset=Choice.objects.all(),allow_null=True,required=False)
    voted_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),allow_null=True,required=False)
    poll = serializers.PrimaryKeyRelatedField(queryset=Poll.objects.all(),allow_null=True,required=False)


    class Meta:
        model = Vote
        fields = "__all__"
    def create(self, validated_data):
        instance = Vote.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.voted_by = validated_data.get('voted_by', instance.voted_by)
        instance.poll = validated_data.get('poll', instance.poll)
        instance.save()
        return instance