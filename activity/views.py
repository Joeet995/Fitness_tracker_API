from rest_framework import generics, permissions
from .models import Activity
from .serializers import ActivitySerializer
from .permissions import IsOwnerOrAdmin

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
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]  # Ensure the user is the owner