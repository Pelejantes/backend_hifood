FROM python:3.8.0

# Set unbuffered output for python
ENV PYTHONUNBUFFERED 1

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Bundle app source
COPY . .

RUN chmod +x /app/django.sh

# Expose port
EXPOSE 8000

COPY django.sh /app/

# entrypoint to run the django.sh file
ENTRYPOINT ["/app/django.sh"]