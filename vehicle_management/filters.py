from django_filters import CharFilter
from django_filters.rest_framework import FilterSet

from vehicle_management.models import Vehiculo


class VehiculoFilter(FilterSet):
    nombre_marca = CharFilter(field_name="marca__nombre", lookup_expr='icontains')

    class Meta:
        model = Vehiculo
        fields = ['modelo', 'color']