from django.urls import path
from .views import inicio_view, usuario_view

urlpatterns = [
    # Inicio
    path('',inicio_view.exibir_urls_view),
    # User - Privado individualmente alunos e professores
    path("usuarios", usuario_view.exibir_usuarios_view),
    path("usuarios/ler/<str:pk>", usuario_view.exibir_usuario_view),
    path("usuarios/criar", usuario_view.criar_usuario_view),
    path("usuarios/atualizar/<str:pk>", usuario_view.atualizar_usuario_view),
    path("usuarios/deletar/<str:pk>", usuario_view.deletar_usuario_view),
    path("usuarios/inativar/<str:pk>", usuario_view.inativar_usuario_view),
    path("usuarios/ativar/<str:pk>", usuario_view.ativar_usuario_view),
    # Login
    # path('login', login_view.login_user_view),
]