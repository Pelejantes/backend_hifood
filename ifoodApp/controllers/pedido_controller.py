from rest_framework.response import Response
from ..models import Pedido
from ..serializers import Pedido_Serializer
from utils.func_gerais import listarErros, serializersValidos


def exibir_pedidos(request):
    pedidos = Pedido.objects.all()
    serializer = Pedido_Serializer(pedidos, many=True)
    return Response(serializer.data)


def exibir_pedido(request, pk):
    try:
        pedido = Pedido.objects.get(pedidoId=pk)
        serializer = Pedido_Serializer(pedido, many=False)
        return Response(serializer.data)
    except Pedido.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"mensagem": f"Pedido {pk} não encontrado"}, status=404)


def criar_pedido(request):
    serializer = Pedido_Serializer(data=request.data)
    if serializer.is_valid():
        pedido = serializer.save()
        return Response({"mensagem": "Pedido criado com sucesso!", "pedidoId": pedido.__dict__['pedidoId']}, status=200)
    else:
        error_messages = listarErros([serializer])
        return Response({"mensagem": "Não foi possível criar o pedido, revise os campos e tente novamente!","erros":error_messages}, status=404)


def editar_pedido(request, pk):
    try:
        pedido = Pedido.objects.get(pedidoId=pk)
        serializer = Pedido_Serializer(instance=pedido, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"mensagem": f"Pedido {pk} atualizado com sucesso.", f"reserva{pk}": serializer.data})

    except Pedido.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"mensagem": f"Pedido {pk} não encontrado"}, status=404)


def deletar_pedido(request, pk):
    try:
        pedido = Pedido.objects.get(pedidoId=pk)
        pedido.delete()
        return Response({"mensagem": f"Pedido {pk} deletado com sucesso!"}, status=200)
    except Pedido.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"mensagem": f"Pedido {pk} não encontrado"}, status=404)
