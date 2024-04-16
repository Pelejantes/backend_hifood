from rest_framework.response import Response
from ..models import Categoria
from ..serializers import Categoria_Serializer


def exibir_categorias(request):
    categorias = Categoria.objects.all()
    serializer = Categoria_Serializer(categorias, many=True)
    return Response(serializer.data)


def exibir_categoria(request, pk):
    try:
        categoria = Categoria.objects.get(categoriaId=pk)
        serializer = Categoria_Serializer(categoria, many=False)
        return Response(serializer.data)
    except Categoria.DoesNotExist:
        # Retorna uma resposta de erro com status 404
        return Response({"message": f"Categoria {pk} não encontrado"}, status=404)
