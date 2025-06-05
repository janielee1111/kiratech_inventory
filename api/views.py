from rest_framework import viewsets

from inventory.models import Inventory

from .serializers import InventorySerializer


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all().order_by("-created_datetime")
    serializer_class = InventorySerializer
    search_fields = ["name", "supplier__name"]
