from django.urls import path
from .views import inicio_view
# from .views import login_view, inicio_view
urlpatterns = [
    # Inicio
    path('',inicio_view.exibir_urls_view),
    # Login
    # path('login', login_view.login_user_view),
]