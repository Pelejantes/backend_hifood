from rest_framework.decorators import api_view, permission_classes
# from ..permissions import Professor, Admin, PodeEditarPerfil,Cadastrado,IsProfessorOrAdmin
from rest_framework.permissions import AllowAny
from ..controllers import enderecoEntrega_controller

@api_view(["GET"])
# @permission_classes([IsProfessorOrAdmin])
def exibir_enderecosEntrega_view(request):
   return enderecoEntrega_controller.exibir_enderecosEntrega(request)

@api_view(["GET"])
# @permission_classes([PodeEditarPerfil])
def exibir_enderecoEntrega_view(request, pk):
   return enderecoEntrega_controller.exibir_enderecoEntrega(request,pk)

@api_view(["POST"])
# @permission_classes([AllowAny])
def criar_enderecoEntrega_view(request):
   return enderecoEntrega_controller.criar_enderecoEntrega(request)

@api_view(["PUT"])
# @permission_classes([PodeEditarPerfil])
def editar_enderecoEntrega_view(request, pk):
   return enderecoEntrega_controller.editar_enderecoEntrega(request,pk)

@api_view(["DELETE"])
# @permission_classes([Admin])
def deletar_enderecoEntrega_view(request, pk):
   return enderecoEntrega_controller.deletar_enderecoEntrega(request,pk)