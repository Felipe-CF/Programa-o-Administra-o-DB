from rest_framework import serializers
from backend.models.Vendedor import Vendedor

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = '__all__' 