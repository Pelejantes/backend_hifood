from rest_framework.decorators import api_view, permission_classes
from ..permissions import Admin, Comprador, Entregador, Estabelecimento, RU_Usuario, Logado
from rest_framework.permissions import AllowAny
from ..controllers import itemPedido_controller

@api_view(["GET"])
@permission_classes([Admin])
def exibir_itensPedidos_view(request):
   return itemPedido_controller.exibir_itemPedidos(request)

@api_view(["GET"])
@permission_classes([Logado])
def exibir_itemPedido_view(request, pk):
   return itemPedido_controller.exibir_itemPedido(request,pk)

@api_view(["POST"])
@permission_classes([Logado])
def criar_itemPedido_view(request):
   return itemPedido_controller.criar_itemPedido(request)

# @api_view(["PUT"])
# @permission_classes([RU_Usuario])
# def editar_itemPedido_view(request, pk):
#    return itemPedido_controller.editar_itemPedido(request,pk)

# @api_view(["DELETE"])
# @permission_classes([RU_Usuario])
# def deletar_itemPedido_view(request, pk):
#    return itemPedido_controller.deletar_itemPedido(request,pk)