from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import forms, models

# Create your views here.


class ItemCategoryDetail(DetailView):
    model = models.ItemCategory


class ItemCategoryList(ListView):
    model = models.ItemCategory

    def get_queryset(self):
        if self.request.GET.get("query"):
            query = self.request.GET.get("query")
            object_list = models.ItemCategory.objects.filter(name__icontains=query)
        else:
            object_list = models.ItemCategory.objects.all()
        return object_list


class ItemCategoryCreate(CreateView):
    model = models.ItemCategory
    form_class = forms.ItemCategoryForm
    success_url = reverse_lazy("item:index")


class ItemCategoryDelete(DeleteView):
    model = models.ItemCategory
    success_url = reverse_lazy("item:itemcategory_list")


class ItemCategoryUpdate(UpdateView):
    model = models.ItemCategory
    success_url = reverse_lazy("item:itemcategory_list")
    form_class = forms.ItemCategoryForm



class ItemCreate(CreateView):
    model = models.Item
    form_class = forms.ItemForm
    success_url = reverse_lazy("item:index")


class ItemList(ListView):
    model = models.Item

    def get_queryset(self):
        if self.request.GET.get("query"):
            query = self.request.GET.get("query")
            object_list = models.Item.objects.filter(nombre__icontains=query)
        else:
            object_list = models.Item.objects.all()
        return object_list


class ItemDetail(DetailView):
    model = models.Item


class ItemDelete(DeleteView):
    model = models.Item
    success_url = reverse_lazy("item:item_list")


class ItemUpdate(UpdateView):
    model = models.Item
    success_url = reverse_lazy("item:item_list")
    form_class = forms.ItemForm
