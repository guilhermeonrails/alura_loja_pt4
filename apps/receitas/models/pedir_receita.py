from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class PedirReceita(models.Model):
    nome_receita = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    date_receita = models.DateTimeField(default=datetime.now, blank=True)
    pedido_atendido = models.BooleanField(default=False)
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome_receita
   
    class Meta:
        verbose_name = 'Pedidos de receita'