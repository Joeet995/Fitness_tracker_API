from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission to allow only the owner of the object or an admin user to access it.
    """
    def has_object_permission(self, request, view, obj):
        # Allow access if the user is an admin
        if request.user.is_staff:
            return True
        elif request.user.id == obj.id: # Allow access if the object belongs to the user (i.e., the user is the owner)
            return True
        else:
            raise PermissionDenied("You do not have permission to view this user.")
