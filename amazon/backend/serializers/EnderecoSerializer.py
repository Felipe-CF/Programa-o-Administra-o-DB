from rest_framework import serializers
from backend.models.Endereco import Endereco

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__' 