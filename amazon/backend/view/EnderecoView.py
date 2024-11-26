from rest_framework import viewsets
from backend.models.Endereco import Endereco
from backend.serializer.EnderecoSerializer import EnderecoSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = Endereco 