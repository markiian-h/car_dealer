# Generated by Django 3.2.6 on 2021-11-28 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0005_auto_20211126_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='model',
            name='brand_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='car.brand'),
        ),
    ]