from rest_framework.routers import DefaultRouter
from backend.view.EnderecoView import EnderecoViewSet

endereco_router = DefaultRouter()
endereco_router.register('endereco', EnderecoViewSet, basename='endereco')