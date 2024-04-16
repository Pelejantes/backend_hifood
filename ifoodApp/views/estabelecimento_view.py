from rest_framework.decorators import api_view, permission_classes
# from ..permissions import Admin, Comprador, Entregador, Estabelecimento, RU_Usuario
from rest_framework.permissions import AllowAny
from ..controllers import estabelecimento_controller


@api_view(["GET"])
@permission_classes([AllowAny])
def exibir_estabelecimentos_view(request):
    return estabelecimento_controller.exibir_estabelecimentos(request)


@api_view(["GET"])
@permission_classes([AllowAny])
def exibir_estabelecimento_view(request, pk):
    return estabelecimento_controller.exibir_estabelecimento(request, pk)

