from rest_framework.response import Response
from ..models import ItemPedido, Pedido
from ..serializers import ItemPedido_Serializer, Pedido_Serializer
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


def criar_itensPedido(request):
    # Esta função cria um novo item em um pedido existente.
    # Verifica se o último pedido está ativo, se não, cria um novo pedido.
    # Em seguida, cria um novo item no pedido e retorna o ID do item.
    data = request.data or {}
    data['usuarioId'] = request.usuario.usuarioId
    # Inicializa data como os dados da requisição, ou um dicionário vazio se não houver dados.
    ultimoPedido = Pedido.objects.filter(usuarioId=data['usuarioId']).last()
    # Obtém o último pedido no banco de dados.
    dataPedido = {
        'usuarioId': request.usuario.__dict__['usuarioId'],
        'formaPagId': data['formaPagId']
    }
    if (not ultimoPedido.statusAtivo) or (ultimoPedido == None):
        # Se o último pedido não está ativo, cria um novo.
        pedido_serializer = Pedido_Serializer(data=dataPedido)
        # Cria um serializador para os dados do pedido.
        if serializersValidos([pedido_serializer]):
            # Se o serializador é válido, salva o pedido.
            ultimoPedido = pedido_serializer.save()
        else:
            # Se o serializador não é válido, retorna uma mensagem de erro.
            error_messages = listarErros([pedido_serializer])
            return Response({"mensagem": "Não foi possível criar o itemPedido.", "errors": error_messages}, status=400)
    else:
        pedido_serializer = Pedido_Serializer(
            instance=ultimoPedido, data=dataPedido)
        if pedido_serializer.is_valid():
            pedido_serializer.save()
        else:
            error_messages = listarErros([pedido_serializer])
            return Response({"mensagem": "Não foi possível criar o itemPedido.", "errors": error_messages}, status=400)

    pedidoId = ultimoPedido.__dict__['pedidoId']
    if not data['itensPedido']:
        return Response({"mensagem": "Não foi possível criar o itemPedido.", "errors": ['Não foi passado nenhum item.']}, status=400)
    else:
        itensPedido = data['itensPedido']
    itensPedidosBemSucedidos = []
    itensPedidosMalSucedidos = []
    for itemPedido in itensPedido:
        itemPedido['pedidoId'] = pedidoId
        # Adiciona o ID do pedido aos dados.
        itemPedido_serializer = ItemPedido_Serializer(data=itemPedido)
        # Cria um serializador para os dados do item.
        if itemPedido_serializer.is_valid():
            # Se o serializador é válido, salva o item.
            itemPedido_serializer.save()
            itensPedidosBemSucedidos.append(itemPedido)
        else:
            # Se o serializador não é válido, retorna uma mensagem de erro.
            error_messages = listarErros([itemPedido_serializer])
            itensPedidosMalSucedidos.append([itemPedido, error_messages])
        if len(itensPedidosMalSucedidos) > 0:
            return Response({"mensagem": f"Não foi possível criar alguns itens do pedido, revise os campos e tente novamente!",
                             "itensPedidosMalSucedidos": f"{itensPedidosMalSucedidos}",
                             "itensPedidosBemSucedidos": f"{itensPedidosBemSucedidos}",
                             }, status=404)
    return Response({"mensagem": "ItemPedido criado com sucesso!", "itensPedidosBemSucedidos": f"{itensPedidosBemSucedidos}"}, status=200)


# def editar_itemPedido(request, pk):
#     try:
#         itemPedido = ItemPedido.objects.get(itemPedidoId=pk)
#         serializer = ItemPedido_Serializer(
#             instance=itemPedido, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response({"mensagem": f"ItemPedido {pk} atualizado com sucesso." })

#     except ItemPedido.DoesNotExist:
#         # Retorna uma resposta de erro com status 404
#         return Response({"mensagem": f"ItemPedido {pk} não encontrado"}, status=404)


# def deletar_itemPedido(request, pk):
#     try:
#         itemPedido = ItemPedido.objects.get(itemPedidoId=pk)
#         itemPedido.delete()
#         return Response({"mensagem": f"ItemPedido {pk} deletado com sucesso!"}, status=200)
#     except ItemPedido.DoesNotExist:
#         # Retorna uma resposta de erro com status 404
#         return Response({"mensagem": f"ItemPedido {pk} não encontrado"}, status=404)
