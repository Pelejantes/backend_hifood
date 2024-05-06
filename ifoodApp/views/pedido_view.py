from rest_framework.decorators import api_view, permission_classes
from ..permissions import Admin, Comprador, Entregador, Estabelecimento, RU_Usuario
from rest_framework.permissions import AllowAny
from ..controllers import pedido_controller

@api_view(["GET"])
@permission_classes([Admin])
def exibir_pedidos_view(request):
   return pedido_controller.exibir_pedidos(request)

@api_view(["GET"])
@permission_classes([AllowAny])
def exibir_pedido_view(request, pk):
   return pedido_controller.exibir_pedido(request,pk)

@api_view(["POST"])
@permission_classes([AllowAny])
def criar_pedido_view(request):
   return pedido_controller.criar_pedido(request)

@api_view(["PUT"])
@permission_classes([AllowAny])
def editar_pedido_view(request, pk):
   return pedido_controller.editar_pedido(request,pk)

@api_view(["DELETE"])
@permission_classes([AllowAny])
def deletar_pedido_view(request, pk):
   return pedido_controller.deletar_pedido(request,pk)