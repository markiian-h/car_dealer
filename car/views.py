from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, ListView
from django.views.generic.edit import ModelFormMixin, DeleteView

from dealers.models import NewUser
from order.models import Order
from utils import DataMixin, update_car_views, get_min_price, get_max_price, get_cars_year
from .forms import AddCarForm, CarUpdateForm
from .models import Car, Picture, Color, Model, Brand


class CarView(DataMixin, ListView):
    model = Car
    template_name = 'car/cars.html'
    queryset = Car.objects.all().select_related('picture', 'model', 'color', 'dealer')
    context_object_name = 'cars'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_context = self.get_user_context(title='Cars')
        return dict(list(context.items()) + list(base_context.items()))


class MyCarView(DataMixin, ListView):
    model = Car
    template_name = 'car/my_cars.html'
    context_object_name = 'cars'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_context = self.get_user_context(title='My cars')
        return dict(list(context.items()) + list(base_context.items()))

    def get_queryset(self):
        return Car.objects.filter(dealer=self.request.user).select_related('picture', 'model', 'color', 'dealer')


class FindCarView(DataMixin, ListView):
    model = Car
    template_name = 'car/find_car.html'
    context_object_name = 'cars'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_context = self.get_user_context(title='Find car')
        return dict(list(context.items()) + list(base_context.items()))

    def get_queryset(self):
        min_price = int(get_min_price())
        max_price = int(get_max_price())
        selected_min_price = int(self.request.GET.get('min_price'))
        selected_max_price = int(self.request.GET.get('max_price'))
        all_years = get_cars_year()
        selected_years = [int(i) for i in self.request.GET.getlist("year")]

        if not self.request.GET.getlist('year'):
            return Car.objects.filter(price__range=(selected_min_price, selected_max_price)) \
                .select_related('picture', 'model', 'color', 'dealer')

        if min_price == selected_min_price and max_price == selected_max_price:
            return Car.objects.filter(
                Q(year__in=selected_years)
            ).select_related('picture', 'model', 'color', 'dealer')
        elif min_price != selected_min_price or max_price != selected_max_price:
            return Car.objects.filter(
                Q(year__in=selected_years),
                Q(price__range=(selected_min_price, selected_max_price))
            ).select_related('picture', 'model', 'color', 'dealer')


class AboutView(DataMixin, TemplateView):
    template_name = 'car/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_context = self.get_user_context(title='About')
        return dict(list(context.items()) + list(base_context.items()))


class CarDetailView(DataMixin, DetailView):
    model = Car
    template_name = 'car/car_detail.html'
    queryset = Car.objects.select_related('model', 'color', 'picture')
    context_object_name = "car"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.dealer != self.request.user:
            context['views'] = update_car_views(self.kwargs['pk'])

        base_context = self.get_user_context(title='Car Detail')
        return dict(list(context.items()) + list(base_context.items()))


class AddCarView(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddCarForm
    model = Car

    template_name = 'car/add_car.html'
    login_url = reverse_lazy('dealers:login')

    def post(self, request, *args, **kwargs):
        user = self.request.user
        form = self.form_class(request.POST, request.FILES)
        form.instance.dealer = NewUser.objects.get(user_name=user.user_name)
        if form.is_valid():
            form.save()

        return redirect('car:cars')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_context = self.get_user_context(title='Add Car')
        return dict(list(context.items()) + list(base_context.items()))


class CarUpdateView(DataMixin, UpdateView, ModelFormMixin):
    model = Car
    form_class = CarUpdateForm
    template_name = 'car/car_edit.html'

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        model = Model.objects.get(pk=self.object.model_id)
        kwargs['initial']['brand'] = Brand.objects.get(pk=model.brand_id)
        kwargs['initial']['color'] = Color.objects.get(pk=self.object.color_id)
        kwargs['initial']['model'] = model
        picture = Picture.objects.filter(pk=self.object.picture_id)
        if picture:
            kwargs['initial']['picture'] = picture[0]
        return kwargs

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(**self.get_form_kwargs())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_context = self.get_user_context(title='Update Car')
        return dict(list(context.items()) + list(base_context.items()))


class CarDeleteView(DataMixin, DeleteView):
    model = Car
    template_name = 'car/car_delete.html'
    success_url = reverse_lazy('car:cars')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_context = self.get_user_context(title='Delete Car')
        return dict(list(context.items()) + list(base_context.items()))


class ContactView(DataMixin, TemplateView):
    template_name = 'car/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_context = self.get_user_context(title='Contact us')
        return dict(list(context.items()) + list(base_context.items()))


class HomePageView(DataMixin, TemplateView):
    template_name = 'car/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_context = self.get_user_context(title='Home page')
        return dict(list(context.items()) + list(base_context.items()))
