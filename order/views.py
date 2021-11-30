from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, TemplateView

from car.models import Car
from order.forms import OrderForm
from order.models import Order
from utils import DataMixin


class CreateOrderView(DataMixin, CreateView):
    model = Order
    template_name = 'add_order.html'
    form_class = OrderForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.car = Car.objects.get(pk=self.kwargs.get('pk'))
        form.instance.user = self.request.user
        form.instance.user_number = self.request.user.phone
        form.instance.user_email = self.request.user.email
        order = Order.objects.filter(car__pk=self.kwargs.get('pk'), user=self.request.user)
        if order:
            return redirect('order:failure')
        if form.is_valid():
            form.save()
        return redirect('car:cars')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_context = self.get_user_context(title='Add orders')
        return dict(list(context.items()) + list(base_context.items()))


class OrderListView(DataMixin, ListView):
    model = Order
    template_name = 'orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).select_related('user', 'car', 'car__dealer', 'car__model',
                                                                           'car__model__brand')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_context = self.get_user_context(title='Orders')
        return dict(list(context.items()) + list(base_context.items()))


class FailureAddOrderView(DataMixin, TemplateView):
    template_name = 'failure_add_order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_context = self.get_user_context(title='Failure')
        return dict(list(context.items()) + list(base_context.items()))


def failure_add_order(request):
    return render(request, 'failure_add_order.html')
