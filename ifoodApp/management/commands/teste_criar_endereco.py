from psycopg2 import Binary
from django.core.management.base import BaseCommand
import os
import psycopg2
import json
# Conectar ao banco de dados
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
path_json = './ifoodApp/management/commands/databanco/dados.json'
with open(path_json, 'r', encoding='utf-8') as arquivo:
    dados_json = json.load(arquivo)
# Abrir um cursor para executar consultas
cur = conn.cursor()

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
