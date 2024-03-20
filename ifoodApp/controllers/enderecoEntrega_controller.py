from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
# from ..permissions import Professor, Admin, PodeEditarPerfil,Cadastrado,IsProfessorOrAdmin
from rest_framework.permissions import AllowAny
from ..models import EnderecoEntrega, Endereco
from ..serializers import EnderecoEntrega_Serializer, Endereco_Serializer


def exibir_enderecosEntrega(request):
    enderecosEntrega = EnderecoEntrega.objects.all()
    serializer = EnderecoEntrega_Serializer(enderecosEntrega, many=True)
    return Response(serializer.data)


def exibir_enderecoEntrega(request, pk):
    try:
        todosEnderecosEntrega = EnderecoEntrega.objects.filter(usuarioId=pk)
        response = []
        # Puxar todos os enderecoId's
        for enderecoEntrega in todosEnderecosEntrega:
            enderecoId = EnderecoEntrega_Serializer(
                enderecoEntrega).data['enderecoId']
            # Puxar endereço por seu id
            endereco = Endereco.objects.get(enderecoId=enderecoId)
            # Adicionar á lista do response
            response.append(Endereco_Serializer(endereco).data)
        return Response({"message": response}, status=200)
    except EnderecoEntrega.DoesNotExist:
        return Response({"message": f"enderecoEntrega {pk} não encontrado"}, status=404)


def criar_enderecoEntrega(request):
    serializer = EnderecoEntrega_Serializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        enderecoEntrega = serializer.save()
        return Response({"message": "enderecoEntrega criado com sucesso!", "enderecoId": enderecoEntrega.__dict__['enderecoEntregaId']}, status=200)
    else:
        return Response({"message": "Não foi possível criar o endereço, revise os campos e tente novamente!"}, status=404)


def editar_enderecoEntrega(request, pk):
    try:
        enderecoEntrega = EnderecoEntrega.objects.get(usuarioId=pk)
        serializer = EnderecoEntrega_Serializer(
            instance=enderecoEntrega, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"mensagem": f"enderecoEntrega {pk} atualizado com sucesso.", f"reserva{pk}": serializer.data})

    except EnderecoEntrega.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"message": f"enderecoEntrega {pk} não encontrado"}, status=404)


def deletar_enderecoEntrega(request, pk):
    try:
        enderecoEntrega = EnderecoEntrega.objects.get(id=pk)
        enderecoEntrega.delete()
        return Response({"message": f"enderecoEntrega {pk} deletado com sucesso!"}, status=200)
    except EnderecoEntrega.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"message": f"enderecoEntrega {pk} não encontrado"}, status=404)
