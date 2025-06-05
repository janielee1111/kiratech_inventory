import pytest

from inventory.models import Inventory, Supplier


@pytest.fixture
def create_inventory():
    def _create_inventory(**kwargs):
        kwargs["supplier"] = Supplier.objects.create(name="supplier A")

        return Inventory.objects.create(**kwargs)

    return _create_inventory
