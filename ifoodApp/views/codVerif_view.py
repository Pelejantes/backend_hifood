from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny
from ..controllers.codVerifi_controller import enviar_codigo

@api_view(["POST"])
# @permission_classes([AllowAny])
def enviar_codigo_view(request):
    return enviar_codigo(request)