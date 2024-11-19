from rest_framework import viewsets
from backend.models.Cliente import Cliente
from backend.serializers.ClienteSerializer import ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer 