from django.test import TestCase
from .models import Pizza, Topping
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from .serializer import PizzaSerializer, ToppingSerializer
from django.urls import reverse
from decimal import Decimal
from django.contrib.auth.models import User

class PizzaModelTest(TestCase):

    def setUp(self):
        self.topping1 = Topping.objects.create(name="Mushrooms")
        self.topping2 = Topping.objects.create(name="Cheese")
        self.pizza = Pizza.objects.create(name="Veggie Delight", price=9.99, vegetarian=True, gluten_free=False)

    def test_create_pizza(self):
        self.pizza.toppings.set([self.topping1, self.topping2])
        self.assertEqual(self.pizza.name, "Veggie Delight")
        self.assertEqual(self.pizza.price, 9.99)
        self.assertEqual(self.pizza.vegetarian, True)
        self.assertEqual(self.pizza.gluten_free, False)
        self.assertEqual(self.pizza.toppings.count(), 2)

    def test_create_topping(self):
        topping = Topping.objects.create(name="Pepperoni")
        self.assertEqual(topping.name, "Pepperoni")

class PizzaSerializerTest(APITestCase):

    def setUp(self):
        self.topping1 = Topping.objects.create(name="Mushrooms")
        self.topping2 = Topping.objects.create(name="Cheese")
        self.pizza_data = {
            'name': "Veggie Delight",
            'price': 9.99,
            'vegetarian': True,
            'gluten_free': False,
            'toppings': [self.topping1.id, self.topping2.id]
        }

    def test_serialize_pizza(self):
        serializer = PizzaSerializer(data=self.pizza_data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        pizza = serializer.save()

        self.assertEqual(pizza.name, "Veggie Delight")
        self.assertEqual(pizza.price, Decimal('9.99')) 

    def test_topping_serializer(self):
        topping_data = {'name': "Olives"}
        serializer = Topping


class PizzaAPITest(APITestCase):

    def setUp(self):
        self.topping1 = Topping.objects.create(name="Mushrooms")
        self.topping2 = Topping.objects.create(name="Cheese")
        self.pizza_data = {
            'name': "Veggie Delight",
            'price': 9.99,
            'vegetarian': True,
            'gluten_free': False,
            'toppings': [self.topping1.id, self.topping2.id]
        }
        # Create a user and log them in
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client = APIClient()
        self.client.login(username='testuser', password='password123')  # Authenticate the client

    def test_create_pizza(self):
        response = self.client.post(reverse('pizza-list'), self.pizza_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pizza.objects.count(), 1)
        self.assertEqual(Pizza.objects.get().name, "Veggie Delight")

    def test_get_pizzas(self):
        pizza = Pizza.objects.create(name="Veggie Delight", price=9.99, vegetarian=True, gluten_free=False)
        pizza.toppings.set([self.topping1, self.topping2])

        response = self.client.get(reverse('pizza-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Veggie Delight")


class ToppingAPITest(APITestCase):

    def setUp(self):
        # Create a test user and log them in
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')

        # Create some toppings
        self.topping1 = Topping.objects.create(name="Mushrooms")
        self.topping2 = Topping.objects.create(name="Cheese")

    def test_create_topping(self):
        data = {'name': "Olives"}
        response = self.client.post(reverse('topping-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Topping.objects.count(), 3)

    def test_get_toppings(self):
        # Test retrieving the topping list
        response = self.client.get(reverse('topping-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], "Mushrooms")
        self.assertEqual(response.data[1]['name'], "Cheese")



