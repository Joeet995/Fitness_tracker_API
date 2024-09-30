from django.urls import path
from .views import ActivityListCreateView, ActivityDetailView

urlpatterns = [
    path('api-activities/', ActivityListCreateView.as_view(), name='activity-list'),
    path('api-activities/<int:pk>/', ActivityDetailView.as_view(), name='activity-detail'),
]

