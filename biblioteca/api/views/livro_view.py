from rest_framework import viewsets
from biblioteca.api.serializers import *
from biblioteca.api.models.livro import Livro
from biblioteca.api.models.editora import Editora
from biblioteca.api.models.emprestimo import Emprestimo
from biblioteca.api.models.usuario import Usuario

class LivroView(viewsets.ViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer 