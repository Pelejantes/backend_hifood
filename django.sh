#!/bin/sh

# Função para aguardar o Postgres ficar pronto
while true; do
    if pg_isready -h db -p 5432; then
        break
    fi
    sleep 1
done
sleep(2)
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
