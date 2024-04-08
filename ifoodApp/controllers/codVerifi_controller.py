from rest_framework.response import Response
from rest_framework import status
from ..models import CodVerif, Usuario
# from utils.utils_jwt import gera_token
from utils.func_gerais import gerar_code, listarErros, serializersValidos
from ..serializers import CodVerif_Serializer, Usuario_Serializer


def enviar_codigo(request):
    # Puxa telefone do request
    try:
        telefoneUsu = request.data['telefoneUsu']
    except AssertionError:
        return Response({"mensagem": "Campo de telefone é obrigatório"}, status=status.HTTP_406_NOT_ACCEPTABLE)
    # Puxa usuario pelo telefone
    try:
        usuario = Usuario.objects.get(telefoneUsu=telefoneUsu)
    except Usuario.DoesNotExist:
        return Response(
            {"mensagem": "Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND
        )
    # Se codVerifId não existir, criar nova table
    if usuario.codVerifId != None:
        codVerif_model = CodVerif.objects.get(
            CodVerifId=f"{usuario.codVerifId}")
        codVerif_Serializer = CodVerif_Serializer(
            instance=codVerif_model, data={"codigo": gerar_code(6)})
    else:
        # Se existir, usar a mesma para armazenar o novo código
        codVerif_Serializer = CodVerif_Serializer(
            data={"codigo": gerar_code(6)})
        
    if serializersValidos([codVerif_Serializer]):
        codVerifInstancia = codVerif_Serializer.save()
        usuario.codVerifId = codVerifInstancia
        usuario.save()
        return Response(
            {"message": f"Código enviado ao usuário."}, status=200,
        )
    else:
        erros = listarErros([codVerif_Serializer])
        return Response(erros, status=status.HTTP_400_BAD_)
