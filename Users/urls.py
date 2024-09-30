from django.urls import path
from .views import UserCreateView, UserListView, UserDetailView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api-users/', UserListView.as_view(), name='user-list'),  # List users
    path('api-register/', UserCreateView.as_view(), name='user-create'),  # Register a new user
    path('api-user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),  # Retrieve, update, delete a user
]

urlpatterns += [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]