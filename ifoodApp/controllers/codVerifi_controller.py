from rest_framework.response import Response
from rest_framework import status
from ..models import CodVerif, Usuario
# from utils.utils_jwt import gera_token
from utils.func_gerais import gerar_code, listarErros, serializersValidos
from ..serializers import CodVerif_Serializer, Usuario_Serializer
from twilio.rest import Client
import os
from dotenv import load_dotenv

dotenv_path = "../../dotenv_files/.env"
load_dotenv(dotenv_path)

economizar_recursos = False

def enviar_codigo(request):
    # Puxa telefone do request
    if 'telefoneUsu' in request.data:
        telefoneUsu = request.data['telefoneUsu']
    else:
        return Response({"mensagem": "Campo de telefone é obrigatório"}, status=status.HTTP_406_NOT_ACCEPTABLE)
    # Puxa usuario pelo telefone
    try:
        usuario = Usuario.objects.get(telefoneUsu=telefoneUsu)
    except Usuario.DoesNotExist:
        return Response(
            {"mensagem": "Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND
        )
    codigo = gerar_code(6)
    # Se codVerifId não existir, criar nova table
    if usuario.codVerifId != None:
        codVerif_model = CodVerif.objects.get(
            CodVerifId=f"{usuario.codVerifId}")
        codVerif_Serializer = CodVerif_Serializer(
            instance=codVerif_model, data={"codigo": codigo})
    else:
        # Se existir, usar a mesma para armazenar o novo código
        codVerif_Serializer = CodVerif_Serializer(
            data={"codigo": codigo})
        
    if serializersValidos([codVerif_Serializer]):
        codVerifInstancia = codVerif_Serializer.save()
        usuario.codVerifId = codVerifInstancia
        usuario.save()
        
        # Fazer req para a API de Msg via Whatsapp
        account_sid = os.getenv('ACCOUNT_SID')
        auth_token = os.getenv('AUTH_TOKEN')
        client = Client(account_sid, auth_token)

        if(not economizar_recursos):
            print('Enviando código!')
            client.messages.create(
            from_=f"whatsapp:+{os.getenv('TEL_FROM')}",
            body=f"Seu código de verificação H!food: *{codigo}*",
            to=f"whatsapp:+{os.getenv('TEL_TO')}"
        )

        return Response(
            {"message": f"Código enviado ao usuário."}, status=200,
        )
    else:
        erros = listarErros([codVerif_Serializer])
        return Response(erros, status=status.HTTP_400_BAD_REQUEST)
