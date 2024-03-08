from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
# from ..permissions import Professor, Admin, PodeEditarPerfil,Cadastrado,IsProfessorOrAdmin
from rest_framework.permissions import AllowAny
from ..models import Usuario
from ..serializers import Usuario_Serializer


def exibir_usuarios(request):
    usuarios = Usuario.objects.all()
    serializer = Usuario_Serializer(usuarios, many=True)
    return Response(serializer.data)


def exibir_usuario(request, pk):
    try:
        usuario = Usuario.objects.get(usuarioId=pk)
        serializer = Usuario_Serializer(usuario, many=False)
        return Response(serializer.data)
    except Usuario.DoesNotExist:
        return Response({"message": f"Usuário {pk} não encontrado"}, status=404)  # Retorna uma resposta de erro com status 404


def criar_usuario(request):
    serializer = Usuario_Serializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Usuário criado com sucesso!"}, status=200)
    else:
        return Response({"message": "Não foi possível criar o usuário, revise os campos e tente novamente!"}, status=404)


def inativar_usuario(request, pk):
    try:
        usuario = Usuario.objects.get(usuarioId=pk)
        if usuario.statusAtivo == 1:
            usuario.statusAtivo = 0
            usuario.save()
            return Response({"message": f"Usuário {pk} inativado com sucesso!"})
        else:
            return Response({"message": f"Usuário {pk} já estava inativado!"})
    except Usuario.DoesNotExist:
        return Response({"message": f"Usuário {pk} não encontrado"}, status=404)  # Retorna uma resposta de erro com status 404


def ativar_usuario(request, pk):
    try:
        usuario = Usuario.objects.get(usuarioId=pk)
        if usuario.statusAtivo == 0:
            usuario.statusAtivo = 1
            usuario.save()
            return Response({"message": f"Usuário {pk} ativado com sucesso!"})
        else:
            return Response({"message": f"Usuário {pk} já estava ativado!"})
    except Usuario.DoesNotExist:
        return Response({"message": f"Usuário {pk} não encontrado"}, status=404)  # Retorna uma resposta de erro com status 404


def editar_usuario(request, pk):
    try:
        usuario = Usuario.objects.get(usuarioId=pk)
        serializer = Usuario_Serializer(instance=usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"mensagem": f"Usuário {pk} atualizado com sucesso.", f"reserva{pk}": serializer.data})
    
    except Usuario.DoesNotExist:
        return Response({"message": f"Usuário {pk} não encontrado"}, status=404)  # Retorna uma resposta de erro com status 404


def deletar_usuario(request, pk):
    try:
        usuario = Usuario.objects.get(id=pk)
        usuario.delete()
        return Response({"message": f"Usuário {pk} deletado com sucesso!"}, status=200)
    except Usuario.DoesNotExist:
        return Response({"message": f"Usuário {pk} não encontrado"}, status=404)  # Retorna uma resposta de erro com status 404