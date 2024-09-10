from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from api.customers.models import Customer
from api.employees.models import Employee
from api.pizzas.models import Pizza
from api.orders.models import Order, OrderItem

class OrderTestCase(TestCase):
    
    def setUp(self):
        # Create a customer user
        self.customer_user = User.objects.create_user(username='testcustomer', password='password')
        self.customer = Customer.objects.create(user=self.customer_user)
        
        # Create an employee user
        self.employee_user = User.objects.create_user(username='testemployee', password='password')
        self.employee = Employee.objects.create(user=self.employee_user, is_approved=True)

        # Create some pizzas
        self.pizza1 = Pizza.objects.create(name='Margherita', price=6.00)
        self.pizza2 = Pizza.objects.create(name='Pepperoni', price=7.50)

        # URLs
        self.place_order_url = reverse('place_order')
        self.customer_orders_url = reverse('customer_orders')
        self.update_order_status_url = lambda order_id: reverse('update_order_status', args=[order_id])
        self.request_order_change_url = lambda order_id: reverse('request_order_change', args=[order_id])
    
    def test_customer_can_update_pending_order(self):
        # Create a pending order for the customer
        order = Order.objects.create(customer=self.customer, total_price=12.00, status='pending')      
        OrderItem.objects.create(order=order, pizza=self.pizza1, quantity=1)

        # Simulate customer login
        self.client.login(username='testcustomer', password='password')

        # Add print statements to see what's happening
        print(f"Order before update: {order.status}")

        # Customer changes the status of the order to 'picked up'
        response = self.client.post(self.request_order_change_url(order.id), {
            'status': 'picked up',
        })

        # Check that the customer was able to update the order status
        print(f"Response status code: {response.status_code}")
        order.refresh_from_db()
        print(f"Order after update: {order.status}")

        self.assertEqual(response.status_code, 302)  # Should redirect to customer orders
        self.assertEqual(order.status, 'picked up') 

    def test_customer_cannot_update_non_pending_order(self):
        # Create a non-pending order for the customer (approved)
        order = Order.objects.create(customer=self.customer, total_price=12.00, status='approved')      
        OrderItem.objects.create(order=order, pizza=self.pizza1, quantity=1)

        # Simulate customer login
        self.client.login(username='testcustomer', password='password')

        # Customer tries to change the status of the approved order
        response = self.client.post(self.request_order_change_url(order.id), {
            'status': 'picked up',
        })

        # Check that the customer cannot update the order status
        self.assertEqual(response.status_code, 403)  # Should return forbidden

    def test_employee_can_update_order_status(self):
        # Create a pending order for the customer
        order = Order.objects.create(customer=self.customer, total_price=12.00, status='pending')      
        OrderItem.objects.create(order=order, pizza=self.pizza1, quantity=1)

        # Simulate employee login
        self.client.login(username='testemployee', password='password')

        # Employee changes the status of the order to 'approved'
        response = self.client.post(self.update_order_status_url(order.id), {
            'status': 'picked up',
        })

        # Check that the employee was able to update the order status
        self.assertEqual(response.status_code, 302)  # Should redirect to employee dashboard
        order.refresh_from_db()
        self.assertEqual(order.status, 'picked up')  # Status should now be 'approved'

    def test_unapproved_employee_cannot_change_order_status(self):
        # Create an unapproved employee
        unapproved_employee_user = User.objects.create_user(username='unapproved_employee', password='password')
        unapproved_employee = Employee.objects.create(user=unapproved_employee_user, is_approved=False)

        # Simulate unapproved employee login
        self.client.login(username='unapproved_employee', password='password')

        # Create an order for the customer
        order = Order.objects.create(customer=self.customer, total_price=12.00, status='pending')      
        OrderItem.objects.create(order=order, pizza=self.pizza1, quantity=1)

        # Unapproved employee tries to change the status
        response = self.client.post(self.update_order_status_url(order.id), {
            'status': 'picked up',
        })

        # Check that the unapproved employee cannot update the order status
        self.assertEqual(response.status_code, 403)  # Should return forbidden

