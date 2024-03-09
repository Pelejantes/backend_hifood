from django.db import models
from datetime import datetime


class SolicAtend(models.Model):
    solicAtendId = models.AutoField(primary_key=True)
    conversaId = models.ForeignKey('Conversa', on_delete=models.CASCADE)
    pedidoId = models.ForeignKey('Pedido', on_delete=models.CASCADE)
    dataSolicitacao = models.DateField()
    statusAtendimento = models.CharField(max_length=50)

    def __str__(self):
        return f"Solicitação de Atendimento {self.solicAtendId}"


class FormaPag(models.Model):
    formaPag = models.AutoField(primary_key=True)
    nomeFormaPag = models.IntegerField()

    def __str__(self):
        return f"Solicitação de Atendimento {self.solicAtendId}"


class CampoEspecifico(models.Model):
    campoEspecificoId = models.AutoField(primary_key=True)
    pergunta = models.CharField(max_length=255)
    qtdLimite = models.SmallIntegerField()

    def __str__(self):
        return f"Campo Específico {self.campoEspecificoId}"


class AlternativasCampEsp(models.Model):
    campoEspecificoId = models.AutoField(primary_key=True)
    alternativa = models.CharField(max_length=50)

    def __str__(self):
        return f"Alternativa para Campo Específico {self.campoEspecificoId}"


class Acompanhamento(models.Model):
    acompanhamentoId = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    qtdLimite = models.SmallIntegerField()
    incluso = models.BooleanField()

    def __str__(self):
        return f"Acompanhamento {self.acompanhamentoId}"


class Notificacao(models.Model):
    notificacaoId = models.AutoField(primary_key=True)
    cuponId = models.ForeignKey('Cupon', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255)
    dataRecebimento = models.DateField()

    def __str__(self):
        return f"Notificação {self.notificacaoId}"


class Cupon(models.Model):
    cuponId = models.AutoField(primary_key=True)
    regraCuponId = models.ForeignKey('RegraCupon', on_delete=models.CASCADE)
    categoriaId = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    valorDesconto = models.FloatField()
    dataValidade = models.DateField()
    limiteUso = models.SmallIntegerField()
    valorMinimo = models.FloatField()

    def __str__(self):
        return f"Cupom {self.cuponId}"


class Conversa(models.Model):
    conversaId = models.AutoField(primary_key=True)
    emissor = models.IntegerField()
    receptor = models.IntegerField()
    conteudo = models.TextField()
    dataEnvio = models.DateField()
    finalizada = models.BooleanField()

    def __str__(self):
        return f"Conversa {self.conversaId}"


class Pedido(models.Model):
    pedidoId = models.AutoField(primary_key=True)
    produtold = models.ForeignKey('Produto', on_delete=models.CASCADE)
    usuariold = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    formaPagld = models.ForeignKey(
        'FormaPag', on_delete=models.CASCADE)
    campoEspecificold = models.ForeignKey(
        'CampoEspecifico', on_delete=models.CASCADE)
    acompanhamentold = models.ForeignKey(
        'Acompanhamento', on_delete=models.CASCADE)
    cuponld = models.ForeignKey('Cupon', on_delete=models.CASCADE)
    statusPedido = models.CharField(max_length=50)
    valorTotal = models.FloatField()
    observacao = models.CharField(max_length=255)
    dataPedido = models.DateField()
    gorjeta = models.SmallIntegerField()
    qtdItens = models.SmallIntegerField()

    def __str__(self):
        return f"Pedido {self.pedidoId}"


class ContaBancaria(models.Model):
    contaBancariaId = models.AutoField(primary_key=True)
    digitAgencia = models.CharField(max_length=2)
    numConta = models.IntegerField()
    nomeBanco = models.CharField(max_length=255)

    def __str__(self):
        return f"Conta Bancária {self.contaBancariaId}"


class TipoUsuario(models.Model):
    tipoUsuarioId = models.AutoField(primary_key=True)
    nomeTipoUsuario = models.CharField(max_length=255)

    def __str__(self):
        return f"Tipo de Usuário {self.tipoUsuarioId}"


class RegraCupon(models.Model):
    regraCuponId = models.AutoField(primary_key=True)
    descricaoRegra = models.TextField()

    def __str__(self):
        return f"Regra: {self.descricaoRegra}"


class Cartao(models.Model):
    cartaold = models.AutoField(primary_key=True)
    usuarioId = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    nomeBandeira = models.CharField(max_length=255)
    numCartao = models.CharField(max_length=16)
    validade = models.DateField()
    cvv = models.CharField(max_length=3)
    nomeTitular = models.CharField(max_length=255)
    cpfCnpj = models.CharField(max_length=14)
    apelidoCartao = models.CharField(max_length=255)

    def __str__(self):
        return f"Cartão {self.numCartao} - Titular: {self.nomeTitular}"


class Usuario(models.Model):
    usuarioId = models.AutoField(primary_key=True)
    nomeUsu = models.CharField(max_length=255, null=True)
    telefoneUsu = models.CharField(max_length=14, null=True)
    cpf = models.CharField(max_length=11, unique=True)
    emailUsu = models.EmailField(max_length=255, unique=True)
    imagemPerfil = models.BinaryField(null=True)
    contaBancariaId = models.ForeignKey(
        'ContaBancaria', on_delete=models.CASCADE, null=True)
    statusAtivo = models.BooleanField(default=True)
    dataCriacao = models.DateField(default=datetime.now)
    tipoUsuarioId = models.ForeignKey(
        'TipoUsuario', on_delete=models.CASCADE, default=0)
    codVerif = models.CharField(max_length=6, null=True)
    USERNAME_FIELD = 'emailUsu'
    REQUIRED_FIELDS = []
    is_anonymous = False
    is_authenticated = False

    def _str_(self):
        return self.nomeUsu


class EnderecoEntrega(models.Model):
    enderecoEntregaId = models.AutoField(primary_key=True)
    enderecoId = models.ForeignKey('Endereco', on_delete=models.CASCADE)
    usuarioId = models.ForeignKey('Usuario', on_delete=models.CASCADE)

    def __str__(self):
        return f"EnderecoEntrega {self.enderecoId} - Usuário: {self.usuarioId}"


class Favorito(models.Model):
    favoritosId = models.AutoField(primary_key=True)
    usuarioId = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    estabelecimentoId = models.ForeignKey(
        'Estabelecimento', on_delete=models.CASCADE)

    def __str__(self):
        return f"Favorito {self.favoritosId} - Usuário: {self.usuarioId}"


class Endereco(models.Model):
    enderecoId = models.AutoField(primary_key=True)
    logradouro = models.CharField(max_length=255, null=False, default='')
    cep = models.CharField(max_length=8, null=False, default='')
    bairro = models.CharField(max_length=255, null=True)
    cidade = models.CharField(max_length=255, null=True)
    estado = models.CharField(max_length=2, null=True)
    numero = models.IntegerField(null=True)
    complemento = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"Endereço {self.numero} - {self.logradouro}, {self.bairro}, {self.cidade}, {self.estado}"


class EntregadorVeic(models.Model):
    tipoVeiculoId = models.AutoField(primary_key=True)
    usuarioId = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    placa = models.CharField(max_length=8)
    cnh = models.CharField(max_length=11)

    def __str__(self) -> str:
        return f"TipoVeiculo {self.tipoVeiculoId}"


class Seguranca(models.Model):
    segurancaId = models.AutoField(primary_key=True)
    usuarioId = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    dispConectados = models.SmallIntegerField()

    def __str__(self):
        return f"Seguranca ID: {self.segurancaId}, Usuário ID: {self.usuarioId}, Dispositivos Conectados: {self.dispConectados}"


class ConfigNotif(models.Model):
    configNotifId = models.AutoField(primary_key=True)
    usuarioId = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    permNotificacao = models.BooleanField()
    permNotifEmail = models.BooleanField()
    permNotifWhatsapp = models.BooleanField()
    permNotifSms = models.BooleanField()

    def __str__(self):
        return f"Config Notification ID: {self.configNotifId}, User ID: {self.usuarioId}"


class Estabelecimento(models.Model):
    estabelecimentold = models.AutoField(primary_key=True)
    categoriaId = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    enderecoId = models.ForeignKey('Endereco', on_delete=models.CASCADE)
    nomeEstab = models.CharField(max_length=255)
    telefoneEstab = models.CharField(max_length=14)
    imagemEstab = models.BinaryField()
    cnpj = models.CharField(max_length=14)
    emailEstab = models.CharField(max_length=255)
    codVerif = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self):
        return f"Estabelecimento ID: {self.estabelecimentold}, Nome: {self.nomeEstab}"


class TipoVeiculo(models.Model):
    tipoVeiculoId = models.AutoField(primary_key=True)
    nomeTipo = models.CharField(max_length=255)

    def __str__(self):
        return f'Tipo Veiculo ID: {self.tipoVeiculoId}, Nome Tipo: {self.nomeTipo}'


class TermoUso(models.Model):
    termoUsoId = models.AutoField(primary_key=True)
    termo = models.TextField()

    def __str__(self):
        return f'termoUsoId: {self.termoUsoId}'


class PoliticaPrivacidade(models.Model):
    politicaPrivacidadeId = models.AutoField(primary_key=True)
    politica = models.TextField()

    def __str__(self):
        return f'politicaPrivacidadeId: {self.politicaPrivacidadeId}'


class Avaliacao(models.Model):
    avaliacaoId = models.AutoField(primary_key=True)
    usuarioId = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    qtdEstrelas = models.PositiveSmallIntegerField()
    descricao = models.CharField(max_length=255)
    dataAvaliacao = models.DateField()

    def __str__(self):
        return f'Avaliação ID: {self.avaliacaoId}, Estrelas: {self.qtdEstrelas}, Descrição: {self.descricao}'


class Produto(models.Model):
    produtoId = models.AutoField(primary_key=True)
    avaliacaoId = models.ForeignKey(
        'Avaliacao', on_delete=models.CASCADE)
    estabelecimentoId = models.ForeignKey(
        'Estabelecimento', on_delete=models.CASCADE)
    categoriaId = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    nomeProd = models.CharField(max_length=255)
    disponibilidade = models.BooleanField()
    preco = models.FloatField()
    imagemProd = models.BinaryField()
    alcoolico = models.BooleanField()
    descricao = models.CharField(max_length=255)

    def _str_(self):
        return f"Produto ID: {self.produtoId}, Nome: {self.nomeProd}"


class Categoria(models.Model):
    categoriaId = models.AutoField(primary_key=True)
    nomeCategoria = models.CharField(max_length=255)

    def __str__(self):
        return f'nomeCategoria: {self.nomeCategoria}'
