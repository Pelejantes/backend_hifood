#!/bin/sh
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

# # Iniciando Servidor
# echo "Starting Server..."
# python manage.py runserver 0.0.0.0:8000
