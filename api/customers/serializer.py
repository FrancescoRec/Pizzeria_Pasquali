from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Customer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {
            'password': {'write_only': True}  
        }

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Nested serializer for the User

    class Meta:
        model = Customer
        fields = ['user', 'phone_number', 'address']

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
        # Extract user data from the validated data
        user_data = validated_data.pop('user')
        
        # Create the user (using create_user to handle password hashing)
        user = User.objects.create_user(**user_data)
        
        # Create the customer and associate the newly created user
        customer = Customer.objects.create(user=user, **validated_data)
        
        return customer
