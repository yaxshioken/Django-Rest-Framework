from drf_yasg.openapi import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from yaml import serialize

from account.models import Interest, User
from account.serializers import (AccountDetialSeriaizer, InterestSerializer,
                                 UserSerializer)


class AccountViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_update(self, serializer):
        super().perform_update(serializer)

    # def perform_update(self, serializer,*args, **kwargs):
    #
    #     serializer = UserSerializer(instance=self.request.user)
    #     serializer.update(self.request.data)
    #     serializer.save(raiseExceptions=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @action(detail=True, methods=["get"], url_path="account_interests")
    def interests(self, *args, **kwargs):
        account = self.get_object()
        serializer = InterestSerializer(account.profile.interests, many=True)
        return Response(serializer.data)


class InterestViewSet(ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
