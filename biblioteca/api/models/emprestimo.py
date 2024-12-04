import uuid
from django.db import models
from datetime import datetime, timedelta
from biblioteca.api.models.livro import Livro
from biblioteca.api.models.usuario import Usuario


class Emprestimo(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    usuario_id = models.OneToOneField(Usuario)
    livro_id = models.OneToOneField(Livro)
    data_entrega = models.DateTimeField(default=(datetime.now() + timedelta(days=10)))

    class Meta:
        verbose_name = "Emprestimo"
        verbose_name_plural = "Emprestimos"

    def __str__(self):
        return f"Prazo: {self.data_entrega}"
    
