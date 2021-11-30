from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Car)
admin.site.register(Color)
admin.site.register(Model)
admin.site.register(Brand)
admin.site.register(Picture)
admin.site.register(Property)
admin.site.register(PropertyCategory)