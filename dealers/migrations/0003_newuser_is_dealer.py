# Generated by Django 3.2.6 on 2021-11-25 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealers', '0002_auto_20211122_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='is_dealer',
            field=models.BooleanField(default=False),
        ),
    ]