from django.shortcuts import render
import json, os
# Create your views here.

JSON_PATH = 'mainapp/json'

def loadMenuFromJSON ():
    with open(os.path.join(JSON_PATH, 'menu.json'), 'r', encoding="utf-8") as readfile:
        return json.load(readfile)

def main(request):
    links_menu = loadMenuFromJSON()
    context = {'links_menu': links_menu, 'username': 'Vadim', 'array': [1, 2, 3], "title": "главная"}
    return render(request, 'mainapp/index.html', context)

def products(request):
    links_menu = loadMenuFromJSON()
    context = {'links_menu': links_menu, "title": "продукты"}
    return render(request, 'mainapp/products.html', context)

def contacts(request):
    links_menu = loadMenuFromJSON()
    context = {'links_menu': links_menu, "title": "контакты"}
    return render(request, 'mainapp/contacts.html', context)
