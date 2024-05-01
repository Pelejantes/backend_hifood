from rest_framework import serializers
from .models import Usuario, Endereco, EnderecoEntrega, CodVerif, TipoUsuario, Estabelecimento, Cupom, CuponsUsuario, Categoria, Produto, Pedido, ItemPedido


class Usuario_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"


class Endereco_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = "__all__"


class Pedido_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = "__all__"


class ItemPedido_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = "__all__"


class Estabelecimento_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Estabelecimento
        fields = "__all__"


class Cupom_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Cupom
        fields = "__all__"


class CuponsUsuario_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CuponsUsuario
        fields = "__all__"


class Categoria_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class Produto_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"


class EnderecoEntrega_Serializer(serializers.ModelSerializer):
    class Meta:
        model = EnderecoEntrega
        fields = "__all__"


class CodVerif_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CodVerif
        fields = "__all__"


class TipoUsuario_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUsuario
        fields = "__all__"
