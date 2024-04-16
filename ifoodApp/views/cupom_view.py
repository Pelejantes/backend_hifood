from rest_framework.decorators import api_view, permission_classes
# from ..permissions import Admin, Comprador, Entregador, Estabelecimento, RU_Usuario
from rest_framework.permissions import AllowAny
from ..controllers import cupom_controller


@api_view(["GET"])
@permission_classes([AllowAny])
def exibir_cupons_view(request):
    return cupom_controller.exibir_cupons(request)


@api_view(["GET"])
@permission_classes([AllowAny])
def exibir_cupom_view(request, pk):
    return cupom_controller.exibir_cupom(request, pk)

