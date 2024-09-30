from django.db import models
from django.conf import settings

class Activity(models.Model):
    ACTIVITY_CHOICES = (
        ('Running', 'Running'),
        ('Cycling', 'Cycling'),
        ('Weightlifting', 'Weightlifting'),
        ('Swimming', 'Swimming'),
        ('Hiking', 'Hiking'),
        ('Yoga', 'Yoga'),
        ('Climbing', 'Climbing'),
        ('Calisthenics', 'Calisthenics'),
        ('Resistance Training', 'Resistance Training'),
        ('Other', 'Other'),
        # Add other activities as needed
    )
    
    # ForeignKey to User model, ensures each activity is associated with a user
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # Activity Type
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_CHOICES)

    #description
    description = models.CharField(max_length=200, null=True, blank=True)
    
    # Duration in minutes
    duration = models.PositiveIntegerField()  # For example, 60 minutes
    
    # Distance in km or miles (optional, since not all activities track distance)
    distance = models.FloatField(null=True, blank=True)  # Can be empty for activities like weightlifting
    
    # Calories burned
    calories_burned = models.PositiveIntegerField()
    
    # Date of the activity
    date = models.DateField()
    
    def __str__(self):
        return f"{self.activity_type} on {self.date} by {self.user.username}"