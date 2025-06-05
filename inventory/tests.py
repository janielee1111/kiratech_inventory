import pytest
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient
from conftest import create_inventory


@pytest.mark.django_db
def test_inventory_list():
    url = reverse("inventory_list_view")
    response = APIClient().get(path=url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_inventory_detail(create_inventory):
    obj = create_inventory(
        name="Item A", description="Item A description", note="note", availability=True
    )
    url = reverse("inventory_detail_view", args=[obj.id])
    response = APIClient().get(path=url)
    assert response.status_code == status.HTTP_200_OK
