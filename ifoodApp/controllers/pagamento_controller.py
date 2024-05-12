from rest_framework.response import Response
from rest_framework import status
from ..models import FormaPag,Cartao
from utils.func_gerais import gerar_code, listarErros, serializersValidos
from ..serializers import CodVerif_Serializer, Usuario_Serializer


def efetuarPagamento(request):
    data = request.data
    data['usuarioId'] = request.usuario.usuarioId
    formaPagId = data['formaPagId']
    # simula pagamento -> puxa dados pagamento
    if(len(FormaPag.objects.filter(formaPagId = formaPagId)) > 0):
        nomeFormaPagamento = FormaPag.objects.get(formaPagId = formaPagId)
    else:
        return Response({"mensagem": "Não foi possível criar o cartao, forma de pagamento inexistente!"}, status=404)
    
    # define etapaPedido como "Preparando Pedido"
    # Simula resposta pagamento "Pagamento realizado com sucesso"

    return Response(f'Pagamento realizado com {nomeFormaPagamento}')
