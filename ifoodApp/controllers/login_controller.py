from rest_framework.response import Response
from rest_framework import status
from ..models import Usuario, CodVerif
from ..serializers import Usuario_Serializer, CodVerif_Serializer
# from utils.utils_jwt import gera_token
from utils.func_gerais import gerar_code

def login_user(dados):
    # UsuarioExiste == True
        # codVerifAtivo == True
            # Receber o código
            # Validar credencial
                # codValido == True
                    # retornar jwt
                    # liberar acesso
                # codValido == False
                    # retornar 'código inválido'
        # codValidoAtivo == False
            #  Gerar novo código
            #  Enviar código via msg
    #  UsuarioExiste == False
        # retornar 'usuario não existe'

    if "telefoneUsu" in dados:
        telefoneUsu = dados["telefoneUsu"]
        try:
            usuario = Usuario.objects.get(telefoneUsu=telefoneUsu)
        except Usuario.DoesNotExist:
            return Response(
                {"mensagem": "Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND
            )
        # return Response({f"{usuario.codVerifId}"})
        if usuario.codVerifId and "codigo" in dados:
            codVerif_model = CodVerif.objects.get(CodVerifId=f"{usuario.codVerifId}")
            if codVerif_model.codigo == dados["codigo"]:
                return Response(
                    {"message": f"Código Valido, login aprovado"}, status=200,
                )
            else:
                return Response(
                    {"message": f"Código inválido, login negado"}, status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            codVerif_Serializer = CodVerif_Serializer(data={})
            if codVerif_Serializer.is_valid():
                codVerif_Serializer.save()
                return Response(
                    {"message": f"Código enviado ao usuário."}, status=200,
                )
            else:
                return Response({"mensagem": "Serializer Invalido"}, status=status.HTTP_400_BAD_)


    # Se request não contem codVerif envia código
    # Se request contem codVerif valida e informa o usuario
    # body = {
    #     "telefoneUsu":"11912345678",
    #     "codVerif": "123456"
    # }
    if "telefoneUsu" in dados:
        telefoneUsu = dados["telefoneUsu"]
        try:
            # Tenta encontrar um usuário com o telefoneUsu_cnpj fornecido
            usuario = Usuario.objects.get(telefoneUsu=telefoneUsu)

            if usuario.statusAtivo == False:
                return Response(
                    {
                        "mensagem": "Não foi possível realizar o login, pois o usuário está inativo."
                    },
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            # Cria um token JWT
            # token_jwt = gera_token(usuario)
            # if "codVerif" in dados:
            #     codVerif = dados["codVerif"]
            # else:
            #     return Response(
            #                 {
            #                     "mensagem": "Login bem-sucedido",
            #                     "usuario_id": usuario.usuarioId,
            #                     # "token_jwt": token_jwt,
            #                 },
            #                 status=status.HTTP_200_OK,
            #             )
            if "codVerifId" in dados and Usuario.codVerifId:
                usuario.codVerifId == dados["codVerif"]
                return Response(
                    {
                        "mensagem": "Login bem-sucedido",
                        "usuario_id": usuario.usuarioId,
                        # "token_jwt": token_jwt,
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {
                        "mensagem": gerar_code(6),
                        "usuario_id": usuario.usuarioId,
                        # "token_jwt": token_jwt,
                    },
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        except Usuario.DoesNotExist:
            return Response(
                {"mensagem": "Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND
            )
    else:
        return Response(
            {"mensagem": "Campos 'telefoneUsu' e 'codVerif' são obrigatórios"},
            status=status.HTTP_400_BAD_REQUEST,
        )