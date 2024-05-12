from psycopg2 import Binary
from django.core.management.base import BaseCommand
import os
import psycopg2
import json
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

with open('./ifoodApp/assets/img/estabelecimento_default.jpg', 'rb') as f:
    imagemEstab = f.read()
imagemEstab = Binary(imagemEstab)

with open('./ifoodApp/assets/img/banner_estab_default.svg', 'rb') as f:
    imagemBanner = f.read()
imagemBanner = Binary(imagemBanner)

with open('./ifoodApp/assets/img/produto_default.jpg', 'rb') as f:
    imagemProduto = f.read()
imagemProduto = Binary(imagemProduto)
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


class Dados_Gerais:
    def __init__(self, descricao, nome_tabela, dados):
        self.descricao = descricao
        self.nome_tabela = nome_tabela
        self.dados = dados
        self.query_construida = f"""\n\n--{self.descricao}"""

    def criar_query(self):
        colunas = ''
        valores = ''
        for chave, valor in self.dados.items():
            colunas += f'"{chave}",'
            valores += f"{valor},"
        colunas = colunas[:-1]
        valores = valores[:-1]

        self.query_construida += f"""\nINSERT INTO "public"."ifoodApp_{self.nome_tabela}" ({colunas}) VALUES ({valores});"""
        return self.query_construida


query_categoria = Dados_Gerais(**{
    "descricao": "GERA CATEGORIA",
    "nome_tabela": "categoria",
    "dados": {
        'nomeCategoria': "'Nome_categoria_' || i ",
        'imagem': f'{imagemCategoria}'
    }
})
query_estabelecimento = Dados_Gerais(**{
    "descricao": "GERA ESTABELECIMENTO",
    "nome_tabela": "estabelecimento",
    "dados": {
        'nomeEstab': "'Estabelecimento_' || i",
        'telefoneEstab': "telefone_gerado",
        'cnpj': "cnpj_gerado",
        'emailEstab': "'estabelecimento_' || i || '@restaurante.com.br'",
        'imagemEstab': f'{imagemEstab}',
        'imagemBanner': f'{imagemBanner}',
        'categoriaId_id': "i"
    }
})
query_produto = Dados_Gerais(**{
    "descricao": "GERA PRODUTO",
    "nome_tabela": "produto",
    "dados": {
    'nomeProd': "'Nome_produto_' || i",
    'disponibilidade': "'true'",
    'preco': "100",
    'imagemProd': f'{imagemProduto}',
    'alcoolico': "'false'",
    'descricao': "'Descricao_' || i",
    'categoriaId_id': "i",
    'estabelecimentoId_id': "i"
}

})

finalQuery = f"""
DO $$
DECLARE
    i integer := 1;
    cnpj_gerado char(14);
    telefone_gerado char(10);
BEGIN
    {query_tipoUsuario.criar_query()}
    {query_tipoFormaPag.criar_query()}
    {query_etapaPedido.criar_query()}
    FOR i IN 1..50 LOOP
        -- GERAR ESTABELECIMENTOS
        -- __Gera um CNPJ único
        cnpj_gerado := LPAD((ROUND(RANDOM() * 99999999999999))::text, 14, '0');
        WHILE EXISTS (SELECT 1 FROM "ifoodApp_estabelecimento" WHERE "cnpj" = cnpj_gerado) LOOP
            cnpj_gerado := LPAD((ROUND(RANDOM() * 99999999999999))::text, 14, '0');
        END LOOP;
        -- __Gera um telefone único
        telefone_gerado := LPAD((ROUND(RANDOM() * 9999999999))::text, 10, '0');
        WHILE EXISTS (SELECT 1 FROM "ifoodApp_estabelecimento" WHERE "telefoneEstab" = telefone_gerado) LOOP
            telefone_gerado := LPAD((ROUND(RANDOM() * 9999999999))::text, 10, '0');
        END LOOP;
        {query_categoria.criar_query()}
        {query_estabelecimento.criar_query()}
        {query_produto.criar_query()}

    END LOOP;
END $$;
"""
# Executar a consulta SQL usando parâmetros de consulta
# print(f"\n\n{finalQuery}\n\n")
cur.execute(finalQuery)

# Commitar as alterações
conn.commit()

# Fechar o cursor e a conexão
cur.close()
conn.close()
