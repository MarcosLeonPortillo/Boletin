from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, generics
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from vehicle_management.models import Vehiculo, Marca
from vehicle_management.permissions import VehiculoPermission
from vehicle_management.serializers import GroupSerializer, UserSerializer, VehiculoSerializer, MarcaSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [VehiculoPermission]


class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['GET'])
    def lista_por_marca(self, request, pk):
        marca = get_object_or_404(Marca, pk=1)
        vehiculos = Vehiculo.objects.filter(marca__nombre=marca.nombre)
        serializer = VehiculoSerializer(vehiculos, many=True, context={'request': self.request})
        response = Response(serializer.data)
        return response
