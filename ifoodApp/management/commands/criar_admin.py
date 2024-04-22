from django.core.management.base import BaseCommand
from ifoodApp.models import Usuario, TipoUsuario
from ifoodApp.controllers.tipoUsuario_controller import criar_tipoUsuario
from ifoodApp.controllers.usuario_controller import criar_usuario
import os


class Command(BaseCommand):
    help = 'Cria um usuário administrador inicial'

    def handle(self, *args, **kwargs):
        # Criar tipo de usuario ADMIn
        criar_tipoUsuario({
            "nomeTipoUsuario": "Admin"
        })
        # Criar Usuario ADMIN
        if not Usuario.objects.all():
            criar_usuario({
                "nomeUsu": os.environ.get("DJANGO_SUPERUSER_USERNAME"),
                "telefoneUsu": os.environ.get("DJANGO_SUPERUSER_TELEFONE"),
                "cpf": os.environ.get("DJANGO_SUPERUSER_CPF"),
                # "emailUsu": os.environ.get("DJANGO_SUPERUSER_EMAIL"),
                "tipoUsuarioId": str(TipoUsuario.objects.get(nomeTipoUsuario="Admin").tipoUsuarioId)
            })
            if Usuario.objects.get(cpf=os.environ.get("DJANGO_SUPERUSER_CPF")):
                self.stdout.write(self.style.SUCCESS(
                    f'USUARIO_ADM_ID_{Usuario.objects.get(cpf=os.environ.get("DJANGO_SUPERUSER_CPF")).usuarioId} criado com sucesso!'))
            else:
                self.stdout.write(self.style.SUCCESS(
                    'Falha ao criar Usuário Administrador Padrão!'))

        else:
            self.stdout.write(self.style.WARNING(
                'Usuário administrador já existe.'))
