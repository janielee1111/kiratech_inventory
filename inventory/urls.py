from django.urls import path
from .views import InventoryListView, InventoryDetailView

urlpatterns = [
    path('', InventoryListView.as_view(), name='inventory_list_view'),
    path('<int:pk>/', InventoryDetailView.as_view(), name='inventory_detail_view')
]
