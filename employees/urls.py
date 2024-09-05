from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet 

# Create a router and register your viewsets
router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employee')  
urlpatterns = [
    path('', include(router.urls)),  
]