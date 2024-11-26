from rest_framework import serializers
from backend.models.Pedido import Pedido

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__' 