from rest_framework.response import Response
from ..models import CuponsUsuario
from ..serializers import CuponsUsuario_Serializer


def exibir_cuponsUsuario(request):
    if hasattr(request, 'auth_payload'):
        usuarioId = request.auth_payload.get("usuarioId")
        cuponsUsuario = CuponsUsuario.objects.filter(usuarioId=usuarioId)
        serializer = CuponsUsuario_Serializer(cuponsUsuario, many=True)
        return Response(serializer.data)
    else:
        return "Autorização nescessária, tente novamente."


def exibir_cupomUsuario(request, pk):
    try:
        cuponsUsuario = CuponsUsuario.objects.get(cuponsUsuarioId=pk)
        serializer = CuponsUsuario_Serializer(cuponsUsuario, many=False)
        return Response(serializer.data)
    except CuponsUsuario.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"mensagem": f"CuponsUsuario {pk} não encontrado"}, status=404)
