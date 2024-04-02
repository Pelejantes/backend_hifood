#!/bin/sh

# Função para aguardar o Postgres ficar pronto
# wait_for_db() {
#   echo "Waiting for Postgres to start..."
#   until pg_isready -h db -p 5432; do
#     sleep 0.1
#   done
#   echo "Postgres started"
# }

# Aguarda o Postgres iniciar
# wait_for_db

# Criando Migrações
echo "Creating Migrations..."
python manage.py makemigrations ifoodApp
echo "===================================="

# Iniciando Migrações
echo "Starting Migrations..."
python manage.py migrate
echo "===================================="

# Iniciando Servidor
echo "Starting Server..."
python manage.py runserver 0.0.0.0:8000
