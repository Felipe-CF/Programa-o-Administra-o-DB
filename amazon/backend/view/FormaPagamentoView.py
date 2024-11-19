from django.db import models

class FormaPagamento(models.Model):
    descricao = models.CharField(max_length=30) 

    def __str__(self):
        return f"descrição {self.descricao}"