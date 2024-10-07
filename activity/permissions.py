from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission to allow only the owner of the object or an admin user to access it.
    """
    def has_object_permission(self, request, view, obj):
        # print(f"Request user: {request.user}, Activity owner: {obj.user}")  # Debugging print statement
        # Allow access if the user is an admin
        if request.user and request.user.is_staff:
            return True
        
        # Allow access if the object belongs to the user (i.e., the user is the owner)
        return obj.id == request.user.id