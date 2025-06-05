from rest_framework import viewsets
from .serializers import InventorySerializer
from inventory.models import Inventory


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all().order_by("-created_datetime")
    serializer_class = InventorySerializer
    search_fields = ["name", "supplier__name"]
