import uuid
from django.db import models


class Editora(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Editora"
        verbose_name_plural = "Editoras"
        
    def __str__(self):
        return f"Editora: {self.nome}   Localização: {self.localizacao}"