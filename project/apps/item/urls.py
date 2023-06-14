from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="item/index.html"), name="index"),
    path("itemcategory/detail/<int:pk>", views.ItemCategoryDetail.as_view(), name="itemcategory_detail"),
    path("itemcategory/list/", views.ItemCategoryList.as_view(), name="itemcategory_list"),
    path("itemcategory/create/", staff_member_required(views.ItemCategoryCreate.as_view()), name="itemcategory_create"),
    path("itemcategory/delete/<int:pk>", staff_member_required(views.ItemCategoryDelete.as_view()), name="itemcategory_delete"),
    path("itemcategory/update/<int:pk>", staff_member_required(views.ItemCategoryUpdate.as_view()), name="itemcategory_update"),
    path("item/detail/<int:pk>", views.ItemDetail.as_view(), name="item_detail"),
    path("item/list/", views.ItemList.as_view(), name="item_list"),
    path("item/create/", staff_member_required(views.ItemCreate.as_view()), name="item_create"),
    path("item/delete/<int:pk>", staff_member_required(views.ItemDelete.as_view()), name="item_delete"),
    path("item/update/<int:pk>", staff_member_required(views.ItemUpdate.as_view()), name="item_update"),
]
