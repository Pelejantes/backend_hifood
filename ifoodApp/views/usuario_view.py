from rest_framework.decorators import api_view, permission_classes
# from ..permissions import Professor, Admin, PodeEditarPerfil,Cadastrado,IsProfessorOrAdmin
from rest_framework.permissions import AllowAny
from ..controllers import usuario_controller


@api_view(["GET"])
# @permission_classes([IsProfessorOrAdmin])
def exibir_usuarios_view(request):
    return usuario_controller.exibir_usuarios(request)


@api_view(["GET"])
# @permission_classes([PodeEditarPerfil])
def exibir_usuario_view(request, pk):
    return usuario_controller.exibir_usuario(request, pk)


@api_view(["POST"])
# @permission_classes([AllowAny])
def criar_usuarioCompleto_view(request):
    return usuario_controller.criar_usuarioCompleto(request)


@api_view(["POST"])
# @permission_classes([AllowAny])
def criar_usuario_view(request):
    return usuario_controller.criar_usuario(request)


@api_view(["PUT"])
# @permission_classes([PodeEditarPerfil])
def inativar_usuario_view(request, pk):
    return usuario_controller.inativar_usuario(request, pk)


@api_view(["PUT"])
# @permission_classes([Admin])
def ativar_usuario_view(request, pk):
    return usuario_controller.ativar_usuario(request, pk)


@api_view(["PUT"])
# @permission_classes([PodeEditarPerfil])
def editar_usuario_view(request, pk):
    return usuario_controller.editar_usuario(request, pk)


@api_view(["DELETE"])
# @permission_classes([Admin])
def deletar_usuario_view(request, pk):
    return usuario_controller.deletar_usuario(request, pk)
