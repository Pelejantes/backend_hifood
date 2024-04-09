from rest_framework import permissions


class Admin(permissions.BasePermission):
    def has_permission(self, request, view):
        if hasattr(request, 'auth_payload') and request.auth_payload:
            payload = request.auth_payload
            if payload.get("tipoUsuarioId") == "0":
                return True
        return False


class Comprador(permissions.BasePermission):
    def has_permission(self, request, view):
        if hasattr(request, 'auth_payload') and request.auth_payload:
            payload = request.auth_payload
            if payload.get("tipoUsuarioId") == "1":
                return True
        return False


class Entregador(permissions.BasePermission):
    def has_permission(self, request, view):
        if hasattr(request, 'auth_payload') and request.auth_payload:
            payload = request.auth_payload
            if payload.get("tipoUsuarioId") == "2":
                return True
        return False


class Estabelecimento(permissions.BasePermission):
    def has_permission(self, request, view):
        if hasattr(request, 'auth_payload') and request.auth_payload:
            payload = request.auth_payload
            if payload.get("tipoUsuarioId") == "3":
                return True
        return False
