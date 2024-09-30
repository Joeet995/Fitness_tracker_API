from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

class UserAdmin(BaseUserAdmin):
    # Fields to be displayed in the admin list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'gender', 'current_weight', 'height', 'date_of_birth', 'is_staff')
    
    # Fields to filter by in the admin interface
    list_filter = ('gender', 'is_staff', 'is_superuser', 'is_active')
    
    # Fields to be used in the detail view (for updating user info)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'height', 'current_weight', 'gender')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Fields to show when adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    
    # Fields to search by in the admin interface
    search_fields = ('username', 'email', 'first_name', 'last_name')
    
    # Default ordering (most recently joined users first)
    ordering = ('-date_joined',)

# Register the User model and the UserAdmin class with Django's admin site
admin.site.register(CustomUser, UserAdmin)
