from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

router = DefaultRouter()
router.register(r'', OrderViewSet, basename='order')


urlpatterns = [
    path('', include(router.urls)),
    path('place_order/', views.place_order, name='place_order'),  # Handles placing an order
    path('customer_orders/', views.customer_orders, name='customer_orders'),  # New URL for customer orders
    path('request_order_change/<int:order_id>/', views.request_order_change, name='request_order_change'),
    path('orders/update_status/<int:order_id>/', views.update_order_status, name='update_order_status'),
]


