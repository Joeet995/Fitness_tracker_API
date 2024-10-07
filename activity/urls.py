from django.urls import path
from .views import ActivityListCreateView, ActivityDetailView, ActivitySummaryView

urlpatterns = [
    path('api-activities/', ActivityListCreateView.as_view(), name='activity-list'),
    path('api-activities/<int:pk>/', ActivityDetailView.as_view(), name='activity-detail'),
    path('api-activity-summary/', ActivitySummaryView.as_view(), name='activity-summary'),
]

