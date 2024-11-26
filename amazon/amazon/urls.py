from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.view.ItemView import ItemViewSet   
from backend.view.PedidoView import PedidoViewSet
from backend.view.ClienteView import ClienteViewSet
from backend.view.EnderecoView import EnderecoViewSet   
from backend.view.VendedorView import VendedorViewSet
from backend.view.FormaPagamentoView import FormaPagamentoViewSet


router = DefaultRouter()
router.register(r'cliente', ClienteViewSet)
router.register(r'vendedor', VendedorViewSet)
router.register(r'endereco', EnderecoViewSet)
router.register(r'pedido', PedidoViewSet)
router.register(r'forma_pagamento', FormaPagamentoViewSet)
router.register(r'item', ItemViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('amazon_api/', include(router.urls)),
]