from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import ShopUserLoginForm
from django.contrib import auth
from django.urls import reverse

# Create your views here.

def login(request):
    title = 'вход'

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main')) # Выбрасывает нас обратно на глагне

    """login_form = ShopUserLoginForm(data=request.POST)"""
    """if request.method == "POST" and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))"""

    """content = {'title': title, 'login_form': login_form}"""
    return render(request, 'authapp/login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))

def register (request):
    return HttpResponseRedirect(reverse('main'))

def edit (request):
    return HttpResponseRedirect(reverse('main'))
