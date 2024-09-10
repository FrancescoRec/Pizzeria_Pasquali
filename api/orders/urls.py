from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

# Set up DRF router for API views
router = DefaultRouter()
router.register(r'', OrderViewSet, basename='order')  # Add 'api' prefix for clarity

urlpatterns = [
    path('', include(router.urls)),

    # Custom HTML views
    path('place_order/', views.place_order, name='place_order'),  # Handles placing an order
    path('customer_orders/', views.customer_orders, name='customer_orders'),  # Customer orders view
    path('request_order_change/<int:order_id>/', views.request_order_change, name='request_order_change'),
    path('update_status/<int:order_id>/', views.update_order_status, name='update_order_status'),
]



