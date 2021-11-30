# Generated by Django 3.2.6 on 2021-11-21 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='dealers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='car.model'),
        ),
        migrations.AddField(
            model_name='car',
            name='picture',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='car.picture'),
        ),
        migrations.AddField(
            model_name='car',
            name='property',
            field=models.ManyToManyField(blank=True, to='car.Property'),
        ),
    ]
