from rest_framework import permissions
from rest_framework.permissions import BasePermission


class VehiculoPermission(BasePermission):
    message = "No puede pazá makina."

    def has_permission(self, request, view):
        if request.user.is_authenticated():
            if request.method in permissions.SAFE_METHODS:
                return True
            else:
                return True #cambiar esto
