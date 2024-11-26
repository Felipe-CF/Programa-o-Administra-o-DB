from rest_framework import viewsets
from backend.models.Vendedor import Vendedor
from backend.serializer.VendedorSerializer import VendedorSerializer

class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer 