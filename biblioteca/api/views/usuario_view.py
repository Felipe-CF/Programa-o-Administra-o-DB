from rest_framework import viewsets
from biblioteca.api.serializers import *
from biblioteca.api.models.usuario import Usuario

class UsuarioView(viewsets.ViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer 
