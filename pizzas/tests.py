from django.test import TestCase

# Create your tests here.
def test1():
    assert 1+1 == 2






# from django.test import TestCase

# # Create your tests here.

# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from .models import Pizza, Topping
# from .serializer import PizzaSerializer, ToppingSerializer

# class PizzaTests(APITestCase):
#     def test_create_pizza(self):
#         """
#         Ensure we can create a new pizza object.
#         """
#         url = reverse('pizza-list')
#         data = {
#             'name': 'Margherita',
#             'price': '9.99',
#             'vegetarian': True,
#             'gluten_free': False,
#             'toppings': []
#         }

#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Pizza.objects.count(), 1)
#         self.assertEqual(Pizza.objects.get().name, 'Margherita')

#     def test_create_topping(self):
#         """
#         Ensure we can create a new topping object.
#         """
#         url = reverse('topping-list')
#         data = {
#             'name': 'Mushrooms'
#         }

#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#         self.assertEqual(Topping.objects.count(), 1)
#         self.assertEqual(Topping.objects.get().name, 'Mushrooms')

#     def test_create_pizza_with_toppings(self):
#         """
#         Ensure we can create a new pizza object with toppings.
#         """
#         topping = Topping.objects.create(name='Mushrooms')
#         url = reverse('pizza-list')
#         data = {
#             'name': 'Margherita',
#             'price': '9.99',
#             'vegetarian': True,
#             'gluten_free': False,
#             'toppings': [topping.id]
#         }

#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Pizza.objects.count(), 1)

#         pizza = Pizza.objects.get()
#         self.assertEqual(pizza.name, 'Margherita')
#         self.assertEqual(pizza.toppings.count(), 1)
#         self.assertEqual(pizza.toppings.get().name, 'Mushrooms')


