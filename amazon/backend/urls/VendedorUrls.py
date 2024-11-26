from rest_framework.routers import DefaultRouter
from backend.view.VendedorView import VendedorViewSet

vendedor_router = DefaultRouter()
vendedor_router.register('vendedor', VendedorViewSet, basename='vendedor')