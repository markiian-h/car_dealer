from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

app_name = 'dealers'

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),

]
