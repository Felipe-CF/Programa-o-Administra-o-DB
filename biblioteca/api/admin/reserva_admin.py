from rest_framework import viewsets
from biblioteca.api.serializers import *
from biblioteca.api.models.usuario import Reserva

class ReservaView(viewsets.ViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer 
