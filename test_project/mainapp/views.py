from django.shortcuts import render, get_object_or_404
import json, os
from mainapp.models import Product, ProductCategory
from basketapp.models import Basket
import random

# Create your views here.

JSON_PATH = 'mainapp/json'


def loadMenuFromJSON ():
    with open(os.path.join(JSON_PATH, 'menu.json'), 'r', encoding="utf-8") as readfile:
        return json.load(readfile)


def main(request):
    links_menu = loadMenuFromJSON()
    context = {'links_menu': links_menu, 'username': 'Vadim', 'array': [1, 2, 3], "title": "главная"}
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    basket = []
    if request.user.is_authenticated:
        # adds to basket var objects inherent to user that is logged and requesting page
        basket = Basket.objects.filter(user=request.user)


    links_menu = loadMenuFromJSON()

    products = Product.objects.all()

    # import object product to connect it to the template

    if pk:
        if pk == '0':
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = products.filter(category__pk=pk)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    context = {'links_menu': links_menu,
               "title": "продукты",
               "products": products,
               'categories': ProductCategory.objects.all(),
               'basket': basket,
               'hot_product': hot_product,
               'same_products': same_products,
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
    product = Products.objects.all()

    return random.sample(list(products), 1)[0]

def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]

    return same_products