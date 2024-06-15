from rest_framework import generics, permissions
from .models import JobOpening, Application
from .serializers import JobOpeningSerializer, ApplicationSerializer

class JobOpeningListCreateView(generics.ListCreateAPIView):
    queryset = JobOpening.objects.all()
    serializer_class = JobOpeningSerializer
    permission_classes = [permissions.IsAuthenticated]

class ApplicationListCreateView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
