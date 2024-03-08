from django.urls import path
from .views import inicio_view, usuario_view, endereco_view

urlpatterns = [
    # Inicio
    path('',inicio_view.exibir_urls_view),
    # Usuario- Privado individualmente alunos e professores
    path("usuarios", usuario_view.exibir_usuarios_view),
    path("usuarios/ler/<str:pk>", usuario_view.exibir_usuario_view),
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
    path("enderecos/deletar/<str:pk>", endereco_view.deletar_endereco_view)
    # Login
    # path('login', login_view.login_user_view),
]