from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny
from ..controllers.login_controller import login_user

@api_view(["POST"])
# @permission_classes([AllowAny])
def login_user_view(request):
    dados = request.data
    return login_user(dados)