from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from mainapp.models import Product
from basketapp.models import Basket
import json, os

# Create your views here.

JSON_PATH = 'mainapp/json'


def loadMenuFromJSON ():
    with open(os.path.join(JSON_PATH, 'menu.json'), 'r', encoding="utf-8") as readfile:
        return json.load(readfile)

def basket(request):
    links_menu = loadMenuFromJSON()
    basket = Basket.objects.all()
    products = []
    for good in basket:
        products.append(good.product)
    content = {"basket": basket,
               'products': products,
               "title": "корзина",
               'links_menu': links_menu}
    return render(request, 'basketapp/basket.html', content)


def basket_add(request, pk):
    print(pk)
    product = get_object_or_404(Product, pk=pk)
    old_basket_slot = Basket.objects.filter(user=request.user, product=product).first()

    if old_basket_slot:
        old_basket_slot.quantity += 1
        old_basket_slot.save()
    else:
        new_basket_slot = Basket(user=request.user, product=product)
        new_basket_slot.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk):
    product = get_object_or_404(Product, pk=pk)
    print(product.pk)
    basket_slot = Basket.objects.filter(user=request.user, product=product).first()

    if basket_slot:
        if basket_slot.quantity <= 1:
            basket_slot.delete()
        else:
            basket_slot.quantity -= 1
            basket_slot.save()
    else:
        pass

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

