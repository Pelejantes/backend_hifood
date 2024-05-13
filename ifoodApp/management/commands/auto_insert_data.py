import binascii
from psycopg2 import Binary
from django.core.management.base import BaseCommand
import os
import psycopg2
import json

class Command(BaseCommand):
    help = 'Executa um script SQL para inserir dados automaticamente'

    def handle(self, *args, **kwargs):
        # Conectar ao banco de dados
        conn = psycopg2.connect(
            dbname=os.getenv('PG_DB'),
            user=os.getenv('PG_USER'),
            password=os.getenv('POSTGRES_PASSWORD'),
            host=os.getenv('PG_HOST'),
            port=os.getenv('PG_PORT', '5432')
        )

        # Abrir um cursor para executar consultas
        cur = conn.cursor()

        # Ler os dados da imagem e converter para uma representação hexadecimal
        with open('./ifoodApp/assets/img/categoria_default.jpg', 'rb') as f:
            imagemCategoria = f.read()
        imagemCategoria = Binary(imagemCategoria)
    def handle(self, *args, **kwargs):
        # Conectar ao banco de dados
        conn = psycopg2.connect(
            dbname=os.getenv('PG_DB'),
            user=os.getenv('PG_USER'),
            password=os.getenv('POSTGRES_PASSWORD'),
            host=os.getenv('PG_HOST'),
            port=os.getenv('PG_PORT', '5432')
        )

        # Abrir um cursor para executar consultas
        cur = conn.cursor()
        path_json = './ifoodApp/management/commands/databanco/dados.json'

        with open(path_json, 'r', encoding='utf-8') as arquivo:
            dados_json = json.load(arquivo)


        class Dados_Regra_Negocio:
            def __init__(self, dados, descricao, nome_tabela, nome_coluna):
                self.dados = dados
                self.descricao = descricao
                self.nome_tabela = nome_tabela
                self.nome_coluna = nome_coluna
                self.query_construida = f"""\n\n--{self.descricao}"""

            def criar_query(self):
                for dado in self.dados:
                    self.query_construida += f"""\nIF NOT EXISTS (SELECT 1 FROM "public"."ifoodApp_{self.nome_tabela}" WHERE "{self.nome_coluna}" = '{dado}') THEN
                INSERT INTO "public"."ifoodApp_{self.nome_tabela}" ("{self.nome_coluna}") VALUES ('{dado}');
                END IF;""".replace(
                        "REPLACE_THIS", dado)
                return self.query_construida


        query_tipoUsuario = Dados_Regra_Negocio(**{
            "dados": ["Admin", "Comprador", "Entregador"],
            "descricao": "GERA TIPO USUARIO",
            "nome_tabela": "tipousuario",
            "nome_coluna": "nomeTipoUsuario"
        })
        query_tipoFormaPag = Dados_Regra_Negocio(**{
            "dados": ["Pix", "Débito", "Crédito"],
            "descricao": "GERA TIPO FORMA PAGAMENTO",
            "nome_tabela": "formapag",
            "nome_coluna": "nomeFormaPag"
        })
        query_etapaPedido = Dados_Regra_Negocio(**{
            "dados": ['Aguardando Pagamento', 'Preparando Pedido', 'Em Rota de Entrega', 'Entregue'],
            "descricao": "GERA TIPO ETAPAS PEDIDO",
            "nome_tabela": "etapapedido",
            "nome_coluna": "etapaPedido"
        })
        finalQuery = f"""
        DO $$
        DECLARE
        BEGIN
            {query_tipoUsuario.criar_query()}
            {query_tipoFormaPag.criar_query()}
            {query_etapaPedido.criar_query()}
        END $$;
        """
        cur.execute(finalQuery)

        for indice, categorias in enumerate(dados_json['categorias'], start=1):
            with open(categorias['imgCategoria'].replace('./assets/', './ifoodApp/management/commands/databanco/assets/'), 'rb') as f:
                imagemCategoria = f.read()
            imagemCategoria = Binary(imagemCategoria)

            query_categorias = f"""\n
            INSERT INTO "public"."ifoodApp_categoria" ("nomeCategoria","imagem") VALUES ('{categorias['nomeCategoria']}',{imagemCategoria});
            \n"""
            cur.execute(query_categorias)

        for indice, estabelecimento in enumerate(dados_json['estabelecimentos'], start=1):
            with open(estabelecimento['imagemEstab'].replace('./assets/', './ifoodApp/management/commands/databanco/assets/'), 'rb') as f:
                imagemEstab = f.read()
            imagemEstab = Binary(imagemEstab)

            with open(estabelecimento['imagemBanner'].replace('./assets/', './ifoodApp/management/commands/databanco/assets/'), 'rb') as f:
                imagemBanner = f.read()
            imagemBanner = Binary(imagemBanner)

            query_estabelecimentos = f"""\n
            INSERT INTO "ifoodApp_estabelecimento" ("nomeEstab", "telefoneEstab", "cnpj", "emailEstab", "imagemEstab","imagemBanner","categoriaId_id")
                VALUES ('{estabelecimento['nomeEstab']}', {indice}, {indice}, 'estabelecimento_' || {indice} || '@restaurante.com.br', {imagemEstab},{imagemBanner}, (select "categoriaId" from "public"."ifoodApp_categoria" WHERE "nomeCategoria" = '{estabelecimento['nomeCategoria']}'));
            \n"""
            cur.execute(query_estabelecimentos)

        for indice, produto in enumerate(dados_json['produtos'], start=1):
            with open(produto['imagemProduto'].replace('./assets/', './ifoodApp/management/commands/databanco/assets/'), 'rb') as f:
                imagemProduto = f.read()
            imagemProduto = Binary(imagemProduto)
            query_produtos = f"""\n
            INSERT INTO "public"."ifoodApp_produto"("nomeProd", "disponibilidade", "preco", "imagemProd","alcoolico", "descricao", "categoriaId_id", "estabelecimentoId_id") VALUES
                ( '{produto['nomeProduto']}', 'true', '{produto['preco']}', {imagemProduto},'false', '{produto['descricao']}',  (select "categoriaId" from "public"."ifoodApp_categoria" WHERE "nomeCategoria" = '{produto['nomeCategoria']}'),(select "estabelecimentoId" from "public"."ifoodApp_estabelecimento" WHERE "nomeEstab" = '{produto['nomeEstab']}'));
            \n"""
            cur.execute(query_produtos)

        # Commitar as alterações
        conn.commit()

        # Fechar o cursor e a conexão
        cur.close()
        conn.close()

        self.stdout.write(self.style.SUCCESS('Dados inseridos com sucesso.'))
