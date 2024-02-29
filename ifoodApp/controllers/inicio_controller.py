from rest_framework.response import Response
routes = [
    {
        "url": "inicio/",
        "methods": ["GET"]
    },
    {
        "url": "login/",
        "methods": ["POST"],
        "body": {
            "cpf_cnpj": "string",
            "password": "string"
        }
    },
    ]
def exibir_urls():
    return Response(routes)