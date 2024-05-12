from rest_framework.decorators import api_view, permission_classes
from ..permissions import Admin, Comprador, Entregador, Estabelecimento, RU_Usuario
from rest_framework.permissions import AllowAny
from ..controllers import cartao_controller

@api_view(["GET"])
@permission_classes([Admin])
def exibir_cartoes_view(request):
   return cartao_controller.exibir_cartoes(request)

@api_view(["GET"])
@permission_classes([Admin])
def exibir_cartoesUsuario_view(request,pk):
   return cartao_controller.exibir_cartoesUsuario(request,pk)

@api_view(["GET"])
@permission_classes([AllowAny])
def exibir_cartao_view(request, pk):
   return cartao_controller.exibir_cartao(request,pk)

@api_view(["POST"])
@permission_classes([AllowAny])
def criar_cartao_view(request):
   return cartao_controller.criar_cartao(request)

@api_view(["PUT"])
@permission_classes([AllowAny])
def editar_cartao_view(request, pk):
   return cartao_controller.editar_cartao(request,pk)

@api_view(["DELETE"])
@permission_classes([AllowAny])
def deletar_cartao_view(request, pk):
   return cartao_controller.deletar_cartao(request,pk)