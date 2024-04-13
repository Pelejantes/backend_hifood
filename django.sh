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
echo "===================================="

# Coleta todos os arquivos estáticos em um único diretório que o Gunicorn possa acessar.
python manage.py collectstatic
echo "===================================="

#  Iniciando Servidor
echo "Starting Gunicorn..."
python manage.py runserver 0.0.0.0:$PORT
# exec gunicorn --bind 0.0.0.0:$PORT project.wsgi:application
echo "===================================="