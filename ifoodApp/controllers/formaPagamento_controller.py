from rest_framework.response import Response
from ..models import ItemPedido
from ..serializers import ItemPedido_Serializer
from utils.func_gerais import listarErros, serializersValidos


def exibir_formasPagamento(request):
    itemPedidos = ItemPedido.objects.all()
    serializer = ItemPedido_Serializer(itemPedidos, many=True)
    return Response(serializer.data)


def exibir_formaPagamento(request, pk):
    try:
        itemPedido = ItemPedido.objects.get(itemPedidoId=pk)
        serializer = ItemPedido_Serializer(itemPedido, many=False)
        return Response(serializer.data)
    except ItemPedido.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"mensagem": f"ItemPedido {pk} não encontrado"}, status=404)
