from django.db.models import Count
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from account.models import Interest, User
from account.serializers import (AccountDetialSeriaizer, InterestSerializer,
                                 UserSerializer, ProfileSerializer)


class AccountViewSet(ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=["POST"], url_path="top-accounts")
    def top_interests(self, request,*args, **kwargs):
        top_interests = User.interests.get(count=Count('interests')).order_by('-count')
        serializer = ProfileSerializer(top_interests, many=True)
        returnResponse(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        serializer = UserSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = AccountDetialSeriaizer(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = AccountDetialSeriaizer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(
            {"message": "Successfully deleted"}, status=status.HTTP_204_NO_CONTENT
        )


class InterestViewSet(ViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer

    def list(self, request):
        serializer = InterestSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = InterestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = InterestSerializer(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = InterestSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = InterestSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(
            {"message": "Successfully deleted"}, status=status.HTTP_204_NO_CONTENT
        )
