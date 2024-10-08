from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)  # Ensure password is required

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'date_of_birth', 'height', 'gender', 'current_weight']

    def create(self, validated_data):
        # Use create_user method to hash the password correctly
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user
