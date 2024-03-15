from rest_framework.response import Response
from rest_framework import status
from ..models import Usuario
# from utils.utils_jwt import gera_token

def login_user(dados):
    if "cpf" in dados:
        cpf = dados["cpf"]

        try:
            # Tenta encontrar um usuário com o cpf_cnpj fornecido
            usuario = Usuario.objects.get(cpf=cpf)

            if usuario.statusAtivo == False:
                return Response(
                    {
                        "mensagem": "Não foi possível realizar o login, pois o usuário está inativo."
                    },
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            
            # Cria um token JWT
            # token_jwt = gera_token(usuario)

            return Response(
                {
                    "mensagem": "Login bem-sucedido",
                    "usuario_id": usuario.usuarioId,
                    # "token_jwt": token_jwt,
                },
                status=status.HTTP_200_OK,
            )
        except Usuario.DoesNotExist:
            return Response(
                {"mensagem": "Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND
            )
    else:
        return Response(
            {"mensagem": "Campos 'cpf_cnpj' são obrigatórios"},
            status=status.HTTP_400_BAD_REQUEST,
        )