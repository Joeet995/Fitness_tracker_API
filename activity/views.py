from rest_framework import generics, permissions
from .models import Activity
from .serializers import ActivitySerializer, ActivitySummarySerializer
from rest_framework.exceptions import PermissionDenied
from django.db.models import Sum
from django.utils import timezone
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django.db.models import Q

# List and Create activities
class ActivityListCreateView(generics.ListCreateAPIView):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can access

    # Enable DjangoFilterBackend and ordering
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['activity_type']  # Filter by activity type
    ordering_fields = ['date', 'duration', 'calories_burned']  # Add sorting options

    def get_queryset(self):

        
        user = self.request.user  # Only show activities of the logged-in user
        queryset = Activity.objects.filter(user=user)


        # Get query parameters for filtering
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        activity_type = self.request.query_params.get('activity_type')

        # Filter by date range if provided
        if start_date and end_date:
            queryset = queryset.filter(date__range=[start_date, end_date])

        # Filter by activity type if provided
        if activity_type:
            queryset = queryset.filter(activity_type=activity_type)

        return queryset
        
    

    def perform_create(self, serializer):
        # Associate the activity with the logged-in user
        serializer.save(user=self.request.user)

# Retrieve, Update, and Delete a specific activity
class ActivityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]# Ensure the user is the owner

    def get_object(self):
        # Get the activity object
        activity = super().get_object()
        
        # Check if the requesting user is the owner of the activity
        if activity.user != self.request.user:
            raise PermissionDenied("You do not have permission to view this activity.")

        # Return the activity if the user is the owner
        return activity
    

class ActivitySummaryView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users
    serializer_class = ActivitySummarySerializer

    def get(self, request, *args, **kwargs):
        # Get the current logged-in user
        user = request.user

        # Optional date filtering (e.g., past week)
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        # Filter activities for the current user
        activities = Activity.objects.filter(user=user)

        # Optionally filter by date range
        if start_date:
            activities = activities.filter(date__gte=start_date)
        if end_date:
            activities = activities.filter(date__lte=end_date)

        # Aggregate the totals (sum of duration, distance, calories burned)
        summary_data = activities.aggregate(
            total_duration=Sum('duration'),
            total_distance=Sum('distance'),
            total_calories=Sum('calories_burned')
        )

        # Serialize the summary data
        serializer = self.get_serializer(summary_data)

        return Response(serializer.data)