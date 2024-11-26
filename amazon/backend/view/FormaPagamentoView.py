from rest_framework import viewsets
from backend.models.FormaPagamento import FormaPagamento
from backend.serializer.FormaPagamentoSerializer import FormaPagamentoSerializer

class FormaPagamentoViewSet(viewsets.ModelViewSet):
    queryset = FormaPagamento.objects.all()
    serializer_class = FormaPagamentoSerializer 