from django.urls import path
from .views import inicio_view, usuario_view, endereco_view, enderecoEntrega_view, login_view

urlpatterns = [
    # Inicio
    path('',inicio_view.exibir_urls_view),
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
    # Endereco Entrega - Privado individualmente alunos e professores
    path("enderecosEntrega", enderecoEntrega_view.exibir_enderecosEntrega_view),
    path("enderecosEntrega/ler/<str:pk>", enderecoEntrega_view.exibir_enderecoEntrega_view),
    path("enderecosEntrega/criar", enderecoEntrega_view.criar_enderecoEntrega_view),
    path("enderecosEntrega/editar/<str:pk>", enderecoEntrega_view.editar_enderecoEntrega_view),
    path("enderecosEntrega/deletar/<str:pk>", enderecoEntrega_view.deletar_enderecoEntrega_view),
    # Login
    path('login', login_view.login_user_view),
]