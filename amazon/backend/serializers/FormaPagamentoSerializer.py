from rest_framework import serializers
from backend.models.FormaPagamento import FormaPagamento

class FormaPagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaPagamento
        fields = '__all__' 