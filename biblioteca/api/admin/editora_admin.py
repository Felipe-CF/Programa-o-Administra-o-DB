from rest_framework import viewsets
from biblioteca.api.serializers import *
from biblioteca.api.models.editora import Editora
from biblioteca.api.models.emprestimo import Emprestimo
from biblioteca.api.models.usuario import Usuario

class EditoraView(viewsets.ViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer 