from rest_framework import permissions
from rest_framework.permissions import BasePermission


class VehiculoPermission(BasePermission):
    message = "No tienes permisos"

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if request.user.is_authenticated:
                return True
            else:
                return False

#class ReadOnlyPermission(permissions.BasePermission):
   # def has_permission(self, request, view):
   #     return request.method in permissions.SAFE_METHODS
