from rest_framework import generics, permissions
from .models import JobDetails, JobApplication 
from .serializers import JobDetailSerializer, ApplicationSerializer

class JobDetailListCreateView(generics.ListCreateAPIView):
    queryset = JobDetails.objects.all()
    serializer_class = JobDetailSerializer

class ApplicationListCreateView(generics.ListCreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = ApplicationSerializer
