from rest_framework import serializers
from .models import Pizza, Topping

class ToppingSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100) 

    class Meta:
        model = Topping
        fields = ['name']  

class PizzaSerializer(serializers.ModelSerializer):
    toppings = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Topping.objects.all()
    )

    class Meta:
        model = Pizza
        fields = ['name', 'toppings', 'price', 'vegetarian', 'gluten_free']

    def to_representation(self, instance):
        """
        Customize the representation of the toppings field.
        """
        representation = super().to_representation(instance)
        representation['toppings'] = ToppingSerializer(instance.toppings, many=True).data
        return representation
