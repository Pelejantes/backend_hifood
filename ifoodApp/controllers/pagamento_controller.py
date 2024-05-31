from rest_framework.response import Response
from rest_framework import status
from ..models import FormaPag, Cartao, Pedido, EtapaPedido
from utils.func_gerais import gerar_code, listarErros, serializersValidos


def efetuarPagamento(request):
    data = request.data
    data['usuarioId'] = request.usuario.usuarioId

    # pedidoId = data['pedidoId']

    if (Pedido.objects.all().last()):
        pedido = Pedido.objects.all().last()
    else:
        return Response({"mensagem": f"Não foi possível realizar ação, nenhum pedido inexistente!"}, status=404)
    if not pedido.statusAtivo :
        return Response({"mensagem": f"Não foi possível realizar ação, nenhum pedido ativo!"}, status=404)
    if pedido.etapaPedidoId.etapaPedidoId != 1:
        return Response({"mensagem": f"Não foi possível realizar ação, pagamento já efetuado anteriormente!"}, status=404)
    # puxa dados de pagamento
    formaPagId = pedido.formaPagId.formaPagId
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
        pedido.etapaPedidoId = etapaPedido
        pedido.save()
    # Simula resposta pagamento "Pagamento realizado com sucesso"
    return Response({"mensagem": f"Pagamento realizado com {nomeFormaPagamento}, bem sucedido!"}, status=200)
