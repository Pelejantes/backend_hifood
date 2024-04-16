from django.urls import path
from .views import inicio_view, usuario_view, endereco_view, enderecoEntrega_view, login_view, tipoUsuario_view, codVerif_view, estabelecimento_view, cupom_view, categoria_view, produto_view

urlpatterns = [
    # Inicio
    path('', inicio_view.exibir_urls_view),
    # Usuario- Privado individualmente alunos e professores
    path("usuarios", usuario_view.exibir_usuarios_view),
    path("usuarios/ler/<str:pk>", usuario_view.exibir_usuario_view),
    path("usuarios/criar/completo", usuario_view.criar_usuarioCompleto_view),
    path("usuarios/criar", usuario_view.criar_usuario_view),
    path("usuarios/editar/<str:pk>", usuario_view.editar_usuario_view),
    path("usuarios/deletar/<str:pk>", usuario_view.deletar_usuario_view),
    path("usuarios/inativar/<str:pk>", usuario_view.inativar_usuario_view),
    path("usuarios/ativar/<str:pk>", usuario_view.ativar_usuario_view),
    # Endereco - Privado individualmente alunos e professores
    path("enderecos", endereco_view.exibir_enderecos_view),
    path("enderecos/ler/<str:pk>", endereco_view.exibir_endereco_view),
    path("enderecos/criar", endereco_view.criar_endereco_view),
    path("enderecos/editar/<str:pk>", endereco_view.editar_endereco_view),
    path("enderecos/deletar/<str:pk>", endereco_view.deletar_endereco_view),
    # Endereco - Privado individualmente alunos e professores
    path("tipoUsuario", tipoUsuario_view.exibir_tipoUsuarios_view),
    path("tipoUsuario/ler/<str:pk>", tipoUsuario_view.exibir_tipoUsuario_view),
    path("tipoUsuario/criar", tipoUsuario_view.criar_tipoUsuario_view),
    path("tipoUsuario/editar/<str:pk>", tipoUsuario_view.editar_tipoUsuario_view),
    path("tipoUsuario/deletar/<str:pk>",
         tipoUsuario_view.deletar_tipoUsuario_view),
    # Endereco Entrega - Privado individualmente alunos e professores
    path("enderecosEntrega", enderecoEntrega_view.exibir_enderecosEntrega_view),
    path("enderecosEntrega/ler/<str:pk>",
         enderecoEntrega_view.exibir_enderecoEntrega_view),
    path("enderecosEntrega/criar", enderecoEntrega_view.criar_enderecoEntrega_view),
    path("enderecosEntrega/editar/<str:pk>",
         enderecoEntrega_view.editar_enderecoEntrega_view),
    path("enderecosEntrega/deletar/<str:pk>",
         enderecoEntrega_view.deletar_enderecoEntrega_view),

    # Estabelecimentos
    path("estabelecimentos", estabelecimento_view.exibir_estabelecimentos_view),
    path("estabelecimentos/ler/<str:pk>",
         estabelecimento_view.exibir_estabelecimento_view),
    # Cupons
    path("cupons", cupom_view.exibir_cupons_view),
    path("cupons/ler/<str:pk>",
         cupom_view.exibir_cupom_view),
    # Categorias
    path("categorias", categoria_view.exibir_categorias_view),
    path("categorias/ler/<str:pk>",
         categoria_view.exibir_categoria_view),
    # Produtos
    path("produtos", produto_view.exibir_produtos_view),
    path("produtos/ler/<str:pk>",
         produto_view.exibir_produto_view),

    # Codigo de Verificação
    path('codVerif', codVerif_view.enviar_codigo_view),
    # Login
    path('login', login_view.login_user_view),
]
