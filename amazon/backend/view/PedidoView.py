from django.db import models
from backend.models.Item import Item
from backend.models.Cliente import Cliente
from backend.models.Vendedor import Vendedor
from backend.models.Endereco import Endereco
from backend.models.FormaPagamento import FormaPagamento


class Pedido(models.Model):
    itens = models.ManyToManyField(Item)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    endereco_entrega = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    forma_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateTimeField()
    
    def __str__(self): 
        return f'{self.cliente} - {self.vendedor} - {self.data_pedido}'