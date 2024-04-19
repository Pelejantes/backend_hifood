from rest_framework.response import Response
from ..models import Estabelecimento
from ..serializers import Estabelecimento_Serializer


def exibir_estabelecimentos(request):
    estabelecimentos = Estabelecimento.objects.all()
    serializer = Estabelecimento_Serializer(estabelecimentos, many=True)
    return Response(serializer.data)


def exibir_estabelecimento(request, pk):
    try:
        estabelecimento = Estabelecimento.objects.get(estabelecimentoId=pk)
        serializer = Estabelecimento_Serializer(estabelecimento, many=False)
        return Response(serializer.data)
    except Estabelecimento.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"mensagem": f"Estabelecimento {pk} não encontrado"}, status=404)
