import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kiratech_inventory.settings")
django.setup()

from inventory.models import (
    Inventory,
    Supplier,
)  # Adjust 'inventory_app' to your actual app name


def create_sample_inventory_items(num_items=10):
    """
    Creates a specified number of sample Inventory items.
    """
    sample_data = [
        {
            "name": "Laptop Pro X",
            "description": "High-performance laptop with 16GB RAM and 512GB SSD.",
            "note": "Popular model, frequently restocked.",
            "stock": 50,
            "supplier_name": "TechGadgets Inc.",
        },
        {
            "name": "Wireless Mouse M300",
            "description": "Ergonomic wireless mouse with long battery life.",
            "note": "Requires 1 AA battery, not included.",
            "stock": 200,
            "supplier_name": "Peripherals Co.",
        },
        {
            "name": "Mechanical Keyboard K900",
            "description": "Gaming mechanical keyboard with RGB backlight.",
            "note": "Cherry MX Red switches.",
            "stock": 30,
            "supplier_name": "GamingGear Ltd.",
        },
        {
            "name": "USB-C Hub 7-in-1",
            "description": "Multi-port adapter with HDMI, USB 3.0, SD card reader.",
            "note": "Compatible with MacBook Pro and Windows laptops.",
            "stock": 100,
            "supplier_name": "ConnectAll Solutions",
        },
        {
            "name": "External SSD 1TB",
            "description": "Portable solid-state drive for fast data transfer.",
            "note": "USB 3.1 Gen 2 compatible.",
            "stock": 75,
            "supplier_name": "StorageMax",
        },
        {
            "name": "Monitor 27-inch 4K",
            "description": "UHD IPS monitor with thin bezels.",
            "note": "Ideal for graphic design and video editing.",
            "stock": 20,
            "supplier_name": "DisplayTech",
        },
        {
            "name": "Webcam HD 1080p",
            "description": "Full HD webcam with built-in microphone.",
            "note": "Plug and play, no drivers needed.",
            "stock": 150,
            "supplier_name": "VideoCall Essentials",
        },
        {
            "name": "Noise-Cancelling Headphones",
            "description": "Over-ear headphones with active noise cancellation.",
            "note": "Up to 30 hours battery life.",
            "stock": 60,
            "supplier_name": "AudioWaves",
        },
        {
            "name": "Router Wi-Fi 6 AX1800",
            "description": "Dual-band Wi-Fi 6 router for high-speed internet.",
            "note": "Supports up to 1200 Mbps on 5GHz band.",
            "stock": 40,
            "supplier_name": "NetConnect",
        },
        {
            "name": "Smart Speaker with AI",
            "description": "Voice-controlled smart speaker with integrated AI assistant.",
            "note": "Available in charcoal and light grey.",
            "stock": 90,
            "supplier_name": "SmartHome Devices",
        },
    ]

    created_count = 0
    for i in range(min(num_items, len(sample_data))):
        item_data = sample_data[i]
        try:
            if Supplier.objects.filter(name=item_data["supplier_name"]).exists():
                supplier = Supplier.objects.get(name=item_data["supplier_name"])
            else:
                supplier = Supplier.objects.create(name=item_data["supplier_name"])

            inventory_item = Inventory.objects.create(
                name=item_data["name"],
                description=item_data["description"],
                note=item_data["note"],
                stock=item_data["stock"],
                availability=True,
                supplier=supplier,
            )
            print(f"Created: {inventory_item.name}")
            created_count += 1
        except Exception as e:
            print(f"Error creating item {item_data['name']}: {e}")

    print(f"\nSuccessfully created {created_count} sample inventory items.")


create_sample_inventory_items()
