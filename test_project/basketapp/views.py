from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from mainapp.models import Product
from basketapp.models import Basket

# Create your views here.


def basket(request):
    basket = Basket.objects.all()
    products = []
    for item in basket:
        products.append(item.product)
    content = {"basket": products,
               "title": "корзина"}
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
        if basket_slot.quantity == 1:
            basket_slot.delete()
        else:
            basket_slot.quantity -= 1
            basket_slot.save()
    else:
        pass

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

