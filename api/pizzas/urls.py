from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PizzaViewSet, ToppingViewSet  # Import your viewsets

# Create a router and register your viewsets
router = DefaultRouter()
router.register(r'pizzas', PizzaViewSet, basename='pizza')  # Registers 'pizzas/' path for PizzaViewSet
router.register(r'toppings', ToppingViewSet, basename='topping') 

urlpatterns = [
    path('', include(router.urls)),  # Include the router-generated URLs
]