DEPENDENCIES = """
Django==3.2.5
psycopg2-binary==2.9.1
djangorestframework==3.12.4
djangorestframework-simplejwt==5.3.0
PyJWT==2.8.0
requests==2.31.0
urllib3==1.26.12
django-cors-headers==4.1.0
python-dotenv==1.0.1
twilio==9.0.2
"""

# Função para escrever as dependências em um arquivo .txt
def write_requirements():
    with open('requirements.txt', 'w') as file:
        file.write(DEPENDENCIES.strip())

# Chame a função para executar a ação
if __name__ == "__main__":
    write_requirements()