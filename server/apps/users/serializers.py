from rest_framework import serializers
from django.contrib.auth.models import User
from apps.users.models import EmployerProfile, JobSeekerProfile, CustomUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "bio",
            "password",
        )
        extra_kwargs = {"password": {"write_only": True, "required": True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class EmployerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = EmployerProfile
        fields = '__all__'

class JobSeekerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = JobSeekerProfile
        fields = '__all__'
