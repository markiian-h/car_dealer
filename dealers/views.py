from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from dealers.forms import RegisterUserForm, LoginForm
from dealers.models import NewUser
from utils import DataMixin

sidebar = [
    {'title': 'Cars', 'url_name': 'cars'}
]
menu = [{'title': 'About', 'url_name': 'about'},
        {'title': 'Add new car', 'url_name': 'add_car'},
        {'title': 'Contact us', 'url_name': 'contact'},
        ]


def index(request):
    return HttpResponse('Hello')


class RegisterUserView(DataMixin, CreateView):
    model = NewUser
    form_class = RegisterUserForm
    template_name = 'dealers/register.html'
    success_url = reverse_lazy('car:cars')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_context = self.get_user_context(title='Registration')
        return dict(list(context.items()) + list(base_context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('car:cars')


class LoginUserView(DataMixin, LoginView):
    authentication_form = LoginForm
    template_name = 'dealers/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_context = self.get_user_context(title='Login')
        return dict(list(context.items()) + list(base_context.items()))

    def get_success_url(self):
        return reverse('car:cars')


def logout_user(request):
    logout(request)
    return redirect('dealers:login')
