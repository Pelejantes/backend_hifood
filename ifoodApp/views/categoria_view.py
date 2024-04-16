from rest_framework.decorators import api_view, permission_classes
# from ..permissions import Admin, Comprador, Entregador, Estabelecimento, RU_Usuario
from rest_framework.permissions import AllowAny
from ..controllers import categoria_controller


@api_view(["GET"])
@permission_classes([AllowAny])
def exibir_categorias_view(request):
    return categoria_controller.exibir_categorias(request)


@api_view(["GET"])
@permission_classes([AllowAny])
def exibir_categoria_view(request, pk):
    return categoria_controller.exibir_categoria(request, pk)

