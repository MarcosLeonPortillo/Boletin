#from django.contrib.auth.models import Group, User
#from django_filters.rest_framework import DjangoFilterBackend
#from rest_framework import permissions, viewsets, filters
#from rest_framework.decorators import action
#from rest_framework.generics import get_object_or_404
#from rest_framework.response import Response

#from .filters import VehiculoFilter
#from .models import Vehiculo, Marca
#from .permissions import VehiculoPermission
#from .serializers import GroupSerializer, UserSerializer, VehiculoSerializer, MarcaSerializer


#class UserViewSet(viewsets.ModelViewSet):
    #"""
    #API endpoint that allows users to be viewed or edited.
#  """
    #queryset = User.objects.all().order_by('-date_joined')
    # serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]


#class GroupViewSet(viewsets.ModelViewSet):
# """
    #API endpoint that allows groups to be viewed or edited.
   # """
    # queryset = Group.objects.all()
    # serializer_class = GroupSerializer
    #permission_classes = [permissions.IsAuthenticated]


#class VehiculoViewSet(viewsets.ModelViewSet):
    #queryset = Vehiculo.objects.all()
    #serializer_class = VehiculoSerializer
    #permission_classes = [VehiculoPermission]
    #filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    #  ordering_fields = ['fecha_fabricacion']
    # ordering = ['fecha_fabricacion']  # Default ordering
    #filterset_class = VehiculoFilter


#class MarcaViewSet(viewsets.ModelViewSet):
#  queryset = Marca.objects.all()
    # serializer_class = MarcaSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['nombre']

    # @action(detail=True, methods=['GET'])
    #   def lista_por_marca(self, request, pk):


#  marca = get_object_or_404(Marca, pk=pk)
        #   vehiculos = Vehiculo.objects.filter(marca__nombre=marca.nombre)
        #   serializer = VehiculoSerializer(vehiculos, many=True, context={'request': self.request})
        # response = Response(serializer.data)
        #  return response



from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Marca, Vehiculo
from .serializers import MarcaSerializer, VehiculoSerializer
from .permissions import VehiculoPermission


class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    permission_classes = [VehiculoPermission]
    filter_backends = [DjangoFilterBackend]


class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [VehiculoPermission]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['marca']
    ordering_fields = ['fecha_fabricacion']