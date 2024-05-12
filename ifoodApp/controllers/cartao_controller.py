from rest_framework.response import Response
from ..models import Cartao
from ..serializers import Cartao_Serializer
from utils.func_gerais import listarErros, serializersValidos


def exibir_cartoes(request):
    cartaos = Cartao.objects.all()
    serializer = Cartao_Serializer(cartaos, many=True)
    return Response(serializer.data)


def exibir_cartao(request, pk):
    try:
        cartao = Cartao.objects.get(cartaoId=pk)
        serializer = Cartao_Serializer(cartao, many=False)
        return Response(serializer.data)
    except Cartao.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"mensagem": f"Cartao {pk} não encontrado"}, status=404)


def criar_cartao(request):
    data = request.data
    data['usuarioId'] = request.usuario.usuarioId
    serializer = Cartao_Serializer(data=data)
    if serializer.is_valid():
        cartao = serializer.save()
        return Response({"mensagem": "Cartao criado com sucesso!", "cartaoId": cartao.__dict__['cartaoId']}, status=200)
    else:
        error_messages = listarErros([serializer])
        return Response({"mensagem": "Não foi possível criar o cartao, revise os campos e tente novamente!","erros":error_messages}, status=404)


def editar_cartao(request, pk):
    try:
        cartao = Cartao.objects.get(cartaoId=pk)
        serializer = Cartao_Serializer(instance=cartao, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"mensagem": f"Cartao {pk} atualizado com sucesso.", f"reserva{pk}": serializer.data})

    except Cartao.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"mensagem": f"Cartao {pk} não encontrado"}, status=404)


def deletar_cartao(request, pk):
    try:
        cartao = Cartao.objects.get(cartaoId=pk)
        cartao.delete()
        return Response({"mensagem": f"Cartao {pk} deletado com sucesso!"}, status=200)
    except Cartao.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"mensagem": f"Cartao {pk} não encontrado"}, status=404)
