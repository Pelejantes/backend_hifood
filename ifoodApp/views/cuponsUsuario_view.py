from rest_framework.decorators import api_view, permission_classes
from ..permissions import Admin, R_CuponsUsuario, Logado
from ..controllers import cuponsUsuario_controller


@api_view(["GET"])
@permission_classes([Logado])
def exibir_cuponsUsuario_view(request):
    return cuponsUsuario_controller.exibir_cuponsUsuario(request)


@api_view(["GET"])
@permission_classes([R_CuponsUsuario])
def exibir_cupomUsuario_view(request, pk):
    return cuponsUsuario_controller.exibir_cupomUsuario(request, pk)

