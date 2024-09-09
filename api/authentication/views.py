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

            # Redirect to dashboard after successful registration
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

# Dashboard View (handles both employees and customers)
@login_required
def dashboard(request):
    # Check if the user has an associated employee object
    if hasattr(request.user, 'employee'):
        if request.user.employee.is_approved:
            return redirect('employee_dashboard')  # Redirect to employee dashboard if approved
        else:
            return HttpResponse("You are still pending approval.")  # Message for unapproved employees
    else:
        # If the user is not an employee (they are a customer), render the customer dashboard
        return render(request, 'dashboard.html')

# Employee Dashboard View
@login_required
def employee_dashboard(request):
    return render(request, 'employee_dashboard.html')
