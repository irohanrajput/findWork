from rest_framework import generics, permissions
from .models import JobOpening, JobApplication 
from .serializers import JobOpeningSerializer, ApplicationSerializer

class JobOpeningListCreateView(generics.ListCreateAPIView):
    queryset = JobOpening.objects.all()
    serializer_class = JobOpeningSerializer

class ApplicationListCreateView(generics.ListCreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = ApplicationSerializer
