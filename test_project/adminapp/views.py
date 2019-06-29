from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.views.generic.list import ListView
from mainapp.models import ProductCategory, Product

# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'adminapp/products.html'
    queryset = Product.objects.all()

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        if 'pk' in self.kwargs:
            if self.kwargs['pk']:
                queryset = queryset.filter(category=self.kwargs['pk'])
        return queryset

# тут переопределили стандаптный метод класса ListView, вписав в него новые ключевые слова.
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'Все продукты. Админка.'
        context['categories'] = ProductCategory.objects.all()
        return context
