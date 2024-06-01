from rest_framework.response import Response
from rest_framework import status
from ..models import Usuario, CodVerif
from ..serializers import Usuario_Serializer, CodVerif_Serializer
from utils.utils_jwt import gerar_token_jwt, extrair_toker_jwt, decode_token_jwt
from utils.func_gerais import gerar_code
from datetime import datetime, timezone


def login_user(request):
    # UsuarioExiste == True
    # codVerifAtivo == True
    # Receber o código
    # Validar credencial
    # codValido == True
    # retornar jwt
    # liberar acesso
    # codValido == False
    # retornar 'código inválido'
    #  UsuarioExiste == False
    # retornar 'usuario não existe'

    if 'telefoneUsu' in request.data:
        telefoneUsu = request.data['telefoneUsu']
    else:
        return Response({"mensagem": "Campo de telefone é obrigatório"}, status=status.HTTP_406_NOT_ACCEPTABLE)
    if not ('codVerif' in request.data):
        return Response({"mensagem": "Campo de codVerif é obrigatório"}, status=status.HTTP_406_NOT_ACCEPTABLE)

    try:
        usuario = Usuario.objects.get(telefoneUsu=telefoneUsu)
    except Usuario.DoesNotExist:
        return Response(
            {"mensagem": "Erro Login, Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND
        )

    if usuario.codVerifId:
        codVerif_model = CodVerif.objects.get(
            CodVerifId=f"{usuario.codVerifId}")

        horario_expiracao = codVerif_model.data_hora_expiracao
        horario_atual = (datetime.now()).replace(tzinfo=timezone.utc)

        if horario_atual > horario_expiracao:
            return Response(
                {"mensagem": f"Código expirou, solicite um novo."}, status=status.HTTP_401_UNAUTHORIZED,
            )
        if codVerif_model.codigo == request.data["codVerif"]:
            token_jwt = gerar_token_jwt(usuario)
            usuario.statusAtivo = True
            usuario.save()
            return Response(
                {"mensagem": f"Código Valido, login aprovado", "token_jwt": token_jwt}, status=200,
            )
        else:
            return Response(
                {"mensagem": f"Código inválido, login negado"}, status=status.HTTP_401_UNAUTHORIZED,
            )
    else:
        return Response(
            {"mensagem": f"Usuário {usuario.usuarioId} não possui código ativo, solite um novo."}, status=status.HTTP_401_UNAUTHORIZED,
        )


def validar_token_user(request):
    authorization_header = request.META.get("HTTP_AUTHORIZATION")
    if authorization_header:
        token = extrair_toker_jwt(authorization_header)
        if token:
            if decode_token_jwt(token):
                return Response({"mensagem": "Token válido"}, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"mensagem": "Erro ao decodificar o token, faça login novamente."},
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            return Response(
                {"mensagem": "Erro ao decodificar o token, faça login novamente."}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(
            {"mensagem": "Authorization ausente no header."}, status=status.HTTP_404_NOT_FOUND)
