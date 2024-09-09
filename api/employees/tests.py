from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Employee
from .serializer import EmployeeSerializer

# Employee Model Tests
class EmployeeModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='employeeuser', password='password123', email='employee@example.com')

    def test_create_employee(self):
        employee = Employee.objects.create(user=self.user, position='Manager', phone_number='987654321', is_approved=True)
        self.assertEqual(employee.user.username, 'employeeuser')
        self.assertEqual(employee.position, 'Manager')
        self.assertTrue(employee.is_approved)

# Employee Serializer Tests
class EmployeeSerializerTest(APITestCase):

    def test_create_employee(self):
        user_data = {
            'username': 'employeeuser',
            'password': 'password123',
            'email': 'employee@example.com',
        }
        employee_data = {
            'user': user_data,
            'position': 'Manager',
            'phone_number': '987654321',
            'is_approved': True,
        }

        serializer = EmployeeSerializer(data=employee_data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        employee = serializer.save()

        self.assertEqual(employee.user.username, 'employeeuser')
        self.assertEqual(employee.position, 'Manager')
        self.assertTrue(employee.is_approved)

    def test_employee_invalid_duplicate_email(self):
        # Create an existing user with the same email
        User.objects.create_user(username='otheremployee', email='employee@example.com', password='password123')

        user_data = {
            'username': 'employeeuser',
            'password': 'password123',
            'email': 'employee@example.com',
        }
        employee_data = {
            'user': user_data,
            'position': 'Manager',
            'phone_number': '987654321',
            'is_approved': True,
        }

        serializer = EmployeeSerializer(data=employee_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors['user'])

# Employee API Tests
class EmployeeAPITest(APITestCase):

    def setUp(self):
        # Create a user and authenticate
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client = APIClient()
        self.client.login(username='testuser', password='password123')  # Log in the user

    def test_create_employee(self):
        data = {
            'user': {
                'username': 'employeeuser',
                'password': 'password123',
                'email': 'employee@example.com',
            },
            'position': 'Manager',
            'phone_number': '987654321',
            'is_approved': True,
        }
        response = self.client.post('/employees/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_employees(self):
        Employee.objects.create(user=self.user, position='Manager', phone_number='987654321', is_approved=True)

        response = self.client.get('/employees/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


