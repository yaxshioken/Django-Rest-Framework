from drf_yasg.openapi import Response
from rest_framework import serializers, status

from account.models import Interest, Profile, User


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "password2", "email"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        password2 = validated_data.pop("password2")

        if password != password2:
            raise serializers.ValidationError({"password": "Passwords must match."})

        user = User.objects.create_user(**validated_data, password=password)
        return user
    def retrieve(self, request, pk=None):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "password": {"write_only": True},
            "first_name": {"required": True, "allow_null": True},  # Updated
            "last_name": {"required": True, "allow_null": True},  # Updated
        }


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ("name", "slug")
        extra_kwargs = {
            "slug": {"read_only": True},
        }


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("city", "passport_number", "passport_letter")
