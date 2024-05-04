from rest_framework.decorators import api_view, permission_classes
from ..permissions import Admin, Comprador, Entregador, Estabelecimento, RU_Usuario, Logado
from rest_framework.permissions import AllowAny
from ..controllers import usuario_controller


@api_view(["GET"])
@permission_classes([Admin])
def exibir_usuarios_view(request):
    return usuario_controller.exibir_usuarios(request)


@api_view(["GET"])
@permission_classes([RU_Usuario])
def exibir_usuario_por_telefone_view(request, pk):
    return usuario_controller.exibir_usuario_por_telefone(request, pk)


@api_view(["GET"])
@permission_classes([RU_Usuario])
def exibir_usuario_view(request, pk):
    return usuario_controller.exibir_usuario(request, pk)


@api_view(["POST"])
@permission_classes([AllowAny])
def criar_usuarioCompleto_view(request):
    return usuario_controller.criar_usuarioCompleto(request)


@api_view(["POST"])
@permission_classes([AllowAny])
def criar_usuario_view(request):
    data = request.data
    return usuario_controller.criar_usuario(data)


@api_view(["PUT"])
@permission_classes([Admin])
def inativar_usuario_view(request, pk):
    return usuario_controller.inativar_usuario(request, pk)


@api_view(["PUT"])
@permission_classes([Admin])
def ativar_usuario_view(request, pk):
    return usuario_controller.ativar_usuario(request, pk)


@api_view(["PUT"])
@permission_classes([RU_Usuario])
def editar_usuario_view(request, pk):
    return usuario_controller.editar_usuario(request, pk)


@api_view(["DELETE"])
@permission_classes([Admin])
def deletar_usuario_view(request, pk):
    return usuario_controller.deletar_usuario(request, pk)
