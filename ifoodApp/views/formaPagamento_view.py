from rest_framework.decorators import api_view, permission_classes
from ..permissions import Admin, Comprador, Entregador, Estabelecimento, RU_Usuario
from rest_framework.permissions import AllowAny
from ..controllers import formaPagamento_controller


@api_view(["GET"])
@permission_classes([Admin])
def exibir_formasPagamento_view(request):
    return formaPagamento_controller.exibir_formasPagamento(request)


@api_view(["GET"])
@permission_classes([RU_Usuario])
def exibir_formaPagamento_view(request, pk):
    return formaPagamento_controller.exibir_formaPagamento(request, pk)


@api_view(["POST"])
@permission_classes([RU_Usuario])
def exibir_formaPagamentoPorNome_view(request):
    return formaPagamento_controller.exibir_formaPagamentoPorNome(request)
