from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PizzaViewSet, ToppingViewSet  # Import your viewsets

# Create a router and register your viewsets
router = DefaultRouter()
router.register(r'', PizzaViewSet, basename='pizza')  # 'pizza-list' and 'pizza-detail'
router.register(r'', ToppingViewSet, basename='topping')  # 'topping-list' and 'topping-detail'

urlpatterns = [
    path('', include(router.urls)),  # Include the router-generated URLs
]