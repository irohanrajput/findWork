from django.urls import path
from .views import EmployerProfileListCreateView, ApplicantProfileListCreateView, EmployerProfileDetailView, ApplicantProfileDetailView

urlpatterns = [
    path('employers/', EmployerProfileListCreateView.as_view(), name='employer-list-create'),
    path("employers/<int:pk>/", EmployerProfileDetailView.as_view(), name="Employer-detail"),
    path("employers/<int:pk>/update", EmployerProfileDetailView.as_view(), name="Employer-update"),
    path("employers/<int:pk>/delete", EmployerProfileDetailView.as_view(), name="Employer-delete"),
    path('applicant/', ApplicantProfileListCreateView.as_view(), name='Applicant-list-create'),
    path("<int:pk>/", ApplicantProfileDetailView.as_view(), name="Employer-detail"),
    path("<int:pk>/update", ApplicantProfileDetailView.as_view(), name="Employer-update"),
    path("<int:pk>/delete", ApplicantProfileDetailView.as_view(), name="Employer-delete"),
]
