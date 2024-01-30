from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    #ruta para establecer idioma
    path('', include('vehicle_management.urls'))
]
