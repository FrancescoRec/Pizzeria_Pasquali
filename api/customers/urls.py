from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet 

# Create a router and register your viewsets
router = DefaultRouter()
router.register(r'', CustomerViewSet, basename='customer')  
urlpatterns = [
    path('', include(router.urls)),  
]