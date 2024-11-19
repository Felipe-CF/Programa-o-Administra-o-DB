from rest_framework import serializers
from backend.models.Cliente import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__' 