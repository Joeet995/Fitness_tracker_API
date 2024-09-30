from django.contrib import admin
from .models import Activity

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type', 'duration', 'distance', 'calories_burned', 'date', 'description')
    list_filter = ('activity_type', 'date')
    search_fields = ('user__username', 'activity_type')

admin.site.register(Activity, ActivityAdmin)