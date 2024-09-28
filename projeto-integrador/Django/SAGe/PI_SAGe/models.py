from django.db import models


# Create your models here.para criar um modelo: python manage.py makemigrations
#E: python manage.py migrate
class Pacientes(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()
    cpf = models.TextField()
    data_consulta = models.DateField()
    telefone = models.TextField(max_length=15)
    
class Medicos(models.Model):
    id_medico = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    data_disponivel = models.DateField()
    telefone = models.TextField(max_length=15)
    
