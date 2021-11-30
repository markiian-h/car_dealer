from django.db import models

# Create your models here.
from car.models import Car
from car_shop import settings


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    user_number = models.CharField(max_length=20)
    user_email = models.EmailField(null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
