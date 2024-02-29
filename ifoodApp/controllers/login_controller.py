from rest_framework.response import Response
from ..models import Usuario
from ..serializers import User_Serializer

def login_user(request):
    dados = request.data
    if "cpf_cnpj" in dados and "password" in dados:
        cpf_cnpj = dados["cpf_cnpj"]
        password = dados["password"]
    else:
        return Response({"error": "Campos 'cpf_cnpj' e 'senha' são obrigatórios."}, status=400)