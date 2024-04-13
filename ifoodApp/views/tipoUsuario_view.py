from rest_framework.decorators import api_view, permission_classes
from ..permissions import Admin, Comprador, Entregador, Estabelecimento
from rest_framework.permissions import AllowAny
from ..controllers import tipoUsuario_controller
@api_view(["GET"])
@permission_classes([Admin])
def exibir_tipoUsuarios_view(request):
   return tipoUsuario_controller.exibir_tipoUsuarios(request)

@api_view(["GET"])
@permission_classes([Admin])
def exibir_tipoUsuario_view(request, pk):
   return tipoUsuario_controller.exibir_tipoUsuario(request,pk)

@api_view(["POST"])
@permission_classes([AllowAny])
def criar_tipoUsuario_view(request):
   return tipoUsuario_controller.criar_tipoUsuario(request.data)

@api_view(["PUT"])
@permission_classes([Admin])
def editar_tipoUsuario_view(request, pk):
   return tipoUsuario_controller.editar_tipoUsuario(request,pk)

@api_view(["DELETE"])
@permission_classes([Admin])
def deletar_tipoUsuario_view(request, pk):
   return tipoUsuario_controller.deletar_tipoUsuario(request,pk)