from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny
from ..controllers.login_controller import login_user,validar_token_user

@api_view(["POST"])
# @permission_classes([AllowAny])
def login_user_view(request):
    return login_user(request)
@api_view(["GET"])
# @permission_classes([AllowAny])
def validar_token_view(request):
    return validar_token_user(request)