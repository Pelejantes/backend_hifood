import jwt
from rest_framework.exceptions import AuthenticationFailed
from django.http import JsonResponse
from django.conf import settings
from .models import Usuario
from utils.utils_jwt import decode_token_jwt, extrair_toker_jwt
from rest_framework import status


class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        authorization_header = request.META.get("HTTP_AUTHORIZATION")
        if authorization_header:
            token = extrair_toker_jwt(authorization_header)
            if token:
                payload = decode_token_jwt(token)
                if payload != None:
                    request.auth_payload = payload
                    try:
                        request.usuario = Usuario.objects.get(
                            usuarioId=payload["usuarioId"])
                    except Usuario.DoesNotExist:
                        return JsonResponse(
                            {"mensagem": "Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND
                        )
                else:
                    return JsonResponse(
                        {"mensagem": "Erro ao decodificar o token, faça login novamente."}, status=status.HTTP_404_NOT_FOUND
                    )
        response = self.get_response(request)
        return response
