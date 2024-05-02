from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
# from ..permissions import Professor, Admin, PodeEditarPerfil,Cadastrado,IsProfessorOrAdmin
from rest_framework.permissions import AllowAny
from ..models import Produto
from ..serializers import Produto_Serializer


def exibir_produtos(request):
    produtos = Produto.objects.all()
    serializer = Produto_Serializer(produtos, many=True)
    return Response(serializer.data)


def exibir_produto(request, pk):
    try:
        produto = Produto.objects.get(produtoId=pk)
        serializer = Produto_Serializer(produto, many=False)
        return Response(serializer.data)
    except Produto.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"mensagem": f"Produto {pk} não encontrado"}, status=404)

def exibir_produtosEstab(request, pk):
    try:
        produto = Produto.objects.filter(estabelecimentoId=pk)
        serializer = Produto_Serializer(produto, many=True)
        return Response(serializer.data)
    except Produto.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"mensagem": f"Produto {pk} não encontrado"}, status=404)