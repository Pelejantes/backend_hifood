from rest_framework.response import Response
from ..models import TipoUsuario
from ..serializers import TipoUsuario_Serializer

def exibir_tipoUsuarios(request):
    tipoUsuarios = TipoUsuario.objects.all()
    serializer = TipoUsuario_Serializer(tipoUsuarios, many=True)
    return Response(serializer.data)


def exibir_tipoUsuario(request, pk):
    try:
        tipoUsuario = TipoUsuario.objects.get(tipoUsuarioId=pk)
        serializer = TipoUsuario_Serializer(tipoUsuario, many=False)
        return Response(serializer.data)
    except TipoUsuario.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"message": f"Tipo de Usuario {pk} não encontrado"}, status=404)


def criar_tipoUsuario(data):
    serializer = TipoUsuario_Serializer(data=data)
    if serializer.is_valid():
        tipoUsuario = serializer.save()
        return Response({"message": "Tipo de Usuario criado com sucesso!", "tipoUsuarioId": tipoUsuario.__dict__['tipoUsuarioId']}, status=200)
    else:
        return Response({"message": "Não foi possível criar o Tipo de Usuario, revise os campos e tente novamente!"}, status=404)


def editar_tipoUsuario(request, pk):
    try:
        tipoUsuario = TipoUsuario.objects.get(tipoUsuarioId=pk)
        serializer = TipoUsuario_Serializer(instance=tipoUsuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"mensagem": f"Tipo de Usuario {pk} atualizado com sucesso.", f"reserva{pk}": serializer.data})

    except TipoUsuario.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"message": f"Tipo de Usuario {pk} não encontrado"}, status=404)


def deletar_tipoUsuario(request, pk):
    try:
        tipoUsuario = TipoUsuario.objects.get(id=pk)
        tipoUsuario.delete()
        return Response({"message": f"Tipo de Usuario {pk} deletado com sucesso!"}, status=200)
    except TipoUsuario.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"message": f"Tipo de Usuario {pk} não encontrado"}, status=404)
