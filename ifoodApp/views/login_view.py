from rest_framework.decorators import api_view
from ..controllers.login_controller import login_user

@api_view(["GET"])
def login_user_view(request):
    return login_user()