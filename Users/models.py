from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Inherits fields like first_name, last_name, username, password, and email from AbstractUser
    
    # Additional fields
    date_of_birth = models.DateField(null=True, blank=True)  # Date of Birth
    height = models.FloatField(null=True, blank=True)  # Height in meters or cm
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)  # Gender choice
    current_weight = models.FloatField(null=True, blank=True)  # Weight in kg or pounds

    def __str__(self):
        return self.username