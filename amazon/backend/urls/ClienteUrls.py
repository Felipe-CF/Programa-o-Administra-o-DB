from rest_framework.routers import DefaultRouter
from backend.view.ClienteView import ClienteViewSet

cliente_router = DefaultRouter()
cliente_router.register('cliente', ClienteViewSet, basename='cliente')