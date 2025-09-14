FROM python:3.10

# Set unbuffered output for python
ENV PYTHONUNBUFFERED 1

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt .

# Copia a imagem default para o diretório /app/assets/img dentro do container
COPY ./ifoodApp/assets/img/imagem_default.png /app/assets/img/

RUN pip install -r requirements.txt

# Instala o cliente do PostgreSQL
RUN apt-get update && apt-get install -y postgresql-client

# Bundle app source
COPY . .

# # Expose port
# EXPOSE 8000
COPY django.sh /app/
RUN sed -i 's/\r$//' django.sh
RUN chmod +x /app/django.sh

# entrypoint to run the django.sh file
ENTRYPOINT ["/app/django.sh"]

# CMD gunicorn --bind 0.0.0.0:$PORT project.wsgi:application