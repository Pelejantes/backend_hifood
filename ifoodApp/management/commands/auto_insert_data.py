from django.core.management.base import BaseCommand
from django.conf import settings
import os
import subprocess

class Command(BaseCommand):
    help = 'Executa um script SQL para inserir dados automaticamente'

    def handle(self, *args, **kwargs):
        if os.getenv("AUTO_INSERT_DATA"):
            try:
                # Caminho para o arquivo .sql
                sql_file_path = os.path.join(settings.BASE_DIR, '/app/scripts/auto_insert_data.sql')
                # Comando para executar o arquivo .sql
                subprocess.run(
                    [
                        'psql',
                        '-U', os.getenv('POSTGRES_USER'), # Usuário do banco de dados
                        '-h', os.getenv('POSTGRES_HOST'), # Host do banco de dados
                        '-p', os.getenv('DB_PORT','5432'), # Porta do banco de dados
                        '-a', '-f', sql_file_path
                    ],
                    env={'PGPASSWORD': os.getenv('POSTGRES_PASSWORD')},
                    check=True
                )
                self.stdout.write(self.style.SUCCESS('Dados inseridos com sucesso!'))
            except subprocess.CalledProcessError as e:
                self.stdout.write(self.style.ERROR('Erro ao inserir dados: {}'.format(e)))
