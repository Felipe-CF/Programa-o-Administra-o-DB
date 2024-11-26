from rest_framework.routers import DefaultRouter
from backend.view.ItemView import ItemViewSet

item_router = DefaultRouter()
item_router.register('item', ItemViewSet, basename='item')