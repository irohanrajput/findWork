from django.urls import path
from .views import JobOpeningListCreateView, ApplicationListCreateView

urlpatterns = [
    path('jobs/', JobOpeningListCreateView.as_view(), name='job-list-create'),
    path('applications/', ApplicationListCreateView.as_view(), name='application-list-create'),
]
