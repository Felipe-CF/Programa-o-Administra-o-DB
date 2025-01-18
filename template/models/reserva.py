import uuid
from datetime import datetime, timedelta
from django.db import models
from biblioteca.api.models.usuario import Usuario, Livro


class Reserva(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario_id = models.OneToOneField(Usuario)
    livro_id = models.OneToOneField(Livro)
    termino_reserva = models.DateTimeField(default=(datetime.now() + timedelta(days=3)))

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self):
        return f"Prazo de liberação: {self.termino_reserva}"


