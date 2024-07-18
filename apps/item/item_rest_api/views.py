from rest_framework import viewsets

from apps.item.item_rest_api.serializers import ItemSerializers
from apps.item.models import Item


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers