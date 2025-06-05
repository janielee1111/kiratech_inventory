# Django Imports
from django.contrib import admin

from .models import Inventory, Supplier


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "created_datetime"]


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass
