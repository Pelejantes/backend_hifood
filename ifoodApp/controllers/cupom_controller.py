from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
# from ..permissions import Professor, Admin, PodeEditarPerfil,Cadastrado,IsProfessorOrAdmin
from rest_framework.permissions import AllowAny
from ..models import Cupom
from ..serializers import Cupom_Serializer


def exibir_cupons(request):
    cupoms = Cupom.objects.all()
    serializer = Cupom_Serializer(cupoms, many=True)
    return Response(serializer.data)


def exibir_cupom(request, pk):
    try:
        cupom = Cupom.objects.get(cupomId=pk)
        serializer = Cupom_Serializer(cupom, many=False)
        return Response(serializer.data)
    except Cupom.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"mensagem": f"Cupom {pk} não encontrado"}, status=404)
