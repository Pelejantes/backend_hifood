from rest_framework.decorators import api_view, permission_classes
from ..permissions import Admin, Comprador, Entregador, Estabelecimento, RU_Usuario
from rest_framework.permissions import AllowAny
from ..controllers import etapaPedido_controller


@api_view(["GET"])
@permission_classes([AllowAny])
def exibir_etapasPedido_view(request):
    return etapaPedido_controller.exibir_etapasPedido(request)


@api_view(["GET"])
# @permission_classes([RU_Usuario])
def exibir_etapaPedido_view(request, pk):
    return etapaPedido_controller.exibir_etapaPedido(request, pk)


@api_view(["GET"])
# @permission_classes([RU_Usuario])
def exibir_etapaPedidoPorNome_view(request):
    return etapaPedido_controller.exibir_etapaPedidoPorNome(request)
