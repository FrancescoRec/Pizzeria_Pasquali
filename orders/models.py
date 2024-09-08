# from django.db import models
# from pizzas.models import Pizza
# from customers.models import Customer
# from django.contrib.auth.models import User

# class Order(models.Model):
#     STATUS_CHOICES = [
#         ('pending', 'Pending'),
#         ('in_progress', 'In Progress'),
#         ('completed', 'Completed'),
#         ('cancelled', 'Cancelled'),
#     ]

#     order_id = models.AutoField(primary_key=True)
#     customer = models.ForeignKey(User, on_delete=models.CASCADE)  
#     pizzas = models.ManyToManyField(Pizza, through='OrderItem')  
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
#     is_delivery = models.BooleanField(default=True)
#     address = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
#     total_amount = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     delivered_at = models.DateTimeField(null=True, blank=True)  

#     def __str__(self):
#         return f"Order #{self.id} by {self.customer.username}"

#     def calculate_total(self):
#         """ Calculate the total of the order by summing the total of each OrderItem """
#         total = sum(item.get_total_price() for item in self.orderitem_set.all())
#         return total

#     def save(self, *args, **kwargs):
#         """ Update the total before saving the order """
#         self.total_amount = self.calculate_total()  
#         super(Order, self).save(*args, **kwargs)


# class OrderItem(models.Model):
#     #make a primary key for the order item
#     order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
#     pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)  
#     quantity = models.IntegerField(default=1)  
#     price = models.DecimalField(max_digits=5, decimal_places=2, blank=True)  

#     def __str__(self):
#         return f"{self.quantity} x {self.pizza.name} for Order #{self.order.id}"

#     def get_total_price(self):
#         """Calculate the total price of the order item"""
#         return self.quantity * self.price
    
#     def save(self, *args, **kwargs):
#         """Salva il prezzo corrente della pizza nel campo 'price' di OrderItem"""
#         if not self.price:  
#             self.price = self.pizza.price  
#         super(OrderItem, self).save(*args, **kwargs)
