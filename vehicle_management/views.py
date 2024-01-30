from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response

from vehicle_management.models import Vehiculo, Marca
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
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['GET'])
    def lista_por_marca(self, request):
        marca = Marca.objects.all().first()
        vehiculos = self.queryset.filter(marca__nombre=marca.nombre)
        #serializer = self.get_serializer(data=vehiculos, many=True)
        serializer = self.serializer_class(vehiculos, many=True, context={'request': self.request})
        response = Response(serializer.data)
        #if serializer.is_valid():
        #    response = Response(serializer.validated_data)
        #else:
        #    print(serializer.errors)
        #    response = Response({"No tira": "unclucky"})
        return response


class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    permission_classes = [permissions.IsAuthenticated]
