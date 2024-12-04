import uuid
from django.db import models
from biblioteca.api.models.livro import Livro
from biblioteca.api.models.emprestimo import Emprestimo

class Usuario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100, required=True)
    matricula = models.CharField(unique=True, max_length=14, required=True)
    login = models.CharField(unique=True, max_length=100, required=True)
    senha = models.CharField(max_length=20, blank=False)
    emprestimos = models.ForeignKey(Emprestimo, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return f"Nome completo: {self.nome}   Conselho: {self.conselho}\nEmail: {self.email} Contato: {self.contato}"
