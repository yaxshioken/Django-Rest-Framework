from rest_framework import serializers
from rest_framework.authentication import (BasicAuthentication,
                                           TokenAuthentication)
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ModelSerializer

from account.models import Interest, Profile, User


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        permission_classes = (IsAuthenticated,)
        fields = "__all__"
        extra_kwargs = {
            "password": {"write_only": True},
            "first_name": {"required": True, "allow_null": True},  # Updated
            "last_name": {"required": True, "allow_null": True},  # Updated
        }


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ("id", "name")


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("city", "passport_number", "passport_letter", "interests")
        extra_kwargs = {
            "interests": {"required": False, "allow_null": True, "allow_empty": True},
        }

    def to_representation(self, instance: Profile):
        representation = super().to_representation(instance)
        representation["interests"] = InterestSerializer(
            instance.interests.all(), many=True
        ).data
        return representation


class AccountDetialSeriaizer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "phone",
            "profile",
        )
        extra_kwargs = {
            "email": {"required": False, "allow_null": True},
            "first_name": {"required": False, "allow_null": True},
            "last_name": {"required": False, "allow_null": True},
            "profile": {"required": False, "allow_null": True},
            "password": {"write_only": True, "required": False},
            "password2": {"write_only": True, "required": False},
        }


