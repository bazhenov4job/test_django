from django.shortcuts import render, get_object_or_404
import json, os
from mainapp.models import Product, ProductCategory

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

    links_menu = loadMenuFromJSON()

    products = Product.objects.all()

    # import object product to connect it to the template

    if pk:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = products.filter(category__pk=pk)

    context = {'links_menu': links_menu, "title": "продукты", "products": products, 'categories': ProductCategory.objects.all()}
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    links_menu = loadMenuFromJSON()
    context = {'links_menu': links_menu, "title": "контакты"}
    return render(request, 'mainapp/contacts.html', context)
