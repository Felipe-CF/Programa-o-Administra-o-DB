from rest_framework import viewsets
from backend.models.Pedido import Pedido
from backend.serializer.PedidoSerializer import PedidoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer