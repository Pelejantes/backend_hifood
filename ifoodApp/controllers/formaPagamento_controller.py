from rest_framework.response import Response
from ..models import FormaPag
from ..serializers import FormaPag_Serializer
from utils.func_gerais import listarErros, serializersValidos


def exibir_formasPagamento(request):
    formaPags = FormaPag.objects.all()
    serializer = FormaPag_Serializer(formaPags, many=True)
    return Response(serializer.data)


def exibir_formaPagamento(request, pk):
    try:
        formaPag = FormaPag.objects.get(formaPagId=pk)
        serializer = FormaPag_Serializer(formaPag, many=False)
        return Response(serializer.data)
    except FormaPag.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"mensagem": f"FormaPag {pk} não encontrado"}, status=404)
