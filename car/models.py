from django.conf import settings
from django.db import models
from django.urls import reverse


class Car(models.Model):
    ENGINE_CHOICES = (
        ('e', 'Electric'),
        ('d', 'Diesel'),
        ('g1', 'Gasoline'),
        ('g2', 'Gas'),
    )

    model = models.ForeignKey(to='Model', on_delete=models.CASCADE, related_name='cars')
    color = models.ForeignKey(to='Color', on_delete=models.CASCADE)
    dealer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cars')
    picture = models.ForeignKey(to='Picture', on_delete=models.SET_NULL, null=True, blank=True)
    is_published = models.BooleanField(default=True)
    price = models.IntegerField()
    year = models.IntegerField(null=True)
    engine_type = models.CharField(max_length=2, choices=ENGINE_CHOICES)
    capacity = models.IntegerField()
    gear_case = models.IntegerField()
    doors = models.IntegerField()
    property = models.ManyToManyField('Property', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.model.name

    def get_absolute_url(self):
        return reverse('car:car', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_at']


class Model(models.Model):
    name = models.CharField(max_length=64, unique=True)
    brand = models.ForeignKey(to='Brand', on_delete=models.CASCADE, related_name='models')

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Picture(models.Model):
    url = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Picture')
    meta_data = models.TextField()

    def __str__(self):
        return f'{self.url}'


class Property(models.Model):
    category = models.ForeignKey(to='PropertyCategory', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class PropertyCategory(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return self.category
