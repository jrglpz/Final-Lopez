from typing import Any, Dict

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import forms, models


class SaleDetail(DetailView):
    model = models.Sale


class SaleList(ListView):
    model = models.Sale

    def get_queryset(self):
        if self.request.GET.get("query"):
            query = self.request.GET.get("query")
            object_list = models.Sale.objects.filter(name__icontains=query)
        else:
            object_list = models.Sale.objects.all()
        return object_list


class SaleCreate(CreateView):
    model = models.Sale
    form_class = forms.SaleForm
    success_url = reverse_lazy("sale:index")

    def form_valid(self, form):
        form.instance.seller = self.request.user.seller
        return super().form_valid(form)


class SaleDelete(DeleteView):
    model = models.Sale
    success_url = reverse_lazy("sale:sale_list")


class SaleUpdate(UpdateView):
    model = models.Sale
    success_url = reverse_lazy("sale:sale_list")
    form_class = forms.SaleForm
