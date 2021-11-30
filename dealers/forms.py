from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from .models import *


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = NewUser
        fields = ['user_name', 'email', 'phone', 'is_dealer']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

    def confirm_login_allowed(self, user):
        pass
