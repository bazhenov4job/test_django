from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from mainapp.models import Product
from basketapp.models import Basket
import json, os
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import JsonResponse


# Create your views here.

JSON_PATH = 'mainapp/json'


def loadMenuFromJSON ():
    with open(os.path.join(JSON_PATH, 'menu.json'), 'r', encoding="utf-8") as readfile:
        return json.load(readfile)


@login_required
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


@login_required
def basket_add(request, pk):

    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('mainapp:product', args=[pk]))

    product = get_object_or_404(Product, pk=pk)
    old_basket_slot = Basket.objects.filter(user=request.user, product=product).first()

    if old_basket_slot:
        old_basket_slot.quantity += 1
        old_basket_slot.save()
    else:
        new_basket_slot = Basket(user=request.user, product=product)
        new_basket_slot.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, pk):
    product = get_object_or_404(Product, pk=pk)
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


@login_required
def basket_edit(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        new_basket_item = Basket.objects.get(pk=int(pk))

        if quantity > 0:
            new_basket_item.quantity = quantity
            new_basket_item.save()
        else:
            new_basket_item.delete()

        basket_items = Basket.objects.filter(user=request.user).order_by('product__category')

        content = {
            'basket_items': basket_items,
        }

        result = render_to_string('basketapp/basket.html', content)

        return JsonResponse({'result': result})
