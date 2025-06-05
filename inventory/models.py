from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=255)
    note = models.TextField()
    stock = models.IntegerField(default=0)
    availability = models.BooleanField()
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Inventory"
        verbose_name_plural = "Inventory"
