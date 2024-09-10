# from django.test import TestCase
# from django.urls import reverse
# from django.contrib.auth.models import User
# from api.customers.models import Customer
# from api.employees.models import Employee
# from api.pizzas.models import Pizza
# from api.orders.models import Order, OrderItem

# class OrderTestCase(TestCase):
    
#     def setUp(self):
#         # Create a customer user
#         self.customer_user = User.objects.create_user(username='testcustomer', password='password')
#         self.customer = Customer.objects.create(user=self.customer_user)
        
#         # Create an employee user
#         self.employee_user = User.objects.create_user(username='testemployee', password='password')
#         self.employee = Employee.objects.create(user=self.employee_user, is_approved=True)

#         # Create some pizzas
#         self.pizza1 = Pizza.objects.create(name='Margherita', price=6.00)
#         self.pizza2 = Pizza.objects.create(name='Pepperoni', price=7.50)

#         # Login URLs and other URLs
#         self.place_order_url = reverse('place_order')
#         self.customer_orders_url = reverse('customer_orders')
#         self.update_order_status_url = lambda order_id: reverse('update_order_status', args=[order_id])
    
#     def test_place_order(self):
#         # Simulate customer login
#         self.client.login(username='testcustomer', password='password')

#         # Simulate placing an order with pizzas
#         response = self.client.post(self.place_order_url, {
#             f'pizza_{self.pizza1.id}': 'on',  # Selecting pizza 1
#             f'quantity_{self.pizza1.id}': '2',  # Quantity 2
#             f'pizza_{self.pizza2.id}': 'on',  # Selecting pizza 2
#             f'quantity_{self.pizza2.id}': '1',  # Quantity 1
#         })
        
#         # Check that the order is placed and customer is redirected to order history
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, self.customer_orders_url)

#         # Check if the order and order items were created
#         order = Order.objects.get(customer=self.customer)
#         self.assertEqual(order.items.count(), 2)  # Two pizzas should be in the order
#         self.assertEqual(order.total_price, 19.50)  # Total price should be 2 * 6.00 + 7.50

#     def test_view_customer_orders(self):
#         # Create an order for the customer
#         order = Order.objects.create(customer=self.customer, total_price=12.00)
#         OrderItem.objects.create(order=order, pizza=self.pizza1, quantity=1)

#         # Simulate customer login
#         self.client.login(username='testcustomer', password='password')

#         # View customer orders
#         response = self.client.get(self.customer_orders_url)
        
#         # Check the response and make sure the order is displayed
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Order #')
#         self.assertContains(response, 'Margherita')

#     def test_update_order_status_by_employee(self):
#         # Create an order for the customer
#         order = Order.objects.create(customer=self.customer, total_price=12.00, status='pending')
#         OrderItem.objects.create(order=order, pizza=self.pizza1, quantity=1)

#         # Simulate employee login
#         self.client.login(username='testemployee', password='password')

#         # Update the order status to 'approved'
#         response = self.client.post(self.update_order_status_url(order.id), {
#             'status': 'approved',
#         })

#         # Check if the status was updated
#         self.assertEqual(response.status_code, 302)
#         order.refresh_from_db()
#         self.assertEqual(order.status, 'approved')

#     def test_employee_cannot_see_orders_if_not_approved(self):
#         # Create a new employee but do not approve them
#         unapproved_employee_user = User.objects.create_user(username='unapproved_employee', password='password')
#         unapproved_employee = Employee.objects.create(user=unapproved_employee_user, is_approved=False)

#         # Simulate unapproved employee login
#         self.client.login(username='unapproved_employee', password='password')

#         # Try to access employee dashboard
#         response = self.client.get(reverse('employee_dashboard'))
        
#         # Check that the unapproved employee cannot access the employee dashboard
#         self.assertEqual(response.status_code, 403)
#         self.assertContains(response, "You do not have permission to access this page.")

#     def test_customer_cannot_update_order_status(self):
#         # Create an order for the customer
#         order = Order.objects.create(customer=self.customer, total_price=12.00, status='pending')
#         OrderItem.objects.create(order=order, pizza=self.pizza1, quantity=1)

#         # Simulate customer login
#         self.client.login(username='testcustomer', password='password')

#         # Try to update the order status as a customer
#         response = self.client.post(self.update_order_status_url(order.id), {
#             'status': 'approved',
#         })

#         # Check that the customer cannot update the order status
#         self.assertEqual(response.status_code, 403)
