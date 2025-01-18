import uuid
from django.db import models
from biblioteca.api.models.editora import Editora


class Autor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100, help_text="Nome do autor")
    editora = models.ForeignKey(Editora, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return f"Nome: {self.nome}"