# Django Imports
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from . import views

api_v1 = DefaultRouter()
api_v1.register("inventory", views.InventoryViewSet, basename="inventory")

urlpatterns = [path("", include(api_v1.urls))]
