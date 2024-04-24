from rest_framework import permissions
from .models import TipoUsuario, CuponsUsuario
# RU -> READ / UPDATE


class Logado(permissions.BasePermission):
    def has_permission(self, request, view):
        return True if hasattr(request, 'auth_payload') else False


class RU_Usuario(permissions.BasePermission):
    def has_permission(self, request, view):
        tipo_usuario_id = request.auth_payload.get(
            "tipoUsuarioId") if hasattr(request, 'auth_payload') else None
        try:
            nomeTipoUsuario = TipoUsuario.get(
                tipoUsuarioId=tipo_usuario_id).nomeTipoUsuario
        except AssertionError:
            return "Tipo de Usuario não foi registrado."
        usuarioId = request.auth_payload.get("usuarioId") if hasattr(
            request, 'auth_payload') else None
        url_pk = view.kwargs.get('pk')

        if nomeTipoUsuario == "Admin".lower():
            return True  # Admin tem acesso a todas as informações

        # Usuários que só podem interagir com os próprios dados.
        if nomeTipoUsuario == "Comprador".lower() and url_pk == usuarioId:
            return True

        if nomeTipoUsuario == "Entregador".lower() and url_pk == usuarioId:
            return True

        if nomeTipoUsuario == "Estabelecimento".lower() and url_pk == usuarioId:
            return True

        # Se não for nenhum dos casos acima, negar acesso
        return False


class R_CuponsUsuario(permissions.BasePermission):
    def has_permission(self, request, view):
        # usuario pode ver UNICAMENTE seus próprios cupons
        cupomUsuarioId = view.kwargs.get('pk')
        if CuponsUsuario.objects.filter(cuponsUsuarioId=cupomUsuarioId):
            cupomUsuario = CuponsUsuario.objects.get(
                cuponsUsuarioId=cupomUsuarioId)
        else:
            return f"Cupom {cupomUsuarioId} do usuário não encontrado."
        
        usuarioId = request.auth_payload.get("usuarioId") if hasattr(
            request, 'auth_payload') else None
        
        try:
            if usuarioId:
                if cupomUsuario.usuarioId.usuarioId == int(usuarioId):
                    return True
        except AssertionError:
            return f'Usuário com id {usuarioId} não registrado.'
        return None


class Admin(permissions.BasePermission):
    def has_permission(self, request, view):
        if hasattr(request, 'auth_payload') and request.auth_payload:
            payload = request.auth_payload
            if payload.get("tipoUsuarioId") == "1":
                return True
        return False


class Comprador(permissions.BasePermission):
    def has_permission(self, request, view):
        if hasattr(request, 'auth_payload') and request.auth_payload:
            payload = request.auth_payload
            if payload.get("tipoUsuarioId") == "2":
                return True
        return False


class Entregador(permissions.BasePermission):
    def has_permission(self, request, view):
        if hasattr(request, 'auth_payload') and request.auth_payload:
            payload = request.auth_payload
            if payload.get("tipoUsuarioId") == "3":
                return True
        return False


class Estabelecimento(permissions.BasePermission):
    def has_permission(self, request, view):
        if hasattr(request, 'auth_payload') and request.auth_payload:
            payload = request.auth_payload
            if payload.get("tipoUsuarioId") == "4":
                return True
        return False


class Logado(permissions.BasePermission):
    def has_permission(self, request, view):
        if hasattr(request, 'auth_payload') and request.auth_payload:
            payload = request.auth_payload
            if payload.get("tipoUsuarioId"):
                return True
        return False
