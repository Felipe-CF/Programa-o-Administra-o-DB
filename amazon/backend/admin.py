from django.contrib import admin
from backend.models.Item import Item
from backend.models.Pedido import Pedido
from backend.models.Cliente import Cliente
from backend.models.Endereco import Endereco
from backend.models.Vendedor import Vendedor
from backend.models.FormaPagamento import FormaPagamento


admin.site.register(Item)
admin.site.register(Pedido)
admin.site.register(Cliente)
admin.site.register(Vendedor)
admin.site.register(Endereco)
admin.site.register(FormaPagamento)