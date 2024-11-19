from rest_framework import serializers
from backend.models.Item import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__' 