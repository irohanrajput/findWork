from django.urls import path
from .views import (
    EmployerProfileListCreateView, JobSeekerProfileListCreateView,
    JobOpeningListCreateView, ApplicationListCreateView
)

urlpatterns = [
    path('employers/', EmployerProfileListCreateView.as_view(), name='employer-list-create'),
    path('jobseekers/', JobSeekerProfileListCreateView.as_view(), name='jobseeker-list-create'),
    path('jobs/', JobOpeningListCreateView.as_view(), name='job-list-create'),
    path('applications/', ApplicationListCreateView.as_view(), name='application-list-create'),
]
