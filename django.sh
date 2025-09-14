#!/bin/sh
set -e
echo "Waiting for database..."

# Aguarda o banco de dados estar pronto
while ! pg_isready -h $PG_HOST -p $PG_PORT -U $PG_USER -d $PG_DB; do
  sleep 2
done

echo "Database is up - continuing..."
# Criando Migrações
echo "Creating Migrations..."
python manage.py makemigrations ifoodApp
echo "===================================="

# Iniciando Migrações
echo "Starting Migrations..."
python manage.py migrate
echo "===================================="

# Chama o comando para criar dados populados caso true
if [ "$AUTO_INSERT_DATA" = 1 ]; then
    python manage.py auto_insert_data
    echo "===================================="
fi

# Chama o comando para criar o usuário administrador
python manage.py criar_admin
echo "===================================="

# Coleta todos os arquivos estáticos em um único diretório que o Gunicorn possa acessar.
# python manage.py collectstatic
# echo "===================================="

#  Iniciando Servidor
echo "Iniciando Servidor..."
python manage.py runserver 0.0.0.0:$PORT
# exec gunicorn --bind 0.0.0.0:$PORT project.wsgi:application
echo "===================================="