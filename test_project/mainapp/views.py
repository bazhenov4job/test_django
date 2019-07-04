from django.shortcuts import render, get_object_or_404
import json, os
from mainapp.models import Product, ProductCategory
from basketapp.models import Basket
import random
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger

# Create your views here.

JSON_PATH = 'mainapp/json'


def loadMenuFromJSON ():
    with open(os.path.join(JSON_PATH, 'menu.json'), 'r', encoding="utf-8") as readfile:
        return json.load(readfile)


def main(request):
    links_menu = loadMenuFromJSON()
    context = {'links_menu': links_menu, 'username': 'Vadim', 'array': [1, 2, 3], "title": "главная"}
    return render(request, 'mainapp/index.html', context)


def product(request, pk):
    title = 'продукт'
    content = {
        'title': title,
        'links_menu': loadMenuFromJSON(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': Product.objects.all(),
        'categories': ProductCategory.objects.all()
    }

    return render(request, 'mainapp/product.html', content)


def products(request, pk=None, page=1):

    basket = []
    if request.user.is_authenticated:
        # adds to basket var objects inherent to user that is logged and requesting page
        basket = Basket.objects.filter(user=request.user)

    links_menu = loadMenuFromJSON()

    products = Product.objects.all()

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    category = ProductCategory.objects.all()

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {
                'pk': 0,
                'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = products.filter(category__pk=pk)

        paginator = Paginator(products, 2)

        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        context = {'links_menu': links_menu,
                   "title": "продукты",
                   "products": products_paginator,
                   'categories': ProductCategory.objects.all(),
                   'basket': basket,
                   'hot_product': hot_product,
                   'same_products': same_products,
                   'category': category,
                   }
        return render(request, 'mainapp/products.html', context)

    # Закинули лист продуктов, который выводится по 2 экземпляра на страницу

    context = {'links_menu': links_menu,
               "title": "продукты",
               "products": products,
               'categories': ProductCategory.objects.all(),
               'basket': basket,
               'hot_product': hot_product,
               'same_products': same_products,
               'category': category,
               }
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    links_menu = loadMenuFromJSON()
    context = {'links_menu': links_menu, "title": "контакты"}
    return render(request, 'mainapp/contacts.html', context)


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 2)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:2]

    return same_products