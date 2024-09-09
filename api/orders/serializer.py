# serializers.py in the orders app
from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    pizza_name = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ['pizza_name', 'quantity']  # Use pizza_name instead of the pizza ID

    def get_pizza_name(self, obj):
        return obj.pizza.name  # Return the pizza name

class OrderSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.user.username', read_only=True)  # Show customer's username
    items = OrderItemSerializer(many=True)  # Serialize related items

    class Meta:
        model = Order
        fields = ['customer_name', 'status', 'total_price', 'items']