from rest_framework import permissions

class IsDocente(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name="Docente"):
            return True
        return False
