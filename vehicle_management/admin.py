from django.contrib import admin

from .models import Vehiculo, Marca

# Register your models here.
admin.site.register(Vehiculo)
admin.site.register(Marca)