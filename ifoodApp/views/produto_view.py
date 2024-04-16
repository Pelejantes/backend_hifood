from rest_framework.decorators import api_view, permission_classes
# from ..permissions import Admin, Comprador, Entregador, Estabelecimento, RU_Usuario
from rest_framework.permissions import AllowAny
from ..controllers import produto_controller


@api_view(["GET"])
@permission_classes([AllowAny])
def exibir_produtos_view(request):
    return produto_controller.exibir_produtos(request)


@api_view(["GET"])
@permission_classes([AllowAny])
def exibir_produto_view(request, pk):
    return produto_controller.exibir_produto(request, pk)

