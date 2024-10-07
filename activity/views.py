from rest_framework import generics, permissions
from .models import Activity
from .serializers import ActivitySerializer
from rest_framework.exceptions import PermissionDenied
from django.db.models import Sum
from django.utils import timezone
from rest_framework.response import Response

# List and Create activities
class ActivityListCreateView(generics.ListCreateAPIView):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can access

    def get_queryset(self):
        # Return only the activities of the logged-in user
        return Activity.objects.filter(user=self.request.user)

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
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users can access the summary
    serializer_class = ActivitySerializer


    def get(self, request):
        # Retrieve query parameters for date filtering (optional)
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        
        # Get the logged-in user
        user = request.user

        # Filter activities based on the date range provided
        activities = Activity.objects.filter(user=user)

        if start_date:
            activities = activities.filter(date__gte=start_date)
        if end_date:
            activities = activities.filter(date__lte=end_date)

        # Aggregate the total duration, distance, and calories burned
        summary = activities.aggregate(
            total_duration=Sum('duration'),
            total_distance=Sum('distance'),
            total_calories=Sum('calories_burned')
        )

        # Add trend data (e.g., activity count over time, if requested)
        trends = self.get_trend_data(activities)

        # Prepare the response data
        response_data = {
            'total_duration': summary['total_duration'] or 0,  # Fallback to 0 if no activities
            'total_distance': summary['total_distance'] or 0,
            'total_calories': summary['total_calories'] or 0,
            'trends': trends  # Optional: trends like weekly/monthly breakdowns
        }

        return Response(response_data)

    def get_trend_data(self, activities):
        # Example trend: Count activities grouped by week (or month)
        # This function can be expanded to include different time periods

        trends = activities.extra(select={'week': "strftime('%W', date)"}) \
                           .values('week') \
                           .annotate(total_duration=Sum('duration')) \
                           .order_by('week')

        return trends