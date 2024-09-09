from django import forms
from django.contrib.auth.models import User
from api.employees.models import Employee
from api.customers.models import Customer

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=[('employee', 'Employee'), ('customer', 'Customer')],
                                  widget=forms.HiddenInput(),  # Hidden input for the field
                                  label="")

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        }
        labels = {
            'username': 'Username',
            'email': 'Email address',
        }
        help_texts = {
            'username': None,  # Removes the help text for the username field
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password2']

