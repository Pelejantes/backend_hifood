from rest_framework.decorators import api_view, permission_classes
from ..permissions import Admin, Comprador, Entregador, Estabelecimento, RU_Usuario
from rest_framework.permissions import AllowAny
from ..controllers import endereco_controller


@api_view(["GET"])
@permission_classes([Admin])
def exibir_enderecos_view(request):
    return endereco_controller.exibir_enderecos(request)


@api_view(["GET"])
@permission_classes([AllowAny])
def exibir_endereco_view(request, pk):
    return endereco_controller.exibir_endereco(request, pk)


@api_view(["POST"])
@permission_classes([AllowAny])
def criar_endereco_view(request):
    return endereco_controller.criar_endereco(request)


@api_view(["PUT"])
@permission_classes([AllowAny])
def editar_endereco_view(request, pk):
    return endereco_controller.editar_endereco(request, pk)


@api_view(["DELETE"])
@permission_classes([AllowAny])
def deletar_endereco_view(request, pk):
    return endereco_controller.deletar_endereco(request, pk)
