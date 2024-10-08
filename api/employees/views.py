from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Employee
from .serializer import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

