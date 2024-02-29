from rest_framework.decorators import api_view
from ..controllers.inicio_controller import exibir_urls

@api_view(["GET"])
def exibir_urls_view(request):
    return exibir_urls()