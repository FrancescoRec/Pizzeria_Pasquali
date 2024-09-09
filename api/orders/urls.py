from django.urls import path
from . import views

urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),  # Handles placing an order
    path('customer_orders/', views.customer_orders, name='customer_orders'),  # New URL for customer orders
    path('request_order_change/<int:order_id>/', views.request_order_change, name='request_order_change'),
]

    # path('manage_orders/', views.manage_orders, name='manage_orders'),  # Employee order management
