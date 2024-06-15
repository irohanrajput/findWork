from rest_framework import generics, permissions
from .models import EmployerProfile, JobSeekerProfile
from .serializers import EmployerProfileSerializer, JobSeekerProfileSerializer

class EmployerProfileListCreateView(generics.ListCreateAPIView):
    queryset = EmployerProfile.objects.all()
    serializer_class = EmployerProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class JobSeekerProfileListCreateView(generics.ListCreateAPIView):
    queryset = JobSeekerProfile.objects.all()
    serializer_class = JobSeekerProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
