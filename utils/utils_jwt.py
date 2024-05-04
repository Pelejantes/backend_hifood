import jwt
from django.conf import settings
from datetime import datetime, timedelta


def decode_token_jwt(token_jwt):
    secret_key = settings.SIMPLE_JWT["SIGNING_KEY"]
    algorithm = settings.SIMPLE_JWT["ALGORITHM"]
    try:
        payload = jwt.decode(token_jwt, secret_key, algorithms=[algorithm])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.DecodeError:
        return None


def extrair_toker_jwt(header):
    token_jwt = header.split("Bearer ")[1]
    token_jwt = token_jwt.replace('"', "")
    return token_jwt


def gerar_token_jwt(usuario):
    exp_timestamp = datetime.now() + timedelta(days=7)
    # Defina as informações que deseja incluir no payload (carga útil) do JWT
    payload = {
        'usuarioId': f"{usuario.usuarioId}",
        'telefoneUsu': f"{usuario.telefoneUsu}",
        'nomeUsu': f"{usuario.nomeUsu}",
        'tipoUsuarioId': f"{usuario.tipoUsuarioId}",
        'exp': exp_timestamp
        # Outras informações personalizadas podem ser adicionadas aqui
    }

    # Acesse a chave secreta e o algoritmo diretamente de settings
    secret_key = settings.SIMPLE_JWT["SIGNING_KEY"]
    # Supondo que você tenha definido JWT_ALGORITHM em settings.py
    algorithm = settings.SIMPLE_JWT["ALGORITHM"]

    # Gere o token JWT
    token_jwt = jwt.encode(payload, secret_key, algorithm=algorithm)

    # Retorna o token_jwt como uma resposta JSON
    return token_jwt
