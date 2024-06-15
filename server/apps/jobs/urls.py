from django.urls import path
from .views import JobDetailListCreateView, ApplicationListCreateView

urlpatterns = [
    path('jobs/', JobDetailListCreateView.as_view(), name='job-list-create'),
    path('applications/', ApplicationListCreateView.as_view(), name='application-list-create'),
]
