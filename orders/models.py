from django.db import models
# from django.contrib.auth.models import User  
# from pizzas.models import Pizza  

# class Order(models.Model):
#     STATUS_CHOICES = [
#         ('pending', 'Pending'),
#         ('in_progress', 'In Progress'),
#         ('completed', 'Completed'),
#         ('cancelled', 'Cancelled'),
#     ]

#     customer = models.ForeignKey(User, on_delete=models.CASCADE)  
#     pizzas = models.ManyToManyField('Pizza', through='OrderItem')  
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
#     is_delivery = models.BooleanField(default=True)
#     delivery_address = models.CharField(max_length=255, blank=True, null=True)
#     total_amount = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"Order #{self.id} by {self.customer.username}"

# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)  
#     pizza = models.ForeignKey('Pizza', on_delete=models.CASCADE)  
#     quantity = models.IntegerField(default=1)  
#     price = models.DecimalField(max_digits=5, decimal_places=2)  

#     def __str__(self):
#         return f"{self.quantity} x {self.pizza.name} for Order #{self.order.id}"

#     def get_total_price(self):
#         """Calculate total price for this order item"""
#         return self.quantity * self.price
