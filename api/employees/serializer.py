from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Employee


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {
            'password': {'write_only': True}  # Ensure the password is write-only and not included in responses
        }


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Nested serializer for the user

    class Meta:
        model = Employee
        fields = ['user', 'position', 'phone_number', 'is_approved']

    def validate_user(self, value):
        """Validate if the username or email already exists."""
        username = value.get('username')
        email = value.get('email')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"username": "A user with this username already exists."})

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "A user with this email already exists."})

        return value

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        
        # Create the user
        user = User.objects.create_user(**user_data) 
        
        # Create the employee and associate the new user
        employee = Employee.objects.create(user=user, **validated_data)
        
        return employee
