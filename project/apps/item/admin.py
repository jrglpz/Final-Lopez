from django.contrib import admin

from . import models

admin.site.site_title = "Items"
admin.site.site_header = "Company Name"


@admin.register(models.ItemCategory)
class ItemCategoryAdmin(admin.ModelAdmin):

    list_display = ("name", "description")
    search_fields = ("name",)
    list_filter = ("name",)
    ordering = ("name",)


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "category",
        "name",
        "measurement",
        "quantity",
        "price",
        "description",
        "updated_date",
    )
    list_display_links = ("name",)
    search_fields = ("name",)
    ordering = (
        "category",
        "name",
    )
    list_filter = ("category",)
    date_hierarchy = "updated_date"
