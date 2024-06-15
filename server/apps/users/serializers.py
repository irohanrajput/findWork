from rest_framework import serializers
from django.contrib.auth.models import User
from apps.users.models import EmployerProfile, JobSeekerProfile, CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'bio', 'address', 'mobile']

class EmployerProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = EmployerProfile
        fields = '__all__'

class JobSeekerProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = JobSeekerProfile
        fields = '__all__'
