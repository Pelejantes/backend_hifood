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


# Expose port
EXPOSE 8000
COPY django.sh /app/
RUN sed -i 's/\r$//' django.sh
RUN chmod +x /app/django.sh

# entrypoint to run the django.sh file
ENTRYPOINT ["/app/django.sh"]