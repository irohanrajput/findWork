from rest_framework import generics
from .models import EmployerProfile, ApplicantProfile, CustomUser
from .serializers import EmployerProfileSerializer, ApplicantProfileSerializer, UserSerializer


class EmployerProfileListCreateView(generics.ListCreateAPIView):
    queryset = EmployerProfile.objects.all()
    serializer_class = EmployerProfileSerializer


class EmployerProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployerProfile.objects.all()
    serializer_class = EmployerProfileSerializer


class ApplicantProfileListCreateView(generics.ListCreateAPIView):
    queryset = ApplicantProfile.objects.all()
    serializer_class = ApplicantProfileSerializer


class ApplicantProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ApplicantProfile.objects.all()
    serializer_class = ApplicantProfileSerializer
    
class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
