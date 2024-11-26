from rest_framework.routers import DefaultRouter
from backend.view.PedidoView import PedidoViewSet

pedido_router = DefaultRouter()
pedido_router.register('pedido', PedidoViewSet, basename='pedido')