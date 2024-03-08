from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
# from ..permissions import Professor, Admin, PodeEditarPerfil,Cadastrado,IsProfessorOrAdmin
from rest_framework.permissions import AllowAny
from ..models import Endereco
from ..serializers import Endereco_Serializer


def exibir_enderecos(request):
    enderecos = Endereco.objects.all()
    serializer = Endereco_Serializer(enderecos, many=True)
    return Response(serializer.data)


def exibir_endereco(request, pk):
    try:
        endereco = Endereco.objects.get(enderecoId=pk)
        serializer = Endereco_Serializer(endereco, many=False)
        return Response(serializer.data)
    except Endereco.DoesNotExist:
        return Response({"message": f"Endereço {pk} não encontrado"}, status=404)  # Retorna uma resposta de erro com status 404


def criar_endereco(request):
    serializer = Endereco_Serializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Endereço criado com sucesso!"}, status=200)
    else:
        return Response({"message": "Não foi possível criar o endereço, revise os campos e tente novamente!"}, status=404)


def editar_endereco(request, pk):
    try:
        endereco = Endereco.objects.get(enderecoId=pk)
        serializer = Endereco_Serializer(instance=endereco, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"mensagem": f"Endereço {pk} atualizado com sucesso.", f"reserva{pk}": serializer.data})
    
    except Endereco.DoesNotExist:
        return Response({"message": f"Endereço {pk} não encontrado"}, status=404)  # Retorna uma resposta de erro com status 404


def deletar_endereco(request, pk):
    try:
        endereco = Endereco.objects.get(id=pk)
        endereco.delete()
        return Response({"message": f"Endereço {pk} deletado com sucesso!"}, status=200)
    except Endereco.DoesNotExist:
        return Response({"message": f"Endereço {pk} não encontrado"}, status=404)  # Retorna uma resposta de erro com status 404