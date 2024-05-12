from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from ..controllers.pagamento_controller import efetuarPagamento


@api_view(["POST"])
@permission_classes([AllowAny])
def efetuarPagamento_view(request):
    return efetuarPagamento(request)
