from django.db import models
from django.utils import timezone


class ItemCategory(models.Model):
   

    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=250, null=True, blank=True, verbose_name="description")

    class Meta:
        verbose_name = "item category"
        verbose_name_plural = "item categories"

    def __str__(self):
        return self.name


class Item(models.Model):
    

    category = models.ForeignKey(ItemCategory, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="category")
    name = models.CharField(max_length=100)
    measurement = models.CharField(max_length=50)
    quantity = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=250, blank=True, null=True, verbose_name="description")
    updated_date = models.DateTimeField(default=timezone.now, editable=False, verbose_name="updated date")

    class Meta:
        verbose_name = "item"
        verbose_name_plural = "items"

    def __str__(self):
        return f"{self.name} ({self.measurement}) ${self.price:.2f}"
