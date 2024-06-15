from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.users.models import EmployerProfile, ApplicantProfile

CustomUser = get_user_model()

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
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            bio=validated_data.get('bio', ''),
        )
        return user

class EmployerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = EmployerProfile
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user') #deleting user from validated data i.e. only fields of EmployerProfile will be left
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        employer_profile = EmployerProfile.objects.create(user=user, **validated_data)
        return employer_profile

class ApplicantProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ApplicantProfile
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        job_seeker_profile = ApplicantProfile.objects.create(user=user, **validated_data)
