from rest_framework import viewsets
from biblioteca.api.serializers import *
from biblioteca.api.models.emprestimo import Emprestimo
from biblioteca.api.models.usuario import Usuario

class EmprestimoView(viewsets.ViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer 
