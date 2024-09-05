# from allauth.account.adapter import get_adapter
# from allauth.account.utils import setup_user_email
# from dj_rest_auth.registration.serializers import RegisterSerializer
# from rest_framework import serializers
# from django.contrib.auth.models import User
# from customers.models import Customer
# from employees.models import Employee

# class CustomRegisterSerializer(RegisterSerializer):
#     is_employee = serializers.BooleanField(default=False)

#     def get_cleaned_data(self):
#         data = super().get_cleaned_data()
#         data['is_employee'] = self.validated_data.get('is_employee', False)
#         return data

#     def save(self, request):
#         user = super().save(request)
#         user.save()

#         # Create Customer or Employee profile based on 'is_employee' field
#         if self.cleaned_data.get('is_employee'):
#             Employee.objects.create(user=user)  # Create employee profile
#         else:
#             Customer.objects.create(user=user)  # Create customer profile

#         return user

