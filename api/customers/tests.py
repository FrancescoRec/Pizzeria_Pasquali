from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Customer
from .serializer import CustomerSerializer


# Customer Model Tests
class CustomerModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='customeruser', password='password123', email='customer@example.com')

    def test_create_customer(self):
        customer = Customer.objects.create(user=self.user, phone_number='123456789', address='123 Main St')
        self.assertEqual(customer.user.username, 'customeruser')
        self.assertEqual(customer.phone_number, '123456789')
        self.assertEqual(customer.address, '123 Main St')

# Customer Serializer Tests
class CustomerSerializerTest(APITestCase):

    def test_create_customer(self):
        user_data = {
            'username': 'customeruser',
            'password': 'password123',
            'email': 'customer@example.com',
        }
        customer_data = {
            'user': user_data,
            'phone_number': '123456789',
            'address': '123 Main St',
        }

        serializer = CustomerSerializer(data=customer_data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        customer = serializer.save()

        self.assertEqual(customer.user.username, 'customeruser')
        self.assertEqual(customer.phone_number, '123456789')
        self.assertEqual(customer.address, '123 Main St')

    def test_customer_invalid_duplicate_email(self):
        # Create an existing user with the same email
        User.objects.create_user(username='otheruser', email='customer@example.com', password='password123')

        user_data = {
            'username': 'customeruser',
            'password': 'password123',
            'email': 'customer@example.com',
        }
        customer_data = {
            'user': user_data,
            'phone_number': '123456789',
            'address': '123 Main St',
        }

        serializer = CustomerSerializer(data=customer_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors['user'])

# Customer API Tests
class CustomerAPITest(APITestCase):

    def setUp(self):
        # Create a user and authenticate
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client = APIClient()
        self.client.login(username='testuser', password='password123')  # Log in the user

    def test_create_customer(self):
        data = {
            'user': {
                'username': 'customeruser',
                'password': 'password123',
                'email': 'customer@example.com',
            },
            'phone_number': '123456789',
            'address': '123 Main St',
        }
        response = self.client.post('/customers/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_customers(self):
        Customer.objects.create(user=self.user, phone_number='123456789', address='123 Main St')

        response = self.client.get('/customers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

