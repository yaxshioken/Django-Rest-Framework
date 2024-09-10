from drf_yasg.views import get_schema_view
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from account.models import Interest, User
from account.serializers import InterestSerializer, UserSerializer

get_schema_view(
    info="THERE ARE FIELD ARE REQUIRED!!!", public=True, generator_class=UserSerializer
)


class AccountViewSet(ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        serializer = UserSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


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
