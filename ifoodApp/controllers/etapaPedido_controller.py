from rest_framework.response import Response
from ..models import EtapaPedido
from ..serializers import EtapaPedido_Serializer
from utils.func_gerais import listarErros, serializersValidos


def exibir_etapasPedido(request):
    etapasPedido = EtapaPedido.objects.all()
    serializer = EtapaPedido_Serializer(etapasPedido, many=True)
    return Response(serializer.data)


def exibir_etapaPedido(request, pk):
    try:
        etapaPedido = EtapaPedido.objects.get(etapaPedidoId=pk)
        serializer = EtapaPedido_Serializer(etapaPedido, many=False)
        return Response(serializer.data)
    except EtapaPedido.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"mensagem": f"EtapaPedido {pk} não encontrado"}, status=404)

def exibir_etapaPedidoPorNome(request):
    if not 'etapaPedido' in request.data:
        return Response({"mensagem": "Não foi possível encontrar etapaPedidoId.", "errors": ["Campo 'nome' ausente."]}, status=400)
    else:
        nome = request.data['etapaPedido']
    try:
        etapaPedido = EtapaPedido.objects.get(etapaPedido=nome)
        etapaPedidoId = EtapaPedido_Serializer(etapaPedido, many=False).data['etapaPedidoId']
        return Response(etapaPedidoId)
    except EtapaPedido.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"mensagem": f"EtapaPedido '{nome}' não encontrado"}, status=404)
