from rest_framework.response import Response
from rest_framework import status
from ..models import FormaPag, Cartao, Pedido, EtapaPedido
from utils.func_gerais import gerar_code, listarErros, serializersValidos


def efetuarPagamento(request):
    data = request.data
    data['usuarioId'] = request.usuario.usuarioId

    pedidoId = data['pedidoId']

    if (Pedido.objects.filter(pedidoId=pedidoId).exists()):
        pedido = Pedido.objects.get(pedidoId=pedidoId)
    else:
        return Response({"mensagem": f"Não foi possível realizar ação, pedido {pedidoId} inexistente!"}, status=404)

    # puxa dados de pagamento
    formaPagId = pedido.formaPagld.formaPagId
    if (FormaPag.objects.filter(formaPagId=formaPagId).exists()):
        nomeFormaPagamento = FormaPag.objects.get(
            formaPagId=formaPagId).nomeFormaPag.lower()
    else:
        return Response({"mensagem": "Não foi possível realizar ação, forma de pagamento inexistente!"}, status=404)

    # define etapaPedido como "Preparando Pedido"
    if EtapaPedido.objects.filter(etapaPedido='Preparando Pedido').exists():
        etapaPedidoId = EtapaPedido.objects.get(
            etapaPedido='Preparando Pedido').etapaPedidoId
        etapaPedido = EtapaPedido.objects.get(etapaPedidoId=etapaPedidoId)
        pedido.etapaPedidold = etapaPedido
        pedido.save()
    # Simula resposta pagamento "Pagamento realizado com sucesso"
    return Response({"mensagem": f"Pagamento realizado com {nomeFormaPagamento}, bem sucedido!"}, status=200)
