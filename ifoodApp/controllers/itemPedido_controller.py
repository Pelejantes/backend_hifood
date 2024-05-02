from rest_framework.response import Response
from ..models import ItemPedido
from ..serializers import ItemPedido_Serializer
from utils.func_gerais import listarErros, serializersValidos


def exibir_itemPedidos(request):
    itemPedidos = ItemPedido.objects.all()
    serializer = ItemPedido_Serializer(itemPedidos, many=True)
    return Response(serializer.data)


def exibir_itemPedido(request, pk):
    try:
        itemPedido = ItemPedido.objects.get(itemPedidoId=pk)
        serializer = ItemPedido_Serializer(itemPedido, many=False)
        return Response(serializer.data)
    except ItemPedido.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"mensagem": f"ItemPedido {pk} não encontrado"}, status=404)


def criar_itemPedido(request):
    serializer = ItemPedido_Serializer(data=request.data)
    if serializer.is_valid():
        itemPedido = serializer.save()
        return Response({"mensagem": "ItemPedido criado com sucesso!", "itemPedidoId": itemPedido.__dict__['itemPedidoId']}, status=200)
    else:
        error_messages = listarErros([serializer])
        return Response({"mensagem": "Não foi possível criar o itemPedido, revise os campos e tente novamente!","erros":error_messages}, status=404)


def editar_itemPedido(request, pk):
    try:
        itemPedido = ItemPedido.objects.get(itemPedidoId=pk)
        serializer = ItemPedido_Serializer(instance=itemPedido, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"mensagem": f"ItemPedido {pk} atualizado com sucesso.", f"reserva{pk}": serializer.data})

    except ItemPedido.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"mensagem": f"ItemPedido {pk} não encontrado"}, status=404)


def deletar_itemPedido(request, pk):
    try:
        itemPedido = ItemPedido.objects.get(itemPedidoId=pk)
        itemPedido.delete()
        return Response({"mensagem": f"ItemPedido {pk} deletado com sucesso!"}, status=200)
    except ItemPedido.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"mensagem": f"ItemPedido {pk} não encontrado"}, status=404)