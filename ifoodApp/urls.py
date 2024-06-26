from django.urls import path
from .views import inicio_view, usuario_view, endereco_view, enderecoEntrega_view, login_view, tipoUsuario_view, codVerif_view, estabelecimento_view, cupom_view, categoria_view, produto_view, cuponsUsuario_view, pedido_view, itemPedido_view, formaPagamento_view, cartao_view, pagamento_view, etapaPedido_view

urlpatterns = [
    # Inicio
    path('', inicio_view.exibir_urls_view),
    # Usuario- Privado individualmente
    path("usuarios", usuario_view.exibir_usuarios_view),
    path("usuarios/ler/<str:pk>", usuario_view.exibir_usuario_view),
    path("telefoneUsu/ler/<str:pk>",
         usuario_view.exibir_usuario_por_telefone_view),
    path("usuarios/criar/completo", usuario_view.criar_usuarioCompleto_view),
    path("usuarios/criar", usuario_view.criar_usuario_view),
    path("usuarios/editar/<str:pk>", usuario_view.editar_usuario_view),
    path("usuarios/deletar/<str:pk>", usuario_view.deletar_usuario_view),
    path("usuarios/inativar/<str:pk>", usuario_view.inativar_usuario_view),
    path("usuarios/ativar/<str:pk>", usuario_view.ativar_usuario_view),
    # Endereco - Privado individualmente
    path("enderecos", endereco_view.exibir_enderecos_view),
    path("enderecos/ler/<str:pk>", endereco_view.exibir_endereco_view),
    path("enderecos/criar", endereco_view.criar_endereco_view),
    path("enderecos/editar/<str:pk>", endereco_view.editar_endereco_view),
    path("enderecos/deletar/<str:pk>", endereco_view.deletar_endereco_view),
    # Endereco Entrega - Privado individualmente
    path("enderecos/usuario/<str:pk>",
         enderecoEntrega_view.exibir_enderecosUsuario_view),
    path("enderecosEntrega", enderecoEntrega_view.exibir_enderecosEntrega_view),
    #     path("enderecosEntrega/ler/<str:pk>", enderecoEntrega_view.exibir_enderecoEntrega_view),
    path("enderecos/usuario/criar/<str:pk>",
         enderecoEntrega_view.criar_enderecoUsuario_view),
    #     path("enderecosEntrega/criar", enderecoEntrega_view.criar_enderecoEntrega_view),
    path("enderecosEntrega/editar/<str:pk>",
         enderecoEntrega_view.editar_enderecoEntrega_view),
    path("enderecosEntrega/deletar/<str:pk>",
         enderecoEntrega_view.deletar_enderecoEntrega_view),
    # Cartões - Privado individualmente
    path("cartoes", cartao_view.exibir_cartoes_view),
    path("cartoes/usuario/<str:pk>", cartao_view.exibir_cartoesUsuario_view),
    path("cartoes/ler/<str:pk>", cartao_view.exibir_cartao_view),
    path("cartoes/criar", cartao_view.criar_cartao_view),
    path("cartoes/editar/<str:pk>", cartao_view.editar_cartao_view),
    path("cartoes/deletar/<str:pk>", cartao_view.deletar_cartao_view),
    # Etapa pedido
    path("etapasPedido", etapaPedido_view.exibir_etapasPedido_view),
    path("etapasPedido/ler/<str:pk>", etapaPedido_view.exibir_etapaPedido_view),
    path("etapasPedidoPorNome", etapaPedido_view.exibir_etapaPedidoPorNome_view),
    # path("etapasPedido/criar", pedido_view.criar_pedido_view),
    # path("etapasPedido/editar/<str:pk>", pedido_view.editar_pedido_view),
    # path("etapasPedido/deletar/<str:pk>", pedido_view.deletar_pedido_view),
    # Pedido - Privado individualmente
    path("pedidos", pedido_view.exibir_pedidos_view),
    path("pedidos/ler/<str:pk>", pedido_view.exibir_pedido_view),
    path("pedidos/criar", pedido_view.criar_pedido_view),
    path("pedidos/editar/<str:pk>", pedido_view.editar_pedido_view),
    path("pedidos/deletar/<str:pk>", pedido_view.deletar_pedido_view),
    # Pedidos Por ID Usuario - Privado individualmente
    path("pedidos/usuario", pedido_view.exibir_pedidosUsuario_view),
    path("ultimoPedido/usuario/ler", pedido_view.exibir_ultimoPedido_view),
    path("ultimoPedido/usuario/editar", pedido_view.editar_ultimoPedido_view),
    path("ultimoPedido/usuario/deletar", pedido_view.deletar_ultimoPedido_view),
    # ItemPedido - Privado individualmente
    path("itensPedidos", itemPedido_view.exibir_itensPedidos_view),
    #     path("itensPedidos/ler/<str:pk>", itemPedido_view.exibir_itemPedido_view),
    path("itensPedidos/criar", itemPedido_view.criar_itemPedido_view),
    #     path("itensPedidos/editar/<str:pk>", itemPedido_view.editar_itemPedido_view),
    #     path("itensPedidos/deletar/<str:pk>", itemPedido_view.deletar_itemPedido_view),
    # FormaPagamento -
    path("formaPagamento", formaPagamento_view.exibir_formasPagamento_view),
    path("formaPagamento/ler/<str:pk>",
         formaPagamento_view.exibir_formaPagamento_view),
    path("formaPagamentoPorNome",
         formaPagamento_view.exibir_formaPagamentoPorNome_view),
    # Endereco - Privado individualmente
    path("tipoUsuario", tipoUsuario_view.exibir_tipoUsuarios_view),
    path("tipoUsuario/ler/<str:pk>", tipoUsuario_view.exibir_tipoUsuario_view),
    path("tipoUsuario/criar", tipoUsuario_view.criar_tipoUsuario_view),
    path("tipoUsuario/editar/<str:pk>",
         tipoUsuario_view.editar_tipoUsuario_view),
    path("tipoUsuario/deletar/<str:pk>",
         tipoUsuario_view.deletar_tipoUsuario_view),
    # Efetuar Pagamento
    path("pagamento",
         pagamento_view.efetuarPagamento_view),
    # Estabelecimentos
    path("estabelecimentos", estabelecimento_view.exibir_estabelecimentos_view),
    path("estabelecimentos/ler/<str:pk>",
         estabelecimento_view.exibir_estabelecimento_view),
    # Cupons
    path("cupons", cupom_view.exibir_cupons_view),
    path("cupons/ler/<str:pk>",
         cupom_view.exibir_cupom_view),
    # CuponsUsuario
    path("cuponsUsuario", cuponsUsuario_view.exibir_cuponsUsuario_view),
    path("cuponsUsuario/ler/<str:pk>",
         cuponsUsuario_view.exibir_cupomUsuario_view),
    # Categorias
    path("categorias", categoria_view.exibir_categorias_view),
    path("categorias/ler/<str:pk>",
         categoria_view.exibir_categoria_view),
    # Produtos
    path("produtos", produto_view.exibir_produtos_view),
    path("produtos/ler/<str:pk>",
         produto_view.exibir_produto_view),
    path("produtosEstab/<str:pk>",
         produto_view.exibir_produtosEstab_view),

    # Codigo de Verificação
    path('codVerif', codVerif_view.enviar_codigo_view),
    # Login
    path('login', login_view.login_user_view),
    # Validar Token
    path('validarToken', login_view.validar_token_view),
]
