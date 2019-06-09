from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'mainapp/index.html', {'username': 'Vasya', 'age': 25, 'array': list(range(3))})

def products(request):
    return render(request, 'mainapp/products.html')

def contacts(request):
    return render(request, 'mainapp/contacts.html')