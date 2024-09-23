from django.db import models


# Create your models here.para criar um modelo: python manage.py makemigrations
#E: python manage.py migrate
class Cadastro(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()
    senha = models.TextField(max_length=15)
    cpf = models.TextField()
    data = models.DateField()
    telefone = models.TextField(max_length=15)
    
