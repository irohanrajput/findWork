from django.urls import path
from .views import EmployerProfileListCreateView, JobSeekerProfileListCreateView

urlpatterns = [
    path('employers/', EmployerProfileListCreateView.as_view(), name='employer-list-create'),
    path('jobseekers/', JobSeekerProfileListCreateView.as_view(), name='jobseeker-list-create'),
]
