from rest_framework import viewsets
from biblioteca.api.serializers import *
from biblioteca.api.models.autor import Autor

class AutorView(viewsets.ViewSet):
    queryset = Autor.objects.all()
    serializer_class = UsuarioSerializer 