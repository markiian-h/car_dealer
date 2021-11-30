from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import *

app_name = 'order'

urlpatterns = [
    path('orders/', OrderListView.as_view(), name='orders'),
    path('create_order/<int:pk>', CreateOrderView.as_view(), name='create_orders'),
    path('failure/', FailureAddOrderView.as_view(), name='failure'),

]
