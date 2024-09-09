from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='user', queryset=User.objects.all())
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Customer
        fields = ['user_id', 'username', 'phone_number', 'email']

    def get_user(self, obj):
        return obj.user.username 