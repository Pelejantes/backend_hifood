from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Usuario(AbstractBaseUser):
    UsuarioId = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=250)
    telefone = models.CharField(max_length=11)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.CharField(max_length=250)
    user_type_id = models.IntegerField(default=0)
    password = models.CharField(
        max_length=128
    )  # Use um campo apropriado para senhas, como PasswordField em produção
    is_active = models.IntegerField(default=0)
    

    def __str__(self):
        return self.nome
