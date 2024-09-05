from rest_framework import viewsets
from .models import Customer
from .serializer import CustomerSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

