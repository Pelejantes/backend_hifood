#!/bin/sh
set -e

sleep 5
# Criando Migrações
echo "Creating Migrations..."
python manage.py makemigrations ifoodApp
echo "===================================="

# Iniciando Migrações
echo "Starting Migrations..."
python manage.py migrate
echo "===================================="

# Chama o comando para criar o usuário administrador
python manage.py criar_admin

# Executando o Gunicorn
echo "Starting Gunicorn..."
exec gunicorn --bind 0.0.0.0:$PORT project.wsgi:application