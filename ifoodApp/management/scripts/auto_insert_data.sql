DO $$
DECLARE
    i integer := 1;
    cnpj_gerado char(14);
    telefone_gerado char(10);
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

        INSERT INTO "ifoodApp_estabelecimento" ("nomeEstab", "telefoneEstab", "cnpj", "emailEstab")
        VALUES ('Estabelecimento_' || i, telefone_gerado, cnpj_gerado, 'estabelecimento_' || i || '@restaurante.com.br');
    END LOOP;
END $$;