from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="sale/index.html"), name="index"),
    path("sale/list/", views.SaleList.as_view(), name="sale_list"),
    path("sale/detail/<int:pk>", views.SaleDetail.as_view(), name="sale_detail"),
    path("sale/create/", staff_member_required(views.SaleCreate.as_view()), name="sale_create"),
    path("sale/delete/<int:pk>", staff_member_required(views.SaleDelete.as_view()), name="sale_delete"),
    path("Sale/update/<int:pk>", staff_member_required(views.SaleUpdate.as_view()), name="sale_update"),
]
