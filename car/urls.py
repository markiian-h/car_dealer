from django.contrib.auth.decorators import login_required
from django.urls import path, re_path

from .views import *

app_name = 'car'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('find_car/', FindCarView.as_view(), name='find_car'),
    path('cars/', CarView.as_view(), name='cars'),
    path('my_cars/', MyCarView.as_view(), name='my_cars'),
    path('about/', AboutView.as_view(), name='about'),
    path('add_car/', AddCarView.as_view(), name='add_car'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('car/<int:pk>', CarDetailView.as_view(), name='car'),
    path('car/<int:pk>/edit/', login_required(CarUpdateView.as_view()), name='car_edit'),
    path('car/<int:pk>/delete/', login_required(CarDeleteView.as_view()), name='car_delete'),
]
