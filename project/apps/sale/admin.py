from django.contrib import admin

from . import models

admin.site.register(models.Seller)


@admin.register(models.Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = (
        "seller",
        "item",
        "quantity",
        "total_price",
        "date_sale",
    )
    list_display_links = ("item",)
    search_fields = ("item.name", "seller")
    list_filter = ("seller",)
    date_hierarchy = ("date_sale")
