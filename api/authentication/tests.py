import pytest
from django.urls import reverse
from django.contrib.auth.models import User
import html

@pytest.mark.django_db
class TestRegistrationView:

    def test_registration_invalid_email(self, client):
        data = {
            'username': 'invalidemail',
            'password': 'password123',
            'password_confirm': 'password123',
            'email': 'bademail',
            'user_type': 'customer'
        }
        response = client.post(reverse('register'), data)
        assert response.status_code == 200  # No redirect, form should re-render with errors
        assert 'Enter a valid email address.' in str(response.content)

    def test_registration_password_mismatch(self, client):
        data = {
            'username': 'testpasswordmismatch',
            'password': 'password123',
            'password2': 'password456',  # Passwords don't match
            'email': 'user@example.com',
            'user_type': 'customer'
        }
        response = client.post(reverse('register'), data)
        content = html.unescape(response.content.decode('utf-8'))
        
        assert response.status_code == 200  # No redirect, form should re-render with errors
        assert "Passwords don't match." in content

    def test_registration_existing_username(self, client):
        # First, create a user
        User.objects.create_user(username='existinguser', password='password123', email='existing@example.com')

        data = {
            'username': 'existinguser',
            'password': 'password123',
            'password_confirm': 'password123',
            'email': 'newuser@example.com',
            'user_type': 'customer'
        }
        response = client.post(reverse('register'), data)
        assert response.status_code == 200  # No redirect, form should re-render with errors
        assert 'A user with that username already exists.' in str(response.content)


# Create your tests here.
