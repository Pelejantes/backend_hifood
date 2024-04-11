from rest_framework import permissions
from .models import TipoUsuario
# RU -> READ / UPDATE
class RU_Usuario(permissions.BasePermission):
    def has_permission(self, request, view):
        tipo_usuario_id = request.auth_payload.get("tipoUsuarioId") if hasattr(request, 'auth_payload') else None
        try:
            nomeTipoUsuario = TipoUsuario.get(tipoUsuarioId=tipo_usuario_id).nomeTipoUsuario
        except AssertionError:
            return "Tipo de Usuario não foi registrado."
        usuarioId = request.auth_payload.get("usuarioId") if hasattr(request, 'auth_payload') else None
        url_pk = view.kwargs.get('pk')  # Obtém a PK da URL
        # Verificações de permissão para Admin
        if nomeTipoUsuario == "Admin".lower():
            return True  # Admin tem acesso total

        # Verificações de permissão para Comprador
        if nomeTipoUsuario == "Comprador".lower() and url_pk == usuarioId:
            return True  # Comprador tem acesso a listagem, leitura e criação

        # Verificações de permissão para Entregador
        if nomeTipoUsuario == "Entregador".lower() and url_pk == usuarioId:
            return True  # Entregador tem acesso a leitura e atualização

        # Verificações de permissão para Estabelecimento
        if nomeTipoUsuario == "Estabelecimento".lower() and url_pk == usuarioId:
            return True  # Estabelecimento tem acesso a listagem e criação

        # Se não for nenhum dos casos acima, negar acesso
        return False


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

class Logado(permissions.BasePermission):
    def has_permission(self, request, view):
        if hasattr(request, 'auth_payload') and request.auth_payload:
            payload = request.auth_payload
            if payload.get("tipoUsuarioId"):
                return True
        return False

