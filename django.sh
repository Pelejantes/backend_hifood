#!/bin/sh
sleep 10
# Criando Migrações
echo "Creating Migrations..."
python manage.py makemigrations ifoodApp
echo "===================================="

# Iniciando Migrações
# echo "Starting Migrations..."
# python manage.py migrate
# echo "===================================="

# # Iniciando Servidor
# echo "Starting Server..."
# python manage.py runserver 0.0.0.0:8000
