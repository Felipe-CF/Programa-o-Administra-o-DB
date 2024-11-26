from rest_framework import viewsets
from backend.models.Item import Item
from backend.serializer.ItemSerializer import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer 