from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from account.models import Profile, User, Interest


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "password2", "email"]

    def validate(self, validated_data):
        password = validated_data.pop("password")
        password2 = validated_data.pop("password2")

        if password != password2:
            raise serializers.ValidationError({"password": "Passwords must match."})

        user = User.objects.create_user(**validated_data, password=password)
        return user

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
        fields = ("city", "passport_number", "passport_letter", "interests")


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
