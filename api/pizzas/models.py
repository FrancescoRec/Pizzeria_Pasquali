from django.db import models


class Topping(models.Model):
    name = models.CharField(max_length=100, unique=True)  

    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    toppings = models.ManyToManyField(Topping)
    vegetarian = models.BooleanField(default=False)
    gluten_free = models.BooleanField(default=False)

    def __str__(self):
        return self.name
