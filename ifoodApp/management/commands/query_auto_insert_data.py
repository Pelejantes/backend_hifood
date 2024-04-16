from django.core.management.base import BaseCommand
from django.conf import settings
import os
import subprocess
import binascii

class Command(BaseCommand):
    help = 'Executa um script SQL para inserir dados automaticamente'

    def handle(self, *args, **kwargs):
        if os.getenv("AUTO_INSERT_DATA"):
            try:
                # Caminho para o arquivo .sql
                sql_file_path = os.path.join(settings.BASE_DIR, './ifoodApp/assets/img/imagem_default.png')
                # Comando para executar o arquivo .sql
                with open(sql_file_path, 'rb') as f:
                    imagem_bytes = f.read()
                imagem_hex = r'\\x' + binascii.hexlify(imagem_bytes).decode('utf-8')
                subprocess.run(
                    [
                        'psql',
                        '-U', os.getenv('PG_USER'), # Usuário do banco de dados
                        '-h', os.getenv('PG_HOST'), # Host do banco de dados
                        '-p', os.getenv('PG_PORT'), # Porta do banco de dados
                        '-c', f"""
        DO $$
DECLARE
    i integer := 1;
    cnpj_gerado char(14);
    telefone_gerado char(10);
    dados_imagem bytea;
BEGIN
    FOR i IN 1..50 LOOP
        -- Gera um CNPJ único
        cnpj_gerado := LPAD((ROUND(RANDOM() * 99999999999999))::text, 14, '0');
        WHILE EXISTS (SELECT 1 FROM "ifoodApp_estabelecimento" WHERE "cnpj" = cnpj_gerado) LOOP
            cnpj_gerado := LPAD((ROUND(RANDOM() * 99999999999999))::text, 14, '0');
        END LOOP;

        -- Gera um telefone único
        telefone_gerado := LPAD((ROUND(RANDOM() * 9999999999))::text, 10, '0');
        WHILE EXISTS (SELECT 1 FROM "ifoodApp_estabelecimento" WHERE "telefoneEstab" = telefone_gerado) LOOP
            telefone_gerado := LPAD((ROUND(RANDOM() * 9999999999))::text, 10, '0');
        END LOOP;

        -- Converte os dados binários da imagem para uma string codificada em base64
        dados_imagem := ENCODE(E'{imagem_hex}', 'base64');

        INSERT INTO "ifoodApp_estabelecimento" ("nomeEstab", "telefoneEstab", "cnpj", "emailEstab", "imagemEstab")
        VALUES ('Estabelecimento_' || i, telefone_gerado, cnpj_gerado, 'estabelecimento_' || i || '@restaurante.com.br', dados_imagem);
    END LOOP;
END $$;
        """
                    ],
                    env={'PGPASSWORD': os.getenv('POSTGRES_PASSWORD')},
                    check=True
                )
                self.stdout.write(self.style.SUCCESS('Dados inseridos com sucesso!'))
            except subprocess.CalledProcessError as e:
                self.stdout.write(self.style.ERROR('Erro ao inserir dados: {}'.format(e)))
