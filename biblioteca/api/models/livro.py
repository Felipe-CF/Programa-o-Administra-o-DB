from django.db import models
from biblioteca.api.models.autor import Autor
from biblioteca.api.models.editora import Editora


class Livro(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    titulo = models.CharField(max_length=100, blank=False, null=False)
    edicao = models.CharField(max_length=20, blank=False, null=False)
    autor = models.OneToOneField(Autor, on_delete=models.CASCADE)
    editora = models.OneToOneField(Editora, on_delete=models.CASCADE)
    paginas = models.BigIntegerField(max_length=20, blank=False, null=False)
    ano_publicacao = models.DateTimeField(default=None)

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"

    def __str__(self):
        return f"Titulo: {self.titulo}   Edição: {self.edicao}\nAno Publicação: {self.ano_publicacao} Páginas: {self.paginas}"
