from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm
from api.employees.models import Employee
from api.customers.models import Customer
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Registration View
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Create a new user
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()

            # Check if the user is registering as an Employee or Customer
            if form.cleaned_data['user_type'] == 'employee':
                Employee.objects.create(user=new_user)
            else:
                Customer.objects.create(user=new_user)

            # Automatically log in the user after registration
            login(request, new_user)

            # Redirect based on employee status
            if hasattr(new_user, 'employee') and new_user.employee.is_approved:
                return redirect('employee_dashboard')  # Redirect to employee dashboard if approved
            else:
                return redirect('dashboard')  # Redirect to normal dashboard otherwise
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

# Dashboard view (redirects employees to employee dashboard if they are approved)
@login_required
def dashboard(request):
    # Check if the user is an employee and is approved
    if hasattr(request.user, 'employee') and request.user.employee.is_approved:
        return redirect('employee_dashboard')  # Redirect to employee dashboard if approved
    return render(request, 'dashboard.html')

# Employee dashboard view
@login_required
def employee_dashboard(request):
    # Check if the user has an associated employee object
    if hasattr(request.user, 'employee'):
        if request.user.employee.is_approved:
            return render(request, 'employee_dashboard.html')
        else:
            return HttpResponse("You are still pending approval.")
    else:
        return HttpResponse("You are not approved to access this page.")
