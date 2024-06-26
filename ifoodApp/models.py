from django.db import models
from datetime import datetime
from utils.func_gerais import gerar_code
from datetime import datetime, timedelta, timezone
from fernet_fields import EncryptedTextField


class FormaPag(models.Model):
    formaPagId = models.AutoField(primary_key=True)
    nomeFormaPag = models.CharField(max_length=255)

    def __str__(self):
        return f"formaPag {self.nomeFormaPag}"


class Notificacao(models.Model):
    notificacaoId = models.AutoField(primary_key=True)
    cupomId = models.ForeignKey('Cupom', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255)
    dataRecebimento = models.DateTimeField()

    def __str__(self):
        return f"Notificação {self.notificacaoId}"


class CuponsUsuario(models.Model):
    cuponsUsuarioId = models.AutoField(primary_key=True)
    usuarioId = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    cupomId = models.ForeignKey('Cupom', on_delete=models.CASCADE)


class Cupom(models.Model):
    cupomId = models.AutoField(primary_key=True)
    regraCupomId = models.ForeignKey('RegraCupom', on_delete=models.CASCADE)
    categoriaId = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    valorDesconto = models.FloatField()
    dataValidade = models.DateTimeField()
    limiteUso = models.SmallIntegerField()
    valorMinimo = models.FloatField()

    def __str__(self):
        return f"Cupom {self.cupomId}"


class Pedido(models.Model):
    pedidoId = models.AutoField(primary_key=True)
    usuarioId = models.ForeignKey(
        'Usuario', on_delete=models.CASCADE, null=False)
    formaPagId = models.ForeignKey(
        'FormaPag', on_delete=models.CASCADE, null=False)
    etapaPedidoId = models.ForeignKey(
        'EtapaPedido', on_delete=models.CASCADE, default=1)
    cupomId = models.ForeignKey('Cupom', on_delete=models.CASCADE, null=True, default=None)
    statusAtivo = models.BooleanField(default=True)
    dataPedido = models.DateTimeField(default=datetime.now())
    gorjeta = models.SmallIntegerField(null=True)

    def __str__(self):
        return f"Pedido {self.pedidoId}"


class ItemPedido(models.Model):
    itemPedidoId = models.AutoField(primary_key=True)
    produtoId = models.ForeignKey('Produto', on_delete=models.CASCADE)
    observacao = models.CharField(max_length=255, null=True, default=None)
    qtdItens = models.SmallIntegerField(default=1)
    pedidoId = models.ForeignKey(
        'Pedido', on_delete=models.CASCADE)

    def __str__(self):
        return f"itemPedido {self.itemPedidoId}"


class ContaBancaria(models.Model):
    contaBancariaId = models.AutoField(primary_key=True)
    digitAgencia = EncryptedTextField(max_length=2)
    numConta = EncryptedTextField()
    nomeBanco = EncryptedTextField(max_length=255)

    def __str__(self):
        return f"Conta Bancária {self.contaBancariaId}"


class TipoUsuario(models.Model):
    tipoUsuarioId = models.AutoField(primary_key=True)
    nomeTipoUsuario = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.tipoUsuarioId}"


class RegraCupom(models.Model):
    regraCupomId = models.AutoField(primary_key=True)
    descricaoRegra = models.TextField()

    def __str__(self):
        return f"Regra: {self.descricaoRegra}"


class Cartao(models.Model):
    cartaoId = models.AutoField(primary_key=True)
    usuarioId = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    formaPagId = models.ForeignKey(
        'formaPag', on_delete=models.CASCADE)
    nomeBandeira = models.CharField(max_length=255)
    numCartao = EncryptedTextField(max_length=16)
    validade = EncryptedTextField()
    cvv = EncryptedTextField(max_length=3)
    nomeTitular = EncryptedTextField(max_length=255)
    cpfCnpj = EncryptedTextField(max_length=14)
    apelidoCartao = models.CharField(max_length=255)

    def __str__(self):
        return f"Cartão {self.numCartao} - Titular: {self.nomeTitular}"

# Aguardando Pagamento: Nesse estágio, o pedido foi feito pelo cliente, mas o pagamento ainda não foi confirmado. O iFood aguarda a confirmação do pagamento para prosseguir.
# Preparando Pedido: Após o pagamento ser confirmado, o restaurante recebe o pedido e começa a preparar a refeição. Esse estágio envolve a cozinha e a equipe do restaurante.
# Em Rota de Entrega: Quando o pedido está pronto, o entregador é acionado e parte para a entrega. Nesse momento, o cliente pode acompanhar o trajeto do entregador pelo aplicativo.
# Entregue: O pedido foi entregue com sucesso ao cliente. Nesse estágio, o cliente pode avaliar a experiência e dar feedback sobre o serviço.


class EtapaPedido(models.Model):
    etapaPedidoId = models.AutoField(primary_key=True)
    etapaPedido = models.CharField(max_length=50)


class Usuario(models.Model):
    usuarioId = models.AutoField(primary_key=True)
    nomeUsu = models.CharField(max_length=255, null=True, default=None)
    telefoneUsu = models.CharField(
        max_length=14, null=True, default=None, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    # emailUsu = models.EmailField(max_length=255, unique=True)
    imagemPerfil = models.BinaryField(null=True, default=None)
    contaBancariaId = models.ForeignKey(
        'ContaBancaria', on_delete=models.CASCADE, null=True, default=None)
    statusAtivo = models.BooleanField(default=False)
    dataCriacao = models.DateTimeField(default=datetime.now)
    tipoUsuarioId = models.ForeignKey(
        'TipoUsuario', on_delete=models.CASCADE, default=2)
    codVerifId = models.ForeignKey(
        'CodVerif', on_delete=models.CASCADE, null=True, default=None)
    USERNAME_FIELD = 'telefoneUsu'
    REQUIRED_FIELDS = []
    is_anonymous = False
    is_authenticated = False

    def _str_(self):
        return f"nomeUsu: {self.nomeUsu}"


class CodVerif(models.Model):
    CodVerifId = models.AutoField(primary_key=True)
    codigo = EncryptedTextField(max_length=6, null=True)
    dataCriacao = models.DateTimeField(auto_now_add=True)
    statusAtivo = models.BooleanField(default=True, null=False)
    duracao_expiracao_minutos = models.PositiveIntegerField(default=5)
    data_hora_expiracao = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.CodVerifId}"

    def save(self, *args, **kwargs):

        # A data_hora_expiracao é definida com base na data de geração do código e duracao_expiracao_minutos.
        if not self.data_hora_expiracao:
            self.data_hora_expiracao = datetime.now(
            ) + timedelta(minutes=self.duracao_expiracao_minutos)

        super(CodVerif, self).save(*args, **kwargs)


class EnderecoEntrega(models.Model):
    enderecoEntregaId = models.AutoField(primary_key=True)
    enderecoId = models.ForeignKey('Endereco', on_delete=models.CASCADE)
    usuarioId = models.ForeignKey('Usuario', on_delete=models.CASCADE)

    def __str__(self):
        return f"EnderecoEntrega {self.enderecoId} - Usuário: {self.usuarioId}"


class Favoritos(models.Model):
    favoritosId = models.AutoField(primary_key=True)
    usuarioId = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    estabelecimentoId = models.ForeignKey(
        'Estabelecimento', on_delete=models.CASCADE)

    def __str__(self):
        return f"Favorito {self.favoritosId} - Usuário: {self.usuarioId}"


class Endereco(models.Model):
    enderecoId = models.AutoField(primary_key=True)
    logradouro = models.CharField(max_length=255, null=False)
    cep = models.CharField(max_length=8, null=False)
    bairro = models.CharField(max_length=255, null=True, default=None)
    cidade = models.CharField(max_length=255, null=True, default=None)
    estado = models.CharField(max_length=2, null=True, default=None)
    numero = models.IntegerField(null=False)
    complemento = models.CharField(max_length=255, null=True, default=None)
    pontoReferencia = models.CharField(max_length=255, null=True, default=None)
    coordenadas = models.CharField(max_length=20, null=True, default=None)
    apelido = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        return f"Endereço {self.enderecoId}"


class EntregadorVeic(models.Model):
    tipoVeiculoId = models.AutoField(primary_key=True)
    usuarioId = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    placa = models.CharField(max_length=8)
    cnh = models.CharField(max_length=11)

    def __str__(self) -> str:
        return f"TipoVeiculo {self.tipoVeiculoId}"


class Estabelecimento(models.Model):
    estabelecimentoId = models.AutoField(primary_key=True)
    categoriaId = models.ForeignKey(
        'Categoria', on_delete=models.CASCADE, null=True, default=None)
    enderecoId = models.ForeignKey(
        'Endereco', on_delete=models.CASCADE, null=True, default=None)
    avaliacaoId = models.ForeignKey(
        'Avaliacao', on_delete=models.CASCADE, null=True, default=None)
    nomeEstab = models.CharField(max_length=255)
    telefoneEstab = models.CharField(max_length=14)
    imagemEstab = models.BinaryField(null=True, default=None)
    imagemBanner = models.BinaryField(null=True, default=None)
    cnpj = models.CharField(max_length=14)
    emailEstab = models.CharField(max_length=255)

    def __str__(self):
        return f"Estabelecimento ID: {self.estabelecimentoId}, Nome: {self.nomeEstab}"


class TipoVeiculo(models.Model):
    tipoVeiculoId = models.AutoField(primary_key=True)
    nomeTipo = models.CharField(max_length=255)

    def __str__(self):
        return f'Tipo Veiculo ID: {self.tipoVeiculoId}, Nome Tipo: {self.nomeTipo}'


class Avaliacao(models.Model):
    avaliacaoId = models.AutoField(primary_key=True)
    tipoAvaliacaoId = models.ForeignKey(
        'TipoAvaliacao', on_delete=models.CASCADE, null=False, default=0)
    usuarioId = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    qtdEstrelas = models.PositiveSmallIntegerField()
    descricao = models.CharField(max_length=255)
    dataAvaliacao = models.DateTimeField()

    def __str__(self):
        return f'Avaliação ID: {self.avaliacaoId}, Estrelas: {self.qtdEstrelas}, Descrição: {self.descricao}'


class TipoAvaliacao(models.Model):
    tipoAvaliacaoId = models.AutoField(primary_key=True)
    nomeTipo = models.CharField(max_length=50)


class Produto(models.Model):
    produtoId = models.AutoField(primary_key=True)
    estabelecimentoId = models.ForeignKey(
        'Estabelecimento', on_delete=models.CASCADE)
    categoriaId = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    nomeProd = models.CharField(max_length=255)
    disponibilidade = models.BooleanField()
    preco = models.FloatField()
    imagemProd = models.BinaryField(null=True, default=None)
    alcoolico = models.BooleanField()
    descricao = models.TextField()

    def _str_(self):
        return f"Produto ID: {self.produtoId}, Nome: {self.nomeProd}"


class Categoria(models.Model):
    categoriaId = models.AutoField(primary_key=True)
    nomeCategoria = models.CharField(max_length=255)
    imagem = models.BinaryField(null=True, default=None)

    def __str__(self):
        return f'nomeCategoria: {self.nomeCategoria}'
