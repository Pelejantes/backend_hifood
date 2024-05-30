from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
# from ..permissions import Professor, Admin, PodeEditarPerfil,Cadastrado,IsProfessorOrAdmin
from rest_framework.permissions import AllowAny
from ..models import Endereco, EnderecoEntrega
from ..serializers import Endereco_Serializer, EnderecoEntrega_Serializer
from utils.func_gerais import gerar_code, listarErros, serializersValidos


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
        # Retorna uma resposta de erro com status 404
        return Response({"mensagem": f"Endereço {pk} não encontrado"}, status=404)



def criar_endereco(request):
    serializer = Endereco_Serializer(data=request.data)
    if serializer.is_valid():
        endereco = serializer.save()
        return Response({"mensagem": "Endereço criado com sucesso!", "enderecoId": endereco.__dict__['enderecoId']}, status=200)
    else:
        error_messages = listarErros([serializer])
        return Response({"mensagem": "Não foi possível criar o endereço.", "errors": error_messages}, status=400)


def editar_endereco(request, pk):
    try:
        endereco = Endereco.objects.get(enderecoId=pk)
        serializer = Endereco_Serializer(instance=endereco, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"mensagem": f"Endereço {pk} atualizado com sucesso." })

    except Endereco.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        error_messages = listarErros([serializer])
        return Response({"mensagem": f"Endereço {pk} não encontrado", "errors": error_messages}, status=400)


def deletar_endereco(request, pk):
    try:
        endereco = Endereco.objects.get(enderecoId=pk)
        endereco.delete()
        return Response({"mensagem": f"Endereço {pk} deletado com sucesso!"}, status=200)
    except Endereco.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"mensagem": f"Endereço {pk} não encontrado"}, status=404)
