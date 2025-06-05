# Django Imports
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, TemplateView

from .models import Inventory


class InventoryListView(TemplateView):
    template_name = "inventory/inventory_list.html"

    def get(self, request):
        context = {
            "title": "Inventory Dashboard",
            "description": "You are looking at the list of inventory in the system.",
        }
        return render(request, self.template_name, context)


class InventoryDetailView(DetailView):
    model = Inventory
    context_object_name = "inventory"
    template_name = "inventory/inventory_detail.html"
