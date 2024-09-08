from django.db.migrations import serializer
from django.shortcuts import get_object_or_404, render
from rest_framework import request, status
from rest_framework.response import Response
from rest_framework.views import APIView

import poll
from poll.models import Poll, Choice, Vote
from poll.serializers import (PollPatchSerializer,
                              PollSerializer, UserSerializer, ChoiceSerializer, ChoicePatchSerializer, VoteSerializer,
                              VoterSerializer)


class PollView(APIView):
    def get(self, request):
        polls = Poll.objects.all()
        serializer = PollSerializer(polls, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PollSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PollPutView(APIView):
    def put(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        serializer = PollSerializer(poll, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PollDeleteView(APIView):
    def delete(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        poll.delete()
        return Response(
            {"message": "Poll Succesfully deleted"}, status=status.HTTP_202_ACCEPTED
        )


class PollPatchView(APIView):
    def patch(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        serializer = PollPatchSerializer(poll, data=request.data)
        if serializer.is_valid():
            for key, value in serializer.validated_data.items():
                setattr(poll, key, value)
                poll.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserCreateView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PollDetailView(APIView):
    def get(self, request, pk):
        polls = get_object_or_404(Poll, pk=pk)
        serializer = PollSerializer(polls)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ChoiceView(APIView):
    def get(self, request):
        choices = Choice.objects.all()
        serializer = ChoiceSerializer(choices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



    def post(self, request):
        serializer = ChoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ChoiceCRUDView(APIView):
    def get(self,request, pk):
        choice = get_object_or_404(Choice, pk=pk)
        serializer = ChoiceSerializer(choice)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        choice = get_object_or_404(Choice, pk=pk)
        serializer = ChoiceSerializer(choice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        choice = get_object_or_404(Choice, pk=pk)
        serializer = ChoicePatchSerializer(choice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        choice = get_object_or_404(Choice, pk=pk)
        choice.delete()
        return Response(
            {"message": "Choice Succesfully deleted"}, status=status.HTTP_202_ACCEPTED
        )
class VoteView(APIView):
    def get(self, request):
        votes = Vote.objects.all()
        serializer = VoteSerializer(votes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = VoteSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VoteDetailView(APIView):
    def get(self, request, pk):
        vote = get_object_or_404(Vote, pk=pk)
        serializer = VoteSerializer(vote)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, pk):
        vote = get_object_or_404(Vote, pk=pk)
        serializer = VoteSerializer(vote, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        vote = get_object_or_404(Vote, pk=pk)
        serializer =VoterSerializer(vote, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        vote = get_object_or_404(Vote, pk=pk)
        vote.delete()
        return Response(
            {"message": "Choice Succesfully deleted"}, status=status.HTTP_202_ACCEPTED
        )