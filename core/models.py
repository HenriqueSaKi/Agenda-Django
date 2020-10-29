from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100) #Titulo da tabela
    descricao = models.TextField(blank=True, null=True) #Descrição que pode ser em branco ou nulo
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True) #Quando for criada, armazena a data atual
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo