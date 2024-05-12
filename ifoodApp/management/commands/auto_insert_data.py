from psycopg2 import Binary
from django.core.management.base import BaseCommand
import os
import psycopg2
import binascii


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
        with open('./ifoodApp/assets/img/estabelecimento_default.jpg', 'rb') as f:
            imagemEstab = f.read()
        imagemEstab = Binary(imagemEstab)
        with open('./ifoodApp/assets/img/produto_default.jpg', 'rb') as f:
            imagemProduto = f.read()
        imagemProduto = Binary(imagemProduto)
        

        # Script SQL para inserir dados
        query = f"""
        DO $$
DECLARE
    i integer := 1;
    cnpj_gerado char(14);
    telefone_gerado char(10);
BEGIN
    -- GERAR TIPO USUARIO
    IF NOT EXISTS (SELECT 1 FROM "public"."ifoodApp_tipousuario" WHERE "nomeTipoUsuario" = 'Admin') THEN
        INSERT INTO "public"."ifoodApp_tipousuario" ("nomeTipoUsuario") VALUES ('Admin');
    END IF;
    IF NOT EXISTS (SELECT 1 FROM "public"."ifoodApp_tipousuario" WHERE "nomeTipoUsuario" = 'Comprador') THEN
        INSERT INTO "public"."ifoodApp_tipousuario" ("nomeTipoUsuario") VALUES ('Comprador');
    END IF;
    IF NOT EXISTS (SELECT 1 FROM "public"."ifoodApp_tipousuario" WHERE "nomeTipoUsuario" = 'Entregador') THEN
        INSERT INTO "public"."ifoodApp_tipousuario" ("nomeTipoUsuario") VALUES ('Entregador');
    END IF;
    IF NOT EXISTS (SELECT 1 FROM "public"."ifoodApp_tipousuario" WHERE "nomeTipoUsuario" = 'Estabelecimento') THEN
        INSERT INTO "public"."ifoodApp_tipousuario" ("nomeTipoUsuario") VALUES ('Estabelecimento');
    END IF;


    -- GERAR TIPO FORMA PAGAMENTO
    IF NOT EXISTS (SELECT 1 FROM "public"."ifoodApp_formapag" WHERE "nomeFormaPag" = 'Pix') THEN
        INSERT INTO "public"."ifoodApp_formapag" ("nomeFormaPag") VALUES ('Pix');
    END IF;
    IF NOT EXISTS (SELECT 1 FROM "public"."ifoodApp_formapag" WHERE "nomeFormaPag" = 'Débito') THEN
        INSERT INTO "public"."ifoodApp_formapag" ("nomeFormaPag") VALUES ('Débito');
    END IF;
    IF NOT EXISTS (SELECT 1 FROM "public"."ifoodApp_formapag" WHERE "nomeFormaPag" = 'Crédito') THEN
        INSERT INTO "public"."ifoodApp_formapag" ("nomeFormaPag") VALUES ('Crédito');
    END IF;


    -- GERAR ETAPA PEDIDO
    IF NOT EXISTS (SELECT 1 FROM "public"."ifoodApp_etapapedido" WHERE "etapaPedido" = 'Aguardando Pagamento') THEN
        INSERT INTO "public"."ifoodApp_etapapedido" ("etapaPedido") VALUES ('Aguardando Pagamento');
    END IF;
    IF NOT EXISTS (SELECT 1 FROM "public"."ifoodApp_etapapedido" WHERE "etapaPedido" = 'Preparando Pedido') THEN
        INSERT INTO "public"."ifoodApp_etapapedido" ("etapaPedido") VALUES ('Preparando Pedido');
    END IF;
    IF NOT EXISTS (SELECT 1 FROM "public"."ifoodApp_etapapedido" WHERE "etapaPedido" = 'Em Rota de Entrega') THEN
        INSERT INTO "public"."ifoodApp_etapapedido" ("etapaPedido") VALUES ('Em Rota de Entrega');
    END IF;
    IF NOT EXISTS (SELECT 1 FROM "public"."ifoodApp_etapapedido" WHERE "etapaPedido" = 'Entregue') THEN
        INSERT INTO "public"."ifoodApp_etapapedido" ("etapaPedido") VALUES ('Entregue');
    END IF;


    FOR i IN 1..50 LOOP

        -- GERAR CATEGORIA
        INSERT INTO "public"."ifoodApp_categoria" ("nomeCategoria","imagem") VALUES ('Nome_categoria_' || i ,{imagemCategoria});
        
        
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
        INSERT INTO "ifoodApp_estabelecimento" ("nomeEstab", "telefoneEstab", "cnpj", "emailEstab", "imagemEstab","categoriaId_id")
        VALUES ('Estabelecimento_' || i, telefone_gerado, cnpj_gerado, 'estabelecimento_' || i || '@restaurante.com.br', {imagemEstab}, i);
        


        -- GERAR REGRACUPOM
        INSERT INTO "public"."ifoodApp_regracupom" ("descricaoRegra") VALUES ('Descrição_Regra_' || i  );
        

        
        -- GERAR CUPONS
        INSERT INTO "public"."ifoodApp_cupom" ("valorDesconto", "dataValidade", "limiteUso", "valorMinimo", "categoriaId_id", "regraCupomId_id") VALUES
        (i, NOW(), i, i * i, i, i);

        
        -- GERAR CUPONS_USUARIO
        IF EXISTS (SELECT 1 FROM "public"."ifoodApp_usuario" WHERE "usuarioId" = 1) THEN
        INSERT INTO "public"."ifoodApp_cuponsusuario" ("usuarioId_id", "cupomId_id") VALUES (1, i);
	    END IF;
        

        -- GERAR PRODUTO
        INSERT INTO "public"."ifoodApp_produto"("nomeProd", "disponibilidade", "preco", "imagemProd","alcoolico", "descricao", "categoriaId_id", "estabelecimentoId_id") VALUES
        ( 'Nome_produto_'||i, 'true', 100, {imagemProduto},'false', 'Descricao_'||i, i, i);



    END LOOP;
    
END $$;
        """

        # Executar a consulta SQL usando parâmetros de consulta
        cur.execute(query)

        # Commitar as alterações
        conn.commit()

        # Fechar o cursor e a conexão
        cur.close()
        conn.close()

        self.stdout.write(self.style.SUCCESS('Dados inseridos com sucesso.'))
