from rest_framework.response import Response
from rest_framework import status
from ..models import CodVerif, Usuario
# from utils.utils_jwt import gera_token
from utils.func_gerais import gerar_code, listarErros, serializersValidos
from ..serializers import CodVerif_Serializer


def enviarCodigo(request, pk):

    usuario = Usuario.objects.get(usuarioId=pk)

    codVerif_Serializer = CodVerif_Serializer({"codigo": gerar_code(6)})
    if serializersValidos([codVerif_Serializer]):
        codVerif_Serializer.save()
        return Response(
            {"message": f"Código enviado ao usuário {pk}."}, status=200,
        )
    else:
        erros = listarErros([codVerif_Serializer])
        return Response(erros, status=status.HTTP_400_BAD_)
